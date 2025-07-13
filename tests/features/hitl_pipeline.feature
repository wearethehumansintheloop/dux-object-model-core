Feature: HITL Pipeline Validation Workflow
  As a DUX Object Model maintainer
  I want to ensure the HITL pipeline correctly processes objects
  So that we maintain quality and prevent regression

  Background:
    Given the HITL folders exist:
      | folder                              |
      | watch_folders/hitl_review           |
      | watch_folders/hitl_review_queue     |
      | watch_folders/hitl_review_rejected  |
      | watch_folders/hitl_rejected         |
      | watch_folders/hitl_failed           |
      | watch_folders/hitl_workshop         |
      | watch_folders/hitl_promotion_candidates |
    And the folders are empty

  Scenario: Accept only markdown files
    When I drop "test_file.txt" into hitl_review
    Then the file should be moved to hitl_rejected
    And the rejection reason should contain "Only .md files are accepted"

  Scenario: Reject files with invalid naming conventions
    When I drop "invalid-name-file.md" into hitl_review
    Then the file should be moved to hitl_rejected
    And the rejection reason should contain "File name does not follow naming conventions"

  Scenario: Enforce one object per folder constraint
    Given a "problem_object_001.md" exists in hitl_workshop
    When I drop "problem_object_002.md" into hitl_review
    And the pipeline processes it through to Stage 3b failure
    Then the file should be moved to hitl_review_queue
    And the queue note should contain "Workshop folder already contains problem object"

  Scenario: Stage 1 validation failure
    When I drop a Problem object without required sections into hitl_review:
      """
      # Problem Object
      
      Missing required sections
      """
    Then the file should be moved to hitl_failed
    And the error log should contain "Missing required section"

  Scenario: Stage 2 consistency validation failure
    When I drop a Problem object with schema-JSON mismatch into hitl_review:
      """
      # 🧩 Problem Object
      
      ## 🎯 Purpose & Strategic Role
      Test purpose
      
      ## 🧠 "What would you say... you do here?"
      > Test JTBD
      
      ## 💡 Why the Problem Object Matters
      - Test matter
      
      ## 📋 Schema Attributes
      | Attribute | Type | Required | Description |
      |-----------|------|----------|-------------|
      | object_type | string | Yes | Must be "Problem" |
      | id | string | Yes | Unique identifier |
      
      ## 📦 Canonical Example (Schema-Compliant)
      ```json
      {
        "object_type": "Problem",
        "id": "problem_001",
        "extra_field": "not in schema"
      }
      ```
      
      ## 🔗 Structural Role & Usage Notes
      - Test notes
      """
    Then the file should be moved to hitl_failed
    And the error log should contain "JSON field 'extra_field' not defined in schema table"

  Scenario: Stage 3a-3b validation failure sends to workshop
    When I drop a valid Problem object with string job_statement into hitl_review:
      """
      # 🧩 Problem Object
      
      ## 🎯 Purpose & Strategic Role
      A Problem object represents a job to be done (JTBD) worth solving.
      
      ## 🧠 "What would you say... you do here?"
      > When I need to test, I want validation, so I can ensure quality.
      
      ## 💡 Why the Problem Object Matters
      - Frames opportunities at the right level
      - Provides structure for scoring
      
      ## 📋 Schema Attributes
      | Attribute | Type | Required | Description |
      |-----------|------|----------|-------------|
      | object_type | string | Yes | Must be "Problem" |
      | id | string | Yes | Unique identifier |
      | job_statement | string | Yes | JTBD statement |
      | evidence | [object] | Yes | Evidence array |
      
      ## 📦 Canonical Example (Schema-Compliant)
      ```json
      {
        "object_type": "Problem",
        "id": "problem_001",
        "job_statement": "When testing, I want validation, so I can ensure quality",
        "evidence": [
          {
            "provenance_id": "test_001",
            "supports_fields": ["job_statement"]
          }
        ]
      }
      ```
      
      ## 🔗 Structural Role & Usage Notes
      - Anchors strategic investment decisions
      - Must be evidence-backed
      """
    Then the file should be moved to hitl_workshop
    And the workshop notes should contain "Stage 3b"
    And the workshop notes should contain "job_statement"

  Scenario: Successful validation promotes to candidates
    When I drop a fully valid Problem object into hitl_review:
      """
      # 🧩 Problem Object
      
      ## 🎯 Purpose & Strategic Role
      A Problem object represents a job to be done (JTBD) worth solving.
      
      ## 🧠 "What would you say... you do here?"
      > When I need to test, I want validation, so I can ensure quality.
      
      ## 💡 Why the Problem Object Matters
      - Frames opportunities at the right level
      - Provides structure for scoring
      
      ## 📋 Schema Attributes
      | Attribute | Type | Required | Description |
      |-----------|------|----------|-------------|
      | object_type | string | Yes | Must be "Problem" |
      | id | string | Yes | Unique identifier |
      | job_statement | object | Yes | JTBD decomposed |
      | evidence | [object] | Yes | Evidence array |
      
      ## 📦 Canonical Example (Schema-Compliant)
      ```json
      {
        "object_type": "Problem",
        "id": "problem_001",
        "job_statement": {
          "user_scenario": "When testing",
          "user_enablement": "I want validation",
          "user_outcome": "so I can ensure quality"
        },
        "evidence": [
          {
            "provenance_id": "test_001",
            "supports_fields": ["job_statement"]
          }
        ]
      }
      ```
      
      ## 🔗 Structural Role & Usage Notes
      - Anchors strategic investment decisions
      - Must be evidence-backed
      """
    Then the file should be moved to hitl_promotion_candidates
    And the validation summary should show all stages passed

  Scenario: Files are cleaned from review folder
    When I drop "problem_object.md" into hitl_review
    And the pipeline starts processing
    Then the file should not exist in hitl_review
    And the file should exist in one of the destination folders

  Scenario Outline: Object type routing
    When I drop "<filename>" into hitl_review
    Then the pipeline should identify object type as "<object_type>"
    
    Examples:
      | filename                          | object_type  |
      | problem_financial_001.md          | problem      |
      | behavior_user_action_002.md       | behavior     |
      | result_efficiency_003.md          | result       |
      | insight_analysis_004.md           | insight      |
      | provenance_survey_005.md          | provenance   |
      | useroutcome_goal_006.md           | useroutcome  |
      | flow_journey_007.md               | flow         |