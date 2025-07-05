"""
Shared Configuration for DUX Object Model Validation Scripts

This module provides centralized configuration and references to documentation
files to ensure consistency across all validation scripts.

References:
- docs/100_START_HERE/dux_object_template.md - Template structure
- docs/infrastructure_as_code/GOVERNANCE_NAMING_CONVENTIONS.md - Naming rules
- src/dux_v9.6_split_schema/ - Schema definitions
"""

from pathlib import Path

# Documentation file paths
TEMPLATE_PATH = Path("docs/100_START_HERE/dux_object_template.md")
GOVERNANCE_NAMING_PATH = Path("docs/infrastructure_as_code/GOVERNANCE_NAMING_CONVENTIONS.md")
SCHEMA_DIR = Path("src/dux_v9.6_split_schema")

# Naming conventions from GOVERNANCE_NAMING_CONVENTIONS.md
OBJECT_TYPE_PATTERNS = {
    "Behavior": r"^behavior_.*",
    "Flow": r"^flow_.*", 
    "Insight": r"^insight_.*",
    "Problem": r"^problem_.*",
    "Provenance": r"^prov_.*",
    "Result": r"^result_.*",
    "UserOutcome": r"^useroutcome_.*"
}

# Schema object types (exact values)
SCHEMA_OBJECT_TYPES = [
    "Behavior", "Flow", "Insight", "Problem", 
    "Provenance", "Result", "UserOutcome"
]

# Validation script execution order (alphabetical)
VALIDATION_SCRIPTS = [
    "validate_behavior_objects.py",
    "validate_flow_objects.py", 
    "validate_insight_objects.py",
    "validate_problem_objects.py",
    "validate_provenance_objects.py",
    "validate_result_objects.py",
    "validate_useroutcome_objects.py"
]

def get_schema_path(object_type: str) -> Path:
    """Get the schema file path for a given object type."""
    return SCHEMA_DIR / f"dux_object_{object_type.lower()}.json"

def validate_documentation_files():
    """Check if required documentation files exist."""
    missing_files = []
    
    if not TEMPLATE_PATH.exists():
        missing_files.append(str(TEMPLATE_PATH))
    
    if not GOVERNANCE_NAMING_PATH.exists():
        missing_files.append(str(GOVERNANCE_NAMING_PATH))
    
    if not SCHEMA_DIR.exists():
        missing_files.append(str(SCHEMA_DIR))
    
    if missing_files:
        print("Warning: Missing documentation files:")
        for file in missing_files:
            print(f"  - {file}")
        return False
    
    return True 