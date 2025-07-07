```json
{
  "object_type": "Behavior",
  "id": "behavior_developer_resource_request_001",
  "user_enablement": "An application developer, when migrating from a VM to a container, is able to specify resource requests and limits for their application.",
  "behavior_type": "Action",
  "signals": [
    "git_commit_pushed",
    "helm_chart_updated",
    "container_resource_request_applied"
  ],
  "acceptance_criteria": [
    "Developer successfully commits a change to a Git repository to update their application's resource requests.",
    "The platform applies the new resource configuration to the running container.",
    "The developer defaults to requesting a large allocation (e.g., 4 vCPU, 16GB RAM) because they are unsure of the actual need, mirroring their previous VM-based workflow."
  ],
  "evidence": ["2023_Q3_Cost Management for OpenShift Feedback Community_P3_VDAB"],
  "flow_ids": []
}
```
