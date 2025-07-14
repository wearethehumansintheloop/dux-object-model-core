# HITL Activity 2 Plan: Canonical Workflow & Directory Structure

**Status**: Ready for Core Team Execution  
**Prerequisites**: P0.2-P0.4 foundation cleanup must be completed first  
**Previous Work**: Activity 1 completed - DoclingDocument explosion proven working

## Background

HITL Activity 1 successfully proved that:
- DoclingDocument processing works using `table.data.grid` approach
- 14 exploded attribute objects can be generated from Problem object
- Structured data access replaces manual regex parsing
- Workshop parser validates the breakthrough concept

**Now we need to define the production workflow and integration points.**

## Prerequisites (P0.2-P0.4 Foundation Work)

Before starting Activity 2, complete these cleanup tasks for a clean foundation:

### P0.2: Move Schemas from Archive
- Move schemas from `docs/99_archive/schema_backup_20250707/` to `src/dux_v9.6_split_schema/`
- Update all validation script references
- Establish stable schema location for Research Platform consumption

### P0.3: Consolidate Scattered Prompts  
- Audit prompts in 4+ locations
- Create unified `src/prompts/` directory
- Consolidate with deduplication
- Update generation scripts

### P0.4: Establish Schema Generation Pipeline
- Identify canonical generation script
- Create single entry point for schema generation
- Document generation workflow
- Test end-to-end generation

## Activity 2 Scope: Post-Explosion Workflow Design

### Key Decisions Needed

#### 1. Canonical Directory Structure
**Questions to resolve:**
- Where do exploded attribute objects live permanently?
- How do they relate to `hitl_promotion_candidates/` → `hitl_approved_for_production/` workflow?
- Integration with existing `src/dux_v9.6_split_schema/` structure?
- Do we need new directories like `src/exploded_attributes/`?

#### 2. Stage 3a/4 Integration  
**Technical integration:**
- Replace broken `scripts/docling/parse_problem_object.py` with workshop version
- Update `scripts/validation/stage3a_problem_basic_docling.py` to use `table.data.grid`
- Define explosion timing: Should explosion happen pre-approval or post-approval?
- Queue management with exploded objects

#### 3. System Propagation
**Automation pipeline:**
- How do approved exploded objects update JSON schemas in `src/dux_v9.6_split_schema/`?
- Integration with prompt generation pipeline in `src/prompts/`
- Backward compatibility strategy during transition
- Research Platform consumption of new structure

### Proposed Workflow Options

#### Option A: Pre-Approval Explosion
```
markdown → Stage 3a (explosion) → promotion_candidates/ (with exploded objects) → human approval → canonical/
```

#### Option B: Post-Approval Explosion  
```
markdown → Stage 3a (basic processing) → promotion_candidates/ → human approval → explosion → canonical/
```

#### Option C: Dual Structure
```
markdown → Stage 3a (both) → promotion_candidates/ (markdown + exploded) → approval → canonical/
```

## Activity 2 Deliverables

### 1. Updated HITL Pipeline Documentation
- Integrate explosion workflow into `HITL_DEVELOPMENT_PIPELINE.md`
- Update Stage 3a/4 documentation with explosion details
- Define canonical directory structure

### 2. Directory Structure Definition
- Finalize location for exploded attribute objects
- Define relationship to existing schema structure
- Document migration path from current to target state

### 3. Integration Plan
- Replace broken parser with workshop version
- Update Stage 3a validation scripts
- Test with real Problem object from promotion candidates

### 4. System Integration Testing
- End-to-end workflow test: markdown → explosion → canonical → system update
- Validation that Research Platform can consume new structure
- Backward compatibility verification

## Success Criteria

- [ ] Complete end-to-end workflow functional: markdown → explosion → canonical → system update
- [ ] Team alignment on canonical directory structure and explosion timing
- [ ] Clear migration plan from current broken state to target state
- [ ] Integration tested with real objects from HITL pipeline
- [ ] Documentation updated to reflect new workflow
- [ ] Research Platform integration verified

## Implementation Approach

### Phase 1: Foundation (Prerequisites)
1. Complete P0.2-P0.4 cleanup tasks
2. Establish clean baseline structure

### Phase 2: Design Decisions (HITL Activity 2)
1. Team discussion on directory structure options
2. Decision on explosion timing (pre vs post approval)
3. Integration approach with existing pipeline

### Phase 3: Implementation
1. Replace broken parser with workshop version
2. Update Stage 3a/4 scripts
3. Create canonical directory structure
4. End-to-end testing

### Phase 4: Validation
1. Test with real Problem object
2. Verify Research Platform integration
3. Document final workflow
4. Team handoff complete

## P0.3 Prompt Consolidation Audit Results

**DISCOVERED: 5+ scattered prompt locations (even more than "4+" in backlog)**

### 📁 **Location 1**: `docs/97_prompt_library/` (3 files) - **USER HANDLING**
- behavior_prompt_persona: columbo, problem_object_prompt_brockavich.md, result_object_prompt_beane .md
- **Status**: User said they have a solution for this location

### 📁 **Location 2**: `scripts/prompts_from_markdown/` (8 files) - **MOST COMPLETE**
- behavior_prompt.md, flow_prompt.md, insight_prompt.md
- problem_agent_prompt.md, problem_agent_prompt_canvas.md 
- provenance_prompt.md, result_prompt.md, useroutcome_prompt.md
- **Analysis**: Most complete set including agent variants

### 📁 **Location 3**: `src/prompt_templates/` (7 files) - **CURRENT TARGET**
- behavior_prompt.md, flow_prompt.md, insight_prompt.md, problem_prompt.md, provenance_prompt.md, result_prompt.md, useroutcome_prompt.md
- **Analysis**: Referenced by `prompt_generator.py` as target directory

### 📁 **Location 4**: `src/generators/scripts/prompts_from_markdown/` (6 files) - **PARTIAL SET**
- behavior_prompt.md, cognitive_sequencing_primer_with_schema_v9.5.md, flow_prompt.md, issue_prompt.md, problem_prompt.md, result_prompt.md
- **Analysis**: Partial set with v9.5 schema primer

### 📁 **Location 5**: **Embedded in Generator Scripts** (3 Python files) - **LOGIC SCATTERED**
- `src/generators/prompt_generator.py` - Contains evidence templates and schema injection logic
- `src/generators/generate_from_markdown.py` - Contains prompt generation templates  
- `src/generators/generate_from_schema.py` - Contains schema-to-prompt conversion
- **Analysis**: Significant prompt generation code embedded in Python files

### 📁 **Location 6**: `test_data/.../extracted_objects_promptNote/` (2 files) - **TEST DATA**
- 316_RUN001.md, 321_RUN002
- **Analysis**: Test data, not active prompts

### P0.3 Consolidation Strategy Recommendations

**Option A: Use Existing Target (`src/prompt_templates/`)**
- Generator already references this location
- Move all .md files here and update embedded Python logic

**Option B: Create New Unified (`src/prompts/`)**
- New clean structure with subdirectories:
  - `src/prompts/templates/` - Static .md files
  - `src/prompts/generators/` - Python generation logic
  - `src/prompts/schemas/` - Schema-aware prompts

**Option C: Activity 2 Scope**
- Defer P0.3 until Activity 2 canonical structure decisions
- Integrate with exploded object workflow design

### Impact on Activity 2
- Prompt consolidation affects where generated prompts from exploded objects should live
- Generator scripts need to consume new exploded attribute structure
- Schema-aware prompt generation must integrate with DoclingDocument workflow

## Notes

- Workshop parser proven working: `watch_folders/hitl_workshop/fixed_docling_parser.py`
- Exploded objects example: `20250707_130903_problem_object_odi_update_exploded_attributes/`
- Current broken parser: `scripts/docling/parse_problem_object.py` (uses regex, ignores DoclingDocument)
- Feature branch: `fix/docling-document-processing` (ready for PR after Activity 2)
- **P0.3 Audit Complete**: 5+ locations documented above

---

**Ready for Core Team**: This plan provides the roadmap for completing the DoclingDocument integration and establishing the canonical workflow for markdown-as-source-code schema governance.