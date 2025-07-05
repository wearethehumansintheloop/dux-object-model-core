# DUX v9.5 Schema Compliance Analysis

## Overview
This document compares the current split schema files (labeled as v9.4) against the v9.5 object model guide to identify differences and migration requirements.

## Major Findings

### 🚨 **CRITICAL SCHEMA ERRORS** 
- ✅ **FIXED**: Flow Schema - removed invalid `flow_type` requirement that was breaking validation
- **Flow Schema Missing**: No `linked_user_outcome_ids` field (required for v9.5 junction logic)

### 1. **Schema Title Mismatch**
- **Issue**: All schema files still reference "DUX v9.4" in their titles  
- **Required**: Update titles to "DUX v9.5" and descriptions to reflect v9.5 changes

### 2. **Evidence Structure Discrepancies**

#### Current Schema Evidence Structure:
```json
"evidence": {
  "type": ["string", "array"],
  "items": {
    "properties": {
      "teaser": {"type": "string"},
      "quote": {"type": "string"}, 
      "citation": {"type": "string"},
      "provenance": {
        "properties": {
          "source_filename": {"type": "string"},
          "timestamp_in": {"type": "string"},
          "timestamp_out": {"type": "string"}
        }
      },
      "evidence_type": {
        "enum": ["qualitative", "quantitative", "mixed"]
      },
      "collection_method": {
        "enum": ["interview", "survey", "usability_test", "analytics", "other"]
      }
    }
  }
}
```

#### v9.5 Guide Required Evidence Structure:
```json
"evidence": {
  "type": "array",
  "items": {
    "properties": {
      "quote": {"type": "string"},
      "citation": {"type": "string"},
      "provenance": {
        "properties": {
          "timestamp_in": {"type": "string"},
          "timestamp_out": {"type": "string"},
          "report_slide": {"type": "string"},
          "report_date": {"type": "string"}
        }
      },
      "evidence_type": {
        "enum": ["qualitative", "quantitative", "system_log", "user_interview", "report_summary"]
      },
      "collection_method": {
        "enum": ["interview", "survey"]
      },
      "confidence_level": {
        "enum": ["high", "medium", "low"]
      }
    },
    "required": ["quote", "citation", "provenance", "evidence_type", "collection_method", "confidence_level"]
  }
}
```

**Key Differences:**
- Missing `confidence_level` field (required in v9.5)
- `evidence_type` enum values differ (`mixed` vs `system_log`, `user_interview`, `report_summary`)
- `collection_method` enum values differ (v9.5 only allows `interview` and `survey`)
- `provenance` structure differs (current has `source_filename`, v9.5 adds `report_slide`, `report_date`)
- Current schemas allow `evidence` to be string or array, v9.5 requires array only
- Current has optional `teaser` field, v9.5 doesn't mention it

## Object-Specific Analysis

### Problem Object ✅ Mostly Compliant

**Compliant Attributes:**
- `id`, `description` (JTBD pattern), `what_is_at_stake`, `end_user`, `opportunity_score`
- `flow_ids`, `result_ids`, `evidence_teaser`, `tags`

**Missing/Different in v9.5 Guide:**
- Guide doesn't mention: `protocol_url`, `result_ids_evidence_status`, `flow_ids_evidence_status`
- Guide doesn't mention Jira URL fields: `related_jira_urls`, `spike_urls`, `work_issue_urls`

**Schema Issues:**
- Evidence structure needs v9.5 updates (see evidence analysis above)

### Behavior Object ⚠️ Needs Updates

**v9.5 Guide Attributes:**
- `id`, `description`, `behavior_type`, `flow_ids`, `acceptance_criteria`, `signals`, `evidence`, `tags`

**Current Schema Issues:**
- ✅ Has all required attributes
- ❌ Evidence structure needs v9.5 updates
- ❌ Missing proper evidence array structure validation
- ❌ Description pattern is different: current uses "^.+ is able to .+$", v9.5 doesn't specify pattern

### Result Object ✅ Mostly Compliant

**v9.5 Guide Attributes:**
- `id`, `description`, `end_user`, `source_behavior_ids`, `key_signals`, `success_criteria`, `outcome_metrics`, `evidence`, `tags`

**Current Schema Issues:**
- ✅ Has all required attributes and more
- ❌ Evidence structure needs v9.5 updates
- Extra fields not mentioned in v9.5 guide but likely beneficial: 
  - `derived_from_behavior_signals`, `signal_discovery_method`, Jira URLs

### Flow Object ⚠️ Partial Updates Needed

**v9.5 Guide Attributes:**
- `id`, `title`, `user_scenario`, `linked_problem_ids`, `linked_user_outcome_ids`, `behavior_sequence`, `protocol_url`, `pain_points`, `end_user`, `evidence`, `tags`

**Current Schema Issues:**
- ✅ **FIXED**: Removed invalid `flow_type` requirement  
- ❌ **MISSING**: `linked_user_outcome_ids` (v9.5 junction requirement)
- ❌ **WRONG FIELD NAME**: Current has `problem_ids`, v9.5 specifies `linked_problem_ids`
- ❌ Evidence structure needs v9.5 updates
- ✅ Has: `id`, `title`, `user_scenario`, `behavior_sequence`, `protocol_url`, `pain_points`, `end_user`

### UserOutcome Object ⚠️ Missing Key v9.5 Features

**v9.5 Guide Attributes:**
- `id`, `user_scenario`, `outcome_statement`, `success_criteria`, `target_metrics`
- `key_signals`, `signal_source`, `target_impact_when_achieved`
- `priority`, `related_problem_ids`, `related_result_ids`, `related_flow_ids`, `evidence`, `tags`

**Current Schema Issues:**
- ✅ Has most attributes
- ❌ Evidence structure needs v9.5 updates
- ❌ Missing v9.5 unique junction attributes mentioned in guide:
  - No mention of "degree_of_signal_change" (v9.5 guide mentions this as unique to UserOutcome)

## Migration Priority Matrix

### Critical (Breaking Changes - IMMEDIATE)
1. **🚨 URGENT: Fix Flow Schema**: Add missing `flow_type` property definition (schema is currently broken)
2. **🚨 URGENT: Add Flow UserOutcome Link**: Add `linked_user_outcome_ids` property for v9.5 junction logic
3. **Evidence Structure**: Update all schemas to v9.5 evidence format with `confidence_level`

### Important (Compliance)
1. Update schema titles from v9.4 to v9.5
2. Update evidence enum values to match v9.5 specification (remove `mixed`, `usability_test`, `analytics`, `other`)
3. Align field naming: `problem_ids` → `linked_problem_ids` in Flow schema

### Nice-to-Have (Enhancements)
1. Consider adding v9.5 junction-specific fields mentioned in guide
2. Validate evidence status propagation logic
3. Review and align extra fields not mentioned in v9.5 guide

## Recommended Action Plan

1. ✅ **COMPLETED**: Fixed broken Flow schema (`flow_type` requirement removed)
2. **Phase 1**: Update evidence structure across all schemas to v9.5 format
3. **Phase 2**: Complete Flow object v9.5 compliance (`linked_user_outcome_ids`, field naming)
4. **Phase 3**: Update schema metadata and validation rules  
5. **Phase 4**: Test all objects with updated schemas
6. **Phase 5**: Update code generators and test data to match

## Files That Need Updates

### Schema Files (Priority 1)
- `src/dux_v9.5_split_schema/dux_object_problem.json` ✅ **Updated to v9.5**
- `src/dux_v9.5_split_schema/dux_object_behavior.json` ✅ **Updated to v9.5** 
- `src/dux_v9.5_split_schema/dux_object_result.json` ✅ **Updated to v9.5**
- `src/dux_v9.5_split_schema/dux_object_flow.json` ✅ **Updated to v9.5**
- `src/dux_v9.5_split_schema/dux_object_useroutcome.json` ✅ **Updated to v9.5**
- `src/dux_v9.5_split_schema/dux_meta_schema.json`

### Code Files (Priority 2)
- `src/generate_from_markdown.py` (needs v9.5 object updates)
- `features/steps/test_data_manager.py` (evidence structure updates)
- All BDD step definitions for evidence validation

### Test Data (Priority 3)
- All generated and sample objects in `test_data/` directories
- CSV mapping logic for evidence fields
