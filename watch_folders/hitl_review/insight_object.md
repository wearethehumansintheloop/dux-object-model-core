## 📌 Insight Object Guide

### 🧠 JTBD (Job to Be Done)

**When I am presented an example of stakeholder fit,** I want to normalize it using the provided atomized data set, so that I can generate and refine 3 insight chains that meet my interpretation of 'fit to purpose'.

---

### 🧩 What Is the Insight Object?

The Insight object is a **junction object** hired by the **researcher** to fulfill the needs of their customer: the **insight requestor**, **decision informer**, or **decision maker**. It emerges when multiple DUX objects (typically Problem X Key Behavior -> Insight) are linked by evidence and presented as a coherent, human-readable story.

The Insight object is:

- **A synthetic yet traceable summary** of a claim
- **Grounded in DUX chains**, each with its own provenance
- **Structurally composed** of:
  - `id`
  - `insight_teaser`
  - `insight_chain` (contains `problem_id`, `behavior_id`, `result_id`)
  - `related_objects[]` (each must include `id`, `object_type`, `job_statement`, `evidence_maturity`, and `provenance[]`)
  - `insight_story_block[]` (human-readable, editable prose)
  - `fit_score` (optional, system-generated): Calculated using a composite weighting of `evidence_maturity` across all linked objects. The score reflects how well the combined Problem → Behavior → Result chain meets defined 'fit to purpose' criteria. Chain-level fit prioritizes maturity distribution balance, weakest-link maturity, and whether the progression supports narrative coherence. The `fit_score` also drives related-object suggestions and serves as an explainability surface for human-in-the-loop workflows.
  - `annotation` (optional): Used to document reasoning for overrides or provide additional context.
  - **Provenance Carousel**: A linked provenance viewer under each object in the chain, allowing direct inspection of supporting source(s). No modals are permitted — all provenance blocks must be inline and visible in scroll.

---

### 📀 Prompt for DUX UI Concept Generation in v0.dev

```prompt
You are an Insight Synthesizer working inside a structured LLM design surface (e.g., v0.dev). Your task is to generate three UI-ready concept candidates for inclusion in the DUX visual language system. Each concept must reflect a valid Insight Chain composed of Problem → Behavior → Result objects, and render them as distinguishable cards conforming to established design constraints.

- Combine: 1 Problem → 1 Key Behavior → 1 Result
- Use: the exact schema and structure from the provided `.json` test examples
- Include: canonical job statements, object IDs, object_type, evidence_maturity, and provenance metadata
- Render as editable Insight Cards, using the canonical card design for each object type
- Display object distinctions visually (pass the squint test — no masked representations)
- Output a teaser and supporting story (insight_story_block[]) per chain
- Enable a no-modal human-in-the-loop refinement workflow, where researchers may swap object candidates from a carousel of provenance-backed alternatives below the chain
- Each object must display an inline provenance panel directly below it (scrollable, no modal popups)

LLM Behavior:
- Assume the persona of a transparent assistant, explaining every transformation step
- Do not recommend incomplete objects unless marked as assumptive with annotation
- Format all output to be valid JSON + Markdown as per `insight_object_guide.md`
- All visuals must reflect object type clearly and consistently (e.g., do not confuse card shapes across objects)

This prompt is designed for UI generation in v0.dev, not prose review. Avoid assumptions. Follow object definitions and rendering logic strictly.
```

---

### 📄 Prompt Primer for NotebookLM

```prompt
You are a research assistant. Given a set of atomized DUX v9.5 objects (Problem, Behavior, Result) derived from the uploaded stakeholder artifact, identify 3 possible insight chains. For each chain:

- Return the component object IDs and their object_type
- Include canonical job statements, provenance references, and evidence_maturity
- Format output as a DUX-compliant JSON array following `insight_object_guide.md`
- Do NOT render as cards. JSON only. Markdown is required.
- Follow the `.json` test example format exactly.
```

---

### 📦 Test Examples (.json)

```json
[
  {
    "id": "insight_101",
    "insight_teaser": "Admin fatigue emerges when quota enforcement overrides visibility into idle GPU metrics.",
    "insight_chain": {
      "problem_id": "problem_4391",
      "behavior_id": "behavior_2201",
      "result_id": "result_3541"
    },
    "related_objects": [
      {
        "id": "problem_4391",
        "object_type": "Problem",
        "job_statement": "When managing shared infrastructure for AI workloads, platform admins want to detect and reclaim idle GPU resources proactively, so that quota allocation remains in SLA.",
        "provenance": ["transcript_7.md#quote_14", "dashboard_review_2025Q1"]
      },
      {
        "id": "behavior_2201",
        "object_type": "Behavior",
        "job_statement": "Admin reviews GPU utilization metrics for underperforming workloads.",
        "provenance": ["observation_logs#34", "transcript_9.md#quote_5"]
      },
      {
        "id": "result_3541",
        "object_type": "Result",
        "job_statement": "Idle GPU usage is proactively reclaimed and reallocated within SLAs.",
        "provenance": ["performance_metrics_2025.csv#idle_stats"]
      }
    ],
    "insight_story_block": [
      "Admins are unable to monitor and reclaim idle GPU resources quickly enough to avoid performance cliffs.",
      "To counter this, they review GPU utilization metrics for underperforming workloads.",
      "When this behavior is supported, idle GPU usage is proactively reclaimed and reallocated within SLAs."
    ],
    "fit_score": 0.92
  }
]
```

---

### 🔁 Usage Context

- May be rendered in Insight Card view
- May seed prompt workflows for refining or validating fit
- Output-ready for inclusion in desk reports, research briefings, or product strategy decks

---

### 🧱 Traceability Notes

- Each object listed must link back to a valid Provenance object
- Insight objects must inherit the lowest `evidence_maturity` from its components unless manually overridden and annotated
- Track `evidence_maturity_distribution` for chain-level heat mapping
- Provenance must be visible below each object card to ensure explainability in all UI views
- All related\_objects must include `object_type`
- Related object references should enable retrieval of full provenance objects from the provenance table if not embedded

---

### 📝 Release Notes

- Replaced `evidence_status`-only model with `evidence_maturity` to improve granularity
- `evidence_maturity` levels:
  - 01\_assumptive
  - 02\_anecdotal
  - 03\_emerging
  - 04\_balanced
  - 05\_complete
- Supports future weighting models for insight reliability and automated triage
- Added NotebookLM-compatible prompt for local HITL analysis workflows
- All prompt workflows now support `.md` readout format for clarity
- Insight UI rendering now requires inline provenance display per object for governance
- v0.dev UI generation prompt now explicitly mandates valid `.json` test schema adherence
- Added `insight_chain` as a discrete field for clarity and logic separation
- Updated `related_objects[]` structure to include `object_type`, `annotation`, and full `provenance[]` compatibility
- Replaced `description` with `job_statement` for clarity and schema compliance

