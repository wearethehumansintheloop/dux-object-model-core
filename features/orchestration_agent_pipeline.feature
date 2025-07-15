Feature: Orchestration Agent Pipeline Trigger and Management
  As an Orchestration Agent
  I want to trigger and manage the Frame-driven extraction pipeline
  So that Frame-specific research agents are generated and deployed for extraction

  Background:
    Given I am the Orchestration Agent for the extraction pipeline
    And I have access to DUX Core API endpoints
    And I can read Frame artifacts from research requests
    And I can generate Frame-specific agent prompts

  Scenario: Pipeline triggered manually for Joel's GPU monitoring research
    Given a researcher requests extraction for "Joel GPU resource optimization"
    And they provide Frame artifact "resource_optimization_frame.md"
    When I receive the manual trigger
    Then I should validate the Frame artifact structure
    And I should extract the Frame's research scope and objectives
    And I should prepare to call DUX Core API for canonical objects

  Scenario: Pipeline triggered automatically by file system watcher
    Given file system watcher detects new research document
    And filename follows governance: "20250108_joel_gpu_interview.md"
    When automatic trigger fires
    Then I should extract Session metadata from filename
    And I should determine appropriate Frame for this session type
    And I should validate Frame availability before proceeding

  Scenario: Orchestration Agent reads Frame artifact
    Given Frame artifact "resource_optimization_frame.md" 
    When I process the Frame with docling
    Then I should extract Frame's research scope and objectives
    And I should identify required agent types (Archivist, Problem, Behavior, Result)
    And I should extract Frame's analysis questions and evidence requirements
    And I should prepare to request canonical object definitions from Core

  Scenario: Orchestration Agent receives prompt canvases from Core API
    Given I need prompt canvases for agent generation
    And I have Frame context for "resource_optimization_frame"
    When I call Core API endpoints with Frame payload
    Then I should POST /api/objects/problem/generate with:
      """
      {
        "frame_type": "resource_optimization",
        "session_id": "joel_gpu_interview_001",
        "context": "GPU monitoring and idle resource challenges"
      }
      """
    And I should POST /api/objects/behavior/generate with Frame context
    And I should POST /api/objects/result/generate with Frame context
    And each response contains Frame-aware prompt canvas as DoclingDocument
    And canvases include Frame-specific examples and agent prompts

  Scenario: Orchestration Agent generates Frame-specific agent prompts
    Given I received prompt canvases as DoclingDocument objects from Core API
    When I generate Frame-specific agents
    Then I should create "resource_opt_archivist_agent.md" with Frame context
    And I should create "resource_opt_problem_agent.md" with canonical Problem
    And I should create "resource_opt_columbo_agent.md" with canonical Behavior
    And I should create "resource_opt_beane_agent.md" with canonical Result
    And each agent should embed Frame's analysis questions in prompt canvas

  Scenario: Generated agents placed in HITL review
    Given I generated 4 Frame-specific agents
    When I prepare for human review
    Then agents should go to "agents_for_review/resource_optimization/" folder
    And each agent file should contain Frame ID and generation timestamp
    And folder should include Frame artifact for review context
    And review should include test scenarios for each agent type

  Scenario: HITL approval triggers agent deployment
    Given agents are approved in HITL review
    When human moves agents to "agents_approved/"
    Then I should deploy agents to extraction pipeline
    And I should create agent coordination metadata
    And I should prepare Session object from research document
    And I should trigger Frame-specific Archivist to begin extraction

  Scenario: Handle Frame API failures gracefully
    Given Core API is unavailable for canonical objects
    When I attempt to generate Frame-specific agents
    Then I should use cached canonical objects if available
    And I should log API failure for system monitoring
    And I should notify requester of degraded capabilities
    And I should queue request for retry when API recovers