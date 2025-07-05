Feature: DUX Object Schema Validation
  As a developer working with the DUX object model
  I want to ensure that all object definitions are schema-compliant
  So that the object model maintains consistency and can be processed reliably

  Background:
    Given I have the DUX v9.5 split schema files

  Scenario: Validate Problem object schema compliance
    Given I have a Problem object schema
    When I validate a sample Problem object
    Then it should pass Problem schema validation
    And it should have the required JTBD format description
    And it should have valid evidence status

  Scenario: Validate Behavior object schema compliance
    Given I have a Behavior object schema
    When I validate a sample Behavior object
    Then it should pass Behavior schema validation
    And it should have the required enablement statement format
    And it should have valid behavior type

  Scenario: Validate Flow object schema compliance
    Given I have a Flow object schema
    When I validate a sample Flow object
    Then it should pass Flow schema validation
    And it should have valid flow type
    And it should have proper behavior sequence

  Scenario: Validate Result object schema compliance
    Given I have a Result object schema
    When I validate a sample Result object
    Then it should pass Result schema validation
    And it should have evidence status defined
    And it should have valid description

  Scenario: Validate UserOutcome object schema compliance
    Given I have a UserOutcome object schema
    When I validate a sample UserOutcome object
    Then it should pass UserOutcome schema validation
    And it should have the required outcome statement format
    And it should have valid priority level

  Scenario: Cross-object reference validation
    Given I have all DUX object schemas
    When I validate cross-object references
    Then Problem objects should reference valid Result IDs
    And Flow objects should reference valid Behavior IDs
    And UserOutcome objects should reference valid Problem IDs
