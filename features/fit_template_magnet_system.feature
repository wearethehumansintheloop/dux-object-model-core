# language: en
Feature: Fit Template Magnet System
  As a research analyst
  I want to use Fit Templates as "magnets" to attract and organize related objects
  So that I can extract structured insights from raw research data

  Background:
    Given I have a Fit Template extracted from a research source
    And I have raw research data from multiple sources
    And I have the DUX v9.5 schema validation system

  Scenario: Apply Cost Management Fit Template to attract cost-related objects
    Given I have a "Cost Management" Fit Template from Joel Platform Admin data
    And I have raw research data from multiple sources
    When I apply the Cost Management Fit Template as a magnet to the data
    Then the system should attract objects related to cost management
    And the attracted objects should include Problems, Behaviors, and Results
    And each attracted object should have evidence maturity classification
    And the objects should be validated against DUX v9.5 schemas
    And the system should output a structured collection of cost-related insights

  Scenario: Apply Kubeflow Bella Fit Template to attract workspace and GenAI objects
    Given I have a "Kubeflow Bella" Fit Template from Workspaces & E2E GenAI study
    And I have raw research data from multiple sources
    When I apply the Kubeflow Bella Fit Template as a magnet to the data
    Then the system should attract objects related to workspace management
    And the system should attract objects related to GenAI adoption patterns
    And the attracted objects should include Flows and UserOutcomes
    And each attracted object should have proper evidence arrays
    And the objects should be validated against DUX v9.5 schemas
    And the system should output a structured collection of workspace and AI insights

  Scenario: Apply Study Guide Purpose Fit Template to attract research methodology objects
    Given I have a "Study Guide Purpose" Fit Template from research methodology artifacts
    And I have raw research data from multiple sources
    When I apply the Study Guide Purpose Fit Template as a magnet to the data
    Then the system should attract objects related to research methodology
    And the system should attract objects related to strategic insights
    And the attracted objects should include Problems and Results
    And each attracted object should have evidence maturity classification
    And the objects should be validated against DUX v9.5 schemas
    And the system should output a structured collection of research framework insights

  Scenario: Apply Operating Models Purpose Fit Template to attract strategic objects
    Given I have an "Operating Models Purpose" Fit Template from IBM MCMP → Nubank & AI GTM artifacts
    And I have raw research data from multiple sources
    When I apply the Operating Models Purpose Fit Template as a magnet to the data
    Then the system should attract objects related to long-term discovery
    And the system should attract objects related to strategic operating models
    And the attracted objects should include UserOutcomes and Results
    And each attracted object should have proper evidence arrays
    And the objects should be validated against DUX v9.5 schemas
    And the system should output a structured collection of strategic insights

  Scenario: Validate attracted objects against Fit Template criteria
    Given I have attracted objects using a Fit Template magnet
    When I validate the attracted objects against the Fit Template criteria
    Then each object should have a fit_matched status of true or false
    And each object should have a fit_alignment_reason explaining the match
    And the system should generate a markdown table with object ID, type, match status, and rationale
    And the system should output an updated JSON array with only matched objects

  Scenario: Generate summary of attracted and matched objects
    Given I have completed Fit Template magnet extraction and validation
    When I generate a summary of the magnet results
    Then the system should provide a narrative summary of total evaluated vs matched objects
    And the summary should include fit quality and thematic alignment
    And the summary should identify gaps or low-confidence areas
    And the summary should include counts by object type and tag
    And the system should output metadata with total_objects, matched_objects, generated_at, and fit_template_version

  Scenario: Export matched objects with governance compliance
    Given I have validated objects that match Fit Template criteria
    When I export the matched objects
    Then the system should output a JSON array with only fit_matched: true objects
    And each object should retain all original fields
    And each object should include fit_alignment_reason
    And the export should include metadata block with total_objects, matched_objects, generated_at, and fit_template_version
    And all objects should be compliant with DUX v9.5 governance standards 