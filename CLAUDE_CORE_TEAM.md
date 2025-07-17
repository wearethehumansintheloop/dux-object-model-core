# CLAUDE.md - Object Model Core Team Guide

This file provides guidance to Claude Code (claude.ai/code) when helping the Object Model Core team maintain and evolve the DUX schema governance infrastructure.

## 🎯 Core Team Mission

You own the **schema governance infrastructure** that eliminated weekend debugging sessions. Your focus: maintain the single source of truth for DUX object definitions while the Research Platform team builds on top of your foundation.

## 🏗️ What You Own

### Schema Governance
- **Canonical Markdown Definitions**: The source of truth for all object types
- **JSON Schema Generation**: Auto-generation from markdown
- **Template Compliance**: DUX object template enforcement
- **Validation Pipeline**: 4-stage validation process
- **HITL Workflow**: Human-in-the-loop review process

### Infrastructure Components
- **watch_folders/**: HITL review and promotion workflow
- **scripts/validation/**: Multi-stage validation pipeline
- **scripts/governance/**: Master governance orchestration
- **docs/100_START_HERE/**: Object templates and documentation
- **Triple Backlog System**: Infrastructure insights, coaching, architecture

## 🚨 Current State Assessment

### Schema Locations (Needs Cleanup)
- **In Archive**: `docs/99_archive/schema_backup_20250707/dux_v9.6_split_schema/`
- **Markdown Sources**: `docs/99_archive/schema_backup_20250707/dux_v9.6_split_schema_core/`
- **Missing**: Production schema directory in standard location

### Prompt Locations (Scattered)
- `scripts/prompts_from_markdown/`
- `src/generators/scripts/prompts_from_markdown/`
- `src/prompt_templates/`
- `docs/97_prompt_library/`

### Generation Scripts (Multiple)
- `src/generate_from_markdown.py`
- `src/generators/generate_from_markdown.py`
- `src/generators/generate_from_schema.py`
- `src/generators/prompt_generator.py`

## 🔧 Core Workflows

### Schema Update Process
```bash
# 1. Edit canonical markdown definition
# 2. Place in HITL review
cp updated_problem_object.md watch_folders/hitl_review/

# 3. Run validation pipeline
python scripts/validation/validate_dux_objects.py

# 4. If successful, approve to production
mv watch_folders/hitl_promotion_candidates/[file] watch_folders/hitl_approved_for_production/

# 5. Generate JSON schemas
python scripts/update_schemas.py
```

### Governance Validation
```bash
# Run full system validation
cd scripts/governance
python run_all_governance.py

# Check specific object types
cd scripts/validation
python validate_problem_objects.py
```

### Adding New Object Types
1. Create markdown definition following template
2. Add validation script: `validate_[type]_objects.py`
3. Update `config.py` with new type patterns
4. Add to governance orchestration
5. Generate JSON schema and prompts

## 📋 Handoff Points with Research Platform

### What You Provide
- **JSON Schemas**: Generated from canonical markdown
- **Agent Prompts**: Auto-generated extraction agents
- **Validation Rules**: Schema compliance logic
- **Canonical Examples**: Reference implementations

### What They Need From You
- **Stable Schema Location**: Not in archive directory
- **Consistent Prompt Location**: Single source for agents
- **Version Notifications**: When schemas update
- **Clear Migration Path**: From current scattered state

## 🎯 Infrastructure Maintenance

### Daily Operations
- Monitor `hitl_review/` for new submissions
- Run governance validation to ensure system health
- Review failed validations in `hitl_failed/`
- Promote validated objects through pipeline

### Schema Evolution
- Maintain backward compatibility
- Version schemas appropriately
- Update BDD tests for changes
- Regenerate dependent artifacts

### Quality Assurance
- Ensure template compliance
- Validate markdown structure
- Check JSON generation accuracy
- Test with sample data

## 🚀 Key Infrastructure Benefits You Maintain

1. **Single Source of Truth**: Markdown definitions drive everything
2. **Automated Validation**: 4-stage pipeline catches errors early
3. **Agent Generation**: Consistent extraction across studies
4. **Natural Language First**: Human-readable definitions
5. **Evidence Traceability**: Built into schema design

## 📚 Critical Documentation

### Your Documentation
- `docs/100_START_HERE/dux_object_template.md` - The sacred template
- `docs/infrastructure_as_code/GOVERNANCE_NAMING_CONVENTIONS.md` - Naming rules
- `docs/architecture/dux-system-boundaries.md` - System boundaries
- `scripts/README_schema_update.md` - Schema update process

### Backlog Management
- `INFRASTRUCTURE_INSIGHTS_BACKLOG.md` - Pattern improvements
- `COACHING_BACKLOG.md` - Teaching moments
- `CORE_TEAM_CLEANUP_BACKLOG.md` - Infrastructure cleanup tasks

## 🔍 Common Issues & Solutions

### Schema Generation Fails
- Check markdown follows template exactly
- Verify Schema Attributes table format
- Ensure Canonical Example is valid JSON
- Review docling parsing output

### Validation Pipeline Issues
- Check naming convention compliance
- Verify all required fields present
- Look for type mismatches
- Review error logs in detail

### HITL Workflow Stuck
- Check file naming patterns
- Ensure proper queue directories exist
- Verify permissions on watch folders
- Clear any corrupted files

## 🎨 Cursor Rules for Core Work

```bash
# For governance and validation work
cp .cursorrules.base .cursorrules

# For development and debugging
cp .cursorrules.development .cursorrules
```

## 🌟 Remember Your Impact

You maintain the infrastructure that:
- **Eliminated weekend debugging** for research teams
- **Scales globally** through natural language
- **Ensures quality** through automated validation
- **Enables innovation** by handling the complexity

The Research Platform team builds amazing extraction pipelines because you provide rock-solid schema governance. Keep the foundation strong!