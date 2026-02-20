# HITL Feature Template (v9.6.1)

## Purpose

A `.feature` file is the **PR-ready composition** of the HITL object graph. It assembles a Flow, its Behaviors, the Problem it solves, the Result it targets, the UserOutcome junction, and all supporting Evidence into a single file that serves as:

1. **The issue** — tracked in GitHub, Linear, and/or Jira
2. **The PR body** — the feature file IS the pull request content
3. **The spec** — executable BDD scenarios written in user enablement language
4. **The audit trail** — every claim links to evidence, every behavior links to a result

## "What would you say... you do here?"

> When I need to deliver a feature with full traceability from research evidence through implementation to business result, I want a single file that carries the complete object graph, so that my PR is my issue is my spec is my audit trail.

## Object Graph Carried by a Feature File

```
.feature file (the PR)
├── UserFlow         — sequences behaviors from problem to outcome
│   ├── Problem      — the JTBD this flow solves
│   ├── Behavior[]   — each scenario (user enablement steps)
│   ├── UserOutcome  — junction: behavior + result
│   │   └── Result   — the lagging business metric
│   └── Evidence[]   — research backing every claim
└── issue_tracking   — GitHub / Linear / Jira references
```

## Template

```gherkin
# yaml-front-matter
# ---
# object_type: UserFlow
# user_flow_id: flow-{descriptive-slug}
# title: "{User Journey Title}"
# description: "{Who} {does what} {with what outcome}"
# problem_id: problem-{descriptive-slug}
# behavior_sequence:
#   - behavior-{step-1-slug}
#   - behavior-{step-2-slug}
#   - behavior-{step-n-slug}
# evidence:
#   - EV-{evidence-id-1}
#   - EV-{evidence-id-2}
# tags: [{domain-tags}]
#
# issue_tracking:
#   # This feature file IS the issue. These IDs link bidirectionally:
#   # .feature file <-> issue tracker <-> PR <-> commit
#   # Each Scenario (Behavior object) can be a sub-task of this issue.
#   github:
#     issue: null          # e.g., repo-name#42
#     pr: null             # e.g., repo-name#43
#     branch: null         # e.g., feature/flow-{slug}
#   linear:
#     issue_id: null       # e.g., PROJ-127
#     project: null        # e.g., Project Name
#     cycle: null          # e.g., 2026-Q1 Sprint 3
#     status: backlog      # backlog | todo | in_progress | in_review | done
#   jira:
#     issue_key: null      # e.g., PROJ-456
#     project_key: null    # e.g., PROJ
#     epic_link: null      # e.g., PROJ-100
#     sprint: null         # e.g., Sprint 2026.Q1.3
#     status: null         # e.g., To Do
# ---
#
# object_type: Problem
# problem_id: problem-{descriptive-slug}
# job_statement: "When {situation}, I want {motivation}, so I can {outcome}."
# what_is_at_stake: "{What users lose or risk if unsolved}"
# opportunity_score: "Importance: {N} + max({N} - {N}, 0) = {score}"
# evidence:
#   - EV-{evidence-id}
# end_user: [{Persona} - {Role}]
# ---
#
# object_type: Result
# result_id: result-{descriptive-slug}
# target_impact: "{Measurable business impact statement}"
# success_criteria: "{Aggregate threshold for success}"
# success_metrics: [{metric_1}, {metric_2}]
# evidence:
#   - EV-{evidence-id}
# ---
#
# object_type: UserOutcome
# user_outcome_id: outcome-{descriptive-slug}
# behavior_id: {final-behavior-in-sequence}
# result_id: result-{descriptive-slug}
# end_user: "{Persona} - {Role}"
# user_flow_id: flow-{descriptive-slug}
# key_signals: [{inherited from behavior signals across the flow}]
# acceptance_criteria:
#   - "{Testable criterion 1}"
#   - "{Testable criterion 2}"
# outcome_statement: "{Who}, the {role}, is able to {action} by {degree of change} — {business context}."
# evidence:
#   - EV-{evidence-id}
# ---

Feature: {User Journey Title}
  As {Persona}, a {role} at {org}
  When {situation from Problem job_statement}
  I want {motivation from Problem job_statement}
  So {outcome from Problem job_statement}

  # User Enablement Chain (when we deliver our solution...):
  #
  #   {Persona} is able to {behavior 1 user_enablement}.
  #   {Persona} then {behavior 2 user_enablement}.
  #   {Persona} then {behavior N user_enablement}.

  Background:
    Given {shared precondition for all scenarios}

  # object_type: Behavior
  # behavior_id: behavior-{step-1-slug}
  # user_enablement: "{Persona} is able to {task/action}"
  # result_id: result-{descriptive-slug}
  # user_flow_id: flow-{descriptive-slug}
  # end_user: "{Persona} - {Role}"
  # signals: [{signal_1}, {signal_2}]
  # evidence: [EV-{evidence-id}]
  # tags: [{domain-tag}, gh:null, linear:null, jira:null]

  @{domain-tag}
  Scenario: {Persona} is able to {task/action}
    Given {user context — what they need}
    When {user action — what they do}
    Then {observable outcome — what they experience}
    And {measurable criterion — how we know it worked}

  # ... repeat Behavior block for each scenario in the flow ...
```

## Template Rules

### Scenario Names = User Enablement Statements

Every scenario name MUST follow the Behavior object `user_enablement` format:

```
{Persona} is able to {specific task/action}
```

The scenario name IS the `user_enablement` field. They are the same string.

### User Enablement Chain = Flow Narrative

The comment block under the Feature description reads as a narrative:

```
# {Persona} is able to {first thing}.
# {Persona} then {second thing}.
# {Other persona} is able to {their thing}.
# {Persona} then {final thing}.
```

This chain maps 1:1 to `behavior_sequence` in the Flow object.

### Tags = Issue Tracking Join Keys

The `tags` field on each Behavior uses namespace prefixes for tracker references:

| Prefix | Tracker | Example |
|--------|---------|---------|
| `gh:` | GitHub | `gh:discrete-connection#42` |
| `linear:` | Linear | `linear:DC-127` |
| `jira:` | Jira | `jira:BISCUIT-456` |

This enables queries like:
- "Show me all Behaviors in Jira epic `BISCUIT-100`"
- "What shipped in Linear cycle `2026-Q1-Sprint-3`?"
- "What's in GitHub PR `discrete-connection#43`?"

Because every Behavior references a `result_id`, you can roll up from tracker issue -> Behavior -> Result to answer: "Is this epic actually moving the business metric?"

### Implementation Details Live in Step Files, Not Feature Files

The `.feature` file describes **what the user does and experiences**. The step definition file (`features/steps/*.py`) is where implementation details live — API calls, SVID transactions, database queries, infrastructure mechanics.

```
.feature file    →  "Bella is able to query the fraud database without handling credentials"
step file        →  service account presents SVID to Vault, Vault verifies against SPIRE trust bundle...
```

### Front Matter = Complete Object Graph

The yaml front matter above the `Feature:` keyword contains the full HITL object graph:

| Section | Object Type | What It Provides |
|---------|-------------|------------------|
| First block | UserFlow | Sequences behaviors, links to problem |
| `issue_tracking` | (meta) | GitHub / Linear / Jira bidirectional references |
| Second block | Problem | JTBD, what's at stake, opportunity score |
| Third block | Result | Target impact, success criteria, metrics |
| Fourth block | UserOutcome | Junction: behavior + result, outcome statement |

Each Scenario carries its own Behavior object metadata as a comment block above it.

## Linter Validation Rules

A feature file linter should validate:

### Structure
- [ ] yaml front matter contains UserFlow with valid `behavior_sequence`
- [ ] Problem block has `job_statement`, `what_is_at_stake`, `evidence`
- [ ] Result block has `target_impact`, `success_criteria`, `evidence`
- [ ] UserOutcome block has `behavior_id`, `result_id`, `outcome_statement`, `acceptance_criteria`
- [ ] `behavior_sequence` order matches actual Scenario order in file

### Scenarios (Behavior Objects)
- [ ] Every Scenario name follows `{Persona} is able to {task}` pattern
- [ ] Every Scenario has a Behavior comment block with `behavior_id`, `user_enablement`, `signals`, `evidence`
- [ ] `user_enablement` matches the Scenario name
- [ ] At least one signal per Behavior (observable from 3000 miles away)
- [ ] All evidence IDs resolve to real Evidence objects

### Issue Tracking
- [ ] At least one tracker has a non-null issue ID before PR merges
- [ ] PR field populated before status moves to `in_review`
- [ ] Branch name matches `flow_id` pattern
- [ ] Each Behavior's tags reference the parent issue

### Quality (4-Layer Pizza)
- [ ] Functional: every Scenario has `Then` steps (assertions)
- [ ] Reliable: measurable criteria present (`<N seconds`, `>N% success`)
- [ ] Usable: domain language, realistic names, no technical jargon in Scenario names
- [ ] Delightful: maps to JTBD, outcome statement present

## Relationship to HITL Repo Structure Standard

This template aligns with the [HITL Repo Structure Standard](https://github.com/wearethehumansintheloop/hitl-core/blob/main/governance/repo-structure-standard.md), which defines the canonical architecture using a Helm/Kubernetes analogy.

### The Helm Analogy

| Helm/K8s | HITL Location | HITL Feature Template |
|---|---|---|
| **CRD** | `hitl-core/governance/object_definitions/` (git) | Same — object definitions are schema authority |
| **etcd** | **Neo4j graph database** | Instances extracted from `.feature` front matter live here at runtime |
| **values.yaml** | Instances queried from Neo4j via API | `# object_type:` blocks in front matter (seed data / authoring format) |
| **Chart** | `hitl/charts/*/feature.feature` (product repos) | The `Feature:` + `Scenario:` gherkin |
| **Chart.md** | `hitl/charts/*/Chart.md` | yaml front matter in the `.feature` file |
| **`helm install`** | `behave` | `behave` (unchanged — the renderer) |
| **Tiller/Operator** | ARB agents (case, hugh, sophia, chaya, jorge) | Schema creation + continuous monitoring |

### Two Directions, One Architecture

The `.feature` file and the Neo4j graph are two representations of the same object graph. Data flows in two directions depending on the lifecycle phase:

```
DIRECTION 1 — AUTHORING (human writes, pipeline extracts)

  Human writes .feature file (natural language first)
       ↓
  PR review (the .feature IS the PR)
       ↓
  Merge to main
       ↓
  Extraction pipeline parses front matter + behavior comments
       ↓
  Neo4j graph (instances loaded as nodes + relationships)
       ↓
  Dashboard, cross-project queries, aggregation

DIRECTION 2 — STEADY STATE (graph generates, human validates)

  Neo4j graph (source of truth for instances)
       ↓
  Generation pipeline renders instances into .feature files
       ↓
  hitl/charts/*/feature.feature (in product repos)
       ↓
  behave runs it → pass/fail
```

**This template serves Direction 1** — the authoring phase. Humans write `.feature` files with the full object graph inlined as front matter. The extraction pipeline loads these into Neo4j. After that, the graph is the source of truth.

The `.md` instance files that seed the graph (and the front matter in `.feature` files) become **historical records** — like database migration files. They document what was authored and when, but the graph is what gets queried at runtime.

### PII and Local-First Runtime

Object instances frequently contain PII — real user names, real personas, real research quotes, real behavioral data. This means the entire pipeline must run locally with zero cloud dependency:

```
LOCAL RUNTIME STACK

  Llama (via Ollama)          ← local inference for extraction + ARB agents
       ↓
  Neo4j (local instance)      ← graph database, instances never leave machine
       ↓
  behave (local execution)    ← test runner, reads from local graph
       ↓
  .feature files (git)        ← committed artifacts (PII-scrubbed or private repo)
```

**What this means for the architecture:**

| Component | Cloud Option | Local Option (PII) |
|---|---|---|
| Extraction pipeline | Claude API | Llama via Ollama |
| ARB agents | Claude API | Llama via Ollama |
| Graph database | Neo4j Aura | Neo4j Community (local) |
| Test execution | CI/CD | `behave` (local) |
| Instance storage | Cloud Neo4j | Local Neo4j only |

The local-first workflow is not just a bootstrap phase — it is the **permanent operating mode** for any product where instances contain PII. The seed data `.md` files, the `.feature` front matter, and the local Neo4j graph all stay on the machine. Git receives the `.feature` files (which may themselves contain PII and require private repos), but the graph never syncs to cloud.

This also means the `.feature` file as authoring surface (Direction 1) is not a transitional pattern. For PII workloads, humans always author locally, extract locally, and the local graph is the runtime. Direction 2 (graph generates `.feature` files) also happens locally — Llama + local Neo4j + local `behave`.

### Why Natural Language First?

The `.feature` file is the natural unit of human communication:

- PRs contain user enablement narratives, not YAML diffs
- Reviewers read "Bella is able to...", not schema-compliant objects
- The thing humans care about (the user flow) reads top-to-bottom as a story

The graph is the natural unit of machine querying. Each serves its audience.

For PII workloads, "natural language first" also means **human-readable first** — the `.feature` file is auditable by the humans whose data it contains. A graph node is not.

### Where the Template Fits in the Org

```
wearethehumansintheloop/                    ← org repo
├── hitl-core/                              ← kernel (submodule)
│   └── governance/
│       ├── object_definitions/             ← CRDs (what types CAN exist)
│       ├── repo-structure-standard.md      ← architecture spec
│       └── instances/                      ← seed data (historical)
│
├── hitl-agents/                            ← ARB agents (schema authority)
│   └── ARB creates Neo4j schema from object_definitions/
│       loads seed data from instances/ (one-time)
│       signal-archaeology monitors continuously
│
└── my-product/                             ← product repo (submodule)
    ├── hitl/charts/                        ← .feature files (generated from graph)
    │   └── bella-gets-config-fix/
    │       ├── Chart.md                    ← which instances compose this chart
    │       └── feature.feature             ← executable spec
    ├── hitl/fixtures/                      ← domain test data (local)
    └── steps/                              ← step definitions (the renderer)
```

### How `behave` Works as `helm install`

Step definitions are the renderer. They query Neo4j for HITL instances (problems, behaviors) to know WHAT to test and load local fixtures (workspaces, service-accounts) to know HOW to test it.

```python
# This step reads from local fixtures
@given('Bella has a workspace template for fraud analysis')
def step_impl(context):
    context.workspace = load_fixture('hitl/fixtures/workspaces/bellas-fraud-workspace.md')

# This step validates against instance data from Neo4j
@then('Bella can start fraud analysis same-day')
def step_impl(context):
    behavior = hitl_api.get_instance('BEH-001', product='discrete_connection')
    assert context.provisioning_time < behavior['measurable_criteria']['time_limit']
```

### Extraction Pipeline Responsibilities

The extraction pipeline (runs on merge to main) must:

1. **Parse front matter** — extract Flow, Problem, Result, UserOutcome objects
2. **Parse behavior comments** — extract Behavior objects from each Scenario block
3. **Validate schema compliance** — each extracted object must match its definition in `hitl-core/governance/object_definitions/`
4. **Load into Neo4j** — create/update graph nodes and relationships
5. **Update Chart.md** — regenerate from the Flow's `behavior_sequence` and references
6. **Detect drift** — if graph was manually edited, flag for reconciliation (`.feature` is the authoring source)

## Canonical Example

See: `biscuits/features/biscuits.features/bella_gets_config_fix_from_collaborator.feature`

This feature file demonstrates the full template with:
- 1 UserFlow (6 behaviors sequenced)
- 1 Problem (collaboration identity blur)
- 1 Result (time-to-fix from days to <1 hour)
- 1 UserOutcome (Bella gets fix deployed with full audit trail)
- 6 Behaviors (each a Scenario with user enablement name)
- Issue tracking placeholders for GitHub, Linear, Jira
- Evidence references throughout

## How to Push to Any Project

### Option 1: Copy the template file

```bash
# Copy to any project's features/ directory
cp hitl_feature_template.md /path/to/project/features/FEATURE_TEMPLATE.md
```

### Option 2: Reference from dux-object-model-core (recommended)

Projects that use the HITL object model should reference this template from the canonical vault:

```
dux-object-model-core/docs/100_START_HERE/hitl_feature_template.md
```

The CLAUDE.md in each project can reference this template:

```markdown
## Feature File Standard
Feature files follow the HITL Feature Template from dux-object-model-core.
See: dux-object-model-core/docs/100_START_HERE/hitl_feature_template.md
```

### Option 3: Scaffold via skill (future)

A `/new-feature` skill could scaffold a new feature file from this template, prompting for:
1. Flow title and description
2. Problem job statement
3. Result target impact
4. Behavior enablement chain (user walks through the flow)
5. Issue tracker IDs

The skill would generate the complete `.feature` file with all object blocks pre-populated.
