# �� Problem Object

## 🎯 Purpose & Strategic Role
A Problem object represents a job to be done (JTBD) worth solving, backed by evidence and evaluated by the ODI scoring metric, opportunity score. It anchors strategic investment decisions and links to User Outcomes, Behaviors, and Results.

## 🧠 "What would you say... you do here?"
> When I need to reallocate roadmap investments in response to low demand or rising customer acquisition costs, I want to evaluate enhancement and offering opportunities based on how important the underlying need is to both customers and non-customers based on the problem's opportunity score, and assess how satisfied each group is with existing solutions in the market, so that I can make evidence-based strategic bets to find product–market fit as fast as possible.

## 💡 Why the Problem Object Matters
- Frames opportunities at the right level of abstraction — tech-agnostic and future-proof.
- Provides a structure for scoring and comparison using frameworks like ODI.
- Acts as a central anchor linking User Outcomes, Behaviors, Issues, and Evidence.
- Supports strategic pivoting based on real-time demand shifts and market saturation.
- The Problem object isn't just a container for unmet needs — it's a decision-making instrument for high-leverage bets.

## 📄 Docling Metadata
```yaml
format_version: 1.0
object_type: Problem
proposal_status: under_review
natural_language_first: true
validation_format: json
generation_format: markdown
```

## 🎯 Purpose & Strategic Role
A Problem object represents a job to be done (JTBD) worth solving, backed by evidence and evaluated by the ODI scoring metric, opportunity score. It anchors strategic investment decisions and links to User Outcomes, Behaviors, and Results.

## 🧠 "What would you say... you do here?"
> When I need to reallocate roadmap investments in response to low demand or rising customer acquisition costs, I want to evaluate enhancement and offering opportunities based on how important the underlying need is to both customers and non-customers based on the problem's opportunity score, and assess how satisfied each group is with existing solutions in the market, so that I can make evidence-based strategic bets to find product–market fit as fast as possible.

## 💡 Why the Problem Object Matters
- Frames opportunities at the right level of abstraction — tech-agnostic and future-proof.
- Provides a structure for scoring and comparison using frameworks like ODI.
- Acts as a central anchor linking User Outcomes, Behaviors, Issues, and Evidence.
- Supports strategic pivoting based on real-time demand shifts and market saturation.
- The Problem object isn't just a container for unmet needs — it's a decision-making instrument for high-leverage bets.

## 📋 Schema Attributes
| Attribute         | Type      | Required | Description                                                                                  |
|-------------------|-----------|----------|----------------------------------------------------------------------------------------------|
| object_type       | string    | Yes      | Must be "Problem"                                                                            |
| id                | string    | Yes      | Unique identifier                                                                            |
| job_statement     | object    | Yes      | Decomposed JTBD with user_scenario, user_enablement, and user_outcome (each with value and source)
| evidence          | [object]  | Yes      | Array of evidence objects (with provenance_id and supports_fields)                           |
| end_user          | [string]  | No       | User personas or roles who experience this problem                                           |
| what_is_at_stake  | string    | No       | What users lose or risk if this problem isn't solved                                         |
| protocol_url      | string    | No       | URL to protocol, methodology, or research documentation                                      |
| result_ids        | [object]  | No       | Envisioned results from solving this problem (with id and reference_context)                 |
| useroutcome_ids   | [object]  | No       | User outcomes that solve this problem (with id and reference_context)                        |
| flow_ids          | [object]  | No       | Flows that address how this problem is solved (with id and reference_context)                |
| tags              | [string]  | No       | System-derived tags                                                                          |
| created_at        | string    | No       | Creation timestamp                                                                           |
| updated_at        | string    | No       | Last update timestamp                                                                        |

## 🔧 Generated JSON Schema (Proposal)
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "proposal/problem_object_schema.json",
  "title": "Problem Object Schema (Proposal)",
  "type": "object",
  "properties": {
    "object_type": {
      "type": "string",
      "description": "Must be \"Problem\""
    },
    "id": {
      "type": "string",
      "description": "Unique identifier"
    },
    "job_statement": {
      "type": "object",
      "properties": {
        "user_scenario": {
          "type": "string",
          "description": "When [situation]..."
        },
        "user_enablement": {
          "type": "string",
          "description": "I want [motivation]..."
        },
        "user_outcome": {
          "type": "string",
          "description": "so I can [outcome]"
        }
      },
      "required": [
        "user_scenario",
        "user_enablement",
        "user_outcome"
      ],
      "description": "Decomposed JTBD with user_scenario, user_enablement, and user_outcome (each with value and source)"
    },
    "evidence": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "provenance_id": {
            "type": "string",
            "description": "Reference to Provenance object"
          },
          "supports_fields": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "Fields this evidence supports"
          }
        },
        "required": [
          "provenance_id",
          "supports_fields"
        ]
      },
      "description": "Array of evidence objects (with provenance_id and supports_fields)"
    },
    "end_user": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "User personas or roles who experience this problem"
    },
    "what_is_at_stake": {
      "type": "string",
      "description": "What users lose or risk if this problem isn't solved"
    },
    "protocol_url": {
      "type": "string",
      "description": "URL to protocol, methodology, or research documentation"
    },
    "result_ids": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string"
          },
          "reference_context": {
            "type": "string"
          }
        },
        "required": [
          "id"
        ]
      },
      "description": "Envisioned results from solving this problem (with id and reference_context)"
    },
    "useroutcome_ids": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string"
          },
          "reference_context": {
            "type": "string"
          }
        },
        "required": [
          "id"
        ]
      },
      "description": "User outcomes that solve this problem (with id and reference_context)"
    },
    "flow_ids": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string"
          },
          "reference_context": {
            "type": "string"
          }
        },
        "required": [
          "id"
        ]
      },
      "description": "Flows that address how this problem is solved (with id and reference_context)"
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
    "job_statement",
    "evidence"
  ]
}
```

## 📦 Canonical Example (Schema-Compliant)
```json
{
  "object_type": "Problem",
  "id": "problem_001",
  "job_statement": {
    "user_scenario": {
      "value": "When onboarding to a new platform",
      "source": "evidence"
    },
    "user_enablement": {
      "value": "I want clear setup steps",
      "source": "evidence"
    },
    "user_outcome": {
      "value": "so I can become productive quickly",
      "source": "evidence"
    }
  },
  "evidence": [
    {
      "provenance_id": "provenance_001",
      "supports_fields": ["job_statement.user_scenario", "job_statement.user_enablement"]
    },
    {
      "provenance_id": "provenance_002",
      "supports_fields": ["job_statement.user_outcome", "what_is_at_stake"]
    }
  ],
  "end_user": ["new_user", "admin"],
  "what_is_at_stake": "Delayed productivity and increased support tickets.",
  "protocol_url": "https://company.com/onboarding-research",
  "result_ids": [
    {
      "id": "result_001",
      "reference_context": "Addresses productivity delays through streamlined onboarding"
    }
  ]
}
```

## 🔗 Structural Role & Usage Notes
- Anchors strategic investment decisions and links to User Outcomes, Behaviors, and Results.
- Must always be evidence-backed (see Provenance object for details).

## ✅ Proposal Validation Status
- Schema table extracted: ✓
- JSON schema generated: ✓
- Table-JSON consistency: ✓
- Ready for Stage 3b validation