# language: en
Feature: DUX Molecules
  As a research analyst working with high volume of fragmented, unstructured research data
  I want to rapidly output fit-to-purpose, traceable intelligence from DUX atoms
  So that I can inform both stakeholders' immediate planning decisions and future investment decisions

  Background:
    Given I have validated DUX atoms (Problem, Behavior, Result, Flow, UserOutcome)
    And I have provenance and evidence objects
    And I have the DUX molecule validation system
    And I have unstructured qualitative data that would normally be "dropped"

  Scenario: Create Insight Molecule from DUX atoms
    Given I have a validated Problem atom with evidence
    And I have a validated Behavior atom with evidence
    And I have a validated Result atom with evidence
    When I combine these atoms into an Insight molecule
    Then the system should create a validated Insight object
    And the Insight should link to the Problem, Behavior, and Result atoms
    And the Insight should inherit evidence maturity from the linked atoms
    And the Insight should have its own evidence array with provenance
    And the Insight should be validated against research rules

  Scenario: Create Fit Template Molecule from DUX atoms
    Given I have a validated Problem atom with evidence
    And I have a validated Behavior atom with evidence
    And I have a validated Result atom with evidence
    When I combine these atoms into a Fit Template molecule
    Then the system should create a validated Fit Template object
    And the Fit Template should contain extraction criteria
    And the Fit Template should define chaining rules
    And the Fit Template should specify evidence requirements
    And the Fit Template should be validated against research rules

  Scenario: Create Protocol Molecule from DUX atoms
    Given I have a validated Flow atom with evidence
    And I have validated Behavior atoms with evidence
    And I have validated UserOutcome atoms with evidence
    When I combine these atoms into a Protocol molecule
    Then the system should create a validated Protocol object
    And the Protocol should define research workflow steps
    And the Protocol should specify validation gates
    And the Protocol should include success criteria
    And the Protocol should be validated against research rules

  Scenario: Create Study Molecule from multiple DUX atoms
    Given I have multiple validated Problem atoms
    And I have multiple validated Behavior atoms
    And I have multiple validated Result atoms
    And I have validated Flow and UserOutcome atoms
    When I combine these atoms into a Study molecule
    Then the system should create a validated Study object
    And the Study should contain all research insights
    And the Study should have a coherent narrative
    And the Study should include evidence triangulation
    And the Study should be validated against research rules

  Scenario: Validate DUX molecule evidence inheritance
    Given I have a DUX molecule with linked atoms
    When I validate the molecule's evidence inheritance
    Then the molecule should inherit evidence maturity from atoms
    And the molecule should have its own evidence array
    And the molecule should maintain provenance links
    And the molecule should pass evidence validation rules

  Scenario: Export DUX molecule for governance
    Given I have a validated DUX molecule
    When I export the molecule for governance
    Then the system should output the molecule as JSON
    And the molecule should include all linked atom references
    And the molecule should include evidence arrays
    And the molecule should be compliant with governance standards
    And the molecule should be ready for production use

  Scenario: Create Insight Chain from multiple molecules
    Given I have multiple validated Insight molecules
    When I chain these insights together
    Then the system should create a validated Insight Chain
    And the chain should show relationships between insights
    And the chain should maintain evidence integrity
    And the chain should be validated against research rules
    And the chain should be exportable for governance

  Scenario: Validate DUX molecule against research protocols
    Given I have a DUX molecule
    And I have research protocol requirements
    When I validate the molecule against the protocol
    Then the system should check protocol compliance
    And the system should identify any gaps
    And the system should suggest improvements
    And the system should provide validation feedback
    And the molecule should be marked as protocol-compliant or not

  Scenario: Data Scientist transforms unstructured qualitative data into structured signals
    Given I have a CSV with unstructured columns like "customer_comments", "notes", "reason_for_churn"
    And I have high volume of inconsistent, qualitative inputs that resist standard modeling techniques
    When I use DUX molecules to structure the qualitative data
    Then the system should extract behavioral signals from user-facing data quickly
    And the system should provide traceable provenance for all extracted signals
    And the system should connect signals to business outcomes in explainable, repeatable ways
    And the system should make the data decision-ready for P&L stakeholders

  Scenario: Middle Manager gains organizational leverage through traceable insights
    Given I am a middle manager in product, engineering, or research
    And I have DUX molecules with traceable insights
    When I use these molecules for strategic planning
    Then I should be able to contribute directly to portfolio shaping and resource allocation
    And I should be able to package insight in the language of investment logic
    And I should gain credibility by tying insight to business wins
    And my work products should persist across planning cycles

  Scenario: Researcher shifts from support role to strategic collaborator
    Given I am a UX researcher with DUX molecules
    And I have traceable, inspectable work products
    When I present my findings to stakeholders
    Then my outputs should shape what gets built and funded
    And I should gain visibility through producing artifacts that persist
    And I should shift from support role to strategic collaborator
    And my research should be trusted and defensible

  Scenario: Transform "drop this column" data into structured intelligence
    Given I have unstructured data that would normally be dropped (customer_comments, notes, etc.)
    And I have real user intent, emotion, and surprise behaviors in the data
    When I apply DUX molecule structuring
    Then the system should normalize the meaning without quantifying it into oblivion
    And the system should make the data traceable, testable, and portable
    And the system should make the data trustworthy through traceability
    And the system should turn noise into actionable intelligence

  Scenario: Connect qualitative signals to business outcomes for P&L stakeholders
    Given I have DUX molecules with behavioral signals
    And I need to communicate findings to P&L stakeholders
    When I translate the molecules into business language
    Then the system should connect signals to performance metrics
    And the system should align with business priorities
    And the system should support near-term roadmap framing
    And the system should provide explainable, reproducible insight outputs

  Scenario: Middle Manager hedges against disruption while resources are allocated elsewhere
    Given I am a middle manager who needs to redirect resources for market/technological shifts
    And I have DUX molecules with emerging opportunities and potential pivots
    When I frame these opportunities for P&L stakeholders
    Then I should be able to align with how P&L owners assess risk, timing, and return
    And I should be able to pivot with confidence
    And I should be able to create optionality
    And my insights should be grounded in traceable user behavior

  Scenario: Middle Manager seeks parallel investment capacity
    Given I am a middle manager preparing for potential market shifts
    And I have DUX molecules identifying patterns of unmet need and friction
    When I use these molecules to justify exploration
    Then I should be able to grow headcount or capacity for new differentiators
    And I should preserve momentum on core investments
    And I should enable experimentation that de-risks future pivots
    And I should avoid prematurely signaling failure

  Scenario: Middle Manager supports new user base and market growth
    Given I am a middle manager expanding into adjacent user segments
    And I have DUX molecules with patterns of unmet need and latent demand
    When I structure these patterns for investment logic
    Then I should be able to justify early exploration and resource allocation
    And I should be able to make the case for growth without undermining priorities
    And I should identify friction points and opportunities
    And I should align with existing investment frameworks

  Scenario: Executor ensures strategy is grounded in user needs
    Given I am an executor carrying out a directed strategy
    And I have DUX molecules with actual user needs and behaviors
    When I validate the strategy against these molecules
    Then I should execute confidently with grounded insights
    And I should surface blockers early
    And I should avoid wasting effort on misaligned implementation
    And I should ensure the strategy reflects real user behavior 