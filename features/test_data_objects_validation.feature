Feature: Test Data Object Validation
  As a developer working with real research data
  I want to validate test objects from the test data folder
  So that I can ensure they meet schema and business requirements

  Background:
    Given I have the DUX v9.5 split schema files
    And I have a Problem object schema

  Scenario: Validate linked Joel-Bella GPU management objects
    When I load a test Problem object from file
    Then it should pass Problem schema validation
    And it should have the required JTBD format description
    And it should have valid evidence status
    And it should have valid cross-object references
    And it should demonstrate persona collaboration
    And the linked objects should have consistent evidence status

  Scenario: Validate sample objects in test data folder
    Given I have sample objects in the test data folder
    When I validate each sample object against its schema
    Then all objects should pass their respective schema validation
    And evidence blocks should follow EvidenceBlock schema structure
    And related object references should be properly formatted

  Scenario: Cross-persona collaboration evidence validation
    Given I have Joel's admin Problem object
    And I have Bella's user Result object
    When I analyze their relationship
    Then the Problem should reference the Result with correct evidence status
    And the evidence should support cross-persona collaboration
    And the relationship should address research questions

  Scenario: Research question mapping validation
    Given I have test objects tagged with research questions
    When I validate their research question alignment
    Then each object should map to appropriate research categories
    And evidence should support the tagged research questions
    And cross-persona objects should address collaboration questions
