Feature: Natural Language API generation
  As a DUX architect
  I want to ensure that our APIs create no garbage data
  So that we can be resource conscious of LLM and cognition costs

  Background:
    Given the API must deliver validated canonical definitions and artifacts
    And all consumers expect current, consistent object definitions
    And the validation pipeline ensures this consistency

  Scenario: API delivers validated canonical payload
    Given the API endpoint "/api/objects/problem/definition" must return current canonical definition
    When tracing backward through the validation pipeline
    Then the API payload must be generated from the canonical vault
    And the canonical vault must contain HITL-approved definitions
    And the HITL approval must have validated against the template
    And the template validation must have checked all required sections:
      """
      ✓ Purpose & Strategic Role
      ✓ "What would you say... you do here?"
      ✓ Why the Object Matters
      ✓ Schema Attributes table
      ✓ Canonical Example (Schema-Compliant)
      ✓ Structural Role & Usage Notes
      ✓ Generated JSON Schema
      """
    And each section must follow the canonical format exactly

  Scenario: Successful API call triggers fresh generation
    Given an agent requests the latest Problem object definition
    When the API receives GET "/api/objects/problem/definition"
    Then the API checks if canonical definition has been updated
    And if updated, triggers fresh generation from canonical vault
    And generates new docling markdown with current timestamp
    And returns the freshly generated payload with 200 OK
    And logs the generation event for cost tracking
    And caches the result for subsequent identical requests

  Scenario: Failed API call prevents garbage generation
    Given an agent requests a non-existent object type
    When the API receives GET "/api/objects/undefined/definition"
    Then the API returns 404 Not Found immediately
    And no generation pipeline is triggered
    And no LLM resources are consumed
    And the error response is minimal and clear:
      """
      {
        "error": "Object type 'undefined' not found in canonical vault",
        "valid_types": ["problem", "behavior", "result", "useroutcome", "flow", "provenance", "insight"]
      }
      """
    And the failure is logged for monitoring

  Scenario: API validates request before generation
    Given a malformed API request arrives
    When the API receives GET "/api/objects/problem/definition?include=invalid_param"
    Then the API validates parameters before any processing
    And returns 400 Bad Request with specific error
    And prevents unnecessary generation cycles
    And saves LLM processing costs
    And provides clear guidance on valid parameters

  Scenario: Cached responses avoid redundant generation
    Given the canonical Problem definition was generated 5 minutes ago
    When multiple identical API requests arrive
    Then the first request triggers generation
    And subsequent requests receive the cached response
    And cache headers indicate freshness
    And no redundant LLM calls are made
    And response time is under 100ms for cached hits
    And cache invalidates only on canonical vault updates

  Scenario: Generation failure returns last known good
    Given the generation pipeline encounters an error
    When the API attempts to generate fresh content
    Then the generation error is logged with full context
    And the API falls back to last known good version
    And returns 200 OK with stale data warning:
      """
      {
        "warning": "Using cached version from [timestamp]",
        "reason": "Current generation failed",
        "data": {last_known_good_payload}
      }
      """
    And triggers alert for manual intervention
    And prevents serving corrupt or incomplete data

  Scenario: Frame context generates fit-to-purpose agents
    Given a docling JSON with rich job_statement examples
    When the API receives POST "/api/objects/problem/generate" with Frame payload:
      """
      {
        "frame_type": "joel_scenarios",
        "job_statement": {
          "user_scenario": [
            "When I need to deploy my fine-tuned model to production",
            "When I want to A/B test model variants",
            "When I need to rollback a problematic model version",
            "When I want to monitor model performance in real-time"
          ],
          "user_enablement": [
            "I want one-click deployment with automatic versioning (signal: deploy_time < 5min)",
            "I want traffic splitting controls without code changes (signal: config_changes_only)",
            "I want instant rollback to previous versions (signal: rollback_time < 30sec)",
            "I want real-time inference metrics dashboard (signal: latency_visibility)"
          ],
          "user_outcome": [
            "so I can iterate faster on model improvements (impact: 3x deployment frequency → faster innovation)",
            "so I can validate improvements before full rollout (impact: risk reduction → higher success rate)",
            "so I can minimize downtime from bad deployments (impact: 99.9% uptime → revenue protection)",
            "so I can catch degradations immediately (impact: MTTR < 5min → customer satisfaction)"
          ]
        },
        "impact_hypothesis": "Reducing ML deployment friction by 80% will increase model iteration speed 3x, leading to 25% improvement in model performance metrics and $2M additional revenue from better predictions"
      }
      """
    Then the API uses multiple examples to create comprehensive agent context
    And generates agents that understand the full problem space
    And each user_scenario maps to specific enablements and outcomes
    And signals are embedded for behavior tracking
    And impact metrics connect to business value
    And the response includes fit-to-purpose agents with rich context

  Scenario: Frame validates against canonical constraints
    Given a Frame context that conflicts with canonical definition
    When the API receives POST with incompatible Frame
    Then the API validates Frame against canonical constraints
    And returns 422 Unprocessable Entity if Frame violates core schema
    And suggests valid Frame modifications
    And prevents generation of non-compliant agents
    And maintains canonical integrity while allowing contextualization
    And the template validation must have checked all required sections:
      """
      ✓ Purpose & Strategic Role
      ✓ "What would you say... you do here?"
      ✓ Why the Object Matters
      ✓ Schema Attributes table
      ✓ Canonical Example (Schema-Compliant)
      ✓ Structural Role & Usage Notes
      ✓ Generated JSON Schema
      """
    And each section must follow the canonical format exactly

  Scenario: Agent prompts contain current canonical examples
    Given agents must use prompts with valid, current examples
    When tracing backward through prompt generation
    Then prompts must be generated from canonical docling markdown
    And docling markdown must contain validated canonical examples
    And canonical examples must pass schema validation
    And schema must be generated from Schema Attributes table
    And Schema Attributes must be from approved canonical definition
    And any mismatch must trigger regeneration

  Scenario: Microservices receive exploded attributes
    Given each attribute must function as an independent microservice
    When tracing backward through attribute explosion
    Then attributes must be exploded by docling from canonical definition
    And canonical definition must contain complete Schema Attributes table
    And each attribute must maintain its relationship context:
      """
      {
        "attribute_name": "job_statement",
        "parent_object": "Problem",
        "schema": {validated_from_canonical},
        "canonical_example": {from_approved_definition},
        "validation_rules": {derived_from_schema},
        "relationship_context": "core_attribute_of_problem_object"
      }
      """
    And explosion must happen only after canonical approval

  Scenario: HITL validates objects with current schemas
    Given HITL pipeline must validate against current canonical schemas
    When tracing backward through validation stages
    Then Stage 3b must use schema generated from canonical markdown
    And Stage 3a must process canonical markdown format
    And Stage 2 must check consistency with canonical template
    And Stage 1 must verify required canonical sections exist
    And all stages must reference the same canonical source
    And validation must prevent non-canonical definitions

  Scenario: Schema reflects canonical attributes exactly
    Given JSON schemas must match canonical Schema Attributes tables
    When tracing backward through schema generation
    Then schemas must be generated from canonical markdown only
    And generation must parse the Schema Attributes table
    And all table attributes must appear in the schema
    And all schema properties must trace to the table
    And any deviation must fail validation
    And regeneration must happen on canonical update