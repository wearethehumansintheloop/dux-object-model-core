# 📘 DUX Object Model Guide — Version 9.5

## 🚀 For Collaborators: Automated CI/CD Pipeline

> **⚠️ IMPORTANT: This guide is monitored by an automated CI/CD pipeline!**

When you edit this guide, the pipeline automatically:
- ✅ Validates your changes against the DUX v9.5 schema
- ✅ Regenerates all prompt templates (standard, NotebookLM, hybrid)
- ✅ Updates test data and validation suites
- ✅ Runs comprehensive BDD and pytest validation
- ✅ Commits changes and packages artifacts for distribution

### Quick Commands for Collaborators:

```bash
# Watch for guide changes (auto-runs pipeline)
python scripts/ci_pipeline.py --watch

# Run pipeline manually after edits
python scripts/ci_pipeline.py --manual

# Setup CI/CD environment (first time)
./scripts/setup_ci.sh
```

### 🤝 Human-in-the-Loop (HITL) Collaboration

**NEW:** For collaborative workflows instead of blind automation:

```bash
# Start HITL file watcher for collaborative workflows
python scripts/hitl_watcher.py --start

# Drop files in watch_folders/hitl_review/ to trigger AI analysis
# Drop completed responses in watch_folders/hitl_feedback/ for processing
```

**📁 HITL Folders:** Drop files for collaborative review instead of automatic processing
- `watch_folders/hitl_review/` → AI analyzes & creates review prompts  
- `watch_folders/hitl_feedback/` → AI processes your feedback & suggests next steps

**📋 See full pipeline details:** [CI/CD README](../CI_CD_README.md)

---

## Table of Contents

1. Overview: What Changed in 9.5
2. The DUX Object Set (v9.5)
   - Problem
   - Behavior
   - Result
   - Flow (junction object)
   - UserOutcome (junction object)
3. Structural Rules
   - Signal Linkage
   - Evidence Annotations
   - Scoping Work from Junctions
4. Object Definitions
   - [Problem](#problem)
   - [Behavior](#behavior)
   - [Result](#result)
   - [Flow](#flow)
   - [UserOutcome](#useroutcome)
5. Migration Notes (v9.4 → v9.5)
6. Governance Philosophy: The Bobs Protocol
7. Future Roadmap (v9.6 Preview)

---

## 1. Overview: What Changed in 9.5

> "We're not here to fill fields. We're here to produce results." — The Bobs

- ✅ Added `UserOutcome`: a measurable, testable junction object representing Behavior × Result.
- ♻️ Replaced `Journey` with `Flow`: now represents Problem × UserOutcome, orchestrating behavior paths.
- ❌ Removed `Issue`: now captured as annotations or external implementation links.
- 🎯 Improved signal linkage: explicit tracking of derived signals, behavior outcomes, and measurement traceability.

---

## 2. The DUX Object Set (v9.5)

| Object        | Purpose                                        | Notes                                     |
| ------------- | ---------------------------------------------- | ----------------------------------------- |
| `Problem`     | Strategic JTBD expression                      | Must include opportunity score            |
| `Behavior`    | Testable user actions with acceptance criteria | Overloaded in v9.5; may decompose in v9.6 |
| `Result`      | Observable system outcomes                     | Derived from Behavior                     |
| `Flow`        | Junction: maps Problem × UserOutcome           | Formerly Journey                          |
| `UserOutcome` | Junction: represents Behavior × Result         | New in v9.5, OKR-compliant                |

---

## 3. Structural Rules

- **Signal linkage is mandatory**: Results and UserOutcomes must point to key signals, not vibes.
- **Junction parentage is explicit**:
  - `UserOutcome = Behavior × Result` (with unique field: `degree_of_signal_change`)
  - `Flow = Problem × UserOutcome` (with unique field: `behavior_sequence`)
- **Annotations replace Issues**: Missing data, assumptions, or junction logic should be captured inline.
- **Flows must define behavior sequences and include known user friction (pain\_points).**

### 🔍 Evidence Requirements (Applies to All Objects)

Every object must include traceable, human-substantiated evidence to support its validity. The required fields are:

- `evidence` (array of objects), each entry must include:
  - `quote`: Verbatim insight or observation
  - `citation`: Source reference (participant ID, timestamp, or slide/report reference)
  - `provenance`:
    - Interviews: `timestamp_in`, `timestamp_out`
    - Reports: `report_slide`, `report_date`
  - `evidence_type`: One of `["qualitative", "quantitative", "system_log", "user_interview", "report_summary"]`
  - `collection_method`: One of `["interview", "survey"]`
  - `confidence_level`: One of `["high", "medium", "low"]`

- `evidence_status` (string):
  - `evidence_backed`: 2+ items, including 1+ quantitative
  - `evidence_present`: 1+ items, may lack quant
  - `assumptive`: no strong evidence; speculative or phase 0

Objects without a valid `evidence` block must include a compliant `annotation`.

---

## 4. Object Definitions

### Problem

*Represents a job to be done (JTBD) worth solving, backed by evidence.*

- Attributes: `id`, `description`, `what_is_at_stake`, `end_user`, `opportunity_score`, `evidence`, `flow_ids`, `result_ids`, `evidence_teaser`, `tags`
- Must use JTBD format: “When [situation], I want to [motivation], so I can [expected outcome]”

### Behavior

*A discrete, observable action that can be tested, tracked, and taught.*

> **When I need to validate how users engage with a product or system, I want to define observable behaviors so I can drive testable, teachable outcomes.** — Behavior JTBD

- Attributes: `id`, `description`, `behavior_type`, `flow_ids`, `acceptance_criteria`, `signals`, `evidence`, `tags`
- Can be linked to multiple flows, but must not exist in isolation
- Overloaded: may split into `Task` and `Action` objects in v9.6

### Result

*An organizational target used to evaluate the health of the organziation that is advanced indicrectly through the delivery of user outcomes meeting success criteria thresholds.*

> **When I need to confirm that our intervention created impact, I want to evalute our progress toward the target success criteria by quantifying successful user outcomes as success metrics that map to the criteria.** — Result JTBD

- Attributes: `id`, `description`, `end_user`, `source_behavior_ids`, `key_signals`, `success_criteria`, `outcome_metrics`, `evidence`, `tags`
- May be derived from one or more Behavior signals

### Flow

*A junction object mapping Problem × UserOutcome, via an ordered sequence of Behaviors.*

> **When I need to communicate how our target customer expects to realize value, I want to demonstrate their preferred and expected golden path so I can accelerate our sprint velocity and reduce lead time.** — Flow JTBD

- Attributes: `id`, `title`, `user_scenario`, `flow_type`, `linked_problem_ids`, `linked_user_outcome_ids`, `behavior_sequence`, `painpoints`, `protocol_url`, `pain_points`, `end_user`, `evidence`, `tags`
- Unique traits: `behavior_sequence`, `painpoints`, `end_user`

**New Attribute: `painpoints`**
- Array of pain point objects, each with:
  - `pain_point`: string (description of the pain point)
  - `impacted_behaviors`: array of Behavior IDs (strings) impacted by this pain point
- Purpose: Explicitly map user/system friction points to the specific behaviors in the flow they impact, making it easy to trace, prioritize, and address pain points in context.

**Canonical Example:**
```json
"painpoints": [
  {
    "pain_point": "Users are confused by the workspace resource selection step.",
    "impacted_behaviors": ["behavior_001", "behavior_003"]
  },
  {
    "pain_point": "Bulk update actions are slow for admins.",
    "impacted_behaviors": ["behavior_005"]
  }
]
```

### UserOutcome

*A junction object combining Behavior × Result to represent measurable user value.*

> “Who does what by how much to make progress toward our target result.” — Core Definition

- 🧑 **Who** = `user_scenario`
- ⚙️ **Does what** = Behavior(s) linked through flows that produce signal change
- 📈 **By how much** = Change in `key_signals`, measured by `success_criteria` and `target_metrics`
- 🎯 **Toward what** = Linked `Result` object (representing target outcome)

This framing helps anchor UserOutcome in both human action and quantifiable value shifts.

- Attributes:
  - `id`
  - `user_scenario` (🧑 Who)
  - `outcome_statement` (🎯 What)
  - `success_criteria` + `target_metrics` (📏 By how much)
  - `key_signals`, `signal_source`, `target_impact_when_achieved`
  - `priority`, `related_problem_ids`, `related_result_ids`, `related_flow_ids`, `evidence`, `tags`
- Unique traits: `signal_source`, `key_signals`, `success_criteria`, `target_metrics`
- Think of it as a quantifiable OKR derived from user experience, not system success alone

---

## 5. New Hires & Retirements

### 👋 Welcome to the Team (New Hires)

#### **UserOutcome** → *Behavior × Result*

- Hired to track **what users do differently** that signals value.
- Brings OKR-compliant traceability to outcomes.
- Anchors our measurement strategy.

#### **Flow** → *Problem × UserOutcome*

- Formerly "Journey," now focused on **golden paths** and **pain point orchestration**.
- Behavior sequences, friction visibility, and evidence-backed.

### 🙏 Thank You for Your Service (Retired)

#### **Journey** → ✨ Replaced by `Flow`

- Its orchestration logic was retained, but restructured for better alignment with junction logic.

#### **Issue** → ❌ Deprecated

- Replaced with **inline annotations** (`annotation`, `risk_flag`, `assumptive`, etc.) and traceable links (e.g., Jira/GitHub).
- Scope and prioritization now inferred from object linkages (e.g., Problem × Result).

### 🧠 Why the New Hires Matter (Strategic Rationale)

#### **Why We Hired ********`UserOutcome`********:**

> We needed a way to **quantify behavior change** that correlates with Result-level impact — not just observe signals, but attribute meaning to them.\
> ✅ It represents “**Who does what by how much** to make progress toward our Result.”

#### **Why We Hired ********`Flow`********:**

> We needed to **sequence** those signal-generating behaviors and **link them to problems worth solving**, so we could ship with intention — not just feature dump.\
> ✅ It aligns golden paths with real friction and measurable progress.

---

## 6. Migration Notes (v9.4 → v9.5)

- `Issue` deprecated → use annotations (`annotation`, `related_jira_urls`, etc.)
- `Journey` replaced by `Flow`: redefined as Problem × UserOutcome
- `UserOutcome` added: junction of Behavior × Result, representing user value
- `Behavior` flagged as overloaded; candidate for decomposition

---

## 6. Governance Philosophy: The Bobs Protocol

> “If your object can’t explain what it does, prove it with signals, or link to a user problem... then, respectfully — what would you say you do here?”

- Objects must justify their existence through signal-linked impact
- Structural compliance is not optional — it is the baseline for toolchain inclusion
- If you have to *explain* your object verbally — it's not ready

---

## 7. Future Roadmap (v9.6 Preview)

- `Annotation` field overhaul: enum-based `assumptive`, `risk_flagged`, `missing_data`, `needs_verification`
- Junction utilities:
- Evaluate integration of BDD test status to enable test-driven progress tracking 
- Object risk matrix linking schema validation to insight readiness

---

> “We’re here to align users, systems, and outcomes — not to write object fan fiction.”

