# 🏗️ IaC Backlog

## User Flow Object Schema Changes

### ✅ Completed Changes
- [x] Reformatted to match template structure
- [x] Added missing `evidence` field
- [x] Replaced `protocol_id` with `reference_url`
- [x] Corrected field names (`Problem_id` → `problem_id`)

### 🔄 In Progress Changes
- [ ] **`result_id` → `user_outcome_id`**: Update field name to reflect correct relationship
- [ ] **Remove progress indicators**: `percent_behaviors_passing`, `last_test_run_at`, `last_failure_at`, `test_results_summary`
- [ ] **Remove metrics**: `completion_rate_goal`, `satisfaction_goal`, `time_goal`
- [ ] **Remove `owner_team`**: Not needed in governance schema
- [ ] **Remove `acceptance_criteria`**: Should be handled by UserOutcome objects

### 📋 Pending Updates
- [ ] Update canonical JSON example to reflect schema changes
- [ ] Update structural role notes to reflect simplified schema
- [ ] Validate that UserFlow is truly Problem × UserOutcome junction
- [ ] Ensure `behavior_sequence` properly references Behavior objects
- [ ] Update governance validation rules for simplified schema

### 🎯 Next Steps
1. Finalize schema simplification
2. Update JSON example
3. Update structural notes
4. Validate against governance requirements
5. Commit and push changes

## Other IaC Items

### Schema Consistency
- [ ] Ensure all object schemas follow same template format
- [ ] Validate field naming conventions across all objects
- [ ] Standardize evidence field usage across objects

### Governance Integration
- [ ] Update validation scripts for UserFlow schema changes
- [ ] Ensure governance pipeline handles simplified schemas
- [ ] Test schema validation with updated requirements

---
*Last updated: 2025-01-07* 