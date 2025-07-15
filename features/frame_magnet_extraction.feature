Feature: Frame Magnet Extraction System
  As the extraction pipeline
  I want to use Frames as magnets to attract and process evidence
  So that insights point to technical solutions not just document problems

  Background:
    Given Frames are the evolution of Fit Templates
    And Frames act as magnets attracting relevant evidence
    And Frame "magnetic charge" increases with multi-frame alignment
    And Solution discovery is embedded in Frame design

  Scenario: Frame contains solution templates not just problem patterns
    Given a Frame for "Resource Optimization"
    When the Frame is loaded
    Then it contains:
      | Component | Traditional Approach | Solution-Oriented Approach |
      | analysis_questions | "What resources are wasted?" | "What can be automated?" |
      | expected_patterns | "time spent", "manual process" | "checking → probe", "monitoring → dashboard" |
      | solution_templates | Not included | "embed probe", "modify template", "add telemetry" |
      | success_criteria | "Find inefficiencies" | "Find automation opportunities" |
    And Frame primes agents to think solutions not just problems

  Scenario: Evidence gains charge through multi-frame alignment
    Given evidence "30 minutes checking idle GPUs"
    When multiple Frames process this evidence
    Then magnetic charging occurs:
      | Frame | Match Reason | Charge Added |
      | Resource Optimization | "idle GPU" = resource waste | +1 charge |
      | Cost Management | "expensive GPU" = cost impact | +1 charge |
      | Admin Efficiency | "30 minutes" = time waste | +1 charge |
      | Platform Intelligence | "checking" = automation opportunity | +1 charge |
    And total charge = 4 (highly charged)
    And highly charged evidence prioritized for extraction
    And multi-perspective synthesis creates richer insights

  Scenario: Frame-specific agents inherit solution focus
    Given Frame "Resource Optimization" with probe automation focus
    When Archivist agent is generated
    Then agent prompt includes:
      """
      You are a Resource Optimization Archivist.
      When you find evidence of manual monitoring, tag it as "automation_opportunity".
      When you find repetitive tasks, note "template_modification_candidate".
      When you find resource checking, think "probe_insertion_point".
      Your goal: Find where embedded intelligence can replace manual work.
      """
    And agent actively seeks automation opportunities
    And evidence is tagged with solution potential

  Scenario: Frames filter but also transform evidence
    Given raw evidence "Joel opens dashboard, scans GPUs, documents idle ones"
    When Resource Optimization Frame processes it
    Then evidence is transformed:
      | Raw Evidence | Frame Lens | Transformed Evidence |
      | "opens dashboard" | Where human intervenes | "probe could auto-open dashboard API" |
      | "scans GPUs" | What could be automated | "probe could scan continuously" |
      | "documents idle" | Manual recording | "probe could auto-flag for reclaim" |
    And transformation includes solution pathways
    And evidence retains original quote for traceability

  Scenario: Solution seeds propagate through extraction
    Given Archivist tags evidence with "automation_opportunity: gpu_probe"
    When evidence passes to downstream agents
    Then solution seeds influence:
      | Agent | Traditional Focus | Solution-Seeded Focus |
      | Advocate | "Is evidence strong?" | "Is automation feasible?" |
      | Columbo | "What exactly happens?" | "What probe signals needed?" |
      | Beane | "What's the cost?" | "What's the ROI of automation?" |
    And final insight includes technical solution design
    And sprint story is implementation-ready