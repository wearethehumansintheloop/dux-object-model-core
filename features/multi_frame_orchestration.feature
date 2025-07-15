Feature: Multi-Frame Orchestration Pipeline
  As the orchestration agent
  I want to coordinate multiple frames processing the same evidence
  So that insights benefit from multiple perspectives and converge on solutions

  Background:
    Given Joel's GPU scenario needs analysis from multiple angles
    And each Frame provides a different lens on the same evidence
    And frames process in parallel for efficiency
    And synthesis must merge perspectives coherently

  Scenario: Orchestration agent coordinates parallel frame processing
    Given Joel's GPU monitoring scenario document
    When orchestration begins
    Then parallel frame application:
      | Frame | Processing Thread | Focus |
      | Resource Optimization | Thread-1 | Find automation opportunities |
      | Cost Management | Thread-2 | Calculate financial impact |
      | Developer Experience | Thread-3 | Identify friction points |
      | Platform Intelligence | Thread-4 | Design self-governing systems |
      | Admin Efficiency | Thread-5 | Quantify time savings |
    And all threads process same source document
    And each thread has frame-specific agents
    And threads complete independently

  Scenario: Evidence junction multiplication across frames
    Given Data object "30 minutes checking GPUs daily"
    When processed by 5 frames in parallel
    Then junctions created:
      | Junction Type | Count | Purpose |
      | ProvenanceJunction | 1 | Single source truth (Data + Session) |
      | EvidenceJunction | 5 | One per frame (Data + Frame) |
      | Frame-specific insights | 5 | Different perspectives |
    And same Data object viewed through 5 lenses
    And each lens extracts different value
    And all perspectives traceable to source

  Scenario: Convergence detection during synthesis
    Given 5 frames processed Joel's evidence
    When Insight Architect synthesizes
    Then convergence patterns emerge:
      | Pattern | Frames Agreeing | Convergence Insight |
      | Time waste | Resource, Cost, Admin | "30min/day × 5 admins = major impact" |
      | Automation possible | Resource, Platform, Developer | "Probes can eliminate manual work" |
      | Template solution | Platform, Developer | "Workspace templates as change vehicle" |
    And convergent insights have higher confidence
    And divergent views noted but de-prioritized
    And synthesis narrative emphasizes convergence

  Scenario: Conflict resolution between frames
    Given frames have different priorities
    When evidence conflicts arise
    Then resolution follows:
      | Conflict | Frame A Says | Frame B Says | Resolution |
      | Solution approach | "Build dashboard" | "Embed probes" | Platform Intelligence wins (self-governance) |
      | Priority | "P2 - nice to have" | "P0 - critical" | Cost Management wins ($3.3M impact) |
      | Implementation | "Train users" | "Silent automation" | Developer Experience wins (no training) |
    And resolution rules favor automation over process
    And silent governance beats active enforcement
    And technical solutions beat behavioral change

  Scenario: Multi-frame synthesis creates compound insights
    Given all frames completed processing
    When final synthesis occurs
    Then compound insights emerge:
      | Single Frame Would Say | Multi-Frame Synthesis Says |
      | "GPU monitoring wastes time" | "GPU monitoring waste drives $3.3M opportunity via probe automation" |
      | "Admins need dashboards" | "Embedded probes feed dashboards, eliminating manual checks entirely" |
      | "Resources are underutilized" | "Lifecycle probes enable 15% utilization gain + instant access + cost savings" |
    And compound insights are more actionable
    And solutions address multiple concerns
    And implementation satisfies all frames

  Scenario: Orchestra output for sprint planning
    Given multi-frame synthesis complete
    When generating final DoclingDocuments
    Then each insight shows:
      | Section | Content |
      | Primary Frame | Resource Optimization (automation focus) |
      | Supporting Frames | Cost ($3.3M), Developer (friction), Admin (time) |
      | Convergence Score | 4/5 frames agree on probe solution |
      | Compound Value | Time + Cost + Experience + Governance |
      | Implementation | Single template modification |
      | Risk Assessment | Low - technical not behavioral |
    And sprint planning sees full picture
    And decision-making is evidence-based
    And ROI calculation includes all benefits