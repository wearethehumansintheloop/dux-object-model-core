# DUX v9.6 Problem Object Prompt Template

## Object Description
Strategic job-to-be-done defining market-level opportunities - focuses on user motivations and desired outcomes

## Schema Information
**Schema Reference:** `/Users/njayanty/Projects/Upstream Contributions/dux-object-model-v9.4_split/src/dux_v9.6_split_schema/dux_object_problem.json`

### Core Required Attributes:
- `object_type`: "Problem"
- `id`: Unique identifier

### Required Problem-Specific Fields:
- **job_statement** (string): Job-to-be-done statement following the pattern: 'When [situation], I want [motivation], so I can [outcome].'
- **evidence** (array): Array of `provenance_id` strings that link to `Provenance` objects.

### Optional Problem-Specific Fields:
- **end_user** (array): User personas or roles who experience this problem
- **what_is_at_stake** (string): What users lose or risk if this problem isn't solved
- **protocol_url** (string): URL to protocol, methodology, or research documentation related to this problem
- **result_ids** (array): Envisioned results from solving this problem
- **useroutcome_ids** (array): User outcomes that solve this problem
- **flow_ids** (array): Flows that address how this problem is solved

## DUX v9.6 Principles:
- **Atomicity**: Each object serves a single, clear purpose
- **Traceability**: Clear relationships to other objects
- **Evidence-backed**: Supported by concrete, traceable evidence via `Provenance` objects.
- **Schema compliance**: All objects must validate against their JSON schema

### Validation:
Objects must pass schema validation using: `jsonschema.validate(object, schema)`

### Example JSON Structure:
```json
{
  "object_type": "Problem",
  "id": "problem_example_001",
  "job_statement": "When I am trying to understand my cloud spending, I want to see a breakdown of costs by service, so I can identify areas for optimization.",
  "evidence": ["provenance_003"]
}
```
