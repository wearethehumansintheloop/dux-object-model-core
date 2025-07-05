"""
Step definitions for Insight Object Pattern Validation
Validates the step-by-step data inheritance flow through the DUX object model
"""

import json
import os
import re
from pathlib import Path
from behave import given, when, then


@given('I have a Problem object with defined scope and evidence')
def step_have_problem_with_scope_and_evidence(context):
    """Set up a Problem object with proper scope and evidence."""
    context.problem = {
        "object_type": "Problem",
        "id": "problem_cost_optimization",
        "title": "Platform teams struggle with cost optimization",
        "description": "Platform teams lack systematic approaches to identify and reduce compute costs while maintaining performance.",
        "scope": "Platform administration and cost management workflows",
        "evidence_status": "validated",
        "evidence": [
            "provenance_problem_cost_optimization",
            {
                "quote": "Platform teams spend 30% of their time on cost optimization but only achieve 5% savings",
                "attribution": "Senior Platform Engineer",
                "participant_id": "P001",
                "source_file": "research/interviews/platform_engineers_2025_01_10.md"
            }
        ],
        "result_ids": ["result_reduce_compute_costs"]
    }


@given('I have a Result object with target impact and success criteria')
def step_have_result_with_impact_and_criteria(context):
    """Set up a Result object with target impact and success criteria."""
    context.result = {
        "object_type": "Result",
        "id": "result_reduce_compute_costs",
        "target_impact": "Reduce compute costs by 20% while maintaining performance",
        "success_criteria": "Platform teams achieve 20% cost reduction through automated optimization",
        "success_metrics": ["cost_reduction_percentage", "performance_maintenance_score"],
        "evidence": [
            "provenance_result_reduce_compute_costs",
            {
                "quote": "Automated cost optimization can reduce compute costs by 20-30% while maintaining performance",
                "attribution": "Cloud Cost Analysis Report",
                "source_file": "research/benchmarks/cloud_cost_analysis_2024_12.md"
            }
        ],
        "useroutcome_ids": []
    }


@given('I have Behavior objects with signals and acceptance criteria')
def step_have_behaviors_with_signals_and_criteria(context):
    """Set up Behavior objects with signals and acceptance criteria."""
    context.behaviors = [
        {
            "object_type": "Behavior",
            "id": "behavior_analyze_usage",
            "user_enablement": "Platform admin is able to analyze resource usage patterns",
            "end_user": "Platform Administrator",
            "signals": ["usage_analysis_started", "usage_analysis_completed", "usage_report_generated"],
            "acceptance_criteria": ["Usage analysis completed within 24 hours", "Usage report includes cost breakdown"],
            "evidence": [
                "provenance_behavior_analyze_usage",
                {
                    "quote": "Usage analysis tools help identify 40% of cost optimization opportunities",
                    "attribution": "Platform Admin Survey",
                    "source_file": "research/surveys/platform_admin_survey_2025_01.md"
                }
            ]
        },
        {
            "object_type": "Behavior",
            "id": "behavior_identify_waste",
            "user_enablement": "Platform admin is able to identify resource waste",
            "end_user": "Platform Administrator", 
            "signals": ["waste_detection_run", "waste_identified", "waste_report_created"],
            "acceptance_criteria": ["Waste detection identifies 15%+ savings opportunities", "Waste report includes actionable recommendations"],
            "evidence": [
                "provenance_behavior_identify_waste",
                {
                    "quote": "Waste detection algorithms can identify 15-25% of unused resources",
                    "attribution": "Infrastructure Analysis",
                    "source_file": "research/analysis/infrastructure_waste_analysis_2025_01.md"
                }
            ]
        }
    ]


@given('I have Provenance objects tracking object creation')
def step_have_provenance_objects(context):
    """Set up Provenance objects tracking object creation."""
    context.provenance_objects = {
        "problem_cost_optimization": {
            "object_type": "Provenance",
            "id": "provenance_problem_cost_optimization",
            "object_id": "problem_cost_optimization",
            "object_type_referenced": "Problem",
            "creation_timestamp": "2025-01-15T10:30:00Z",
            "data_source": "User research interviews",
            "method": "Qualitative analysis",
            "researcher": "UX Research Team",
            "evidence_maturity": "validated"
        },
        "result_reduce_compute_costs": {
            "object_type": "Provenance",
            "id": "provenance_result_reduce_compute_costs",
            "object_id": "result_reduce_compute_costs",
            "object_type_referenced": "Result",
            "creation_timestamp": "2025-01-15T11:00:00Z",
            "data_source": "Business analysis",
            "method": "Quantitative analysis",
            "researcher": "Product Strategy Team",
            "evidence_maturity": "validated"
        },
        "behavior_analyze_usage": {
            "object_type": "Provenance",
            "id": "provenance_behavior_analyze_usage",
            "object_id": "behavior_analyze_usage",
            "object_type_referenced": "Behavior",
            "creation_timestamp": "2025-01-15T11:15:00Z",
            "data_source": "Task analysis",
            "method": "Behavioral observation",
            "researcher": "UX Research Team",
            "evidence_maturity": "validated"
        },
        "behavior_identify_waste": {
            "object_type": "Provenance",
            "id": "provenance_behavior_identify_waste",
            "object_id": "behavior_identify_waste",
            "object_type_referenced": "Behavior",
            "creation_timestamp": "2025-01-15T11:20:00Z",
            "data_source": "Task analysis",
            "method": "Behavioral observation",
            "researcher": "UX Research Team",
            "evidence_maturity": "validated"
        }
    }


@given('I have a Problem object with id "{problem_id}"')
def step_have_problem_with_id(context, problem_id):
    """Set up a specific Problem object."""
    context.current_problem = context.problem
    assert context.current_problem['id'] == problem_id


@given('I have a Result object with id "{result_id}"')
def step_have_result_with_id(context, result_id):
    """Set up a specific Result object."""
    context.current_result = context.result
    assert context.current_result['id'] == result_id


@given('I have Behavior objects with ids {behavior_ids}')
def step_have_behaviors_with_ids(context, behavior_ids):
    """Set up specific Behavior objects."""
    # Parse the list of behavior IDs
    ids = eval(behavior_ids)  # Safe for our test data
    context.current_behaviors = [b for b in context.behaviors if b['id'] in ids]
    assert len(context.current_behaviors) == len(ids)


@when('I validate the core object generation')
def step_validate_core_object_generation(context):
    """Validate that core objects are properly generated."""
    context.validation_results = {
        'problem_valid': False,
        'result_valid': False,
        'behaviors_valid': False
    }


@then('the Problem should have a clear scope and evidence status')
def step_verify_problem_scope_and_evidence(context):
    """Verify Problem has proper scope and evidence."""
    problem = context.current_problem
    assert 'scope' in problem, "Problem should have a scope"
    assert len(problem['scope']) > 10, "Problem scope should be descriptive"
    assert 'evidence_status' in problem, "Problem should have evidence_status"
    assert problem['evidence_status'] in ['draft', 'validated', 'proven'], "Invalid evidence_status"


@then('the Result should have target impact and success criteria')
def step_verify_result_impact_and_criteria(context):
    """Verify Result has target impact and success criteria."""
    result = context.current_result
    assert 'target_impact' in result, "Result should have target_impact"
    assert len(result['target_impact']) > 20, "Target impact should be descriptive"
    assert 'success_criteria' in result, "Result should have success_criteria"
    assert len(result['success_criteria']) > 20, "Success criteria should be descriptive"


@then('the Behaviors should have signals and acceptance criteria')
def step_verify_behaviors_signals_and_criteria(context):
    """Verify Behaviors have signals and acceptance criteria."""
    for behavior in context.current_behaviors:
        assert 'signals' in behavior, f"Behavior {behavior['id']} should have signals"
        assert len(behavior['signals']) > 0, f"Behavior {behavior['id']} should have signals"
        assert 'acceptance_criteria' in behavior, f"Behavior {behavior['id']} should have acceptance_criteria"
        assert len(behavior['acceptance_criteria']) > 0, f"Behavior {behavior['id']} should have acceptance_criteria"


@then('all objects should have proper IDs and metadata')
def step_verify_objects_have_ids_and_metadata(context):
    """Verify all objects have proper IDs and metadata."""
    # Check Problem
    assert 'id' in context.current_problem, "Problem should have an ID"
    assert 'object_type' in context.current_problem, "Problem should have object_type"
    
    # Check Result
    assert 'id' in context.current_result, "Result should have an ID"
    assert 'object_type' in context.current_result, "Result should have object_type"
    
    # Check Behaviors
    for behavior in context.current_behaviors:
        assert 'id' in behavior, f"Behavior should have an ID"
        assert 'object_type' in behavior, f"Behavior should have object_type"


@then('Provenance objects should be created for each object')
def step_verify_provenance_objects_created(context):
    """Verify Provenance objects are created for each object."""
    # Check that provenance objects exist for each core object
    assert context.problem['id'] in context.provenance_objects, "Provenance should exist for Problem"
    assert context.result['id'] in context.provenance_objects, "Provenance should exist for Result"
    
    for behavior in context.behaviors:
        assert behavior['id'] in context.provenance_objects, f"Provenance should exist for Behavior {behavior['id']}"


@then('each object should reference its Provenance ID in the evidence array')
def step_verify_objects_reference_provenance_in_evidence(context):
    """Verify each object references its Provenance ID in the evidence array."""
    # Check Problem
    problem_evidence = context.problem['evidence']
    problem_provenance_id = f"provenance_{context.problem['id']}"
    assert problem_provenance_id in problem_evidence, f"Problem should reference {problem_provenance_id} in evidence"
    
    # Check Result
    result_evidence = context.result['evidence']
    result_provenance_id = f"provenance_{context.result['id']}"
    assert result_provenance_id in result_evidence, f"Result should reference {result_provenance_id} in evidence"
    
    # Check Behaviors
    for behavior in context.behaviors:
        behavior_evidence = behavior['evidence']
        behavior_provenance_id = f"provenance_{behavior['id']}"
        assert behavior_provenance_id in behavior_evidence, f"Behavior {behavior['id']} should reference {behavior_provenance_id} in evidence"


@then('each object should have a teaser quote in the evidence array')
def step_verify_objects_have_teaser_quotes(context):
    """Verify each object has a teaser quote in the evidence array."""
    # Check Problem
    problem_evidence = context.problem['evidence']
    has_teaser_quote = any(isinstance(evidence, dict) and 'quote' in evidence for evidence in problem_evidence)
    assert has_teaser_quote, "Problem should have a teaser quote in evidence"
    
    # Check Result
    result_evidence = context.result['evidence']
    has_teaser_quote = any(isinstance(evidence, dict) and 'quote' in evidence for evidence in result_evidence)
    assert has_teaser_quote, "Result should have a teaser quote in evidence"
    
    # Check Behaviors
    for behavior in context.behaviors:
        behavior_evidence = behavior['evidence']
        has_teaser_quote = any(isinstance(evidence, dict) and 'quote' in evidence for evidence in behavior_evidence)
        assert has_teaser_quote, f"Behavior {behavior['id']} should have a teaser quote in evidence"


@then('each teaser quote should have proper attribution and source file')
def step_verify_teaser_quotes_have_attribution_and_source(context):
    """Verify each teaser quote has proper attribution and source file."""
    # Check Problem
    problem_evidence = context.problem['evidence']
    for evidence in problem_evidence:
        if isinstance(evidence, dict) and 'quote' in evidence:
            assert 'attribution' in evidence, "Teaser quote should have attribution"
            assert 'source_file' in evidence, "Teaser quote should have source_file"
            assert evidence['source_file'].endswith('.md'), "Source file should be markdown"
    
    # Check Result
    result_evidence = context.result['evidence']
    for evidence in result_evidence:
        if isinstance(evidence, dict) and 'quote' in evidence:
            assert 'attribution' in evidence, "Teaser quote should have attribution"
            assert 'source_file' in evidence, "Teaser quote should have source_file"
            assert evidence['source_file'].endswith('.md'), "Source file should be markdown"
    
    # Check Behaviors
    for behavior in context.behaviors:
        behavior_evidence = behavior['evidence']
        for evidence in behavior_evidence:
            if isinstance(evidence, dict) and 'quote' in evidence:
                assert 'attribution' in evidence, "Teaser quote should have attribution"
                assert 'source_file' in evidence, "Teaser quote should have source_file"
                assert evidence['source_file'].endswith('.md'), "Source file should be markdown"


@when('the Result links to the Behaviors')
def step_result_links_to_behaviors(context):
    """Simulate Result linking to Behaviors and creating UserOutcome."""
    # Create UserOutcome with inherited data
    context.useroutcome = {
        "object_type": "UserOutcome",
        "id": "outcome_cost_optimization",
        "result_id": context.current_result['id'],
        "behavior_id": context.current_behaviors[0]['id'],  # Primary behavior
        "end_user": context.current_behaviors[0]['end_user'],
        "outcome_statement": f"Platform teams achieve {context.current_result['target_impact']}",
        "key_signals": [],
        "acceptance_criteria": [],
        "evidence": []
    }
    
    # Inherit signals from behaviors
    for behavior in context.current_behaviors:
        context.useroutcome['key_signals'].extend(behavior['signals'])
        context.useroutcome['acceptance_criteria'].extend(behavior['acceptance_criteria'])
        context.useroutcome['evidence'].extend(behavior['evidence'])


@then('a UserOutcome should be created with id "{outcome_id}"')
def step_verify_useroutcome_created(context, outcome_id):
    """Verify UserOutcome is created with correct ID."""
    assert context.useroutcome['id'] == outcome_id, f"UserOutcome should have ID {outcome_id}"


@then('the UserOutcome should inherit signals from the linked Behaviors')
def step_verify_useroutcome_inherits_signals(context):
    """Verify UserOutcome inherits signals from behaviors."""
    expected_signals = []
    for behavior in context.current_behaviors:
        expected_signals.extend(behavior['signals'])
    
    for signal in expected_signals:
        assert signal in context.useroutcome['key_signals'], f"UserOutcome should inherit signal: {signal}"


@then('the UserOutcome should inherit acceptance criteria from the Behaviors')
def step_verify_useroutcome_inherits_criteria(context):
    """Verify UserOutcome inherits acceptance criteria from behaviors."""
    expected_criteria = []
    for behavior in context.current_behaviors:
        expected_criteria.extend(behavior['acceptance_criteria'])
    
    for criterion in expected_criteria:
        assert criterion in context.useroutcome['acceptance_criteria'], f"UserOutcome should inherit criterion: {criterion}"


@then('the UserOutcome should reference the Result via result_id')
def step_verify_useroutcome_references_result(context):
    """Verify UserOutcome references the Result."""
    assert context.useroutcome['result_id'] == context.current_result['id'], "UserOutcome should reference Result"


@then('the UserOutcome should have an outcome statement derived from the Result target impact')
def step_verify_outcome_statement_derived_from_result(context):
    """Verify outcome statement is derived from Result target impact."""
    outcome_statement = context.useroutcome['outcome_statement']
    target_impact = context.current_result['target_impact']
    
    # Check that key concepts from target impact appear in outcome statement
    key_terms = ['cost', 'optimization', 'performance', 'reduce']
    for term in key_terms:
        if term in target_impact.lower():
            assert term in outcome_statement.lower(), f"Outcome statement should include '{term}' from target impact"


@given('I have UserOutcome objects related to the Problem')
def step_have_useroutcomes_related_to_problem(context):
    """Set up UserOutcome objects related to the Problem."""
    context.related_useroutcomes = [context.useroutcome]


@when('the Problem identifies related UserOutcomes')
def step_problem_identifies_useroutcomes(context):
    """Simulate Problem identifying related UserOutcomes and creating UserFlow."""
    context.userflow = {
        "object_type": "UserFlow",
        "user_flow_id": "flow_cost_optimization_workflow",
        "title": "Cost Optimization Workflow",
        "description": "Systematic approach to identify and reduce compute costs",
        "problem_id": context.current_problem['id'],
        "user_outcome_id": context.related_useroutcomes[0]['id'],
        "behavior_sequence": [],
        "evidence": ["User journey mapping", "Task analysis with platform admins"]
    }


@then('a UserFlow should be created with id "{flow_id}"')
def step_verify_userflow_created(context, flow_id):
    """Verify UserFlow is created with correct ID."""
    assert context.userflow['user_flow_id'] == flow_id, f"UserFlow should have ID {flow_id}"


@then('the UserFlow should reference the Problem via problem_id')
def step_verify_userflow_references_problem(context):
    """Verify UserFlow references the Problem."""
    assert context.userflow['problem_id'] == context.current_problem['id'], "UserFlow should reference Problem"


@then('the UserFlow should reference the UserOutcome via user_outcome_id')
def step_verify_userflow_references_useroutcome(context):
    """Verify UserFlow references the UserOutcome."""
    assert context.userflow['user_outcome_id'] == context.related_useroutcomes[0]['id'], "UserFlow should reference UserOutcome"


@then('the UserFlow should have a title and description')
def step_verify_userflow_has_title_and_description(context):
    """Verify UserFlow has title and description."""
    assert 'title' in context.userflow, "UserFlow should have a title"
    assert len(context.userflow['title']) > 5, "UserFlow title should be descriptive"
    assert 'description' in context.userflow, "UserFlow should have a description"
    assert len(context.userflow['description']) > 20, "UserFlow description should be descriptive"


@then('the UserFlow should have evidence supporting the relationship')
def step_verify_userflow_has_evidence(context):
    """Verify UserFlow has evidence supporting the relationship."""
    assert 'evidence' in context.userflow, "UserFlow should have evidence"
    assert len(context.userflow['evidence']) > 0, "UserFlow should have evidence"


@given('I have Behavior objects that contribute to the flow\'s outcome')
def step_have_behaviors_contributing_to_flow(context):
    """Set up behaviors that contribute to the flow's outcome."""
    context.flow_behaviors = context.current_behaviors


@when('the UserFlow generates a behavior sequence')
def step_userflow_generates_behavior_sequence(context):
    """Simulate UserFlow generating a behavior sequence."""
    # Generate logical sequence based on behavior dependencies
    context.userflow['behavior_sequence'] = [b['id'] for b in context.flow_behaviors]


@then('the UserFlow should have a behavior_sequence array')
def step_verify_userflow_has_behavior_sequence(context):
    """Verify UserFlow has behavior_sequence array."""
    assert 'behavior_sequence' in context.userflow, "UserFlow should have behavior_sequence"
    assert isinstance(context.userflow['behavior_sequence'], list), "behavior_sequence should be an array"


@then('the behavior_sequence should contain Behavior IDs in logical order')
def step_verify_behavior_sequence_logical_order(context):
    """Verify behavior_sequence contains Behavior IDs in logical order."""
    sequence = context.userflow['behavior_sequence']
    assert len(sequence) > 0, "behavior_sequence should not be empty"
    
    # Check that all behaviors in sequence exist
    for behavior_id in sequence:
        assert any(b['id'] == behavior_id for b in context.flow_behaviors), f"Behavior {behavior_id} should exist"


@then('each Behavior in the sequence should have defined signals')
def step_verify_behaviors_in_sequence_have_signals(context):
    """Verify each Behavior in sequence has defined signals."""
    for behavior_id in context.userflow['behavior_sequence']:
        behavior = next(b for b in context.flow_behaviors if b['id'] == behavior_id)
        assert 'signals' in behavior, f"Behavior {behavior_id} should have signals"
        assert len(behavior['signals']) > 0, f"Behavior {behavior_id} should have signals"


@then('the sequence should represent a complete user journey')
def step_verify_sequence_complete_user_journey(context):
    """Verify sequence represents a complete user journey."""
    sequence = context.userflow['behavior_sequence']
    assert len(sequence) >= 2, "User journey should have at least 2 behaviors"
    
    # Check for logical flow (analysis → identification → action)
    behavior_names = [b['id'] for b in context.flow_behaviors]
    assert 'analyze' in behavior_names[0] or 'identify' in behavior_names[0], "Sequence should start with analysis/identification"


@then('the sequence should be evidence-backed')
def step_verify_sequence_evidence_backed(context):
    """Verify sequence is evidence-backed."""
    assert 'evidence' in context.userflow, "UserFlow should have evidence"
    assert len(context.userflow['evidence']) > 0, "UserFlow should have evidence"


@given('I have a UserOutcome related to the UserFlow')
def step_have_useroutcome_related_to_userflow(context):
    """Set up UserOutcome related to the UserFlow."""
    context.flow_useroutcome = context.useroutcome


@when('the UserOutcome inherits data from the flow\'s behaviors')
def step_useroutcome_inherits_from_flow_behaviors(context):
    """Simulate UserOutcome inheriting data from flow behaviors."""
    # Update UserOutcome with data from flow behaviors
    context.flow_useroutcome['user_flow_id'] = context.userflow['user_flow_id']
    
    # Inherit signals from flow behaviors
    flow_signals = []
    for behavior_id in context.userflow['behavior_sequence']:
        behavior = next(b for b in context.flow_behaviors if b['id'] == behavior_id)
        flow_signals.extend(behavior['signals'])
    
    context.flow_useroutcome['key_signals'] = list(set(context.flow_useroutcome['key_signals'] + flow_signals))


@then('the UserOutcome should have key_signals from the behavior sequence')
def step_verify_useroutcome_has_signals_from_sequence(context):
    """Verify UserOutcome has key_signals from behavior sequence."""
    flow_signals = []
    for behavior_id in context.userflow['behavior_sequence']:
        behavior = next(b for b in context.flow_behaviors if b['id'] == behavior_id)
        flow_signals.extend(behavior['signals'])
    
    for signal in flow_signals:
        assert signal in context.flow_useroutcome['key_signals'], f"UserOutcome should have signal from sequence: {signal}"


@then('the UserOutcome should have acceptance_criteria derived from behavior criteria')
def step_verify_useroutcome_criteria_from_behaviors(context):
    """Verify UserOutcome has acceptance_criteria from behaviors."""
    flow_criteria = []
    for behavior_id in context.userflow['behavior_sequence']:
        behavior = next(b for b in context.flow_behaviors if b['id'] == behavior_id)
        flow_criteria.extend(behavior['acceptance_criteria'])
    
    for criterion in flow_criteria:
        assert criterion in context.flow_useroutcome['acceptance_criteria'], f"UserOutcome should have criterion from behaviors: {criterion}"


@then('the UserOutcome should reference the UserFlow via user_flow_id')
def step_verify_useroutcome_references_userflow(context):
    """Verify UserOutcome references the UserFlow."""
    assert context.flow_useroutcome['user_flow_id'] == context.userflow['user_flow_id'], "UserOutcome should reference UserFlow"


@then('the inherited signals should be traceable to specific behaviors')
def step_verify_signals_traceable_to_behaviors(context):
    """Verify inherited signals are traceable to specific behaviors."""
    for signal in context.flow_useroutcome['key_signals']:
        # Check that signal comes from at least one behavior in the sequence
        signal_found = False
        for behavior_id in context.userflow['behavior_sequence']:
            behavior = next(b for b in context.flow_behaviors if b['id'] == behavior_id)
            if signal in behavior['signals']:
                signal_found = True
                break
        assert signal_found, f"Signal {signal} should be traceable to a behavior in the sequence"


@then('the acceptance criteria should be measurable and specific')
def step_verify_acceptance_criteria_measurable(context):
    """Verify acceptance criteria are measurable and specific."""
    for criterion in context.flow_useroutcome['acceptance_criteria']:
        # Check for measurable elements
        measurable_patterns = [r'\d+%', r'\d+\.\d+', r'\d+', r'increase', r'decrease', r'improve', r'reduce']
        has_measurement = any(re.search(pattern, criterion, re.IGNORECASE) for pattern in measurable_patterns)
        assert has_measurement, f"Acceptance criterion should be measurable: '{criterion}'"


@given('I have a Result object that created the UserOutcome')
def step_have_result_that_created_useroutcome(context):
    """Set up Result object that created the UserOutcome."""
    context.original_result = context.result


@when('the Result inherits success metrics from the UserOutcome')
def step_result_inherits_from_useroutcome(context):
    """Simulate Result inheriting success metrics from UserOutcome."""
    # Update Result with data from UserOutcome
    context.original_result['useroutcome_ids'] = [context.flow_useroutcome['id']]
    context.original_result['success_metrics'] = context.flow_useroutcome['key_signals']
    context.original_result['success_criteria'] = context.flow_useroutcome['acceptance_criteria'][0]  # Primary criterion


@then('the Result should have success_metrics derived from UserOutcome key_signals')
def step_verify_result_has_metrics_from_useroutcome(context):
    """Verify Result has success_metrics from UserOutcome key_signals."""
    for signal in context.flow_useroutcome['key_signals']:
        assert signal in context.original_result['success_metrics'], f"Result should have metric from UserOutcome: {signal}"


@then('the Result should have success_criteria aligned with UserOutcome acceptance_criteria')
def step_verify_result_criteria_aligned_with_useroutcome(context):
    """Verify Result success_criteria aligned with UserOutcome acceptance_criteria."""
    result_criteria = context.original_result['success_criteria']
    useroutcome_criteria = context.flow_useroutcome['acceptance_criteria']
    
    # Check that key concepts from UserOutcome criteria appear in Result criteria
    key_terms = ['cost', 'optimization', 'performance', 'reduce', 'improve']
    for term in key_terms:
        if any(term in criterion.lower() for criterion in useroutcome_criteria):
            assert term in result_criteria.lower(), f"Result criteria should include '{term}' from UserOutcome criteria"


@then('the Result should reference UserOutcomes via useroutcome_ids')
def step_verify_result_references_useroutcomes(context):
    """Verify Result references UserOutcomes."""
    assert context.flow_useroutcome['id'] in context.original_result['useroutcome_ids'], "Result should reference UserOutcome"


@then('the success metrics should be quantifiable leading indicators')
def step_verify_success_metrics_leading_indicators(context):
    """Verify success metrics are quantifiable leading indicators."""
    for metric in context.original_result['success_metrics']:
        # Leading indicators should be observable before business impact
        leading_keywords = ['usage', 'analysis', 'detection', 'report', 'completion']
        assert any(keyword in metric.lower() for keyword in leading_keywords), f"Metric {metric} should be a leading indicator"


@then('the metrics should support the Result\'s target impact')
def step_verify_metrics_support_target_impact(context):
    """Verify metrics support the Result's target impact."""
    target_impact = context.original_result['target_impact']
    metrics = context.original_result['success_metrics']
    
    # Check that metrics relate to target impact
    impact_keywords = ['cost', 'optimization', 'performance', 'reduce']
    for keyword in impact_keywords:
        if keyword in target_impact.lower():
            metric_support = any(keyword in metric.lower() for metric in metrics)
            assert metric_support, f"Metrics should support '{keyword}' from target impact"


@given('I have a complete insight object chain')
def step_have_complete_insight_chain(context):
    """Set up complete insight object chain."""
    context.insight_chain = {
        'problem': context.problem,
        'result': context.original_result,
        'behaviors': context.behaviors,
        'useroutcome': context.flow_useroutcome,
        'userflow': context.userflow
    }


@when('I trace data inheritance through the entire chain')
def step_trace_data_inheritance(context):
    """Trace data inheritance through the entire chain."""
    context.inheritance_trace = {
        'signals_flow': [],
        'criteria_flow': [],
        'relationships': []
    }
    
    # Trace signals: Behavior → UserOutcome → Result
    for behavior in context.behaviors:
        for signal in behavior['signals']:
            if signal in context.flow_useroutcome['key_signals']:
                if signal in context.original_result['success_metrics']:
                    context.inheritance_trace['signals_flow'].append({
                        'signal': signal,
                        'behavior': behavior['id'],
                        'useroutcome': context.flow_useroutcome['id'],
                        'result': context.original_result['id']
                    })


@then('Problem → Result → Behavior → UserOutcome → UserFlow → UserOutcome → Result')
def step_verify_complete_chain_flow(context):
    """Verify complete chain flow."""
    chain = context.insight_chain
    
    # Verify relationships exist
    assert chain['problem']['result_ids'][0] == chain['result']['id'], "Problem should reference Result"
    assert chain['useroutcome']['result_id'] == chain['result']['id'], "UserOutcome should reference Result"
    assert chain['userflow']['problem_id'] == chain['problem']['id'], "UserFlow should reference Problem"
    assert chain['userflow']['user_outcome_id'] == chain['useroutcome']['id'], "UserFlow should reference UserOutcome"
    assert chain['useroutcome']['user_flow_id'] == chain['userflow']['user_flow_id'], "UserOutcome should reference UserFlow"


@then('signals should flow from Behaviors to UserOutcome key_signals')
def step_verify_signals_flow_behaviors_to_useroutcome(context):
    """Verify signals flow from Behaviors to UserOutcome key_signals."""
    behavior_signals = []
    for behavior in context.behaviors:
        behavior_signals.extend(behavior['signals'])
    
    useroutcome_signals = context.flow_useroutcome['key_signals']
    
    # At least some behavior signals should flow to UserOutcome
    flowing_signals = [s for s in behavior_signals if s in useroutcome_signals]
    assert len(flowing_signals) > 0, "Signals should flow from Behaviors to UserOutcome"


@then('UserOutcome key_signals should flow to Result success_metrics')
def step_verify_signals_flow_useroutcome_to_result(context):
    """Verify UserOutcome key_signals flow to Result success_metrics."""
    useroutcome_signals = context.flow_useroutcome['key_signals']
    result_metrics = context.original_result['success_metrics']
    
    # At least some UserOutcome signals should flow to Result
    flowing_signals = [s for s in useroutcome_signals if s in result_metrics]
    assert len(flowing_signals) > 0, "UserOutcome key_signals should flow to Result success_metrics"


@then('acceptance criteria should be consistent across the chain')
def step_verify_acceptance_criteria_consistent(context):
    """Verify acceptance criteria are consistent across the chain."""
    behavior_criteria = []
    for behavior in context.behaviors:
        behavior_criteria.extend(behavior['acceptance_criteria'])
    
    useroutcome_criteria = context.flow_useroutcome['acceptance_criteria']
    result_criteria = context.original_result['success_criteria']
    
    # Check for consistency in key concepts
    all_criteria = behavior_criteria + useroutcome_criteria + [result_criteria]
    key_concepts = ['cost', 'optimization', 'performance', 'reduce', 'improve']
    
    for concept in key_concepts:
        concept_mentions = sum(1 for criterion in all_criteria if concept in criterion.lower())
        if concept_mentions > 0:
            assert concept_mentions >= 2, f"Concept '{concept}' should appear consistently across criteria"


@then('all relationships should be properly referenced')
def step_verify_all_relationships_referenced(context):
    """Verify all relationships are properly referenced."""
    chain = context.insight_chain
    
    # Check all required references exist
    assert chain['problem']['result_ids'][0] == chain['result']['id'], "Problem → Result"
    assert chain['useroutcome']['result_id'] == chain['result']['id'], "UserOutcome → Result"
    assert chain['userflow']['problem_id'] == chain['problem']['id'], "UserFlow → Problem"
    assert chain['userflow']['user_outcome_id'] == chain['useroutcome']['id'], "UserFlow → UserOutcome"
    assert chain['useroutcome']['user_flow_id'] == chain['userflow']['user_flow_id'], "UserOutcome → UserFlow"
    assert chain['result']['useroutcome_ids'][0] == chain['useroutcome']['id'], "Result → UserOutcome"


@then('the chain should support business impact measurement')
def step_verify_chain_supports_business_impact(context):
    """Verify the chain supports business impact measurement."""
    # Check that we can trace from signals to business impact
    result_metrics = context.original_result['success_metrics']
    target_impact = context.original_result['target_impact']
    
    # Metrics should relate to target impact
    impact_keywords = ['cost', 'optimization', 'performance', 'reduce']
    metric_support = any(
        any(keyword in metric.lower() for keyword in impact_keywords)
        for metric in result_metrics
    )
    assert metric_support, "Chain should support business impact measurement"


@given('I have a complete insight object chain with signals')
def step_have_complete_chain_with_signals(context):
    """Set up complete insight object chain with signals."""
    # Already set up in previous steps
    pass


@when('I validate signal traceability')
def step_validate_signal_traceability(context):
    """Validate signal traceability through the chain."""
    context.signal_trace = []
    
    for behavior in context.behaviors:
        for signal in behavior['signals']:
            trace = {'signal': signal, 'source': behavior['id'], 'path': []}
            
            if signal in context.flow_useroutcome['key_signals']:
                trace['path'].append('UserOutcome')
                if signal in context.original_result['success_metrics']:
                    trace['path'].append('Result')
            
            if len(trace['path']) > 0:
                context.signal_trace.append(trace)


@then('I can trace signals from Behavior → UserOutcome → Result')
def step_verify_signal_trace_behavior_to_result(context):
    """Verify signals can be traced from Behavior → UserOutcome → Result."""
    complete_traces = [trace for trace in context.signal_trace if 'Result' in trace['path']]
    assert len(complete_traces) > 0, "Should be able to trace signals from Behavior → UserOutcome → Result"


@then('each signal should be observable and measurable')
def step_verify_signals_observable_measurable(context):
    """Verify each signal is observable and measurable."""
    for trace in context.signal_trace:
        signal = trace['signal']
        # Check signal naming convention (technical event names)
        assert '_' in signal or signal.islower(), f"Signal {signal} should follow technical naming"
        assert len(signal) > 5, f"Signal {signal} should be descriptive"


@then('signal changes should predict business impact')
def step_verify_signals_predict_business_impact(context):
    """Verify signal changes predict business impact."""
    # Leading indicators should predict the target impact
    target_impact = context.original_result['target_impact']
    signals = [trace['signal'] for trace in context.signal_trace]
    
    # Check that signals relate to impact measurement
    impact_keywords = ['cost', 'optimization', 'performance', 'reduce']
    predictive_signals = [
        signal for signal in signals
        if any(keyword in signal.lower() for keyword in impact_keywords)
    ]
    assert len(predictive_signals) > 0, "Signals should predict business impact"


@then('the signal chain should support leading indicator analysis')
def step_verify_signal_chain_supports_leading_indicators(context):
    """Verify signal chain supports leading indicator analysis."""
    # Leading indicators should be observable before business impact
    leading_keywords = ['usage', 'analysis', 'detection', 'report', 'completion']
    leading_signals = [
        trace['signal'] for trace in context.signal_trace
        if any(keyword in trace['signal'].lower() for keyword in leading_keywords)
    ]
    assert len(leading_signals) > 0, "Signal chain should support leading indicator analysis"


@then('signal aggregation should contribute to target metrics')
def step_verify_signal_aggregation_contributes_to_target(context):
    """Verify signal aggregation contributes to target metrics."""
    result_metrics = context.original_result['success_metrics']
    signals = [trace['signal'] for trace in context.signal_trace]
    
    # Check that aggregated signals contribute to result metrics
    contributing_signals = [s for s in signals if s in result_metrics]
    assert len(contributing_signals) > 0, "Signal aggregation should contribute to target metrics"


@given('I have insight objects with evidence')
def step_have_insight_objects_with_evidence(context):
    """Set up insight objects with evidence."""
    # Already set up in previous steps
    pass


@when('I validate evidence maturity across the chain')
def step_validate_evidence_maturity(context):
    """Validate evidence maturity across the chain."""
    context.evidence_maturity = {
        'problem': context.problem['evidence_status'],
        'result': 'validated',  # Assuming Result has validated evidence
        'behaviors': [b.get('evidence_status', 'draft') for b in context.behaviors],
        'useroutcome': 'validated',  # Inherited from behaviors
        'userflow': 'validated'  # Based on evidence
    }


@then('each object should have appropriate evidence_status')
def step_verify_objects_have_evidence_status(context):
    """Verify each object has appropriate evidence_status."""
    valid_statuses = ['draft', 'validated', 'proven']
    
    assert context.evidence_maturity['problem'] in valid_statuses, "Problem should have valid evidence_status"
    assert context.evidence_maturity['result'] in valid_statuses, "Result should have valid evidence_status"
    for status in context.evidence_maturity['behaviors']:
        assert status in valid_statuses, "Behaviors should have valid evidence_status"


@then('evidence should support the relationships between objects')
def step_verify_evidence_supports_relationships(context):
    """Verify evidence supports relationships between objects."""
    # Check that evidence exists for key relationships
    assert len(context.problem['evidence']) > 0, "Problem should have evidence"
    assert len(context.userflow['evidence']) > 0, "UserFlow should have evidence"
    
    # Check that behavior evidence supports the flow
    for behavior in context.behaviors:
        assert len(behavior['evidence']) > 0, f"Behavior {behavior['id']} should have evidence"


@then('evidence maturity should increase through the chain')
def step_verify_evidence_maturity_increases(context):
    """Verify evidence maturity increases through the chain."""
    # Evidence maturity should generally increase as we move through the chain
    maturity_scores = {
        'draft': 1,
        'validated': 2,
        'proven': 3
    }
    
    problem_maturity = maturity_scores.get(context.evidence_maturity['problem'], 0)
    result_maturity = maturity_scores.get(context.evidence_maturity['result'], 0)
    
    # Result should have at least as much evidence as Problem
    assert result_maturity >= problem_maturity, "Evidence maturity should increase through the chain"


@then('evidence should validate signal strength and reliability')
def step_verify_evidence_validates_signals(context):
    """Verify evidence validates signal strength and reliability."""
    # Check that evidence supports signal claims
    for behavior in context.behaviors:
        assert len(behavior['evidence']) > 0, f"Behavior {behavior['id']} should have evidence supporting signals"
    
    # Check that UserFlow evidence supports the behavior sequence
    assert len(context.userflow['evidence']) > 0, "UserFlow should have evidence supporting behavior sequence"


@then('evidence should support business impact claims')
def step_verify_evidence_supports_business_impact(context):
    """Verify evidence supports business impact claims."""
    # Check that Result has evidence supporting target impact
    assert len(context.original_result['evidence']) > 0, "Result should have evidence supporting business impact"
    
    # Check that evidence includes business impact validation
    evidence_text = ' '.join(context.original_result['evidence']).lower()
    impact_keywords = ['benchmark', 'pilot', 'study', 'analysis', 'results']
    assert any(keyword in evidence_text for keyword in impact_keywords), "Evidence should support business impact claims" 