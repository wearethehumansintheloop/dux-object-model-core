#!/usr/bin/env python3
"""
Bulk DUX Object Validation Harness

This script reads a JSON file containing a collection of DUX objects 
(e.g., from a prototype or a large extraction run) and validates each 
object against its corresponding schema using the individual validation scripts.
"""

import os
import json
import subprocess
import sys
from pathlib import Path

# --- Configuration ---
# Get the directory of the script to build absolute paths
SCRIPT_DIR = Path(__file__).parent.resolve()
ROOT_DIR = SCRIPT_DIR.parent.parent
VALIDATION_DIR = SCRIPT_DIR

# The input file should be passed as a command-line argument
try:
    INPUT_JSON_PATH = Path(sys.argv[1])
except IndexError:
    print("❌ ERROR: Please provide the path to the input JSON file as a command-line argument.")
    sys.exit(1)

# --- Main Logic ---

def get_object_type(obj: dict) -> str:
    """Determine the object type from the object's data."""
    # Assumption: Each object has a key like 'object_type' or can be inferred
    # from its structure. Let's check for a common key first.
    if 'object_type' in obj:
        return obj['object_type'].lower()
    
    # Add other inference rules if needed, e.g., checking for unique keys
    if 'measurable_signal' in obj and 'frequency' in obj:
        return 'behavior'
    if 'measurable_signal' in obj and 'impact' in obj:
        return 'result'
    if 'justification' in obj and 'evidence_status' in obj:
        return 'insight'
    if 'job_to_be_done' in obj:
        return 'problem'
        
    return None

def main():
    """Main validation function."""
    print(f"\n=== Starting Bulk Validation for: {INPUT_JSON_PATH.name} ===")

    if not INPUT_JSON_PATH.exists():
        print(f"❌ ERROR: Input file not found at: {INPUT_JSON_PATH}")
        return

    with open(INPUT_JSON_PATH, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError as e:
            print(f"❌ ERROR: Invalid JSON in the input file. {e}")
            return

    # The structure might be a list of objects, or a dict containing lists
    objects_to_validate = []
    if isinstance(data, list):
        objects_to_validate = data
    elif isinstance(data, dict) and 'objects' in data and isinstance(data['objects'], dict):
        # Handle the structure from dux_processor.py: {"objects": {"problem": [...]}}
        for obj_list in data['objects'].values():
            objects_to_validate.extend(obj_list)
    elif isinstance(data, dict):
        # Handle structure like: {"problem": [...], "behavior": [...]}
        is_object_collection = True
        for key, value in data.items():
            if not isinstance(value, list):
                is_object_collection = False
                break
        if is_object_collection:
            for obj_list in data.values():
                objects_to_validate.extend(obj_list)
        else:
            print("❌ ERROR: Unsupported JSON structure. Expected a list of objects or a dict with an 'objects' key.")
            return
    else:
        print("❌ ERROR: Unsupported JSON structure. Expected a list of objects or a dict with an 'objects' key.")
        return

    print(f"Found {len(objects_to_validate)} total objects to validate.")

    valid_objects = {}
    invalid_objects = {}
    validation_summary = {}

    # Create a temporary directory to write individual objects for validation
    temp_dir = ROOT_DIR / "temp_validation_objects"
    temp_dir.mkdir(exist_ok=True)

    for i, obj in enumerate(objects_to_validate):
        obj_type = get_object_type(obj)
        if not obj_type:
            print(f"⚠️  Skipping object {i+1} - Could not determine type.")
            continue

        validator_script = VALIDATION_DIR / f"validate_{obj_type}.py"
        if not validator_script.exists():
            print(f"⚠️  Skipping object {i+1} of type '{obj_type}' - Validator script not found: {validator_script.name}")
            continue
            
        # Write the single object to a temporary file
        temp_obj_path = temp_dir / f"temp_{obj_type}_{i}.json"
        with open(temp_obj_path, 'w') as f:
            json.dump(obj, f, indent=2)

        # Run the specific validator script on the temporary file
        # We need to pass the file path to the script
        result = subprocess.run(
            [sys.executable, str(validator_script), str(temp_obj_path)],
            capture_output=True, text=True
        )
        
        # Initialize counters
        if obj_type not in validation_summary:
            validation_summary[obj_type] = {'valid': 0, 'invalid': 0}
            valid_objects[obj_type] = []
            invalid_objects[obj_type] = []

        if result.returncode == 0:
            validation_summary[obj_type]['valid'] += 1
            valid_objects[obj_type].append(obj)
        else:
            validation_summary[obj_type]['invalid'] += 1
            invalid_objects[obj_type].append({
                "object": obj,
                "error": result.stdout or result.stderr
            })

    # --- Report Results ---
    print("\n=== Validation Summary ===")
    for obj_type, counts in validation_summary.items():
        total = counts['valid'] + counts['invalid']
        print(f"  - {obj_type.capitalize()}: {counts['valid']} valid, {counts['invalid']} invalid (out of {total})")

    # Save the results to output files
    output_dir = ROOT_DIR / "validation_results"
    output_dir.mkdir(exist_ok=True)
    
    with open(output_dir / "valid_objects.json", 'w') as f:
        json.dump(valid_objects, f, indent=2)
        
    with open(output_dir / "invalid_objects.json", 'w') as f:
        json.dump(invalid_objects, f, indent=2)

    print(f"\n✅ Bulk validation complete. Results saved in: {output_dir}")
    
    # Clean up temporary files
    for temp_file in temp_dir.glob("*.json"):
        os.remove(temp_file)
    os.rmdir(temp_dir)


if __name__ == "__main__":
    main()
