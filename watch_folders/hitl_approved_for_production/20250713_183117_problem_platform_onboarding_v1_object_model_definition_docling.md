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
| job_statement     | object    | Yes      | JTBD decomposed into user_scenario, user_enablement, user_outcome with evidence tracking |
| evidence          | [object]  | Yes      | Array of evidence mappings with provenance_id and supported fields                          |
| end_user          | [string]  | No       | User personas or roles who experience this problem                                           |
| what_is_at_stake  | string    | No       | What users lose or risk if this problem isn't solved                                         |
| protocol_url      | string    | No       | URL to protocol, methodology, or research documentation                                      |
| result_ids        | [object]  | No       | Envisioned results from solving this problem (with id and reference_context)                 |
| useroutcome_ids   | [object]  | No       | User outcomes that solve this problem (with id and reference_context)                        |
| flow_ids          | [object]  | No       | Flows that address how this problem is solved (with id and reference_context)                |
| opportunity_score | object    | No       | ODI opportunity score with value, importance, satisfaction, and source tracking (evidence/synthetic) |
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
          "type": "object",
          "properties": {
            "value": {
              "type": "string",
              "description": "When [situation]..."
            },
            "source": {
              "type": "string",
              "enum": [
                "evidence",
                "synthetic"
              ]
            }
          },
          "required": [
            "value",
            "source"
          ]
        },
        "user_enablement": {
          "type": "object",
          "properties": {
            "value": {
              "type": "string",
              "description": "I want [motivation]..."
            },
            "source": {
              "type": "string",
              "enum": [
                "evidence",
                "synthetic"
              ]
            }
          },
          "required": [
            "value",
            "source"
          ]
        },
        "user_outcome": {
          "type": "object",
          "properties": {
            "value": {
              "type": "string",
              "description": "so I can [outcome]"
            },
            "source": {
              "type": "string",
              "enum": [
                "evidence",
                "synthetic"
              ]
            }
          },
          "required": [
            "value",
            "source"
          ]
        }
      },
      "required": [
        "user_scenario",
        "user_enablement",
        "user_outcome"
      ],
      "description": "JTBD decomposed into user_scenario, user_enablement, user_outcome with evidence tracking"
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
      "description": "Array of evidence mappings with provenance_id and supported fields"
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
    "opportunity_score": {
      "type": "object",
      "properties": {
        "value": {
          "type": "number",
          "description": "ODI opportunity score value"
        },
        "importance": {
          "type": "number",
          "description": "How important is this to users (1-10)"
        },
        "satisfaction": {
          "type": "number",
          "description": "How satisfied are users currently (1-10)"
        },
        "value_source": {
          "type": "string",
          "enum": [
            "evidence",
            "synthetic"
          ],
          "description": "Source of the value score"
        },
        "importance_source": {
          "type": "string",
          "enum": [
            "evidence",
            "synthetic"
          ],
          "description": "Source of the importance score"
        },
        "satisfaction_source": {
          "type": "string",
          "enum": [
            "evidence",
            "synthetic"
          ],
          "description": "Source of the satisfaction score"
        }
      },
      "required": [
        "value",
        "importance",
        "satisfaction",
        "value_source",
        "importance_source",
        "satisfaction_source"
      ],
      "description": "ODI opportunity score with value, importance, satisfaction, and source tracking (evidence/synthetic)"
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
      "provenance_id": "survey_001",
      "supports_fields": ["opportunity_score", "end_user"]
    },
    {
      "provenance_id": "interview_002", 
      "supports_fields": ["job_statement", "what_is_at_stake"]
    }
  ],
  "end_user": ["new_user", "admin"],
  "what_is_at_stake": "Delayed productivity and increased support tickets.",
  "opportunity_score": {
    "value": 12.3,
    "importance": 8.2,
    "satisfaction": 4.1,
    "value_source": "evidence",
    "importance_source": "evidence",
    "satisfaction_source": "evidence"
  },
  "protocol_url": "https://company.com/onboarding-research"
}
```

## 🔗 Structural Role & Usage Notes
- Anchors strategic investment decisions and links to User Outcomes, Behaviors, and Results.
- Must always be evidence-backed (see Provenance object for details).
- **ODI Source Tracking**: Each opportunity_score component (value, importance, satisfaction) requires a source field indicating "evidence" (derived from actual data) or "synthetic" (agent-generated hypothesis). This enables proper color coding and transparency in extraction scenarios.

## ✅ Proposal Validation Status
- Schema table extracted: ✓
- JSON schema generated: ✓
- Table-JSON consistency: ✓
- Ready for Stage 3b validation