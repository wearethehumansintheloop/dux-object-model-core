# 🟢 Result Object

## 1. Purpose & Strategic Role
A Result object defines the measurable impact we're aiming to achieve, often expressed as revenue, cost, retention, satisfaction, or mission outcomes. It anchors investment and strategic decisions in business logic and is always evidence-backed.

## 2. JTBD Example
> When I need to decide whether to continue investing in a product or service, I need to assess whether it is producing measurable impact toward our business goals, so that I can prioritize future work based on actual impact — not just activity or effort.

## 3. Why the Result Object Matters
- Defines the measurable impact we're aiming to achieve.
- Validates whether behaviors and outcomes are worth continued investment.
- Enables value-driven prioritization and de-risks roadmap planning.
- Translates tactical actions into strategic signals visible to leadership.
- Ensures the product is not just usable or adopted — but valuable.

## 4. Schema Attributes
| Attribute           | Type      | Required | Description                                                                                  |
|---------------------|-----------|----------|----------------------------------------------------------------------------------------------|
| object_type         | string    | Yes      | Must be "Result"                                                                             |
| id                  | string    | Yes      | Unique identifier                                                                            |
| target_impact       | string    | Yes      | Clear description of the business' desired impact, revenue targets, cost reduction target     |
| success_criteria    | string    | No       | Aggregate target threshold set by stakeholder - required delta in related outcomes' key signals to meet success criteria |
| success_metrics     | [string]  | No       | Aggregate metrics used to measure success criteria, derived from key signals of related outcome objects |
| evidence_maturity   | string    | Yes      | Enum: 01_assumptive, 02_anecdotal, 03_early_signal, 04_balanced_signal, 05_triangulated      |
| evidence            | [string]  | Yes      | Array of Provenance object IDs                                                               |
| useroutcome_ids     | [object]  | No       | User outcomes that measure progress toward this result (with id and reference_context)        |
| tags                | [string]  | No       | System-derived tags                                                                          |
| created_at          | string    | No       | Creation timestamp                                                                           |
| updated_at          | string    | No       | Last update timestamp                                                                        |

## 5. Canonical Example (Schema-Compliant)
```json
{
  "object_type": "Result",
  "id": "result_001",
  "target_impact": "Increase revenue by $1M in the first quarter",
  "success_criteria": "Achieve at least 10% growth in new customer acquisition.",
  "success_metrics": ["revenue_growth", "customer_acquisition_rate"],
  "evidence_maturity": "03_early_signal",
  "evidence": ["provenance_005", "provenance_006"],
  "useroutcome_ids": [
    {"id": "useroutcome_001", "reference_context": "Measures progress toward revenue growth."}
  ]
}
```

## 6. Structural Role & Usage Notes
- Anchors investment and strategic decisions in business logic.
- Represents the north star for measurement and impact assessment.
- Must always be evidence-backed (see Provenance object for details). 