# DUX v9.6 Flow Object Prompt Template

## Object Description
Behavior orchestration defining sequences of atomic user actions - maps user workflows and journey phases. **Note: Flow serves as a junction object connecting Problems and UserOutcomes.**

## Schema Information
**Schema Reference:** `/Users/njayanty/Projects/Upstream Contributions/dux-object-model-v9.4_split/src/dux_v9.6_split_schema/dux_object_flow.json`

### Core Required Attributes:
- `object_type`: "Flow"
- `id`: Unique identifier

### Required Flow-Specific Fields:
- **title** (string): Human-readable name for this flow
- **behavior_sequence** (array): Ordered sequence of behavior IDs that make up this flow. The context can specify if a behavior is a 'key_behavior'. PROMPT GUIDANCE: When generating flows, LLM should infer and create synthetic Task-type behaviors if they don't exist. Only reference Task behaviors, not Actions.
- **evidence** (array): Array of `provenance_id` strings that link to `Provenance` objects.

### Optional Flow-Specific Fields:
- **end_user** (array): User personas or roles who execute this flow
- **user_scenario** (string): Context or situation that triggers this flow
- **protocol_url** (string): URL to protocol, methodology, or workflow documentation for this flow
- **problem_ids** (array): Array of Problem objects that this flow addresses
- **useroutcome_id** (string): ID of the UserOutcome that this flow contributes to achieving. 1:1 relationship - each flow supports one specific outcome.

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
  "object_type": "Flow",
  "id": "flow_example_001",
  "title": "User Completes Profile Setup",
  "behavior_sequence": [
    "behavior_create_account_001",
    "behavior_upload_photo_002",
    "behavior_add_bio_003"
  ],
  "problem_ids": [
      {
          "id": "problem_low_user_engagement_001",
          "reference_context": "This flow directly addresses the problem of low user engagement by guiding users through the critical profile completion steps."
      }
  ],
  "useroutcome_ids": [
      {
          "id": "useroutcome_profile_completion_rate_increase_001",
          "reference_context": "Completing this flow is the primary driver for achieving the desired increase in profile completion rates."
      }
  ],
  "evidence": ["provenance_001", "provenance_002"]
}
```
