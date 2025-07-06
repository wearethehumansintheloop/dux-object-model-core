"""
DUX Object Extraction Processor

Handles the 15-minute LLM processing workflow for extracting DUX objects 
from uploaded transcripts. This module provides the core functionality for 
transforming raw research data into structured DUX objects.
"""

import json
import time
from datetime import datetime
from typing import Dict, List, Any
from pathlib import Path

import jsonschema
from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate
from pydantic import ValidationError

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
    
    def __init__(self, llm_name: str = "claudev2", 
                 ollama_base_url: str = "http://localhost:11434"):
        """Initialize the DUX object extractor with LLM configuration."""
        self.logger = BaseLogger()
        
        # Ensure ollama/ is stripped from the model name if present
        processed_llm_name = llm_name.split('/')[-1] if 'ollama/' in llm_name else llm_name

        self.llm = load_llm(
            processed_llm_name, 
            logger=self.logger, 
            config={"ollama_base_url": ollama_base_url}
        )
        
        # Load DUX schemas
        self.schemas = self._load_dux_schemas()
        
        # Initialize extraction prompts
        self.prompts = self._initialize_prompts()
        
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
    
    def process_transcript(self, transcript_path: str, 
                         source_filename: str) -> Dict[str, Any]:
        """
        Main processing function for extracting DUX objects from a transcript.
        
        Args:
            transcript_path: Path to the transcript file
            source_filename: Name of the source file for provenance tracking
            
        Returns:
            Dictionary containing extracted objects and processing metadata
        """
        start_time = time.time()
        self.logger.info(f"Starting DUX object extraction from: {transcript_path}")
        
        # Read transcript
        with open(transcript_path, 'r', encoding='utf-8') as f:
            transcript_content = f.read()
        
        # Extract objects
        extracted_objects = {}
        provenance_objects = []
        
        # Extract each object type
        for obj_type in ["problem", "behavior", "result", "useroutcome"]:
            try:
                objects = self._extract_objects(
                    obj_type, transcript_content, source_filename
                )
                extracted_objects[obj_type] = objects
                
                # Create provenance objects for extracted evidence
                for obj in objects:
                    if "evidence" in obj and obj["evidence"]:
                        provenance = self._create_provenance_object(
                            obj, transcript_content, source_filename
                        )
                        provenance_objects.append(provenance)
                        
            except Exception as e:
                self.logger.error(f"Error extracting {obj_type} objects: {e}")
                extracted_objects[obj_type] = []
        
        # Add provenance objects
        extracted_objects["provenance"] = provenance_objects
        
        # Calculate processing time
        processing_time = time.time() - start_time
        
        # Create processing summary
        summary = {
            "source_filename": source_filename,
            "processing_time_seconds": processing_time,
            "objects_extracted": {
                obj_type: len(objects)
                for obj_type, objects in extracted_objects.items()
            },
            "total_objects": sum(
                len(objects) for objects in extracted_objects.values()
            ),
            "timestamp": datetime.now().isoformat()
        }
        
        self.logger.info(
            f"Extraction completed in {processing_time:.2f} seconds"
        )
        self.logger.info(f"Objects extracted: {summary['objects_extracted']}")
        
        return {
            "summary": summary,
            "objects": extracted_objects
        }
    
    def _extract_objects(self, obj_type: str, transcript: str, 
                        source_filename: str) -> List[Dict]:
        """Extract objects of a specific type from the transcript."""
        if obj_type not in self.prompts:
            raise ValueError(f"Unknown object type: {obj_type}")
        
        # Prepare prompt with schema
        schema_json = json.dumps(self.schemas.get(obj_type, {}), indent=2)
        
        prompt = self.prompts[obj_type].format(
            transcript=transcript,
            **{f"{obj_type}_schema": schema_json}
        )
        
        # Generate extraction
        response = self.llm.invoke(prompt)
        
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
                if self._validate_object(obj, obj_type):
                    # Add required fields
                    obj["created_at"] = datetime.now().isoformat()
                    obj["updated_at"] = datetime.now().isoformat()
                    
                    # Generate evidence array if not present
                    if "evidence" not in obj:
                        obj["evidence"] = []
                    
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
        """Extract a relevant quote from the transcript for the given object."""
        # This is a simplified implementation
        # In practice, you'd use more sophisticated NLP to find the most relevant quote
        
        # For now, return a placeholder
        return (
            f"Evidence supporting {obj.get('object_type', 'object')} "
            f"{obj.get('id', 'unknown')}"
        )
    
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
    parser.add_argument("--llm", default="claudev2", help="LLM model to use")
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
    results = extractor.process_transcript(args.transcript_path, source_filename)
    
    # Save results
    output_path = extractor.save_extraction_results(results, args.output_dir)
    
    print(f"Extraction completed! Results saved to: {output_path}")
    print(f"Objects extracted: {results['summary']['objects_extracted']}")


if __name__ == "__main__":
    main()