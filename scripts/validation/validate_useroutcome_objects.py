#!/usr/bin/env python3
"""
User Outcome Object Validation Script for HITL Review Process

This script processes markdown files in the watch_folders/hitl_review directory,
extracts User Outcome objects from JSON blocks, validates them against the schema,
and moves invalid files to hitl_failed with error details.

Handles conditional validation where key_signals are only required if there's a 
related user_flow.

References:
- docs/100_START_HERE/dux_object_template.md - Template structure
- docs/infrastructure_as_code/GOVERNANCE_NAMING_CONVENTIONS.md - Naming rules
- src/dux_v9.6_split_schema/dux_object_useroutcome.json - Schema definition
"""

import json
import re
import shutil
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any, Tuple
from duplicate_handler import filter_duplicate_files, get_duplicate_summary
from config import OBJECT_TYPE_PATTERNS, validate_documentation_files

# Schema for User Outcome objects (v9.6) - matches actual schema
# Reference: src/dux_v9.6_split_schema/dux_object_useroutcome.json
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


def extract_json_blocks(content: str) -> List[Dict[str, Any]]:
    """Extract JSON blocks from markdown content."""
    json_blocks = []
    
    # Pattern to match JSON blocks (```json ... ```)
    json_pattern = r'```json\s*\n(.*?)\n```'
    matches = re.findall(json_pattern, content, re.DOTALL)
    
    for match in matches:
        try:
            json_obj = json.loads(match.strip())
            json_blocks.append(json_obj)
        except json.JSONDecodeError as e:
            print(f"  Warning: Invalid JSON block: {e}")
            continue
    
    return json_blocks


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
    """Validate a single User Outcome object against the schema with conditional logic."""
    errors = []
    
    # Check required fields (excluding conditional ones)
    base_required_fields = ["object_type", "id", "outcome_statement", "acceptance_criteria", "evidence_maturity", "evidence"]
    
    for field in base_required_fields:
        if field not in obj:
            errors.append(f"Missing required field: {field}")
            continue
        
        if obj[field] is None or obj[field] == "":
            errors.append(f"Required field '{field}' cannot be empty")
    
    # Check object_type
    if "object_type" in obj and obj["object_type"] != "UserOutcome":
        errors.append("object_type must be 'UserOutcome'")
    
    # Check outcome_statement pattern
    if "outcome_statement" in obj:
        statement = obj["outcome_statement"]
        if not re.match(r'^[A-Z][^.]*[.!]$', statement):
            errors.append("outcome_statement must start with capital letter and end with period or exclamation mark")
    
    # Check evidence array
    if "evidence" in obj:
        if not isinstance(obj["evidence"], list):
            errors.append("evidence must be an array")
        elif len(obj["evidence"]) == 0:
            errors.append("evidence array cannot be empty")
        else:
            for i, evidence in enumerate(obj["evidence"]):
                if not isinstance(evidence, str):
                    errors.append(f"evidence[{i}] must be a string, got {type(evidence)}")
    
    # Check acceptance_criteria array
    if "acceptance_criteria" in obj:
        if not isinstance(obj["acceptance_criteria"], list):
            errors.append("acceptance_criteria must be an array")
        elif len(obj["acceptance_criteria"]) == 0:
            errors.append("acceptance_criteria array cannot be empty")
        else:
            for i, criteria in enumerate(obj["acceptance_criteria"]):
                if not isinstance(criteria, str):
                    errors.append(f"acceptance_criteria[{i}] must be a string, got {type(criteria)}")
    
    # Check evidence_maturity enum
    if "evidence_maturity" in obj:
        valid_maturity_levels = ["01_assumptive", "02_anecdotal", "03_early_signal", "04_balanced_signal", "05_triangulated"]
        if obj["evidence_maturity"] not in valid_maturity_levels:
            errors.append(f"evidence_maturity must be one of: {', '.join(valid_maturity_levels)}")
    
    # CONDITIONAL VALIDATION: key_signals only required if there's a related user flow
    has_flow = has_related_user_flow(obj)
    
    if has_flow:
        # If there's a related user flow, key_signals should be present
        if "key_signals" not in obj or not obj["key_signals"]:
            errors.append("key_signals required when user_flow is related - ETL pipeline should suggest signals from the flow")
        elif not isinstance(obj["key_signals"], list) or len(obj["key_signals"]) == 0:
            errors.append("key_signals must be a non-empty array when user_flow is related")
        else:
            for i, signal in enumerate(obj["key_signals"]):
                if not isinstance(signal, str):
                    errors.append(f"key_signals[{i}] must be a string, got {type(signal)}")
    else:
        # If no related user flow, key_signals is optional but should be noted for ETL suggestion
        if "key_signals" not in obj or not obj["key_signals"]:
            # This is not an error, but we could add a note for the ETL pipeline
            pass
    
    # Check priority enum if present
    if "priority" in obj:
        valid_priorities = ["critical", "high", "medium", "low"]
        if obj["priority"] not in valid_priorities:
            errors.append(f"priority must be one of: {', '.join(valid_priorities)}")
    
    return len(errors) == 0, errors


def main():
    """Main validation process."""
    print("🔍 User Outcome Object Validation Script")
    print("=" * 60)
    
    # Setup paths
    review_dir = Path("watch_folders/hitl_review")
    failed_dir = Path("watch_folders/hitl_failed")
    
    if not review_dir.exists():
        print("❌ Review directory not found")
        return
    
    failed_dir.mkdir(exist_ok=True)
    
    # Find markdown files (recursively)
    all_markdown_files = list(review_dir.rglob("*.md"))
    if not all_markdown_files:
        print("📭 No markdown files found in review directory")
        return
    
    # Filter out duplicates, keeping only the most recent version of each object
    markdown_files = filter_duplicate_files(all_markdown_files)
    
    print(get_duplicate_summary(all_markdown_files))
    
    valid_files = 0
    failed_files = 0
    total_useroutcomes = 0
    
    # Process each file
    for file_path in markdown_files:
        print(f"\nProcessing: {file_path.name}")
        
        try:
            content = file_path.read_text(encoding='utf-8')
        except Exception as e:
            print(f"  ❌ Error reading file: {e}")
            continue
        
        # Extract JSON blocks
        json_blocks = extract_json_blocks(content)
        if not json_blocks:
            print("  ⚪ No JSON blocks found")
            continue
        
        # Extract User Outcome objects
        useroutcome_objects = extract_useroutcome_objects(json_blocks)
        if not useroutcome_objects:
            print("  ⚪ No User Outcome objects found")
            continue
        
        # Validate each User Outcome object
        all_valid = True
        all_errors = []
        
        for i, useroutcome in enumerate(useroutcome_objects):
            is_valid, errors = validate_useroutcome_object(useroutcome)
            if not is_valid:
                all_valid = False
                useroutcome_id = useroutcome.get("id", f"UserOutcome[{i}]")
                for error in errors:
                    all_errors.append(f"- {useroutcome_id}: {error}")
        
        if all_valid:
            print(f"  ✅ UserOutcome: {len(useroutcome_objects)} objects")
            valid_files += 1
            total_useroutcomes += len(useroutcome_objects)
        else:
            print(f"  ❌ Invalid: {len(all_errors)} errors")
            
            # Move file to failed directory
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            failed_filename = f"{timestamp}_{file_path.name}"
            failed_path = failed_dir / failed_filename
            
            try:
                shutil.copy2(file_path, failed_path)
                
                # Create error log
                error_filename = f"{timestamp}_{file_path.stem}_errors.txt"
                error_path = failed_dir / error_filename
                
                with open(error_path, 'w', encoding='utf-8') as f:
                    f.write("User Outcome Object Validation Errors\n")
                    f.write(f"File: {file_path.name}\n")
                    f.write(f"Timestamp: {datetime.now().isoformat()}\n")
                    f.write(f"Total Errors: {len(all_errors)}\n\n")
                    f.write("Errors:\n")
                    for error in all_errors:
                        f.write(f"{error}\n")
                
                print(f"  📁 Moved to: {failed_filename}")
                print(f"  📝 Error log: {error_filename}")
                failed_files += 1
                
            except Exception as e:
                print(f"  ❌ Error moving file: {e}")
    
    # Summary
    print(f"\n" + "=" * 60)
    print("📊 VALIDATION SUMMARY")
    print(f"✅ Valid files: {valid_files}")
    print(f"❌ Failed files: {failed_files}")
    print(f"📦 Total User Outcome objects: {total_useroutcomes}")
    
    if failed_files > 0:
        print(f"\n🔍 Check {failed_dir} for failed files and error logs")
    else:
        print(f"\n🎉 All User Outcome objects passed validation!")


if __name__ == "__main__":
    main() 