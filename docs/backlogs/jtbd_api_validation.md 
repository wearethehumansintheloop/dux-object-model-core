# ui-tests/features/api/jtbd_api_validation.feature
Feature: JTBD API Validation with Test Data
  As a frontend developer
  I want to validate JTBD API responses using realistic test data
  So that I can ensure data integrity across the system

  Background:
    Given the MatchRx UI API is running
    And I have JTBD test data loaded

  @api @data-driven
  Scenario Outline: Validate JTBD categories return correct data
    When I request "/api/test-results?source=features&jtbd=<category>"
    Then the response status should be 200
    And the response should contain only "<category>" features
    And each JTBD should have valid structure
    And the jtbd_metadata should show applied_filter: "<category>"

    Examples:
      | category          |
      | account_management|
      | verification      |
      | matching          |
      | health_services   |
      | financial         |

  @api @integration
  Scenario: Validate cross-reference matrix with scenario data
    Given I have features with cross-references
    When I request "/api/test-results?source=cross-reference-matrix"
    Then the response should include journey mappings
    And each journey should map to test scenarios
    And target alignments should be present