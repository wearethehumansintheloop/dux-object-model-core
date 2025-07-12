# DUX v9.6 UserOutcome Object Prompt Template

## Object Description
OKR-style tracking object linking user scenarios to measurable business outcomes.

## Schema Information
**Schema Reference:** `/Users/njayanty/Projects/Upstream Contributions/dux-object-model-v9.4_split/src/dux_v9.6_split_schema/dux_object_useroutcome.json`

### Core Required Attributes:
- `object_type`: "UserOutcome"
- `id`: Unique identifier

### Required UserOutcome-Specific Fields:
- **outcome_statement** (string): Who does what by how much to make progress toward our target result? When our user succeeds how will our solution have changed their behavior?
- **key_signals** (array): Observable signals that indicate this outcome is being achieved - derived from key behaviors in related flows
- **acceptance_criteria** (array): Clear, testable criteria that define successful achievement of this outcome
- **evidence** (array): Array of `provenance_id` strings that link to `Provenance` objects.

### Optional UserOutcome-Specific Fields:
- **user_scenario** (string): High-level scenario or context for this outcome
- **target_impact_when_achieved** (string): Expected business or user impact when this outcome is achieved
- **priority** (string): Business priority level for this outcome
- **flow_ids** (array): Array of Flow IDs that contribute to achieving this outcome
- **problem_ids** (array): Array of Problem IDs that this outcome addresses
- **result_ids** (array): Array of Result IDs that contribute to this outcome
- **end_user** (array): User personas or roles who experience this outcome

### Allowed Values:
- **priority**: critical, high, medium, low

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
  "object_type": "UserOutcome",
  "id": "useroutcome_example_001",
  "outcome_statement": "The user is able to complete the checkout process in under 60 seconds.",
  "key_signals": ["checkout_success_event"],
  "acceptance_criteria": ["The time from cart to confirmation is less than 60 seconds on average."],
  "evidence": ["provenance_005"]
}
```
