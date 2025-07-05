#!/usr/bin/env python3
"""
Provenance Object Validation Script for HITL Review Process

This script processes markdown files in the watch_folders/hitl_review directory,
extracts Provenance objects from JSON blocks, validates them against the schema,
and moves invalid files to hitl_failed with error details.
"""

import json
import re
import shutil
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any, Tuple
from duplicate_handler import filter_duplicate_files, get_duplicate_summary

# Schema for Provenance objects (v9.6)
PROVENANCE_SCHEMA = {
    "type": "object",
    "required": ["object_type", "id", "evidence_block"],
    "properties": {
        "object_type": {"type": "string", "enum": ["Provenance"]},
        "id": {"type": "string", "pattern": "^prov_.*"},
        "evidence_block": {"type": "object"},
        "source_type": {"type": "string"},
        "source_url": {"type": "string"},
        "collection_date": {"type": "string", "format": "date-time"},
        "participant_count": {"type": "integer", "minimum": 1},
        "methodology": {"type": "string"},
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


def extract_provenance_objects(json_blocks: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Extract Provenance objects from JSON blocks."""
    provenance_objects = []
    
    for block in json_blocks:
        # Handle both direct Provenance objects and nested structures
        if isinstance(block, dict):
            if block.get("object_type") == "Provenance":
                provenance_objects.append(block)
            # Check for nested provenance in arrays or other structures
            elif "provenance" in block and isinstance(block["provenance"], list):
                for prov in block["provenance"]:
                    if isinstance(prov, dict) and prov.get("object_type") == "Provenance":
                        provenance_objects.append(prov)
    
    return provenance_objects


def validate_provenance_object(obj: Dict[str, Any]) -> Tuple[bool, List[str]]:
    """Validate a single Provenance object against the schema."""
    errors = []
    
    # Check required fields
    required_fields = PROVENANCE_SCHEMA["required"]
    for field in required_fields:
        if field not in obj:
            errors.append(f"Missing required field: {field}")
            continue
        
        if obj[field] is None or obj[field] == "":
            errors.append(f"Required field '{field}' cannot be empty")
    
    # Check object_type
    if "object_type" in obj and obj["object_type"] != "Provenance":
        errors.append("object_type must be 'Provenance'")
    
    # Check ID pattern
    if "id" in obj and not re.match(r'^prov_.*', obj["id"]):
        errors.append("ID must start with 'prov_'")
    
    # Check evidence_block is an object
    if "evidence_block" in obj and not isinstance(obj["evidence_block"], dict):
        errors.append("evidence_block must be an object")
    
    # Check participant_count is positive integer
    if "participant_count" in obj:
        try:
            count = int(obj["participant_count"])
            if count < 1:
                errors.append("participant_count must be at least 1")
        except (ValueError, TypeError):
            errors.append("participant_count must be an integer")
    
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
    print("🔍 Provenance Object Validation Script")
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
    total_provenance = 0
    
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
        
        # Extract Provenance objects
        provenance_objects = extract_provenance_objects(json_blocks)
        if not provenance_objects:
            print("  ⚪ No Provenance objects found")
            continue
        
        # Validate each Provenance object
        all_valid = True
        all_errors = []
        
        for i, provenance in enumerate(provenance_objects):
            is_valid, errors = validate_provenance_object(provenance)
            if not is_valid:
                all_valid = False
                provenance_id = provenance.get("id", f"Provenance[{i}]")
                for error in errors:
                    all_errors.append(f"- {provenance_id}: {error}")
        
        if all_valid:
            print(f"  ✅ Provenance: {len(provenance_objects)} objects")
            valid_files += 1
            total_provenance += len(provenance_objects)
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
                    f.write("Provenance Object Validation Errors\n")
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
    print(f"  Provenance: {total_provenance}")
    
    if failed_files > 0:
        print(f"\n❌ {failed_files} files moved to watch_folders/hitl_failed/")


if __name__ == "__main__":
    main() 