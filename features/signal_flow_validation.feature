Feature: Signal Flow and Success Metrics Validation
  As a product strategist
  I want to validate that UserFlow sequences identify key behaviors whose signals drive UserOutcome success metrics
  So that we can ensure proper signal traceability from user actions to business impact ($46M ACV target)

  Background:
    Given I have the DUX v9.5 split schema files
    And I have UserFlow objects with behavior sequences
    And I have Behavior objects with defined signals
    And I have UserOutcome objects with key signals and success metrics
    And I have a target business impact of "$46M ACV increase by end of 2025"

  Scenario: Validate UserFlow behavior sequencing identifies key behaviors
    Given I have a UserFlow with a defined behavior_sequence
    When I analyze the behavior sequence for key behaviors
    Then each behavior in the sequence should have defined signals
    And at least one behavior should be marked as a key behavior for the flow
    And the key behavior should have signals that are observable and measurable
    And the key behavior signals should contribute to downstream UserOutcome metrics

  Scenario: Validate key behavior signals are passed to related UserOutcome
    Given I have a UserFlow with key behaviors identified
    And I have a UserOutcome related to that UserFlow
    When I validate the signal flow from behavior to outcome
    Then the UserOutcome key_signals should include signals from the flow's key behaviors
    And the UserOutcome should reference the UserFlow in its flow_ids array
    And the reference_context should explain how the flow contributes to the outcome
    And the signal mapping should be traceable and logical

  Scenario: Validate UserOutcome success metrics derive from key signals
    Given I have a UserOutcome with defined key_signals
    And I have related UserFlow behaviors contributing those signals
    When I analyze the success metrics derivation
    Then the UserOutcome should have measurable acceptance_criteria
    And the acceptance_criteria should reference the key_signals
    And the success metrics should include "degree of signal change" measurements
    And the metrics should be quantifiable leading indicators

  Scenario: Validate signal change measurements drive toward target impact
    Given I have UserOutcome success metrics with signal change measurements
    And I have a target impact of "$46M ACV increase aggregated across existing customers"
    When I evaluate the metrics against the target impact
    Then the UserOutcome target_impact_when_achieved should align with ACV growth
    And the success metrics should specify required signal change thresholds
    And the aggregated outcomes should contribute to the $46M target
    And the leading indicators should predict ACV impact

  Scenario: Validate end-to-end signal traceability for business impact
    Given I have a complete signal chain from UserFlow to business target
    When I trace signals from behavior through outcome to business impact
    Then I can identify the path: UserFlow → key Behavior → signals → UserOutcome → success metrics → ACV impact
    And each link in the chain should be evidence-backed
    And the evidence_maturity should support the signal strength claims
    And the LLM evaluation criteria should be explicit and measurable

  Scenario: Validate LLM evaluation criteria for success metrics
    Given I have UserOutcome objects with success metrics
    When I analyze the LLM evaluation requirements
    Then the success metrics should include clear evaluation criteria
    And the criteria should specify how to measure "degree of signal change"
    And the evaluation should distinguish between leading and lagging indicators
    And the LLM should be able to assess progress toward the $46M target
    And the evaluation framework should handle signal aggregation across customers
