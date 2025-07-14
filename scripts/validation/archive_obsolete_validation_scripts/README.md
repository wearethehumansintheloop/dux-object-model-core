# Archived Obsolete Validation Scripts

## Purpose
These validation scripts contain WRONG schemas and are archived according to the Generation-First Principle.

## Generation-First Principle
- **NEVER manually create or edit**: JSON schemas, validation scripts, prompts
- **ALWAYS generate from**: Approved docling markdown files
- **If something is wrong**: Fix the markdown source, regenerate - don't fix the script

## Archived Files

### Obsolete Validation Scripts
- `validate_problem_objects.py.OBSOLETE` - Had wrong schema (job_statement as string instead of object)
- `validate_behavior_objects.py.OBSOLETE` - Likely wrong schema
- `validate_result_objects.py.OBSOLETE` - Likely wrong schema

### Broken Stage 3a Scripts
- `stage3a_problem_basic_docling.py.BROKEN` - Import from non-existent parse_problem_object module
- `stage3a_behavior_basic_docling.py.BROKEN` - Import from non-existent parse_behavior_object module  
- `stage3a_result_basic_docling.py.BROKEN` - Import from non-existent parse_result_object module

## Correct Approach
1. Objects pass through HITL pipeline Stages 1-3b
2. Stage 4 GENERATES new validation scripts from docling markdown
3. Generated scripts replace any manual ones

## Date Archived
2025-01-13

## Reason
User directive: "let's stop fixing things - if the file is wrong - lets archive it - we should be generating them from the right docling markdown file"