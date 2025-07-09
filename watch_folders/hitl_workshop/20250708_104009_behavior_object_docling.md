# Behavior Object Docling Export

Source: behavior_object.md
Generated: Stage 3a Basic Docling

## Generated JSON Schema

```json
{
  "type": "object",
  "properties": {
    "object_type": {
      "type": "string",
      "description": "Must be \"Behavior\"",
      "enum": [
        "Behavior"
      ]
    },
    "id": {
      "type": "string",
      "description": "Unique identifier",
      "pattern": "^behavior_"
    },
    "user_enablement": {
      "type": "string",
      "description": "User enablement statement: '[Persona] is able to [task/action]'"
    },
    "behavior_type": {
      "type": "string",
      "description": "Enum: Task, Action",
      "enum": [
        "Action",
        "Navigation",
        "Verification",
        "Configuration",
        "Analysis"
      ]
    },
    "signals": {
      "type": "string",
      "description": "Loggable system events that prove this behavior occurred"
    },
    "flow_ids": {
      "type": "object",
      "description": "Array of Flow objects that contain this behavior"
    },
    "acceptance_criteria": {
      "type": "string",
      "description": "Clear, testable criteria that define successful completion of this behavior"
    },
    "evidence_maturity": {
      "type": "string",
      "description": "Enum: 01_assumptive, 02_anecdotal, 03_early_signal, 04_balanced_signal, 05_triangulated"
    },
    "evidence": {
      "type": "string",
      "description": "Array of Provenance object IDs"
    },
    "tags": {
      "type": "string",
      "description": "System-derived tags"
    },
    "created_at": {
      "type": "string",
      "description": "Creation timestamp"
    },
    "updated_at": {
      "type": "string",
      "description": "Last update timestamp"
    }
  },
  "required": [
    "object_type",
    "id",
    "user_enablement",
    "behavior_type",
    "signals",
    "acceptance_criteria",
    "evidence_maturity",
    "evidence"
  ]
}
```

## Extracted Table Data

```json
[
  {
    "field": "object_type",
    "type": "string",
    "required": "Yes",
    "description": "Must be \"Behavior\""
  },
  {
    "field": "id",
    "type": "string",
    "required": "Yes",
    "description": "Unique identifier"
  },
  {
    "field": "user_enablement",
    "type": "string",
    "required": "Yes",
    "description": "User enablement statement: '[Persona] is able to [task/action]'"
  },
  {
    "field": "behavior_type",
    "type": "string",
    "required": "Yes",
    "description": "Enum: Task, Action"
  },
  {
    "field": "signals",
    "type": "[string]",
    "required": "Yes",
    "description": "Loggable system events that prove this behavior occurred"
  },
  {
    "field": "flow_ids",
    "type": "[object]",
    "required": "No",
    "description": "Array of Flow objects that contain this behavior"
  },
  {
    "field": "acceptance_criteria",
    "type": "[string]",
    "required": "Yes",
    "description": "Clear, testable criteria that define successful completion of this behavior"
  },
  {
    "field": "evidence_maturity",
    "type": "string",
    "required": "Yes",
    "description": "Enum: 01_assumptive, 02_anecdotal, 03_early_signal, 04_balanced_signal, 05_triangulated"
  },
  {
    "field": "evidence",
    "type": "[string]",
    "required": "Yes",
    "description": "Array of Provenance object IDs"
  },
  {
    "field": "tags",
    "type": "[string]",
    "required": "No",
    "description": "System-derived tags"
  },
  {
    "field": "created_at",
    "type": "string",
    "required": "No",
    "description": "Creation timestamp"
  },
  {
    "field": "updated_at",
    "type": "string",
    "required": "No",
    "description": "Last update timestamp"
  }
]
```
