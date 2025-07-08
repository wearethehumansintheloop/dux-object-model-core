Feature: Frame-Archivist API Integration - Extraction Pipeline
  As a researcher triggering the extraction pipeline
  I want the Frame object to interact with the Archivist via API
  So that extraction uses the latest canonical object definitions and schemas

  Background:
    Given the canonical object vault contains current Problem object definitions
    And the core service API is running on port 8504
    And the extraction pipeline is available
    And the Archivist agent is operational

  Scenario: Researcher triggers extraction with Frame update
    Given a researcher triggers the extraction pipeline
    When the Frame object is initialized
    Then the Frame should be updated with latest schemas for core objects
    And the Frame should be updated with latest schemas for junction objects
    And the Frame should maintain "DUX is always a frame" principle
    And the Frame should be ready to coordinate with Archivist

  Scenario: Archivist requests Problem object definition from API
    Given the Frame object has been updated with latest schemas
    And the Archivist needs Problem object definition
    When the Archivist makes a GET request to "localhost:8504/api/objects/problem/definition"
    Then the response should contain the canonical Problem object definition
    And the response should include the complete Schema Attributes table
    And the response should include the canonical example
    And the response should include the current JSON schema

  Scenario: Archivist requests Problem object schema from API
    Given the Archivist has received the Problem object definition
    When the Archivist makes a GET request to "localhost:8504/api/objects/problem/schema"
    Then the response should contain the current JSON schema
    And the schema should be generated from the canonical markdown
    And the schema should be valid JSON Schema draft-07
    And the schema should match the canonical definition

  Scenario: Archivist sends populated object via POST
    Given the Archivist has processed the Frame context
    And the Frame context is "making it easier for Data scientists to deploy models for fine tuning"
    When the Archivist creates a Problem object with attribute values mapped to the Frame
    Then the Problem object should have job_statement relevant to data scientist model deployment
    And the Problem object should have evidence linked to the Frame context
    And the Problem object should have end_user populated with "Data scientists"
    And the Archivist should POST the populated object to "localhost:8504/api/objects/problem"

  Scenario: Frame context influences Problem object examples
    Given the Frame context is "making it easier for Data scientists to deploy models for fine tuning"
    And the Archivist receives the canonical Problem object definition
    When the Archivist processes the canonical example
    Then the canonical example should be contextually relevant to the Frame
    And the job_statement should relate to data scientist workflow challenges
    And the what_is_at_stake should reflect deployment friction costs
    And the end_user should include data scientist personas

  Scenario: API ensures Archivist has latest definitions
    Given the canonical Problem object definition has been updated
    When the Archivist makes a GET request to the API
    Then the API should return the most current definition
    And the API should include version information
    And the API should indicate if the definition has changed since last request
    And the Archivist should update its processing accordingly

  Scenario: Schema injection with Frame-mapped attribute values
    Given the Archivist has the Problem object schema
    And the Frame context provides specific attribute value mappings
    When the agent injects the schema with attribute values
    Then each attribute should be populated with Frame-relevant values
    And the job_statement should reflect the Frame's specific use case
    And the evidence should reference Frame-related provenance
    And the populated object should validate against the canonical schema

  Scenario: Full Frame-to-Archivist workflow
    Given a researcher triggers extraction for "GPU management for ML workflows"
    When the Frame object coordinates with the Archivist
    Then the Frame should fetch latest Problem object definition from API
    And the Archivist should receive contextually relevant examples
    And the Archivist should populate Problem objects with Frame-mapped values
    And the populated objects should be sent back via API POST
    And the extraction should proceed with current canonical definitions