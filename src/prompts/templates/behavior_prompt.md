# DUX v9.6 Behavior Object Prompt Template

## Object Description
Atomic, testable user action serving as an instrumentation anchor - defines what adoption means and maps to loggable signals.

## Schema Information
**Schema Reference:** `/Users/njayanty/Projects/Upstream Contributions/dux-object-model-v9.4_split/src/dux_v9.6_split_schema/dux_object_behavior.json`

### Core Required Attributes:
- `object_type`: "Behavior"
- `id`: Unique identifier

### Required Behavior-Specific Fields:
- **user_enablement** (string): User enablement statement: '[Persona] is able to [task/action]' - This core enablement statement defines what behavior we need to make happen for users.
- **behavior_type** (string): Type of behavior being defined
- **signals** (array): Loggable system events that prove this behavior occurred (e.g., 'report_config_event_created'). PROMPT GUIDANCE: Always provide at least one signal - behaviors must be measurable. Use specific, technical event names that developers can implement.
- **acceptance_criteria** (array): Clear, testable criteria that define successful completion of this behavior. PROMPT GUIDANCE: Include at least one criterion that directly relates to the defined signals (e.g., 'User successfully triggers report_config_event_created signal'). Make criteria specific and measurable.
- **evidence** (array): Array of `provenance_id` strings that link to `Provenance` objects.

### Optional Behavior-Specific Fields:
- **flow_ids** (array): Array of Flow objects that contain this behavior - behaviors exist within flow context.

### Allowed Values:
- **behavior_type**: Task, Action

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
  "object_type": "Behavior",
  "id": "behavior_example_001",
  "user_enablement": "A user is able to successfully upload a profile picture.",
  "behavior_type": "Action",
  "signals": ["profile_picture_upload_success"],
  "acceptance_criteria": ["The user's new profile picture is visible on their profile page within 5 seconds of a successful upload."],
  "evidence": ["provenance_001", "provenance_002"]
}
```
