Feature: DUX Object Model Markdown Processing
  As a developer working with the DUX object model
  I want the prompt templates to be automatically updated when the markdown guide changes
  So that the generated prompts stay in sync with the object model specification

  Background:
    Given I have the DUX object model guide markdown file
    And I have the generate_from_markdown.py script

  Scenario: Extract core object definitions from markdown
    When I run the generate_from_markdown.py script
    Then it should extract Problem object definition
    And it should extract Behavior object definition
    And it should extract Result object definition
    And it should extract UserOutcome object definition
    And it should extract Flow object definition
    And each prompt template should include object-specific attributes

  Scenario: Generate prompt templates with proper structure
    When I run the generate_from_markdown.py script
    Then each generated prompt should have a clear object description
    And each prompt should include core DUX v9.5 attributes
    And each prompt should follow the DUX principles of atomicity, traceability, and evidence
    And each prompt should generate the unique attribute values described in the DUX v9.5 split schema definitions
    And the prompts should be saved to the scripts/prompts_from_markdown directory as .md files

  Scenario: Handle missing or malformed markdown gracefully
    Given the markdown file path is incorrect
    When I run the generate_from_markdown.py script
    Then it should display an error message about the missing file
    And it should not create any prompt files
