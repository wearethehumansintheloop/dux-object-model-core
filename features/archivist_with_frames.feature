Feature: Archivist Applies Frames During Evidence Extraction
  As an Archivist agent
  I want to apply Frames while extracting evidence
  So that I create properly contextualized evidence molecules

  Background:
    Given I have Joel's GPU monitoring scenario
    And I have canonical Frames from DUX Core
    And I have initialized an extraction session
    And I can validate objects against the current Frame schema from DUX Core
    And I can validate objects against the current Data schema from DUX Core
    And I can validate objects against the current Session schema from DUX Core

  Scenario: Archivist receives multiple Frames to apply
    Given DUX Core provides Frames for "resource optimization" and "cost management"
    When I begin evidence extraction
    Then I should load all Frame analysis questions
    And I should prepare to extract Data through each Frame lens

  Scenario: Archivist identifies Data through Frame lenses
    Given I'm scanning Joel's text "expensive GPU nodes sitting idle"
    When I apply the "cost management" Frame lens
    Then I identify this as Data type "cost_waste_indicator"
    And when I apply the "resource optimization" Frame lens
    Then I identify this as Data type "underutilized_resource"

  Scenario: Archivist creates Session when finding first Data
    Given I identified Data through Frame analysis
    When I extract the first Data object
    Then I automatically create a Session that validates against current schema
    And the Session includes all required fields per schema
    And the Session tracks which Frames are being applied

  Scenario: Archivist creates Data objects with Session reference
    Given I have an active Session
    When I create Data objects for identified evidence
    Then each Data object validates against current Data schema
    And each Data object includes all required fields per schema
    And each Data object maintains reference to the Session
    And each Data object preserves the original quote

  Scenario: Archivist creates junction objects
    Given I have Data objects and active Frames
    When I create the junction objects
    Then I create Evidence Junctions (Data × Frame) for strategic context
    And I create Provenance Junctions (Data × Session) for traceability
    And each junction has proper ID references

  Scenario: Archivist builds evidence molecules for job_statement
    Given I have Evidence and Provenance junctions
    When I analyze for job_statement components
    And I find evidence for "user_scenario" from resource optimization Frame
    And I find evidence for "user_enablement" from cost management Frame
    Then I create an evidence molecule with both components
    And the molecule includes all junction IDs
    And the molecule is ready for Advocate

  Scenario: Archivist passes evidence molecule to Advocate
    Given I created an evidence molecule with 2+ job_statement fields
    When I prepare the handoff
    Then the package includes the evidence molecule
    And it includes which Frames contributed to each field
    And it recommends which agents should process next
    And I pause extraction pending Advocate response

  Scenario: Archivist handles multiple scenarios in sequence
    Given I have both Joel's and Bella's scenarios to process
    When I complete Joel's GPU monitoring extraction
    Then I should reset context for Bella's scenario
    And I should apply appropriate Frames for her use case
    And I should create a new Session for her extraction

  Scenario: Archivist detects multi-Frame alignment (magnetic charge)
    Given I'm analyzing text that matches multiple Frames differently
    When "expensive GPU nodes sitting idle" matches cost, resource, and workspace Frames
    Then I should create separate Evidence Junctions for each Frame
    And I should calculate a "magnetic charge" based on Frame alignment count
    And evidence matching 3+ Frames should be marked as "highly charged"
    And highly charged evidence should be prioritized for extraction

  Scenario: Archivist handles sparse evidence with Frame templates
    Given a Frame contains expected job_statement patterns
    When I find evidence with only "user_scenario" but missing enablement/outcome
    Then I should store this partial evidence for later matching
    And I should continue scanning for the Frame's expected enablement pattern
    And I should match using semantic similarity OR keyword fallback
    And unmatched evidence goes to a "parking lot" for future Frames

  Scenario: Archivist enriches evidence with cross-references
    Given I found similar evidence in previous extractions
    When creating new evidence molecules
    Then I should note patterns across scenarios
    And I should reference related evidence molecules
    And I should calculate pattern confidence scores

  Scenario: Archivist handles evidence maturity progression
    Given I have evidence at "01_assumptive" maturity level
    When I find corroborating evidence in the text
    Then I should upgrade maturity to "02_anecdotal" or higher
    And I should document what triggered the upgrade
    And I should update all related junctions

  Scenario: Archivist manages Frame priority conflicts
    Given multiple Frames want to claim the same evidence
    When "workspace management" and "deployment enablement" both match
    Then I should respect Frame priority levels
    And high priority Frames should process first
    And I should queue lower priority Frame processing

  Scenario: Archivist handles real-time Frame updates
    Given I'm mid-extraction with current Frames
    When DUX Core provides an updated Frame definition
    Then I should complete current evidence molecule
    And I should apply updated Frame to remaining text
    And I should note the Frame version change in metadata