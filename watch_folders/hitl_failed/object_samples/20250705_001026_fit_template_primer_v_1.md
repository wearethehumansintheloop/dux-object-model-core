# 🧠 Fit Template Extraction Primer (NotebookLM + DUX v9.5)

## Purpose
Extract structured Fit Templates from stakeholder artifacts using DUX v9.5 schema.
This enables reliable insight chaining and prioritization across teams.

## Cognitive Protocol
Follow these steps:
1. Observe the artifact and identify problem/behavior/result framings
2. Cluster them into related chains
3. Structure objects using embedded `.json` schema
4. Render both markdown explanations and final `.json` export block

## Required Output
- Markdown summaries
- Inline `.json` code blocks for each object
- Final export block combining all extractions
- Inline citation for each object

## Schemas

# 📦 DUX v9.5 Schemas for Fit Template Extraction

## 🟡 FitTemplate
```json
{
  "object_type": "FitTemplate",
  "fit_id": "fit_example_001",
  "source_stakeholder": "Product Strategy Lead",
  "artifact_filename": "vision_statement_q3.md",
  "intended_use": "roadmap planning",
  "target_audience": "PM org",
  "framing_assumptions": [
    "Prioritize insights linked to testable behaviors",
    "Fit should align to quarterly OKR cycles"
  ],
  "preferred_chaining_criteria": {
    "problem_scope": "activation",
    "behavior_constraints": ["testable within 30 days"],
    "result_requirements": ["metric-based"],
    "required_evidence_status": "evidence_present"
  },
  "dux_object_map": {
    "problem": { "id": "problem_example_001", "job_statement": "..." },
    "behavior": { "id": "behavior_example_001", "user_enablement": "..." },
    "result": { "id": "result_example_001", "target_impact": "..." }
  },
  "fit_template_type": "starter_hypothesis",
  "evidence_status": "assumptive"
}
```

## 🔶 Problem
```json
{
  "object_type": "Problem",
  "id": "problem_example_001",
  "description": "When users onboard, I want them to activate within 3 days, so I can improve retention.",
  "evidence_maturity": "01_assumptive",
  "evidence": ["provenance_001", "provenance_002", "provenance_003"]
}
```

## 🔷 Behavior
```json
{
  "object_type": "Behavior",
  "id": "behavior_example_001",
  "description": "PM is able to launch re-engagement nudges within the first 3 days",
  "behavior_type": "Task",
  "flow_ids": ["flow_activation"],
  "acceptance_criteria": [
    "Triggered automatically",
    "Tracked via CTR"
  ],
  "evidence_maturity": {
            "type": "string",
            "enum": [
                "01_assumptive",
                "02_anecdotal",
                "03_early_signal",
                "04_balanced_signal",
                "05_triangulated"
            ],
            "description": "Progressive evidence maturity tier: 01_assumptive (inferred, no direct support), 02_anecdotal (1-2 qualitative signals), 03_early_signal (recurring signal, no quant), 04_balanced_signal (qualitative + quantitative), 05_triangulated (cross-method validation)"
  },
  "evidence": ["provenance_001", "provenance_002", "provenance_003"]
}
```

## 🟢 Result
```json
{
  "object_type": "Result",
  "id": "result_example_001",
  "description": "Increase revenue by XM in the first 3 days",
  "evidence_maturity": "01_assumptive",
  "evidence": ["provenance_001", "provenance_002", "provenance_003"]
}
```

## 🧾 Provenance Object (DUX v9.5)
The following schema defines how source attribution must be tracked for each piece of evidence. All DUX objects must include one or more evidence items with full provenance. NotebookLM must extract, store, and return these values inline with every evidence entry.

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "title": "DUX v9.5 Provenance Object",
  "description": "Simple source attribution record for evidence traceability",
  "properties": {
    "object_type": {
      "type": "string",
      "const": "Provenance",
      "description": "Object type discriminator - always 'Provenance'"
    },
    "id": {
      "type": "string",
      "description": "Unique identifier for this provenance record"
    },
    "evidence_block": {
      "type": "object",
      "properties": {
        "source_filename": {
          "type": "string",
          "description": "Original source file name"
        },
        "participant_id": {
          "type": "string",
          "description": "Anonymized participant identifier"
        },
        "timestamp_in": {
          "type": "string",
          "description": "Start time/location within source"
        },
        "timestamp_out": {
          "type": "string",
          "description": "End time/location within source"
        },
        "teaser": {
          "type": "string",
          "description": "Brief summary or hook that captures the essence of this evidence"
        },
        "quote": {
          "type": "string",
          "description": "Direct quote or summary from source material - complete timestamped segment with no character limits"
        },
        "citation": {
          "type": "string",
          "description": "Who said it, when, and where (e.g. 'Participant 7, timestamp 00:12:45, interview_transcript_p7.md')"
        },
        "evidence_type": {
          "type": "string",
          "enum": [
            "pull_quote",
            "business_directive",
            "user_research_finding",
            "trend_insight"
          ],
          "description": "Type of evidence collected - v.000001 constrained to bounded, traceable data points"
        }
      },
      "required": [
        "source_filename",
        "timestamp_in",
        "timestamp_out",
        "quote",
        "citation",
        "evidence_type"
      ],
      "description": "Single evidence piece with complete source attribution"
    },
    "tags": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "System-derived tags generated by NotebookLM DUX scan - not manually set"
    },
    "created_at": {
      "type": "string",
      "format": "date-time",
      "description": "Creation time of the provenance object instance, not the source material"
    },
    "updated_at": {
      "type": "string",
      "format": "date-time",
      "description": "Last update time of the provenance object instance, not the source material"
    }
  },
  "required": [
    "object_type",
    "id",
    "evidence_block"
  ],
  "additionalProperties": false
}
```

## 🔗 Insight (Junction Object)

An `Insight` object represents a validated chain of `Problem → Behavior → Result` with linked provenance and evidence status propagation.

```json
{
  "object_type": "Insight",
  "id": "insight_example_001",
  "insight_summary": "Disjointed governance structures delay multicloud rollout due to unclear handoffs.",
  "problem_id": "problem_example_001",
  "behavior_id": "behavior_example_001",
  "result_id": "result_example_001",
  "evidence": [
    {
      "object_type": "Provenance",
      "id": "provenance_001",
      "evidence_block": {
        "source_filename": "interview_transcript_p7.md",
        "participant_id": "participant_7",
        "timestamp_in": "00:12:00",
        "timestamp_out": "00:12:45",
        "quote": "When governance roles aren't clear, our migration gets stalled in planning.",
        "citation": "Participant 7, timestamp 00:12:45, interview_transcript_p7.md",
        "evidence_type": "user_research_finding"
      }
    }
  ],
  "evidence_status": "evidence_backed",
  "justification": "This insight reflects a repeated bottleneck in orchestrated planning cited across multicloud teams and supports strategic prioritization of governance alignment in pre-deployment workflows.",
  "tags": ["governance", "multicloud", "orchestration"]
}
```

📌 Linked Provenance should be derived from the individual `Problem`, `Behavior`, and `Result` objects.

📌 The `evidence_status` should reflect the lowest strength of the linked objects, or apply weighted logic if needed.

📌 The `justification` should connect the linked chain to a strategic or observable outcome.

