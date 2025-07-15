Feature: Atomic Object Model V3 Validation
  As a QE team member  
  I want to validate that the atomic object model v3 is fully functional
  So that I can trust the multi-project BDD aggregation system

  Background:
    Given the UI service is running at http://matchrx-ui:3000  # ✅ Updated for container
    And the atomic object model contains test data for multiple projects

  @data-structure
  Scenario: Data structure validation
    Given the atomic object model is loaded
    When I query the data structure  
    Then I should see 3 targets
    And I should see 3 journeys  
    And I should see 6 BDD specifications
    And I should see 3 issues
    And I should see 4 projects
    And all cross-references should be properly linked

  @api-basic
  Scenario: Basic atomic API endpoint
    When I call the atomic object model API
    Then I should receive a 200 response
    And the response should include atomic metadata
    And the response should include features data
    And the response should include project summaries
    And the atomic metadata should show cross_references as true

  @api-filtering
  Scenario Outline: Project filtering functionality
    When I call the atomic API with project filter "<project_id>"
    Then I should receive a 200 response
    And the response should only contain data for project "<project_id>"
    And the project filter should be indicated in metadata

    Examples:
      | project_id |
      | PRJ-001    |
      | PRJ-002    |
      | PRJ-003    |
      | PRJ-004    |

  @gap-analysis
  Scenario: Gap analysis endpoint
    When I call the gap analysis API
    Then I should receive a 200 response
    And the response should include status mismatches
    And the response should include failing tests
    And the response should include blocked items
    And each mismatch should have a clear description

  @cross-reference
  Scenario: Cross-reference analysis endpoint
    When I call the cross-reference analysis API
    Then I should receive a 200 response
    And the response should include coverage data for all targets
    And the response should include gap identification
    And each target should have a completion score
    And gaps should be categorized by type

  @hybrid-mode
  Scenario: Hybrid data source functionality
    When I call the API with hybrid data source
    Then I should receive a 200 response
    And the response should include both junit and atomic data sources
    And the response should include combined summary statistics
    And the junit results should be present
    And the atomic results should be present

  @multi-project
  Scenario: Multi-project user flows
    Given there are journeys spanning multiple projects
    When I query cross-project flows
    Then I should see journeys that span multiple projects
    And each cross-project journey should reference specs from different projects
    And the project sources should be clearly identified

  @query-layer
  Scenario: Query layer cross-reference functionality
    Given I have a target ID "TGT-001"
    When I query target relationships
    Then I should see related journeys
    And I should see related BDD specifications
    And I should see related issues
    And I should see related targets
    And all relationships should be bidirectional

  @health-metrics
  Scenario: System health calculation
    When I calculate system health metrics
    Then I should receive an overall health score
    And I should receive test health percentage
    And I should receive alignment score
    And I should see total spec counts
    And I should see passing/failing breakdown

  @team-performance
  Scenario: Team performance analysis
    When I query team performance metrics
    Then I should see performance data for each team
    And each team should have journey count
    And each team should have issue count
    And each team should have BDD spec count
    And each team should have health score

  @status-mismatches
  Scenario: Status mismatch detection
    Given there are issues marked as "Done"
    And there are related BDD specs that are "failing"
    When I run status mismatch analysis
    Then I should detect "Done but Not Passing" mismatches
    And each mismatch should identify the issue and failing specs
    And the mismatch should have a clear description

  @orphaned-objects
  Scenario: Orphaned object detection
    When I run orphaned object analysis
    Then I should find BDD specs without related issues
    And I should find issues without related BDD specs
    And I should find targets with insufficient coverage
    And each orphaned object should be clearly identified

  @project-health
  Scenario Outline: Individual project health validation
    When I query project data for "<project_id>"
    Then I should see project information
    And I should see BDD specifications for that project
    And I should see related journeys
    And I should see related targets
    And I should see a health score calculation

    Examples:
      | project_id |
      | PRJ-001    |
      | PRJ-002    |
      | PRJ-003    |
      | PRJ-004    |

  @error-handling
  Scenario Outline: API error handling
    When I call the API with invalid parameter "<parameter>"
    Then I should receive an appropriate error response
    And the error should include helpful information

    Examples:
      | parameter                    |
      | ?source=invalid             |
      | ?project=NON-EXISTENT       |
      | ?analysis=invalid           |

  @performance
  Scenario: API response performance
    When I call each API endpoint
    Then each response should return within 2 seconds
    And the response should include timing metadata

  @backwards-compatibility
  Scenario: Backwards compatibility with existing JUnit XML
    Given the test-results directory contains valid JUnit XML files
    When I call the test results API with default parameters
    Then I should receive JUnit XML parsed results
    And the existing functionality should work unchanged
    When I call the test results API with source "junit"
    Then I should receive the same JUnit XML results

  @end-to-end
  Scenario: Complete end-to-end workflow
    Given I have multiple projects with test results
    When I aggregate all project data through the API
    And I perform cross-reference analysis
    And I identify gaps and mismatches
    And I calculate health metrics
    Then I should have a complete view of system health
    And I should be able to drill down into specific projects
    And I should see clear actionable insights

  @jtbd-integration  # ✅ Your existing JTBD scenarios are perfect!
  Scenario Outline: JTBD-filtered API endpoints
    When I call the API with JTBD filter "<jtbd_category>"
    Then I should receive a 200 response
    And the response should include jtbd_metadata
    And the applied_filter should be "<jtbd_category>"
    And all features should have matching JTBD category

    Examples:
      | jtbd_category     |
      | account_management|
      | verification      |  
      | matching          |
      | health_services   |
      | financial         |

  @jtbd-metadata
  Scenario: JTBD metadata validation
    When I call the API with source "bdd-enriched"
    Then the response should include jtbd_metadata
    And the jtbd_metadata should have object_model_version "v3"
    And the jtbd_metadata should include timestamp
    And the jtbd_metadata should include applied_filter