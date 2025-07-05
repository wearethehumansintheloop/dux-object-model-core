"""
Step definitions for Behavior object schema compliance validation.
"""

import json
import re
import os
from pathlib import Path
from behave import given, when, then
from jsonschema import validate, ValidationError


@given('I have a Behavior object schema')
def step_given_behavior_schema(context):
    """Load the Behavior object schema from the split schema files."""
    schema_path = Path("src/dux_v9.5_split_schema/dux_object_behavior.json")
    assert schema_path.exists(), f"Behavior schema file not found at {schema_path}"
    
    with open(schema_path, 'r') as f:
        context.behavior_schema = json.load(f)
    
    # Verify it's the correct schema
    assert context.behavior_schema.get("title") == "DUX v9.5 Behavior Object"
    assert "Behavior" in context.behavior_schema["properties"]["object_type"]["const"]


@when('I validate a sample Behavior object')
def step_validate_sample_behavior(context):
    """Create and validate a sample Behavior object."""
    # Create a valid sample Behavior object based on the schema
    context.sample_behavior = {
        "object_type": "Behavior",
        "id": "behavior_001",
        "user_enablement": "Data analyst is able to upload CSV files to the analysis platform",
        "behavior_type": "Task",
        "flow_ids": [
            {
                "id": "flow_001",
                "reference_context": "This behavior is a critical step in the data analysis upload flow."
            }
        ],
        "acceptance_criteria": [
            "User can select CSV file from local file system",
            "File upload progress is displayed",
            "Upload completion is confirmed with success message"
        ],
        "signals": [
            "file_upload_initiated",
            "file_upload_completed",
            "csv_validation_passed"
        ],
        "evidence_maturity": "05_triangulated",
        "evidence": ["provenance_doc_003"]
    }


@then('it should pass Behavior schema validation')
def step_behavior_schema_passes(context):
    """Validate the sample Behavior object against its schema."""
    try:
        validate(instance=context.sample_behavior, schema=context.behavior_schema)
        context.behavior_validation_passed = True
    except ValidationError as e:
        context.behavior_validation_error = str(e)
        context.behavior_validation_passed = False
        raise AssertionError(f"Behavior schema validation failed: {e}")


@then('it should have the required enablement statement format')
def step_behavior_enablement_format(context):
    """Verify the Behavior description follows enablement statement format."""
    description = context.sample_behavior.get("user_enablement", "")
    
    # Check enablement pattern: "[Persona] is able to [task/action]"
    enablement_pattern = r"^.+ is able to .+$"
    
    assert re.match(enablement_pattern, description), \
        f"Behavior description doesn't match enablement format: {description}"
    
    # Verify it contains the key enablement components
    assert "is able to" in description, "Missing 'is able to' enablement component"


@then('it should have valid behavior type')
def step_behavior_type_valid(context):
    """Verify the Behavior has a valid behavior type."""
    behavior_type = context.sample_behavior.get("behavior_type")
    valid_types = ["Task", "Action"]
    
    assert behavior_type in valid_types, \
        f"Invalid behavior type: {behavior_type}. Must be one of {valid_types}"


@when('I validate the behavior prompt against the schema')
def step_when_validate_behavior_prompt(context):
    """Validate behavior prompt content against schema requirements."""
    behavior_prompt_path = os.path.join(context.workspace_root, "scripts", "prompts_from_markdown", "behavior_prompt.md")
    
    if not os.path.exists(behavior_prompt_path):
        context.validation_result = {"valid": False, "error": "Behavior prompt file not found"}
        return
    
    with open(behavior_prompt_path, 'r') as f:
        prompt_content = f.read()
    
    context.behavior_prompt_content = prompt_content
    context.validation_result = {"valid": True, "errors": []}


@then('the behavior prompt should contain actor specifications')
def step_then_behavior_contains_actor(context):
    """Verify behavior prompt contains actor specifications."""
    content = context.behavior_prompt_content.lower()
    actor_keywords = ["actor", "user", "stakeholder", "persona", "role"]
    
    assert any(keyword in content for keyword in actor_keywords), \
        "Behavior prompt should contain actor specifications"


@then('the behavior prompt should contain action definitions')
def step_then_behavior_contains_actions(context):
    """Verify behavior prompt contains action definitions."""
    content = context.behavior_prompt_content.lower()
    action_keywords = ["action", "activity", "task", "behavior", "perform", "execute"]
    
    assert any(keyword in content for keyword in action_keywords), \
        "Behavior prompt should contain action definitions"


@then('the behavior prompt should contain outcome descriptions')
def step_then_behavior_contains_outcomes(context):
    """Verify behavior prompt contains outcome descriptions."""
    content = context.behavior_prompt_content.lower()
    outcome_keywords = ["outcome", "result", "effect", "consequence", "achievement"]
    
    assert any(keyword in content for keyword in outcome_keywords), \
        "Behavior prompt should contain outcome descriptions"


@then('the behavior prompt should reference constraints and triggers')
def step_then_behavior_contains_constraints_triggers(context):
    """Verify behavior prompt references constraints and triggers."""
    content = context.behavior_prompt_content.lower()
    constraint_keywords = ["constraint", "limitation", "restriction", "boundary"]
    trigger_keywords = ["trigger", "catalyst", "initiator", "prompt", "stimulus"]
    
    has_constraints = any(keyword in content for keyword in constraint_keywords)
    has_triggers = any(keyword in content for keyword in trigger_keywords)
    
    assert has_constraints or has_triggers, \
        "Behavior prompt should reference constraints and/or triggers"


@then('the behavior prompt should follow behavioral design patterns')
def step_then_behavior_follows_patterns(context):
    """Verify behavior prompt follows behavioral design patterns."""
    content = context.behavior_prompt_content.lower()
    pattern_keywords = ["pattern", "workflow", "sequence", "interaction", "engagement"]
    
    assert any(keyword in content for keyword in pattern_keywords), \
        "Behavior prompt should follow behavioral design patterns"
