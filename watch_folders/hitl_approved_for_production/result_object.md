# 🟢 Result Object

## 🎯 Purpose & Strategic Role
A Result object defines the measurable impact we're aiming to achieve, often expressed as revenue, cost, retention, satisfaction, or mission outcomes. It anchors investment and strategic decisions in business logic and is always evidence-backed.

## 🧠 JTBD Example
> When I need to decide whether to continue investing in a product or service, I need to assess whether it is producing measurable impact toward our business goals, so that I can prioritize future work based on actual impact — not just activity or effort.

## 💡 Why the Result Object Matters
- Defines the measurable impact we're aiming to achieve.
- Validates whether behaviors and outcomes are worth continued investment.
- Enables value-driven prioritization and de-risks roadmap planning.
- Translates tactical actions into strategic signals visible to leadership.
- Ensures the product is not just usable or adopted — but valuable.

## 📋 Schema Attributes
| Attribute           | Type      | Required | Description                                                                                  |
|---------------------|-----------|----------|----------------------------------------------------------------------------------------------|
| object_type         | string    | Yes      | Must be "Result"                                                                             |
| id                  | string    | Yes      | Unique identifier                                                                            |
| target_impact       | string    | Yes      | Clear description of the business' desired impact, revenue targets, cost reduction target     |
| success_criteria    | string    | No       | System-derived or LLM-suggested target threshold for related outcomes' key signals               |
| success_metrics     | [string]  | No       | LLM-suggested metrics to help insight building find relevant behaviors                           |
| evidence            | [string]  | Yes      | Array of Provenance object IDs                                                               |
| useroutcome_ids     | [string]  | No       | Array of UserOutcome object IDs that measure progress toward this result                        |
| tags                | [string]  | No       | System-derived tags                                                                          |
| created_at          | string    | No       | Creation timestamp                                                                           |
| updated_at          | string    | No       | Last update timestamp                                                                        |

## 📦 Canonical Example (Schema-Compliant)
```json
{
  "object_type": "Result",
  "id": "result_001",
  "target_impact": "Increase revenue by $1M in the first quarter",
  "success_criteria": "Achieve at least 10% growth in new customer acquisition",
  "success_metrics": ["revenue_growth", "customer_acquisition_rate"],
  "evidence": ["provenance_005", "provenance_006"],
  "useroutcome_ids": ["useroutcome_001", "useroutcome_002"],
  "tags": ["revenue_growth", "customer_acquisition", "v9.5"],
  "created_at": "2025-01-07T10:30:00Z",
  "updated_at": "2025-01-07T10:30:00Z"
}
```

## 🔗 Structural Role & Usage Notes
- Anchors investment and strategic decisions in business logic.
- Represents the north star for measurement and impact assessment.
- Must always be evidence-backed (see Provenance object for details).
- Links to UserOutcome objects that measure progress toward the target impact.
- Success criteria can be system-derived from stakeholder config or LLM-suggested.
- Success metrics are LLM-suggested to help insight building find relevant behaviors.
- The Result object is the business goal that UserOutcomes help achieve through Behavior + Result junctions. 