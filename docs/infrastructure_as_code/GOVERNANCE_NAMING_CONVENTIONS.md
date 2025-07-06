# DUX Object Model Governance - Naming Conventions

## Overview
This document defines the naming conventions for the DUX Object Model governance system to ensure consistent sorting, organization, and execution order.

## Validation Script Naming Convention

### Format: `validate_[object_type]_objects.py`

**Rules:**
- All lowercase with underscores
- Prefix: `validate_`
- Object type: lowercase, singular form
- Suffix: `_objects.py`
- File extension: `.py`

### Current Validation Scripts (Alphabetical Order)

| Order | Script Name | Object Type | Description |
|-------|-------------|-------------|-------------|
| 1 | `validate_behavior_objects.py` | Behavior | Observable user actions |
| 2 | `validate_flow_objects.py` | Flow | User journey sequences |
| 3 | `validate_insight_objects.py` | Insight | Synthesized findings |
| 4 | `validate_problem_objects.py` | Problem | JTBD statements |
| 5 | `validate_provenance_objects.py` | Provenance | Evidence sources |
| 6 | `validate_result_objects.py` | Result | Desired outcomes |
| 7 | `validate_useroutcome_objects.py` | UserOutcome | User goals |

## Object Type Naming in Schemas

### Schema Object Types (Exact Values)
- `"Behavior"`
- `"Flow"`
- `"Insight"`
- `"Problem"`
- `"Provenance"`
- `"Result"`
- `"UserOutcome"`

### ID Pattern Conventions

| Object Type | ID Pattern | Example |
|-------------|------------|---------|
| Behavior | `^behavior_.*` | `behavior_investigate_001` |
| Flow | `^flow_.*` | `flow_onboarding_001` |
| Insight | `^insight_.*` | `insight_101` |
| Problem | `^problem_.*` | `problem_financial_exclusion_001` |
| Provenance | `^prov_.*` | `prov_financial_exclusion_001` |
| Result | `^result_.*` | `result_001` |
| UserOutcome | `^useroutcome_.*` | `useroutcome_001` |

## File Organization

### Directory Structure
```
dux-object-model-v9.4_split/
├── validate_[object_type]_objects.py    # Individual validation scripts
├── run_all_governance.py                # Master governance script
├── GOVERNANCE_NAMING_CONVENTIONS.md     # This document
├── watch_folders/
│   ├── hitl_review/                     # Input files for validation
│   └── hitl_failed/                     # Quarantined invalid files
└── src/
    └── dux_v9.6_split_schema/           # Schema definitions
```

### Error Log Naming Convention
Format: `{timestamp}_{original_filename}_errors.txt`

Example: `20250705_001406_provenance_object_errors.txt`

## Execution Order

### Governance Flow
1. **Behavior** - Validate observable actions first
2. **Flow** - Validate user journey sequences
3. **Insight** - Validate synthesized findings
4. **Problem** - Validate JTBD statements
5. **Provenance** - Validate evidence sources
6. **Result** - Validate desired outcomes
7. **UserOutcome** - Validate user goals

### Rationale for Order
- **Alphabetical sorting** ensures consistent execution
- **Predictable flow** for governance automation
- **Easy maintenance** when adding new object types
- **Clear dependencies** between object types

## Adding New Object Types

### Steps to Add New Object Type
1. Create validation script: `validate_[newtype]_objects.py`
2. Add to `VALIDATION_SCRIPTS` list in `run_all_governance.py`
3. Maintain alphabetical order
4. Update this document
5. Test with master governance script

### Example for New Object Type "Evidence"
```python
# Script name: validate_evidence_objects.py
# Add to VALIDATION_SCRIPTS list in alphabetical position
VALIDATION_SCRIPTS = [
    "validate_behavior_objects.py",
    "validate_evidence_objects.py",      # New addition
    "validate_flow_objects.py",
    # ... rest of list
]
```

## Best Practices

### Script Naming
- ✅ Use consistent lowercase with underscores
- ✅ Follow the `validate_[object_type]_objects.py` pattern
- ✅ Maintain alphabetical order in master script
- ❌ Don't use camelCase or PascalCase
- ❌ Don't use hyphens or spaces

### Object Type References
- ✅ Use exact schema values in validation scripts
- ✅ Use consistent ID patterns
- ✅ Follow established naming conventions
- ❌ Don't mix naming styles
- ❌ Don't use abbreviations without documentation

### File Organization
- ✅ Keep all validation scripts in root directory
- ✅ Use descriptive error log names
- ✅ Maintain clear directory structure
- ❌ Don't scatter validation scripts across subdirectories
- ❌ Don't use generic or unclear names

## Maintenance

### Regular Tasks
1. **Review naming consistency** - Monthly
2. **Update documentation** - When adding new object types
3. **Test execution order** - After any changes
4. **Validate schema alignment** - Quarterly

### Version Control
- Commit naming convention changes with clear messages
- Tag releases with governance version numbers
- Document breaking changes to naming conventions

---

**Last Updated:** 2025-07-05
**Version:** 1.0
**Governance System:** DUX Object Model v9.6 