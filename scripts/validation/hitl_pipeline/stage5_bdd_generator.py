#!/usr/bin/env python3
"""
Stage 5: BDD Step Generator (Generation-First)
Purpose: Auto-generate BDD feature files and step definitions from canonical object definitions

Generation-First Principle:
- BDD tests are GENERATED from canonical markdown, not manually maintained
- Step definitions extracted from schema attributes and validation rules
- Feature files updated with current v9.6 object types and relationships
- Cross-object validation based on canonical schema relationships

Usage: python stage5_bdd_generator.py <docling_markdown_path>
"""

import argparse
import json
import re
from pathlib import Path
from typing import Dict, List, Any, Tuple
from datetime import datetime

def extract_object_metadata(docling_content: str) -> Dict[str, Any]:
    """Extract object type and metadata from docling markdown."""
    metadata = {}
    
    # Extract object type from metadata block
    metadata_pattern = r'```yaml\n(.*?)\n```'
    metadata_match = re.search(metadata_pattern, docling_content, re.DOTALL)
    if metadata_match:
        yaml_content = metadata_match.group(1)
        for line in yaml_content.split('\n'):
            if ':' in line:
                key, value = line.split(':', 1)
                metadata[key.strip()] = value.strip()
    
    # Extract object type from header if not in metadata
    if 'object_type' not in metadata:
        header_match = re.search(r'^# (\w+) Object', docling_content, re.MULTILINE)
        if header_match:
            metadata['object_type'] = header_match.group(1)
    
    return metadata

def extract_schema_from_docling(docling_content: str) -> Dict[str, Any]:
    """Extract JSON schema from docling markdown."""
    # Find the Generated JSON Schema section
    schema_pattern = r'## 🔧 Generated JSON Schema.*?\n```json\n(.*?)\n```'
    schema_match = re.search(schema_pattern, docling_content, re.DOTALL)
    
    if schema_match:
        try:
            return json.loads(schema_match.group(1))
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON schema: {e}")
            return {}
    
    return {}

def extract_attributes_table(docling_content: str) -> List[Dict[str, str]]:
    """Extract schema attributes from markdown table."""
    attributes = []
    
    # Find the Schema Attributes table
    table_pattern = r'## 📋 Schema Attributes\n\|.*?\n\|.*?\n((?:\|.*?\n)*)'
    table_match = re.search(table_pattern, docling_content, re.DOTALL)
    
    if table_match:
        table_rows = table_match.group(1).strip().split('\n')
        for row in table_rows:
            if row.startswith('|') and '|' in row[1:]:
                cells = [cell.strip() for cell in row.split('|')[1:-1]]
                if len(cells) >= 4:  # Field, Type, Required, Description
                    attributes.append({
                        'field': cells[0],
                        'type': cells[1], 
                        'required': cells[2],
                        'description': cells[3]
                    })
    
    return attributes

def generate_feature_file(object_type: str, attributes: List[Dict[str, str]], schema: Dict[str, Any]) -> str:
    """Generate BDD feature file for object type."""
    object_lower = object_type.lower()
    
    feature_content = f"""Feature: DUX {object_type} Object Validation (v9.6)
  As a developer working with the DUX object model
  I want to ensure that {object_type} objects are schema-compliant and follow Generation-First principles
  So that the object model maintains consistency and can be processed reliably

  Background:
    Given I have the DUX v9.6 canonical {object_type} object definition
    And I have the generated JSON schema for {object_type} objects

  Scenario: Validate {object_type} object schema compliance
    Given I have a sample {object_type} object
    When I validate it against the {object_type} schema
    Then it should pass {object_type} schema validation
    And it should have all required fields
    And it should follow DUX v9.6 naming conventions

  Scenario: Validate {object_type} required attributes
    Given I have a {object_type} object
    When I check for required attributes
"""
    
    # Add required field validation scenarios
    for attr in attributes:
        if attr['required'].lower() in ['yes', 'true', 'required']:
            feature_content += f"    Then it should have a valid '{attr['field']}' field\n"
    
    feature_content += f"""
  Scenario: Validate {object_type} evidence array structure
    Given I have a {object_type} object with evidence
    When I validate the evidence array
    Then each evidence item should have a 'provenance_id' field
    And each evidence item should have a 'supports_fields' array
    And each evidence item should have a 'quote' field
    And each evidence item should have an 'attribution' field

  Scenario: Validate {object_type} ID naming convention
    Given I have a {object_type} object
    When I check the object ID format
    Then it should follow the pattern '{object_lower}_<descriptor>_<nnn>'
    And it should be unique within the system

  Scenario: Cross-object reference validation for {object_type}
    Given I have a {object_type} object with references to other objects
    When I validate cross-object references
    Then all referenced object IDs should exist
    And all referenced object types should be valid
    And relationship integrity should be maintained
"""

    return feature_content

def generate_step_definitions(object_type: str, attributes: List[Dict[str, str]], schema: Dict[str, Any]) -> str:
    """Generate Python step definitions for object type."""
    object_lower = object_type.lower()
    
    step_content = f'''"""
Generated BDD step definitions for {object_type} object validation (v9.6)
Auto-generated by Stage 5 BDD Generator - DO NOT EDIT MANUALLY

Generation-First Principle: This file is generated from canonical markdown definitions.
To modify, update the canonical {object_type} object definition and regenerate.
"""

import json
import re
from behave import given, when, then
from jsonschema import validate, ValidationError
from pathlib import Path

# Load schema from canonical vault
CANONICAL_VAULT = Path(__file__).parent.parent.parent / "canonical_vault"
SCHEMA_PATH = CANONICAL_VAULT / "dux-core" / "{object_lower}_schema.json"

@given("I have the DUX v9.6 canonical {object_type} object definition")
def step_load_canonical_definition(context):
    """Load canonical {object_type} definition."""
    context.object_type = "{object_type}"
    context.canonical_path = CANONICAL_VAULT / "dux-core" / "{object_lower}_object.md"
    assert context.canonical_path.exists(), f"Canonical {object_type} definition not found"

@given("I have the generated JSON schema for {object_type} objects")
def step_load_schema(context):
    """Load generated JSON schema."""
    if SCHEMA_PATH.exists():
        with open(SCHEMA_PATH) as f:
            context.schema = json.load(f)
    else:
        # Fallback to embedded schema
        context.schema = {schema_json}

@given("I have a sample {object_type} object")
def step_create_sample_object(context):
    """Create a sample {object_type} object for testing."""
    context.sample_object = {{
        "object_type": "{object_type}",
        "id": "{object_lower}_test_001",
'''
    
    # Add sample fields based on attributes
    for attr in attributes:
        field_name = attr['field']
        field_type = attr['type']
        
        if 'string' in field_type.lower():
            if field_name == 'id':
                continue  # Already added
            elif 'array' in field_type.lower():
                step_content += f'        "{field_name}": [],\n'
            else:
                step_content += f'        "{field_name}": "Sample {field_name}",\n'
        elif 'object' in field_type.lower():
            step_content += f'        "{field_name}": {{}},\n'
        elif 'number' in field_type.lower() or 'integer' in field_type.lower():
            step_content += f'        "{field_name}": 1,\n'
        elif 'boolean' in field_type.lower():
            step_content += f'        "{field_name}": true,\n'
    
    step_content += '''    }

@when("I validate it against the {object_type} schema")
def step_validate_schema(context):
    """Validate object against schema."""
    try:
        validate(instance=context.sample_object, schema=context.schema)
        context.validation_result = True
        context.validation_error = None
    except ValidationError as e:
        context.validation_result = False
        context.validation_error = str(e)

@then("it should pass {object_type} schema validation")
def step_check_validation_passed(context):
    """Check that validation passed."""
    assert context.validation_result, f"Schema validation failed: {context.validation_error}"

@then("it should have all required fields")
def step_check_required_fields(context):
    """Check all required fields are present."""
    required_fields = context.schema.get("required", [])
    for field in required_fields:
        assert field in context.sample_object, f"Required field '{field}' missing"

@then("it should follow DUX v9.6 naming conventions")
def step_check_naming_conventions(context):
    """Check naming conventions."""
    object_id = context.sample_object.get("id", "")
    pattern = r"^{object_lower}_[a-z0-9_]+_\d{{3}}$"
    assert re.match(pattern, object_id), f"ID '{object_id}' doesn't follow naming convention"
'''

    # Add attribute-specific validation steps
    for attr in attributes:
        if attr['required'].lower() in ['yes', 'true', 'required']:
            field_name = attr['field']
            step_content += f'''
@then("it should have a valid '{field_name}' field")
def step_check_{field_name.replace(".", "_")}_field(context):
    """Check {field_name} field is valid."""
    assert "{field_name}" in context.sample_object, "'{field_name}' field missing"
    assert context.sample_object["{field_name}"] is not None, "'{field_name}' field is null"
'''

    step_content += '''
@when("I validate the evidence array")
def step_validate_evidence_array(context):
    """Validate evidence array structure."""
    evidence = context.sample_object.get("evidence", [])
    context.evidence_validation = []
    
    for item in evidence:
        validation = {
            "has_provenance_id": "provenance_id" in item,
            "has_supports_fields": "supports_fields" in item,
            "has_quote": "quote" in item,
            "has_attribution": "attribution" in item
        }
        context.evidence_validation.append(validation)

@then("each evidence item should have a 'provenance_id' field")
def step_check_provenance_id(context):
    """Check provenance_id in evidence."""
    for validation in context.evidence_validation:
        assert validation["has_provenance_id"], "Evidence missing provenance_id"

@then("each evidence item should have a 'supports_fields' array")  
def step_check_supports_fields(context):
    """Check supports_fields in evidence."""
    for validation in context.evidence_validation:
        assert validation["has_supports_fields"], "Evidence missing supports_fields"

@then("each evidence item should have a 'quote' field")
def step_check_quote_field(context):
    """Check quote in evidence."""
    for validation in context.evidence_validation:
        assert validation["has_quote"], "Evidence missing quote"

@then("each evidence item should have an 'attribution' field")
def step_check_attribution_field(context):
    """Check attribution in evidence."""
    for validation in context.evidence_validation:
        assert validation["has_attribution"], "Evidence missing attribution"
'''

    return step_content

def generate_bdd_artifacts(docling_path: Path) -> Tuple[str, str]:
    """Generate BDD feature file and step definitions from docling markdown."""
    docling_content = docling_path.read_text()
    
    # Extract metadata and schema
    metadata = extract_object_metadata(docling_content)
    object_type = metadata.get('object_type', 'Unknown')
    schema = extract_schema_from_docling(docling_content)
    attributes = extract_attributes_table(docling_content)
    
    # Generate artifacts
    feature_content = generate_feature_file(object_type, attributes, schema)
    step_content = generate_step_definitions(object_type, attributes, schema)
    
    return feature_content, step_content

def main():
    parser = argparse.ArgumentParser(description='Generate BDD artifacts from docling markdown')
    parser.add_argument('docling_path', type=Path, help='Path to docling markdown file')
    parser.add_argument('--output-dir', type=Path, default=Path('features'), help='Output directory for generated files')
    
    args = parser.parse_args()
    
    if not args.docling_path.exists():
        print(f"Error: Docling file not found: {args.docling_path}")
        return 1
    
    try:
        # Generate artifacts
        feature_content, step_content = generate_bdd_artifacts(args.docling_path)
        
        # Extract object type for file naming
        docling_content = args.docling_path.read_text()
        metadata = extract_object_metadata(docling_content)
        object_type = metadata.get('object_type', 'unknown').lower()
        
        # Ensure output directories exist
        features_dir = args.output_dir
        steps_dir = features_dir / 'steps'
        features_dir.mkdir(parents=True, exist_ok=True)
        steps_dir.mkdir(parents=True, exist_ok=True)
        
        # Write feature file
        feature_file = features_dir / f"{object_type}_validation.feature"
        feature_file.write_text(feature_content)
        print(f"✅ Generated feature file: {feature_file}")
        
        # Write step definitions
        steps_file = steps_dir / f"{object_type}_validation_steps.py"
        steps_file.write_text(step_content)
        print(f"✅ Generated step definitions: {steps_file}")
        
        # Add generation metadata
        timestamp = datetime.now().isoformat()
        metadata_file = features_dir / f"{object_type}_generation_metadata.json"
        generation_metadata = {
            "generated_at": timestamp,
            "source_docling": str(args.docling_path),
            "object_type": object_type,
            "generation_method": "stage5_bdd_generator",
            "artifacts": [str(feature_file), str(steps_file)]
        }
        metadata_file.write_text(json.dumps(generation_metadata, indent=2))
        print(f"✅ Generated metadata: {metadata_file}")
        
        print(f"\n🎉 BDD artifacts generated for {object_type} object")
        return 0
        
    except Exception as e:
        print(f"❌ Error generating BDD artifacts: {e}")
        return 1

if __name__ == "__main__":
    exit(main())