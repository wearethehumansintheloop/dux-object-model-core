Feature: Insight Object Pattern Validation
  As a UX researcher
  I want to validate the step-by-step insight object pattern and data inheritance
  So that I can ensure proper signal traceability and data flow through the DUX object model

  Background:
    Given I have the DUX v9.6 split schema files
    And I have a Problem object with defined scope and evidence
    And I have a Result object with target impact and success criteria
    And I have Behavior objects with signals and acceptance criteria
    And I have Provenance objects tracking object creation

  Scenario: Step 1 - Core objects are generated (Problem, Result, Behavior)
    Given I have a Problem object with id "problem_cost_optimization"
    And I have a Result object with id "result_reduce_compute_costs"
    And I have Behavior objects with ids ["behavior_analyze_usage", "behavior_identify_waste"]
    When I validate the core object generation
    Then the Problem should have a clear scope and evidence status
    And the Result should have target impact and success criteria
    And the Behaviors should have signals and acceptance criteria
    And all objects should have proper IDs and metadata
    And Provenance objects should be created for each object
    And each object should reference its Provenance ID in the evidence array
    And each object should have a teaser quote in the evidence array
    And each teaser quote should have proper attribution and source file

  Scenario: Step 2 - Result links to Behavior, UserOutcome is created with inherited data
    Given I have a Result object with id "result_reduce_compute_costs"
    And I have Behavior objects with signals and acceptance criteria
    When the Result links to the Behaviors
    Then a UserOutcome should be created with id "outcome_cost_optimization"
    And the UserOutcome should inherit signals from the linked Behaviors
    And the UserOutcome should inherit acceptance criteria from the Behaviors
    And the UserOutcome should reference the Result via result_id
    And the UserOutcome should have an outcome statement derived from the Result target impact
    And a Provenance object should be created for the UserOutcome
    And the UserOutcome should reference its Provenance ID in the evidence array

  Scenario: Step 3 - Problem finds Outcomes, UserFlow is created
    Given I have a Problem object with id "problem_cost_optimization"
    And I have UserOutcome objects related to the Problem
    When the Problem identifies related UserOutcomes
    Then a UserFlow should be created with id "flow_cost_optimization_workflow"
    And the UserFlow should reference the Problem via problem_id
    And the UserFlow should reference the UserOutcome via user_outcome_id
    And the UserFlow should have a title and description
    And the UserFlow should have evidence supporting the relationship
    And a Provenance object should be created for the UserFlow
    And the UserFlow should reference its Provenance ID in the evidence array

  Scenario: Step 4 - Behavior sequence is generated or linked
    Given I have a UserFlow with id "flow_cost_optimization_workflow"
    And I have Behavior objects that contribute to the flow's outcome
    When the UserFlow generates a behavior sequence
    Then the UserFlow should have a behavior_sequence array
    And the behavior_sequence should contain Behavior IDs in logical order
    And each Behavior in the sequence should have defined signals
    And the sequence should represent a complete user journey
    And the sequence should be evidence-backed

  Scenario: Step 5 - UserOutcome inherits data from Behaviors in the flow sequence
    Given I have a UserFlow with a behavior_sequence
    And I have a UserOutcome related to the UserFlow
    When the UserOutcome inherits data from the flow's behaviors
    Then the UserOutcome should have key_signals from the behavior sequence
    And the UserOutcome should have acceptance_criteria derived from behavior criteria
    And the UserOutcome should reference the UserFlow via user_flow_id
    And the inherited signals should be traceable to specific behaviors
    And the acceptance criteria should be measurable and specific

  Scenario: Step 6 - Result inherits from UserOutcome (success metrics)
    Given I have a UserOutcome with key_signals and acceptance_criteria
    And I have a Result object that created the UserOutcome
    When the Result inherits success metrics from the UserOutcome
    Then the Result should have success_metrics derived from UserOutcome key_signals
    And the Result should have success_criteria aligned with UserOutcome acceptance_criteria
    And the Result should reference UserOutcomes via useroutcome_ids
    And the success metrics should be quantifiable leading indicators
    And the metrics should support the Result's target impact

  Scenario: Complete data inheritance validation
    Given I have a complete insight object chain
    When I trace data inheritance through the entire chain
    Then Problem → Result → Behavior → UserOutcome → UserFlow → UserOutcome → Result
    And signals should flow from Behaviors to UserOutcome key_signals
    And UserOutcome key_signals should flow to Result success_metrics
    And acceptance criteria should be consistent across the chain
    And all relationships should be properly referenced
    And the chain should support business impact measurement
    And Provenance objects should track the complete creation chain

  Scenario: Signal traceability validation
    Given I have a complete insight object chain with signals
    When I validate signal traceability
    Then I can trace signals from Behavior → UserOutcome → Result
    And each signal should be observable and measurable
    And signal changes should predict business impact
    And the signal chain should support leading indicator analysis
    And signal aggregation should contribute to target metrics

  Scenario: Provenance tracking validation
    Given I have a complete insight object chain with provenance
    When I validate provenance tracking across the chain
    Then each DUX object should have a corresponding Provenance object
    And each DUX object should reference its Provenance ID in the evidence array
    And each DUX object should have a teaser quote in the evidence array
    And each teaser quote should have proper attribution and source file
    And Provenance objects should record creation timestamps
    And Provenance objects should track data sources and methods
    And Provenance objects should reference related objects
    And Provenance objects should maintain audit trail integrity

  Scenario: Evidence maturity validation
    Given I have insight objects with evidence
    When I validate evidence maturity across the chain
    Then each object should have appropriate evidence_status
    And evidence should support the relationships between objects
    And evidence maturity should increase through the chain
    And evidence should validate signal strength and reliability
    And evidence should support business impact claims 