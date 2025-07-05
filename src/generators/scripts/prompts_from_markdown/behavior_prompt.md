# DUX v9.4 Behavior Object Prompt Template

## Object Description
The smallest, testable user or system action required to address

## Prompt Template
Create a Behavior object that follows the DUX v9.4 specification:

**Object Type:** Behavior
**Purpose:** The smallest, testable user or system action required to address

Please define the following core attributes:
- object_type: "Behavior"
- id: Unique identifier
- description: Clear, specific description following DUX v9.4 format
- evidence: Supporting evidence for this behavior
- evidence_status: "evidence_backed", "evidence_present", or "assumptive"

Behavior-specific attributes (refer to schema):
- acceptance_criteria
- user_not_observable
- no_bdd_coverage
- status_reason
- acceptance_criteria_untestable
- time_on_task_goal
- steps_undefined
- related_journey_ids
- dependencies_undefined
- task_with_parent

Ensure the behavior follows DUX v9.4 principles:
- Atomicity: Each object serves a single, clear purpose
- Traceability: Clear relationships to other objects
- Evidence-backed: Supported by concrete evidence
