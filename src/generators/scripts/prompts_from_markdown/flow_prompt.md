# DUX v9.4 User Flow Object Prompt Template

## Object Description
| Risk Value | Description | Resolution Path | - Unified orchestration for all behavior sequences (minutes to months).

## Prompt Template
Create a Journey object configured as a User Flow that follows the DUX v9.4 specification:

**Object Type:** Journey
**Journey Type:** user_flow
**Category:** Junction Object (Relationship/Experience)  
**Purpose:** Unified orchestration for behavior sequences from tactical (minutes) to strategic (months)

Please define the following core attributes:
- object_type: "Journey"
- journey_type: "user_flow"
- id: Unique identifier
- title: Human-readable name for the user flow
- behavior_sequence: Ordered array of Behavior IDs
- parent_journey_id: Reference to parent user flow (if nested)

Content attributes:
- journey_map_content: Narrative content for strategic flows (transformation story, gates, milestones)
- usability_protocol_content: Testing procedures for tactical flows (validation criteria)

Flow-specific attributes (refer to schema):
- CRITICAL
- no_linked_result
- insufficient_behaviors
- behavior_sequence_broken
- unclear_success_metrics

Junction Object principles:
- Orchestration: Manages relationships between core objects
- Unified approach: Handles both tactical (minutes/hours) and strategic (weeks/months) flows
- Evidence aggregation: Inherits evidence from linked objects
