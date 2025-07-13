Feature: Natural Language API generation
  As a DUX architect
  I want to ensure that our APIs create no garbage data
  So that we can be resource conscious of LLM and cognition costs

  Background:
    Given a new object definition is approved and moved to canonical vault
    And the docling markdown contains embedded JSON schema
    And the object specific validation tests have been passed for all newly created docling Canonical Objects and attributes

  Scenario: Generate a docling markdown payload structure
    Given a docling markdown document for Problem object has passed validaiton
    When I examine the payload structure
    Then it should contain ALL required sections from the template
    And the payload should include:
      """
      # 🎯 Problem Object

      ## 🎯 Purpose & Strategic Role
      Strategic job-to-be-done defining market-level opportunities - focuses on user motivations and desired outcomes

      ## 🧠 "What would you say... you do here?"
      > When I need to understand unmet user needs, I want to capture the core job-to-be-done, so that I can guide product strategy towards meaningful outcomes.

      ## 💡 Why the Problem Object Matters
      - Captures the essential user motivation driving product decisions
      - Links user needs to measurable outcomes and behaviors
      - Provides traceability from evidence to strategic decisions
      - Enables prioritization based on opportunity scores

      ## 📋 Schema Attributes
      | Field | Type | Required | Description |
      |-------|------|----------|-------------|
      | object_type | string (const: "Problem") | Yes | Object type discriminator |
      | id | string | Yes | Unique identifier for this problem |
      | job_statement | object | Yes | JTBD decomposed into three components |
      | evidence | array | Yes | Array of provenance IDs supporting this problem |
      | opportunity_score | object | Yes | ODI score with importance, satisfaction, and value |
      | end_user | array | No | User personas experiencing this problem |
      | what_is_at_stake | string | No | Consequences if problem remains unsolved |

      ## 📦 Canonical Example (Schema-Compliant)
      ```json
      {
        "object_type": "Problem",
        "id": "problem_gpu_management_001",
        "job_statement": {
          "user_scenario": "When I need to deploy ML models quickly",
          "user_enablement": "I want automated infrastructure",
          "user_outcome": "so I can focus on model improvement"
        },
        "evidence": ["provenance_001", "provenance_002"],
        "opportunity_score": {
          "value": 8.5,
          "importance": 9,
          "satisfaction": 1.5
        }
      }
      ```

      ## 🔗 Structural Role & Usage Notes
      - Links to Provenance objects via evidence array
      - Referenced by UserOutcome objects solving this problem
      - Connected to Result objects measuring success
      - Must have at least one evidence reference

      ## 🔧 Generated JSON Schema (From Canonical Definition)
      ```json
      {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "$id": "canonical/problem_object_schema.json",
        "title": "Problem Object Schema (Canonical)",
        "type": "object",
        "properties": {
          "job_statement": {
            "type": "object",
            "properties": {
              "user_scenario": {"type": "string"},
              "user_enablement": {"type": "string"},
              "user_outcome": {"type": "string"}
            },
            "required": ["user_scenario", "user_enablement", "user_outcome"]
          }
        }
      }
      ```
      """

  Scenario: Validate canonical to schema generation
    Given a docling markdown with embedded JSON schema
    When the validation script processes the document
    Then it should extract the Schema Attributes table - one object per table entry
    And it should validate the embedded JSON matches the table in structure and content
    And it should ensure all table attributes exist in the JSON
    And it should verify data types match between table and JSON

  Scenario: Validate prompt generation from docling payload
    Given a docling markdown payload with canonical example
    And the 
    And the example should validate against the embedded schema
    And the prompt should reference current Schema Attributes
    And validation should prevent prompt-schema drift

  Scenario: Validate complex attribute explosion
    Given a docling markdown with complex attributes like job_statement
    When docling explodes the attributes
    Then each complex attribute should produce a microservice payload:
      """
      {
        "attribute_name": "job_statement",
        "parent_object": "Problem",
        "schema": {
          "type": "object",
          "properties": {
            "user_scenario": {"type": "string"},
            "user_enablement": {"type": "string"},
            "user_outcome": {"type": "string"}
          }
        },
        "canonical_example": {
          "user_scenario": "When I need to deploy ML models quickly",
          "user_enablement": "I want automated infrastructure",
          "user_outcome": "so I can focus on model improvement"
        },
        "validation_rules": ["all_properties_required", "string_format_checks"],
        "relationship_context": "core_attribute_of_problem_object"
      }
      """

  Scenario: Validate HITL pipeline compatibility
    Given a new canonical Problem definition with updated schema
    When the HITL validation stages are tested
    Then Stage 3a should process the docling markdown successfully
    And Stage 3b should validate against the new embedded schema
    And the canonical example should pass all validation stages
    And any validation failures should be clearly reported

  Scenario: Validate API payload consistency
    Given a canonical docling markdown document
    When the API serves the canonical definition
    Then the API response should include the full markdown content
    And the response should include the extracted JSON schema
    And the response should include exploded attribute payloads
    And all payloads should maintain relationship context