Feature: Advocate Agent Coordination and Relationship Orchestration
  As an Advocate agent
  I want to coordinate specialized extraction agents and orchestrate object relationships
  So that Problem, Behavior, and Result objects are properly linked with evidence

  Background:
    Given I receive evidence packages from Archivist
    And I have access to Columbo (Behavior agent) and Beane (Result agent)
    And I understand the signal flow requirements for object relationships

  Scenario: Advocate receives evidence package with sufficient job_statement coverage
    Given Archivist passes evidence molecule with 2/3 job_statement fields + 1 gap
    When I analyze the evidence package quality
    Then I should identify which field has evidence and which has the gap
    And I should assess if the evidence supports specialized agent extraction
    And I should prepare pitches for appropriate downstream agents

  Scenario: Advocate pitches to Columbo for behavior extraction
    Given evidence package contains user_enablement evidence
    When I prepare a pitch for Columbo
    Then I should include relevant provenance IDs for behavior evidence
    And I should specify expected behavior signals from the evidence
    And I should request Columbo to extract Behavior objects
    And if Columbo accepts, I pass the provenance IDs for evidence arrays

  Scenario: Advocate pitches to Beane for result extraction  
    Given evidence package contains user_outcome evidence
    When I prepare a pitch for Beane
    Then I should include relevant provenance IDs for result evidence
    And I should specify expected result metrics from the evidence
    And I should request Beane to extract Result objects
    And if Beane accepts, I pass the provenance IDs for evidence arrays

  Scenario: Advocate orchestrates object relationship creation
    Given Columbo created a Behavior object with ID "behavior_001"
    And Beane created a Result object with ID "result_001"
    And Problem object "problem_001" was the source evidence
    When I coordinate the relationship linking
    Then newly created Behavior object stores "problem_001" in problem_ids array
    And newly created Result object stores "problem_001" in problem_ids array
    And Problem object "problem_001" stores "behavior_001" in its relationship field
    And Problem object "problem_001" stores "result_001" in its relationship field

  Scenario: Advocate handles agent rejection scenarios
    Given I pitched evidence to Columbo for behavior extraction
    When Columbo rejects the pitch due to insufficient evidence
    Then I should note the rejection reason
    And I should return the evidence to Archivist for additional scanning
    And I should specify what additional evidence is needed

  Scenario: Advocate maintains signal flow traceability
    Given I coordinated creation of linked Problem, Behavior, and Result objects
    When I validate the signal flow requirements
    Then Behavior signals should be traceable to Problem evidence
    And Result metrics should derive from Behavior signals
    And the complete chain should support UserOutcome measurement
    And evidence_maturity should be preserved through the relationship chain