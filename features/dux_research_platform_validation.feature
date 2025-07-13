Feature: DUX Research Platform Object Validation
  As a researcher working with the DUX research platform
  I want to ensure that all research objects are schema-compliant and properly linked
  So that research data maintains integrity and can be reliably analyzed

  Background:
    Given I have the DUX v9.6 split schema files
    And I have sample research platform objects

  # Core Atomic Objects
  Scenario: Validate Session object schema compliance
    Given I have a Session object schema
    When I validate a sample Session object
    Then it should pass Session schema validation
    And it should have a valid session_type
    And it should have a valid session_status
    And it should have positive duration_minutes
    And it should have positive participant_count
    And it should reference a valid researcher_id

  Scenario: Validate Data object schema compliance
    Given I have a Data object schema
    When I validate a sample Data object
    Then it should pass Data schema validation
    And it should have a valid data_type
    And it should have non-empty content
    And it should reference a valid source_session_id
    And it should have a valid confidence_level
    And it should have valid timestamp_in and timestamp_out

  Scenario: Validate Frame object schema compliance
    Given I have a Frame object schema
    When I validate a sample Frame object
    Then it should pass Frame schema validation
    And it should have a valid frame_name
    And it should have non-empty frame_description
    And it should have at least one analysis_question
    And it should have a valid priority_level
    And it should have a valid frame_type

  # Collection Objects
  Scenario: Validate Study object schema compliance
    Given I have a Study object schema
    When I validate a sample Study object
    Then it should pass Study schema validation
    And it should have a valid study_name
    And it should have non-empty study_description
    And it should have at least one target_participant
    And it should have positive planned_sessions
    And it should have non-negative completed_sessions
    And it should have a valid study_status
    And it should have at least one researcher_id

  Scenario: Validate Report object schema compliance
    Given I have a Report object schema
    When I validate a sample Report object
    Then it should pass Report schema validation
    And it should have a valid report_name
    And it should have non-empty report_description
    And it should have a valid report_type
    And it should have non-negative data_count
    And it should have a valid report_status
    And it should have a valid created_by

  Scenario: Validate Report Gallery object schema compliance
    Given I have a Report Gallery object schema
    When I validate a sample Report Gallery object
    Then it should pass Report Gallery schema validation
    And it should have a valid gallery_name
    And it should have non-empty gallery_description
    And it should have a valid strategic_theme
    And it should have at least one target_audience
    And it should have non-negative frame_count
    And it should have a valid gallery_status
    And it should have at least one strategic_objective

  # Junction Objects
  Scenario: Validate Provenance Junction object schema compliance
    Given I have a Provenance Junction object schema
    When I validate a sample Provenance Junction object
    Then it should pass Provenance Junction schema validation
    And it should reference a valid session_id
    And it should reference a valid data_id
    And it should have a valid evidence_maturity level
    And it should have at least one evidence_block
    And it should have a confidence_score between 0.0 and 1.0
    And it should have a valid validation_status

  Scenario: Validate Evidence Junction object schema compliance
    Given I have an Evidence Junction object schema
    When I validate a sample Evidence Junction object
    Then it should pass Evidence Junction schema validation
    And it should reference a valid session_id
    And it should reference a valid frame_id
    And it should have a non-empty teaser_quote
    And it should have a valid quote_attribution
    And it should have at least one strategic_insight
    And it should have a relevance_score between 0.0 and 1.0

  Scenario: Validate Insight Junction object schema compliance
    Given I have an Insight Junction object schema
    When I validate a sample Insight Junction object
    Then it should pass Insight Junction schema validation
    And it should reference a valid evidence_id
    And it should reference a valid frame_id
    And it should have a fit_score between 0.0 and 1.0
    And it should have a non-empty insight_teaser
    And it should have at least one insight_story_block
    And it should have a valid confidence_level
    And it should have an actionability_score between 0.0 and 1.0
    And it should have a valid priority_level

  # Cross-Object Relationship Validation
  Scenario: Validate Session-Data relationships
    Given I have Session and Data objects
    When I validate Session-Data relationships
    Then Session objects should reference valid Data IDs
    And Data objects should reference valid Session IDs
    And Session data_ids should match Data source_session_id

  Scenario: Validate Session-Frame relationships
    Given I have Session and Frame objects
    When I validate Session-Frame relationships
    Then Evidence Junction objects should reference valid Session IDs
    And Evidence Junction objects should reference valid Frame IDs
    And Session objects should be analyzable through Frame objects

  Scenario: Validate Evidence-Frame relationships
    Given I have Evidence Junction and Frame objects
    When I validate Evidence-Frame relationships
    Then Insight Junction objects should reference valid Evidence IDs
    And Insight Junction objects should reference valid Frame IDs
    And fit_scores should reflect evidence-frame alignment

  Scenario: Validate Study-Session relationships
    Given I have Study and Session objects
    When I validate Study-Session relationships
    Then Study objects should reference valid Session IDs
    And Session objects should reference valid Study IDs
    And Study session_ids should match Session study_id

  Scenario: Validate Report-Data relationships
    Given I have Report and Data objects
    When I validate Report-Data relationships
    Then Report objects should reference valid Data IDs
    And Data objects should reference valid Report IDs
    And Report data_ids should match Data report_id

  Scenario: Validate Gallery-Frame relationships
    Given I have Report Gallery and Frame objects
    When I validate Gallery-Frame relationships
    Then Report Gallery objects should reference valid Frame IDs
    And Frame objects should reference valid Gallery IDs
    And Gallery frame_ids should match Frame gallery_id

  # Evidence Maturity and Quality Validation
  Scenario: Validate evidence maturity progression
    Given I have Provenance Junction objects with different maturity levels
    When I analyze evidence maturity progression
    Then evidence_maturity should follow the progression: 01_assumptive → 02_anecdotal → 03_early_signal → 04_balanced_signal → 05_triangulated
    And higher maturity levels should have higher confidence_scores
    And triangulation_count should increase with maturity level

  Scenario: Validate fit score calculation
    Given I have Insight Junction objects with fit scores
    When I analyze fit score distribution
    Then fit_scores should be between 0.0 and 1.0
    And high fit_scores should indicate strong evidence-frame alignment
    And low fit_scores should indicate weak evidence-frame alignment
    And fit_scores should correlate with actionability_scores

  # Data Integrity Validation
  Scenario: Validate timestamp consistency
    Given I have Session and Data objects with timestamps
    When I validate timestamp consistency
    Then Session session_date should be before Data created_at
    And Data timestamp_in should be before Data timestamp_out
    And Data timestamps should be within Session duration

  Scenario: Validate ID format consistency
    Given I have research platform objects with IDs
    When I validate ID format consistency
    Then Session IDs should follow pattern "^session_.*"
    And Data IDs should follow pattern "^data_.*"
    And Frame IDs should follow pattern "^frame_.*"
    And Study IDs should follow pattern "^study_.*"
    And Report IDs should follow pattern "^report_.*"
    And Gallery IDs should follow pattern "^gallery_.*"
    And Provenance Junction IDs should follow pattern "^provenance_junction_.*"
    And Evidence Junction IDs should follow pattern "^evidence_junction_.*"
    And Insight Junction IDs should follow pattern "^insight_junction_.*"

  # Workflow Validation
  Scenario: Validate research workflow progression
    Given I have a complete research workflow
    When I validate workflow progression
    Then Session objects should generate Data objects
    And Session × Data should create Provenance Junction objects
    And Session × Frame should create Evidence Junction objects
    And Evidence × Frame should create Insight Junction objects
    And Study objects should group Session objects
    And Report objects should group Data objects
    And Report Gallery objects should group Frame objects

  Scenario: Validate research quality metrics
    Given I have research platform objects with quality metrics
    When I validate quality metrics
    Then confidence_scores should reflect evidence quality
    And relevance_scores should reflect strategic alignment
    And fit_scores should reflect evidence-frame compatibility
    And actionability_scores should reflect implementation potential
    And priority_levels should reflect strategic importance 