#!/usr/bin/env python3
"""
Flow Object Validation Script for HITL Review Process

This script processes markdown files in the watch_folders/hitl_review directory,
extracts Flow objects from JSON blocks, validates them against the schema,
and moves invalid files to hitl_failed with error details.
"""

import json
import re
import shutil
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any, Tuple

# Schema for Flow objects (v9.6)
FLOW_SCHEMA = {
    "type": "object",
    "required": ["object_type", "id", "flow_statement", "steps", "evidence"],
    "properties": {
        "object_type": {"type": "string", "enum": ["Flow"]},
        "id": {"type": "string", "pattern": "^flow_.*"},
        "flow_statement": {"type": "string", "minLength": 10},
        "steps": {
            "type": "array",
            "items": {"type": "object"},
            "minItems": 1
        },
        "evidence": {
            "type": "array",
            "items": {"type": "string"},
            "minItems": 1
        },
        "context": {"type": "string"},
        "triggers": {"type": "array", "items": {"type": "string"}},
        "outcomes": {"type": "array", "items": {"type": "string"}},
        "related_problems": {"type": "array", "items": {"type": "string"}},
        "related_behaviors": {"type": "array", "items": {"type": "string"}},
        "related_results": {"type": "array", "items": {"type": "string"}},
        "tags": {"type": "array", "items": {"type": "string"}},
        "confidence": {"type": "number", "minimum": 0, "maximum": 1},
        "created_at": {"type": "string", "format": "date-time"},
        "updated_at": {"type": "string", "format": "date-time"}
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


def extract_flow_objects(json_blocks: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Extract Flow objects from JSON blocks."""
    flow_objects = []
    
    for block in json_blocks:
        # Handle both direct Flow objects and nested structures
        if isinstance(block, dict):
            if block.get("object_type") == "Flow":
                flow_objects.append(block)
            # Check for nested flows in arrays or other structures
            elif "flows" in block and isinstance(block["flows"], list):
                for flow in block["flows"]:
                    if isinstance(flow, dict) and flow.get("object_type") == "Flow":
                        flow_objects.append(flow)
    
    return flow_objects


def validate_flow_object(obj: Dict[str, Any]) -> Tuple[bool, List[str]]:
    """Validate a single Flow object against the schema."""
    errors = []
    
    # Check required fields
    required_fields = FLOW_SCHEMA["required"]
    for field in required_fields:
        if field not in obj:
            errors.append(f"Missing required field: {field}")
            continue
        
        if obj[field] is None or obj[field] == "":
            errors.append(f"Required field '{field}' cannot be empty")
    
    # Check object_type
    if "object_type" in obj and obj["object_type"] != "Flow":
        errors.append("object_type must be 'Flow'")
    
    # Check ID pattern
    if "id" in obj and not re.match(r'^flow_.*', obj["id"]):
        errors.append("ID must start with 'flow_'")
    
    # Check flow_statement length
    if "flow_statement" in obj and len(obj["flow_statement"]) < 10:
        errors.append("flow_statement must be at least 10 characters")
    
    # Check steps array
    if "steps" in obj:
        if not isinstance(obj["steps"], list):
            errors.append("steps must be an array")
        elif len(obj["steps"]) == 0:
            errors.append("steps array cannot be empty")
        else:
            for i, step in enumerate(obj["steps"]):
                if not isinstance(step, dict):
                    errors.append(f"steps[{i}] must be an object, got {type(step)}")
    
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
    
    # Check confidence range
    if "confidence" in obj:
        try:
            confidence = float(obj["confidence"])
            if confidence < 0 or confidence > 1:
                errors.append("confidence must be between 0 and 1")
        except (ValueError, TypeError):
            errors.append("confidence must be a number")
    
    return len(errors) == 0, errors


def main():
    """Main validation process."""
    print("🔍 Flow Object Validation Script")
    print("=" * 60)
    
    # Setup paths
    review_dir = Path("watch_folders/hitl_review")
    failed_dir = Path("watch_folders/hitl_failed")
    
    if not review_dir.exists():
        print("❌ Review directory not found")
        return
    
    failed_dir.mkdir(exist_ok=True)
    
    # Find markdown files (recursively)
    markdown_files = list(review_dir.rglob("*.md"))
    if not markdown_files:
        print("📭 No markdown files found in review directory")
        return
    
    print(f"📁 Found {len(markdown_files)} markdown files")
    
    valid_files = 0
    failed_files = 0
    total_flows = 0
    
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
        
        # Extract Flow objects
        flow_objects = extract_flow_objects(json_blocks)
        if not flow_objects:
            print("  ⚪ No Flow objects found")
            continue
        
        # Validate each Flow object
        all_valid = True
        all_errors = []
        
        for i, flow in enumerate(flow_objects):
            is_valid, errors = validate_flow_object(flow)
            if not is_valid:
                all_valid = False
                flow_id = flow.get("id", f"Flow[{i}]")
                for error in errors:
                    all_errors.append(f"- {flow_id}: {error}")
        
        if all_valid:
            print(f"  ✅ Flow: {len(flow_objects)} objects")
            valid_files += 1
            total_flows += len(flow_objects)
        else:
            print(f"  ❌ Invalid: {len(all_errors)} errors")
            
            # Move file to failed directory
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            failed_filename = f"{timestamp}_{file_path.name}"
            failed_path = failed_dir / failed_filename
            
            try:
                shutil.move(str(file_path), str(failed_path))
                print(f"  Moved to: {failed_path}")
                
                # Create error log
                error_log_path = failed_dir / f"{timestamp}_{file_path.stem}_errors.txt"
                with open(error_log_path, 'w') as f:
                    f.write("Flow Object Validation Errors\n")
                    f.write(f"File: {file_path.name}\n")
                    f.write(f"Timestamp: {datetime.now().isoformat()}\n")
                    f.write(f"Total Errors: {len(all_errors)}\n\n")
                    f.write("Errors:\n")
                    for error in all_errors:
                        f.write(f"{error}\n")
                
                print(f"  Error log: {error_log_path}")
                failed_files += 1
                
            except Exception as e:
                print(f"  ❌ Error moving file: {e}")
    
    # Summary
    print("\n" + "=" * 60)
    print("📊 Summary:")
    print(f"  Total processed: {len(markdown_files)}")
    print(f"  Valid files: {valid_files}")
    print(f"  Failed files: {failed_files}")
    print(f"\n📦 Objects by type:")
    print(f"  Flow: {total_flows}")
    
    if failed_files > 0:
        print(f"\n❌ {failed_files} files moved to watch_folders/hitl_failed/")


if __name__ == "__main__":
    main() 