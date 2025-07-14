"""
DUX Object Extraction Processor

Handles the 15-minute LLM processing workflow for extracting DUX objects 
from uploaded transcripts. This module provides the core functionality for 
transforming raw research data into structured DUX objects.
"""

from datetime import datetime
from typing import Dict, List, Any
from pathlib import Path
import json
import time
import re
import numpy as np
import jsonschema
from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate
from pydantic import ValidationError
from langchain_community.embeddings import OllamaEmbeddings

from core.chains import load_llm
from core.utils import BaseLogger
from utils.id_generator import generate_unique_id


class DUXObjectExtractor:
    """
    Main processor for extracting DUX objects from research transcripts.
    
    Handles the complete workflow:
    1. Transcript upload and preprocessing
    2. LLM-based object extraction
    3. Schema validation
    4. Provenance creation
    5. Object relationship mapping
    """
    
    def __init__(self, llm_name: str = "llama3", 
                 ollama_base_url: str = "http://localhost:11434",
                 embedding_model_name: str = "llama3",
                 hitl_output_dir: str = "test_output/hitl_review",
                 validation_mode: str = 'simple'):
        """Initialize the DUX object extractor with LLM and embedding model configuration."""
        self.logger = BaseLogger()
        self.hitl_output_dir = Path(hitl_output_dir)
        self.hitl_output_dir.mkdir(parents=True, exist_ok=True)
        self.validation_mode = validation_mode
        
        # Ensure ollama/ is stripped from the model name if present
        processed_llm_name = llm_name.split('/')[-1] if 'ollama/' in llm_name else llm_name

        self.llm = load_llm(
            processed_llm_name, 
            logger=self.logger, 
            config={"ollama_base_url": ollama_base_url}
        )
        
        # Initialize the Ollama embedding model
        self.embedding_model = OllamaEmbeddings(
            model=embedding_model_name,
            base_url=ollama_base_url
        )
        self.logger.info(f"Embedding model '{embedding_model_name}' loaded via Ollama.")
        
        # Initialize extraction prompts
        self.prompts = self._initialize_prompts()
        
        # Load DUX schemas
        self.schemas = self._load_dux_schemas()
    
    def _load_dux_schemas(self) -> Dict[str, Dict]:
        """Load all DUX object schemas for validation."""
        # This script is in DUX Research Platform, schemas are in DUX Object Model (Core)
        # Build a robust path from this file's location.
        current_dir = Path(__file__).resolve().parent
        # Go up from src/app/orchestrators to dux-research-platform/
        project_root = current_dir.parent.parent.parent
        # Navigate to the sibling project's schema folder
        schema_dir = (
            project_root.parent / 'dux-object-model-core' / 'src' /
            'dux_v9.6_split_schema'
        )

        schemas = {}
        
        schema_files = {
            "problem": "dux_object_problem.json",
            "behavior": "dux_object_behavior.json",
            "result": "dux_object_result.json",
            "user_outcome": "dux_object_useroutcome.json",
            "flow": "dux_object_flow.json",
            "provenance": "dux_object_provenance.json"
        }
        
        for obj_type, filename in schema_files.items():
            schema_path = schema_dir / filename
            if schema_path.exists():
                with open(schema_path, 'r') as f:
                    schemas[obj_type] = json.load(f)
            else:
                self.logger.warning(f"Schema file not found: {schema_path}")
                
        return schemas
    
    def _initialize_prompts(self) -> Dict[str, ChatPromptTemplate]:
        """Initialize extraction prompts for each DUX object type."""
        prompts = {}
        
        # System prompt template for all extractions
        system_template = """You are a DUX (Design User Experience) research analyst 
specializing in extracting structured insights from user research transcripts.

Your task is to identify and extract DUX objects from research data. Each 
object must be:
- Schema compliant (follow the exact JSON structure provided)
- Evidence-backed (supported by specific quotes or data points)
- Atomic (single, clear purpose)
- Traceable (clear relationships to other objects)

{fit_template_section}

After extracting each object, you MUST evaluate its 'fit' against the provided 'Fit Template Context'.
- Add a "fit_score" field (float, 0.0 to 1.0) representing how well the object aligns with the template's goals.
- Add a "fit_reasoning" field (string) with a brief explanation for your score.

IMPORTANT: Always return valid JSON that matches the provided schema exactly. 
Do not include any explanatory text outside the JSON structure."""

        # Problem extraction prompt
        problem_template = """Extract Problem objects from the research transcript.

PROBLEM OBJECT SCHEMA:
{problem_schema}

A Problem represents a strategic job-to-be-done that defines market-level 
opportunities. Focus on:
- User motivations and desired outcomes
- Situations where users struggle
- What's at stake if the problem isn't solved

FIT TEMPLATE CONTEXT:
{fit_template}

TRANSCRIPT:
{transcript}

Extract all Problem objects you can identify. Return as a JSON array of Problem objects."""

        # Behavior extraction prompt  
        behavior_template = """Extract Behavior objects from the research transcript.

BEHAVIOR OBJECT SCHEMA:
{behavior_schema}

A Behavior represents an atomic, testable user action that serves as an 
instrumentation anchor. Focus on:
- Specific actions users take or want to take
- Measurable signals that prove the behavior occurred
- User enablement statements

FIT TEMPLATE CONTEXT:
{fit_template}

TRANSCRIPT:
{transcript}

Extract all Behavior objects you can identify. Return as a JSON array of Behavior objects."""

        # Result extraction prompt
        result_template = """Extract Result objects from the research transcript.

RESULT OBJECT SCHEMA:
{result_schema}

A Result represents a measurable outcome that users achieve. Focus on:
- Quantifiable outcomes and metrics
- Success indicators
- Business value delivered

FIT TEMPLATE CONTEXT:
{fit_template}

TRANSCRIPT:
{transcript}

Extract all Result objects you can identify. Return as a JSON array of Result objects."""

        # User Outcome extraction prompt
        useroutcome_template = """Extract User Outcome objects from the research transcript.

USER OUTCOME OBJECT SCHEMA:
{useroutcome_schema}

A User Outcome represents the human impact and value delivered to users. 
Focus on:
- Personal benefits and improvements
- Quality of life enhancements
- Emotional and practical outcomes

FIT TEMPLATE CONTEXT:
{fit_template}

TRANSCRIPT:
{transcript}

Extract all User Outcome objects you can identify. Return as a JSON array of 
User Outcome objects."""

        # Create prompt templates
        prompts["problem"] = ChatPromptTemplate.from_messages([
            SystemMessagePromptTemplate.from_template(
                system_template + "\n\n" + problem_template
            )
        ])
        
        prompts["behavior"] = ChatPromptTemplate.from_messages([
            SystemMessagePromptTemplate.from_template(
                system_template + "\n\n" + behavior_template
            )
        ])
        
        prompts["result"] = ChatPromptTemplate.from_messages([
            SystemMessagePromptTemplate.from_template(
                system_template + "\n\n" + result_template
            )
        ])
        
        prompts["useroutcome"] = ChatPromptTemplate.from_messages([
            SystemMessagePromptTemplate.from_template(
                system_template + "\n\n" + useroutcome_template
            )
        ])
        
        return prompts
    
    def _get_object_text_representation(self, obj: Dict) -> str:
        """Get a single string representation of an object for embedding."""
        # Combine key text fields to create a representative string for matching
        obj_type = obj.get("object_type", "").lower()
        text_parts = []

        if obj_type == "problem":
            text_parts.append(obj.get("job_statement", ""))
            text_parts.append(obj.get("problem_statement", ""))
        elif obj_type == "behavior":
            text_parts.append(obj.get("user_enablement", ""))
        elif obj_type == "result":
            text_parts.append(obj.get("target_impact", ""))
        elif obj_type == "useroutcome":
            text_parts.append(obj.get("user_outcome_statement", ""))
        
        # Generic fallback
        if not any(text_parts):
            text_parts.append(obj.get("title", ""))
            text_parts.append(obj.get("description", ""))

        return " ".join(filter(None, text_parts)).strip()

    def _calculate_fit_score(self, obj: Dict, fit_template_embedding: np.ndarray) -> float:
        """Calculate the fit score based on embedding similarity."""
        if fit_template_embedding is None:
            return 0.0  # No template to compare against

        obj_text = self._get_object_text_representation(obj)
        if not obj_text:
            return 0.0

        try:
            obj_embedding = self.embedding_model.embed_query(obj_text)
            # Cosine similarity is the dot product of normalized vectors
            # OllamaEmbeddings should return normalized vectors
            similarity = np.dot(obj_embedding, fit_template_embedding)
            return float(similarity)
        except Exception as e:
            self.logger.error(f"Error calculating fit score for object {obj.get('id')}: {e}")
            return 0.0

    def process_transcript(self, transcript_path: str, 
                         source_filename: str,
                         fit_template_path: str = None,
                         fit_score_threshold: float = 0.7) -> Dict[str, Any]:
        """
        Main processing function for extracting DUX objects from a transcript.
        
        Args:
            transcript_path: Path to the transcript file
            source_filename: Name of the source file for provenance tracking
            fit_template_path: Optional path to a fit template markdown file.
            fit_score_threshold: The minimum fit score for an object to be accepted.
            
        Returns:
            Dictionary containing extracted objects and processing metadata
        """
        start_time = time.time()
        self.logger.info(f"Starting DUX object extraction from: {transcript_path}")
        
        # Read transcript
        with open(transcript_path, 'r', encoding='utf-8') as f:
            transcript_content = f.read()

        # Read fit template and generate its embedding
        fit_template_content = ""
        fit_template_embedding = None
        if fit_template_path:
            self.logger.info(f"Processing fit template: {fit_template_path}")
            try:
                with open(fit_template_path, 'r', encoding='utf-8') as f:
                    fit_template_content = f.read()
                self.logger.info(f"Successfully loaded fit template: {fit_template_path}")
                if fit_template_content.strip():
                    self.logger.info("Generating embedding for fit template...")
                    fit_template_embedding = self.embedding_model.embed_query(fit_template_content)
                    self.logger.info("Successfully generated embedding for fit template.")
            except FileNotFoundError:
                self.logger.warning(f"Fit template file not found: {fit_template_path}. Proceeding without it.")
        
        # Extract objects and create provenance
        extracted_objects = {}
        all_provenance_objects = []
        
        # Extract each object type
        for obj_type in ["problem", "behavior", "result", "useroutcome"]:
            self.logger.info(f"--- Starting extraction for object type: {obj_type} ---")
            try:
                objects = self._extract_objects(
                    obj_type, transcript_content, source_filename, fit_template_content, fit_template_embedding
                )
                self.logger.info(f"--- Completed extraction for object type: {obj_type}, found {len(objects)} objects ---")
                
                # Create provenance for each extracted object and link it
                self.logger.info(f"Creating provenance for {len(objects)} {obj_type} objects...")
                for i, obj in enumerate(objects):
                    self.logger.debug(f"Processing object {i+1}/{len(objects)} for provenance.")
                    # --- Judge Validation Step ---
                    if self.validation_mode == 'judge':
                        validation_result = self._validate_with_judge_llm(obj, transcript_content)
                        obj['validation_status'] = validation_result
                        # If judge rejects, send to HITL and skip further processing
                        if not validation_result.get('validation_passed', False):
                            # Use a dedicated list for judge-rejected items
                            if 'judge_rejected' not in hitl_review_objects:
                                hitl_review_objects['judge_rejected'] = []
                            hitl_review_objects['judge_rejected'].append(obj)
                            continue  # Skip to the next object

                    provenance = self._create_provenance_object(
                        obj, transcript_content, source_filename
                    )
                    all_provenance_objects.append(provenance)
                    # Link the provenance object back to the source object
                    obj["evidence"] = [provenance["id"]]

                extracted_objects[obj_type] = objects
                self.logger.info(f"Finished creating provenance for {obj_type} objects.")
                        
            except Exception as e:
                self.logger.error(f"Error extracting {obj_type} objects: {e}")
                extracted_objects[obj_type] = []
        
        # Add all created provenance objects to the final dictionary
        extracted_objects["provenance"] = all_provenance_objects
        
        # --- HITL and False Positive Logging ---
        hitl_review_objects = {}
        final_extracted_objects = {"provenance": all_provenance_objects}

        for obj_type, objects in extracted_objects.items():
            if obj_type == "provenance":
                continue
            
            passing_objects = []
            review_objects = []
            for obj in objects:
                if obj.get('fit_score', 0.0) < fit_score_threshold:
                    review_objects.append(obj)
                else:
                    passing_objects.append(obj)
            
            final_extracted_objects[obj_type] = passing_objects
            if review_objects:
                hitl_review_objects[obj_type] = review_objects

        # Save objects for HITL review
        if hitl_review_objects:
            self.save_hitl_review_files(hitl_review_objects, source_filename)
        
        # --- Success Criteria Evaluation ---
        total_objects = sum(len(objects) for obj_type, objects in final_extracted_objects.items() if obj_type != 'provenance')
        success_criteria = {}
        
        OVER_EXTRACTION_THRESHOLD = 150
        LOW_YIELD_THRESHOLD = 25

        if total_objects > OVER_EXTRACTION_THRESHOLD:
            success_criteria = {
                "status": "FLAG_OVER_EXTRACTION",
                "message": f"High object count ({total_objects}) suggests over-extraction. Ideal range is {LOW_YIELD_THRESHOLD}-{OVER_EXTRACTION_THRESHOLD}."
            }
        elif total_objects < LOW_YIELD_THRESHOLD:
            # Sum of fit scores for all extracted objects as a quality proxy
            all_objects = [
                obj for obj_type, obj_list in final_extracted_objects.items() 
                if obj_type != 'provenance' for obj in obj_list
            ]
            quality_score_sum = sum(obj.get('fit_score', 0.0) for obj in all_objects)
            success_criteria = {
                "status": "FLAG_LOW_YIELD",
                "message": f"Low object count ({total_objects}). May be insufficient for robust insight generation. Ideal range is {LOW_YIELD_THRESHOLD}-{OVER_EXTRACTION_THRESHOLD}.",
                "quality_score_sum": round(quality_score_sum, 2)
            }
        else:
             success_criteria = {
                "status": "NOMINAL",
                "message": f"Object count ({total_objects}) is within the nominal range ({LOW_YIELD_THRESHOLD}-{OVER_EXTRACTION_THRESHOLD})."
            }

        # Calculate processing time
        processing_time = time.time() - start_time

        # --- Calculate evidence density for logging --- 
        word_count = len(transcript_content.split())
        # Assuming an average speaking rate of 150 words per minute for estimation
        # 1 hour = 60 minutes * 150 words/min = 9000 words
        estimated_hours = word_count / 9000 if word_count > 0 else 0
        
        num_provenance = len(all_provenance_objects)
        evidence_per_hour = (num_provenance / estimated_hours) if estimated_hours > 0 else 0

        evidence_density_log = {
            "estimated_transcript_hours": round(estimated_hours, 2),
            "total_evidence_count": num_provenance,
            "evidence_per_hour": round(evidence_per_hour, 2),
            "target_evidence_per_hour": "10-12",
            "message": f"Extracted {num_provenance} evidence items from an estimated {round(estimated_hours, 2)} hour transcript.",
            "note": "This is a benchmark to help with prompt tuning and RAG/embedding refinement."
        }
        self.logger.info(f"Evidence Density: {evidence_density_log['message']}")
        
        # Create processing summary
        summary = {
            "source_filename": source_filename,
            "processing_time_seconds": processing_time,
            "evidence_density": evidence_density_log,
            "objects_extracted": {
                obj_type: len(objects)
                for obj_type, objects in final_extracted_objects.items()
            },
            "total_objects": sum(
                len(objects) for objects in final_extracted_objects.values()
            ),
            "hitl_review_summary": {
                obj_type: len(objects)
                for obj_type, objects in hitl_review_objects.items()
            },
            "total_hitl_review_objects": sum(
                len(objects) for objects in hitl_review_objects.values()
            ),
            "success_criteria": success_criteria,
            "timestamp": datetime.now().isoformat()
        }

        # Add the "Count Study" for HITL review
        summary["count_study"] = {
            "problems": len(final_extracted_objects.get("problem", [])),
            "behaviors": len(final_extracted_objects.get("behavior", [])),
            "results": len(final_extracted_objects.get("result", [])),
            "user_outcomes": len(final_extracted_objects.get("useroutcome", [])),
            "total_insight_candidates": (
                len(final_extracted_objects.get("problem", [])) +
                len(final_extracted_objects.get("behavior", [])) +
                len(final_extracted_objects.get("result", []))
            )
        }
        
        self.logger.info(
            f"Extraction completed in {processing_time:.2f} seconds"
        )
        self.logger.info(f"Objects extracted: {summary['objects_extracted']}")
        self.logger.info(f"Objects for HITL review: {summary['hitl_review_summary']}")
        
        return {
            "summary": summary,
            "objects": final_extracted_objects
        }
    
    def _extract_objects(self, obj_type: str, transcript: str, 
                        source_filename: str, fit_template: str, fit_template_embedding: np.ndarray) -> List[Dict]:
        """Extract objects of a specific type from the transcript."""
        if obj_type not in self.prompts:
            raise ValueError(f"Unknown object type: {obj_type}")
        
        # Prepare prompt with schema
        schema_json = json.dumps(self.schemas.get(obj_type, {}), indent=2)
        
        prompt = self.prompts[obj_type].format(
            transcript=transcript,
            fit_template=fit_template or "No specific fit template provided. Focus on general DUX principles.",
            **{f"{obj_type}_schema": schema_json}
        )
        
        self.logger.info(f"Invoking LLM for {obj_type} extraction...")
        # Generate extraction
        response = self.llm.invoke(prompt)
        self.logger.info(f"LLM invocation complete for {obj_type}.")
        
        try:
            # Parse JSON response - handle different response formats
            if hasattr(response, 'content'):
                response_content = response.content
            else:
                response_content = str(response)
                
            extracted_data = json.loads(response_content)
            
            # Ensure it's a list
            if isinstance(extracted_data, dict):
                extracted_data = [extracted_data]
            
            # Validate each object against schema
            validated_objects = []
            for obj in extracted_data:
                # Add object_type for filtering and identification
                # Capitalize to match schema enum if necessary, e.g., "Problem"
                obj["object_type"] = obj_type.capitalize()

                if self._validate_object(obj, obj_type):
                    # Add required fields
                    obj["created_at"] = datetime.now().isoformat()
                    obj["updated_at"] = datetime.now().isoformat()
                    
                    # Generate evidence array if not present
                    if "evidence" not in obj:
                        obj["evidence"] = []
                    
                    # Calculate fit score programmatically
                    obj["fit_score"] = self._calculate_fit_score(obj, fit_template_embedding)
                    
                    # Ensure fit_reasoning is present (from LLM)
                    if "fit_reasoning" not in obj:
                        obj["fit_reasoning"] = "No reasoning provided by LLM."

                    validated_objects.append(obj)
                else:
                    self.logger.warning(
                        f"Invalid {obj_type} object: {obj.get('id', 'unknown')}"
                    )
            
            return validated_objects
            
        except json.JSONDecodeError as e:
            self.logger.error(f"Failed to parse JSON response for {obj_type}: {e}")
            return []
        except Exception as e:
            self.logger.error(f"Error extracting {obj_type} objects: {e}")
            return []
    
    def _validate_object(self, obj: Dict, obj_type: str) -> bool:
        """Validate an object against its schema."""
        if obj_type not in self.schemas:
            return True  # Skip validation if schema not available
        
        try:
            jsonschema.validate(instance=obj, schema=self.schemas[obj_type])
            return True
        except (ValidationError, jsonschema.ValidationError) as e:
            self.logger.warning(f"Schema validation failed for {obj_type}: {e}")
            return False
    
    def _create_provenance_object(self, obj: Dict, transcript: str, 
                                source_filename: str) -> Dict:
        """Create a provenance object for an extracted DUX object."""
        relevant_quote = self._extract_relevant_quote(obj, transcript)
        
        provenance_id = generate_unique_id(
            "Provenance", 
            f"{obj['id']}_{source_filename}_{relevant_quote}"
        )

        return {
            "object_type": "Provenance",
            "id": provenance_id,
            "source_filename": source_filename,
            "original_object_id": obj['id'],
            "evidence_quote": relevant_quote,
            "created_at": datetime.now().isoformat()
        }
    
    def _extract_relevant_quote(self, obj: Dict, transcript: str) -> str:
        """Extract a relevant quote from the transcript for the given object using sentence embeddings."""
        
        # 1. Get a text representation of the DUX object
        obj_text = self._get_object_text_representation(obj)
        if not obj_text.strip():
            self.logger.warning(f"Object {obj.get('id')} has no text representation to match.")
            return "No representative text found for object."

        # 2. Split transcript into sentences (simple regex split)
        sentences = re.split(r'(?<=[.!?]) +', transcript)
        sentences = [s.strip() for s in sentences if s.strip()]
        if not sentences:
            self.logger.warning("Transcript could not be split into sentences.")
            return "Transcript is empty or could not be processed."

        # 3. Generate embeddings
        try:
            self.logger.debug(f"Generating embedding for object: {obj.get('id')}")
            obj_embedding = self.embedding_model.embed_query(obj_text)
            self.logger.debug(f"Generating embeddings for {len(sentences)} transcript sentences...")
            sentence_embeddings = self.embedding_model.embed_documents(sentences)
            self.logger.debug("Embeddings generated successfully.")
            
            # 4. Calculate cosine similarity
            # OllamaEmbeddings returns normalized vectors, so dot product is cosine similarity
            similarities = np.dot(sentence_embeddings, obj_embedding)
            
            # 5. Find the most similar sentence
            most_similar_index = np.argmax(similarities)
            relevant_quote = sentences[most_similar_index]
            
            self.logger.info(f"Found relevant quote for object {obj.get('id')} with similarity {similarities[most_similar_index]:.4f}")
            return relevant_quote

        except Exception as e:
            self.logger.error(f"Failed to extract relevant quote using embeddings: {e}")
            # Fallback if embedding fails
            return (
                f"Evidence supporting {obj.get('object_type', 'object')} "
                f"{obj.get('id', 'unknown')}"
            )

    def save_hitl_review_files(self, hitl_objects: Dict[str, List[Dict]], source_filename: str):
        """Save objects that need human review to separate files."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        for obj_type, objects in hitl_objects.items():
            if objects:
                # Sanitize the source filename to be used in the output filename
                sanitized_source_name = re.sub(r'[^a-zA-Z0-9_\.-]', '_', Path(source_filename).stem)
                
                hitl_filename = f"hitl_{obj_type}_{sanitized_source_name}_{timestamp}.json"
                output_path = self.hitl_output_dir / hitl_filename
                
                with open(output_path, 'w') as f:
                    json.dump(objects, f, indent=2)
                
                self.logger.info(f"Saved {len(objects)} {obj_type} objects for HITL review to: {output_path}")

    def save_extraction_results(self, results: Dict[str, Any], 
                              output_dir: str) -> str:
        """Save extraction results to files."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_path = Path(output_dir) / f"dux_extraction_{timestamp}"
        output_path.mkdir(parents=True, exist_ok=True)
        
        # Save summary
        with open(output_path / "extraction_summary.json", 'w') as f:
            json.dump(results["summary"], f, indent=2)
        
        # Save objects by type
        for obj_type, objects in results["objects"].items():
            if objects:
                with open(output_path / f"{obj_type}_objects.json", 'w') as f:
                    json.dump(objects, f, indent=2)
        
        # Save complete results
        with open(output_path / "complete_extraction.json", 'w') as f:
            json.dump(results, f, indent=2)
        
        self.logger.info(f"Extraction results saved to: {output_path}")
        return str(output_path)

    def _validate_with_judge_llm(self, obj: Dict, transcript: str) -> Dict:
        """Use a 'judge' LLM to validate a generated object against the transcript."""
        self.logger.info(f"Performing 'judge' validation for object {obj.get('id')}")

        judge_system_prompt = """You are a meticulous quality assurance auditor. 
Your task is to validate a DUX object against the original transcript it was supposedly extracted from.
You must determine if the object is a faithful and accurate representation of the evidence in the transcript.
Do not be lenient. Your job is to catch inaccuracies, hallucinations, or misinterpretations.
Respond with a single JSON object with two keys:
- "validation_passed": boolean (true if the object is valid, false otherwise)
- "validation_reasoning": string (a brief, clear explanation for your decision)"""

        judge_user_prompt = f"""**TRANSCRIPT (EVIDENCE):**
---
{transcript}
---

**DUX OBJECT (TO VALIDATE):**
---
{json.dumps(obj, indent=2)}
---

Based on the evidence, is this DUX object valid? Respond with JSON."""

        prompt = f"""{judge_system_prompt}

{judge_user_prompt}"""

        try:
            response = self.llm.invoke(prompt)
            response_content = response.content if hasattr(response, 'content') else str(response)
            
            # Clean the response to ensure it's valid JSON
            # The model might sometimes include markdown backticks
            cleaned_response = re.sub(r'```json\n|\n```', '', response_content).strip()

            validation_data = json.loads(cleaned_response)
            
            # Add metadata to the validation status
            validation_data['source'] = 'judge_llm_review'
            validation_data['model'] = self.llm.model_name if hasattr(self.llm, 'model_name') else 'unknown'
            validation_data['timestamp'] = datetime.now().isoformat()

            if validation_data.get('validation_passed'):
                self.logger.info(f"Object {obj.get('id')} PASSED judge validation.")
            else:
                self.logger.warning(f"Object {obj.get('id')} FAILED judge validation. Reason: {validation_data.get('validation_reasoning')}")

            return validation_data

        except json.JSONDecodeError as e:
            self.logger.error(f"Failed to parse judge validation response for object {obj.get('id')}: {e}")
            return {
                "validation_passed": False,
                "validation_reasoning": "Failed to parse judge LLM response.",
                "source": "judge_llm_review",
                "error": str(e)
            }
        except Exception as e:
            self.logger.error(f"Error during judge validation for object {obj.get('id')}: {e}")
            return {
                "validation_passed": False,
                "validation_reasoning": "An unexpected error occurred during validation.",
                "source": "judge_llm_review",
                "error": str(e)
            }


def main():
    """Example usage of the DUX Object Extractor."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Extract DUX objects from research transcripts"
    )
    parser.add_argument("transcript_path", help="Path to the transcript file")
    parser.add_argument(
        "--output-dir", 
        default="./extraction_results", 
        help="Output directory for results"
    )
    parser.add_argument(
        "--fit-template",
        default=None,
        help="Path to the fit template markdown file."
    )
    parser.add_argument("--llm", default="llama3", help="LLM model to use")
    parser.add_argument(
        "--ollama-url", 
        default="http://localhost:11434", 
        help="Ollama base URL"
    )
    
    args = parser.parse_args()
    
    # Initialize extractor
    extractor = DUXObjectExtractor(
        llm_name=args.llm,
        ollama_base_url=args.ollama_url
    )
    
    # Process transcript
    source_filename = Path(args.transcript_path).name
    results = extractor.process_transcript(
        args.transcript_path, 
        source_filename,
        fit_template_path=args.fit_template
    )
    
    # Save results
    output_path = extractor.save_extraction_results(results, args.output_dir)
    
    print(f"Extraction completed! Results saved to: {output_path}")
    print(f"Objects extracted: {results['summary']['objects_extracted']}")


if __name__ == "__main__":
    main()