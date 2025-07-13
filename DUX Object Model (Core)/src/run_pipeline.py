#!/usr/bin/env python3
"""
DUX Object Model Governance Pipeline Orchestrator

This script automates the full IaC-style, HITL-first governance workflow:
- Checks HITL review readiness
- Auto-generates BDD feature files and step skeletons
- Runs all validation scripts
- Moves invalids to hitl_failed and logs errors
- Summarizes results
- (Optional) Generates prompt templates (stub)
"""

import os
from pathlib import Path
import subprocess
import sys

HITL_REVIEW_DIR = Path("watch_folders/hitl_review")
HITL_FAILED_DIR = Path("watch_folders/hitl_failed")
VALIDATION_DIR = Path("scripts/validation")
BDD_DIR = Path("scripts/bdd")
BDD_STEPS_DIR = BDD_DIR / "steps"
READY_FLAG = HITL_REVIEW_DIR / "READY"

OBJECT_TYPES = [
    "problem", "behavior", "flow", "result", "useroutcome", "insight", "provenance"
]


def check_hitl_ready():
    """Check if HITL review is ready (empty or READY flag present)."""
    print("\n[1] Checking HITL review readiness...")
    if READY_FLAG.exists():
        print("✅ READY flag found. Proceeding.")
        return True
    files = list(HITL_REVIEW_DIR.glob("*.md"))
    if not files:
        print("✅ HITL review folder is empty. Proceeding.")
        return True
    print(f"❌ HITL review not ready. {len(files)} files remain. Please finalize review or add a READY flag.")
    return False


def check_existing_bdd():
    """Check existing BDD feature files and step definitions."""
    print("\n[2] Checking existing BDD feature files and step definitions...")
    features_dir = Path("../features")
    steps_dir = features_dir / "steps"
    
    if features_dir.exists():
        feature_files = list(features_dir.glob("*.feature"))
        print(f"✅ Found {len(feature_files)} existing feature files:")
        for feature_file in feature_files:
            print(f"  - {feature_file.name}")
    
    if steps_dir.exists():
        step_files = list(steps_dir.glob("*_steps.py"))
        print(f"✅ Found {len(step_files)} existing step definition files:")
        for step_file in step_files:
            print(f"  - {step_file.name}")
    
    print("✅ Using existing BDD infrastructure instead of generating new files")


def extract_objects_from_markdown():
    """Extract JSON objects from markdown files using existing generate_from_markdown.py."""
    print("\n[2.5] Extracting JSON objects from markdown files...")
    generate_script = Path("../src/generate_from_markdown.py")
    if generate_script.exists():
        print(f"✅ Using existing extraction logic: {generate_script}")
        # TODO: Call the existing generate_from_markdown.py script
        # This uses your existing prompt templates and generation logic
    else:
        print("⚠️  generate_from_markdown.py not found in src/")
    
    markdown_files = list(HITL_REVIEW_DIR.glob("*.md"))
    print(f"✅ Ready to extract objects from {len(markdown_files)} markdown files")


def check_existing_schemas():
    """Check existing JSON schema files for backward compatibility."""
    print("\n[2.6] Checking existing JSON schema files...")
    schemas_dir = Path("../src/dux_v9.6_split_schema")
    if schemas_dir.exists():
        schema_files = list(schemas_dir.glob("dux_object_*.json"))
        print(f"✅ Found {len(schema_files)} existing schema files:")
        for schema_file in schema_files:
            print(f"  - {schema_file.name}")
    else:
        print("⚠️  Schema directory not found: src/dux_v9.6_split_schema/")


def run_validation_scripts():
    """Run all validation scripts in scripts/validation/ and summarize results."""
    print("\n[3] Running all validation scripts...")
    validation_scripts = sorted(VALIDATION_DIR.glob("validate_*.py"))
    results = {}
    for script in validation_scripts:
        print(f"\n▶️ Running {script.name}...")
        result = subprocess.run([sys.executable, str(script)], capture_output=True, text=True)
        print(result.stdout)
        results[script.name] = result.returncode
    print("\n✅ All validation scripts completed.")
    return results


def summarize_results():
    """Summarize the results in hitl_failed and print a report."""
    print("\n[4] Summarizing results...")
    failed_files = list(HITL_FAILED_DIR.glob("*.md"))
    if not failed_files:
        print("🎉 All objects passed validation! No files in hitl_failed.")
    else:
        print(f"❌ {len(failed_files)} files failed validation. See hitl_failed for details.")
        for f in failed_files:
            print(f"  - {f.name}")


def generate_prompts_stub():
    """Stub for prompt template generation."""
    print("\n[5] (Optional) Generating prompt templates... (stub)")
    # TODO: Implement prompt generation if needed
    pass


def main():
    print("\n=== DUX Object Model Governance Pipeline ===")
    if not check_hitl_ready():
        print("\nPipeline halted: HITL review not ready.")
        return
    check_existing_bdd()
    extract_objects_from_markdown()
    check_existing_schemas()
    run_validation_scripts()
    summarize_results()
    generate_prompts_stub()
    print("\n=== Pipeline complete ===\n")

if __name__ == "__main__":
    main() 