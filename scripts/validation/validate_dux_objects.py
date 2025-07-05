#!/usr/bin/env python3
"""
DUX Object Model Validation Script for HITL Review Process

This script processes markdown files in the watch_folders/hitl_review directory,
extracts DUX objects from JSON blocks, validates them against their respective schemas,
and moves invalid files to hitl_failed with error details.

Supports all DUX object types: Problem, Behavior, Result, User Outcome, Flow, Insight, Provenance
"""

import json
import re
import shutil
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any, Tuple

# DUX Object Schemas (v9.6)
DUX_SCHEMAS = {
    "Problem": {
        "required": ["object_type", "id", "job_statement", "evidence"],
        "properties": {
            "object_type": {"type": "string", "enum": ["Problem"]},
            "id": {"type": "string"},
            "job_statement": {"type": "string"},
            "evidence": {"type": "array", "items": {"type": "string"}},
            "end_user": {"type": "array", "items": {"type": "string"}},
            "what_is_at_stake": {"type": "string"},
            "protocol_url": {"type": "string"},
            "result_ids": {"type": "array", "items": {"type": "object"}},
            "useroutcome_ids": {"type": "array", "items": {"type": "object"}},
            "flow_ids": {"type": "array", "items": {"type": "object"}},
            "tags": {"type": "array", "items": {"type": "string"}},
            "created_at": {"type": "string"},
            "updated_at": {"type": "string"}
        }
    },
    "Behavior": {
        "required": ["object_type", "id", "user_enablement", "behavior_type", "evidence"],
        "properties": {
            "object_type": {"type": "string", "enum": ["Behavior"]},
            "id": {"type": "string"},
            "user_enablement": {"type": "string"},
            "behavior_type": {"type": "string", "enum": ["system_action", "organizational_process", "user_action"]},
            "signals": {"type": "array", "items": {"type": "string"}},
            "acceptance_criteria": {"type": "string"},
            "evidence": {"type": "array", "items": {"type": "string"}},
            "problem_ids": {"type": "array", "items": {"type": "object"}},
            "result_ids": {"type": "array", "items": {"type": "object"}},
            "tags": {"type": "array", "items": {"type": "string"}},
            "created_at": {"type": "string"},
            "updated_at": {"type": "string"}
        }
    },
    "Result": {
        "required": ["object_type", "id", "target_impact", "success_criteria", "evidence"],
        "properties": {
            "object_type": {"type": "string", "enum": ["Result"]},
            "id": {"type": "string"},
            "target_impact": {"type": "string"},
            "success_criteria": {"type": "string"},
            "evidence": {"type": "array", "items": {"type": "string"}},
            "problem_ids": {"type": "array", "items": {"type": "object"}},
            "behavior_ids": {"type": "array", "items": {"type": "object"}},
            "useroutcome_ids": {"type": "array", "items": {"type": "object"}},
            "tags": {"type": "array", "items": {"type": "string"}},
            "created_at": {"type": "string"},
            "updated_at": {"type": "string"}
        }
    },
    "UserOutcome": {
        "required": ["object_type", "id", "outcome_statement", "evidence"],
        "properties": {
            "object_type": {"type": "string", "enum": ["UserOutcome"]},
            "id": {"type": "string"},
            "outcome_statement": {"type": "string"},
            "evidence": {"type": "array", "items": {"type": "string"}},
            "problem_ids": {"type": "array", "items": {"type": "object"}},
            "behavior_ids": {"type": "array", "items": {"type": "object"}},
            "result_ids": {"type": "array", "items": {"type": "object"}},
            "tags": {"type": "array", "items": {"type": "string"}},
            "created_at": {"type": "string"},
            "updated_at": {"type": "string"}
        }
    },
    "Flow": {
        "required": ["object_type", "id", "flow_name", "flow_description", "evidence"],
        "properties": {
            "object_type": {"type": "string", "enum": ["Flow"]},
            "id": {"type": "string"},
            "flow_name": {"type": "string"},
            "flow_description": {"type": "string"},
            "flow_steps": {"type": "array", "items": {"type": "object"}},
            "evidence": {"type": "array", "items": {"type": "string"}},
            "problem_ids": {"type": "array", "items": {"type": "object"}},
            "behavior_ids": {"type": "array", "items": {"type": "object"}},
            "useroutcome_ids": {"type": "array", "items": {"type": "object"}},
            "tags": {"type": "array", "items": {"type": "string"}},
            "created_at": {"type": "string"},
            "updated_at": {"type": "string"}
        }
    },
    "Insight": {
        "required": ["object_type", "id", "insight_teaser", "insight_chain", "evidence_maturity"],
        "properties": {
            "object_type": {"type": "string", "enum": ["Insight"]},
            "id": {"type": "string"},
            "insight_teaser": {"type": "string"},
            "insight_chain": {"type": "array", "items": {"type": "string"}},
            "related_objects": {"type": "array", "items": {"type": "object"}},
            "insight_story_block": {"type": "string"},
            "evidence_maturity": {"type": "string", "enum": ["01_raw", "02_processed", "03_analyzed", "04_synthesized", "05_triangulated"]},
            "tags": {"type": "array", "items": {"type": "string"}},
            "created_at": {"type": "string"},
            "updated_at": {"type": "string"}
        }
    },
    "Provenance": {
        "required": ["object_type", "id", "evidence_block"],
        "properties": {
            "object_type": {"type": "string", "enum": ["Provenance"]},
            "id": {"type": "string"},
            "evidence_block": {"type": "object"},
            "tags": {"type": "array", "items": {"type": "string"}},
            "created_at": {"type": "string"},
            "updated_at": {"type": "string"}
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


def extract_dux_objects(json_blocks: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
    """Extract DUX objects from JSON blocks, organized by type."""
    objects_by_type = {obj_type: [] for obj_type in DUX_SCHEMAS.keys()}
    
    for block in json_blocks:
        if isinstance(block, dict):
            # Handle direct objects
            obj_type = block.get("object_type")
            if obj_type in DUX_SCHEMAS:
                objects_by_type[obj_type].append(block)
            
            # Handle nested object collections
            for obj_type in DUX_SCHEMAS.keys():
                collection_key = f"{obj_type.lower()}_objects"
                if collection_key in block and isinstance(block[collection_key], list):
                    objects_by_type[obj_type].extend(block[collection_key])
    
    return objects_by_type


def validate_dux_object(obj: Dict[str, Any], obj_type: str) -> List[str]:
    """Validate a single DUX object against its schema."""
    errors = []
    schema = DUX_SCHEMAS[obj_type]
    
    # Check required fields
    for field in schema["required"]:
        if field not in obj:
            errors.append(f"Missing required field: {field}")
    
    # Check object_type
    if "object_type" in obj and obj["object_type"] != obj_type:
        errors.append(f"Invalid object_type: {obj['object_type']}, must be '{obj_type}'")
    
    # Check evidence is array of strings (for objects that have it)
    if "evidence" in obj:
        if not isinstance(obj["evidence"], list):
            errors.append("Evidence must be an array")
        else:
            for i, evidence_id in enumerate(obj["evidence"]):
                if not isinstance(evidence_id, str):
                    errors.append(f"Evidence[{i}] must be a string, got {type(evidence_id)}")
    
    # Type-specific validations
    if obj_type == "Problem":
        if "job_statement" in obj:
            job_stmt = obj["job_statement"]
            if not isinstance(job_stmt, str) or len(job_stmt.strip()) < 10:
                errors.append("Job statement must be a non-empty string")
    
    elif obj_type == "Behavior":
        if "behavior_type" in obj:
            valid_types = ["system_action", "organizational_process", "user_action"]
            if obj["behavior_type"] not in valid_types:
                errors.append(f"Invalid behavior_type: {obj['behavior_type']}")
    
    elif obj_type == "Insight":
        if "evidence_maturity" in obj:
            valid_maturity = ["01_raw", "02_processed", "03_analyzed", "04_synthesized", "05_triangulated"]
            if obj["evidence_maturity"] not in valid_maturity:
                errors.append(f"Invalid evidence_maturity: {obj['evidence_maturity']}")
    
    return errors


def process_markdown_file(file_path: Path) -> Dict[str, Any]:
    """Process a single markdown file and return validation results."""
    print(f"Processing: {file_path.name}")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return {
            "valid": False,
            "errors": [f"Failed to read file: {e}"],
            "objects_by_type": {},
            "total_objects": 0
        }
    
    # Extract JSON blocks
    json_blocks = extract_json_blocks(content)
    if not json_blocks:
        return {
            "valid": True,
            "errors": [],
            "objects_by_type": {},
            "total_objects": 0,
            "note": "No JSON blocks found"
        }
    
    # Extract DUX objects
    objects_by_type = extract_dux_objects(json_blocks)
    total_objects = sum(len(objects) for objects in objects_by_type.values())
    
    if total_objects == 0:
        return {
            "valid": True,
            "errors": [],
            "objects_by_type": {},
            "total_objects": 0,
            "note": "No DUX objects found"
        }
    
    # Validate each object
    all_errors = []
    valid_objects_by_type = {obj_type: [] for obj_type in DUX_SCHEMAS.keys()}
    
    for obj_type, objects in objects_by_type.items():
        for i, obj in enumerate(objects):
            errors = validate_dux_object(obj, obj_type)
            if errors:
                obj_id = obj.get('id', f'unknown_{i}')
                all_errors.extend([f"{obj_type}[{i}] ({obj_id}): {error}" for error in errors])
            else:
                valid_objects_by_type[obj_type].append(obj)
    
    return {
        "valid": len(all_errors) == 0,
        "errors": all_errors,
        "objects_by_type": valid_objects_by_type,
        "total_objects": total_objects
    }


def move_to_failed(file_path: Path, errors: List[str]):
    """Move invalid file to hitl_failed folder with error details."""
    failed_dir = Path("watch_folders/hitl_failed")
    failed_dir.mkdir(exist_ok=True)
    
    # Create timestamped filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    failed_filename = f"{timestamp}_{file_path.name}"
    failed_path = failed_dir / failed_filename
    
    # Copy file to failed directory
    shutil.copy2(file_path, failed_path)
    
    # Create error log
    error_log_path = failed_dir / f"{timestamp}_{file_path.stem}_errors.txt"
    with open(error_log_path, 'w') as f:
        f.write(f"Validation failed for: {file_path.name}\n")
        f.write(f"Timestamp: {datetime.now().isoformat()}\n")
        f.write(f"Original location: {file_path}\n")
        f.write("\nErrors:\n")
        for error in errors:
            f.write(f"- {error}\n")
    
    print(f"  Moved to: {failed_path}")
    print(f"  Error log: {error_log_path}")


def main():
    """Main validation process."""
    print("🔍 DUX Object Model Validation Script")
    print("=" * 60)
    
    # Setup paths
    review_dir = Path("watch_folders/hitl_review")
    if not review_dir.exists():
        print(f"❌ Review directory not found: {review_dir}")
        return
    
    # Find markdown files (recursively)
    markdown_files = list(review_dir.rglob("*.md"))
    if not markdown_files:
        print("📭 No markdown files found in review directory")
        return
    
    print(f"📁 Found {len(markdown_files)} markdown files")
    print()
    
    # Process each file
    total_processed = 0
    total_valid = 0
    total_failed = 0
    total_objects_by_type = {obj_type: 0 for obj_type in DUX_SCHEMAS.keys()}
    
    for file_path in markdown_files:
        result = process_markdown_file(file_path)
        total_processed += 1
        
        if result["valid"]:
            total_valid += 1
            if result.get("objects_by_type"):
                # Count objects by type
                for obj_type, objects in result["objects_by_type"].items():
                    if objects:
                        total_objects_by_type[obj_type] += len(objects)
                        print(f"  ✅ {obj_type}: {len(objects)} objects")
            else:
                print(f"  ⚪ No DUX objects found")
        else:
            total_failed += 1
            print(f"  ❌ Invalid: {len(result['errors'])} errors")
            move_to_failed(file_path, result["errors"])
        
        print()
    
    # Summary
    print("=" * 60)
    print(f"📊 Summary:")
    print(f"  Total processed: {total_processed}")
    print(f"  Valid files: {total_valid}")
    print(f"  Failed files: {total_failed}")
    print()
    print(f"📦 Objects by type:")
    for obj_type, count in total_objects_by_type.items():
        if count > 0:
            print(f"  {obj_type}: {count}")
    
    if total_failed > 0:
        print(f"\n❌ {total_failed} files moved to watch_folders/hitl_failed/")
    else:
        print(f"\n✅ All files passed validation!")


if __name__ == "__main__":
    main() 