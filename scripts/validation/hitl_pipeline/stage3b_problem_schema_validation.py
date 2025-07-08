#!/usr/bin/env python3
"""
Stage 3b: Problem Object Schema Validation
Validate Docling proposal against canonical governance schema

This stage validates that the proposal:
- Complies with DUX object template structure
- Has all required Problem object fields
- Follows relationship field conventions
- Is ready for explosion into microservices (Stage 4)
"""

import json
import re
from pathlib import Path
from typing import Dict, List, Any, Optional

# Canonical Problem Object Requirements (v9.6)
PROBLEM_CANONICAL_SCHEMA = {
    "required_fields": [
        "object_type",
        "id", 
        "job_statement",
        "evidence"
    ],
    "optional_fields": [
        "end_user",
        "what_is_at_stake",
        "protocol_url",
        "result_ids",
        "useroutcome_ids",
        "flow_ids",
        "opportunity_score",
        "tags",
        "created_at",
        "updated_at"
    ],
    "field_types": {
        "object_type": "string",
        "id": "string",
        "job_statement": "object",
        "evidence": "array",
        "end_user": "array",
        "what_is_at_stake": "string",
        "protocol_url": "string",
        "result_ids": "array",
        "useroutcome_ids": "array", 
        "flow_ids": "array",
        "opportunity_score": "object",
        "tags": "array",
        "created_at": "string",
        "updated_at": "string"
    },
    "special_validations": {
        "job_statement": {
            "required_properties": ["user_scenario", "user_enablement", "user_outcome"]
        },
        "evidence": {
            "item_type": "object",
            "required_properties": ["provenance_id", "supports_fields"]
        },
        "opportunity_score": {
            "required_properties": ["value", "importance", "satisfaction", 
                                  "value_source", "importance_source", "satisfaction_source"]
        }
    }
}


def load_docling_markdown(file_path: Path) -> Dict[str, Any]:
    """Load and parse Docling markdown with embedded JSON schema."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract JSON schema from Docling markdown
    json_match = re.search(
        r'## 🔧 Generated JSON Schema \(Proposal\)\s*```json\s*(.*?)\s*```',
        content,
        re.DOTALL
    )
    
    if not json_match:
        return {
            'success': False,
            'errors': ['No JSON schema found in Docling markdown']
        }
    
    try:
        json_schema = json.loads(json_match.group(1))
        return {
            'success': True,
            'content': content,
            'json_schema': json_schema
        }
    except json.JSONDecodeError as e:
        return {
            'success': False,
            'errors': [f'Invalid JSON schema: {str(e)}']
        }


def validate_against_canonical(json_schema: Dict[str, Any]) -> List[str]:
    """Validate proposal schema against canonical Problem object requirements."""
    errors = []
    
    properties = json_schema.get('properties', {})
    required = json_schema.get('required', [])
    
    # Check all required fields are present
    for field in PROBLEM_CANONICAL_SCHEMA['required_fields']:
        if field not in properties:
            errors.append(f"Missing required field in schema: {field}")
        if field not in required:
            errors.append(f"Field should be marked as required: {field}")
    
    # Check field types match canonical
    for field, expected_type in PROBLEM_CANONICAL_SCHEMA['field_types'].items():
        if field in properties:
            actual_type = properties[field].get('type', 'unknown')
            if actual_type != expected_type:
                errors.append(f"Field '{field}' type mismatch: expected {expected_type}, got {actual_type}")
    
    # Special validations for complex fields
    
    # Evidence array validation
    if 'evidence' in properties:
        evidence_def = properties['evidence']
        if evidence_def.get('type') != 'array':
            errors.append("Evidence must be an array")
        else:
            items = evidence_def.get('items', {})
            if items.get('type') != 'object':
                errors.append("Evidence items must be objects")
            else:
                # Check for required evidence properties
                evidence_props = items.get('properties', {})
                for prop in PROBLEM_CANONICAL_SCHEMA['special_validations']['evidence']['required_properties']:
                    if prop not in evidence_props:
                        errors.append(f"Evidence items missing required property: {prop}")
    
    # Opportunity score validation
    if 'opportunity_score' in properties:
        odi_def = properties['opportunity_score']
        if odi_def.get('type') != 'object':
            errors.append("Opportunity score must be an object")
        else:
            odi_props = odi_def.get('properties', {})
            for prop in PROBLEM_CANONICAL_SCHEMA['special_validations']['opportunity_score']['required_properties']:
                if prop not in odi_props:
                    errors.append(f"Opportunity score missing required property: {prop}")
    
    # Check for unknown fields (not in canonical)
    all_canonical_fields = (
        set(PROBLEM_CANONICAL_SCHEMA['required_fields']) | 
        set(PROBLEM_CANONICAL_SCHEMA['optional_fields'])
    )
    unknown_fields = set(properties.keys()) - all_canonical_fields
    if unknown_fields:
        errors.append(f"Unknown fields not in canonical schema: {unknown_fields}")
    
    return errors


def validate_natural_language_consistency(content: str, json_schema: Dict[str, Any]) -> List[str]:
    """Validate that natural language descriptions match JSON schema."""
    errors = []
    
    # Extract Schema Attributes table from content
    table_match = re.search(
        r'## 📋 Schema Attributes\s*\n(.*?)(?=\n##)',
        content,
        re.DOTALL
    )
    
    if not table_match:
        errors.append("Schema Attributes table not found in Docling markdown")
        return errors
    
    # Count attributes in table
    table_content = table_match.group(1)
    table_rows = [line for line in table_content.split('\n') 
                  if '|' in line and not line.strip().startswith('|--')]
    # Subtract 1 for header row
    table_attr_count = len(table_rows) - 1 if table_rows else 0
    
    # Count properties in JSON schema
    json_attr_count = len(json_schema.get('properties', {}))
    
    if table_attr_count != json_attr_count:
        errors.append(f"Attribute count mismatch: Table has {table_attr_count}, JSON has {json_attr_count}")
    
    return errors


def check_proposal_readiness(json_schema: Dict[str, Any]) -> Dict[str, Any]:
    """Check if proposal is ready for Stage 4 explosion."""
    readiness = {
        'ready': True,
        'checks': {}
    }
    
    # Check 1: Has properties
    has_properties = len(json_schema.get('properties', {})) > 0
    readiness['checks']['has_properties'] = has_properties
    if not has_properties:
        readiness['ready'] = False
    
    # Check 2: Has required fields
    has_required = len(json_schema.get('required', [])) > 0
    readiness['checks']['has_required_fields'] = has_required
    if not has_required:
        readiness['ready'] = False
    
    # Check 3: Evidence structure correct
    evidence_valid = False
    if 'evidence' in json_schema.get('properties', {}):
        evidence_def = json_schema['properties']['evidence']
        if evidence_def.get('type') == 'array':
            items = evidence_def.get('items', {})
            if items.get('type') == 'object':
                evidence_valid = True
    readiness['checks']['evidence_structure_valid'] = evidence_valid
    if not evidence_valid:
        readiness['ready'] = False
    
    # Check 4: Job statement present
    has_job_statement = 'job_statement' in json_schema.get('properties', {})
    readiness['checks']['has_job_statement'] = has_job_statement
    if not has_job_statement:
        readiness['ready'] = False
    
    return readiness


def process_stage3b_validation(docling_file_path: Path) -> Dict[str, Any]:
    """Main Stage 3b validation process."""
    print(f"📋 Stage 3b: Validating {docling_file_path.name}")
    
    # Load Docling markdown
    load_result = load_docling_markdown(docling_file_path)
    if not load_result['success']:
        return {
            'success': False,
            'stage': 'loading',
            'errors': load_result['errors']
        }
    
    content = load_result['content']
    json_schema = load_result['json_schema']
    
    print(f"  ✓ Loaded JSON schema with {len(json_schema.get('properties', {}))} properties")
    
    # Validate against canonical
    canonical_errors = validate_against_canonical(json_schema)
    if canonical_errors:
        print(f"  ✗ {len(canonical_errors)} canonical validation errors")
        return {
            'success': False,
            'stage': 'canonical_validation',
            'errors': canonical_errors
        }
    
    print("  ✓ Canonical validation passed")
    
    # Validate natural language consistency
    nl_errors = validate_natural_language_consistency(content, json_schema)
    if nl_errors:
        print(f"  ✗ {len(nl_errors)} natural language consistency errors")
        return {
            'success': False,
            'stage': 'nl_consistency',
            'errors': nl_errors
        }
    
    print("  ✓ Natural language consistency validated")
    
    # Check readiness for Stage 4
    readiness = check_proposal_readiness(json_schema)
    if not readiness['ready']:
        failed_checks = [k for k, v in readiness['checks'].items() if not v]
        return {
            'success': False,
            'stage': 'readiness_check',
            'errors': [f"Not ready for Stage 4: failed checks - {failed_checks}"]
        }
    
    print("  ✓ Ready for Stage 4 explosion")
    
    return {
        'success': True,
        'stage': 'completed',
        'errors': [],
        'json_schema': json_schema,
        'readiness': readiness,
        'validation_status': 'proposal_validated',
        'next_stage': 'stage4_explosion'
    }


def main():
    """Run Stage 3b validation."""
    print("🔍 Stage 3b: Problem Object Schema Validation")
    print("=" * 60)
    print("Validating proposals against canonical governance schema")
    print()
    
    import sys
    
    if len(sys.argv) > 1:
        # Process specific file
        file_path = Path(sys.argv[1])
        if not file_path.exists():
            print(f"❌ File not found: {file_path}")
            return
        
        result = process_stage3b_validation(file_path)
        
        if result['success']:
            print(f"\n✅ Stage 3b Complete!")
            print(f"🎯 Status: {result['validation_status']}")
            print(f"➡️  Next: {result['next_stage']}")
        else:
            print(f"\n❌ Stage 3b Failed at: {result['stage']}")
            for error in result['errors']:
                print(f"  - {error}")
    
    else:
        # Look for Docling files in review folder
        review_dir = Path("watch_folders/hitl_review")
        if not review_dir.exists():
            print(f"❌ Review directory not found: {review_dir}")
            return
        
        docling_files = list(review_dir.glob("*_docling.md"))
        if not docling_files:
            print("📭 No Docling markdown files found (run Stage 3a first)")
            return
        
        for file_path in docling_files:
            print(f"\n{'='*60}")
            result = process_stage3b_validation(file_path)
            
            if result['success']:
                print(f"\n✅ {file_path.name} → Stage 4")
            else:
                print(f"\n❌ {file_path.name} → Workshop (failed at {result['stage']})")


if __name__ == "__main__":
    main()