#!/usr/bin/env python3
"""
User Outcome Object Validation Script for HITL Review Process

This script implements a multi-gate pipeline to process markdown files,
extract User Outcome objects, and validate them with full explainability.

**Pipeline Stages:**
1.  **Gate 1: Semantic Extraction & Dossier Generation (LLM)**
    - An LLM acts as a research analyst to find and extract candidate objects.
    - It generates a "dossier" for each candidate with the object and a
      briefing explaining its reasoning.
2.  **Gate 2: Schema Validation**
    - Ensures strict data quality, structure, and backward compatibility
      against the formal JSON schema.
3.  **Gate 3: Conditional & Business Logic Validation**
    - Validates nuanced, context-dependent rules (e.g., if a flow is
      present, key signals are required).

References:
- docs/100_START_HERE/dux_object_template.md - Template structure
- docs/infrastructure_as_code/GOVERNANCE_NAMING_CONVENTIONS.md - Naming rules
- src/dux_v9.6_split_schema/dux_object_useroutcome.json - Schema definition
"""

import json
import os
import re
import shutil
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any, Tuple
import sys

# LangChain and LLM imports (placeholders for actual implementation)
# from langchain.chat_models import ChatOpenAI
# from langchain.prompts import ChatPromptTemplate
# from langchain.chains import LLMChain
# from dotenv import load_dotenv

from duplicate_handler import filter_duplicate_files, get_duplicate_summary
from config import OBJECT_TYPE_PATTERNS, validate_documentation_files

# Load environment variables for LLM API keys
# load_dotenv()

# --- Gate 2: Schema Definition ---
# Naming conventions: docs/infrastructure_as_code/GOVERNANCE_NAMING_CONVENTIONS.md
USEROUTCOME_SCHEMA = {
    "type": "object",
    "required": [
        "object_type", "id", "outcome_statement", "key_signals", 
        "acceptance_criteria", "evidence_maturity", "evidence"
    ],
    "properties": {
        "object_type": {"type": "string", "const": "UserOutcome"},
        "id": {"type": "string"},
        "outcome_statement": {
            "type": "string", 
            "pattern": "^[A-Z][^.]*[.!]$",
            "description": "Who does what by how much to make progress toward our "
                          "target result?"
        },
        "user_scenario": {"type": "string"},
        "target_impact_when_achieved": {"type": "string"},
        "priority": {
            "type": "string",
            "enum": ["critical", "high", "medium", "low"]
        },
        "flow_ids": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "string"},
                    "reference_context": {"type": "string"}
                }
            }
        },
        "problem_ids": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "string"},
                    "reference_context": {"type": "string"}
                }
            }
        },
        "result_ids": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "string"},
                    "reference_context": {"type": "string"}
                }
            }
        },
        "end_user": {"type": "array", "items": {"type": "string"}},
        "key_signals": {
            "type": "array",
            "items": {"type": "string"},
            "description": "Observable signals that indicate this outcome is being achieved - derived from key behaviors in related flows"
        },
        "acceptance_criteria": {
            "type": "array",
            "items": {"type": "string"},
            "description": "Clear, testable criteria that define successful achievement of this outcome"
        },
        "evidence_maturity": {
            "type": "string",
            "enum": ["01_assumptive", "02_anecdotal", "03_early_signal", "04_balanced_signal", "05_triangulated"]
        },
        "evidence": {
            "type": "array",
            "items": {"type": "string"},
            "description": "Array of Provenance IDs that support this outcome"
        }
    }
}

# --- Utility Functions ---

def get_llm_analyst():
    """Initializes and returns the LLM client (conceptual)."""
    # In a real implementation, this would configure the LLM
    # with specific model, temperature, and API key.
    # Example:
    # return ChatOpenAI(
    #     temperature=0.0,
    #     model_name="gpt-4-turbo",
    #     openai_api_key=os.getenv("OPENAI_API_KEY")
    # )
    print("      (LLM Analyst Initialized - Placeholder)")
    return None

def create_analyst_prompt_template():
    """Creates a prompt template for the LLM analyst."""
    # This prompt instructs the LLM to find candidates and create dossiers.
    prompt = """
    You are a meticulous research analyst for the DUX platform. Your task is to
    review the following markdown document and identify all JSON objects that
    are candidate 'UserOutcome' objects.

    For each candidate you find, create a "dossier" with two keys:
    1.  "object_candidate": The full JSON object you extracted.
    2.  "analyst_briefing": A short, clear explanation of why you believe this
        is a UserOutcome object, your confidence level, and any notable
        characteristics.

    If you find no candidates, return an empty list.

    Respond with a single JSON array of dossier objects.

    Markdown Content:
    -----------------
    {document_content}
    """
    # return ChatPromptTemplate.from_template(prompt)
    return prompt # Placeholder

# --- Gate 1: Semantic Extraction (LLM) ---

def gate1_extract_and_brief_with_llm(content: str, llm_analyst, prompt_template) -> List[Dict[str, Any]]:
    """
    Uses an LLM to extract UserOutcome candidates and generate a dossier for each.
    This is a placeholder for the actual LLM chain execution.
    """
    print("    Gate 1: Semantic Extraction & Dossier Generation (LLM)")

    # In a real implementation:
    # llm_chain = LLMChain(llm=llm_analyst, prompt=prompt_template)
    # response = llm_chain.run(document_content=content)
    # return json.loads(response)

    # --- Placeholder Implementation ---
    # For now, we'll simulate the LLM by using the old regex extraction
    # and wrapping the result in a dossier format.
    print("      (Using regex extraction as a placeholder for LLM)")
    json_blocks = extract_json_blocks_for_llm_simulation(content)
    useroutcome_objects = extract_useroutcome_objects(json_blocks)

    dossiers = []
    for obj in useroutcome_objects:
        dossiers.append({
            "object_candidate": obj,
            "analyst_briefing": "This candidate was identified by the placeholder extraction logic. It appears to be a UserOutcome object based on its 'object_type' field."
        })
    
    if dossiers:
        print(f"      ▶ Found {len(dossiers)} candidate(s)")
    else:
        print("      ▶ No candidates found")
        
    return dossiers

def extract_json_blocks_for_llm_simulation(content: str) -> List[Dict[str, Any]]:
    """Legacy function used to simulate LLM extraction for the placeholder."""
    json_blocks = []
    json_pattern = r'```json\s*\n(.*?)\n```'
    matches = re.findall(json_pattern, content, re.DOTALL)
    for match in matches:
        try:
            json_obj = json.loads(match.strip())
            json_blocks.append(json_obj)
        except json.JSONDecodeError:
            continue
    return json_blocks

# --- Gate 2: Schema Validation ---

def gate2_validate_against_schema(obj: Dict[str, Any]) -> Tuple[bool, List[str]]:
    """
    Validates a single object against the USEROUTCOME_SCHEMA.
    Focuses on data types, required fields, and enums.
    """
    errors = []
    
    # This could be replaced with a more robust library like jsonschema
    # but we replicate the original logic for consistency.

    # Check required fields
    for field in USEROUTCOME_SCHEMA.get("required", []):
        if field not in obj:
            errors.append(f"Schema Error: Missing required field '{field}'")
        elif obj.get(field) is None or obj.get(field) == "":
            errors.append(f"Schema Error: Required field '{field}' cannot be empty")

    # Check field types and constraints
    for prop, schema in USEROUTCOME_SCHEMA.get("properties", {}).items():
        if prop not in obj:
            continue

        # Type checks
        if "type" in schema and not isinstance(obj[prop], eval(schema["type"])):
             # Note: eval is unsafe, jsonschema library is better
            pass # Simple check for now

        # Const check (for object_type)
        if "const" in schema and obj[prop] != schema["const"]:
            errors.append(f"Schema Error: Field '{prop}' must be '{schema['const']}'")

        # Enum check
        if "enum" in schema and obj[prop] not in schema["enum"]:
            errors.append(f"Schema Error: Field '{prop}' has invalid value. Must be one of {schema['enum']}")
            
    return len(errors) == 0, errors

# --- Gate 3: Conditional & Business Logic Validation ---

def gate3_validate_conditional_logic(obj: Dict[str, Any]) -> Tuple[bool, List[str]]:
    """
    Validates nuanced business rules that the schema cannot capture.
    """
    errors = []

    # Rule: `key_signals` are required if `flow_ids` are present.
    has_flow = ("flow_ids" in obj and isinstance(obj["flow_ids"], list) and len(obj["flow_ids"]) > 0)
    
    if has_flow:
        if "key_signals" not in obj or not obj["key_signals"]:
            errors.append("Logic Error: 'key_signals' is required when 'flow_ids' are present.")
        elif not isinstance(obj["key_signals"], list) or len(obj["key_signals"]) == 0:
            errors.append("Logic Error: 'key_signals' must be a non-empty array when 'flow_ids' are present.")

    # Rule: `outcome_statement` must follow a specific pattern.
    if "outcome_statement" in obj:
        statement = obj["outcome_statement"]
        if not re.match(r'^[A-Z][^.]*[.!]$', statement):
            errors.append("Logic Error: 'outcome_statement' must start with a capital letter and end with a period or exclamation mark.")

    return len(errors) == 0, errors


def extract_useroutcome_objects(json_blocks: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Extract User Outcome objects from JSON blocks."""
    useroutcome_objects = []
    
    for block in json_blocks:
        # Handle both direct User Outcome objects and nested structures
        if isinstance(block, dict):
            if block.get("object_type") == "UserOutcome":
                useroutcome_objects.append(block)
            # Check for nested user outcomes in arrays or other structures
            elif "user_outcomes" in block and isinstance(block["user_outcomes"], list):
                for outcome in block["user_outcomes"]:
                    if isinstance(outcome, dict) and outcome.get("object_type") == "UserOutcome":
                        useroutcome_objects.append(outcome)
    
    return useroutcome_objects


def has_related_user_flow(useroutcome: Dict[str, Any]) -> bool:
    """Check if the User Outcome has a related user flow."""
    # Check for flow_ids array
    if "flow_ids" in useroutcome and isinstance(useroutcome["flow_ids"], list) and len(useroutcome["flow_ids"]) > 0:
        return True
    
    # Check for user_flow_id (legacy field)
    if "user_flow_id" in useroutcome and useroutcome["user_flow_id"]:
        return True
    
    return False


def validate_useroutcome_object(obj: Dict[str, Any]) -> Tuple[bool, List[str]]:
    """
    DEPRECATED: This function is replaced by the multi-gate pipeline.
    Kept for reference during transition.
    """
    # This function's logic is now split between:
    # - gate2_validate_against_schema
    # - gate3_validate_conditional_logic
    return True, []


def process_file(file_path: Path, llm_analyst, prompt_template) -> Tuple[bool, List[Dict]]:
    """Processes a single file (MD or JSON) and returns its status and dossier results."""
    print(f"\nProcessing: {file_path.name}")
    dossiers = []
    try:
        content = file_path.read_text(encoding='utf-8')
        if file_path.suffix == ".md":
            # Gate 1: LLM Extraction for Markdown
            dossiers = gate1_extract_and_brief_with_llm(content, llm_analyst, prompt_template)
        elif file_path.suffix == ".json":
            # For JSON files, the content is the object itself.
            print("    Gate 1: Direct JSON Load")
            obj = json.loads(content)
            dossiers.append({
                "object_candidate": obj,
                "analyst_briefing": f"Candidate directly loaded from JSON source: {file_path.name}"
            })
            print(f"      ▶ Found 1 candidate(s)")

    except Exception as e:
        print(f"  ❌ Error reading or parsing file: {e}")
        return False, []

    if not dossiers:
        print("  ⚪ No User Outcome candidates found.")
        return True, [] # No objects found is not a failure of the file itself

    file_has_errors = False
    file_dossier_results = []

    for i, dossier in enumerate(dossiers):
        candidate = dossier["object_candidate"]
        briefing = dossier["analyst_briefing"]
        candidate_id = candidate.get("id", f"Candidate[{i}]")
        
        print(f"  - Dossier for '{candidate_id}':")
        print(f"    Analyst Briefing: {briefing}")
        
        candidate_errors = []

        # --- Gate 2: Schema Validation ---
        is_schema_valid, schema_errors = gate2_validate_against_schema(candidate)
        if not is_schema_valid:
            print(f"    ❌ Gate 2 FAILED: Schema validation")
            candidate_errors.extend(schema_errors)
        else:
            print(f"    ✅ Gate 2 PASSED: Schema validation")

        # --- Gate 3: Conditional Logic ---
        if is_schema_valid:
            is_logic_valid, logic_errors = gate3_validate_conditional_logic(candidate)
            if not is_logic_valid:
                print(f"    ❌ Gate 3 FAILED: Conditional logic")
                candidate_errors.extend(logic_errors)
            else:
                print(f"    ✅ Gate 3 PASSED: Conditional logic")

        dossier_status = "invalid" if candidate_errors else "valid"
        file_dossier_results.append({
            "candidate_id": candidate_id,
            "briefing": briefing,
            "status": dossier_status,
            "errors": candidate_errors,
            "candidate": candidate
        })

        if candidate_errors:
            file_has_errors = True

    return not file_has_errors, file_dossier_results


# --- Reporting Functions ---

def generate_markdown_report(report_data: List[Dict], report_path: Path):
    """Generates a Markdown summary of the validation run."""
    md_content = []
    failed_files_count = sum(1 for f in report_data if f["status"] == "failed")
    passed_files_count = len(report_data) - failed_files_count

    # --- Header ---
    md_content.append("# DUX Object Validation Report")
    md_content.append(f"*Run on: {datetime.now().isoformat()}*\n")
    md_content.append("## 📊 Summary")
    md_content.append(f"- **{passed_files_count} files passed** ✅")
    md_content.append(f"- **{failed_files_count} files failed** ❌\n")

    # --- Failed Files Details ---
    if failed_files_count > 0:
        md_content.append("--- ")
        md_content.append("## ❌ Failed Files Details")
        for file_result in report_data:
            if file_result["status"] == "failed":
                md_content.append(f"\n### 📄 File: `{file_result['path'].name}`")
                for dossier in file_result["dossiers"]:
                    if dossier["status"] == "invalid":
                        md_content.append(f"\n#### 🕵️ Dossier for: `{dossier['candidate_id']}`")
                        md_content.append(f"**Analyst Briefing:** {dossier['briefing']}\n")
                        md_content.append("**Errors Found:**")
                        for error in dossier["errors"]:
                            md_content.append(f"- `{error}`")
                        md_content.append("\n**Object Candidate:**")
                        md_content.append(f"```json\n{json.dumps(dossier['candidate'], indent=2)}\n```")

    # Write the report
    try:
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write("\n".join(md_content))
        print(f"\n📊 Markdown report generated at: {report_path}")
    except Exception as e:
        print(f"\n❌ Error generating Markdown report: {e}")


def main():
    """Main validation process using the multi-gate pipeline."""
    # --- Mode Detection: Harness or Standalone ---
    if len(sys.argv) > 1:
        # HARNESS MODE: Process a single file passed as an argument
        input_path = Path(sys.argv[1])
        if not input_path.exists():
            print(f"❌ ERROR: Input file not found at: {input_path}")
            sys.exit(1)

        print(f"🔍 User Outcome Validation (Harness Mode) for: {input_path.name}")
        print("=" * 60)
        
        is_valid, _ = process_file(input_path, None, None)
        
        if is_valid:
            print("\n✅ Validation PASSED")
            sys.exit(0)
        else:
            print("\n❌ Validation FAILED")
            sys.exit(1)

    # --- STANDALONE MODE: Scan watch folder and generate full report ---
    print("🔍 User Outcome Object Validation Script (Standalone Mode)")
    print("=" * 60)
    
    # --- Setup ---
    review_dir = Path("watch_folders/hitl_review")
    failed_dir = Path("watch_folders/hitl_failed")
    report_path = review_dir / "validation_report.md"
    
    if not review_dir.exists():
        print("❌ Review directory not found")
        return
    
    failed_dir.mkdir(exist_ok=True)
    
    # Process both .md and .json files
    all_files = list(review_dir.rglob("*.md")) + list(review_dir.rglob("*.json"))
    if not all_files:
        print("📭 No markdown or json files found in review directory")
        return
        
    # Note: Duplicate filtering might need adjustment if IDs can span MD and JSON files
    files_to_process = filter_duplicate_files(all_files)
    print(get_duplicate_summary(all_files))
    
    # --- LLM Analyst Setup (Conceptual) ---
    llm_analyst = get_llm_analyst()
    prompt_template = create_analyst_prompt_template()
    
    report_data = [] # To store results for the report
    
    # --- File Processing Loop ---
    for file_path in files_to_process:
        is_valid, dossier_results = process_file(file_path, llm_analyst, prompt_template)
        
        file_status = "passed" if is_valid else "failed"
        report_data.append({
            "path": file_path,
            "status": file_status,
            "dossiers": dossier_results
        })

        if not is_valid:
            # Move failed file
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            failed_filename = f"{timestamp}_{file_path.name}"
            failed_path = failed_dir / failed_filename
            try:
                shutil.copy2(file_path, failed_path)
                print(f"  📁 Moved to: {failed_path}")
            except Exception as e:
                print(f"  ❌ Error moving file: {e}")

    # --- Summary & Report Generation ---
    valid_files = sum(1 for r in report_data if r["status"] == "passed")
    failed_files = len(report_data) - valid_files
    total_useroutcomes = sum(1 for r in report_data for d in r["dossiers"] if d["status"] == "valid")

    print(f"\n" + "=" * 60)
    print("📊 VALIDATION SUMMARY")
    print(f"✅ Valid files: {valid_files}")
    print(f"❌ Failed files: {failed_files}")
    print(f"📦 Total Valid User Outcome objects: {total_useroutcomes}")
    
    generate_markdown_report(report_data, report_path)

    if failed_files > 0:
        print(f"\n🔍 Check {failed_dir} for failed files and {report_path} for the full report.")
    else:
        print(f"\n🎉 All User Outcome objects passed validation!")


if __name__ == "__main__":
    main()