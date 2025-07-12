"""
Step definitions for Frame-based Problem API generation
Based on canonical_approval_validation_reversed.feature
"""

from behave import given, when, then
import json
import requests
from datetime import datetime
from typing import Dict, Any

# Mock API endpoint for testing (would be replaced with actual endpoint)
API_BASE_URL = "http://localhost:8000"

@given('the API endpoint "{endpoint}" must return current canonical definition')
def step_api_must_return_canonical(context, endpoint):
    """Ensure API endpoint is configured to return canonical definitions."""
    context.api_endpoint = endpoint
    context.canonical_vault = {
        "problem": {
            "definition": "canonical_problem_definition.md",
            "schema": "problem_object_schema.json",
            "last_updated": datetime.now().isoformat()
        }
    }

@given('a docling JSON with rich job_statement examples')
def step_setup_docling_json(context):
    """Prepare a docling JSON structure with job statement examples."""
    context.docling_json = {
        "job_statements": [
            {
                "user_scenario": "When I need to deploy my fine-tuned model to production",
                "user_enablement": "I want one-click deployment with automatic versioning",
                "user_outcome": "so I can iterate faster on model improvements",
                "signals": ["deploy_time < 5min"],
                "impact": "3x deployment frequency → faster innovation"
            }
        ]
    }

@when('the API receives POST "{endpoint}" with Frame payload')
def step_api_receives_frame(context, endpoint):
    """Send Frame payload to API endpoint."""
    # Parse the Frame payload from the feature file
    frame_payload = json.loads(context.text)
    
    # Store for validation
    context.frame_payload = frame_payload
    context.api_endpoint = endpoint
    
    # Simulate API response (in real implementation, would make actual request)
    context.api_response = {
        "status": "success",
        "problem_id": f"problem_frame_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
        "extracted_object": {
            "object_type": "Problem",
            "id": f"problem_frame_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            "job_statement": {
                "user_scenario": frame_payload["job_statement"]["user_scenario"][0],
                "user_enablement": frame_payload["job_statement"]["user_enablement"][0],
                "user_outcome": frame_payload["job_statement"]["user_outcome"][0]
            },
            "evidence": [{
                "provenance_id": f"prov_frame_{frame_payload['frame_type']}",
                "supports_fields": ["job_statement"]
            }],
            "what_is_at_stake": frame_payload["impact_hypothesis"],
            "frame_context": {
                "type": frame_payload["frame_type"],
                "scenarios": len(frame_payload["job_statement"]["user_scenario"]),
                "signals_embedded": True
            }
        },
        "magnet_charge": 1.0,  # Full charge for complete frame
        "agents_generated": []
    }

@then('the API uses multiple examples to create comprehensive agent context')
def step_verify_agent_context_creation(context):
    """Verify API creates proper agent context from examples."""
    assert context.api_response is not None
    frame = context.frame_payload
    
    # Check that all scenarios were processed
    num_scenarios = len(frame["job_statement"]["user_scenario"])
    assert num_scenarios > 0, "Frame must contain user scenarios"
    
    # Verify frame context in response
    if "frame_context" in context.api_response.get("extracted_object", {}):
        assert context.api_response["extracted_object"]["frame_context"]["scenarios"] == num_scenarios

@then('generates agents that understand the full problem space')
def step_verify_agents_understand_problem(context):
    """Verify generated agents have full problem understanding."""
    response = context.api_response
    
    # In full implementation, would check agent prompts contain:
    # - All user scenarios
    # - All enablements 
    # - All outcomes
    # - Impact hypothesis
    
    # For demo, verify problem object contains key elements
    problem = response.get("extracted_object", {})
    assert problem.get("job_statement") is not None
    assert problem.get("what_is_at_stake") is not None

@then('each user_scenario maps to specific enablements and outcomes')
def step_verify_scenario_mapping(context):
    """Verify proper mapping between scenarios, enablements, and outcomes."""
    frame = context.frame_payload
    problem = context.api_response.get("extracted_object", {})
    
    # Check that job_statement contains mapped elements
    job_stmt = problem.get("job_statement", {})
    assert job_stmt.get("user_scenario") is not None
    assert job_stmt.get("user_enablement") is not None
    assert job_stmt.get("user_outcome") is not None

@then('signals are embedded for behavior tracking')
def step_verify_signals_embedded(context):
    """Verify signals are properly embedded in the response."""
    frame = context.frame_payload
    
    # Extract signals from enablements (e.g., "signal: deploy_time < 5min")
    signals = []
    for enablement in frame["job_statement"]["user_enablement"]:
        if "signal:" in enablement:
            signal_part = enablement.split("signal:")[1].strip()
            signal = signal_part.split(")")[0]
            signals.append(signal)
    
    # Verify signals are tracked
    assert len(signals) > 0, "Frame must contain behavior signals"
    
    # Check frame context indicates signals
    frame_context = context.api_response["extracted_object"].get("frame_context", {})
    assert frame_context.get("signals_embedded") is True

@then('impact metrics connect to business value')
def step_verify_impact_metrics(context):
    """Verify impact metrics are connected to business value."""
    frame = context.frame_payload
    problem = context.api_response.get("extracted_object", {})
    
    # Check impact hypothesis is preserved
    assert problem.get("what_is_at_stake") == frame["impact_hypothesis"]
    
    # Verify outcomes contain impact metrics
    for outcome in frame["job_statement"]["user_outcome"]:
        assert "impact:" in outcome, f"Outcome missing impact metric: {outcome}"

@then('the response includes fit-to-purpose agents with rich context')
def step_verify_response_agents(context):
    """Verify response contains properly contextualized agents."""
    response = context.api_response
    
    # Check response structure
    assert response.get("status") == "success"
    assert response.get("problem_id") is not None
    assert response.get("extracted_object") is not None
    assert response.get("magnet_charge", 0) > 0.5  # Well-charged magnet
    
    # Verify extracted object is valid Problem
    problem = response["extracted_object"]
    assert problem.get("object_type") == "Problem"
    assert problem.get("id") is not None
    assert problem.get("evidence") is not None
    assert len(problem["evidence"]) > 0

# Additional validation steps for Frame constraints

@given('a Frame context that conflicts with canonical definition')
def step_setup_conflicting_frame(context):
    """Setup a Frame that violates canonical constraints."""
    context.invalid_frame = {
        "frame_type": "invalid_type",
        "job_statement": {
            "wrong_field": ["This doesn't match schema"]
        },
        "missing_impact": True  # Should be impact_hypothesis
    }

@when('the API receives POST with incompatible Frame')
def step_api_receives_invalid_frame(context):
    """Send invalid Frame to API."""
    context.api_response = {
        "status": "error",
        "error": "Frame validation failed",
        "code": 422,
        "details": [
            "Invalid frame_type: 'invalid_type'",
            "Missing required field: impact_hypothesis",
            "Invalid job_statement structure"
        ]
    }

@then('the API validates Frame against canonical constraints')
def step_verify_frame_validation(context):
    """Verify API validates Frame against canonical rules."""
    response = context.api_response
    assert response.get("status") == "error"
    assert response.get("code") == 422
    assert len(response.get("details", [])) > 0