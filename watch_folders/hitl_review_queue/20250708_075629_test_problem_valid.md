# 🧩 Problem Object

## 🎯 Purpose & Strategic Role
A Problem object represents a job to be done (JTBD) worth solving.

## 🧠 "What would you say... you do here?"
> When I need to test, I want validation, so I can ensure quality.

## 💡 Why the Problem Object Matters
- Frames opportunities at the right level
- Provides structure for scoring

## 📋 Schema Attributes
| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| object_type | string | Yes | Must be "Problem" |
| id | string | Yes | Unique identifier |
| job_statement | object | Yes | JTBD decomposed |
| evidence | [object] | Yes | Evidence array |

## 📦 Canonical Example (Schema-Compliant)
```json
{
  "object_type": "Problem",
  "id": "problem_001",
  "job_statement": {
    "user_scenario": "When testing",
    "user_enablement": "I want validation",
    "user_outcome": "so I can ensure quality"
  },
  "evidence": [
    {
      "provenance_id": "test_001",
      "supports_fields": ["job_statement"]
    }
  ]
}
```

## 🔗 Structural Role & Usage Notes
- Anchors strategic investment decisions
- Must be evidence-backed
