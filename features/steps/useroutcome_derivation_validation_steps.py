"""
Step definitions for UserOutcome Derivation from Result Target Impact Metrics
Validates how UserOutcome objects derive acceptance criteria from Result target metrics
"""

import json
import re
from pathlib import Path
from behave import given, when, then


@given('I have Result objects with structured target impact metrics')
def step_have_results_with_target_metrics(context):
    """Set up Result objects with structured target impact metrics."""
    context.results = [
        {
            "object_type": "Result",
            "id": "result_platform_cost_optimization",
            "target_impact": "Reduce customer compute costs leading to $46M ACV increase across existing customers",
            "target_impact_metrics": {
                "metric_type": "revenue",
                "target_value": "$46M ACV increase",
                "target_timeline": "by end of 2025", 
                "customer_scope": "existing customers",
                "success_threshold": "$35M minimum ACV increase"
            },
            "success_criteria": "Achieve 20% average cost reduction across 80% of existing enterprise customers",
            "evidence_maturity": "03_early_signal",
            "evidence": ["prov_customer_cost_analysis", "prov_market_research"]
        },
        {
            "object_type": "Result",
            "id": "result_improved_efficiency",
            "target_impact": "Improve operational efficiency contributing to customer retention and expansion",
            "target_impact_metrics": {
                "metric_type": "efficiency",
                "target_value": "25% efficiency improvement",
                "target_timeline": "Q4 2025",
                "customer_scope": "enterprise segment",
                "success_threshold": "20% minimum efficiency gain"
            },
            "evidence_maturity": "04_balanced_signal",
            "evidence": ["prov_efficiency_studies"]
        }
    ]


@given('I have UserOutcome objects that derive metrics from Results')
def step_have_useroutcomes_derived_from_results(context):
    """Set up UserOutcome objects with derivation from Results."""
    context.useroutcomes = [
        {
            "object_type": "UserOutcome",
            "id": "outcome_automated_cost_optimization",
            "outcome_statement": "Platform teams achieve 20% cost reduction through automated optimization tools.",
            "key_signals": ["optimization_tool_adopted", "cost_analysis_completed", "recommendations_applied"],
            "success_metrics": [
                {
                    "signal": "optimization_tool_adopted",
                    "source_behavior_id": "behavior_adopt_optimization_tool",
                    "measurement_type": "percentage",
                    "baseline_value": "15%",
                    "target_value": "80%",
                    "degree_of_change_required": "65% increase in adoption",
                    "customer_organizations_count": "320 out of 400 existing enterprise customers",
                    "derived_from_result_id": "result_platform_cost_optimization",
                    "leading_indicator": True
                },
                {
                    "signal": "cost_analysis_completed",
                    "source_behavior_id": "behavior_analyze_cost_patterns",
                    "measurement_type": "frequency",
                    "baseline_value": "monthly",
                    "target_value": "weekly",
                    "degree_of_change_required": "4x increase in analysis frequency",
                    "customer_organizations_count": "280 out of 400 existing enterprise customers",
                    "derived_from_result_id": "result_platform_cost_optimization",
                    "leading_indicator": True
                }
            ],
            "acceptance_criteria": [
                "80% of existing enterprise customers adopt optimization tools within 12 months",
                "Weekly cost analysis completion rate reaches 70% across target customer base",
                "Average cost reduction of 20% achieved across participating customers"
            ],
            "derivation_logic": {
                "source_result_ids": ["result_platform_cost_optimization"],
                "inference_method": "proportional_allocation",
                "customer_impact_assumption": "Each customer achieving 20% cost reduction contributes average $115K annual ACV increase"
            },
            "target_impact_when_achieved": "Contributes $36.8M of the $46M ACV target through customer cost savings",
            "evidence_maturity": "03_early_signal",
            "evidence": ["prov_customer_adoption_data"]
        }
    ]


@given('I have a business target of "{target}"')
def step_have_business_target(context, target):
    """Set the business target for validation."""
    context.business_target = target
    context.target_acv_amount = 46000000  # $46M
    context.target_customer_scope = "existing customers"
    context.target_timeline = "end of 2025"


@given('I have a UserOutcome that needs to define success metrics')
def step_have_useroutcome_needing_metrics(context):
    """Set up a UserOutcome that needs to define success metrics."""
    context.current_useroutcome = context.useroutcomes[0]


@given('I have multiple Behavior objects with different signal types')
def step_have_behaviors_with_different_signals(context):
    """Set up Behavior objects with various signal types."""
    context.available_behaviors = [
        {
            "object_type": "Behavior",
            "id": "behavior_adopt_optimization_tool",
            "user_enablement": "Platform admin is able to adopt automated optimization tools",
            "signals": ["optimization_tool_adopted", "tool_configuration_completed", "first_optimization_run"],
            "behavior_type": "Task"
        },
        {
            "object_type": "Behavior", 
            "id": "behavior_analyze_cost_patterns",
            "user_enablement": "Platform admin is able to analyze cost patterns regularly",
            "signals": ["cost_analysis_completed", "pattern_identification", "cost_report_generated"],
            "behavior_type": "Task"
        },
        {
            "object_type": "Behavior",
            "id": "behavior_irrelevant_task",
            "user_enablement": "User is able to perform irrelevant task",
            "signals": ["irrelevant_signal", "unrelated_action"],
            "behavior_type": "Action"
        }
    ]


@when('the UserOutcome selects behaviors with relevant signals')
def step_useroutcome_selects_relevant_behaviors(context):
    """Analyze how UserOutcome selects relevant behavior signals."""
    outcome_signals = context.current_useroutcome.get('key_signals', [])
    
    context.signal_selection_analysis = {
        'outcome_signals': outcome_signals,
        'selected_behaviors': [],
        'signal_alignment': {},
        'relevance_scores': {}
    }
    
    # Analyze which behaviors have signals that align with the outcome
    for behavior in context.available_behaviors:
        behavior_signals = behavior.get('signals', [])
        aligned_signals = set(outcome_signals) & set(behavior_signals)
        
        if aligned_signals:
            context.signal_selection_analysis['selected_behaviors'].append(behavior)
            context.signal_selection_analysis['signal_alignment'][behavior['id']] = list(aligned_signals)
            context.signal_selection_analysis['relevance_scores'][behavior['id']] = len(aligned_signals) / len(behavior_signals)


@then('it should choose behaviors whose signals align with the target impact')
def step_verify_signal_alignment_with_target(context):
    """Verify that selected behaviors align with target impact."""
    selected_behaviors = context.signal_selection_analysis['selected_behaviors']
    
    assert len(selected_behaviors) > 0, "UserOutcome should select at least one behavior with aligned signals"
    
    # Verify that irrelevant behaviors are not selected
    selected_ids = [b['id'] for b in selected_behaviors]
    assert 'behavior_irrelevant_task' not in selected_ids, "Should not select behaviors with irrelevant signals"
    
    # Verify that relevant behaviors are selected
    assert 'behavior_adopt_optimization_tool' in selected_ids, "Should select behavior with optimization signals"


@then('the selected signals should be measurable and observable')
def step_verify_signals_measurable_observable(context):
    """Verify that selected signals are measurable and observable."""
    for behavior in context.signal_selection_analysis['selected_behaviors']:
        signals = behavior.get('signals', [])
        
        for signal in signals:
            # Check signal naming conventions for measurability
            assert len(signal) > 5, f"Signal should be descriptive: {signal}"
            assert '_' in signal or 'event' in signal.lower(), f"Signal should follow naming convention: {signal}"
            
            # Signals should suggest observable events
            observable_keywords = ['completed', 'adopted', 'generated', 'created', 'started', 'finished']
            has_observable_aspect = any(keyword in signal.lower() for keyword in observable_keywords)
            assert has_observable_aspect, f"Signal should be observable: {signal}"


@then('the UserOutcome should reference the source_behavior_id for each selected signal')
def step_verify_source_behavior_references(context):
    """Verify that UserOutcome references source behaviors for signals."""
    success_metrics = context.current_useroutcome.get('success_metrics', [])
    
    for metric in success_metrics:
        assert 'source_behavior_id' in metric, f"Success metric should reference source_behavior_id: {metric}"
        
        source_behavior_id = metric['source_behavior_id']
        signal = metric['signal']
        
        # Verify the referenced behavior actually contains this signal
        behavior_found = False
        for behavior in context.available_behaviors:
            if behavior['id'] == source_behavior_id:
                behavior_signals = behavior.get('signals', [])
                assert signal in behavior_signals, f"Signal {signal} not found in behavior {source_behavior_id}"
                behavior_found = True
                break
        
        assert behavior_found, f"Referenced behavior {source_behavior_id} not found"


@given('I have a Result with target_impact_metrics specifying "{target_amount}"')
def step_have_result_with_specific_target(context, target_amount):
    """Set up a Result with specific target amount."""
    context.target_result = context.results[0]  # Use the first result
    assert target_amount in context.target_result['target_impact_metrics']['target_value']


@given('I have a UserOutcome related to that Result')
def step_have_related_useroutcome(context):
    """Set up a UserOutcome related to the target Result."""
    context.related_useroutcome = context.useroutcomes[0]
    
    # Verify the relationship
    derivation_logic = context.related_useroutcome.get('derivation_logic', {})
    source_result_ids = derivation_logic.get('source_result_ids', [])
    assert context.target_result['id'] in source_result_ids


@when('the UserOutcome derives its acceptance criteria from the Result metrics')
def step_derive_acceptance_criteria_from_result(context):
    """Analyze how UserOutcome derives criteria from Result metrics."""
    result_metrics = context.target_result['target_impact_metrics']
    outcome_metrics = context.related_useroutcome['success_metrics']
    
    context.derivation_analysis = {
        'result_target_value': result_metrics['target_value'],
        'result_customer_scope': result_metrics['customer_scope'],
        'result_timeline': result_metrics['target_timeline'],
        'outcome_metrics_count': len(outcome_metrics),
        'derived_references': [],
        'customer_scope_alignment': False
    }
    
    # Check if outcome metrics reference the result
    for metric in outcome_metrics:
        if metric.get('derived_from_result_id') == context.target_result['id']:
            context.derivation_analysis['derived_references'].append(metric)
    
    # Check customer scope alignment
    if result_metrics['customer_scope'] in context.related_useroutcome.get('target_impact_when_achieved', ''):
        context.derivation_analysis['customer_scope_alignment'] = True


@then('the success_metrics should include derived_from_result_id references')
def step_verify_derived_from_result_references(context):
    """Verify that success metrics reference their source Result."""
    derived_metrics = context.derivation_analysis['derived_references']
    total_metrics = context.derivation_analysis['outcome_metrics_count']
    
    assert len(derived_metrics) > 0, "At least some success metrics should reference derived_from_result_id"
    
    # Most metrics should be derived from the target Result
    derivation_ratio = len(derived_metrics) / total_metrics
    assert derivation_ratio >= 0.5, f"At least 50% of metrics should be derived from Result. Got {derivation_ratio:.2%}"


@then('the customer_organizations_count should specify required behavior change scope')
def step_verify_customer_organizations_scope(context):
    """Verify that customer organization counts are specified."""
    success_metrics = context.related_useroutcome['success_metrics']
    
    for metric in success_metrics:
        assert 'customer_organizations_count' in metric, f"Metric should specify customer_organizations_count: {metric}"
        
        count_spec = metric['customer_organizations_count']
        assert len(count_spec) > 10, f"customer_organizations_count should be detailed: {count_spec}"
        
        # Should include both target count and total population
        assert 'out of' in count_spec or 'of' in count_spec, f"Should specify target out of total: {count_spec}"


@then('the degree_of_change_required should align with Result target thresholds')
def step_verify_degree_change_aligns_with_result(context):
    """Verify that degree of change aligns with Result targets."""
    success_metrics = context.related_useroutcome['success_metrics']
    result_target = context.target_result['target_impact_metrics']['target_value']
    
    for metric in success_metrics:
        degree_change = metric['degree_of_change_required']
        
        # Change requirements should be substantial enough to drive business impact
        change_patterns = [r'\d+%', r'\dx', r'\d+\.\dx']
        has_quantified_change = any(re.search(pattern, degree_change) for pattern in change_patterns)
        assert has_quantified_change, f"degree_of_change_required should be quantified: {degree_change}"
        
        # Extract percentage if present
        percentage_match = re.search(r'(\d+)%', degree_change)
        if percentage_match:
            percentage = int(percentage_match.group(1))
            assert percentage >= 10, f"Change requirement should be substantial (>=10%): {percentage}%"


@then('the derivation_logic should document the inference method used')
def step_verify_derivation_logic_documented(context):
    """Verify that derivation logic is properly documented."""
    derivation_logic = context.related_useroutcome.get('derivation_logic', {})
    
    required_fields = ['source_result_ids', 'inference_method', 'customer_impact_assumption']
    for field in required_fields:
        assert field in derivation_logic, f"derivation_logic should include {field}"
    
    # Verify inference method is valid
    valid_methods = ['proportional_allocation', 'threshold_based', 'correlation_analysis', 'expert_judgment']
    inference_method = derivation_logic['inference_method']
    assert inference_method in valid_methods, f"inference_method should be valid: {inference_method}"
    
    # Customer impact assumption should be detailed
    assumption = derivation_logic['customer_impact_assumption']
    assert len(assumption) > 50, f"customer_impact_assumption should be detailed: {assumption}"


@when('I analyze the customer organization behavior change requirements')
def step_analyze_customer_behavior_change_requirements(context):
    """Analyze customer organization behavior change requirements."""
    success_metrics = context.related_useroutcome['success_metrics']
    target_value = context.target_result['target_impact_metrics']['target_value']
    
    context.behavior_change_analysis = {
        'target_business_value': target_value,
        'customer_counts': [],
        'change_requirements': [],
        'total_customers_affected': 0,
        'mathematical_validation': {}
    }
    
    for metric in success_metrics:
        # Extract customer count
        count_spec = metric['customer_organizations_count']
        count_match = re.search(r'(\d+)\s+out of\s+(\d+)', count_spec)
        if count_match:
            target_count = int(count_match.group(1))
            total_count = int(count_match.group(2))
            context.behavior_change_analysis['customer_counts'].append({
                'target': target_count,
                'total': total_count,
                'percentage': target_count / total_count
            })
        
        context.behavior_change_analysis['change_requirements'].append(metric['degree_of_change_required'])
    
    # Calculate total unique customers affected (assuming some overlap)
    if context.behavior_change_analysis['customer_counts']:
        max_customers = max(count['target'] for count in context.behavior_change_analysis['customer_counts'])
        context.behavior_change_analysis['total_customers_affected'] = max_customers


@then('the success_metrics should specify how many customer organizations need to change')
def step_verify_customer_organization_counts_specified(context):
    """Verify that customer organization counts are clearly specified."""
    customer_counts = context.behavior_change_analysis['customer_counts']
    
    assert len(customer_counts) > 0, "Should have extracted customer organization counts from metrics"
    
    for count_info in customer_counts:
        assert count_info['target'] > 0, "Target customer count should be positive"
        assert count_info['total'] > count_info['target'], "Total should be greater than target"
        assert 0.1 <= count_info['percentage'] <= 1.0, f"Target percentage should be reasonable: {count_info['percentage']:.2%}"


@then('the degree_of_change_required should be realistic and achievable')
def step_verify_change_requirements_realistic(context):
    """Verify that change requirements are realistic."""
    change_requirements = context.behavior_change_analysis['change_requirements']
    
    for change_req in change_requirements:
        # Extract percentage changes
        percentage_match = re.search(r'(\d+)%', change_req)
        if percentage_match:
            percentage = int(percentage_match.group(1))
            assert 5 <= percentage <= 200, f"Percentage change should be realistic (5-200%): {percentage}%"
        
        # Extract multiplier changes
        multiplier_match = re.search(r'(\d+)x', change_req)
        if multiplier_match:
            multiplier = int(multiplier_match.group(1))
            assert 1 <= multiplier <= 10, f"Multiplier should be achievable (1-10x): {multiplier}x"


@then('the aggregated behavior changes should mathematically support the ${amount:d}M target')
def step_verify_mathematical_support_for_target(context, amount):
    """Verify that aggregated changes mathematically support the target."""
    total_customers = context.behavior_change_analysis['total_customers_affected']
    target_amount = amount * 1000000  # Convert to dollars
    
    # Extract customer impact assumption
    derivation_logic = context.related_useroutcome['derivation_logic']
    assumption = derivation_logic['customer_impact_assumption']
    
    # Extract dollar amount from assumption if present
    dollar_match = re.search(r'\$(\d+(?:,\d+)*(?:\.\d+)?)[KM]?', assumption)
    if dollar_match:
        dollar_str = dollar_match.group(1).replace(',', '')
        per_customer_value = float(dollar_str)
        
        # Check if it's in thousands (K) or millions (M)
        if 'K' in assumption:
            per_customer_value *= 1000
        elif 'M' in assumption:
            per_customer_value *= 1000000
        
        # Calculate total potential impact
        total_potential_impact = total_customers * per_customer_value
        
        # Should be reasonable relative to target
        assert total_potential_impact >= target_amount * 0.5, \
            f"Total potential impact ({total_potential_impact:,.0f}) should support target ({target_amount:,.0f})"
        
        context.behavior_change_analysis['mathematical_validation'] = {
            'per_customer_value': per_customer_value,
            'total_potential': total_potential_impact,
            'target_amount': target_amount,
            'coverage_ratio': total_potential_impact / target_amount
        }


@then('the customer_impact_assumption should be documented and reasonable')
def step_verify_customer_impact_assumption_reasonable(context):
    """Verify that customer impact assumptions are reasonable."""
    derivation_logic = context.related_useroutcome['derivation_logic']
    assumption = derivation_logic['customer_impact_assumption']
    
    assert len(assumption) > 30, f"Assumption should be detailed: {assumption}"
    
    # Should include quantified impact
    has_quantified_impact = any(pattern in assumption for pattern in ['$', '%', 'increase', 'reduction', 'improvement'])
    assert has_quantified_impact, f"Assumption should include quantified impact: {assumption}"
    
    # Mathematical validation if available
    math_validation = context.behavior_change_analysis.get('mathematical_validation')
    if math_validation:
        coverage_ratio = math_validation['coverage_ratio']
        assert 0.5 <= coverage_ratio <= 2.0, \
            f"Coverage ratio should be reasonable (0.5-2.0): {coverage_ratio:.2f}"
