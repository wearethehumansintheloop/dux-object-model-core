Feature: Journey Map Component
  As a product team member
  I want to visualize the connection between engineering outputs and user value
  So that I can track progress and make informed decisions about work prioritization

  Background:
    Given the atomic object model is properly configured
    And the journey map component is initialized
    And test data is available with object model mappings

  Scenario: Display journey stages with object model connections
    Given I am viewing the journey map
    When the component loads
    Then I should see all journey stages in the correct order:
      | Stage | Order |
      | Authentication | 1 |
      | Profile Creation | 2 |
      | Health Verification | 3 |
      | Consent Management | 4 |
      | Medication Matching | 5 |
      | Prescription Processing | 6 |
    And each stage should display its current status
    And each stage should show connected object model data

  Scenario: Target owns journey - User Outcome drives display
    Given I am viewing the journey map
    When I examine any journey stage
    Then the stage should be organized by its User Outcome (Target)
    And the User Outcome should be the primary information displayed
    And related Phase, Workflow, and Feature information should be secondary
    And implementation details (Issues, BDD tests) should be tertiary

  Scenario: View stage details with object model drill-down
    Given I am viewing the journey map
    When I click on the "Authentication" stage
    Then a stage detail modal should open
    And I should see the following object model connections:
      | Object Type | Information Displayed |
      | Phase | User Registration Phase |
      | User Outcome | Secure user account creation |
      | Related Feature BDD | User authentication and security |
      | Capabilities | Identity verification, Session management |
      | Delivery Features | OAuth integration, MFA setup |
      | Work Items | Authentication API, Login UI, Security tests |
    And I should see test scenarios with their current status
    And I should see documentation links for each object

  Scenario: Navigate between related objects
    Given I am viewing stage details for "Authentication"
    When I click on a work item link
    Then I should see implementation details for that work item
    And I should see links to related code repositories
    And I should see links to GitHub/Jira issues
    And I should see test execution results

  Scenario: Filter journey view by object types
    Given I am viewing the journey map
    When I apply a filter for "BDD Features only"
    Then stages should highlight their BDD feature connections
    And stages without BDD features should be dimmed
    When I apply a filter for "Failed tests"
    Then stages with failing tests should be highlighted in red
    And stages with passing tests should be green
    And stages without tests should be gray

  Scenario: Track progress through object model hierarchy
    Given I am viewing the journey map
    When I examine the progress indicators
    Then each stage should show:
      | Metric | Description |
      | User Outcome Progress | Percentage of outcome criteria met |
      | Feature Completion | BDD scenarios passing/total |
      | Work Item Status | Issues completed/total |
      | Test Coverage | Steps with automated tests |
    And the overall journey progress should aggregate from all stages

  Scenario: Real-time updates from work tracking systems
    Given the journey map is connected to GitHub/Jira APIs
    When a work item status changes in the external system
    Then the journey map should update within 5 minutes
    And the affected stage should show the new status
    And progress indicators should recalculate automatically

  Scenario: Traceability validation through ownership model
    Given I am viewing any stage detail
    When I examine the object relationships
    Then data ownership rules should be respected:
      | Owner | Owns References To |
      | Journey Features | Core features, Integration features, External features |
      | GitHub Issues | Related feature files, Related protocols |
      | Journey Phases | Child workflows, Related features, Supporting issues |
    And visual hierarchy should follow Target → Journey → Phase → Implementation
    And cross-references should only be modifiable by their owners

  Scenario: Protocol success criteria mapping
    Given I am viewing a journey stage
    When I examine the success criteria
    Then I should see mapped usability protocol criteria
    And I should see current evaluation status for each criterion
    And I should see links to protocol documentation
    And I should see historical success rate trends

  Scenario: Pre-release vs post-release status visualization
    Given the journey map displays both development and production status
    When I view any stage
    Then I should see two status indicators:
      | Status Type | Description |
      | Development | Current progress in pre-release work |
      | Production | Live system performance and user metrics |
    And I should be able to toggle between views
    And discrepancies between dev and prod should be highlighted

  Scenario: Mobile responsive journey map
    Given I am using a mobile device
    When I view the journey map
    Then stages should stack vertically
    And tap interactions should work for drill-down
    And all essential information should remain accessible
    And the interface should be optimized for touch interaction

  Scenario: Accessibility compliance
    Given I am using assistive technology
    When I navigate the journey map
    Then all stages should be keyboard accessible
    And screen readers should announce stage status clearly
    And color-coded status should have text alternatives
    And focus indicators should be clearly visible

  Scenario: Export journey map data
    Given I am viewing the journey map
    When I request an export
    Then I should be able to export in multiple formats:
      | Format | Content |
      | PDF | Visual journey map with current status |
      | CSV | Detailed object model data and relationships |
      | JSON | Full API response with all object connections |
    And the export should include timestamp and data source information

  Scenario: Journey map performance optimization
    Given the journey map loads with full object model data
    When the component renders
    Then the initial load should complete within 2 seconds
    And stage interactions should respond within 500ms
    And API calls should be cached for 5 minutes
    And the interface should remain responsive during data updates

@debug-page
Scenario: Debug page API exploration
  Given I navigate to the debug page
  When I select different API endpoints
  Then I should see formatted JSON responses
  And each response should include proper metadata

@debug-jtbd-filtering
Scenario: Debug page JTBD filtering
  Given I am on the debug page
  When I test JTBD filtering for "account_management"
  Then I should see only account_management features
  And the response metadata should show the applied filter
