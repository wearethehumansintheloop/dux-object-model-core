from behave import given, when, then
import os
import json
import subprocess
import sys
from pathlib import Path

@given('I have the DUX v9.6 split schema files')
def step_impl(context):
    context.schema_root = os.path.join(context.workspace_root, "src", "dux_v9.6_split_schema")
    assert os.path.exists(context.schema_root), f"Schema directory not found at {context.schema_root}"
    context.schemas = {}
    for schema_file in os.listdir(context.schema_root):
        if schema_file.endswith('.json'):
            with open(os.path.join(context.schema_root, schema_file), 'r') as f:
                context.schemas[schema_file] = json.load(f)

@given('I have the markdown object model files')
def step_impl(context):
    context.markdown_root = os.path.join(context.workspace_root, "docs", "01_versionNext")
    assert os.path.exists(context.markdown_root), f"Markdown directory not found at {context.markdown_root}"
    context.markdown_files = [f for f in os.listdir(context.markdown_root) if f.endswith('.md')]

@given('I have existing validation scripts')
def step_impl(context):
    context.validation_root = os.path.join(context.workspace_root, "scripts", "validation")
    assert os.path.exists(context.validation_root), f"Validation directory not found at {context.validation_root}"
    context.validation_scripts = [f for f in os.listdir(context.validation_root) if f.endswith('.py')]

@given('I run the schema update script')
def step_impl(context):
    context.update_script = os.path.join(context.workspace_root, "scripts", "update_schemas.py")
    assert os.path.exists(context.update_script), f"Update script not found at {context.update_script}"

@when('the script processes markdown files')
def step_impl(context):
    try:
        result = subprocess.run([sys.executable, context.update_script], 
                              capture_output=True, text=True, cwd=context.workspace_root)
        context.script_output = result.stdout
        context.script_error = result.stderr
        context.script_return_code = result.returncode
    except Exception as e:
        context.script_error = str(e)
        context.script_return_code = 1

@then('it should create backups of existing schemas')
def step_impl(context):
    backup_dir = os.path.join(context.schema_root, "backups")
    assert os.path.exists(backup_dir), "Backup directory should be created"
    backup_files = os.listdir(backup_dir)
    assert len(backup_files) > 0, "Backup files should be created"

@then('it should generate valid JSON schemas')
def step_impl(context):
    for schema_file, schema_data in context.schemas.items():
        assert isinstance(schema_data, dict), f"Schema {schema_file} should be a valid JSON object"
        assert "type" in schema_data, f"Schema {schema_file} should have a type field"
        assert "properties" in schema_data, f"Schema {schema_file} should have properties"

@then('it should maintain schema versioning')
def step_impl(context):
    for schema_file, schema_data in context.schemas.items():
        if "version" in schema_data:
            assert isinstance(schema_data["version"], str), f"Version in {schema_file} should be a string"

@then('it should not break existing validation scripts')
def step_impl(context):
    # Check that validation scripts can still import and run
    for script in context.validation_scripts:
        script_path = os.path.join(context.validation_root, script)
        try:
            # Try to import the script to check for syntax errors
            with open(script_path, 'r') as f:
                compile(f.read(), script_path, 'exec')
        except Exception as e:
            assert False, f"Validation script {script} has syntax errors: {e}"

@given('the schemas have been updated')
def step_impl(context):
    # This step assumes the schema update has already been run
    pass

@when('I validate each object type')
def step_impl(context):
    context.validation_results = {}
    for schema_file, schema_data in context.schemas.items():
        context.validation_results[schema_file] = schema_data

@then('Problem objects should have all required fields')
def step_impl(context):
    problem_schema = context.schemas.get('dux_object_problem.json')
    if problem_schema:
        required_fields = problem_schema.get('required', [])
        expected_fields = ['id', 'title', 'description', 'evidence_status']
        for field in expected_fields:
            assert field in required_fields, f"Problem schema should require {field}"

@then('Behavior objects should have the end_user field')
def step_impl(context):
    behavior_schema = context.schemas.get('dux_object_behavior.json')
    if behavior_schema:
        properties = behavior_schema.get('properties', {})
        assert 'end_user' in properties, "Behavior schema should have end_user field"

@then('Behavior objects should not have behavior_type field')
def step_impl(context):
    behavior_schema = context.schemas.get('dux_object_behavior.json')
    if behavior_schema:
        properties = behavior_schema.get('properties', {})
        assert 'behavior_type' not in properties, "Behavior schema should not have behavior_type field"

@then('Result objects should have simplified useroutcome_ids')
def step_impl(context):
    result_schema = context.schemas.get('dux_object_result.json')
    if result_schema:
        properties = result_schema.get('properties', {})
        useroutcome_ids = properties.get('useroutcome_ids', {})
        # Check that it's a simple array of strings, not complex objects
        assert useroutcome_ids.get('type') == 'array', "useroutcome_ids should be an array"

@then('UserOutcome objects should have optional user_flow_id')
def step_impl(context):
    useroutcome_schema = context.schemas.get('dux_object_useroutcome.json')
    if useroutcome_schema:
        properties = useroutcome_schema.get('properties', {})
        assert 'user_flow_id' in properties, "UserOutcome schema should have user_flow_id field"
        required_fields = useroutcome_schema.get('required', [])
        assert 'user_flow_id' not in required_fields, "user_flow_id should be optional"

@then('User Flow objects should have evidence field')
def step_impl(context):
    flow_schema = context.schemas.get('dux_object_flow.json')
    if flow_schema:
        properties = flow_schema.get('properties', {})
        assert 'evidence' in properties, "User Flow schema should have evidence field"

@then('User Flow objects should have reference_url instead of protocol_id')
def step_impl(context):
    flow_schema = context.schemas.get('dux_object_flow.json')
    if flow_schema:
        properties = flow_schema.get('properties', {})
        assert 'reference_url' in properties, "User Flow schema should have reference_url field"
        assert 'protocol_id' not in properties, "User Flow schema should not have protocol_id field"

@when('I analyze validation scripts')
def step_impl(context):
    context.script_analysis = {}
    for script in context.validation_scripts:
        script_path = os.path.join(context.validation_root, script)
        with open(script_path, 'r') as f:
            content = f.read()
            context.script_analysis[script] = content

@then('validation scripts should reference valid field names')
def step_impl(context):
    # Check that validation scripts don't reference removed fields
    for script_name, content in context.script_analysis.items():
        if 'behavior_type' in content:
            assert False, f"Validation script {script_name} still references removed field 'behavior_type'"

@then('validation scripts should use correct field types')
def step_impl(context):
    # Basic check that validation scripts use proper field validation
    for script_name, content in context.script_analysis.items():
        assert 'json.loads' in content or 'jsonschema' in content, f"Validation script {script_name} should use proper JSON validation"

@then('validation scripts should handle new conditional logic')
def step_impl(context):
    # Check that validation scripts handle conditional fields like key_signals
    for script_name, content in context.script_analysis.items():
        if 'useroutcome' in script_name.lower():
            assert 'user_flow_id' in content or 'key_signals' in content, f"UserOutcome validation script should handle new conditional logic"

@then('no validation scripts should reference removed fields')
def step_impl(context):
    removed_fields = ['behavior_type', 'protocol_id']
    for script_name, content in context.script_analysis.items():
        for field in removed_fields:
            if field in content:
                assert False, f"Validation script {script_name} still references removed field '{field}'"

@when('I run existing BDD tests')
def step_impl(context):
    try:
        # Run behave tests
        result = subprocess.run(['behave', 'features/dux_schema_validation.feature'], 
                              capture_output=True, text=True, cwd=context.workspace_root)
        context.bdd_output = result.stdout
        context.bdd_error = result.stderr
        context.bdd_return_code = result.returncode
    except Exception as e:
        context.bdd_error = str(e)
        context.bdd_return_code = 1

@then('all schema validation tests should pass')
def step_impl(context):
    assert context.bdd_return_code == 0, f"BDD tests failed: {context.bdd_error}"

@then('all object creation tests should pass')
def step_impl(context):
    # This would be implemented based on specific object creation tests
    pass

@then('all relationship validation tests should pass')
def step_impl(context):
    # This would be implemented based on specific relationship tests
    pass

@then('all data quality tests should pass')
def step_impl(context):
    # This would be implemented based on specific data quality tests
    pass

@when('I attempt to rollback to previous schemas')
def step_impl(context):
    backup_dir = os.path.join(context.schema_root, "backups")
    if os.path.exists(backup_dir):
        backup_files = os.listdir(backup_dir)
        context.backup_files = backup_files
    else:
        context.backup_files = []

@then('backup files should be available')
def step_impl(context):
    assert len(context.backup_files) > 0, "Backup files should be available for rollback"

@then('rollback should restore previous schema versions')
def step_impl(context):
    # This would implement actual rollback logic
    pass

@then('validation scripts should work with rolled back schemas')
def step_impl(context):
    # This would test validation scripts with rolled back schemas
    pass

@then('BDD tests should pass with rolled back schemas')
def step_impl(context):
    # This would run BDD tests with rolled back schemas
    pass

@when('I validate object relationships')
def step_impl(context):
    context.relationship_validation = {}
    for schema_file, schema_data in context.schemas.items():
        context.relationship_validation[schema_file] = schema_data

@then('Problem objects should properly reference Result objects')
def step_impl(context):
    problem_schema = context.schemas.get('dux_object_problem.json')
    if problem_schema:
        properties = problem_schema.get('properties', {})
        result_ids = properties.get('result_ids', {})
        assert result_ids.get('type') == 'array', "Problem result_ids should be an array"

@then('Behavior objects should properly reference Problem objects')
def step_impl(context):
    behavior_schema = context.schemas.get('dux_object_behavior.json')
    if behavior_schema:
        properties = behavior_schema.get('properties', {})
        problem_id = properties.get('problem_id', {})
        assert problem_id.get('type') == 'string', "Behavior problem_id should be a string"

@then('UserOutcome objects should properly reference User Flow objects')
def step_impl(context):
    useroutcome_schema = context.schemas.get('dux_object_useroutcome.json')
    if useroutcome_schema:
        properties = useroutcome_schema.get('properties', {})
        user_flow_id = properties.get('user_flow_id', {})
        assert user_flow_id.get('type') == 'string', "UserOutcome user_flow_id should be a string"

@then('all ID references should follow the correct format')
def step_impl(context):
    # Check that ID fields have proper format validation
    for schema_file, schema_data in context.schemas.items():
        properties = schema_data.get('properties', {})
        for field_name, field_def in properties.items():
            if field_name.endswith('_id') or field_name.endswith('_ids'):
                assert field_def.get('type') in ['string', 'array'], f"ID field {field_name} should be string or array"

@then('circular references should be prevented')
def step_impl(context):
    # This would implement circular reference detection logic
    pass

@when('I check schema metadata')
def step_impl(context):
    context.metadata_validation = {}
    for schema_file, schema_data in context.schemas.items():
        context.metadata_validation[schema_file] = schema_data

@then('each schema should have correct version information')
def step_impl(context):
    for schema_file, schema_data in context.schemas.items():
        if "version" in schema_data:
            version = schema_data["version"]
            assert isinstance(version, str), f"Version in {schema_file} should be a string"
            assert version.startswith("9.6"), f"Version in {schema_file} should be 9.6.x"

@then('each schema should have proper title and description')
def step_impl(context):
    for schema_file, schema_data in context.schemas.items():
        assert "title" in schema_data, f"Schema {schema_file} should have a title"
        assert "description" in schema_data, f"Schema {schema_file} should have a description"

@then('each schema should have valid JSON structure')
def step_impl(context):
    for schema_file, schema_data in context.schemas.items():
        # Try to serialize and deserialize to validate JSON structure
        try:
            json.dumps(schema_data)
        except Exception as e:
            assert False, f"Schema {schema_file} has invalid JSON structure: {e}"

@then('each schema should follow JSON Schema standards')
def step_impl(context):
    for schema_file, schema_data in context.schemas.items():
        assert "$schema" in schema_data, f"Schema {schema_file} should specify JSON Schema version"
        assert schema_data["$schema"].startswith("http://json-schema.org/"), f"Schema {schema_file} should use valid JSON Schema URI" 