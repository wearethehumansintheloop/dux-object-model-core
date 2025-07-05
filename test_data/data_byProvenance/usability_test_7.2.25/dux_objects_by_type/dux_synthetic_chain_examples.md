
## 📦 Structured DUX Object Blocks for NotebookLM (v9.5)

This file contains **synthetic example** objects for validation and chaining inside NotebookLM. These objects simulate a complete Problem → Result → Behavior flow using canonical v9.5 schema.

---

### 📦 Problem Object

```json
{
  "object_type": "Problem",
  "id": "bella-get-started-easily",
  "description": "When Bella is using the platform for the first time, she wants to launch a development environment quickly, so she can start experimenting and building without friction.",
  "evidence_status": "evidence_present",
  "result_ids": [
    {
      "id": "bella-successful-first-launch",
      "evidence_status": "assumptive"
    }
  ]
}
```

---

### 📦 Result Object

```json
{
  "object_type": "Result",
  "id": "bella-successful-first-launch",
  "description": "First-time users successfully launch a workspace within 5 minutes of clicking 'Create Environment'.",
  "key_signals": [
    "workspace_launch_success_within_5min",
    "new_user_task_completion_without_support_ticket",
    "median_clicks_to_first_environment_ready"
  ],
  "source_behavior_ids": [
    "bella-select-workspace-kind"
  ],
  "acceptance_criteria": [
    "80% of new users complete environment setup in under 5 minutes.",
    "Support requests for 'failed launch' within first session drop below 5%.",
    "At least one environment is running for 90% of users within their first session."
  ],
  "evidence_status": "assumptive",
  "annotation": {
    "type": "assumptive",
    "issue_description": "Signals inferred from UX heuristics and onboarding friction logs — unvalidated in this domain context.",
    "issue_id": "TBD"
  }
}
```

---

### 📦 Behavior Object

```json
{
  "object_type": "Behavior",
  "id": "bella-select-workspace-kind",
  "description": "Bella selects a workspace kind that fits her project’s requirements from the environment setup screen.",
  "behavior_type": "Action",
  "evidence_status": "evidence_present",
  "acceptance_criteria": [
    "Workspace kind options are clearly labeled and categorized.",
    "Bella selects an option without assistance in under 60 seconds.",
    "System logs the selection and launches the corresponding template."
  ]
}
```
