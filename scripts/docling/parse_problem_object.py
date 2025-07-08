#!/usr/bin/env python3
"""
Docling-based Problem Object Parser

This script implements the three-stage docling integration process:
1. Docling parse markdown → structured document
2. Validation check → ensure completeness/correctness  
3. JSON generation → create schema from validated structure

Specifically extracts Schema Attributes table from Problem object markdown
and generates corresponding JSON schema.
"""

import json
import re
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from docling.document_converter import DocumentConverter


def parse_schema_attributes_table(content: str) -> Optional[Dict[str, Any]]:
    """
    Extract and parse the Schema Attributes table from markdown content.
    
    Returns:
        Dict with parsed attributes or None if table not found
    """
    # Find the Schema Attributes section
    schema_section_pattern = r'## 📋 Schema Attributes\s*\n(.*?)(?=\n## |\Z)'
    schema_match = re.search(schema_section_pattern, content, re.DOTALL)
    
    if not schema_match:
        return None
    
    schema_section = schema_match.group(1)
    
    # Extract markdown table using a more robust approach
    lines = schema_section.split('\n')
    
    # Find table start (headers)
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
    
    # Skip separator line
    table_start += 2
    
    # Parse table rows - handle multi-line cells
    rows = []
    current_row = []
    
    for line in lines[table_start:]:
        line = line.strip()
        if not line:
            continue
        if line.startswith('|') and line.endswith('|'):
            # This is a table row
            cells = [cell.strip() for cell in line[1:-1].split('|')]
            if len(cells) == len(headers):
                # Complete row
                rows.append(dict(zip(headers, cells)))
            elif len(cells) > 0:
                # Possible continuation of previous row
                if current_row:
                    # Merge with previous incomplete row
                    for i, cell in enumerate(cells):
                        if i < len(current_row):
                            current_row[i] += ' ' + cell
                        else:
                            current_row.append(cell)
                    if len(current_row) == len(headers):
                        rows.append(dict(zip(headers, current_row)))
                        current_row = []
                else:
                    current_row = cells
        elif line.startswith('|') or ('|' in line and current_row):
            # Continuation line
            cells = [cell.strip() for cell in line.split('|') if cell.strip()]
            for i, cell in enumerate(cells):
                if i < len(current_row):
                    current_row[i] += ' ' + cell
        else:
            # End of table
            break
    
    # Add any remaining row
    if current_row and len(current_row) == len(headers):
        rows.append(dict(zip(headers, current_row)))
    
    return {
        'headers': headers,
        'attributes': rows
    }


def convert_to_json_schema_property(attribute: Dict[str, str]) -> Dict[str, Any]:
    """
    Convert a single attribute row to JSON schema property definition.
    
    Args:
        attribute: Dict with keys like 'Attribute', 'Type', 'Required', 'Description'
    
    Returns:
        JSON schema property definition
    """
    attr_name = attribute.get('Attribute', '').strip()
    attr_type = attribute.get('Type', '').strip()
    required = attribute.get('Required', '').strip().lower() == 'yes'
    description = attribute.get('Description', '').strip()
    
    # Convert markdown type notation to JSON schema
    json_property = {'description': description}
    
    if attr_type == 'string':
        json_property['type'] = 'string'
    elif attr_type == 'number':
        json_property['type'] = 'number'
    elif attr_type == 'boolean':
        json_property['type'] = 'boolean'
    elif attr_type.startswith('[') and attr_type.endswith(']'):
        # Array type like [string] or [object]
        inner_type = attr_type[1:-1]
        json_property['type'] = 'array'
        if inner_type == 'string':
            json_property['items'] = {'type': 'string'}
        elif inner_type == 'object':
            # Special handling for evidence arrays
            if attr_name == 'evidence':
                json_property['items'] = {
                    'type': 'object',
                    'properties': {
                        'provenance_id': {'type': 'string'},
                        'supports_fields': {'type': 'array', 'items': {'type': 'string'}}
                    },
                    'required': ['provenance_id', 'supports_fields']
                }
            else:
                json_property['items'] = {'type': 'object'}
        else:
            json_property['items'] = {'type': inner_type}
    elif attr_type == 'object':
        json_property['type'] = 'object'
        
        # Special handling for known complex objects
        if attr_name == 'job_statement' and 'decomposed' in description.lower():
            # Handle decomposed job_statement structure
            json_property['properties'] = {
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
            }
            json_property['required'] = ['user_scenario', 'user_enablement', 'user_outcome']
        elif attr_name == 'opportunity_score':
            json_property['properties'] = {
                'value': {'type': 'number', 'minimum': 1, 'maximum': 20},
                'importance': {'type': 'number', 'minimum': 1, 'maximum': 10},
                'satisfaction': {'type': 'number', 'minimum': 1, 'maximum': 10},
                'value_source': {'type': 'string', 'enum': ['evidence', 'synthetic']},
                'importance_source': {'type': 'string', 'enum': ['evidence', 'synthetic']},
                'satisfaction_source': {'type': 'string', 'enum': ['evidence', 'synthetic']}
            }
            json_property['required'] = ['value', 'importance', 'satisfaction', 'value_source', 'importance_source', 'satisfaction_source']
    else:
        # Default to string for unknown types
        json_property['type'] = 'string'
    
    return attr_name, json_property, required


def validate_parsed_schema(schema_data: Dict[str, Any]) -> List[str]:
    """
    Validate the parsed schema data for completeness and correctness.
    
    Returns:
        List of validation errors (empty if valid)
    """
    errors = []
    
    if not schema_data:
        errors.append("No schema data found")
        return errors
    
    if 'attributes' not in schema_data:
        errors.append("No attributes found in schema data")
        return errors
    
    attributes = schema_data['attributes']
    
    # Check for required core attributes
    required_attrs = {'object_type', 'id', 'job_statement', 'evidence'}
    found_attrs = {attr.get('Attribute', '').strip() for attr in attributes}
    
    missing_required = required_attrs - found_attrs
    if missing_required:
        errors.append(f"Missing required attributes: {', '.join(missing_required)}")
    
    # Validate each attribute has required fields
    for i, attr in enumerate(attributes):
        if not attr.get('Attribute', '').strip():
            errors.append(f"Row {i+1}: Missing attribute name")
        if not attr.get('Type', '').strip():
            errors.append(f"Row {i+1}: Missing type for attribute '{attr.get('Attribute', '')}'")
        if not attr.get('Required', '').strip():
            errors.append(f"Row {i+1}: Missing required field for attribute '{attr.get('Attribute', '')}'")
    
    return errors


def generate_json_schema(schema_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Generate JSON schema from validated schema data.
    
    Returns:
        Complete JSON schema for Problem object
    """
    properties = {}
    required_fields = []
    
    for attr in schema_data['attributes']:
        attr_name, json_property, is_required = convert_to_json_schema_property(attr)
        
        if attr_name:
            properties[attr_name] = json_property
            if is_required:
                required_fields.append(attr_name)
    
    schema = {
        'type': 'object',
        'properties': properties,
        'required': required_fields
    }
    
    return schema


def process_problem_object_markdown(file_path: Path) -> Dict[str, Any]:
    """
    Main processing function implementing the three-stage docling process.
    
    Returns:
        Dict with processing results including schema, errors, and metadata
    """
    print(f"Processing Problem object: {file_path.name}")
    
    try:
        # Stage 1: Docling parse markdown
        converter = DocumentConverter()
        result = converter.convert(file_path)
        
        # Extract markdown content
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Parse schema attributes table
        schema_data = parse_schema_attributes_table(content)
        
        if not schema_data:
            return {
                'success': False,
                'stage': 'parsing',
                'errors': ['Schema Attributes table not found in markdown'],
                'schema_data': None,
                'json_schema': None
            }
        
        # Stage 2: Validation check
        validation_errors = validate_parsed_schema(schema_data)
        
        if validation_errors:
            return {
                'success': False,
                'stage': 'validation',
                'errors': validation_errors,
                'schema_data': schema_data,
                'json_schema': None
            }
        
        # Stage 3: JSON generation
        json_schema = generate_json_schema(schema_data)
        
        return {
            'success': True,
            'stage': 'completed',
            'errors': [],
            'schema_data': schema_data,
            'json_schema': json_schema,
            'docling_metadata': {
                'pages': len(result.document.pages),
                'tables': len([elem for page in result.document.pages for elem in page.elements if hasattr(elem, 'type') and 'table' in str(elem.type).lower()])
            }
        }
        
    except Exception as e:
        return {
            'success': False,
            'stage': 'parsing',
            'errors': [f"Docling processing failed: {str(e)}"],
            'schema_data': None,
            'json_schema': None
        }


def main():
    """Test the docling parser on the promoted Problem object."""
    print("🔍 Docling Problem Object Parser")
    print("=" * 50)
    
    # Test with promoted Problem object
    test_file = Path("watch_folders/hitl_promotion_candidates/20250707_130903_problem_object_odi_update.md")
    
    if not test_file.exists():
        print(f"❌ Test file not found: {test_file}")
        return
    
    result = process_problem_object_markdown(test_file)
    
    print(f"📁 Processing: {test_file.name}")
    print(f"🎯 Stage completed: {result['stage']}")
    print(f"✅ Success: {result['success']}")
    
    if result['errors']:
        print(f"❌ Errors ({len(result['errors'])}):")
        for error in result['errors']:
            print(f"  - {error}")
    
    if result['schema_data']:
        attrs = result['schema_data']['attributes']
        print(f"📋 Found {len(attrs)} schema attributes")
        
        # Show sample attributes
        for attr in attrs[:3]:
            print(f"  • {attr.get('Attribute', 'N/A')} ({attr.get('Type', 'N/A')}) - {attr.get('Required', 'N/A')}")
        if len(attrs) > 3:
            print(f"  ... and {len(attrs) - 3} more")
    
    if result['json_schema']:
        required_count = len(result['json_schema'].get('required', []))
        total_props = len(result['json_schema'].get('properties', {}))
        print(f"🔧 Generated schema: {total_props} properties, {required_count} required")
        
        # Output sample of generated schema
        print("\n📄 Sample generated schema:")
        sample_schema = {
            'type': result['json_schema']['type'],
            'required': result['json_schema']['required'][:5],  # First 5 required fields
            'properties': dict(list(result['json_schema']['properties'].items())[:3])  # First 3 properties
        }
        print(json.dumps(sample_schema, indent=2))
    
    if result['success']:
        print(f"\n✅ Docling parsing completed successfully!")
    else:
        print(f"\n❌ Docling parsing failed at {result['stage']} stage")


if __name__ == "__main__":
    main()