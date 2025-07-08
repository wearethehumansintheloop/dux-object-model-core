Feature: Frame-Agent Extraction Strategy - End First
  As an extraction pipeline architect
  I want to determine optimal agent-frame mapping strategy
  So that extraction is efficient and maintains DUX compliance

  Background:
    Given the extraction pipeline must produce DUX-compliant objects
    And agents must be contextualized to specific frames
    And we must minimize LLM costs while maximizing quality

  Scenario: One agent instance per frame (Option A)
    Given the extraction produces focused, high-quality objects per scenario
    When working backward through the pipeline
    Then each frame gets its own specialized agent instance
    And each agent has deep context for one specific scenario:
      """
      Agent 1: ML Model Deployment Frame
      - Focuses only on deployment friction
      - Extracts problems specific to deployment
      - Deep understanding of deployment signals
      
      Agent 2: A/B Testing Frame  
      - Focuses only on experimentation friction
      - Extracts problems specific to testing
      - Deep understanding of testing signals
      """
    And extraction parallelizes across multiple agents
    And each agent maintains focus without context switching
    And results are aggregated post-extraction
    But this requires N agent instances for N frames

  Scenario: Single agent handles all frames (Option B)
    Given the extraction must maintain holistic problem understanding
    When working backward through the pipeline
    Then one agent processes all frames sequentially
    And the agent maintains context across all scenarios:
      """
      Single Problem Agent:
      - Processes all 4-5 frames in sequence
      - Maintains relationships between scenarios
      - Identifies overlapping problems across frames
      - Holistic view of problem space
      """
    And agent can identify cross-frame patterns
    And maintains consistent problem identification
    And reduces agent initialization overhead
    But risks context overflow and reduced focus

  Scenario: Hybrid approach - Frame-aware agent pool
    Given we need both focus and efficiency
    When designing the optimal extraction strategy
    Then use a small pool of frame-specialized agents
    And each agent handles related frames:
      """
      Technical Operations Agent:
      - Deployment frame
      - Rollback frame
      - Monitoring frame
      
      Experimentation Agent:
      - A/B testing frame
      - Validation frame
      """
    And agents share canonical base but have frame specialization
    And extraction maintains both depth and breadth
    And LLM costs are balanced with quality

  Scenario: Frame complexity determines strategy
    Given frames vary in complexity and overlap
    When the extraction pipeline analyzes frame set
    Then simple, distinct frames get individual agents
    And complex, overlapping frames share an agent
    And the decision is made dynamically:
      """
      if (frame_overlap > 0.7) {
        use_single_agent();
      } else if (frame_count > 5) {
        use_agent_pool();
      } else {
        use_one_agent_per_frame();
      }
      """
    And extraction quality metrics guide strategy selection