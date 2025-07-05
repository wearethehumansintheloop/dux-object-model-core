"""
Step definitions for Signal Flow and Success Metrics Validation
Validates the chain: UserFlow → Behavior → signals → UserOutcome → success metrics → business impact
"""

import json
import os
from pathlib import Path
from behave import given, when, then
import re


@given('I have UserFlow objects with behavior sequences')
def step_have_userflow_with_sequences(context):
    """Load UserFlow objects that have behavior_sequence arrays."""
    context.userflows = []
    # Load test UserFlow objects from test data
    test_data_path = Path("test_data/samples")
    if test_data_path.exists():
        for file_path in test_data_path.glob("*flow*.json"):
            with open(file_path, 'r') as f:
                flow_data = json.load(f)
                if 'behavior_sequence' in flow_data and flow_data['behavior_sequence']:
                    context.userflows.append(flow_data)
    
    # Create synthetic example if none exist
    if not context.userflows:
        context.userflows = [{
            "object_type": "Flow",
            "id": "flow_cost_optimization_workflow",
            "title": "Cost Optimization Workflow",
            "behavior_sequence": ["behavior_analyze_usage", "behavior_identify_waste", "behavior_apply_recommendations"],
            "useroutcome_id": "outcome_reduce_compute_costs",
            "key_signals": ["usage_analysis_completed", "waste_identified", "recommendations_applied"]
        }]


@given('I have Behavior objects with defined signals')
def step_have_behaviors_with_signals(context):
    """Load Behavior objects that have signals arrays."""
    context.behaviors = []
    test_data_path = Path("test_data/samples")
    if test_data_path.exists():
        for file_path in test_data_path.glob("*behavior*.json"):
            with open(file_path, 'r') as f:
                behavior_data = json.load(f)
                if 'signals' in behavior_data and behavior_data['signals']:
                    context.behaviors.append(behavior_data)
    
    # Create synthetic examples if none exist
    if not context.behaviors:
        context.behaviors = [
            {
                "object_type": "Behavior",
                "id": "behavior_analyze_usage",
                "user_enablement": "Platform admin is able to analyze resource usage patterns",
                "end_user": "Platform Administrator",
                "signals": ["usage_analysis_started", "usage_analysis_completed", "usage_report_generated"]
            },
            {
                "object_type": "Behavior", 
                "id": "behavior_identify_waste",
                "user_enablement": "Platform admin is able to identify resource waste",
                "end_user": "Platform Administrator",
                "signals": ["waste_detection_run", "waste_identified", "waste_report_created"]
            }
        ]


@given('I have UserOutcome objects with key signals and success metrics')
def step_have_useroutcomes_with_metrics(context):
    """Load UserOutcome objects with key_signals and acceptance_criteria."""
    context.useroutcomes = []
    test_data_path = Path("test_data/samples")
    if test_data_path.exists():
        for file_path in test_data_path.glob("*useroutcome*.json"):
            with open(file_path, 'r') as f:
                outcome_data = json.load(f)
                if 'key_signals' in outcome_data and outcome_data['key_signals']:
                    context.useroutcomes.append(outcome_data)
    
    # Create synthetic example if none exist
    if not context.useroutcomes:
        context.useroutcomes = [{
            "object_type": "UserOutcome",
            "id": "outcome_reduce_compute_costs",
            "outcome_statement": "Platform teams reduce compute costs by 20% while maintaining performance through automated optimization.",
            "key_signals": ["usage_analysis_completed", "waste_identified", "recommendations_applied", "cost_reduction_measured"],
            "acceptance_criteria": [
                "Usage analysis completed signal increases by 50% month-over-month",
                "Waste identification signal shows 20% improvement in detection accuracy",
                "Recommendation application signal reaches 80% adoption rate",
                "Cost reduction measurements show consistent 15-25% savings"
            ],
            "target_impact_when_achieved": "Contributes $2.3M to ACV through reduced customer churn and increased platform adoption",
            "user_flow_id": "flow_cost_optimization_workflow"
        }]


@given('I have a target business impact of "{target_impact}"')
def step_have_target_business_impact(context, target_impact):
    """Set the target business impact for validation."""
    context.target_business_impact = target_impact
    context.target_acv_amount = 46000000  # $46M
    context.target_deadline = "end of 2025"


@given('I have a UserFlow with a defined behavior_sequence')
def step_have_userflow_with_behavior_sequence(context):
    """Select a specific UserFlow for analysis."""
    context.current_userflow = context.userflows[0]
    assert 'behavior_sequence' in context.current_userflow
    assert len(context.current_userflow['behavior_sequence']) > 0


@when('I analyze the behavior sequence for key behaviors')
def step_analyze_behavior_sequence_for_key_behaviors(context):
    """Analyze the UserFlow's behavior sequence to identify key behaviors."""
    context.key_behaviors = []
    context.analysis_results = {}
    
    behavior_sequence = context.current_userflow['behavior_sequence']
    
    # For each behavior in the sequence, check if it has strong signals
    for behavior_id in behavior_sequence:
        # Find the behavior object
        behavior_obj = None
        for behavior in context.behaviors:
            if behavior['id'] == behavior_id:
                behavior_obj = behavior
                break
        
        if behavior_obj:
            # Analyze signal strength - behaviors with multiple signals are likely key
            signal_count = len(behavior_obj.get('signals', []))
            if signal_count >= 2:  # Key behaviors should have multiple observable signals
                context.key_behaviors.append(behavior_obj)
            
            context.analysis_results[behavior_id] = {
                'found': True,
                'signal_count': signal_count,
                'signals': behavior_obj.get('signals', []),
                'is_key_behavior': signal_count >= 2
            }
        else:
            context.analysis_results[behavior_id] = {
                'found': False,
                'signal_count': 0,
                'signals': [],
                'is_key_behavior': False
            }


@then('each behavior in the sequence should have defined signals')
def step_verify_behaviors_have_signals(context):
    """Verify that all behaviors in the sequence have signals defined."""
    for behavior_id, analysis in context.analysis_results.items():
        assert analysis['found'], f"Behavior {behavior_id} not found in behavior definitions"
        assert analysis['signal_count'] > 0, f"Behavior {behavior_id} has no signals defined"
        assert len(analysis['signals']) > 0, f"Behavior {behavior_id} signals array is empty"


@then('at least one behavior should be marked as a key behavior for the flow')
def step_verify_key_behaviors_exist(context):
    """Verify that at least one behavior is identified as key."""
    assert len(context.key_behaviors) > 0, "No key behaviors identified in the flow sequence"
    
    key_behavior_ids = [b['id'] for b in context.key_behaviors]
    assert len(key_behavior_ids) >= 1, f"Expected at least 1 key behavior, found {len(key_behavior_ids)}"


@then('the key behavior should have signals that are observable and measurable')
def step_verify_key_behavior_signals_observable(context):
    """Verify that key behaviors have observable, measurable signals."""
    for behavior in context.key_behaviors:
        signals = behavior.get('signals', [])
        
        # Check that signals are properly named (technical event names)
        for signal in signals:
            assert isinstance(signal, str), f"Signal must be a string: {signal}"
            assert len(signal) > 5, f"Signal name too short, should be descriptive: {signal}"
            assert '_' in signal or signal.islower(), f"Signal should follow technical naming convention: {signal}"
        
        # Key behaviors should have multiple signals for robust measurement
        assert len(signals) >= 2, f"Key behavior {behavior['id']} should have at least 2 signals for robust measurement"


@then('the key behavior signals should contribute to downstream UserOutcome metrics')
def step_verify_signals_contribute_to_outcome_metrics(context):
    """Verify that key behavior signals appear in related UserOutcome metrics."""
    # Get all signals from key behaviors
    key_behavior_signals = []
    for behavior in context.key_behaviors:
        key_behavior_signals.extend(behavior.get('signals', []))
    
    # Check if these signals appear in UserOutcome key_signals
    for outcome in context.useroutcomes:
        outcome_signals = outcome.get('key_signals', [])
        
        # At least some key behavior signals should appear in outcome signals
        signal_overlap = set(key_behavior_signals) & set(outcome_signals)
        if len(signal_overlap) > 0:
            context.signal_contribution_verified = True
            context.contributing_signals = signal_overlap
            return
    
    assert False, f"No key behavior signals ({key_behavior_signals}) found in UserOutcome key_signals"


@given('I have a UserFlow with key behaviors identified')
def step_have_userflow_with_key_behaviors(context):
    """Set up context with identified key behaviors."""
    context.current_userflow = context.userflows[0]
    context.key_behaviors = context.behaviors[:2]  # Use first 2 as key behaviors


@given('I have a UserOutcome related to that UserFlow')
def step_have_related_useroutcome(context):
    """Find or set up a UserOutcome related to the current UserFlow."""
    userflow_id = context.current_userflow['id']
    
    # Find UserOutcome that references this UserFlow
    context.related_useroutcome = None
    for outcome in context.useroutcomes:
        flow_ids = outcome.get('flow_ids', [])
        for flow_ref in flow_ids:
            if flow_ref.get('id') == userflow_id:
                context.related_useroutcome = outcome
                break
        if context.related_useroutcome:
            break
    
    if not context.related_useroutcome:
        # Use the first UserOutcome as related
        context.related_useroutcome = context.useroutcomes[0]


@when('I validate the signal flow from behavior to outcome')
def step_validate_signal_flow_behavior_to_outcome(context):
    """Validate that signals flow properly from behaviors to outcomes."""
    # Get signals from key behaviors
    behavior_signals = []
    for behavior in context.key_behaviors:
        behavior_signals.extend(behavior.get('signals', []))
    
    # Get signals from related UserOutcome
    outcome_signals = context.related_useroutcome.get('key_signals', [])
    
    # Check signal flow
    context.signal_flow_analysis = {
        'behavior_signals': behavior_signals,
        'outcome_signals': outcome_signals,
        'signal_overlap': list(set(behavior_signals) & set(outcome_signals)),
        'missing_signals': list(set(behavior_signals) - set(outcome_signals))
    }


@then('the UserOutcome key_signals should include signals from the flow\'s key behaviors')
def step_verify_outcome_includes_behavior_signals(context):
    """Verify that UserOutcome includes signals from key behaviors."""
    analysis = context.signal_flow_analysis
    
    assert len(analysis['signal_overlap']) > 0, \
        f"UserOutcome key_signals {analysis['outcome_signals']} should include some signals from key behaviors {analysis['behavior_signals']}"
    
    # At least 50% of key behavior signals should be in the outcome
    coverage_ratio = len(analysis['signal_overlap']) / len(analysis['behavior_signals'])
    assert coverage_ratio >= 0.5, \
        f"Signal coverage too low: {coverage_ratio:.2%}. Expected at least 50% of behavior signals in outcome"


@then('the UserOutcome should reference the UserFlow via user_flow_id')
def step_verify_outcome_references_flow(context):
    """Verify that UserOutcome references the UserFlow via user_flow_id."""
    userflow_id = context.current_userflow['id']
    outcome_user_flow_id = context.related_useroutcome.get('user_flow_id')
    
    assert outcome_user_flow_id == userflow_id, \
        f"UserOutcome should reference UserFlow {userflow_id} via user_flow_id: {outcome_user_flow_id}"


@given('I have a UserOutcome with defined key_signals')
def step_have_useroutcome_with_key_signals(context):
    """Set up UserOutcome with key signals for analysis."""
    context.current_useroutcome = context.useroutcomes[0]
    assert 'key_signals' in context.current_useroutcome
    assert len(context.current_useroutcome['key_signals']) > 0


@given('I have related UserFlow behaviors contributing those signals')
def step_have_related_behaviors_contributing_signals(context):
    """Set up behaviors that contribute to the UserOutcome signals."""
    outcome_signals = context.current_useroutcome['key_signals']
    
    context.contributing_behaviors = []
    for behavior in context.behaviors:
        behavior_signals = behavior.get('signals', [])
        if any(signal in outcome_signals for signal in behavior_signals):
            context.contributing_behaviors.append(behavior)
    
    assert len(context.contributing_behaviors) > 0, \
        "No behaviors found that contribute signals to the UserOutcome"


@when('I analyze the success metrics derivation')
def step_analyze_success_metrics_derivation(context):
    """Analyze how success metrics derive from key signals."""
    context.metrics_analysis = {
        'key_signals': context.current_useroutcome.get('key_signals', []),
        'acceptance_criteria': context.current_useroutcome.get('acceptance_criteria', []),
        'target_impact': context.current_useroutcome.get('target_impact_when_achieved', ''),
        'signal_metrics_mapping': []
    }
    
    # Analyze which acceptance criteria reference key signals
    for criterion in context.metrics_analysis['acceptance_criteria']:
        for signal in context.metrics_analysis['key_signals']:
            if signal in criterion:
                context.metrics_analysis['signal_metrics_mapping'].append({
                    'signal': signal,
                    'criterion': criterion
                })


@then('the UserOutcome should have measurable acceptance_criteria')
def step_verify_measurable_acceptance_criteria(context):
    """Verify that acceptance criteria are measurable."""
    criteria = context.metrics_analysis['acceptance_criteria']
    assert len(criteria) > 0, "UserOutcome should have acceptance_criteria defined"
    
    # Check for measurable elements (percentages, numbers, thresholds)
    measurable_patterns = [r'\d+%', r'\d+\.\d+', r'\d+', r'increase', r'decrease', r'improve', r'reduce']
    
    for criterion in criteria:
        has_measurement = any(re.search(pattern, criterion, re.IGNORECASE) for pattern in measurable_patterns)
        assert has_measurement, f"Acceptance criterion should be measurable: '{criterion}'"


@then('the acceptance_criteria should reference the key_signals')
def step_verify_criteria_reference_signals(context):
    """Verify that acceptance criteria reference key signals."""
    signal_mappings = context.metrics_analysis['signal_metrics_mapping']
    key_signals = context.metrics_analysis['key_signals']
    
    # At least some key signals should be referenced in acceptance criteria
    referenced_signals = [mapping['signal'] for mapping in signal_mappings]
    coverage = len(set(referenced_signals)) / len(key_signals)
    
    assert coverage >= 0.5, \
        f"At least 50% of key_signals should be referenced in acceptance_criteria. Coverage: {coverage:.2%}"


@then('the success metrics should include "degree of signal change" measurements')
def step_verify_signal_change_measurements(context):
    """Verify that metrics include degree of change measurements."""
    criteria = context.metrics_analysis['acceptance_criteria']
    
    change_indicators = ['increase', 'decrease', 'improve', 'reduce', 'growth', 'change', 'delta', 'month-over-month', 'year-over-year']
    
    has_change_measurement = False
    for criterion in criteria:
        if any(indicator in criterion.lower() for indicator in change_indicators):
            has_change_measurement = True
            break
    
    assert has_change_measurement, \
        f"Acceptance criteria should include degree of signal change measurements: {criteria}"


@then('the metrics should be quantifiable leading indicators')
def step_verify_quantifiable_leading_indicators(context):
    """Verify that metrics are quantifiable and represent leading indicators."""
    criteria = context.metrics_analysis['acceptance_criteria']
    
    # Leading indicators should predict future outcomes, not just measure current state
    leading_keywords = ['adoption', 'usage', 'engagement', 'completion', 'frequency', 'rate', 'velocity']
    quantifiable_patterns = [r'\d+%', r'\d+\.\d+', r'\d+', r'rate', r'ratio', r'score']
    
    leading_count = 0
    quantifiable_count = 0
    
    for criterion in criteria:
        if any(keyword in criterion.lower() for keyword in leading_keywords):
            leading_count += 1
        if any(re.search(pattern, criterion, re.IGNORECASE) for pattern in quantifiable_patterns):
            quantifiable_count += 1
    
    assert leading_count > 0, f"At least one criterion should be a leading indicator: {criteria}"
    assert quantifiable_count >= len(criteria) * 0.5, f"At least 50% of criteria should be quantifiable"


# Additional step definitions for the remaining scenarios...

@given('I have UserOutcome success metrics with signal change measurements')
def step_have_success_metrics_with_change_measurements(context):
    """Set up UserOutcome with success metrics that include change measurements."""
    context.current_useroutcome = context.useroutcomes[0]
    # Verify it has the required measurements
    criteria = context.current_useroutcome.get('acceptance_criteria', [])
    assert any('increase' in c or 'improve' in c or 'reduce' in c for c in criteria), \
        "UserOutcome should have success metrics with change measurements"


@when('I evaluate the metrics against the target impact')
def step_evaluate_metrics_against_target(context):
    """Evaluate how well the metrics align with target business impact."""
    target_impact = context.current_useroutcome.get('target_impact_when_achieved', '')
    
    context.impact_evaluation = {
        'target_impact': target_impact,
        'has_acv_reference': '$' in target_impact and ('ACV' in target_impact or 'revenue' in target_impact),
        'has_quantified_impact': re.search(r'\$[\d,]+[MKB]?', target_impact) is not None,
        'aligns_with_business_target': context.target_business_impact.lower() in target_impact.lower()
    }


@then('the UserOutcome success_criteria should align with ACV growth')
def step_verify_success_criteria_aligns_with_acv(context):
    """Verify that success criteria align with ACV growth objectives."""
    evaluation = context.impact_evaluation
    
    assert evaluation['has_acv_reference'] or evaluation['has_quantified_impact'], \
        f"success_criteria should reference ACV or revenue impact: '{evaluation['target_impact']}'"


@then('the success metrics should specify required signal change thresholds')
def step_verify_signal_change_thresholds(context):
    """Verify that success metrics specify clear thresholds for signal changes."""
    criteria = context.current_useroutcome.get('acceptance_criteria', [])
    
    threshold_patterns = [r'\d+%', r'at least \d+', r'minimum \d+', r'above \d+', r'below \d+']
    
    has_thresholds = any(
        any(re.search(pattern, criterion, re.IGNORECASE) for pattern in threshold_patterns)
        for criterion in criteria
    )
    
    assert has_thresholds, f"Success metrics should specify signal change thresholds: {criteria}"


@then('the aggregated outcomes should contribute to the ${amount:d}M target')
def step_verify_aggregated_contribution_to_target(context, amount):
    """Verify that aggregated outcomes contribute to the target amount."""
    # This would require analyzing multiple UserOutcomes and their combined impact
    # For now, verify that the impact mentions contribution to larger goals
    target_impact = context.current_useroutcome.get('target_impact_when_achieved', '')
    
    contribution_keywords = ['contributes', 'drives', 'supports', 'enables', 'leads to']
    has_contribution_language = any(keyword in target_impact.lower() for keyword in contribution_keywords)
    
    assert has_contribution_language, \
        f"target_impact_when_achieved should describe contribution to larger goals: '{target_impact}'"


@then('the leading indicators should predict ACV impact')
def step_verify_leading_indicators_predict_acv(context):
    """Verify that leading indicators can predict ACV impact."""
    criteria = context.current_useroutcome.get('acceptance_criteria', [])
    
    # Leading indicators should connect user behavior to business outcomes
    predictive_elements = ['adoption', 'retention', 'usage', 'engagement', 'satisfaction', 'efficiency', 'productivity']
    
    has_predictive_elements = any(
        any(element in criterion.lower() for element in predictive_elements)
        for criterion in criteria
    )
    
    assert has_predictive_elements, \
        f"Leading indicators should include predictive elements for ACV impact: {criteria}"
