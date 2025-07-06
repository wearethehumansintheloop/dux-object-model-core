# 🔷 Behavior Object

## 🎯 Purpose & Strategic Role
A Behavior object is a discrete, observable action that can be tested, tracked, and taught. It is foundational to tracking user adoption and forecasting demand, and is always evidence-backed.

## 🧠 JTBD Example
> When I need to evaluate the success of a new product enhancement, I need a way to monitor specific actions that signal people are using it, so that I can measure adoption rates and project future capacity based on demand.

## 💡 Why the Behavior Object Matters
- Defines what adoption means in terms of real-world interaction.
- Enables instrumentation — maps to loggable signals (e.g., `report_config_event_created`).
- Supports capacity forecasting — connects usage patterns to architectural demand.
- Provides the definitional glue between user intent, system telemetry, and business outcomes.

## 📋 Schema Attributes
| Attribute           | Type      | Required | Description                                                                                  |
|---------------------|-----------|----------|----------------------------------------------------------------------------------------------|
| object_type         | string    | Yes      | Must be "Behavior"                                                                           |
| id                  | string    | Yes      | Unique identifier                                                                            |
| user_enablement     | string    | Yes      | User enablement statement: '[Persona] is able to [task/action]'                              |

| signals             | [string]  | Yes      | Loggable system events that prove this behavior occurred                                     |
| end_user            | string    | Yes      | The user who performs this behavior (e.g., "Admin", "Data Scientist")                        |
| acceptance_criteria | [string]  | Yes      | Clear, testable criteria that define successful completion of this behavior                  |
| evidence            | [string]  | Yes      | Array of Provenance object IDs                                                               |
| tags                | [string]  | No       | System-derived tags                                                                          |
| created_at          | string    | No       | Creation timestamp                                                                           |
| updated_at          | string    | No       | Last update timestamp                                                                        |

## 📦 Canonical Example (Schema-Compliant)
```json
{
  "object_type": "Behavior",
  "id": "behavior_001",
  "user_enablement": "Admin is able to configure automated report delivery",
  "end_user": "Admin",
  "signals": ["report_config_event_created", "scheduled_delivery_triggered"],
  "acceptance_criteria": ["Setup flow completed in under 5 minutes", "Report received within 7 days"],
  "evidence": ["provenance_003", "provenance_004"],
  "tags": ["admin", "automation", "v9.5"],
  "created_at": "2025-01-07T10:30:00Z",
  "updated_at": "2025-01-07T10:30:00Z"
}
```

## 🔗 Structural Role & Usage Notes
- Behaviors must be measurable and always reference at least one signal.
- Behaviors are always evidence-backed and linked to UserFlows.
- The end_user field provides the "Who" component that UserOutcome inherits.
- Behaviors contain signals that UserFlow sequences and UserOutcome inherits as key_signals.
- UserFlows contain behaviors in their behavior_sequence, creating the path from Problem to UserOutcome. 