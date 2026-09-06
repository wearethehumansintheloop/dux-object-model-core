# [EMOJI] [Object Name] Object

## 🎯 Purpose & Strategic Role
[Clear, concise description of what this object represents and its role in the DUX ecosystem. Should explain the object's function and why it exists.]

## 🧠 "What would you say... you do here?"
> When I need to [specific situation or context], I want to [motivation or goal], so that I can [desired outcome or benefit].

## 💡 Why the [Object Name] Object Matters
- [Key benefit or value proposition #1]
- [Key benefit or value proposition #2]
- [Key benefit or value proposition #3]
- [Key benefit or value proposition #4]

## 📋 Schema Attributes

**Legend**

- `*` = asterisked (drift / confabulation–critical) when the object uses attribute-hashes; companion **attribute-hash** is system-derived.
- **Origin:** `user-authored` | `system-proposed` | `system-derived`
- **Values:** constraint — free text when unconstrained; otherwise the closed set (enum literals, const, etc.)
- **Sample:** illustrative instance value(s); not exhaustive. Canonical JSON below is authoritative for multi-field examples.
- Table order is **HITL / ORCA** (Core → Metadata → Nested objects). Canonical JSON key order is a **runtime** concern — not a drift surface against this table.
- **Base fields (every object):** `object_type`, typed id (e.g. `outcome_id`, `user_outcome_id` — template `id`), `tags`, `created_at`, `updated_at`.

| Attribute | Data type | Values | Sample | Origin | Required | Description |
| --------- | --------- | ------ | ------ | ------ | -------- | ----------- |
| `object_type` | string (const: `"[ObjectType]"`) | `"[ObjectType]"` | `"[ObjectType]"` | system-derived | Yes | Object type discriminator |
| `[object]_id` | string | opaque / typed id | `[object]_001` | system-derived | Yes | Unique identifier for this object (template `id`) |
| `[field_name]` | [type] | [constraint or free text] | [example] | user-authored \| system-proposed \| system-derived | Yes/No | [Clear description of what this field represents and how it's used] |
| `[field_name]` | [type] | [constraint or free text] | [example] | user-authored \| system-proposed \| system-derived | Yes/No | [Clear description of what this field represents and how it's used] |
| `tags` | array of strings | free text items | `["tag1", "tag2"]` | user-authored \| system-derived | No | Traceability / classification tags |
| `created_at` | datetime | ISO 8601 | `2026-08-31T00:00:00Z` | system-derived | No | Creation timestamp |
| `updated_at` | datetime | ISO 8601 | `2026-08-31T00:00:00Z` | system-derived | No | Last update timestamp |

### Nested objects (when applicable)

| Attribute | Data type | Values | Sample | Origin | Required | Description |
| --------- | --------- | ------ | ------ | ------ | -------- | ----------- |
| `[ref]_id` | [Object].id | opaque instance id | `[object]_001` | system-derived | Yes/No | Nested object reference |

## 📦 Canonical Example (Schema-Compliant)
```json
{
  "object_type": "[ObjectType]",
  "[object]_id": "[object]_001",
  "[field_name]": "[example_value]",
  "[field_name]": ["example_array_value_1", "example_array_value_2"],
  "tags": ["tag1", "tag2"],
  "created_at": "2026-08-31T00:00:00Z",
  "updated_at": "2026-08-31T00:00:00Z"
}
```

## 🔗 Structural Role & Usage Notes
- [Key relationship or dependency information]
- [Important usage constraints or requirements]
- [How this object connects to other DUX objects]
- [Any special considerations for implementation or validation]

## 🎨 Emoji Reference
- 🔷 Behavior
- 🧬 Provenance
- 🧭 User Outcome
- 🎯 Outcome (Kit / career track-record deliverable — distinct from User Outcome)
- 🟢 Result
- 🎯 Problem
- 💡 Insight
- 🔄 Flow
- 👤 Persona
- 🎪 Journey
- 🏷️ Tag
- 📊 Metric
- 🔗 Relationship
