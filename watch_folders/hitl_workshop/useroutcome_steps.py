"""
Step definitions for UserOutcome object schema compliance validation.
"""

import json
import re
from pathlib import Path
from behave import given, when, then
from jsonschema import validate, ValidationError


@given('I have a UserOutcome object schema')
def step_given_useroutcome_schema(context):
    """Load the UserOutcome object schema from the split schema files."""
    schema_path = Path("src/dux_v9.4_split_schema/dux_object_useroutcome.json")
    assert schema_path.exists(), f"UserOutcome schema file not found at {schema_path}"
    
    with open(schema_path, 'r') as f:
        context.useroutcome_schema = json.load(f)
    
    # Verify it's the correct schema
    assert "UserOutcome" in context.useroutcome_schema["properties"]["object_type"]["const"]


@when('I validate a sample UserOutcome object')
def step_validate_sample_useroutcome(context):
    """Create and validate a sample UserOutcome object."""
    # Create a valid sample UserOutcome object based on the schema
    context.sample_useroutcome = {
        "object_type": "UserOutcome",
        "id": "useroutcome_001",
        "user_scenario": "Data scientists need faster model training to iterate more quickly",
        "outcome_statement": "Data scientists complete model training 50% faster (from 4 hours to 2 hours) by Q3.",
        "target_impact_when_achieved": "Increased experimentation velocity and faster time to production",
        "priority": "critical",
        "related_problem_ids": ["problem_001"],
        "related_problem_ids_evidence_status": "evidence_backed",
        "related_result_ids": ["result_001", "result_002"]
    }


@then('it should pass UserOutcome schema validation')
def step_useroutcome_schema_passes(context):
    """Validate the sample UserOutcome object against its schema."""
    try:
        validate(instance=context.sample_useroutcome, schema=context.useroutcome_schema)
        context.useroutcome_validation_passed = True
    except ValidationError as e:
        context.useroutcome_validation_error = str(e)
        context.useroutcome_validation_passed = False
        raise AssertionError(f"UserOutcome schema validation failed: {e}")


@then('it should have the required outcome statement format')
def step_useroutcome_statement_format(context):
    """Verify the UserOutcome has the required Key Result format."""
    outcome_statement = context.sample_useroutcome.get("outcome_statement", "")
    
    # Check Key Result pattern: Must start with capital, end with period/exclamation
    statement_pattern = r"^[A-Z][^.]*[.!]$"
    
    assert re.match(statement_pattern, outcome_statement), \
        f"UserOutcome statement doesn't match required format: {outcome_statement}"
    
    # Should contain key elements: WHO, DOES WHAT, BY HOW MUCH, BY TIMEFRAME
    assert len(outcome_statement.strip()) > 0, "Outcome statement cannot be empty"


@then('it should have valid priority level')
def step_useroutcome_priority_valid(context):
    """Verify the UserOutcome has a valid priority level."""
    priority = context.sample_useroutcome.get("priority")
    valid_priorities = ["critical", "important", "nice_to_have"]
    
    assert priority in valid_priorities, \
        f"Invalid priority: {priority}. Must be one of {valid_priorities}"

@given('a UserOutcome object with a specific ID')
def step_impl(context):
    context.useroutcome_data = json.loads(context.text)
    context.useroutcome_id = context.useroutcome_data.get("user_outcome_id")

@when('I search for the UserOutcome by its ID')
def step_impl(context):
    """Search for the UserOutcome object by its ID."""
    useroutcome_id = context.useroutcome_id
    
    # Simulate a search by ID (in real scenario, this would query a database or service)
    if useroutcome_id == "useroutcome_001":
        context.found_useroutcome = context.sample_useroutcome
    else:
        context.found_useroutcome = None

@then('the found UserOutcome should match the sample UserOutcome')
def step_impl(context):
    """Verify the found UserOutcome matches the sample UserOutcome."""
    assert context.found_useroutcome is not None, "UserOutcome not found"
    assert context.found_useroutcome == context.sample_useroutcome, "Found UserOutcome does not match sample"
