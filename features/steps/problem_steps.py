"""
Step definitions for Problem Object validation
Tests Problem object extraction and schema compliance
"""

import json
import re
from pathlib import Path
from behave import given, when, then
from jsonschema import validate, ValidationError


@given('I have a Problem object schema')
def step_have_problem_schema(context):
    """Load the Problem object schema from the split schema files."""
    schema_path = Path("src/dux_v9.5_split_schema/dux_object_problem.json")
    assert schema_path.exists(), f"Problem schema file not found at {schema_path}"
    
    with open(schema_path, 'r') as f:
        context.problem_schema = json.load(f)
    
    # Verify it's the correct schema
    assert context.problem_schema.get("title") == "DUX v9.5 Problem Object"
    assert "Problem" in context.problem_schema["properties"]["object_type"]["const"]


@when('I validate a sample Problem object')
def step_validate_sample_problem(context):
    """Create and validate a sample Problem object."""
    # Create a valid sample Problem object based on the schema
    context.sample_problem = {
        "object_type": "Problem",
        "id": "problem_001",
        "job_statement": "When conducting data analysis, I want to process large datasets efficiently, so I can deliver insights faster.",
        "what_is_at_stake": "Time to insight and analysis productivity",
        "protocol_url": "https://example.com/protocol",
        "end_user": ["Data Analyst"],
        "result_ids": [
            {
                "id": "result_001",
                "reference_context": "Shared data analysis workflow"
            }
        ],
        "useroutcome_ids": [
            {
                "id": "useroutcome_001",
                "reference_context": "This problem is a key blocker for achieving the user outcome of faster model training."
            }
        ],
        "flow_ids": [
            {
                "id": "flow_001",
                "reference_context": "The data analysis upload flow is directly impacted by this problem."
            }
        ],
        "evidence_maturity": "04_balanced_signal",
        "evidence": ["provenance_doc_001", "provenance_doc_002"]
    }


@then('it should pass Problem schema validation')
def step_problem_schema_passes(context):
    """Validate the sample Problem object against its schema."""
    try:
        validate(instance=context.sample_problem, schema=context.problem_schema)
        context.problem_validation_passed = True
    except ValidationError as e:
        context.problem_validation_error = str(e)
        context.problem_validation_passed = False
        raise AssertionError(f"Problem schema validation failed: {e}")


@then('it should have the required JTBD format description')
def step_problem_jtbd_format(context):
    """Verify the Problem description follows JTBD format."""
    description = context.sample_problem.get("job_statement", "")
    
    # Check JTBD pattern: "When [situation], I want [motivation], so I can [outcome]."
    jtbd_pattern = r"^When .+, I want .+, so I can .+\.$"
    
    assert re.match(jtbd_pattern, description), \
        f"Problem description doesn't match JTBD format: {description}"
    
    # Verify it contains the three key JTBD components
    assert "When " in description, "Missing 'When' situation component"
    assert "I want " in description, "Missing 'I want' motivation component"
    assert "so I can " in description, "Missing 'so I can' outcome component"


@then('it should have valid evidence status')
def step_problem_evidence_status(context):
    """Verify the Problem has a valid evidence status."""
    evidence_status = context.sample_problem.get("evidence_maturity")
    valid_statuses = ['01_assumptive', '02_anecdotal', '03_early_signal', '04_balanced_signal', '05_triangulated']
    
    assert evidence_status in valid_statuses, \
        f"Invalid evidence status: {evidence_status}. Must be one of {valid_statuses}"


@then('the Problem prompt should follow JTBD format guidelines')
def step_problem_prompt_jtbd_format(context):
    """Verify Problem prompt includes JTBD format guidelines."""
    prompts_dir = Path("scripts/prompts_from_markdown")
    if not prompts_dir.exists():
        prompts_dir = Path("src/scripts/prompts_from_markdown")
    
    problem_prompt = prompts_dir / "problem_prompt.md"
    content = problem_prompt.read_text()
    
    # Check for JTBD-specific content
    jtbd_indicators = [
        "JTBD",
        "job statement",
        "When [situation]",
        "I want to [motivation]",
        "so I can [expected outcome]"
    ]
    
    jtbd_found = any(indicator in content for indicator in jtbd_indicators)
    assert jtbd_found, "Problem prompt missing JTBD format guidelines"


@then('the Problem prompt should include ODI methodology references')
def step_problem_prompt_odi_methodology(context):
    """Verify Problem prompt includes ODI methodology references."""
    prompts_dir = Path("scripts/prompts_from_markdown")
    if not prompts_dir.exists():
        prompts_dir = Path("src/scripts/prompts_from_markdown")
    
    problem_prompt = prompts_dir / "problem_prompt.md"
    content = problem_prompt.read_text()
    
    # Check for ODI-specific content
    odi_indicators = [
        "ODI",
        "Outcome-Driven Innovation",
        "opportunity_score",
        "importance",
        "satisfaction"
    ]
    
    odi_found = any(indicator in content for indicator in odi_indicators)
    assert odi_found, "Problem prompt missing ODI methodology references"


@then('the Problem prompt should include risk management attributes')
def step_problem_prompt_risk_management(context):
    """Verify Problem prompt includes risk management attributes."""
    prompts_dir = Path("scripts/prompts_from_markdown")
    if not prompts_dir.exists():
        prompts_dir = Path("src/scripts/prompts_from_markdown")
    
    problem_prompt = prompts_dir / "problem_prompt.md"
    content = problem_prompt.read_text()
    
    # Check for risk-specific content
    risk_indicators = [
        "risk",
        "evidence_missing",
        "impact_undefined", 
        "user_ambiguous",
        "jtbd_malformed",
        "outdated_evidence"
    ]
    
    risk_found = any(indicator in content for indicator in risk_indicators)
    assert risk_found, "Problem prompt missing risk management attributes"


@when('I load a test Problem object from file')
def step_load_test_problem_from_file(context):
    """Load a real test Problem object from the test data."""
    # Try to load the linked object we created
    linked_object_path = Path("test_data/samples/linked_objects/joel_bella_gpu_management.json")
    
    if linked_object_path.exists():
        with open(linked_object_path, 'r') as f:
            linked_data = json.load(f)
        context.sample_problem = linked_data["object1"]  # Extract the Problem object
        context.linked_result = linked_data["object2"]   # Also store the linked Result
        context.relationship_analysis = linked_data["relationship_analysis"]
    else:
        # Fallback to sample objects
        sample_path = Path("test_data/generated/dux_v9.4_sample_objects/problem_sample.json")
        with open(sample_path, 'r') as f:
            context.sample_problem = json.load(f)


@then('it should have valid cross-object references')
def step_should_have_valid_cross_references(context):
    """Verify that cross-object references have proper evidence status."""
    problem = context.sample_problem
    
    # Check result_ids references
    result_ids = problem.get("result_ids", [])
    
    for result_ref in result_ids:
        if isinstance(result_ref, dict):
            # Check required fields for object references
            assert "id" in result_ref, "Result reference missing 'id' field"
            assert "evidence_status" in result_ref, "Result reference missing 'evidence_status' field"
            
            # Validate evidence status
            valid_statuses = ["evidence_backed", "evidence_present", "assumptive"]
            assert result_ref["evidence_status"] in valid_statuses, \
                f"Invalid evidence status in result reference: {result_ref['evidence_status']}"


@then('it should demonstrate persona collaboration')
def step_should_demonstrate_persona_collaboration(context):
    """Verify the object shows cross-persona collaboration evidence."""
    problem = context.sample_problem
    
    # Check if this appears to be a Joel (admin) problem
    joel_indicators = ["cluster", "admin", "gpu", "resource", "monitor", "manage"]
    description = problem.get("description", "").lower()
    end_users = str(problem.get("end_user", [])).lower()
    
    joel_related = any(indicator in description or indicator in end_users 
                      for indicator in joel_indicators)
    
    if joel_related:
        # If it's Joel's problem, it should reference Bella's outcomes
        result_ids = problem.get("result_ids", [])
        assert len(result_ids) > 0, "Joel's admin problem should reference user outcomes"
        
        # Check if linked to user-facing results
        bella_indicators = ["data scientist", "workspace", "training", "user"]
        for result_ref in result_ids:
            if isinstance(result_ref, dict):
                ref_description = result_ref.get("description", "").lower()
                bella_related = any(indicator in ref_description for indicator in bella_indicators)
                if bella_related:
                    print(f"✅ Found cross-persona link: Admin problem -> User outcome")
                    break


@then('the linked objects should have consistent evidence status')
def step_linked_objects_consistent_evidence_status(context):
    """Verify that linked objects maintain evidence status consistency."""
    if not hasattr(context, 'linked_result'):
        # Skip if we don't have linked objects
        return
        
    problem = context.sample_problem
    result = context.linked_result
    
    # Check that references maintain proper evidence status
    result_ids = problem.get("result_ids", [])
    
    for result_ref in result_ids:
        if isinstance(result_ref, dict) and result_ref.get("id") == result.get("id"):
            # Found the reference to our linked result
            ref_evidence_status = result_ref.get("evidence_status")
            actual_evidence_status = result.get("evidence_status")
            
            print(f"Reference evidence status: {ref_evidence_status}")
            print(f"Actual object evidence status: {actual_evidence_status}")
            
            # They should match
            assert ref_evidence_status == actual_evidence_status, \
                f"Evidence status mismatch: reference has '{ref_evidence_status}' but actual object has '{actual_evidence_status}'"
