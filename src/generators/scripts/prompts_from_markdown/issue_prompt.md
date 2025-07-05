# DUX v9.4 Issue Object Prompt Template

## Object Description
| Risk Value | Description | Resolution Path |

## Prompt Template
Create a Issue object (Junction Object) that follows the DUX v9.4 specification:

**Object Type:** Issue
**Category:** Junction Object (Relationship/Experience)
**Purpose:** | Risk Value | Description | Resolution Path |

Please define the following core attributes:
- object_type: "Issue"
- id: Unique identifier
- Junction-specific relationships and orchestration fields

Issue-specific attributes (refer to schema):
- user_story_malformed
- evidence_missing
- behavior_unlinked
- problem_unlinked
- result_unlinked

Junction Object principles:
- Orchestration: Manages relationships between core objects
- Experience flow: Defines user experience sequences
- Evidence aggregation: Inherits evidence from linked objects
