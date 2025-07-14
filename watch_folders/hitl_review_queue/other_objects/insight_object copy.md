## 📌 Insight Object Guide

### 🧠 JTBD (Job to Be Done)

**When I am presented an example of stakeholder fit,** I want to normalize it using the provided atomized data set, so that I can generate and refine 3 insight chains that meet my interpretation of 'fit to purpose'.

---

### 🧩 What Is the Insight Object?

The Insight object is a **junction object** hired by the **researcher** to fulfill the needs of their customer: the **insight requestor**, **decision informer**, or **decision maker**. It emerges when multiple DUX objects (typically Problem → Key Behavior → Result) are linked by evidence and presented as a coherent, human-readable story.

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

---

### 🎨 Rendering & Interaction Notes (In Progress)

- **Provenance Carousel**: A linked provenance viewer should be rendered under each object in the chain, allowing direct inspection of supporting source(s). No modals are permitted—all provenance blocks must be inline and visible in scroll. This feature is currently in development.

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
        "evidence_maturity": "04_balanced",
        "job_statement": "When managing shared infrastructure for AI workloads, platform admins want to detect and reclaim idle GPU resources proactively, so that quota allocation remains in SLA.",
        "provenance": ["transcript_7.md#quote_14", "dashboard_review_2025Q1"]
      },
      {
        "id": "behavior_2201",
        "object_type": "Behavior",
        "evidence_maturity": "02_anecdotal",
        "job_statement": "Admin reviews GPU utilization metrics for underperforming workloads.",
        "provenance": ["observation_logs#34", "transcript_9.md#quote_5"]
      },
      {
        "id": "result_3541",
        "object_type": "Result",
        "evidence_maturity": "05_complete",
        "job_statement": "Idle GPU usage is proactively reclaimed and reallocated within SLAs.",
        "provenance": ["performance_metrics_2025.csv#idle_stats"]
      }
    ],
    "insight_story_block": [
      {
        "type": "paragraph",
        "content": "Platform administrators are struggling to manage GPU resources effectively. While quota systems are in place, they lack the visibility to identify and reclaim idle GPUs. This leads to inefficient resource allocation and potential SLA breaches. By proactively detecting and reallocating idle GPUs, administrators can improve efficiency and ensure service levels are met."
      }
    ],
    "fit_score": 0.78,
    "annotation": "This insight is based on a combination of direct user feedback and system-level performance data."
  }
]
```
