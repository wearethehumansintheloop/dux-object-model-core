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
| Field               | Type                           | Required | Description                                                                                  |
|---------------------|--------------------------------|----------|----------------------------------------------------------------------------------------------|
| object_type         | string (const: "[ObjectType]") | Yes      | Object type discriminator                                                                    |
| id                  | string                         | Yes      | Unique identifier for this object                                                            |
| [field_name]        | [type]                         | [Yes/No] | [Clear description of what this field represents and how it's used]                         |
| [field_name]        | [type]                         | [Yes/No] | [Clear description of what this field represents and how it's used]                         |
| [field_name]        | [type]                         | [Yes/No] | [Clear description of what this field represents and how it's used]                         |
| tags                | [string]                       | No       | System-derived tags from DUX scan (not manually added)                                      |
| created_at          | string                         | No       | Creation timestamp                                                                           |
| updated_at          | string                         | No       | Last update timestamp                                                                        |

## 📦 Canonical Example (Schema-Compliant)
```json
{
  "object_type": "[ObjectType]",
  "id": "[object_type]_001",
  "[field_name]": "[example_value]",
  "[field_name]": "[example_value]",
  "[field_name]": ["example_array_value_1", "example_array_value_2"],
  "evidence": ["provenance_001", "provenance_002"],
  "tags": ["tag1", "tag2"]
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
- 🟢 Result
- 🎯 Problem
- 💡 Insight
- 🔄 Flow
- 👤 Persona
- 🎪 Journey
- 🏷️ Tag
- 📊 Metric
- 🔗 Relationship 