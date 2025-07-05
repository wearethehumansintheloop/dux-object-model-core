Feature: Schema Update Validation
  As a developer updating DUX object schemas
  I want to ensure schema updates are safe and maintain data integrity
  So that the governance system remains reliable and consistent

  Background:
    Given I have the DUX v9.6 split schema files
    And I have the markdown object model files
    And I have existing validation scripts

  Scenario: Schema update process validation
    Given I run the schema update script
    When the script processes markdown files
    Then it should create backups of existing schemas
    And it should generate valid JSON schemas
    And it should maintain schema versioning
    And it should not break existing validation scripts

  Scenario: Schema field validation after update
    Given the schemas have been updated
    When I validate each object type
    Then Problem objects should have all required fields
    And Behavior objects should have the end_user field
    And Behavior objects should not have behavior_type field
    And Result objects should have simplified useroutcome_ids
    And UserOutcome objects should have optional user_flow_id
    And User Flow objects should have evidence field
    And User Flow objects should have reference_url instead of protocol_id

  Scenario: Validation script compatibility check
    Given the schemas have been updated
    When I analyze validation scripts
    Then validation scripts should reference valid field names
    And validation scripts should use correct field types
    And validation scripts should handle new conditional logic
    And no validation scripts should reference removed fields

  Scenario: BDD test compatibility after schema update
    Given the schemas have been updated
    When I run existing BDD tests
    Then all schema validation tests should pass
    And all object creation tests should pass
    And all relationship validation tests should pass
    And all data quality tests should pass

  Scenario: Rollback capability validation
    Given the schemas have been updated
    When I attempt to rollback to previous schemas
    Then backup files should be available
    And rollback should restore previous schema versions
    And validation scripts should work with rolled back schemas
    And BDD tests should pass with rolled back schemas

  Scenario: Cross-object relationship integrity
    Given the schemas have been updated
    When I validate object relationships
    Then Problem objects should properly reference Result objects
    And Behavior objects should properly reference Problem objects
    And UserOutcome objects should properly reference User Flow objects
    And all ID references should follow the correct format
    And circular references should be prevented

  Scenario: Schema metadata validation
    Given the schemas have been updated
    When I check schema metadata
    Then each schema should have correct version information
    And each schema should have proper title and description
    And each schema should have valid JSON structure
    And each schema should follow JSON Schema standards 