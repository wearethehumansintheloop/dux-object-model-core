# 🔷 Behavior Object (v9.6.1)

## 🎯 Purpose & Strategic Role
A Behavior object is a discrete, observable action that can be tested, tracked, and taught. It is foundational to tracking user adoption and forecasting demand, and is always evidence-backed.

## 🧠 "What would you say... you do here?"
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
| behavior_id         | string    | Yes      | Unique identifier                                                                            |
| user_enablement     | string    | Yes      | User enablement statement: '[Persona] is able to [task/action]'                              |
| result_id           | string    | Yes      | The result for which the behavior is a leading indicator for signaling progress toward result|
| user_flow_id        | string    | Yes      | The user flow that contains this behavior and its sibling behaviors                          |
| signals             | [string]  | Yes      | Loggable system events that prove this behavior occurred                                     |
| end_user            | string    | Yes      | The user who performs this behavior (e.g., "Admin", "Data  Scientist")                       |
| evidence            | [string]  | Yes      | Array of evidence object IDs                                                                 |
| tags                | [string]  | No       | Development traceability tags (GitHub issues, PRs, commits, Jira tickets, status indicators) |
| created_at          | string    | No       | Creation timestamp                                                                           |
| updated_at          | string    | No       | Last update timestamp                                                                        |

## 📦 Canonical Example (Schema-Compliant)
```json
{
  "object_type": "Behavior",
  "behavior_id": "behavior_001",
  "user_enablement": "Admin is able to configure automated report delivery",
  "result_id": "result_004",
  "user_flow_id": "flow_004",
  "end_user": "Admin",
  "signals": ["report_config_event_created", "scheduled_delivery_triggered"],
  "evidence": ["evidence_003", "evidence_004"],
  "tags": ["admin", "automation", "issue-14", "pr-89", "open"],
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