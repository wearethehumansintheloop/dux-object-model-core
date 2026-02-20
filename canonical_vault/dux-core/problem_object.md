# 🟡 Problem Object (v9.6.1)

## 🎯 Purpose & Strategic Role
A Problem object represents a job to be done (JTBD) worth solving, backed by evidence. It anchors strategic investment decisions and links to User Outcomes, Behaviors, and Results.

## 🧠 What would you say you do here?
> When I need to reallocate roadmap investments in response to low demand or rising acquisition costs, I want to evaluate enhancement and offering opportunities based on how important the underlying need is to both customers and non-customers, and assess how satisfied each group is with existing solutions in the market, so that I can make evidence-based strategic bets to find product–market fit as fast as possible.

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
| problem_id        | string    | Yes      | Unique identifier                                                                            |
| job_statement     | string    | Yes      | JTBD format: "When [situation], I want [motivation], so I can [outcome]."                    |
| opportunity_score | string    | Yes      | Importance + max(Importance - Satisfaction, 0) = Opportunity Score.                           |
| evidence          | [string]  | Yes      | Array of evidence object IDs                                                               |
| end_user          | [string]  | No       | User personas or roles who experience this problem                                           |
| what_is_at_stake  | string    | No       | What users lose or risk if this problem isn't solved                                         |
| protocol_url      | string    | No       | URL to protocol, methodology, or research documentation                                      |
| result_ids        | [object]  | No       | Envisioned results from solving this problem (with id and reference_context)                 |
| useroutcome_ids   | [object]  | No       | User outcomes that solve this problem (with id and reference_context)                        |
| flow_ids          | [object]  | No       | Flows that address how this problem is solved (with id and reference_context)                |
| tags              | [string]  | No       | Development traceability tags (GitHub issues, PRs, commits, Jira tickets, status indicators) |
| created_at        | string    | No       | Creation timestamp                                                                           |
| updated_at        | string    | No       | Last update timestamp                                                                        |

## 📦 Canonical Example (Schema-Compliant)
```json
{
  "object_type": "Problem",
  "problem_id": "problem_001",
  "what_is_at_stake": "Delayed productivity and increased support tickets.",
  "job_statement": "When onboarding to a new platform (situation), I want clear setup steps (motivation), so I can become productive quickly (outcome).",
  "opportunity_score": "Importance + max(Importance - Satisfaction, 0) = Opportunity Score.",
  "evidence": ["evidence_001", "evidence_002"],
  "end_user": ["new_user", "admin"],
  "protocol_url": "https://company.com/onboarding-research"
}
```

## 🔗 Structural Role & Usage Notes
- Anchors strategic investment decisions and links to User Outcomes, Behaviors, and Results.
- Must always be evidence-backed (see evidence object for details). 