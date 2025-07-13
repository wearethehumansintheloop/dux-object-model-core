Feature: Canonical Object Lifecycle - Natural Language First
  As a developer working with the DUX Object Model
  I want a sacred canonical object vault with proper backup procedures
  So that approved object definitions are safely promoted to production

  Background:
    Given the canonical object vault exists
    And the backup system is operational
    And the HITL pipeline is running

  Scenario: Sacred backup before canonical promotion
    Given an object definition approved for production in "hitl_promotion_candidates/"
    When the canonical promotion process begins
    Then the current canonical object definitions should be backed up immediately
    And the backup should be timestamped and stored safely
    And the backup should be verified before proceeding
    And only then should the new definition be moved to the canonical vault

  Scenario: Canonical object vault structure
    Given the canonical object vault
    When I examine the vault structure
    Then it should contain one canonical definition per object type
    And each definition should be in markdown format (natural language first)
    And each definition should have a complete Schema Attributes table
    And the vault should be protected from direct modification

  Scenario: Promotion triggers canonical update
    Given an object definition in "hitl_promotion_candidates/problem_object.md"
    When the promotion automation runs
    Then the current canonical problem definition should be backed up
    And the new definition should replace the canonical version
    And JSON schema should be regenerated from the new canonical markdown
    And validation should confirm the canonical update succeeded

  Scenario: Backup verification and rollback capability
    Given a canonical object backup exists
    When I need to rollback a canonical definition
    Then the backup should be complete and valid
    And the rollback should restore the previous canonical state
    And all dependent schemas should be regenerated
    And the system should validate the rollback succeeded

  Scenario: Natural language first validation
    Given a canonical object definition in markdown
    When validation runs
    Then the Schema Attributes table should be the source of truth
    And JSON schema should be generated from the markdown table
    And the generated schema should validate against the canonical example
    And any inconsistencies should prevent canonical promotion

  Scenario: Object vault protection
    Given the canonical object vault
    When someone attempts direct modification
    Then the modification should be rejected
    And the only valid path should be through HITL promotion
    And audit logs should track all access attempts
    And the vault integrity should be maintained

  Scenario: Canonical vault triggers generation workflow
    Given an object definition has been moved to the canonical object vault
    When the vault detects the new canonical definition
    Then the generation workflow should be triggered automatically
    And docling should explode the attributes into microservices
    And each attribute should be extracted as a separate JSON file
    And each attribute should contain its own schema definition
    And each attribute should be independently validatable
    And each attribute should maintain its relationship context
    And each attribute should be deployable as a standalone service
    And JSON schema should be generated from the canonical markdown
    And prompt templates should be updated from the canonical definition
    And agent prompts should be regenerated with new examples
    And all dependent artifacts should be updated consistently
    And the generation should complete before accepting new promotions