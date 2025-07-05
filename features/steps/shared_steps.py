from behave import given
import os

@given('I have the DUX v9.6 split schema files')
def step_impl(context):
    context.schema_root = os.path.join(context.workspace_root, "src", "dux_v9.6_split_schema")
    assert os.path.exists(context.schema_root), f"Schema directory not found at {context.schema_root}"
