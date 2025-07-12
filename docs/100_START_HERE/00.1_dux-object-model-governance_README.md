# DUX Object Model Governance & Validation Scripts

## Overview
This directory contains the core scripts and utilities for validating, governing, and managing the canonical DUX Object Model. The system ensures that only schema-compliant, high-quality UX research objects (Problems, Behaviors, Results, User Outcomes, Flows, Insights, Provenance) enter the canonical source of truth.

## Directory Structure
```
/scripts
  /validation      # Individual object validation scripts (Problem, Behavior, etc.)
  /governance      # Master governance runner and orchestration scripts
  /utilities       # Shared utilities (e.g., duplicate handler)
  /prompts_from_markdown # Prompt templates for extraction/ETL (if present)
```

## Validation Workflow
1. **Drop candidate object files** (usually markdown with embedded JSON) into the `watch_folders/hitl_review` directory.
2. **Run validation scripts** in `/scripts/validation/` for each object type. Each script:
   - Extracts JSON objects from markdown
   - Validates against the latest schema
   - Handles duplicate files (only the most recent version of each object is processed)
   - Moves invalid files to `watch_folders/hitl_failed` with detailed error logs
   - Reports a summary of validation results
3. **Only valid, schema-compliant objects** are considered for governance and canonical inclusion.

## Prompts & Human-in-the-Loop (HITL)
- **Prompts** in `/scripts/prompts_from_markdown/` (if present) are used by the ETL/extraction pipeline to guide LLMs or humans in extracting structured objects from unstructured research data.
- **HITL Review**: Human reviewers can drop, edit, or correct markdown files in the review folder. The validation scripts provide immediate feedback on compliance and errors, supporting iterative improvement.
- **Interplay**: Prompts help generate candidate objects; validation scripts enforce quality; humans can intervene at any stage to correct or improve data.

## Governance Integration
- **Governance scripts** in `/scripts/governance/` (e.g., `run_all_governance.py`) orchestrate the full validation suite, running all object validators in a consistent order and producing a comprehensive governance report.
- **Only validated objects** are eligible for canonical inclusion, versioning, and further governance actions (e.g., approvals, merges, releases).
- **Branch protection and version control** (via git) ensure that all changes to the canonical model are auditable and reviewable.

## Extending the System
- **To add a new object type**: Create a new validation script in `/scripts/validation/` following the established pattern. Update the governance runner if needed.
- **To add new prompts**: Place prompt templates in `/scripts/prompts_from_markdown/` and reference them in your ETL or extraction pipeline.
- **To add new governance logic**: Extend scripts in `/scripts/governance/`.
- **To share utilities**: Place reusable code in `/scripts/utilities/`.

## Quick Start
1. Place candidate markdown files in `watch_folders/hitl_review/`.
2. Run the relevant validation script(s) from `/scripts/validation/`:
   ```bash
   python scripts/validation/validate_problem_objects.py
   python scripts/validation/validate_useroutcome_objects.py
   # ...etc.
   ```
3. Review results and error logs in the console and `watch_folders/hitl_failed/`.
4. Use `/scripts/governance/run_all_governance.py` to run all validations and get a summary.

---

**This system ensures that only high-quality, schema-compliant, and traceable UX research objects enter the DUX Object Model, supporting scalable, collaborative, and auditable research workflows.** 