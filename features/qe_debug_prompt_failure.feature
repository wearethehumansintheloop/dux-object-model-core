Feature: QE debugs prompt producing incorrect outputs
  As a QE (Quality Engineer) person
  I want to debug when character agents produce incorrect outputs
  So that I can identify prompt issues and improve extraction quality

  Background:
    Given I am a QE engineer monitoring extraction quality
    And I have access to extraction logs and agent think-aloud traces
    And I can view both successful and failed extraction attempts
    And I can access the prompt canvas history

  Scenario: QE detects malformed Problem object from Advocate
    Given the Advocate agent completed extraction job "job_456"
    When I review the generated Problem objects
    And I find a Problem with invalid job_statement format:
      """
      {
        "object_type": "Problem",
        "id": "problem_gpu_001",
        "job_statement": "Users need better GPU monitoring",
        "evidence": ["prov_001"]
      }
      """
    Then I should see this failed schema validation:
      """
      ValidationError: job_statement must be object with user_scenario, user_enablement, user_outcome
      Got: string "Users need better GPU monitoring"
      """
    And I should access the Advocate's think-aloud trace

  Scenario: QE traces incorrect extraction to prompt issue
    Given I'm investigating malformed Problem "problem_gpu_001"
    When I examine the Advocate's think-aloud trace:
      """
      ADVOCATE (V.O)
      The user is talking about GPU monitoring needs. This is clearly a problem.
      I'll create a simple job statement: "Users need better GPU monitoring"
      [END SCENE]
      """
    Then I identify the prompt is using outdated schema (v9.5 string format)
    And I see the agent didn't decompose into user_scenario/enablement/outcome
    And I trace this to the prompt canvas missing v9.6 schema example

  Scenario: QE examines prompt canvas generation history
    Given I identified the Advocate prompt uses outdated schema
    When I check the prompt canvas generation log
    Then I see the canvas was generated from:
      """
      Source: /api/objects/problem/generate
      Frame: resource_optimization
      Generated: 2025-01-08T10:00:00Z
      Schema Version: v9.5 (outdated)
      ```
    And I identify Core API returned old schema version
    And I see canonical vault wasn't updated after schema migration

  Scenario: QE debugs missing evidence attribution
    Given Columbo agent extracted Behaviors without proper evidence
    When I examine a Behavior missing provenance links:
      """
      {
        "object_type": "Behavior",
        "id": "behavior_filter_gpu_001",
        "user_enablement": "Admin filters by GPU type",
        "evidence": []
      }
      """
    And I check Columbo's think-aloud:
      """
      COLUMBO (V.O)
      Just one more thing... I see the filtering action here.
      But I can't find the specific provenance reference.
      I'll create the behavior anyway.
      [END SCENE]
      """
    Then I identify Columbo didn't receive Provenance objects from Archivist
    And I trace the handoff failure between agents

  Scenario: QE identifies Frame context mismatch
    Given Billy Beane agent created Results for wrong domain
    When I see Results about "code deployment metrics" in GPU research:
      """
      {
        "object_type": "Result",
        "id": "result_deployment_speed_001",
        "desired_outcome": "Deploy code in under 5 minutes"
      }
      """
    And I check the Frame context Beane received
    Then I discover Frame was "deployment_optimization" not "resource_optimization"
    And I trace this to Orchestration Agent routing error
    And I find Session metadata had incorrect Frame assignment

  Scenario: QE creates prompt fix recommendation
    Given I've identified Advocate uses outdated v9.5 schema
    When I create a fix recommendation
    Then I document:
      | Issue | Root Cause | Fix Required |
      | Advocate creates string job_statement | Prompt canvas has v9.5 example | Update canonical Problem definition to v9.6 |
      | Missing decomposed structure | No example of user_scenario/enablement/outcome | Add decomposed job_statement to prompt |
      | Schema validation failures | Prompt doesn't match current schema | Regenerate prompt canvas from canonical vault |
    And I create test cases for the fixed prompt:
      """
      Test Input: "When managing GPU resources, I want visibility, so I can optimize"
      Expected Output: {
        "job_statement": {
          "user_scenario": "When managing GPU resources",
          "user_enablement": "I want visibility", 
          "user_outcome": "so I can optimize"
        }
      }
      ```
    And I queue prompt regeneration in HITL pipeline

  Scenario: QE monitors prompt fix effectiveness
    Given I deployed fixed Advocate prompt to staging
    When I run test extraction with same source data
    Then I compare outputs:
      | Metric | Before Fix | After Fix |
      | Schema validation pass rate | 20% | 95% |
      | Job statement decomposition | 0% | 100% |
      | Evidence attribution | 60% | 90% |
    And I verify think-aloud shows correct reasoning:
      """
      ADVOCATE (V.O)
      I need to decompose this into the three components.
      User scenario: "When managing GPU resources"
      User enablement: "I want visibility" 
      User outcome: "so I can optimize"
      This follows the v9.6 decomposed structure.
      [END SCENE]
      ```
    And I approve prompt for production deployment