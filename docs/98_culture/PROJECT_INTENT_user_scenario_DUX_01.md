# Protocol in Action: From Customer Call to Agile Plan

This scenario demonstrates the end-to-end workflow that forms the
foundation of all protocol steps and is the primary engine for
outcome-driven product management—from initial customer insight to
actionable agile delivery.

1.  **Customer Engagement**

    - PM demos a feature in a customer call.

    - Customer voices a specific pain or need (e.g., “We can’t monitor
      all those notebooks running locally”).

2.  **Capture & Extract JTBDs**

    - PM uploads the call transcript to an LLM.

    - The LLM parses and identifies Jobs to Be Done (JTBDs), user
      outcomes, and critical success criteria.

3.  **Review, Select & Refine**

    - PM and team review the AI-suggested JTBDs.

    - They select and refine the ones that matter (e.g., “Gain
      visibility of local notebook GPU usage”), clarify outcomes, and
      fine-tune success criteria.

4.  **Visualize as a Journey**

    - With one click, the system generates a live journey map segmented
      by phase (e.g., Discover Notebooks → Aggregate Metrics → Visualize
      Usage → Enable Actions).

    - PM and team annotate and validate the narrative so it reflects
      real need and aligns the organization for execution.

5.  **Drill Down & Commit**

    - PM zooms in on a journey phase (e.g., "Aggregate Metrics"),
      inspects the specific tasks and actions required, views linked BDD
      specs/scenarios, implementation issue status, blockers, and
      opportunities for asset reuse.

6.  **Agile Plan Generation**

    - The system auto-generates an actionable plan: tasks become epics
      and user stories, BDD specs populate the QA backlog, and the
      journey map snapshot is used in sprint planning and leadership
      reviews.

7.  **Continuous Inspection**

    - PM leverages the live journey dashboard for weekly check-ins,
      drilling down to tasks with lagging BDD specs, issue progress, or
      test coverage, and actively flags blockers for rapid resolution.

**This full-loop, real-world scenario is the foundation for all
subsequent protocol steps and stands as the core workflow for
outcome-driven product management—ensuring every insight rapidly becomes
an aligned, inspectable, and executable plan.**

------------------------------------------------------------------------

# LLM-Driven JTBD Extraction & Live Journey Map Protocol

## Protocol Overview

This protocol defines a comprehensive process for leveraging large
language models (LLMs) to extract actionable Jobs to Be Done (JTBD),
user outcomes, and success criteria from real customer input (e.g.,
transcripts, meeting notes, surveys). The protocol ensures these
elements become the backbone of a live, interactive journey map—serving
as the narrative, collaborative, and operational anchor for all
subsequent protocol, spec, and delivery activity. Journey map
visualization and multi-level drilldown are mandatory: every phase,
task, and action is exposed for real-time inspection, traceability, and
reporting.

------------------------------------------------------------------------

## Phase: Ingest Customer Voice & Extract JTBDs

**Phase Target:**

Transform raw customer interaction data into a prioritized, actionable
set of Jobs to Be Done (JTBDs), user outcomes, and success criteria.

**Key Tasks:**

- Collect customer input (transcript, meeting recording, survey, etc.).

- Process input through LLM to extract:

  - Stated and implied JTBDs

  - Concrete user outcomes

  - Success criteria or business results

- Review and refine LLM outputs for accuracy and relevance.

- Select JTBDs, outcomes, and success criteria for protocolization.

------------------------------------------------------------------------

## Phase: Visualize JTBDs and Outcomes as a Live Journey Map

**Phase Target:**

Establish a living, interactive journey map—the central, always-current
artifact for narrative, drilldown, alignment, and outcome tracking.

### Task 1: Construct a Live, Interactive Journey Map in a Collaborative Tool

- **Action 1.1:** Place user outcomes and JTBDs as nodes within discrete
  journey phases.

- **Action 1.2:** Annotate each phase node with critical success
  criteria and ownership.

- **Action 1.3:** Link each phase node out to all related artifacts:

  - Relevant issues

  - BDD specs (features)

  - Implementation epics

### Task 2: Enable Phase-Level Drilldown

- **Action 2.1:** PM (or any user) can zoom into a specific phase
  directly within the map.

- **Action 2.2:** Within the phase, display all tasks necessary to
  enable the user outcome for that phase.

- **Action 2.3:** For every task at the phase level:

  - Cross-reference to the corresponding BDD Feature and display test
    results (pass/fail)

  - Show implementation issues/Epics or stories and their acceptance
    criteria

  - Display live delivery/test status

### Task 3: Enable Task-Level Drilldown

- **Action 3.1:** For each task, expose the sequence of actions required
  to achieve the specific task goal.

- **Action 3.2:** Cross-reference every action with:

  - The relevant BDD scenario

  - Live test results for each scenario and explicit scenario step
    outcomes

  - Corresponding user story ticket(s)

- **Action 3.3:** Display live progress on each action, scenario, and
  step, including links to user story status and related implementation
  artifacts (PRs, docs, etc.)

### Task 4: Continuous Visualization and Snapshotting

- **Action 4.1:** Permit the journey map to be updated in real-time as
  new JTBDs, outcomes, phases, or tasks emerge, and as items are
  completed or change status.

- **Action 4.2:** Enable export of up-to-date map snapshots for sharing
  in reviews, reporting, and stakeholder demos.

**Mandatory:**

The live journey map (with drilldowns and artifact cross-linking) is
required before protocolization, BDD spec generation, or issue kickoff.
All tracking, cross-team coordination, and leadership/executive roll-ups
rely on this artifact.

------------------------------------------------------------------------

## Phase: Auto-Generate Protocols and Traceable Delivery Artifacts

**Phase Target:**

Instantly generate and cross-link phase-level protocols, detailed tasks,
BDD specs, and delivery issues to the live journey map.

**Key Tasks:**

- For every journey phase, auto-segment by outcome and primary user
  flow.

- For every phase:

  - Attach protocol (task goals, task list, intended flow)

  - Cross-link to all supporting BDD Features and their scenarios

  - Cross-reference generated delivery artifacts:

    - One Epic per main feature/protocol

    - User stories per BDD scenario

    - Acceptance criteria per story

    - Test result/performance status (pass/fail/in progress) exposed and
      inspectable from the journey map

- Maintain bidirectional traceability—from journey map phase to
  implementation and from delivery artifact back to originating
  outcome/JTBD.

------------------------------------------------------------------------

## Protocol in Action: Demo-to-Delivery Visualization Flow

**Scenario:**

- PM demos "Distributed Workloads" to a key customer, who exposes their
  real job: “Monitor GPU usage across all locally running notebooks.”

- PM uploads call transcript to LLM extraction tool.

- LLM outputs JTBD: “Monitor GPU/compute for all notebook sessions—local
  and remote.”

- User outcome generated: “Admins see and act on GPU bottlenecks in real
  time.”

- PM reviews, selects outcome, refines success metric with customer’s
  criteria (“Reduce detection time for GPU shortages to \<2 minutes”).

**System Automatically Generates & Visualizes:**

- **A Live Journey Map**

  - Phases: Discover Sessions → Collect Metrics → Visualize Usage →
    Alert & Act

  - Each phase node links to critical outcome, success criteria, and
    ownership

  - Phase nodes interlink with BDD Features (e.g., “Dashboard shows all
    sessions”), related issues (Epics), and implementation status

- **Drilldown**

  - PM zooms into “Visualize Usage” phase: sees tasks like “Aggregate
    usage data,” “Render sessions in dashboard,” “Annotate local vs
    remote”

  - Each task links to its Feature, BDD scenario status, and user
    stories

  - For any task (e.g., “Show real-time metrics”), the PM drills to
    action steps: “Collect metric stream,” “Display trend,” “Alert when
    high”

  - Each action shows cross-linked scenario, step result status, user
    story, and acceptance criteria; live test results are visible

- **Continuous Update**

  - Map updates as new JTBDs, success criteria, or implementation
    changes occur.

  - PM exports a snapshot or presents live in reviews—using it to
    narrate what’s needed, what’s built, and where value/gaps/blocks
    remain.

------------------------------------------------------------------------

## Journey Map Intake, Review, and Cross-Referencing Guidelines

**Review Requirements:**

- PM/team must validate:

  - All JTBDs, user outcomes, and criteria are placed in the live
    journey map

  - Each journey phase is discrete, intuitively named, and contains no
    overlap

  - Every phase maps to its outcomes, tasks, success criteria, and
    ownership

  - Drilldown is enabled from phase → task → action, with every item
    cross-linked to BDD specs, test results (pass/fail and scenario step
    status), user stories/acceptance criteria, and implementation
    tickets/artifacts

- Confirm that all protocols/BDDs/issues originate from the live journey
  map nodes

- Review is required before moving to sprint planning, design, or
  delivery

------------------------------------------------------------------------

## Protocol Validation Checklist

- Raw customer input captured and run through LLM extraction

- JTBDs, user outcomes, and criteria are reviewed, selected, and refined

- Live, interactive journey map is constructed in a collaborative tool

- All phase nodes annotated with outcome, criteria, and owner

- Cross-linking from phase node to issues, BDD specs, and implementation
  tickets is complete

- Drilldown and artifact cross-referencing working at both phase and
  task level

- Task/action drilldown exposes all user stories, scenarios, step
  results, and current status/progress

- Continuous map updating enabled; snapshot/export configured for
  reviews

- All downstream work gated on journey map artifact review and signoff

------------------------------------------------------------------------

## Dashboard Mockup & Artifact Navigation

**Core Features:**

- **Interactive Journey Map View:**

  - Phases spatially organized (columns or swimlanes)

  - Nodes representing user outcomes and JTBDs

  - Clickable drilldown: phase → task → action sequence

- **For each Phase Node:**

  - JTBD, outcome, and success criteria visible

  - Ownership and status

  - Linked Epics, BDD Features, top-level acceptance result

- **Within Phase Drilldown:**

  - List of all enabling tasks

  - Each task: links to BDD Feature, Epic, scenario test status,
    acceptance criteria, and latest implementation/test progress

- **Within Task Drilldown:**

  - List of sub-actions

  - Each action: BDD scenario, step result (assertion outcome), user
    story, direct link to test run or PR/status artifact

  - Live progress indicator (in progress, complete, blocked, failing,
    needs review)

- **Global Actions:**

  - Update nodes/phases/tasks as new requirements emerge or items are
    delivered

  - Export snapshot (PDF/image/interactive HTML) for reporting or
    exec/partner review

------------------------------------------------------------------------

**Mandatory:**

The live journey map is the operational and reporting source of truth,
required for kickoff, tracking, and demonstration of outcome delivery.
All teams and executives use it for ongoing alignment, inspection, and
strategic prioritization.

------------------------------------------------------------------------
