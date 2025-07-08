# HITL Promotion Candidates

## Purpose
Objects that have **passed validation** and are awaiting **human review** for final approval.

## Workflow
1. **Auto-promoted from review** - Objects that pass validation are automatically moved here
2. **Human review required** - Manual review for content quality, strategic alignment, completeness
3. **Manual promotion to approved** - Human reviewer moves to `hitl_approved_for_production/`

## Automated Pipeline
- ✅ **Pass validation** → Auto-move here from `hitl_review/`
- 👤 **Human approval** → Manual move to `hitl_approved_for_production/`
- ❌ **Human rejection** → Manual move back to queue with feedback

## Current Status
- Created: $(date)
- Purpose: Bridge between automated validation and human oversight
- Next: Objects awaiting human review for final approval