
import os
import json
from behave import given, when, then
from jsonschema import validate, ValidationError

@given('I have sample objects in the test data folder')
def step_impl(context):
    context.sample_objects = []
    test_data_path = os.path.join(os.path.dirname(__file__), '../test_data')
    for filename in os.listdir(test_data_path):
        if filename.endswith('.json'):
            with open(os.path.join(test_data_path, filename)) as f:
                context.sample_objects.append(json.load(f))

@when('I validate each sample object against its schema')
def step_impl(context):
    context.validation_results = []
    schema_dir = os.path.join(os.path.dirname(__file__), '../schemas')
    for obj in context.sample_objects:
        object_type = obj.get("object_type", "").lower()
        schema_file = f"dux_object_{object_type}.json"
        schema_path = os.path.join(schema_dir, schema_file)
        try:
            with open(schema_path) as f:
                schema = json.load(f)
            validate(instance=obj, schema=schema)
            context.validation_results.append((object_type, True))
        except (ValidationError, FileNotFoundError, json.JSONDecodeError) as e:
            context.validation_results.append((object_type, False, str(e)))

@then('all objects should pass their respective schema validation')
def step_impl(context):
    failures = [result for result in context.validation_results if not result[1]]
    assert not failures, f"Schema validation failed for: {failures}"

@then('related object references should be properly formatted')
def step_impl(context):
    for obj in context.sample_objects:
        for key in obj:
            if key.endswith("_ids") and isinstance(obj[key], list):
                for ref in obj[key]:
                    assert isinstance(ref, str) and len(ref) > 0, f"Invalid reference in {key}: {ref}"
            if key.endswith("_evidence_status"):
                assert isinstance(obj[key], str), f"Invalid evidence status in {key}: {obj[key]}"
