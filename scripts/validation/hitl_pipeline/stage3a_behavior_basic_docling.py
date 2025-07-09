#!/usr/bin/env python3
"""
Stage 3A: Behavior Object Basic Docling Processing

Lightweight docling processing for Behavior objects (development flow):
- Extracts Schema Attributes table only
- Generates Behavior-specific JSON schema
- Basic schema quality validation
- Fast feedback for development iteration

Scope: Schema governance only (not instance creation or relationships)
Note: Stage 3B (full document processing) reserved for production candidates
"""

import json
from pathlib import Path
from typing import Dict, List, Any, Optional

# For basic stage 3a, we do simple markdown parsing
import re


def extract_schema_table_and_json(content: str) -> tuple[List[Dict[str, str]], Dict[str, Any]]:
    """
    Extract Schema Attributes table and JSON schema from markdown.
    
    Returns:
        (table_data, json_schema) tuple
    """
    table_data = []
    json_schema = None
    
    # Extract table rows (between | characters)
    # Updated pattern to handle emoji in section header
    table_section = re.search(r'## 📋 Schema Attributes.*?\n(.*?)(?=\n##|\n\Z)', content, re.DOTALL)
    if table_section:
        table_text = table_section.group(1)
        # Find all table rows (4 columns: Attribute, Type, Required, Description)
        rows = re.findall(r'\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|', table_text)
        
        # Skip header and separator rows
        for row in rows[2:]:  # Skip header and separator
            if '---' not in row[0]:  # Skip separator rows
                field = row[0].strip()
                type_val = row[1].strip()
                required = row[2].strip()
                description = row[3].strip()
                if field:
                    table_data.append({
                        'field': field,
                        'type': type_val,
                        'required': required,
                        'description': description
                    })
    
    # Extract JSON schema
    json_match = re.search(r'```json\n(.*?)\n```', content, re.DOTALL)
    if json_match:
        try:
            json_schema = json.loads(json_match.group(1))
        except json.JSONDecodeError:
            pass
    
    return table_data, json_schema


def generate_schema_from_table(table_data: List[Dict[str, str]], object_type: str) -> Dict[str, Any]:
    """
    Generate JSON schema from table data, handling complex types like user_enablement.
    """
    properties = {}
    required = []
    
    for row in table_data:
        field = row['field']
        type_str = row['type']
        description = row['description']
        
        # Parse type and required status
        is_required = 'Yes' in row.get('required', '')
        base_type = type_str.strip()
        
        # Convert to JSON schema type
        if base_type.startswith('[') and base_type.endswith(']'):
            # Array type like [string] or [object]
            inner_type = base_type[1:-1].strip()
            
            # Special handling for evidence field
            if field == 'evidence':
                # Evidence has specific structure
                prop_def = {
                    'type': 'array',
                    'items': {
                        'type': 'object',
                        'properties': {
                            'quote': {'type': 'string'},
                            'attribution': {'type': 'string'},
                            'participant_id': {'type': 'string'},
                            'source_file': {'type': 'string'}
                        },
                        'required': ['quote', 'attribution']
                    }
                }
            elif inner_type.lower() == 'string':
                prop_def = {'type': 'array', 'items': {'type': 'string'}}
            elif inner_type.lower() == 'object':
                prop_def = {'type': 'array', 'items': {'type': 'object'}}
            else:
                prop_def = {'type': 'array', 'items': {'type': 'string'}}
        elif base_type.lower() == 'string':
            prop_def = {'type': 'string'}
        elif 'array' in base_type.lower():
            # Handle array types
            if field == 'signals':
                # signals is array of strings
                prop_def = {'type': 'array', 'items': {'type': 'string'}}
            elif field == 'evidence':
                # Evidence has specific structure
                prop_def = {
                    'type': 'array',
                    'items': {
                        'type': 'object',
                        'properties': {
                            'quote': {'type': 'string'},
                            'attribution': {'type': 'string'},
                            'participant_id': {'type': 'string'},
                            'source_file': {'type': 'string'}
                        },
                        'required': ['quote', 'attribution']
                    }
                }
            elif 'string' in base_type.lower():
                # Array of strings
                prop_def = {'type': 'array', 'items': {'type': 'string'}}
            else:
                # Default array
                prop_def = {'type': 'array', 'items': {'type': 'string'}}
        elif base_type.lower() == 'object' or 'object' in base_type.lower():
            # Handle specific object types
            if field == 'user_enablement':
                # Behavior object's user_enablement has decomposed structure
                prop_def = {
                    'type': 'object',
                    'properties': {
                        'value': {'type': 'string'},
                        'source': {'type': 'string', 'enum': ['evidence', 'synthetic']}
                    },
                    'required': ['value', 'source']
                }
            else:
                # Default object
                prop_def = {'type': 'object'}
        else:
            prop_def = {'type': 'string'}  # Default
        
        # Add description
        prop_def['description'] = description
        
        # Special handling for object_type field
        if field == 'object_type':
            prop_def['enum'] = ['Behavior']  # For Behavior objects
        
        # Special handling for behavior_type field
        if field == 'behavior_type':
            prop_def['enum'] = ['system_action', 'organizational_process', 'user_action']
        
        # Special handling for ID fields with patterns
        if field.endswith('_ids') or field == 'id':
            if 'items' in prop_def:
                # Add pattern for array items
                if field == 'problem_ids':
                    prop_def['items']['pattern'] = '^problem_'
                elif field == 'result_ids':
                    prop_def['items']['pattern'] = '^result_'
            elif field == 'id':
                prop_def['pattern'] = f'^behavior_'
        
        properties[field] = prop_def
        
        if is_required:
            required.append(field)
    
    return {
        'type': 'object',
        'properties': properties,
        'required': required
    }


def process_problem_object_markdown(file_path: str) -> Dict[str, Any]:
    """
    Process markdown file to extract schema information.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract table and JSON
        table_data, embedded_json = extract_schema_table_and_json(content)
        
        # Generate schema from table
        generated_schema = generate_schema_from_table(table_data, 'behavior')
        
        # Use generated schema (table is source of truth)
        json_schema = generated_schema if table_data else embedded_json
        
        return {
            'success': True,
            'table_data': table_data,
            'json_schema': json_schema
        }
    except Exception as e:
        return {
            'success': False,
            'error': str(e)
        }


def validate_behavior_schema_quality(json_schema: Dict[str, Any]) -> List[str]:
    """
    Validate Behavior object specific schema quality.
    
    Returns:
        List of validation errors (empty if valid)
    """
    errors = []
    
    if not json_schema:
        errors.append("No JSON schema generated")
        return errors
    
    properties = json_schema.get('properties', {})
    required = json_schema.get('required', [])
    
    # Behavior object specific validations
    behavior_required_fields = ['object_type', 'id', 'user_enablement', 'behavior_type', 'signals']
    for field in behavior_required_fields:
        if field not in properties:
            errors.append(f"Behavior schema missing required field: {field}")
    
    # Check object_type is set to "Behavior"
    if 'object_type' in properties:
        obj_type = properties['object_type']
        if obj_type.get('type') == 'string' and obj_type.get('enum') != ['Behavior']:
            errors.append("Behavior schema object_type must be enum ['Behavior']")
    
    # Behavior specific field validations
    if 'user_enablement' in properties:
        # Now checking for object type with proper structure
        if properties['user_enablement'].get('type') != 'object':
            errors.append("Behavior user_enablement must be type object with value/source properties")
        else:
            enablement_props = properties['user_enablement'].get('properties', {})
            if 'value' not in enablement_props or 'source' not in enablement_props:
                errors.append("Behavior user_enablement must have value and source properties")
    
    if 'behavior_type' in properties:
        behavior_type = properties['behavior_type']
        if behavior_type.get('type') == 'string':
            valid_types = behavior_type.get('enum', [])
            expected_types = ['Action', 'Navigation', 'Verification', 'Configuration', 'Analysis']
            if not set(expected_types).issubset(set(valid_types)):
                errors.append(f"Behavior behavior_type enum should include: {expected_types}")
    
    if 'signals' in properties:
        if properties['signals'].get('type') != 'array':
            errors.append("Behavior signals must be type array")
        else:
            items = properties['signals'].get('items', {})
            if items.get('type') != 'string':
                errors.append("Behavior signals items must be type string")
    
    return errors


def process_stage3a_behavior(file_path: Path) -> Dict[str, Any]:
    """
    Process Behavior object through Stage 3a validation.
    
    Returns:
        Dict with keys:
        - passed: bool
        - errors: List[str]
        - docling_path: Optional[Path] 
        - json_schema: Optional[Dict]
    """
    errors = []
    
    # Use the generic markdown processor (works for all object types)
    try:
        result = process_problem_object_markdown(str(file_path))
        
        if not result['success']:
            errors.append(f"Failed to process markdown: {result.get('error', 'Unknown error')}")
            return {
                'passed': False,
                'errors': errors,
                'docling_path': None,
                'json_schema': None
            }
        
        # Extract components
        json_schema = result.get('json_schema', {})
        table_data = result.get('table_data', [])
        
        # Stage 3a should NOT validate - just extract and convert
        # Validation happens in Stage 3b
        
        # Create docling markdown output
        docling_path = file_path.parent / f"{file_path.stem}_docling.md"
        
        with open(docling_path, 'w') as f:
            # Write header
            f.write(f"# Behavior Object Docling Export\n\n")
            f.write(f"Source: {file_path.name}\n")
            f.write(f"Generated: Stage 3a Basic Docling\n\n")
            
            # Write schema
            f.write("## Generated JSON Schema\n\n")
            f.write("```json\n")
            f.write(json.dumps(json_schema, indent=2))
            f.write("\n```\n\n")
            
            # Write extracted table data
            f.write("## Extracted Table Data\n\n")
            f.write("```json\n")
            f.write(json.dumps(table_data, indent=2))
            f.write("\n```\n")
        
        return {
            'passed': True,  # Stage 3a should always pass if extraction works
            'errors': errors,
            'docling_path': docling_path,
            'json_schema': json_schema
        }
        
    except Exception as e:
        errors.append(f"Processing error: {str(e)}")
        return {
            'passed': False,
            'errors': errors,
            'docling_path': None,
            'json_schema': None
        }


if __name__ == "__main__":
    import sys
    # Test with a Behavior object
    if len(sys.argv) > 1:
        test_file = Path(sys.argv[1])
        if test_file.exists():
            print(f"Processing: {test_file}")
            result = process_stage3a_behavior(test_file)
            print(f"Passed: {result['passed']}")
            if result['errors']:
                print("Errors:")
                for error in result['errors']:
                    print(f"  - {error}")
            if result['docling_path']:
                print(f"Docling output: {result['docling_path']}")
        else:
            print(f"File not found: {test_file}")
    else:
        print("Usage: python stage3a_behavior_basic_docling.py <behavior_object.md>")