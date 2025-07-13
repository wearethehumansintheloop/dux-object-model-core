
## DUX Objects (for NotebookLM Import)

This file includes:
- Problem objects
- Result objects
- Behavior objects
- Flow and UserOutcome scaffolds

Each block is formatted per DUX v9.5 schema, with embedded annotations.

---

## 🧱 Problem Objects

Below are structured `Problem` objects extracted for DUX v9.5. Each is fully schema-compliant and annotated as needed.

```json
{
  "object_type": "Problem",
  "id": "bella-get-started-easily"
}
```

```json
{
  "object_type": "Problem",
  "id": "joel-manage-secure-deprecation",
  "description": "When Joel manages infrastructure updates, he wants to phase out deprecated container images and configs safely, so he can avoid user disruption and maintain system integrity.",
  "evidence_status": "evidence_present",
  "result_ids": [
    {
      "id": "joel-safe-deprecation-process-adopted",
      "evidence_status": "assumptive"
    }
  ]
}
```

---

## 🎯 Result Objects

DUX `Result` objects reflect measurable outcomes. These examples include both validated and assumptive signals.

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
    "bella-browse-filter-workspacekinds",
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

```json
{
  "object_type": "Result",
  "id": "joel-safe-deprecation-process-adopted",
  "description": "Platform admins follow a consistent process for safely deprecating outdated container images or workspace configs.",
  "key_signals": [
    "deprecation_notice_timeline_adherence_rate",
    "percentage_of_users_migrated_prior_to_end_of_support",
    "number_of_failed_workspace_launches_post-deprecation"
  ],
  "source_behavior_ids": [
    "joel-apply-bulk-updates-impacted-workspaces"
  ],
  "acceptance_criteria": [
    "No workspace launches fail due to outdated image after deprecation window.",
    "Over 90% of users voluntarily migrate before force update is applied.",
    "All deprecated configs are flagged and logged within admin dashboard."
  ],
  "evidence_status": "assumptive",
  "annotation": {
    "type": "assumptive",
    "issue_description": "Signals derived from administrative intuition; needs validation from user logs and upgrade telemetry.",
    "issue_id": "TBD"
  }
}
```

---

## 🏃 Behavior Objects

DUX `Behavior` objects describe atomic user actions. Each includes acceptance criteria and annotation metadata.

```json
{
  "object_type": "Behavior",
  "id": "bella-select-workspace-kind"
}
```

---

## 🔄 Flow Objects

```json
{
  "object_type": "Flow",
  "id": "bella-get-started-flow"
}
```

---

## 🌟 UserOutcome Objects

```json
{
  "object_type": "UserOutcome",
  "id": "bella-first-time-user-success"
}
```
