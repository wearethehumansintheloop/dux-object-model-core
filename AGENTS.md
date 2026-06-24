# AGENTS.md

This file provides guidance to Codex (Codex.ai/code) when working with code in this repository.

## Commit Messages
Always use: "co-authored by imstilllearning and claudette xoxo"
Do not use any other credit messaging in commit messages.

## Important Instructions
- Do what has been asked; nothing more, nothing less
- NEVER create files unless absolutely necessary
- ALWAYS prefer editing existing files to creating new ones
- NEVER proactively create documentation files (*.md) or README files unless explicitly requested

## Core Framework

**Declarative UX (DUX)** is an AI-powered framework that transforms UX research into executable, testable code. The system decomposes all software artifacts into three molecular components: **Problems**, **Behaviors**, and **Results**.

## Quick Start Commands

### Run BDD Tests
```bash
# Run all BDD tests
behave features/

# Run specific feature
behave features/dux_schema_validation.feature

# Run tests from tests directory
behave tests/features/
```

### HITL Validation Pipeline
```bash
# Run full 4-stage validation pipeline
python scripts/validation/hitl_pipeline/hitl_orchestrator.py

# Individual validation stages
python scripts/validation/hitl_pipeline/stage1_structure_validation.py    # Structure
python scripts/validation/hitl_pipeline/stage2_consistency_validation.py  # Consistency
python scripts/validation/hitl_pipeline/stage3a_problem_docling_md.py    # Docling processing
python scripts/validation/hitl_pipeline/stage3b_problem_schema_validation.py # Schema validation
python scripts/validation/hitl_pipeline/stage4_object_validation.py      # Object validation
```

### Test Manually
```bash
# Test HITL components manually
python tests/test_hitl_manually.py

# Run unit tests
python tests/unit/test_hitl_components.py
```

## HITL Development Workflow

The Human-In-The-Loop pipeline validates DUX object definitions through 4 stages:

1. **Stage 1**: Structure validation (markdown template format)
2. **Stage 2**: Consistency validation (content checks)
3. **Stage 3a**: Docling processing (parse markdown to structured data)
4. **Stage 3b**: Schema validation (validate against DUX schemas)
5. **Stage 4**: Object instance validation

### Watch Folders Structure
```
watch_folders/
├── hitl_review/          # Entry point for new objects
├── hitl_review_queue/    # Queued by object type
├── hitl_workshop/        # Objects needing fixes
├── hitl_failed/          # Failed validation
├── hitl_rejected/        # Wrong naming convention
├── hitl_promotion_candidates/  # Passed all stages
└── hitl_approved_for_production/  # Final approved
```

### Object Naming Convention
Files MUST follow: `{object_type}_*_*_object_model_definition.md`

Examples:
- ✅ `problem_cost_optimization_v1_object_model_definition.md`
- ❌ `problem_object.md` (missing suffix)

## Architecture Overview

### Current Focus: dux-object-model-core
This repository handles the **object model governance** - the schema definitions and validation pipeline for DUX objects.

### Key Components
- **Canonical Vault**: Approved object model definitions organized by type
- **Features**: BDD test scenarios using Gherkin syntax
- **Scripts**: Validation, docling processing, and HITL orchestration
- **Src**: Schemas, prompts, and component definitions
- **Watch Folders**: HITL pipeline queue management

### Object Types (v9.6)
Core Objects: Problem, Behavior, Result, Flow, UserOutcome
Research Objects: Data, Frame, Session, Insight
Junction Objects: Evidence, Provenance, Insight junctions
Collections: Report, Report Gallery, Study

## Schema Architecture

### Markdown-First Approach
DUX uses markdown files as the canonical source of truth:
- **Canonical**: `canonical_vault/{category}/{object_type}/*.md`
- **Generated**: JSON schemas auto-generated from markdown
- **Philosophy**: Human-readable definitions that generate validation contracts

### Problem Object Structure (v9.6)
```json
{
  "job_statement": {
    "user_scenario": {"value": "string", "source": "evidence|synthetic"},
    "user_enablement": {"value": "string", "source": "evidence|synthetic"},
    "user_outcome": {"value": "string", "source": "evidence|synthetic"}
  }
}
```

## Development Principles

### Natural Language Centricity
- Markdown-first documentation and schemas
- JSON schemas are generated artifacts for validation
- Human readability and AI collaboration are primary

### Evidence-Based Validation
- Every object requires evidence attribution
- Quality scoring and completeness metrics
- Cross-object relationship validation

### HITL Pipeline Philosophy
- Fail fast with clear error messages
- Route to appropriate queues based on failure type
- Maintain single canonical definition per object type

## Key Dependencies
- **Python**: behave, jsonschema, docling, langchain, neo4j
- **Testing**: BDD with Behave framework
- **Processing**: Docling for markdown parsing
- **Validation**: JSON Schema compliance

## Backlog System

Three documentation streams for continuous improvement:

1. **INFRASTRUCTURE_INSIGHTS_BACKLOG.md**: System patterns, architectural insights
2. **COACHING_BACKLOG.md**: Teaching moments, skill growth opportunities
3. **Architecture Docs** (`docs/architecture/`): ADRs and system boundaries

## Integration Points

- Generates schemas consumed by **dux-research-platform**
- Validates objects created by **duckie** CLI
- Provides canonical definitions for all DUX components
- Exports validated objects to downstream systems