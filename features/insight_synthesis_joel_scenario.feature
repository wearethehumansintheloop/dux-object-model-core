Feature: Insight Synthesis Drives Sprint Planning for Silent Governance
  As a product team using DUX insights
  I want insights that drive technical solutions through silent governance
  So that behavior changes naturally without enforcement or scolding

  Background:
    Given Joel wastes 30 minutes daily checking GPU utilization manually
    And the team wants to change behavior through workspace templates not rules
    And silent governance means embedding good practices invisibly
    And insights must point to technical solutions not just problems

  Scenario: SUCCESS - Auto-probing templates solve Joel's problem silently
    Given the team received insights about GPU monitoring inefficiency
    When they implement sprint stories based on these insights
    Then workspace templates include auto-probing for GPU idle detection
    And probes report to control plane automatically every 5 minutes
    And idle GPUs are reclaimed based on experiment status not arbitrary timeouts
    And Joel never needs to check GPU status manually again
    And developers stop hoarding GPUs because lifecycle is managed for them
    And the platform dashboard shows real-time utilization without manual updates across local and shared resources 
    And behavior changed to enable design for horizontal scale and optimization mindsets

  Scenario: Insights structured for sprint planning action
    Given the extraction pipeline produced 5 insights
    When the team reviews them for sprint planning
    Then each insight contains:
      | Insight Focus | Problem | Solution Path | Sprint Story |
      | GPU Monitoring | 30min daily manual checks | Auto-probe templates | "As Joel, I want notebooks to auto-report GPU usage" |
      | Access Delays | Waiting for GPU allocation | Smart scheduling probe | "As Bella, I want immediate GPU when available" |
      | Visibility Gaps | No real-time dashboards | Probe aggregation API | "As Joel, I want live GPU utilization view" |
      | Resource Hoarding | GPUs kept "just in case" | Idle reclaim probe | "As platform, I want automatic GPU recycling" |
      | Cost Opacity | Unknown GPU burn rate | Cost tracking probe | "As finance, I want per-project GPU costs" |
    And each solution leverages workspace template modifications
    And no solution requires user behavior enforcement

  Scenario: Insight must point to auto-probe solution
    Given agents extracted "Joel spends 30min daily on manual GPU checks"
    When Insight Architect synthesizes the complete insight
    Then the insight structure includes:
      | Field | Content |
      | problem.job_statement | "When monitoring GPU resources, I want automated visibility, so I can reclaim time" |
      | behavior.signals | ["open_dashboard", "manual_scan", "document_idle", "repeat_daily"] |
      | result.metrics | ["time_saved: 30min/day", "cost_saved: $375/day"] |
      | solution_pathway | "Embed auto-probing in workspace templates to eliminate manual checks" |
      | technical_approach | "Notebook kernels report GPU metrics to control plane via lightweight probe" |
    And the insight explicitly connects problem to template-based solution
    And the solution requires zero behavior change from Joel

  Scenario: Archivist discovers probe opportunity (Inner Monologue)
    Given Archivist is processing Joel's "checking which GPUs are sitting idle" quote
    When Archivist's inner monologue begins
    Then "Wait... he's checking if they're IDLE? That's automatable!"
    And "If notebooks could self-report their GPU usage..."
    And "Oh! This isn't about dashboards, it's about embedded intelligence"
    And "Advocate will love this - technical solution, not process change"
    And Archivist tags evidence: "automation_opportunity: embedded_probe"
    And creates Data object with solution seeds not just problem documentation

  Scenario: Advocate evaluates template solution viability (Engineering Manager Mode)
    Given Advocate receives probe automation evidence from Archivist
    When Advocate's engineering assessment begins
    Then "Embedded probes in templates? That's platform thinking..."
    And "No user training required - it just works. Perfect."
    And "Risk: probe overhead? Minimal if designed right"
    And "This solves 5 problems with one template change"
    And Advocate approves: "Template-based probe is the way"
    And pitches to Columbo: "Detail the exact monitoring workflow to automate"

  Scenario: Columbo designs probe behavior (UX Designer Mode)  
    Given Columbo receives probe automation opportunity
    When Columbo's detail design begins
    Then "Probe must be invisible to users - no popups or alerts"
    And "Check GPU every 5min: utilization%, memory%, active processes"
    And "If idle >15min AND no jupyter cells running: flag for reclaim"
    And "Auto-save work before any reclaim action"
    And Columbo creates Behavior: "workspace.probe.gpu.lifecycle"
    And Behavior includes signals: ["gpu.check", "idle.detect", "safe.reclaim"]

  Scenario: Beane calculates platform-wide impact (Revenue Focus)
    Given Beane receives probe automation proposal
    When Beane's platform ROI calculation begins
    Then "5 admins × 30min/day × $150/hr = $1,875/day saved"
    And "GPU utilization increase 15% = $72K/month in avoided purchases"
    And "Developer productivity from instant GPU access = $200K/month"
    And "One template change yields $3.3M annual impact"
    And Beane creates Result: "platform.efficiency.gain.$3.3M.annual"
    And Result includes metrics: ["gpu.utilization.rate", "admin.time.saved", "developer.wait.reduced"]

  Scenario: Insight Architect weaves solution-focused narrative
    Given all agents discovered probe automation opportunity
    When Insight Architect synthesizes complete insight
    Then "This isn't just about time waste - it's about platform intelligence"
    And creates Insight_001: "Embed GPU lifecycle management in workspace templates"
    And narrative structure:
      | Section | Content |
      | Problem Story | "Joel and 4 other admins waste 2.5hr/week on manual GPU monitoring" |
      | Root Cause | "Notebooks don't self-report their resource usage to platform" |
      | Solution Design | "Lightweight probes in workspace templates auto-report every 5min" |
      | Behavior Impact | "Admins never check manually; devs can't hoard; platform auto-reclaims" |
      | Platform Value | "$3.3M annual impact from one template enhancement" |
    And packages as DoclingDocument with embedded schemas and agent rationale

  Scenario: Complete insight with solution traceability
    Given Insight_001 "GPU lifecycle probe" is assembled
    When generating the final DoclingDocument
    Then document structure includes:
      | Component | Purpose | Traceability |
      | Problem with job_statement | Define need for automation | Joel's quote → Data_001 → Session_001 |
      | Behavior with probe signals | Detail monitoring to automate | Columbo design → gpu.check signal |
      | Result with platform metrics | Quantify $3.3M impact | Beane calculation → ROI evidence |
      | UserFlow | Current manual workflow | Login → check → document → repeat |
      | UserOutcome | Automated efficiency | No manual checks → 15% utilization gain |
      | Solution Pathway | Template probe design | Technical approach with zero training |
    And agent decision logs show how probe solution emerged
    And evidence chain proves ROI calculation

  Scenario: Five insights create complete sprint backlog
    Given extraction pipeline processed all Joel scenarios
    When all 5 insights are synthesized
    Then insights form coherent sprint plan:
      | Priority | Insight | Sprint Story | Silent Governance Method |
      | P0 | GPU Lifecycle Probe | Embed auto-reporting in notebooks | Templates handle lifecycle |
      | P1 | Smart GPU Queue | Priority access for active research | Templates pre-allocate resources |
      | P2 | Real-time Dashboard | Aggregate probe data to control plane | Probes feed live metrics |
      | P3 | Cost Attribution | Track GPU costs per project | Probes tag usage to projects |
      | P4 | Idle Reclamation | Auto-reclaim after experiment ends | Probes detect completion |
    And every story uses workspace templates as change vehicle
    And zero stories require user behavior modification
    And platform becomes self-governing through embedded intelligence