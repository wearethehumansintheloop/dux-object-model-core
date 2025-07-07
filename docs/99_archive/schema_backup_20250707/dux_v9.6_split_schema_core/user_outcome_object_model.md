# 🧭 User Outcome Object

## 🎯 Purpose & Strategic Role
A **User Outcome** represents the observable benefit a user enjoys as a result of engaging in key behaviors within a given user flow. It is used to **link behavioral evidence to business impact** by way of success metrics, key signals, and intended degree of change.

## 🧠 JTBD Example
> When I need to evaluate the success of a new product enhancement, I need a way to monitor specific actions that signal people are using it, so that I can measure adoption rates and project future capacity based on demand.

## 💡 Why the User Outcome Object Matters
- Links behavioral evidence to business impact through success metrics and key signals.
- Provides observable benefits that users experience from engaging in key behaviors.
- Enables measurement of progress toward business results through user-level outcomes.
- Creates the bridge between user actions and business impact.

## 📋 Schema Attributes
| Field                | Type      | Required | Description                                                                                  |
|---------------------|-----------|----------|----------------------------------------------------------------------------------------------|
| object_type         | string    | Yes      | Must be "UserOutcome"                                                                        |
| id                  | string    | Yes      | Unique identifier                                                                            |
| result_id           | string    | Yes      | Links the outcome to the business/customer goal                                              |
| user_flow_id        | string    | Yes      | Flow context used to derive behaviors and signals                                            |
| key_behavior_ids    | [string]  | Yes      | Sequence of behaviors linked to outcome achievement                                          |
| key_signal_ids      | [string]  | Yes      | Specific signals emitted that can be observed or measured                                    |
| success_metric_id   | string    | Yes      | Metric that this outcome helps move                                                          |
| degree_of_change    | string    | Yes      | How much the signal must change to impact the success metric                                 |
| impact_target       | string    | Yes      | Business measure that improves when success metric is hit                                    |
| evidence            | [string]  | Yes      | Array of Provenance object IDs                                                               |
| tags                | [string]  | No       | System-derived tags                                                                          |
| created_at          | string    | No       | Creation timestamp                                                                           |
| updated_at          | string    | No       | Last update timestamp                                                                        |

## 📦 Canonical Example (Schema-Compliant)
```json
{
  "object_type": "UserOutcome",
  "id": "useroutcome_001",
  "result_id": "result_001",
  "user_flow_id": "flow_001",
  "key_behavior_ids": ["behavior_001", "behavior_002"],
  "key_signal_ids": ["signal_001", "signal_002"],
  "success_metric_id": "metric_001",
  "degree_of_change": "10% increase",
  "impact_target": "Revenue growth",
  "evidence": ["provenance_007", "provenance_008"]
}
```

## 🔗 Structural Role & Usage Notes
- A **User Outcome** emerges as a **junction object** formed when a Behavior and Result come together.
- It only comes into being when a Result exists that defines the desired success metric and impact target.
- A User Flow is linked, containing sequenced Behaviors with traceable signals.
- Those Behaviors emit or infer measurable Signals tied to progress toward the Result.
- User Outcome validity requires at least 1 key behavior, at least 1 associated signal, traceability to a Result object, and explicit or inferred degree of change.