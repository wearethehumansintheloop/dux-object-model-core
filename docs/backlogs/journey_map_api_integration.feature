Feature: Journey Map API Integration
  As a developer or stakeholder
  I want to verify the journey map API returns correct test results
  So that the UI and reporting are accurate and trustworthy

  Background:
    Given the test-results directory contains valid JUnit XML files

  Scenario: API returns summary and feature data
    When I call the journey map API endpoint for test results
    Then the response should include a summary with total, passed, failed, and skipped counts
    And the response should include a features object with feature names and scenario lists

  Scenario: API handles missing or empty test-results directory
    Given the test-results directory does not exist or is empty
    When I call the journey map API endpoint for test results
    Then the response should include a summary with all counts set to zero
    And the features object should be empty

  Scenario: API returns correct tags for features
    When I call the journey map API endpoint for test results
    Then each feature in the response should include a tags array if tags are present in the feature name
