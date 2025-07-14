# 🧭 User Flow Object

## 🎯 Purpose & Strategic Role
A **User Flow** is a tactical junction object between a **Problem** and a **User Outcome**. It sequences a set of Behaviors to concretely represent the path a specific Problem is expected to follow to achieve a targeted outcome. It supports usability testing, PRD scoping, and demo storytelling across cross-functional teams.

## 🧠 JTBD Example
> When I need to communicate how our target customer expects to realize value, I want to demonstrate their preferred and expected golden path so I can accelerate our sprint velocity and reduce lead time.

## 💡 Why the User Flow Object Matters
- Sequences behaviors to show the concrete path from Problem to User Outcome
- Supports usability testing and PRD scoping
- Enables demo storytelling across cross-functional teams
- Provides tactical implementation guidance for product teams

## 📋 Schema Attributes
| Field                    | Type      | Required | Description                                                                                  |
|-------------------------|-----------|----------|----------------------------------------------------------------------------------------------|
| object_type             | string    | Yes      | Must be "UserFlow"                                                                           |
| user_flow_id            | string    | Yes      | Unique identifier                                                                            |
| title                   | string    | Yes      | Human-readable name of the flow (e.g., "Onboarding Flow")                                    |
| description             | string    | Yes      | What this flow accomplishes and for whom                                                     |
| problem_id              | string    | Yes      | Problem this flow is scoped to                                                               |
| user_outcome_id         | string    | Yes      | User Outcome the flow aims to fulfill                                                        |
| behavior_sequence       | [string]  | Yes      | Ordered list of Behavior IDs                                                                 |
| evidence                | [string]  | No       | Array of Provenance object IDs or reference URLs                                             |
| reference_url           | string    | No       | Optional link to external protocol or documentation                                          |
| created_at              | datetime  | No       | Creation timestamp                                                                           |
| updated_at              | datetime  | No       | Last update timestamp                                                                        |
| tags                    | [string]  | No       | System-derived tags                                                                          |

## 📦 Canonical Example (Schema-Compliant)
```json
{
  "object_type": "UserFlow",
  "user_flow_id": "flow_001",
  "title": "Onboarding Flow",
  "description": "New user onboarding process to achieve first successful model deployment",
  "problem_id": "problem_001",
  "user_outcome_id": "useroutcome_001",
  "behavior_sequence": ["behavior_001", "behavior_002", "behavior_003"],
  "evidence": ["provenance_001", "provenance_002"],
  "reference_url": "https://docs.example.com/onboarding-protocol",
  "created_at": "2025-01-07T10:30:00Z",
  "updated_at": "2025-01-07T10:30:00Z",
  "tags": ["onboarding", "new_user", "v9.5"]
}
```

## 🔗 Structural Role & Usage Notes
- A **User Flow** emerges as a **junction object** formed when a Problem and User Outcome come together.
- It sequences behaviors to show the concrete path from Problem to User Outcome.
- Behavior sequence is derived based on behaviors tagged to the Problem (indicating capability or motivation) and behaviors linked to the User Outcome (indicating relevance or necessity).
- The system prompts contributors to confirm, edit, or manually compose the golden path by selecting and sequencing behaviors across these two anchors.
- User Flow validity requires at least 2 behaviors in the sequence, a valid problem_id, and a valid user_outcome_id.
- Governance validates the behavior sequence structure and ensures proper Problem-UserOutcome alignment.
- The behavior_sequence provides the signal sources that UserOutcome inherits as key_signals.
- User Flow supports usability testing, PRD scoping, and demo storytelling across cross-functional teams.

