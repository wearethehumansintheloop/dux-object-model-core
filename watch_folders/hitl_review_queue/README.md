# HITL Review Queue

## Purpose
The review queue maintains **one object definition per type** in the active `hitl_review/` folder to prevent version conflicts and maintain single source of truth.

## Governance Rules

### Single Object Per Type Rule
- **Only ONE** object definition per type allowed in `hitl_review/` at any time
- Multiple versions of same object type must queue here until current review is complete
- Sequential processing: current review → approved → next from queue

### Directory Structure
- `problem_objects/` - Queued Problem object definitions
- `behavior_objects/` - Queued Behavior object definitions  
- `result_objects/` - Queued Result object definitions
- `other_objects/` - All other object types

### Processing Workflow
1. **Current object** in `hitl_review/` gets validated for template compliance
2. **If approved**: Moves to `hitl_approved_for_production/`
3. **Next in queue**: Moves from queue to `hitl_review/` for processing
4. **If rejected**: Returns to queue with error log

### File Naming Convention
Use timestamps to maintain queue order:
- `YYYYMMDD_HHMMSS_object_name.md`
- Example: `20250707_143000_problem_object_odi_update.md`

## Current Status
- Established: $(date)
- Purpose: Prevent duplicate object versions in review folder
- Next: Move duplicate objects from hitl_review/ to appropriate queue directories