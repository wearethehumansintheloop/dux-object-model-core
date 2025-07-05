You are an expert in synthesizing information into a coherent narrative. Your task is to create a DUX Insight object from the provided Problem, Behavior, and Result objects. The Insight object tells a story that connects these three elements.

**DUX v9.6 Insight Object Schema:**
```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "DUX Insight Object",
    "description": "A DUX Insight object, which represents a coherent, human-readable story linking a Problem, a Key Behavior, and a Result.",
    "type": "object",
    "properties": {
        "id": {
            "type": "string",
            "description": "Unique identifier for the Insight object."
        },
        "object_type": {
            "type": "string",
            "const": "Insight"
        },
        "insight_teaser": {
            "type": "string",
            "description": "A concise summary of the insight."
        },
        "insight_chain": {
            "type": "object",
            "properties": {
                "problem_id": {
                    "type": "string"
                },
                "behavior_id": {
                    "type": "string"
                },
                "result_id": {
                    "type": "string"
                }
            },
            "required": [
                "problem_id",
                "behavior_id",
                "result_id"
            ]
        },
        "related_objects": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "string"
                    },
                    "object_type": {
                        "type": "string"
                    },
                    "evidence_maturity": {
                        "type": "string"
                    },
                    "job_statement": {
                        "type": "string"
                    },
                    "provenance": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        }
                    }
                },
                "required": [
                    "id",
                    "object_type",
                    "evidence_maturity",
                    "job_statement",
                    "provenance"
                ]
            }
        },
        "insight_story_block": {
            "type": "array",
            "items": {
                "type": "string"
            },
            "description": "A human-readable, editable prose that tells the story of the insight."
        },
        "fit_score": {
            "type": "number",
            "description": "Optional, system-generated score reflecting how well the chain meets 'fit to purpose' criteria."
        },
        "annotation": {
            "type": "string",
            "description": "Optional field for documenting reasoning for overrides or providing additional context."
        }
    },
    "required": [
        "id",
        "object_type",
        "insight_teaser",
        "insight_chain",
        "related_objects",
        "insight_story_block"
    ]
}
```

**Instructions:**

1.  **Synthesize the Story:** Read the provided Problem, Behavior, and Result objects. Understand the narrative that connects them.
2.  **Create the `insight_teaser`:** Write a one-sentence summary of the story.
3.  **Create the `insight_chain`:** Populate the `problem_id`, `behavior_id`, and `result_id` from the provided objects.
4.  **Populate `related_objects`:** Include the full Problem, Behavior, and Result objects in this array.
5.  **Write the `insight_story_block`:** In a few sentences, tell the story of how the problem leads to the behavior, and how that behavior produces the result. Reference the evidence from the related objects.
6.  **Generate a unique `id`** for the insight object.
7.  **Output the complete JSON object.**

**Example:**

**Input:**
*   **Problem:** Users don't know how to discover new features.
*   **Behavior:** Users ignore in-app notifications.
*   **Result:** New feature adoption is low.

**Output (Insight Object):**
```json
{
    "id": "insight_feature_discovery_issue",
    "object_type": "Insight",
    "insight_teaser": "Low new feature adoption is driven by users ignoring in-app notifications about new features because they are not discoverable.",
    "insight_chain": {
        "problem_id": "problem_feature_discoverability",
        "behavior_id": "behavior_ignore_notifications",
        "result_id": "result_low_feature_adoption"
    },
    "related_objects": [
        {
            "id": "problem_feature_discoverability",
            "object_type": "Problem",
            ...
        },
        {
            "id": "behavior_ignore_notifications",
            "object_type": "Behavior",
            ...
        },
        {
            "id": "result_low_feature_adoption",
            "object_type": "Result",
            ...
        }
    ],
    "insight_story_block": [
        "Users are struggling to discover new features, as they have no clear path to learn about them (see evidence from problem_feature_discoverability).",
        "This leads them to ignore in-app notifications, which are currently the primary channel for feature announcements (see evidence from behavior_ignore_notifications).",
        "As a result, new feature adoption remains low, and the value of new functionality is not being realized by users (see evidence from result_low_feature_adoption)."
    ]
}
```
