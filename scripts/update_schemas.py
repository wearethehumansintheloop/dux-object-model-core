#!/usr/bin/env python3
"""
Schema Update Pipeline for DUX v9.6
Updates JSON schemas and validation scripts to reflect new schema changes.
"""

import json
import os
import shutil
from pathlib import Path

def update_useroutcome_schema():
    """Update UserOutcome schema with new structure."""
    schema = {
        "type": "object",
        "properties": {
            "object_type": {"type": "string", "const": "UserOutcome"},
            "id": {"type": "string"},
            "behavior_id": {"type": "string"},
            "result_id": {"type": "string"},
            "end_user": {"type": "string"},
            "user_flow_id": {"type": "string"},
            "key_signals": {"type": "array", "items": {"type": "string"}},
            "acceptance_criteria": {"type": "array", "items": {"type": "string"}},
            "outcome_statement": {"type": "string"},
            "evidence": {"type": "array", "items": {"type": "string"}},
            "tags": {"type": "array", "items": {"type": "string"}},
            "created_at": {"type": "string"},
            "updated_at": {"type": "string"}
        },
        "required": ["object_type", "id", "behavior_id", "result_id", "end_user", "acceptance_criteria", "outcome_statement", "evidence"]
    }
    return schema

def update_behavior_schema():
    """Update Behavior schema with end_user and without behavior_type."""
    schema = {
        "type": "object",
        "properties": {
            "object_type": {"type": "string", "const": "Behavior"},
            "id": {"type": "string"},
            "user_enablement": {"type": "string"},
            "end_user": {"type": "string"},
            "signals": {"type": "array", "items": {"type": "string"}},
            "acceptance_criteria": {"type": "array", "items": {"type": "string"}},
            "evidence": {"type": "array", "items": {"type": "string"}},
            "tags": {"type": "array", "items": {"type": "string"}},
            "created_at": {"type": "string"},
            "updated_at": {"type": "string"}
        },
        "required": ["object_type", "id", "user_enablement", "end_user", "signals", "acceptance_criteria", "evidence"]
    }
    return schema

def update_result_schema():
    """Update Result schema with clarified success_criteria and success_metrics."""
    schema = {
        "type": "object",
        "properties": {
            "object_type": {"type": "string", "const": "Result"},
            "id": {"type": "string"},
            "target_impact": {"type": "string"},
            "success_criteria": {"type": "string"},
            "success_metrics": {"type": "array", "items": {"type": "string"}},
            "evidence": {"type": "array", "items": {"type": "string"}},
            "useroutcome_ids": {"type": "array", "items": {"type": "string"}},
            "tags": {"type": "array", "items": {"type": "string"}},
            "created_at": {"type": "string"},
            "updated_at": {"type": "string"}
        },
        "required": ["object_type", "id", "target_impact", "evidence"]
    }
    return schema

def update_userflow_schema():
    """Update UserFlow schema as Problem × UserOutcome junction."""
    schema = {
        "type": "object",
        "properties": {
            "object_type": {"type": "string", "const": "UserFlow"},
            "user_flow_id": {"type": "string"},
            "title": {"type": "string"},
            "description": {"type": "string"},
            "problem_id": {"type": "string"},
            "user_outcome_id": {"type": "string"},
            "behavior_sequence": {"type": "array", "items": {"type": "string"}},
            "evidence": {"type": "array", "items": {"type": "string"}},
            "reference_url": {"type": "string"},
            "created_at": {"type": "string"},
            "updated_at": {"type": "string"},
            "tags": {"type": "array", "items": {"type": "string"}}
        },
        "required": ["object_type", "user_flow_id", "title", "description", "problem_id", "user_outcome_id", "behavior_sequence"]
    }
    return schema

def update_meta_schema():
    """Update meta schema to reflect new object relationships."""
    schema = {
        "type": "object",
        "properties": {
            "version": {"type": "string", "const": "v9.6"},
            "objects": {
                "type": "object",
                "properties": {
                    "UserOutcome": {"$ref": "dux_object_useroutcome.json"},
                    "Behavior": {"$ref": "dux_object_behavior.json"},
                    "Result": {"$ref": "dux_object_result.json"},
                    "UserFlow": {"$ref": "dux_object_flow.json"},
                    "Problem": {"$ref": "dux_object_problem.json"},
                    "Provenance": {"$ref": "dux_object_provenance.json"}
                }
            }
        }
    }
    return schema

def write_schema_file(schema, filename):
    """Write schema to JSON file."""
    schema_dir = Path("src/dux_v9.6_split_schema")
    schema_dir.mkdir(exist_ok=True)
    
    filepath = schema_dir / filename
    with open(filepath, 'w') as f:
        json.dump(schema, f, indent=2)
    print(f"Updated schema: {filepath}")

def update_validation_scripts():
    """Update validation scripts to reflect new schema changes."""
    # This would involve updating the validation logic in each script
    # For now, we'll just note which scripts need updates
    scripts_to_update = [
        "validate_useroutcome_objects.py",
        "validate_behavior_objects.py", 
        "validate_result_objects.py",
        "validate_flow_objects.py"
    ]
    
    print("Validation scripts that need manual updates:")
    for script in scripts_to_update:
        print(f"  - scripts/validation/{script}")

def run_bdd_validation():
    """Run BDD tests to validate schema updates."""
    import subprocess
    import sys
    
    print("\n🧪 Running BDD validation tests...")
    
    # List of BDD features to run
    bdd_features = [
        "features/schema_update_validation.feature",
        "features/signal_flow_validation.feature",
        "features/insight_object_pattern_validation.feature",
        "features/dux_schema_validation.feature"
    ]
    
    all_passed = True
    
    for feature in bdd_features:
        print(f"\n📋 Running {feature}...")
        try:
            result = subprocess.run([
                sys.executable, "-m", "behave", feature
            ], capture_output=True, text=True, cwd=Path.cwd().parent)
            
            if result.returncode == 0:
                print(f"✅ {feature} passed!")
            else:
                print(f"❌ {feature} failed!")
                print("Error output:")
                print(result.stderr)
                print("Standard output:")
                print(result.stdout)
                all_passed = False
                
        except Exception as e:
            print(f"❌ Error running {feature}: {e}")
            all_passed = False
    
    if all_passed:
        print("\n🎉 All BDD validation tests passed!")
    else:
        print("\n⚠️  Some BDD validation tests failed. Please review the output above.")

def main():
    """Main function to update all schemas."""
    print("🔄 Updating DUX v9.6 schemas...")
    
    # Update JSON schemas
    write_schema_file(update_useroutcome_schema(), "dux_object_useroutcome.json")
    write_schema_file(update_behavior_schema(), "dux_object_behavior.json")
    write_schema_file(update_result_schema(), "dux_object_result.json")
    write_schema_file(update_userflow_schema(), "dux_object_flow.json")
    write_schema_file(update_meta_schema(), "dux_meta_schema.json")
    
    # Note about validation scripts
    update_validation_scripts()
    
    # Run BDD validation
    run_bdd_validation()
    
    print("✅ Schema update complete!")
    print("📝 Next steps:")
    print("  1. Review updated JSON schemas")
    print("  2. Update validation scripts manually")
    print("  3. Review BDD test results")
    print("  4. Test with sample data")
    print("  5. Update prompt templates if needed")

if __name__ == "__main__":
    main() 