#!/usr/bin/env python3
"""
Stage 3a: Problem Object Docling Markdown Conversion
Natural Language First - Validate with JSON, Generate with MD

⚠️  IMPORTANT: This stage MUST run on the host machine with docling installed.
⚠️  Container environments may not have docling available.
⚠️  See requirements.txt for docling dependencies.

Converts Problem object markdown to Docling markdown format with:
- Structured attribute table extraction
- Embedded JSON schema generation from table
- Validation that table matches embedded JSON
- Treatment as "proposal" until promoted to canon

NO explosion into microservices - that's Stage 4.
"""

import json
import re
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
import sys

# Add docling parser to path
sys.path.append(str(Path(__file__).parent.parent / "docling"))

def extract_schema_table_from_markdown(content: str) -> Optional[Dict[str, Any]]:
    """
    Extract Schema Attributes table from markdown content.
    Natural language first - parse the human-readable table.
    """
    # Find Schema Attributes section
    schema_section = re.search(
        r'## 📋 Schema Attributes\s*\n(.*?)(?=\n## |\Z)', 
        content, 
        re.DOTALL
    )
    
    if not schema_section:
        return None
    
    # Extract table rows
    lines = schema_section.group(1).split('\n')
    table_rows = []
    headers = []
    
    for line in lines:
        if '|' in line and not line.strip().startswith('|--'):
            cells = [cell.strip() for cell in line.split('|') if cell.strip()]
            if not headers:
                headers = cells
            else:
                table_rows.append(cells)
    
    if not headers or not table_rows:
        return None
    
    # Convert to structured data
    attributes = []
    for row in table_rows:
        if len(row) >= len(headers):
            attr_dict = {}
            for i, header in enumerate(headers):
                if i < len(row):
                    attr_dict[header] = row[i]
            attributes.append(attr_dict)
    
    return {
        'headers': headers,
        'attributes': attributes,
        'source': 'markdown_table'
    }


def generate_json_schema_from_table(schema_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Generate JSON schema from extracted table data.
    This is the 'proposal' schema that will be validated.
    Includes canonical-attribute definitions for complex objects.
    """
    json_schema = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "$id": "proposal/problem_object_schema.json",
        "title": "Problem Object Schema (Proposal)",
        "type": "object",
        "properties": {},
        "required": []
    }
    
    # Define canonical structures for Problem object complex attributes
    CANONICAL_STRUCTURES = {
        "job_statement": {
            "type": "object",
            "properties": {
                "user_scenario": {
                    "type": "string",
                    "description": "When [situation]..."
                },
                "user_enablement": {
                    "type": "string", 
                    "description": "I want [motivation]..."
                },
                "user_outcome": {
                    "type": "string",
                    "description": "so I can [outcome]"
                }
            },
            "required": ["user_scenario", "user_enablement", "user_outcome"],
            "description": "JTBD decomposed into three components"
        },
        "evidence": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "provenance_id": {
                        "type": "string",
                        "description": "Reference to Provenance object"
                    },
                    "supports_fields": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Fields this evidence supports"
                    }
                },
                "required": ["provenance_id", "supports_fields"]
            }
        },
        "opportunity_score": {
            "type": "object",
            "properties": {
                "value": {
                    "type": "number",
                    "description": "ODI opportunity score value"
                },
                "importance": {
                    "type": "number",
                    "description": "How important is this to users (1-10)"
                },
                "satisfaction": {
                    "type": "number",
                    "description": "How satisfied are users currently (1-10)"
                },
                "value_source": {
                    "type": "string",
                    "enum": ["evidence", "synthetic"],
                    "description": "Source of the value score"
                },
                "importance_source": {
                    "type": "string",
                    "enum": ["evidence", "synthetic"],
                    "description": "Source of the importance score"
                },
                "satisfaction_source": {
                    "type": "string",
                    "enum": ["evidence", "synthetic"],
                    "description": "Source of the satisfaction score"
                }
            },
            "required": ["value", "importance", "satisfaction", 
                        "value_source", "importance_source", "satisfaction_source"]
        },
        "result_ids": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "string"},
                    "reference_context": {"type": "string"}
                },
                "required": ["id"]
            }
        },
        "useroutcome_ids": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "string"},
                    "reference_context": {"type": "string"}
                },
                "required": ["id"]
            }
        },
        "flow_ids": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "string"},
                    "reference_context": {"type": "string"}
                },
                "required": ["id"]
            }
        }
    }
    
    for attr in schema_data['attributes']:
        attr_name = attr.get('Attribute', '')
        attr_type = attr.get('Type', 'string')
        description = attr.get('Description', '')
        is_required = attr.get('Required', '').lower() in ['yes', 'true']
        
        if not attr_name:
            continue
        
        # Check if this attribute has a canonical structure
        if attr_name in CANONICAL_STRUCTURES:
            prop_schema = CANONICAL_STRUCTURES[attr_name].copy()
            prop_schema['description'] = description
        else:
            # Convert markdown types to JSON schema types
            schema_type = attr_type.strip()
            if schema_type.startswith('[') and schema_type.endswith(']'):
                # Array type
                inner_type = schema_type[1:-1]
                if inner_type == "string":
                    prop_schema = {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": description
                    }
                else:
                    prop_schema = {
                        "type": "array",
                        "items": {"type": "object"},
                        "description": description
                    }
            else:
                prop_schema = {
                    "type": schema_type if schema_type != "object" else "object",
                    "description": description
                }
        
        json_schema['properties'][attr_name] = prop_schema
        
        if is_required:
            json_schema['required'].append(attr_name)
    
    return json_schema


def validate_table_json_consistency(schema_data: Dict[str, Any], json_schema: Dict[str, Any]) -> List[str]:
    """
    Validate that the attribute table and generated JSON schema are consistent.
    This ensures the proposal is internally coherent.
    """
    errors = []
    
    # Check all table attributes are in JSON schema
    table_attrs = {attr.get('Attribute') for attr in schema_data['attributes'] if attr.get('Attribute')}
    json_attrs = set(json_schema.get('properties', {}).keys())
    
    missing_in_json = table_attrs - json_attrs
    if missing_in_json:
        errors.append(f"Attributes in table but not in JSON schema: {missing_in_json}")
    
    # Check required fields consistency
    table_required = {
        attr.get('Attribute') 
        for attr in schema_data['attributes'] 
        if attr.get('Required', '').lower() in ['yes', 'true'] and attr.get('Attribute')
    }
    json_required = set(json_schema.get('required', []))
    
    if table_required != json_required:
        errors.append(f"Required fields mismatch - Table: {table_required}, JSON: {json_required}")
    
    return errors


def create_docling_markdown(original_content: str, schema_data: Dict[str, Any], json_schema: Dict[str, Any]) -> str:
    """
    Create Docling-format markdown with embedded JSON schema.
    Natural language first with JSON as structured validation.
    """
    # Extract sections from original
    sections = {}
    section_patterns = {
        'header': r'^(# .* Object.*?)(?=\n##)',
        'purpose': r'(## 🎯 Purpose & Strategic Role.*?)(?=\n##)',
        'what_you_do': r'(## 🧠 "What would you say.*?".*?)(?=\n##)',
        'why_matters': r'(## 💡 Why the .* Object Matters.*?)(?=\n##)',
        'schema_attributes': r'(## 📋 Schema Attributes.*?)(?=\n##)',
        'canonical_example': r'(## 📦 Canonical Example.*?)(?=\n##|\Z)',
        'structural_role': r'(## 🔗 Structural Role.*?)(?=\n##|\Z)'
    }
    
    for name, pattern in section_patterns.items():
        match = re.search(pattern, original_content, re.DOTALL | re.MULTILINE)
        if match:
            sections[name] = match.group(1).strip()
    
    # Build Docling markdown
    docling_md = []
    
    # Add header
    if 'header' in sections:
        docling_md.append(sections['header'])
        docling_md.append("")
    
    # Add metadata block
    docling_md.append("## 📄 Docling Metadata")
    docling_md.append("```yaml")
    docling_md.append("format_version: 1.0")
    docling_md.append("object_type: Problem")
    docling_md.append("proposal_status: under_review")
    docling_md.append("natural_language_first: true")
    docling_md.append("validation_format: json")
    docling_md.append("generation_format: markdown")
    docling_md.append("```")
    docling_md.append("")
    
    # Add original sections
    for section in ['purpose', 'what_you_do', 'why_matters', 'schema_attributes']:
        if section in sections:
            docling_md.append(sections[section])
            docling_md.append("")
    
    # Add generated JSON schema
    docling_md.append("## 🔧 Generated JSON Schema (Proposal)")
    docling_md.append("```json")
    docling_md.append(json.dumps(json_schema, indent=2))
    docling_md.append("```")
    docling_md.append("")
    
    # Add canonical example if present
    if 'canonical_example' in sections:
        docling_md.append(sections['canonical_example'])
        docling_md.append("")
    
    if 'structural_role' in sections:
        docling_md.append(sections['structural_role'])
        docling_md.append("")
    
    # Add validation status
    docling_md.append("## ✅ Proposal Validation Status")
    docling_md.append("- Schema table extracted: ✓")
    docling_md.append("- JSON schema generated: ✓")
    docling_md.append("- Table-JSON consistency: ✓")
    docling_md.append("- Ready for Stage 3b validation")
    
    return "\n".join(docling_md)


def process_problem_to_docling_md(file_path: Path) -> Dict[str, Any]:
    """
    Stage 3a main process: Convert Problem .md to Docling .md with embedded JSON.
    """
    print(f"📄 Stage 3a: Converting {file_path.name} to Docling markdown")
    
    try:
        # Read original markdown
        with open(file_path, 'r', encoding='utf-8') as f:
            original_content = f.read()
        
        # Extract Schema Attributes table
        schema_data = extract_schema_table_from_markdown(original_content)
        if not schema_data:
            return {
                'success': False,
                'stage': 'table_extraction',
                'errors': ['Schema Attributes table not found in markdown']
            }
        
        print(f"  ✓ Extracted {len(schema_data['attributes'])} attributes from table")
        
        # Generate JSON schema from table
        json_schema = generate_json_schema_from_table(schema_data)
        print(f"  ✓ Generated JSON schema with {len(json_schema['properties'])} properties")
        
        # Validate consistency
        consistency_errors = validate_table_json_consistency(schema_data, json_schema)
        if consistency_errors:
            return {
                'success': False,
                'stage': 'consistency_validation',
                'errors': consistency_errors
            }
        
        print("  ✓ Table and JSON schema are consistent")
        
        # Create Docling markdown
        docling_content = create_docling_markdown(original_content, schema_data, json_schema)
        
        # Save Docling markdown
        output_path = file_path.parent / f"{file_path.stem}_docling.md"
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(docling_content)
        
        print(f"  ✓ Created Docling markdown: {output_path.name}")
        
        return {
            'success': True,
            'stage': 'completed',
            'errors': [],
            'schema_data': schema_data,
            'json_schema': json_schema,
            'output_path': str(output_path),
            'proposal_status': 'ready_for_stage3b'
        }
        
    except Exception as e:
        return {
            'success': False,
            'stage': 'processing_error',
            'errors': [f"Stage 3a processing failed: {str(e)}"]
        }


def main():
    """Run Stage 3a on Problem objects in review folder."""
    print("🔍 Stage 3a: Problem Object → Docling Markdown Conversion")
    print("=" * 60)
    print("Natural Language First - Validate with JSON, Generate with MD")
    print()
    
    if len(sys.argv) > 1:
        # Process specific file
        file_path = Path(sys.argv[1])
        if not file_path.exists():
            print(f"❌ File not found: {file_path}")
            return
        
        result = process_problem_to_docling_md(file_path)
        
        if result['success']:
            print(f"\n✅ Stage 3a Complete!")
            print(f"📁 Output: {result['output_path']}")
            print(f"🎯 Status: {result['proposal_status']}")
        else:
            print(f"\n❌ Stage 3a Failed at: {result['stage']}")
            for error in result['errors']:
                print(f"  - {error}")
    
    else:
        # Process all Problem objects in review folder
        review_dir = Path("watch_folders/hitl_review")
        if not review_dir.exists():
            print(f"❌ Review directory not found: {review_dir}")
            return
        
        problem_files = [f for f in review_dir.glob("*.md") if "problem" in f.name.lower()]
        if not problem_files:
            print("📭 No Problem object files found in review")
            return
        
        for file_path in problem_files:
            print(f"\n{'='*60}")
            result = process_problem_to_docling_md(file_path)
            
            if result['success']:
                print(f"\n✅ {file_path.name} → Stage 3b")
            else:
                print(f"\n❌ {file_path.name} → Workshop (failed at {result['stage']})")


if __name__ == "__main__":
    main()