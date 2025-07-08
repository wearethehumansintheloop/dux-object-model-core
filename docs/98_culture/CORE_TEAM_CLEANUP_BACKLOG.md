# Core Team Infrastructure Cleanup Backlog

This backlog contains infrastructure cleanup tasks for the Object Model Core team. These tasks ensure the Research Platform team has stable, well-organized resources to consume.

## Priority Levels
- **P0**: Critical - Blocking Research Platform team
- **P1**: High - Needed for clean handoff
- **P2**: Medium - Quality of life improvements
- **P3**: Low - Nice to have

---

## P0: Critical Infrastructure Tasks

### 1. Fix DoclingDocument Processing in HITL Pipeline
**Current State**: Stage 3a/4 bypass proper DoclingDocument creation, manual regex parsing
**Desired State**: Proper InputFormat.MD → DoclingDocument → Exploded attribute objects
**Why Critical**: Core markdown-as-source-code philosophy broken without structured docling objects
**Actions**:
- Fix `parse_problem_object.py` to use InputFormat.MD properly
- Implement DoclingDocument explosion into individual attribute objects
- Create HITL workshop activity to validate approach
- Update Stage 3a/4 to use proper DoclingDocument workflow
- Generate exploded docling objects in promotion_candidates

### 2. Move Schemas from Archive to Production Location
**Current State**: Schemas in `docs/99_archive/schema_backup_20250707/dux_v9.6_split_schema/`
**Desired State**: Schemas in `src/dux_v9.6_split_schema/`
**Why Critical**: Research Platform needs stable path for schema consumption
**Actions**:
- Create `src/dux_v9.6_split_schema/` directory
- Move JSON schemas from archive
- Update all references in validation scripts
- Test validation pipeline with new location
- Notify Research Platform of new path

### 3. Consolidate Scattered Prompts
**Current State**: Prompts in 4+ locations:
- `scripts/prompts_from_markdown/`
- `src/prompt_templates/`
- `src/generators/scripts/prompts_from_markdown/`
- `docs/97_prompt_library/`

**Desired State**: Single location: `src/prompts/`
**Why Critical**: Research Platform needs consistent prompt access
**Actions**:
- Audit all prompt locations for latest versions
- Create unified `src/prompts/` directory
- Consolidate all prompts with deduplication
- Update generation scripts to use new location
- Remove old prompt directories

### 4. Establish Schema Generation Pipeline
**Current State**: Multiple generation scripts, unclear which is canonical
**Desired State**: Single entry point for schema generation
**Why Critical**: Need reliable schema updates from markdown
**Actions**:
- Identify canonical generation script
- Create `scripts/generate_schemas.py` as single entry point
- Document generation workflow
- Add to governance pipeline
- Test end-to-end generation

---

## P1: High Priority Tasks

### 5. Create Schema Version Management
**Current State**: No clear versioning strategy
**Desired State**: Semantic versioning with change notifications
**Why Important**: Research Platform needs to track schema changes
**Actions**:
- Add version field to schemas
- Create changelog for schema updates
- Implement version comparison tool
- Add migration guides for breaking changes

### 6. Document Production Paths
**Current State**: Paths scattered across documentation
**Desired State**: Single source of truth for all paths
**Why Important**: Clear contract with Research Platform
**Actions**:
- Create `PRODUCTION_PATHS.md`
- Document all schema locations
- Document all prompt locations
- Document generation scripts
- Add to CLAUDE.md files

### 7. Clean Up Duplicate Directories
**Current State**: Multiple copies of similar content
**Desired State**: Single location for each resource type
**Why Important**: Prevents confusion and sync issues
**Actions**:
- Remove duplicate prompt directories
- Archive old schema versions properly
- Clean up test data duplicates
- Update all references

---

## P2: Medium Priority Tasks

### 8. Standardize Generation Scripts
**Current State**: Multiple generation approaches
**Desired State**: Unified generation framework
**Why Useful**: Maintainability and consistency
**Actions**:
- Refactor generation scripts to shared library
- Create consistent CLI interface
- Add proper logging and error handling
- Write comprehensive tests

### 9. Improve HITL Workflow Documentation
**Current State**: Workflow documented but scattered
**Desired State**: Single comprehensive guide
**Why Useful**: Easier onboarding for new team members
**Actions**:
- Consolidate HITL documentation
- Add workflow diagrams
- Create troubleshooting guide
- Add automation opportunities

### 10. Create Schema Validation Tests
**Current State**: Manual validation only
**Desired State**: Automated schema integrity tests
**Why Useful**: Catch schema issues early
**Actions**:
- Write unit tests for each schema
- Add relationship validation tests
- Create backwards compatibility tests
- Integrate with CI/CD

---

## P3: Nice to Have Tasks

### 11. Archive Old Versions Properly
**Current State**: Old versions in various locations
**Desired State**: Organized archive with clear versioning
**Why Nice**: Historical reference and rollback capability
**Actions**:
- Create structured archive directory
- Move old versions with proper naming
- Add archive README with version history
- Create restoration scripts

### 12. Create Schema Documentation Site
**Current State**: Schema docs in markdown files
**Desired State**: Interactive documentation site
**Why Nice**: Better developer experience
**Actions**:
- Generate HTML docs from schemas
- Add interactive examples
- Create schema relationship visualizations
- Deploy to GitHub Pages

### 13. Add Schema Linting
**Current State**: No automated schema quality checks
**Desired State**: Linting rules for schema consistency
**Why Nice**: Maintain schema quality standards
**Actions**:
- Define schema style guide
- Implement linting rules
- Add pre-commit hooks
- Create auto-fix capabilities

---

## Implementation Notes

### Quick Wins First
Start with P0 tasks that unblock the Research Platform team. Moving schemas and consolidating prompts can be done quickly with immediate impact.

### Communication is Key
Notify Research Platform team before any path changes. Provide migration window and support during transitions.

### Test Everything
Each change should be validated through the full pipeline before considering it complete.

### Document as You Go
Update CLAUDE.md files and other documentation immediately when making changes.

---

## Progress Tracking

- [x] P0.1: Fix DoclingDocument processing in HITL pipeline - BREAKTHROUGH: DoclingDocument uses table.data.grid, not pages. Old parser ignores structured data!
- [ ] P0.2: Move schemas from archive
- [ ] P0.3: Consolidate prompts
- [ ] P0.4: Establish generation pipeline
- [ ] P1.5: Create version management
- [ ] P1.6: Document production paths
- [ ] P1.7: Clean up duplicates
- [ ] P2.8: Standardize generation
- [ ] P2.9: Improve HITL docs
- [ ] P2.10: Create validation tests
- [ ] P3.11: Archive properly
- [ ] P3.12: Create docs site
- [ ] P3.13: Add linting

---

*Last Updated: 2025-07-07*
*Owner: Object Model Core Team*