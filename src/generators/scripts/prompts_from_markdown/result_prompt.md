# DUX v9.4 Result Object Prompt Template

## Object Description
A user- or business-facing outcome, explicitly validated and directly

## Prompt Template
Create a Result object that follows the DUX v9.4 specification:

**Object Type:** Result
**Purpose:** A user- or business-facing outcome, explicitly validated and directly

Please define the following core attributes:
- object_type: "Result"
- id: Unique identifier
- description: Clear, specific description following DUX v9.4 format
- evidence: Supporting evidence for this result
- evidence_status: "evidence_backed", "evidence_present", or "assumptive"

Result-specific attributes (refer to schema):
- metrics_unrealistic
- scope_misaligned
- validation_impossible
- journey_sequence
- orphaned_behaviors
- success_criteria_missing
- journey_sequence_broken
- owner_team_undefined
- business_value_unclear
- behavior_change_undefined

Ensure the result follows DUX v9.4 principles:
- Atomicity: Each object serves a single, clear purpose
- Traceability: Clear relationships to other objects
- Evidence-backed: Supported by concrete evidence
