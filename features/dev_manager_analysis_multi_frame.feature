Feature: Development Manager Analysis - Multi-Frame Pipeline Requirements
  As the Development Manager Agent
  I want to reverse engineer the extraction pipeline requirements
  So my team can deliver the auto-probe template success story with multi-frame support

  Background:
    Given I reviewed the insight synthesis success scenarios
    And I see we need 5 actionable insights for sprint planning
    And I understand Fit Templates are now called Frames
    And Frames act as magnets attracting relevant evidence
    And Multiple frames can be applied to same evidence

  Scenario: Frame Magnet System Requirements
    Given the fit_template_magnet_system.feature shows magnetic attraction
    When I analyze how Frames work as magnets
    Then Frames must have:
      | Component | Purpose | Example |
      | analysis_questions | Define what evidence to attract | "How much time do admins waste?" |
      | attraction_criteria | Semantic matching rules | "time waste", "manual process", "repetitive" |
      | magnetic_charge | Multi-frame alignment scoring | 3+ frames = highly charged evidence |
      | solution_templates | Point to technical solutions | "auto-probe", "template modification" |
    And highly charged evidence (matching multiple frames) gets priority
    And Frames filter evidence but also seed solution discovery

  Scenario: Multi-Frame Processing Pipeline Architecture
    Given Joel's scenario needs multiple frames for complete analysis
    When I design the multi-frame pipeline
    Then pipeline must support:
      | Frame | Focus | Expected Output |
      | Resource Optimization | GPU utilization | Auto-probe for idle detection |
      | Cost Management | Expense reduction | Cost attribution probes |
      | Developer Experience | Reduce friction | Instant GPU access |
      | Platform Intelligence | Self-governance | Embedded lifecycle management |
      | Operational Efficiency | Admin productivity | Automated monitoring |
    And frames process in parallel not sequence
    And evidence can match multiple frames simultaneously
    And synthesis combines multi-frame perspectives

  Scenario: Frame-to-Agent Generation Flow
    Given each Frame needs specialized agents
    When orchestration agent generates frame-specific agents
    Then generation flow must be:
      | Step | Action | Output |
      | 1 | Read Frame artifact | Extract solution focus |
      | 2 | Call Core API for prompt canvas | Get agent templates |
      | 3 | Inject Frame context | Create frame-specific agents |
      | 4 | Apply to evidence | Extract with solution lens |
      | 5 | Synthesize insights | Actionable sprint stories |
    And agents inherit Frame's solution orientation
    And agents look for automation opportunities not just problems

  Scenario: Evidence Processing with Solution Seeds
    Given Archivist must find solution opportunities
    When processing "30 minutes checking idle GPUs"
    Then evidence extraction includes:
      | Evidence Type | Traditional Extraction | Solution-Oriented Extraction |
      | Time waste | "30 minutes daily" | "30 minutes automatable via probe" |
      | Activity | "checking GPUs" | "checking = probe opportunity" |
      | Target | "idle resources" | "idle = lifecycle management trigger" |
    And Data objects include solution_seeds field
    And Provenance tracks both problem and opportunity

  Scenario: Multi-Frame Synthesis Requirements
    Given multiple frames produced evidence
    When Insight Architect synthesizes
    Then synthesis must:
      | Requirement | Purpose | Implementation |
      | Combine perspectives | Holistic view | Merge evidence from all frames |
      | Resolve conflicts | Consistent narrative | Priority-based resolution |
      | Find convergence | Stronger insights | High-charge evidence emphasized |
      | Generate solutions | Sprint-ready | Technical approach included |
      | Maintain traceability | Governance | Full evidence chain preserved |
    And output points to workspace template modifications
    And no enforcement-based solutions allowed

  Scenario: Pipeline Orchestration for Multi-Frame Success
    Given the complete requirements
    When I plan the implementation
    Then development priorities are:
      | Priority | Component | Deliverable |
      | P0 | Frame magnet system | Frames attract evidence with solution focus |
      | P1 | Multi-frame orchestration | Parallel frame processing with charging |
      | P2 | Solution-oriented agents | Agents find automation opportunities |
      | P3 | Synthesis with convergence | Combine multi-frame insights coherently |
      | P4 | Sprint-ready output | DoclingDocuments with embedded solutions |
    And success metric: 5 insights → 5 sprint stories → 1 template change → $3.3M impact