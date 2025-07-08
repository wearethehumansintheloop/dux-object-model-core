#!/usr/bin/env python3
"""
Stage 2: Consistency Validation

Validates consistency between schema table and JSON example:
- Schema table attributes match JSON example fields
- Types are compatible between table and example
- Required fields present in JSON example
- No extra fields in JSON that aren't in schema table
"""

import json
import re
from pathlib import Path
from typing import Dict, List, Any, Optional, Set


def extract_schema_attributes(content: str) -> Optional[Dict[str, Dict[str, str]]]:
    """
    Extract schema attributes from markdown table.
    
    Returns:
        Dict mapping attribute names to their properties (type, required, description)
    """
    # Find Schema Attributes section
    schema_pattern = r'## 📋 Schema Attributes\s*\n(.*?)(?=\n## |\Z)'
    schema_match = re.search(schema_pattern, content, re.DOTALL)
    
    if not schema_match:
        return None
    
    schema_section = schema_match.group(1)
    lines = schema_section.split('\n')
    
    # Find table start
    table_start = -1
    for i, line in enumerate(lines):
        if '|' in line and 'Attribute' in line:
            table_start = i
            break
    
    if table_start == -1:
        return None
    
    # Parse headers
    header_line = lines[table_start]
    headers = [h.strip() for h in header_line.split('|') if h.strip()]
    
    # Parse rows
    attributes = {}
    for line in lines[table_start + 2:]:  # Skip separator line
        line = line.strip()
        if not line or not line.startswith('|'):
            continue
        
        cells = [cell.strip() for cell in line[1:-1].split('|')]
        if len(cells) >= 3:  # At least Attribute, Type, Required
            attr_name = cells[0]
            attr_type = cells[1]
            required = cells[2]
            description = cells[3] if len(cells) > 3 else ""
            
            attributes[attr_name] = {
                'type': attr_type,
                'required': required,
                'description': description
            }
    
    return attributes


def extract_json_example(content: str) -> Optional[Dict[str, Any]]:
    """
    Extract JSON example from Canonical Example section.
    
    Returns:
        Parsed JSON object or None if not found
    """
    json_pattern = r'```json\s*\n(.*?)\n```'
    json_matches = re.findall(json_pattern, content, re.DOTALL)
    
    if not json_matches:
        return None
    
    # Use first JSON block
    try:
        return json.loads(json_matches[0].strip())
    except json.JSONDecodeError:
        return None


def validate_type_compatibility(schema_type: str, json_value: Any) -> bool:
    """
    Check if JSON value is compatible with schema type.
    
    Returns:
        True if compatible, False otherwise
    """
    if schema_type == 'string':
        return isinstance(json_value, str)
    elif schema_type == 'number':
        return isinstance(json_value, (int, float))
    elif schema_type == 'boolean':
        return isinstance(json_value, bool)
    elif schema_type == 'object':
        return isinstance(json_value, dict)
    elif schema_type.startswith('[') and schema_type.endswith(']'):
        # Array type
        if not isinstance(json_value, list):
            return False
        inner_type = schema_type[1:-1]
        if inner_type == 'string':
            return all(isinstance(item, str) for item in json_value)
        elif inner_type == 'object':
            return all(isinstance(item, dict) for item in json_value)
        elif inner_type == 'number':
            return all(isinstance(item, (int, float)) for item in json_value)
        return True
    else:
        # Unknown type, assume compatible
        return True


def validate_schema_json_consistency(schema_attrs: Dict[str, Dict[str, str]], 
                                   json_example: Dict[str, Any]) -> List[str]:
    """
    Validate consistency between schema table and JSON example.
    
    Returns:
        List of validation errors (empty if valid)
    """
    errors = []
    
    # Check required fields are present in JSON
    for attr_name, attr_info in schema_attrs.items():
        if attr_info['required'].lower() == 'yes':
            if attr_name not in json_example:
                errors.append(f"Required field '{attr_name}' missing from JSON example")
    
    # Check JSON fields exist in schema
    for json_field in json_example.keys():
        if json_field not in schema_attrs:
            errors.append(f"JSON field '{json_field}' not defined in schema table")
    
    # Check type compatibility
    for attr_name, attr_info in schema_attrs.items():
        if attr_name in json_example:
            json_value = json_example[attr_name]
            schema_type = attr_info['type']
            
            if not validate_type_compatibility(schema_type, json_value):
                errors.append(f"Type mismatch for '{attr_name}': schema expects {schema_type}, JSON has {type(json_value).__name__}")
    
    return errors


def process_file_stage2(file_path: Path) -> Dict[str, Any]:
    """
    Process a single file through Stage 2 validation.
    
    Returns:
        Validation result dictionary
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return {
            "valid": False,
            "stage": "stage2_consistency",
            "errors": [f"Failed to read file: {e}"]
        }
    
    errors = []
    
    # Extract schema attributes
    schema_attrs = extract_schema_attributes(content)
    if not schema_attrs:
        errors.append("Could not extract schema attributes from table")
        return {
            "valid": False,
            "stage": "stage2_consistency",
            "errors": errors
        }
    
    # Extract JSON example
    json_example = extract_json_example(content)
    if not json_example:
        errors.append("Could not extract JSON example")
        return {
            "valid": False,
            "stage": "stage2_consistency",
            "errors": errors
        }
    
    # Validate consistency
    errors.extend(validate_schema_json_consistency(schema_attrs, json_example))
    
    return {
        "valid": len(errors) == 0,
        "stage": "stage2_consistency",
        "errors": errors,
        "schema_attrs": schema_attrs,
        "json_example": json_example
    }


def validate_consistency(content: str) -> Dict[str, Any]:
    """
    Main validation function called by the orchestrator.
    
    Args:
        content: File content to validate
        
    Returns:
        Validation result dictionary
    """
    errors = []
    
    # Extract schema attributes
    schema_attrs = extract_schema_attributes(content)
    if not schema_attrs:
        errors.append("Could not extract schema attributes from table")
        return {
            "valid": False,
            "stage": "stage2_consistency",
            "errors": errors
        }
    
    # Extract JSON example
    json_example = extract_json_example(content)
    if not json_example:
        errors.append("Could not extract JSON example")
        return {
            "valid": False,
            "stage": "stage2_consistency",
            "errors": errors
        }
    
    # Validate consistency
    errors.extend(validate_schema_json_consistency(schema_attrs, json_example))
    
    return {
        "valid": len(errors) == 0,
        "stage": "stage2_consistency",
        "errors": errors,
        "schema_attrs": schema_attrs,
        "json_example": json_example
    }


def main():
    """Test Stage 2 validation on current review files."""
    print("🔍 Stage 2: Consistency Validation")
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
        result = process_file_stage2(file_path)
        
        print(f"\n📁 {file_path.name}")
        print(f"✅ Stage 2 Valid: {result['valid']}")
        
        if result['errors']:
            print(f"❌ Errors ({len(result['errors'])}):")
            for error in result['errors']:
                print(f"  - {error}")
        else:
            print("✅ Schema table and JSON example are consistent")
            
        if 'schema_attrs' in result:
            print(f"📋 Schema attributes: {len(result['schema_attrs'])}")
        if 'json_example' in result:
            print(f"📦 JSON fields: {len(result['json_example'])}")


if __name__ == "__main__":
    main()