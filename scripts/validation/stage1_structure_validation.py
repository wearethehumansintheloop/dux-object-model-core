#!/usr/bin/env python3
"""
Stage 1: Structure & Template Validation

Validates that markdown files follow the DUX object template format:
- Required sections present
- Schema Attributes table exists
- Canonical Example JSON block exists
- Basic structural integrity
"""

import re
from pathlib import Path
from typing import Dict, List, Any, Optional


def validate_dux_template_structure(content: str) -> List[str]:
    """
    Validate that markdown follows DUX object template structure.
    
    Returns:
        List of validation errors (empty if valid)
    """
    errors = []
    
    # Required sections for DUX object template
    required_sections = {
        "Purpose & Strategic Role": r"## 🎯 Purpose & Strategic Role",
        "What would you say": r"## 🧠 \"What would you say",
        "Why the Object Matters": r"## 💡 Why the .* Object Matters",
        "Schema Attributes": r"## 📋 Schema Attributes",
        "Canonical Example": r"## 📦 Canonical Example",
        "Structural Role": r"## 🔗 Structural Role"
    }
    
    # Check for required sections
    for section_name, pattern in required_sections.items():
        if not re.search(pattern, content, re.IGNORECASE):
            errors.append(f"Missing required section: {section_name}")
    
    # Check for Schema Attributes table
    if "Schema Attributes" in content:
        # Look for table structure
        table_pattern = r'## 📋 Schema Attributes\s*\n.*?\|.*?Attribute.*?\|.*?Type.*?\|.*?Required.*?\|'
        if not re.search(table_pattern, content, re.DOTALL):
            errors.append("Schema Attributes section missing proper table structure")
    
    # Check for JSON block in Canonical Example
    if "Canonical Example" in content:
        json_pattern = r'```json\s*\n.*?\n```'
        if not re.search(json_pattern, content, re.DOTALL):
            errors.append("Canonical Example section missing JSON block")
    
    # Check for object type in title
    object_type_pattern = r'# .* (Problem|Behavior|Result|UserOutcome|Flow|Insight|Provenance) Object'
    if not re.search(object_type_pattern, content):
        errors.append("Title must specify object type (Problem, Behavior, Result, etc.)")
    
    return errors


def validate_schema_attributes_table(content: str) -> List[str]:
    """
    Validate Schema Attributes table structure and content.
    
    Returns:
        List of validation errors (empty if valid)
    """
    errors = []
    
    # Extract schema section
    schema_pattern = r'## 📋 Schema Attributes\s*\n(.*?)(?=\n## |\Z)'
    schema_match = re.search(schema_pattern, content, re.DOTALL)
    
    if not schema_match:
        errors.append("Schema Attributes section not found")
        return errors
    
    schema_section = schema_match.group(1)
    
    # Check for required core attributes
    required_attrs = ['object_type', 'id']
    for attr in required_attrs:
        if attr not in schema_section:
            errors.append(f"Missing required attribute in table: {attr}")
    
    # Check table format
    if not re.search(r'\|.*?Attribute.*?\|.*?Type.*?\|.*?Required.*?\|', schema_section):
        errors.append("Schema table missing proper headers (Attribute, Type, Required)")
    
    # Check for separator line
    if not re.search(r'\|[-\s|:]+\|', schema_section):
        errors.append("Schema table missing separator line")
    
    return errors


def validate_canonical_example(content: str) -> List[str]:
    """
    Validate Canonical Example JSON structure.
    
    Returns:
        List of validation errors (empty if valid)
    """
    errors = []
    
    # Extract JSON blocks
    json_pattern = r'```json\s*\n(.*?)\n```'
    json_matches = re.findall(json_pattern, content, re.DOTALL)
    
    if not json_matches:
        errors.append("No JSON block found in Canonical Example")
        return errors
    
    # Basic JSON validation
    import json
    for i, json_text in enumerate(json_matches):
        try:
            json_obj = json.loads(json_text.strip())
            
            # Check for object_type
            if 'object_type' not in json_obj:
                errors.append(f"JSON block {i+1}: Missing object_type field")
            
            # Check for id
            if 'id' not in json_obj:
                errors.append(f"JSON block {i+1}: Missing id field")
            
        except json.JSONDecodeError as e:
            errors.append(f"JSON block {i+1}: Invalid JSON format - {str(e)}")
    
    return errors


def process_file_stage1(file_path: Path) -> Dict[str, Any]:
    """
    Process a single file through Stage 1 validation.
    
    Returns:
        Validation result dictionary
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return {
            "valid": False,
            "stage": "stage1_structure",
            "errors": [f"Failed to read file: {e}"]
        }
    
    errors = []
    
    # Run all Stage 1 validations
    errors.extend(validate_dux_template_structure(content))
    errors.extend(validate_schema_attributes_table(content))
    errors.extend(validate_canonical_example(content))
    
    return {
        "valid": len(errors) == 0,
        "stage": "stage1_structure",
        "errors": errors
    }


def main():
    """Test Stage 1 validation on current review files."""
    print("🔍 Stage 1: Structure & Template Validation")
    print("=" * 50)
    
    review_dir = Path("watch_folders/hitl_review")
    if not review_dir.exists():
        print(f"❌ Review directory not found: {review_dir}")
        return
    
    markdown_files = list(review_dir.glob("*.md"))
    if not markdown_files:
        print("📭 No markdown files found")
        return
    
    for file_path in markdown_files:
        result = process_file_stage1(file_path)
        
        print(f"\n📁 {file_path.name}")
        print(f"✅ Stage 1 Valid: {result['valid']}")
        
        if result['errors']:
            print(f"❌ Errors ({len(result['errors'])}):")
            for error in result['errors']:
                print(f"  - {error}")
        else:
            print("✅ All Stage 1 checks passed")


if __name__ == "__main__":
    main()