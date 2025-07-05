# 🧬 Provenance Object

## 🎯 Purpose & Strategic Role
Represents a traceable, timestamped, and participant-attributed molecule composed of evidence attributes (atoms) used to support DUX objects like Problem, Behavior, Result, and Insight.

## 🧠 JTBD Example
> When I need to validate the evidence behind a research claim, I want to trace back to the original source material and understand the context, so that I can assess the quality and reliability of the evidence supporting our insights.

## 💡 Why the Provenance Object Matters
- Provides traceable evidence for all DUX object claims.
- Enables auditability and validation of research insights.
- Supports evidence maturity assessment and quality scoring.
- Creates transparency in the research process and decision-making.

## 📋 Schema Attributes
| Field               | Type                           | Required | Description                                                                                  |
|---------------------|--------------------------------|----------|----------------------------------------------------------------------------------------------|
| object_type         | string (const: "Provenance")   | Yes      | Object type discriminator                                                                    |
| id                  | string                         | Yes      | Unique identifier for this provenance record                                                |
| source_filename     | string                         | Yes      | Name of the source file (e.g., transcript or dataset)                                       |
| timestamp_in        | string                         | Yes      | Start time or location within source                                                        |
| timestamp_out       | string                         | Yes      | End time or location within source                                                          |
| evidence_maturity   | string (enum)                  | Yes      | System-derived evidence quality tier: 01_assumptive, 02_anecdotal, 03_early_signal, 04_balanced_signal, 05_triangulated |
| evidence_block      | array                          | Yes      | Required array of grouped evidence units — minimum 1 entry to instantiate Provenance object |
| evidence_teaser     | string                         | No       | Optional summary of insight hook for pain point, stat, or finding                           |
| tags                | [string]                       | No       | System-derived tags from DUX scan (not manually added)                                      |
| created_at          | string                         | No       | Creation timestamp                                                                           |
| updated_at          | string                         | No       | Last update timestamp                                                                        |

## 📦 Canonical Example (Schema-Compliant)
```json
{
  "object_type": "Provenance",
  "id": "provenance_001",
  "source_filename": "user_interview_transcript_001.md",
  "timestamp_in": "00:12:45",
  "timestamp_out": "00:15:30",
  "evidence_maturity": "03_early_signal",
  "evidence_block": [
    {
      "teaser": "User expresses frustration with onboarding process",
      "quote": "I spent 20 minutes trying to figure out how to get started, and I'm still not sure I did it right.",
      "citation": "Participant 7, timestamp 00:12:45",
      "provenance_id": "provenance_001",
      "evidence_type": "user_research_finding",
      "confidence_level": "high"
    }
  ],
  "evidence_teaser": "Users struggle with initial platform setup and onboarding flow"
}
```

## 🔗 Structural Role & Usage Notes
- Linked via `provenance_id` in DUX objects.
- Aggregated to derive Insight object `evidence_maturity`.
- Governs auditability and traceability of synthesized claims.
- `EvidenceBlock` is a view within `Provenance`, not a standalone molecule.
- Atoms = individual attribute values (e.g. `quote`, `confidence_level`), not objects.
- Molecules = any composite object traceable to atomic provenance.

