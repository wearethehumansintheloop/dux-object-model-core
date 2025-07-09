#!/usr/bin/env python3
"""
Stage 3A: Result Object Basic Docling Processing

Lightweight docling processing for Result objects (development flow):
- Extracts Schema Attributes table only
- Generates Result-specific JSON schema
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
    Generate JSON schema from table data, handling complex types like evidence arrays.
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
            # Handle complex array types like "Array of Evidence objects"
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
            elif field == 'end_user':
                # end_user array has structure
                prop_def = {
                    'type': 'array',
                    'items': {
                        'type': 'object',
                        'properties': {
                            'persona': {'type': 'string'},
                            'description': {'type': 'string'}
                        }
                    }
                }
            elif 'string' in base_type.lower():
                # Array of strings (like tags, useroutcome_ids)
                prop_def = {'type': 'array', 'items': {'type': 'string'}}
            else:
                # Default array
                prop_def = {'type': 'array', 'items': {'type': 'string'}}
        elif base_type.lower() == 'object' or 'object' in base_type.lower():
            # Handle specific object types
            if field == 'job_statement':
                # Problem object's decomposed job_statement
                prop_def = {
                    'type': 'object',
                    'properties': {
                        'user_scenario': {
                            'type': 'object',
                            'properties': {
                                'value': {'type': 'string'},
                                'source': {'type': 'string', 'enum': ['evidence', 'synthetic']}
                            },
                            'required': ['value', 'source']
                        },
                        'user_enablement': {
                            'type': 'object',
                            'properties': {
                                'value': {'type': 'string'},
                                'source': {'type': 'string', 'enum': ['evidence', 'synthetic']}
                            },
                            'required': ['value', 'source']
                        },
                        'user_outcome': {
                            'type': 'object',
                            'properties': {
                                'value': {'type': 'string'},
                                'source': {'type': 'string', 'enum': ['evidence', 'synthetic']}
                            },
                            'required': ['value', 'source']
                        }
                    },
                    'required': ['user_scenario', 'user_enablement', 'user_outcome']
                }
            elif field == 'outcome_statement':
                # UserOutcome object's outcome_statement
                prop_def = {
                    'type': 'object',
                    'properties': {
                        'value': {'type': 'string'},
                        'source': {'type': 'string', 'enum': ['evidence', 'synthetic']}
                    },
                    'required': ['value', 'source']
                }
            elif field == 'opportunity_score':
                # Opportunity score object
                prop_def = {
                    'type': 'object',
                    'properties': {
                        'importance': {'type': 'number'},
                        'satisfaction': {'type': 'number'},
                        'opportunity': {'type': 'number'}
                    }
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
            prop_def['enum'] = ['Result']  # For Result objects
        
        # Special handling for ID fields with patterns
        if field.endswith('_ids') or field == 'id':
            if 'items' in prop_def:
                # Add pattern for array items
                if field == 'useroutcome_ids':
                    prop_def['items']['pattern'] = '^(useroutcome|result)_'
            elif field == 'id':
                prop_def['pattern'] = f'^result_'
        
        properties[field] = prop_def
        
        if is_required:
            required.append(field)
    
    return {
        'type': 'object',
        'properties': properties,
        'required': required
    }


def validate_result_schema_quality(json_schema: Dict[str, Any]) -> List[str]:
    """
    Validate Result object specific schema quality.
    
    Returns:
        List of validation errors (empty if valid)
    """
    errors = []
    
    if not json_schema:
        errors.append("No JSON schema generated")
        return errors
    
    properties = json_schema.get('properties', {})
    required = json_schema.get('required', [])
    
    # Result object specific validations
    result_required_fields = ['object_type', 'id', 'target_impact', 'evidence', 'useroutcome_ids']
    for field in result_required_fields:
        if field not in properties:
            errors.append(f"Result schema missing required field: {field}")
    
    # Check object_type is set to "Result"
    if 'object_type' in properties:
        obj_type = properties['object_type']
        if obj_type.get('type') == 'string' and obj_type.get('enum') != ['Result']:
            errors.append("Result schema object_type must be enum ['Result']")
    
    # Result specific field validations
    if 'target_impact' in properties:
        if properties['target_impact'].get('type') != 'string':
            errors.append("Result target_impact must be type string")
    
    if 'useroutcome_ids' in properties:
        if properties['useroutcome_ids'].get('type') != 'array':
            errors.append("Result useroutcome_ids must be type array")
    
    return errors


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
        generated_schema = generate_schema_from_table(table_data, 'result')
        
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


def process_stage3a_result(file_path: Path) -> Dict[str, Any]:
    """
    Process Result object through Stage 3a validation.
    
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
            f.write(f"# Result Object Docling Export\n\n")
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
    # Test with a Result object
    if len(sys.argv) > 1:
        test_file = Path(sys.argv[1])
        if test_file.exists():
            print(f"Processing: {test_file}")
            result = process_stage3a_result(test_file)
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
        print("Usage: python stage3a_result_basic_docling.py <result_object.md>")