Feature: Frame-Driven Evidence Extraction Flow
  As a research platform
  I want to properly orchestrate Frame → Data → Evidence → Provenance flow
  So that evidence molecules are created with full traceability

  Background:
    Given I have the canonical Frame object from DUX Core
    And I have Joel's GPU monitoring scenario text
    And I have initialized a new extraction session

  Scenario: Frame agent receives canonical Frame object
    Given DUX Core provides a Frame for "resource optimization"
    When the Frame agent ingests this Frame artifact
    Then it should extract the analysis questions
    And it should identify what type of Data to look for
    And it should prepare Frame-specific extraction prompts

  Scenario: Multiple Frames can be applied to same scenario
    Given I have Frames for "resource optimization", "cost management", and "workspace management"
    When analyzing Joel's GPU monitoring story
    Then each Frame should generate different analysis questions
    And "resource optimization" should ask about utilization patterns
    And "cost management" should ask about expensive resource waste
    And "workspace management" should ask about workspace lifecycle

  Scenario: Frame agent identifies Data in Joel's story
    Given the "cost management" Frame asks "What expensive resources are underutilized?"
    When the Frame agent scans Joel's text
    And it finds "expensive GPU nodes sitting idle" 
    Then it should identify this as Data type "cost_waste_indicator"
    And it should mark this for extraction

  Scenario: Session gets logged when Data is identified
    Given the Frame agent identified Data in the text
    When Data extraction begins
    Then a new Session should be created automatically
    And the Session should record "Frame-driven extraction for Joel"
    And the Session should link to the Frame being used

  Scenario: Create Data objects from identified evidence
    Given a Session has been created
    When extracting the identified Data points
    Then each Data object should reference the Session ID
    And each Data object should contain the actual quote
    And each Data object should specify its data_type

  Scenario: Data × Frame creates Evidence Junction
    Given I have a Data object "expensive GPU nodes sitting idle"
    And I have the Frame "cost management"
    When I create the Evidence Junction
    Then it should link data_id and frame_id
    And it should extract a teaser quote
    And it should note strategic insights like "GPU cost waste identified"

  Scenario: Data × Session creates Provenance Junction
    Given I have a Data object with session_id
    And I have the extraction Session
    When I create the Provenance Junction
    Then it should link session_id and data_id
    And it should assess evidence maturity
    And it should create the evidence molecule

  Scenario: Evidence molecules ready for Archivist
    Given I have created Evidence Junctions (Data × Frame)
    And I have created Provenance Junctions (Data × Session)
    When the Archivist receives these molecules
    Then it can analyze them for job_statement components
    And it has full traceability back to source
    And it knows the strategic context from the Frame