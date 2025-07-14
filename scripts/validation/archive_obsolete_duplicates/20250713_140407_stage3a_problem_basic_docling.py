#!/usr/bin/env python3
"""
Stage 3A: Problem Object Basic Docling Processing

Lightweight docling processing for Problem objects (development flow):
- Extracts Schema Attributes table only
- Generates Problem-specific JSON schema
- Basic schema quality validation
- Fast feedback for development iteration

Scope: Schema governance only (not instance creation or relationships)
Note: Stage 3B (full document processing) reserved for production candidates
"""

import json
from pathlib import Path
from typing import Dict, List, Any, Optional

# Import our existing Problem object docling parser
import sys
sys.path.append(str(Path(__file__).parent.parent / "docling"))
from parse_problem_object import (
    parse_schema_attributes_table,
    validate_parsed_schema,
    generate_json_schema,
    process_problem_object_markdown
)


def validate_problem_schema_quality(json_schema: Dict[str, Any]) -> List[str]:
    """
    Validate Problem object specific schema quality.
    
    Returns:
        List of validation errors (empty if valid)
    """
    errors = []
    
    if not json_schema:
        errors.append("No JSON schema generated")
        return errors
    
    properties = json_schema.get('properties', {})
    required = json_schema.get('required', [])
    
    # Problem object specific validations
    problem_required_fields = ['object_type', 'id', 'job_statement', 'evidence']
    for field in problem_required_fields:
        if field not in properties:
            errors.append(f"Problem schema missing required field: {field}")
        if field not in required:
            errors.append(f"Problem schema should require field: {field}")
    
    # Validate job_statement structure (new decomposed format)
    if 'job_statement' in properties:
        job_stmt_def = properties['job_statement']
        if job_stmt_def.get('type') == 'object':
            # Validate decomposed structure
            job_props = job_stmt_def.get('properties', {})
            job_required = job_stmt_def.get('required', [])
            
            decomposed_fields = ['user_scenario', 'user_enablement', 'user_outcome']
            for field in decomposed_fields:
                if field not in job_props:
                    errors.append(f"job_statement missing decomposed field: {field}")
                if field not in job_required:
                    errors.append(f"job_statement should require field: {field}")
                
                # Validate source tracking
                if field in job_props:
                    field_props = job_props[field].get('properties', {})
                    if 'source' not in field_props:
                        errors.append(f"job_statement.{field} missing source tracking")
                    elif field_props['source'].get('enum') != ['evidence', 'synthetic']:
                        errors.append(f"job_statement.{field}.source should enforce evidence/synthetic enum")
    
    # Validate evidence structure
    if 'evidence' in properties:
        evidence_def = properties['evidence']
        if evidence_def.get('type') == 'array':
            items_def = evidence_def.get('items', {})
            if items_def.get('type') == 'object':
                item_props = items_def.get('properties', {})
                item_required = items_def.get('required', [])
                
                evidence_fields = ['provenance_id', 'supports_fields']
                for field in evidence_fields:
                    if field not in item_props:
                        errors.append(f"evidence items missing field: {field}")
                    if field not in item_required:
                        errors.append(f"evidence items should require field: {field}")
    
    # Validate opportunity_score structure (ODI scoring)
    if 'opportunity_score' in properties:
        odi_def = properties['opportunity_score']
        if odi_def.get('type') == 'object':
            odi_props = odi_def.get('properties', {})
            odi_required = odi_def.get('required', [])
            
            odi_fields = ['value', 'importance', 'satisfaction', 'value_source', 'importance_source', 'satisfaction_source']
            for field in odi_fields:
                if field not in odi_props:
                    errors.append(f"opportunity_score missing field: {field}")
                if field not in odi_required:
                    errors.append(f"opportunity_score should require field: {field}")
    
    return errors


def process_problem_object_stage3(file_path: Path) -> Dict[str, Any]:
    """
    Process Problem object through Stage 3 docling processing.
    
    Returns:
        Validation result dictionary
    """
    try:
        # Use existing docling parser
        result = process_problem_object_markdown(file_path)
        
        if not result['success']:
            return {
                "valid": False,
                "stage": "stage3_problem_docling",
                "errors": result.get('errors', []),
                "parsing_stage": result.get('stage', 'failed'),
                "object_type": "Problem"
            }
        
        # Additional Problem-specific schema validation
        schema_errors = validate_problem_schema_quality(result.get('json_schema', {}))
        
        return {
            "valid": len(schema_errors) == 0,
            "stage": "stage3_problem_docling",
            "errors": schema_errors,
            "docling_metadata": result.get('docling_metadata', {}),
            "schema_data": result.get('schema_data', {}),
            "json_schema": result.get('json_schema', {}),
            "parsing_stage": result.get('stage', 'completed'),
            "object_type": "Problem"
        }
        
    except Exception as e:
        return {
            "valid": False,
            "stage": "stage3_problem_docling",
            "errors": [f"Problem object docling processing failed: {str(e)}"],
            "parsing_stage": "error",
            "object_type": "Problem"
        }


def main():
    """Test Stage 3 Problem object docling processing."""
    print("🔍 Stage 3: Problem Object Docling Processing")
    print("=" * 50)
    
    review_dir = Path("watch_folders/hitl_review")
    if not review_dir.exists():
        print(f"❌ Review directory not found: {review_dir}")
        return
    
    markdown_files = [f for f in review_dir.glob("*.md") if "problem" in f.name.lower()]
    if not markdown_files:
        print("📭 No Problem object files found")
        return
    
    for file_path in markdown_files:
        result = process_problem_object_stage3(file_path)
        
        print(f"\n📁 {file_path.name}")
        print(f"🎯 Object Type: {result.get('object_type', 'Unknown')}")
        print(f"🎯 Parsing Stage: {result.get('parsing_stage', 'unknown')}")
        print(f"✅ Stage 3 Valid: {result['valid']}")
        
        if result['errors']:
            print(f"❌ Errors ({len(result['errors'])}):")
            for error in result['errors']:
                print(f"  - {error}")
        
        if result.get('docling_metadata'):
            metadata = result['docling_metadata']
            print(f"📄 Docling: {metadata.get('pages', 0)} pages, {metadata.get('tables', 0)} tables")
        
        if result.get('schema_data'):
            attrs = result['schema_data'].get('attributes', [])
            print(f"📋 Schema attributes: {len(attrs)}")
        
        if result.get('json_schema'):
            schema = result['json_schema']
            props = len(schema.get('properties', {}))
            required = len(schema.get('required', []))
            print(f"🔧 Generated schema: {props} properties, {required} required")
        
        if result['valid']:
            print("✅ Problem object schema generation successful")
            
            # Show key schema components
            if result.get('json_schema'):
                schema = result['json_schema']
                if 'job_statement' in schema.get('properties', {}):
                    job_type = schema['properties']['job_statement'].get('type', 'unknown')
                    print(f"🎯 job_statement type: {job_type}")
                    
                if 'opportunity_score' in schema.get('properties', {}):
                    print("📊 ODI scoring structure: present")


if __name__ == "__main__":
    main()