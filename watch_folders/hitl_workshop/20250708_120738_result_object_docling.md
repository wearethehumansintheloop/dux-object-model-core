# Result Object Docling Export

Source: result_object.md
Generated: Stage 3a Basic Docling

## Generated JSON Schema

```json
{
  "type": "object",
  "properties": {
    "object_type": {
      "type": "string",
      "description": "Must be \"Result\"",
      "enum": [
        "Result"
      ]
    },
    "id": {
      "type": "string",
      "description": "Unique identifier",
      "pattern": "^result_"
    },
    "target_impact": {
      "type": "string",
      "description": "Clear description of the business' desired impact, revenue targets, cost reduction target"
    },
    "success_criteria": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "System-derived or LLM-suggested target threshold for related outcomes' key signals"
    },
    "success_metrics": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "LLM-suggested metrics to help insight building find relevant behaviors"
    },
    "evidence": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Array of Provenance object IDs"
    },
    "useroutcome_ids": {
      "type": "array",
      "items": {
        "type": "string",
        "pattern": "^useroutcome_"
      },
      "description": "Array of UserOutcome object IDs that measure progress toward this result"
    },
    "tags": {
      "type": "array",
      "items": {
        "type": "string"
      },
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
    "target_impact",
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
    "description": "Must be \"Result\""
  },
  {
    "field": "id",
    "type": "string",
    "required": "Yes",
    "description": "Unique identifier"
  },
  {
    "field": "target_impact",
    "type": "string",
    "required": "Yes",
    "description": "Clear description of the business' desired impact, revenue targets, cost reduction target"
  },
  {
    "field": "success_criteria",
    "type": "[string]",
    "required": "No",
    "description": "System-derived or LLM-suggested target threshold for related outcomes' key signals"
  },
  {
    "field": "success_metrics",
    "type": "[string]",
    "required": "No",
    "description": "LLM-suggested metrics to help insight building find relevant behaviors"
  },
  {
    "field": "evidence",
    "type": "[string]",
    "required": "Yes",
    "description": "Array of Provenance object IDs"
  },
  {
    "field": "useroutcome_ids",
    "type": "[string]",
    "required": "No",
    "description": "Array of UserOutcome object IDs that measure progress toward this result"
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
