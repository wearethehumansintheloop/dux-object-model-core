# DUX v9.4 Problem Object Prompt Template

## Object Description
A user, business, technical, or operational problem worth solving.

## Prompt Template
Create a Problem object that follows the DUX v9.4 specification:

**Object Type:** Problem
**Purpose:** A user, business, technical, or operational problem worth solving.

Please define the following core attributes:
- object_type: "Problem"
- id: Unique identifier
- description: Clear, specific description following DUX v9.4 format
- evidence: Supporting evidence for this problem
- evidence_status: "evidence_backed", "evidence_present", or "assumptive"

Problem-specific attributes (refer to schema):
- jtbd_opportunity_score_missing
- behavior_ids
- impact_undefined
- evidence_missing
- user_ambiguous
- jtbd_malformed
- s_at_stake
- outdated_evidence
- end_user
- updated_at

Ensure the problem follows DUX v9.4 principles:
- Atomicity: Each object serves a single, clear purpose
- Traceability: Clear relationships to other objects
- Evidence-backed: Supported by concrete evidence
