#!/usr/bin/env python3
"""
Problem Object Validation Script for HITL Review Process

This script processes markdown files in the watch_folders/hitl_review directory,
extracts Problem objects from JSON blocks, validates them against the schema,
and moves invalid files to hitl_failed with error details.
"""

import json
import re
import shutil
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any

# Schema for Problem objects (v9.6)
PROBLEM_SCHEMA = {
    "type": "object",
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


def extract_problem_objects(json_blocks: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Extract Problem objects from JSON blocks."""
    problem_objects = []
    
    for block in json_blocks:
        # Handle both direct Problem objects and nested structures
        if isinstance(block, dict):
            if block.get("object_type") == "Problem":
                problem_objects.append(block)
            elif "problem_objects" in block:
                problem_objects.extend(block["problem_objects"])
    
    return problem_objects


def validate_problem_object(problem: Dict[str, Any]) -> List[str]:
    """Validate a single Problem object against the schema."""
    errors = []
    
    # Check required fields
    required_fields = ["object_type", "id", "job_statement", "evidence"]
    for field in required_fields:
        if field not in problem:
            errors.append(f"Missing required field: {field}")
    
    # Check object_type
    if "object_type" in problem and problem["object_type"] != "Problem":
        errors.append(
            f"Invalid object_type: {problem['object_type']}, must be 'Problem'"
        )
    
    # Check evidence is array of strings
    if "evidence" in problem:
        if not isinstance(problem["evidence"], list):
            errors.append("Evidence must be an array")
        else:
            for i, evidence_id in enumerate(problem["evidence"]):
                if not isinstance(evidence_id, str):
                    errors.append(
                        f"Evidence[{i}] must be a string, got {type(evidence_id)}"
                    )
    
    # Check job_statement format (basic JTBD format)
    if "job_statement" in problem:
        job_stmt = problem["job_statement"]
        if not isinstance(job_stmt, str):
            errors.append("Job statement must be a string")
        elif len(job_stmt.strip()) < 10:
            errors.append("Job statement too short")
    
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
            "problem_objects": []
        }
    
    # Extract JSON blocks
    json_blocks = extract_json_blocks(content)
    if not json_blocks:
        return {
            "valid": True,
            "errors": [],
            "problem_objects": [],
            "note": "No JSON blocks found"
        }
    
    # Extract Problem objects
    problem_objects = extract_problem_objects(json_blocks)
    if not problem_objects:
        return {
            "valid": True,
            "errors": [],
            "problem_objects": [],
            "note": "No Problem objects found"
        }
    
    # Validate each Problem object
    all_errors = []
    valid_problems = []
    
    for i, problem in enumerate(problem_objects):
        errors = validate_problem_object(problem)
        if errors:
            all_errors.extend([f"Problem[{i}] ({problem.get('id', 'unknown')}): {error}" for error in errors])
        else:
            valid_problems.append(problem)
    
    return {
        "valid": len(all_errors) == 0,
        "errors": all_errors,
        "problem_objects": valid_problems,
        "total_problems": len(problem_objects)
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
    print("🔍 Problem Object Validation Script")
    print("=" * 50)
    
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
    
    for file_path in markdown_files:
        result = process_markdown_file(file_path)
        total_processed += 1
        
        if result["valid"]:
            total_valid += 1
            if result.get("problem_objects"):
                print(f"  ✅ Valid: {len(result['problem_objects'])} Problem objects")
            else:
                print(f"  ⚪ No Problem objects found")
        else:
            total_failed += 1
            print(f"  ❌ Invalid: {len(result['errors'])} errors")
            move_to_failed(file_path, result["errors"])
        
        print()
    
    # Summary
    print("=" * 50)
    print(f"📊 Summary:")
    print(f"  Total processed: {total_processed}")
    print(f"  Valid files: {total_valid}")
    print(f"  Failed files: {total_failed}")
    
    if total_failed > 0:
        print(f"\n❌ {total_failed} files moved to watch_folders/hitl_failed/")
    else:
        print(f"\n✅ All files passed validation!")

if __name__ == "__main__":
    main() 