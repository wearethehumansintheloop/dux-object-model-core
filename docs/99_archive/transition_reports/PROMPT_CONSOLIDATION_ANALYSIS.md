# Prompt Consolidation Analysis

## Overview
This analysis documents all prompt locations in the DUX Object Model Core codebase to support consolidation efforts. The goal is to address the problem where "LLMs context windows get full they forget the directory structure and create a whole new architecture within an architecture."

## Current Prompt Locations

### 1. `/src/prompts/` (Recommended Primary Location)
**Status**: Well-structured, appears to be the intended consolidated location
- **agents/**: 6 agent prompts (advocate, archivist, behavior, dev_manager, problem, result)
- **library/**: 13 archived/variant prompts (canvas variations, personas)
- **templates/**: 7 object-type prompts (behavior, flow, insight, problem, provenance, result, useroutcome)
- **README.md**: Present

### 2. `/src/prompt_templates/` (Duplicate)
**Status**: Contains identical files to `/src/prompts/templates/`
- 7 files that are exact duplicates of templates in `/src/prompts/templates/`
- Should be removed - redundant

### 3. `/docs/97_prompt_library/` (Archive)
**Status**: Contains archived prompt variations
- 13 files - appear to be the same as `/src/prompts/library/`
- Archive of different prompt personas and approaches
- Includes: archivist canvas, behavior personas (Columbo), problem personas (Brockavich), result personas (Beane)

### 4. `/scripts/prompts_from_markdown/` (Complete Set)
**Status**: Most complete object prompt set, includes agent variants
- 8 files including:
  - Object prompts: behavior, flow, insight, problem, provenance, result, useroutcome
  - Agent variant: problem_agent_prompt.md, problem_agent_prompt_canvas.md

### 5. `/src/generators/scripts/prompts_from_markdown/` (Partial Set)
**Status**: Subset with schema primer
- 6 files including:
  - Object prompts: behavior, flow, problem, result
  - Special: cognitive_sequencing_primer_with_schema_v9.5.md
  - Extra: issue_prompt.md (not found elsewhere)

### 6. Embedded in Python Files
**Status**: Prompts embedded in generator code
- `/src/generators/prompt_generator.py`: References prompts in `/src/prompt_templates/`
- `/src/generators/generate_synthetic_data.py`: Contains data generation logic but no user-facing prompts
- `/src/generators/generate_from_markdown.py`: Likely contains prompt logic

## Unique Content by Location

### Unique to `/src/generators/scripts/prompts_from_markdown/`:
- `cognitive_sequencing_primer_with_schema_v9.5.md` - Schema primer document
- `issue_prompt.md` - GitHub issue generation prompt

### Unique to `/scripts/prompts_from_markdown/`:
- `problem_agent_prompt_canvas.md` - Canvas variant of problem agent

### Common Across Multiple Locations:
- Basic object prompts (problem, behavior, result, flow, etc.)
- Agent prompts with various personas
- Archive versions with different approaches

## Dependencies

### Scripts Referencing Prompts:
1. `/src/generators/prompt_generator.py` - References `/src/prompt_templates/`
2. Various validation scripts may reference prompts for object generation

## Consolidation Recommendation

### Phase 1: Immediate Actions
1. **Delete** `/src/prompt_templates/` - Pure duplicate of `/src/prompts/templates/`
2. **Move** unique files from `/src/generators/scripts/prompts_from_markdown/`:
   - `cognitive_sequencing_primer_with_schema_v9.5.md` → `/src/prompts/library/`
   - `issue_prompt.md` → `/src/prompts/templates/`

### Phase 2: Merge and Organize
1. **Compare** `/scripts/prompts_from_markdown/` with `/src/prompts/templates/`
   - Identify any content differences
   - Merge best versions into `/src/prompts/templates/`
2. **Archive** older versions in `/src/prompts/library/` with clear naming

### Phase 3: Update References
1. Update `/src/generators/prompt_generator.py` to use `/src/prompts/templates/`
2. Update any other scripts referencing old prompt locations
3. Remove empty directories after migration

### Phase 4: Clean Up
1. Delete `/scripts/prompts_from_markdown/` after content merged
2. Delete `/src/generators/scripts/prompts_from_markdown/` after content moved
3. Delete `/docs/97_prompt_library/` if truly duplicate of `/src/prompts/library/`

## Final Structure
```
/src/prompts/
├── README.md
├── agents/          # Agent-specific prompts
├── library/         # Archive/variants/experiments
└── templates/       # Current production prompts for each object type
```

This consolidation will prevent the "architecture within architecture" problem by establishing a single, clear location for all prompts.