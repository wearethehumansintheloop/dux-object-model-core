Feature: Signal Flow and Success Metrics Validation
  As a product strategist
  I want to validate that UserFlow sequences provide behaviors whose signals drive UserOutcome acceptance criteria
  So that we can ensure proper signal traceability from user actions to business impact ($46M ACV target)

  Background:
    Given I have the DUX v9.5 split schema files
    And I have UserFlow objects with behavior sequences
    And I have Behavior objects with defined signals
    And I have UserOutcome objects with acceptance criteria
    And I have Result objects with success metrics
    And I have a target business impact of "$46M ACV increase by end of 2025"

  Scenario: Validate UserFlow behavior sequencing provides signal sources
    Given I have a UserFlow with a defined behavior_sequence
    When I analyze the behavior sequence for signal sources
    Then each behavior in the sequence should have defined signals
    And the behavior signals should be observable and measurable
    And the behavior signals should contribute to downstream UserOutcome acceptance criteria

  Scenario: Validate behavior signals are inherited by related UserOutcome
    Given I have a UserFlow with behaviors containing signals
    And I have a UserOutcome linked to that UserFlow
    When I validate the signal inheritance from UserFlow to UserOutcome
    Then the UserOutcome key_signals should include signals from the flow's behaviors
    And the UserOutcome should reference the UserFlow in its user_flow_id field
    And the signal inheritance should be traceable and logical

  Scenario: Validate UserOutcome acceptance criteria reference key signals
    Given I have a UserOutcome with defined key_signals
    And I have related UserFlow behaviors contributing those signals
    When I analyze the acceptance criteria derivation
    Then the UserOutcome should have measurable acceptance_criteria
    And the acceptance_criteria should reference the key_signals
    And the acceptance_criteria should include "degree of signal change" measurements
    And the criteria should be quantifiable leading indicators

  Scenario: Validate acceptance criteria drive toward Result success metrics
    Given I have UserOutcome acceptance criteria with signal change measurements
    And I have a Result with success metrics
    And I have a target impact of "$46M ACV increase aggregated across existing customers"
    When I evaluate the acceptance criteria against the Result success metrics
    Then the Result success metrics should align with ACV growth
    And the acceptance criteria should specify required signal change thresholds
    And the aggregated outcomes should contribute to the $46M target
    And the leading indicators should predict ACV impact

  Scenario: Validate end-to-end signal traceability for business impact
    Given I have a complete signal chain from UserFlow to business target
    When I trace signals from behavior through outcome to business impact
    Then I can identify the path: UserFlow → behaviors → signals → UserOutcome → acceptance_criteria → Result → success metrics → ACV impact
    And each link in the chain should be evidence-backed
    And the evidence should support the signal strength claims
    And the LLM evaluation criteria should be explicit and measurable

  Scenario: Validate LLM evaluation criteria for acceptance criteria
    Given I have UserOutcome objects with acceptance criteria
    When I analyze the LLM evaluation requirements
    Then the acceptance criteria should include clear evaluation criteria
    And the criteria should specify how to measure "degree of signal change"
    And the evaluation should distinguish between leading and lagging indicators
    And the LLM should be able to assess progress toward the $46M target
    And the evaluation framework should handle signal aggregation across customers
