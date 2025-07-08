# 🔷 Behavior Object

## 1. Purpose & Strategic Role
A Behavior object is a discrete, observable action that can be tested, tracked, and taught. It is foundational to tracking user adoption and forecasting demand, and is always evidence-backed.

## 2. JTBD Example
> When I need to evaluate the success of a new product enhancement, I need a way to monitor specific actions that signal people are using it, so that I can measure adoption rates and project future capacity based on demand.

## 3. Why the Behavior Object Matters
- Defines what adoption means in terms of real-world interaction.
- Enables instrumentation — maps to loggable signals (e.g., `report_config_event_created`).
- Supports capacity forecasting — connects usage patterns to architectural demand.
- Provides the definitional glue between user intent, system telemetry, and business outcomes.

## 4. Schema Attributes
| Attribute           | Type      | Required | Description                                                                                  |
|---------------------|-----------|----------|----------------------------------------------------------------------------------------------|
| object_type         | string    | Yes      | Must be "Behavior"                                                                           |
| id                  | string    | Yes      | Unique identifier                                                                            |
| user_enablement     | string    | Yes      | User enablement statement: '[Persona] is able to [task/action]'                              |
| behavior_type       | string    | Yes      | Enum: Task, Action                                                                           |
| signals             | [string]  | Yes      | Loggable system events that prove this behavior occurred                                     |
| flow_ids            | [object]  | No       | Array of Flow objects that contain this behavior                                             |
| acceptance_criteria | [string]  | Yes      | Clear, testable criteria that define successful completion of this behavior                  |
| evidence_maturity   | string    | Yes      | Enum: 01_assumptive, 02_anecdotal, 03_early_signal, 04_balanced_signal, 05_triangulated      |
| evidence            | [string]  | Yes      | Array of Provenance object IDs                                                               |
| tags                | [string]  | No       | System-derived tags                                                                          |
| created_at          | string    | No       | Creation timestamp                                                                           |
| updated_at          | string    | No       | Last update timestamp                                                                        |

## 5. Canonical Example (Schema-Compliant)
```json
{
  "object_type": "Behavior",
  "id": "behavior_001",
  "user_enablement": "Admin is able to configure automated report delivery",
  "behavior_type": "Task",
  "signals": ["report_config_event_created", "scheduled_delivery_triggered"],
  "acceptance_criteria": ["Setup flow completed in under 5 minutes", "Report received within 7 days"],
  "evidence_maturity": "03_early_signal",
  "evidence": ["provenance_003", "provenance_004"]
}
```

## 6. Structural Role & Usage Notes
- Behaviors must be measurable and always reference at least one signal.
- Behaviors are always evidence-backed and linked to flows. 