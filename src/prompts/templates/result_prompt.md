# DUX v9.6 Result Object Prompt Template

## Object Description
Measurable outcome from behavior change - tracks what happens when users adopt new behaviors. A Result is achieved when a set of UserOutcomes are realized, and it addresses one or more Problems.

## Schema Information
**Schema Reference:** `/Users/njayanty/Projects/Upstream Contributions/dux-object-model-v9.4_split/src/dux_v9.6_split_schema/dux_object_result.json`

### Core Required Attributes:
- `object_type`: "Result"
- `id`: Unique identifier

### Required Result-Specific Fields:
- **target_impact** (string): Clear description of the business' desired impact, revenue targets, cost reduction target
- **evidence** (array): Array of `provenance_id` strings that link to `Provenance` objects.

### Optional Result-Specific Fields:
- **useroutcome_ids** (array): User outcomes that measure progress toward this result

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
  "object_type": "Result",
  "id": "result_example_001",
  "target_impact": "Increase user retention by 15% in the next quarter.",
  "evidence": ["provenance_004"]
}
```
