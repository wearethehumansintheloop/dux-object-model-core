# 🧩 Problem Object

## 🎯 Purpose & Strategic Role
Test purpose

## 🧠 "What would you say... you do here?"
> Test JTBD

## 💡 Why the Problem Object Matters
- Test

## 📋 Schema Attributes
| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| object_type | string | Yes | Must be "Problem" |
| id | string | Yes | Unique identifier |
| job_statement | string | Yes | JTBD statement |
| evidence | [object] | Yes | Evidence array |

## 📦 Canonical Example (Schema-Compliant)
```json
{
  "object_type": "Problem",
  "id": "problem_001",
  "job_statement": "Test statement",
  "evidence": [{"provenance_id": "test", "supports_fields": ["job_statement"]}]
}
```

## 🔗 Structural Role & Usage Notes
- Test
