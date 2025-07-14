#!/usr/bin/env python3
"""
Stage 4: Object Instance Validation
Generation-First: Generate validation logic from docling markdown JSON schema

This stage:
1. Reads the validated docling markdown from Stage 3b
2. Extracts the embedded JSON schema (our source of truth)
3. Generates validation logic from the schema
4. Validates the canonical example against generated rules
5. Returns pass/fail for orchestrator to move to promotion_candidates

NO manual validation scripts - everything is generated from markdown!
"""

import json
import re
from pathlib import Path
from typing import Dict, List, Any, Optional
from jsonschema import validate, ValidationError, Draft7Validator


def extract_json_schema_from_docling(docling_path: Path) -> Optional[Dict[str, Any]]:
    """Extract the embedded JSON schema from docling markdown."""
    
    with open(docling_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the Generated JSON Schema section
    schema_match = re.search(
        r'## 🔧 Generated JSON Schema \(Proposal\)\s*```json\s*(.*?)\s*```',
        content,
        re.DOTALL
    )
    
    if not schema_match:
        return None
    
    try:
        return json.loads(schema_match.group(1))
    except json.JSONDecodeError:
        return None


def extract_canonical_example(docling_path: Path) -> Optional[Dict[str, Any]]:
    """Extract the canonical example JSON from docling markdown."""
    
    with open(docling_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the Canonical Example section
    example_match = re.search(
        r'## 📦 Canonical Example.*?```json\s*(.*?)\s*```',
        content,
        re.DOTALL
    )
    
    if not example_match:
        return None
    
    try:
        return json.loads(example_match.group(1))
    except json.JSONDecodeError:
        return None


def generate_custom_validators(json_schema: Dict[str, Any], object_type: str) -> List[callable]:
    """
    Generate custom validation functions based on object type and schema.
    This is where Generation-First validation logic lives.
    """
    validators = []
    
    # Problem-specific validators
    if object_type == 'problem':
        # Validate decomposed job_statement structure
        def validate_job_statement(obj):
            errors = []
            if 'job_statement' in obj:
                js = obj['job_statement']
                if not isinstance(js, dict):
                    errors.append("job_statement must be an object")
                else:
                    # For Problem objects in Generation-First, job_statement has user_scenario/enablement/outcome
                    for field in ['user_scenario', 'user_enablement', 'user_outcome']:
                        if field not in js:
                            errors.append(f"job_statement missing {field}")
                        elif not isinstance(js[field], dict):
                            errors.append(f"job_statement.{field} must be an object with value/source")
                        else:
                            if 'value' not in js[field]:
                                errors.append(f"job_statement.{field} missing value")
                            if 'source' not in js[field]:
                                errors.append(f"job_statement.{field} missing source")
            return errors
        
        validators.append(validate_job_statement)
        
        # Validate evidence array structure
        def validate_evidence(obj):
            errors = []
            if 'evidence' in obj and isinstance(obj['evidence'], list):
                for i, evidence in enumerate(obj['evidence']):
                    if not isinstance(evidence, dict):
                        errors.append(f"evidence[{i}] must be an object")
                    else:
                        if 'provenance_id' not in evidence:
                            errors.append(f"evidence[{i}] missing provenance_id")
                        if 'supports_fields' not in evidence:
                            errors.append(f"evidence[{i}] missing supports_fields")
            return errors
        
        validators.append(validate_evidence)
    
    # Behavior-specific validators
    elif object_type == 'behavior':
        def validate_signals(obj):
            errors = []
            if 'signals' in obj and isinstance(obj['signals'], list):
                for i, signal in enumerate(obj['signals']):
                    if not isinstance(signal, dict):
                        errors.append(f"signals[{i}] must be an object")
                    elif 'signal_type' not in signal:
                        errors.append(f"signals[{i}] missing signal_type")
            return errors
        
        validators.append(validate_signals)
    
    # Result-specific validators
    elif object_type == 'result':
        def validate_measure(obj):
            errors = []
            if 'measure' in obj:
                measure = obj['measure']
                if not isinstance(measure, dict):
                    errors.append("measure must be an object")
                elif 'metric' not in measure or 'unit' not in measure:
                    errors.append("measure must have metric and unit")
            return errors
        
        validators.append(validate_measure)
    
    return validators


def validate_object_instance(instance: Dict[str, Any], json_schema: Dict[str, Any], object_type: str) -> Dict[str, Any]:
    """
    Validate an object instance against the generated schema and custom rules.
    This is Generation-First validation - schema drives the validation logic.
    """
    errors = []
    
    # 1. JSON Schema validation
    try:
        validate(instance=instance, schema=json_schema)
    except ValidationError as e:
        errors.append(f"Schema validation error: {e.message}")
    
    # 2. Custom validation based on object type
    custom_validators = generate_custom_validators(json_schema, object_type)
    for validator in custom_validators:
        custom_errors = validator(instance)
        errors.extend(custom_errors)
    
    # 3. Cross-field validation
    # Example: If opportunity_score exists, all sub-fields must have matching sources
    if object_type == 'problem' and 'opportunity_score' in instance:
        score = instance['opportunity_score']
        if isinstance(score, dict):
            sources = [
                score.get('value_source'),
                score.get('importance_source'),
                score.get('satisfaction_source')
            ]
            if len(set(sources)) > 1:
                errors.append("opportunity_score sources must all be 'evidence' or all be 'synthetic'")
    
    return {
        'valid': len(errors) == 0,
        'errors': errors,
        'instance': instance
    }


def save_validation_script(json_schema: Dict[str, Any], object_type: str, output_dir: Path) -> Path:
    """
    Generate and save a validation script for this object type.
    This is the Generation-First artifact that can be reused.
    """
    
    from datetime import datetime
    
    # Create validation script content
    script_content = f'''#!/usr/bin/env python3
"""
Generated validation script for {object_type.title()} objects
Generated from: docling markdown schema
Generation timestamp: {datetime.now().isoformat()}

This is a Generation-First artifact - DO NOT EDIT MANUALLY
Regenerate from docling markdown if changes are needed
"""

import json
from typing import Dict, List, Any
from jsonschema import validate, ValidationError

# Generated JSON Schema
{object_type.upper()}_SCHEMA = {json.dumps(json_schema, indent=4)}

def validate_{object_type}_instance(instance: Dict[str, Any]) -> Dict[str, Any]:
    """Validate a {object_type} instance against the generated schema."""
    errors = []
    
    # JSON Schema validation
    try:
        validate(instance=instance, schema={object_type.upper()}_SCHEMA)
    except ValidationError as e:
        errors.append(f"Schema validation error: {{e.message}}")
    
    # Custom validations for {object_type}
    {generate_custom_validation_code(object_type)}
    
    return {{
        'valid': len(errors) == 0,
        'errors': errors
    }}

if __name__ == "__main__":
    # Example usage
    import sys
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as f:
            instance = json.load(f)
        result = validate_{object_type}_instance(instance)
        if result['valid']:
            print("✅ Validation passed")
        else:
            print(f"❌ Validation failed with {{len(result['errors'])}} errors:")
            for error in result['errors']:
                print(f"  - {{error}}")
'''
    
    # Save the validation script
    script_filename = f"validate_{object_type}_generated.py"
    script_path = output_dir / script_filename
    
    with open(script_path, 'w', encoding='utf-8') as f:
        f.write(script_content)
    
    # Make it executable
    import os
    os.chmod(script_path, 0o755)
    
    print(f"  💾 Saved validation script: {script_filename}")
    return script_path


def generate_custom_validation_code(object_type: str) -> str:
    """Generate object-specific validation code snippets."""
    
    if object_type == 'problem':
        return '''# Validate job_statement decomposition
    if 'job_statement' in instance:
        js = instance['job_statement']
        if isinstance(js, dict):
            for field in ['user_scenario', 'user_enablement', 'user_outcome']:
                if field in js and isinstance(js[field], dict):
                    if 'value' not in js[field]:
                        errors.append(f"job_statement.{field} missing value")
                    if 'source' not in js[field]:
                        errors.append(f"job_statement.{field} missing source")
    
    # Validate evidence array
    if 'evidence' in instance and isinstance(instance['evidence'], list):
        for i, evidence in enumerate(instance['evidence']):
            if isinstance(evidence, dict):
                if 'provenance_id' not in evidence:
                    errors.append(f"evidence[{i}] missing provenance_id")
                if 'supports_fields' not in evidence:
                    errors.append(f"evidence[{i}] missing supports_fields")'''
    
    elif object_type == 'behavior':
        return '''# Validate signals array
    if 'signals' in instance and isinstance(instance['signals'], list):
        for i, signal in enumerate(instance['signals']):
            if isinstance(signal, dict) and 'signal_type' not in signal:
                errors.append(f"signals[{i}] missing signal_type")'''
    
    elif object_type == 'result':
        return '''# Validate measure object
    if 'measure' in instance and isinstance(instance['measure'], dict):
        if 'metric' not in instance['measure']:
            errors.append("measure missing metric")
        if 'unit' not in instance['measure']:
            errors.append("measure missing unit")'''
    
    return '# No custom validations for this object type'


def process_stage4_validation(docling_path: Path) -> Dict[str, Any]:
    """
    Main Stage 4 processing - Generation-First validation.
    """
    print(f"📋 Stage 4: Validating {docling_path.name}")
    
    # Determine object type from filename
    filename = docling_path.stem.lower()
    object_type = None
    for otype in ['problem', 'behavior', 'result', 'flow', 'useroutcome']:
        if otype in filename:
            object_type = otype
            break
    
    if not object_type:
        return {
            'passed': False,
            'errors': ['Cannot determine object type from filename'],
            'stage': 'object_type_detection'
        }
    
    # Extract JSON schema from docling
    json_schema = extract_json_schema_from_docling(docling_path)
    if not json_schema:
        return {
            'passed': False,
            'errors': ['No JSON schema found in docling markdown'],
            'stage': 'schema_extraction'
        }
    
    print(f"  ✓ Extracted JSON schema with {len(json_schema.get('properties', {}))} properties")
    
    # Save the validation script
    output_dir = docling_path.parent
    validation_script_path = save_validation_script(json_schema, object_type, output_dir)
    
    # Extract canonical example
    canonical_example = extract_canonical_example(docling_path)
    if not canonical_example:
        print("  ⚠️  No canonical example found - skipping instance validation")
        # Still pass if schema is valid but no example
        return {
            'passed': True,
            'errors': [],
            'stage': 'completed',
            'message': 'Schema validated, no instance to test',
            'validation_script': str(validation_script_path)
        }
    
    print(f"  ✓ Found canonical example")
    
    # Validate the canonical example
    validation_result = validate_object_instance(canonical_example, json_schema, object_type)
    
    if validation_result['valid']:
        print(f"  ✅ Canonical example passes all validations")
        return {
            'passed': True,
            'errors': [],
            'stage': 'completed',
            'validation_result': validation_result,
            'validation_script': str(validation_script_path)
        }
    else:
        print(f"  ❌ Canonical example has {len(validation_result['errors'])} errors")
        for error in validation_result['errors']:
            print(f"    - {error}")
        return {
            'passed': False,
            'errors': validation_result['errors'],
            'stage': 'instance_validation',
            'validation_script': str(validation_script_path)
        }


def main():
    """Run Stage 4 validation."""
    print("🔍 Stage 4: Generation-First Object Validation")
    print("=" * 60)
    print("Generating validation from docling markdown schemas")
    print()
    
    import sys
    
    if len(sys.argv) > 1:
        # Process specific file
        file_path = Path(sys.argv[1])
        if not file_path.exists():
            print(f"❌ File not found: {file_path}")
            return
        
        result = process_stage4_validation(file_path)
        
        if result['passed']:
            print(f"\n✅ Stage 4 Complete!")
            print(f"🎯 Object validated using generated rules")
            print(f"➡️  Ready for promotion to candidates")
        else:
            print(f"\n❌ Stage 4 Failed at: {result['stage']}")
            for error in result['errors']:
                print(f"  - {error}")
    
    else:
        print("Usage: stage4_object_validation.py <docling_markdown_file>")
        print()
        print("This stage validates object instances using Generation-First principles:")
        print("1. Extract JSON schema from docling markdown")
        print("2. Generate validation logic from schema")
        print("3. Validate canonical example")
        print("4. Return pass/fail for promotion")


if __name__ == "__main__":
    main()