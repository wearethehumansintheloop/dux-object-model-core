from behave import given
import os
import json

@given('I have the DUX v9.6 split schema files')
def step_impl(context):
    context.schema_root = os.path.join(context.workspace_root, "src", "dux_v9.6_split_schema")
    assert os.path.exists(context.schema_root), f"Schema directory not found at {context.schema_root}"
    context.schemas = {}
    for schema_file in os.listdir(context.schema_root):
        if schema_file.endswith('.json'):
            with open(os.path.join(context.schema_root, schema_file), 'r') as f:
                context.schemas[schema_file] = json.load(f)
