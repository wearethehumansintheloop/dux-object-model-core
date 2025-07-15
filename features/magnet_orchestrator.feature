Feature: Extract Joel's Resource Management Insights
  As Joel (Cluster Admin)
  I want my resource management challenges to be understood semantically
  So that the platform can help me find solutions regardless of how I describe them

  Background:
    Given I am Joel, a cluster admin managing compute resources
    And I spend significant time manually tracking resource usage
    And I need visibility into resource consumption patterns

  Scenario: Joel describes resource challenges in his own words
    Given I explain my daily routine in natural language
    When the Archivist agent with LLM comprehension reads my story
    Then it should understand resource concepts (GPU, CPU, compute, nodes)
    And it should recognize time-related frustrations regardless of phrasing
    And it should capture the essence not just keywords

  Scenario: RAG enhances understanding of Joel's context
    Given the Archivist found evidence in my story
    When it queries the RAG for similar admin challenges
    Then it should find related problems from other admins
    And it should identify patterns across different resource types
    And it should enrich my evidence with organizational context

  Scenario: Evidence molecules capture semantic meaning
    Given my story mentions "expensive resources" or "idle machines" or "wasted capacity"
    When the LLM creates evidence molecules
    Then each molecule should capture the semantic intent
    And similar concepts should be linked (GPU = compute = resources)
    And the molecules should reflect what I mean, not just what I said

  Scenario: Joel's problem emerges from pattern recognition
    Given evidence molecules and RAG-enhanced context
    When the Problem agent analyzes the semantic patterns
    Then it should synthesize my core job-to-be-done
    And it should understand enablement regardless of technical terms used
    And it should connect my story to broader resource optimization themes

  Scenario: Continuous learning from Joel's language
    Given the extraction understood my resource management story
    When similar scenarios are processed later
    Then the RAG should remember my phrasing patterns
    And future extractions should recognize my terminology
    And the system should adapt to how our team talks about resources