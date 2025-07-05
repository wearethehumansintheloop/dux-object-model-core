Feature: Test Data Manager Schema Validation
  As a developer working with real research data
  I want the TestDataManager to generate schema-compliant objects
  So that CSV imports produce valid DUX objects

  Background:
    Given I have the DUX v9.5 split schema files
    And I have a TestDataManager instance

  Scenario: TestDataManager generates valid Problem objects
    Given I have sample CSV interview data
    When I generate a Problem object from CSV data
    Then it should pass Problem schema validation
    And it should have valid JTBD format
    And it should have structured evidence blocks
    And it should have proper evidence status

  Scenario: TestDataManager generates valid Behavior objects
    Given I have sample CSV interview data
    When I generate a Behavior object from CSV data
    Then it should pass Behavior schema validation
    And it should have valid enablement statement format
    And it should have structured evidence blocks

  Scenario: TestDataManager handles missing CSV fields gracefully
    Given I have incomplete CSV data
    When I generate objects from incomplete data
    Then it should still produce valid schema-compliant objects
    And it should set appropriate default values
    And it should maintain evidence traceability

  Scenario: Evidence extraction follows schema requirements
    Given I have CSV data with various field names
    When I extract evidence blocks
    Then each evidence block should have required fields
    And provenance should be properly structured
    And evidence types should be correctly classified
    And collection methods should be valid enum values

  Scenario: Cross-validation with actual schema files
    Given I have generated objects from TestDataManager
    When I validate against the actual Problem schema
    Then all required fields should be present
    And all field types should match schema requirements
    And evidence blocks should follow EvidenceBlock schema
    And related object references should follow RelatedObjectReference schema
