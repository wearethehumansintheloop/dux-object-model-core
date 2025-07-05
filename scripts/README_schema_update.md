# Schema Update Pipeline

## Overview

The `update_schemas.py` script is a comprehensive schema management tool that updates JSON schemas based on the latest markdown object model definitions and identifies validation scripts that need manual updates.

## What This Script Does

### 1. Schema Generation
- Reads markdown object model files from `docs/01_versionNext/`
- Extracts JSON schema definitions using the existing `generate_from_markdown.py` logic
- Updates corresponding JSON schema files in `src/dux_v9.6_split_schema/`
- Maintains schema versioning and metadata

### 2. Validation Script Analysis
- Scans all validation scripts in `scripts/validation/`
- Identifies scripts that reference fields or patterns that may have changed
- Generates a report of scripts that need manual review and updates
- Provides specific guidance on what to check in each script

### 3. BDD Validation
- **Runs comprehensive BDD tests** to validate schema updates
- Tests schema field validation, relationship integrity, and metadata
- Validates that validation scripts remain compatible
- Ensures rollback capability and cross-object relationships
- **BDD is the primary validation mechanism** - not just documentation

### 3. Backup and Safety
- Creates timestamped backups of existing schemas before updating
- Validates generated schemas against basic JSON structure
- Provides rollback instructions if needed

## Files Processed

### Input Files (Markdown Object Models)
- `docs/01_versionNext/problem_object_model.md`
- `docs/01_versionNext/behavior_object_model.md`
- `docs/01_versionNext/result_object_model.md`
- `docs/01_versionNext/useroutcome_object_model.md`
- `docs/01_versionNext/user_flow_object_model.md`
- `docs/01_versionNext/provenance_object_model.md`

### Output Files (JSON Schemas)
- `src/dux_v9.6_split_schema/dux_object_problem.json`
- `src/dux_v9.6_split_schema/dux_object_behavior.json`
- `src/dux_v9.6_split_schema/dux_object_result.json`
- `src/dux_v9.6_split_schema/dux_object_useroutcome.json`
- `src/dux_v9.6_split_schema/dux_object_flow.json`
- `src/dux_v9.6_split_schema/dux_object_provenance.json`

### Validation Scripts Analyzed
- `scripts/validation/validate_problem_objects.py`
- `scripts/validation/validate_behavior_objects.py`
- `scripts/validation/validate_result_objects.py`
- `scripts/validation/validate_useroutcome_objects.py`
- `scripts/validation/validate_flow_objects.py`
- `scripts/validation/validate_provenance_objects.py`

### BDD Files (Primary Validation)
The script runs BDD tests as the primary validation mechanism:
- `features/schema_update_validation.feature` - Schema update validation scenarios
- `features/steps/schema_update_steps.py` - Schema update validation logic
- `features/signal_flow_validation.feature` - Signal flow and success metrics validation
- `features/steps/signal_flow_validation_steps.py` - Signal flow validation logic
- `features/insight_object_pattern_validation.feature` - Step-by-step insight object pattern validation
- `features/steps/insight_object_pattern_steps.py` - Insight object pattern validation logic
- `features/dux_schema_validation.feature` - General schema validation tests
- BDD tests validate the entire update process and ensure data integrity

## Expected Changes

Based on recent markdown updates, expect these schema changes:

### Problem Object
- No major changes expected
- Field validation patterns may be refined

### Behavior Object
- Added `end_user` field
- Removed `behavior_type` field
- Updated relationship patterns

### Result Object
- Simplified `useroutcome_ids` structure
- Updated `success_criteria` and `success_metrics` descriptions
- Clarified LLM-suggested vs system-derived fields

### UserOutcome Object
- Added optional `user_flow_id` field
- Updated `key_signals` conditional logic
- Clarified inheritance patterns

### User Flow Object
- Added `evidence` field
- Replaced `protocol_id` with `reference_url`
- Updated field names and descriptions

### Provenance Object
- No major changes expected
- Metadata patterns may be refined

## Running the Script

```bash
cd "DUX Object Model (Core)"
python scripts/update_schemas.py
```

## Output

The script will generate:

1. **Updated JSON schemas** in `src/dux_v9.6_split_schema/`
2. **Backup files** in `src/dux_v9.6_split_schema/backups/`
3. **Validation script report** showing which scripts need manual updates
4. **BDD test results** validating the entire update process
5. **Console output** with progress and summary information

## Post-Run Actions Required

### 1. Review Schema Changes
- Check that all expected fields are present
- Verify field types and constraints are correct
- Ensure relationship patterns are properly defined

### 2. Update Validation Scripts
- Follow the generated report to identify scripts needing updates
- Update field validation logic where needed
- Test validation scripts with sample data

### 3. Review BDD Test Results
- Check BDD test output for any validation failures
- Review schema field validation results
- Verify relationship integrity test results
- Ensure rollback capability tests pass

### 4. Test the Pipeline
- Run the governance pipeline to ensure everything works
- Check that existing valid objects still pass validation
- Verify that invalid objects are properly caught
- Run additional BDD tests to ensure all feature specifications work

## Rollback Instructions

If issues arise:

1. **Restore schemas from backup:**
   ```bash
   cp src/dux_v9.6_split_schema/backups/*.json src/dux_v9.6_split_schema/
   ```

2. **Check git history:**
   ```bash
   git log --oneline -10
   git checkout <previous-commit> -- src/dux_v9.6_split_schema/
   ```

## Safety Notes

- The script creates backups before making changes
- It validates JSON structure before writing files
- It doesn't modify validation scripts automatically
- All changes are logged for audit purposes

## Integration with Governance

This script is part of the governance system's schema management workflow:

1. **Markdown updates** → Schema generation
2. **Schema validation** → Validation script updates
3. **Testing** → Governance pipeline verification
4. **Production** → Deployment to main branch

The script maintains the declarative UX approach where schemas are the source of truth for object structure and validation rules. 