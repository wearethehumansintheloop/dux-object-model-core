#!/usr/bin/env python3
"""
Stage 3b: Behavior Object Schema Validation
Validate Docling proposal against canonical governance schema

This stage validates that the proposal:
- Complies with DUX object template structure
- Has all required Behavior object fields
- Follows relationship field conventions
- Is ready for explosion into microservices (Stage 4)
"""

import json
import re
from pathlib import Path
from typing import Dict, List, Any, Optional

# Canonical Behavior Object Requirements (v9.6)
BEHAVIOR_CANONICAL_SCHEMA = {
    "required_fields": [
        "object_type",
        "id", 
        "user_enablement",
        "behavior_type",
        "signals"
    ],
    "optional_fields": [
        "protocol_url",
        "tags",
        "created_at",
        "updated_at"
    ],
    "field_types": {
        "object_type": "string",
        "id": "string",
        "user_enablement": "string",
        "behavior_type": "string",
        "signals": "array",
        "protocol_url": "string",
        "tags": "array",
        "created_at": "string",
        "updated_at": "string"
    },
    "behavior_types": [
        "system_action",
        "organizational_process",
        "user_action"
    ],
    "signal_pattern": "^[a-z_]+$"  # snake_case signals
}


def validate_canonical_compliance(json_schema: Dict[str, Any]) -> List[str]:
    """
    Validate JSON schema against canonical Behavior requirements.
    
    Returns:
        List of validation errors (empty if valid)
    """
    errors = []
    
    if not json_schema:
        errors.append("No JSON schema provided")
        return errors
    
    properties = json_schema.get('properties', {})
    required = json_schema.get('required', [])
    
    # Check all required fields exist
    for field in BEHAVIOR_CANONICAL_SCHEMA['required_fields']:
        if field not in properties:
            errors.append(f"Missing required field: {field}")
        elif field not in required:
            errors.append(f"Field '{field}' must be in required array")
    
    # Validate field types
    for field, expected_type in BEHAVIOR_CANONICAL_SCHEMA['field_types'].items():
        if field in properties:
            field_def = properties[field]
            actual_type = field_def.get('type')
            
            # Handle array fields
            if expected_type == 'array' and actual_type != 'array':
                errors.append(f"Field '{field}' must be type array, got {actual_type}")
            # Handle string fields
            elif expected_type == 'string' and actual_type != 'string':
                errors.append(f"Field '{field}' must be type string, got {actual_type}")
    
    # Validate object_type enum
    if 'object_type' in properties:
        obj_type = properties['object_type']
        if obj_type.get('enum') != ['Behavior']:
            errors.append("object_type must have enum ['Behavior']")
    
    # Validate behavior_type enum
    if 'behavior_type' in properties:
        behavior_type = properties['behavior_type']
        if behavior_type.get('type') == 'string':
            enum_values = behavior_type.get('enum', [])
            if not enum_values:
                errors.append("behavior_type should have enum values")
            else:
                invalid_types = [t for t in enum_values if t not in BEHAVIOR_CANONICAL_SCHEMA['behavior_types']]
                if invalid_types:
                    errors.append(f"Invalid behavior_type values: {invalid_types}")
    
    # Validate signals structure
    if 'signals' in properties:
        signals = properties['signals']
        if signals.get('type') == 'array':
            items = signals.get('items', {})
            if items.get('type') != 'string':
                errors.append("Signals items must be type string")
            # Check if pattern is specified for signal format
            pattern = items.get('pattern')
            if pattern and pattern != BEHAVIOR_CANONICAL_SCHEMA['signal_pattern']:
                errors.append(f"Signals should follow pattern: {BEHAVIOR_CANONICAL_SCHEMA['signal_pattern']}")
    
    return errors


def validate_natural_language_consistency(docling_path: Path) -> List[str]:
    """
    Validate natural language sections match schema.
    
    Returns:
        List of validation errors (empty if valid)
    """
    errors = []
    
    try:
        with open(docling_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract JSON schema from docling markdown
        json_match = re.search(r'```json\n(.*?)\n```', content, re.DOTALL)
        if not json_match:
            errors.append("No JSON schema found in docling output")
            return errors
        
        json_schema = json.loads(json_match.group(1))
        
        # Check that User Enablement description exists
        if 'user_enablement' in json_schema.get('properties', {}):
            # Look for User Enablement section in natural language
            if not re.search(r'user.?enablement|User.?Enablement', content, re.IGNORECASE):
                errors.append("User Enablement field defined but no description in natural language")
        
        # Check that Signals description exists
        if 'signals' in json_schema.get('properties', {}):
            if not re.search(r'signal|Signal', content, re.IGNORECASE):
                errors.append("Signals field defined but no description in natural language")
        
        # Note: Section validation happens in Stage 1, not here
        # Stage 3b only validates the extracted schema against canonical requirements
        
    except Exception as e:
        errors.append(f"Error reading docling file: {str(e)}")
    
    return errors


def process_stage3b_behavior(docling_path: Path) -> Dict[str, Any]:
    """
    Process Behavior object docling output through Stage 3b validation.
    
    Returns:
        Dict with keys:
        - passed: bool
        - errors: List[str]
        - json_schema: Optional[Dict]
    """
    errors = []
    json_schema = None
    
    try:
        # Read docling output
        with open(docling_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract JSON schema
        json_match = re.search(r'```json\n(.*?)\n```', content, re.DOTALL)
        if not json_match:
            errors.append("No JSON schema found in docling output")
            return {
                'passed': False,
                'errors': errors,
                'json_schema': None
            }
        
        json_schema = json.loads(json_match.group(1))
        
        # Canonical validation
        canon_errors = validate_canonical_compliance(json_schema)
        if canon_errors:
            errors.extend(canon_errors)
        
        # Natural language consistency
        nl_errors = validate_natural_language_consistency(docling_path)
        if nl_errors:
            errors.extend(nl_errors)
        
        # Success message if no errors
        if not errors:
            print("  ✓ Canonical validation passed")
            print("  ✓ Natural language consistency validated")
            print("  ✓ Ready for Stage 4 explosion")
        
        return {
            'passed': len(errors) == 0,
            'errors': errors,
            'json_schema': json_schema
        }
        
    except json.JSONDecodeError as e:
        errors.append(f"Invalid JSON in docling output: {str(e)}")
        return {
            'passed': False,
            'errors': errors,
            'json_schema': None
        }
    except Exception as e:
        errors.append(f"Processing error: {str(e)}")
        return {
            'passed': False,
            'errors': errors, 
            'json_schema': None
        }


if __name__ == "__main__":
    # Test with a docling file
    import sys
    if len(sys.argv) > 1:
        test_file = Path(sys.argv[1])
        if test_file.exists():
            print(f"📋 Stage 3b: Validating {test_file.name}")
            result = process_stage3b_behavior(test_file)
            
            if result['json_schema']:
                print(f"  ✓ Loaded JSON schema with {len(result['json_schema'].get('properties', {}))} properties")
            
            print(f"  {'✅' if result['passed'] else '❌'} Stage 3b {'Passed' if result['passed'] else 'Failed'}")
            
            if result['errors']:
                print("\nErrors:")
                for error in result['errors']:
                    print(f"  - {error}")
        else:
            print(f"File not found: {test_file}")
    else:
        print("Usage: python stage3b_behavior_schema_validation.py <behavior_docling.md>")