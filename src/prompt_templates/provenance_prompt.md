# DUX v9.6 Provenance Object Prompt Template

## Object Description
Simple source attribution record for evidence traceability.

## Schema Information
**Schema Reference:** `/Users/njayanty/Projects/Upstream Contributions/dux-object-model-v9.4_split/src/dux_v9.6_split_schema/dux_object_provenance.json`

### Core Required Attributes:
- `object_type`: "Provenance"
- `id`: Unique identifier

### Required Provenance-Specific Fields:
- **evidence_block** (object): Single evidence piece with complete source attribution.

## DUX v9.6 Principles:
- **Atomicity**: Each object serves a single, clear purpose
- **Traceability**: Clear relationships to other objects
- **Evidence-backed**: Supported by concrete, traceable evidence
- **Schema compliance**: All objects must validate against their JSON schema

### Validation:
Objects must pass schema validation using: `jsonschema.validate(object, schema)`

### Example JSON Structure:
```json
{
  "object_type": "Provenance",
  "id": "provenance_example_001",
  "evidence_block": {
    "source_filename": "interview_notes.md",
    "timestamp_in": "00:15:10",
    "timestamp_out": "00:15:45",
    "teaser": "User expresses frustration with discount codes.",
    "quote": "I got frustrated and just gave up when I couldn't figure out how to apply the discount code.",
    "citation": "User Interview, Participant 3, 2025-06-28",
    "evidence_type": "user_interview"
  }
}
```
