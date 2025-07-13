# Governance Workflow Fixes - TODO

## Purpose
Critical gaps identified in the HITL governance workflow that need fixing.

## Template Validation Gap
**Issue**: Validation pipeline only checks JSON schema compliance, completely misses template format compliance.

**Missing Validations:**
- Section structure compliance (must match DUX object template)
- Section title format validation
- Required sections presence check
- Canonical example consistency with schema table

**Impact**: Objects can pass validation while being template non-compliant, breaking the governance workflow.

**Priority**: High - Template compliance is core to object definition standards.

## Status
- Identified: $(date)
- Category: Governance workflow enhancement
- Next: Enhance validation pipeline to include template format checks