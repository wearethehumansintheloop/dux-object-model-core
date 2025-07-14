# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Core Framework

**Declarative UX (DUX)** is an AI-powered framework that transforms UX research into executable, testable code. The system decomposes all software artifacts into three molecular components: **Problems**, **Behaviors**, and **Results**.

## Architecture Overview

The framework consists of four main modules:

### 1. dux-object-model-core (this repository)
- **Schema Foundation**: JSON schemas for DUX objects (v9.6 current)
- **Object Types**: Problem, Behavior, Result, Flow, UserOutcome, Provenance, Insight, Data, Evidence/Provenance/Insight Junctions, Frame, Report, Report Gallery, Session, Study
- **Validation Pipeline**: Multi-layer validation with schema, quality, and integrity checks
- **BDD Framework**: Behave-based testing using Gherkin syntax

### 2. dux-research-platform
- **Neo4j Knowledge Graph**: Stores and queries DUX objects
- **Multi-Service Architecture**: Bot (8501), Loader (8502), PDF Bot (8503), API (8504), CSV Bot (8506)
- **LLM Integration**: Supports Ollama, OpenAI, Claude, and other models
- **RAG Pipeline**: Vector embeddings with semantic search

### 3. duckie
- **CLI Orchestrator**: Converts user scenarios into BDD tests and GitHub issues
- **Core Commands**: `teach-me-how-to-duckie`, `drop`, `check`, `push`, `remix`
- **Dual Parsing**: Simple parsing and LLM-enabled parsing modes

### 4. dux-white-label-ui
- **Frontend Interface**: Next.js/React UI connecting to API at port 8504
- **Integration**: Connects to research platform backend

## Common Development Commands

### Environment Setup
```bash
# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows

# Install dependencies
pip install -r requirements.txt
```

### Testing Commands
```bash
# Run all BDD tests
behave features/

# Run specific feature file
behave features/dux_schema_validation.feature

# Run research platform validation tests
behave features/dux_research_platform_validation.feature

# Run a single test scenario by name
behave features/dux_schema_validation.feature -n "Validate Problem object schema"

# Run with specific format output
behave features/ -f plain
behave features/ -f progress

# Run HITL pipeline tests
./scripts/test_hitl_pipeline.sh
```

### HITL Validation Pipeline
```bash
# Run complete HITL orchestrator (all 4 stages)
python scripts/validation/hitl_pipeline/hitl_orchestrator.py

# Run individual validation stages
python scripts/validation/hitl_pipeline/stage1_structure_validation.py  # Markdown structure
python scripts/validation/hitl_pipeline/stage2_consistency_validation.py # Content consistency
python scripts/validation/hitl_pipeline/stage3a_problem_basic_docling.py # Docling processing

# Run final object validation
python scripts/validation/validate_dux_objects.py

# Run bulk validation on JSON objects
python scripts/validation/run_bulk_validation.py <input_json_path>
```

### Governance Commands
```bash
# Run individual object type validations
python scripts/validation/validate_behavior_objects.py
python scripts/validation/validate_flow_objects.py
python scripts/validation/validate_insight_objects.py
python scripts/validation/validate_problem_objects.py
python scripts/validation/validate_provenance_objects.py
python scripts/validation/validate_result_objects.py
python scripts/validation/validate_useroutcome_objects.py
```

### Object Extraction Pipeline
```bash
# Extract DUX objects from a transcript
python src/app/orchestrators/dux_processor.py <transcript_path> \
    --fit-template <fit_template_path> \
    --output-dir ./extraction_results \
    --llm llama3

# Test the extraction pipeline
python scripts/test_pipeline.py
```

### Schema Management
```bash
# Generate prompts from markdown schemas
python src/generators/generate_from_markdown.py

# Generate synthetic data from schemas
python src/generators/generate_synthetic_data.py
```

## Markdown-First Schema Governance

**CRITICAL**: DUX uses a **markdown-first** approach where human-readable schema definitions are the canonical source of truth:

- **Canonical Source**: Markdown files in approved locations (see documentation)
- **Generated Artifacts**: JSON schemas are auto-generated from markdown
- **Philosophy**: Schemas evolve with research - markdown enables rapid iteration while maintaining validation

### Generation-First Principle (CRITICAL)
- **NEVER manually create or edit**: JSON schemas, validation scripts, prompts
- **ALWAYS generate from**: Approved docling markdown files
- **Flow**: Markdown → Docling → Generated Artifacts
- **If something is wrong**: Fix the markdown source, regenerate
- **If you find outdated files**: Archive them, don't fix them

### Problem Object Schema Updates (Critical)
The Problem object now uses a **decomposed job_statement** structure:
```json
{
  "job_statement": {
    "user_scenario": {"value": "string", "source": "evidence|synthetic"},
    "user_enablement": {"value": "string", "source": "evidence|synthetic"},
    "user_outcome": {"value": "string", "source": "evidence|synthetic"}
  }
}
```

## HITL Development Pipeline

### Four-Stage Validation Pipeline

1. **Stage 1: Structure & Template Validation** (`stage1_structure_validation.py`)
   - Validates markdown follows DUX object template format
   - Checks required sections and Schema Attributes table
   - Fail → `hitl_failed/`

2. **Stage 2: Consistency Validation** (`stage2_consistency_validation.py`)
   - Validates content consistency and completeness
   - Checks field descriptions match types
   - Fail → `hitl_failed/`

3. **Stage 3: Docling Processing & Schema Generation**
   - **Stage 3a**: Creates docling markdown (canonical source)
   - **Stage 3b**: Validates schema definition against canonical requirements
   - Uses docling to parse markdown structure (requires host machine installation)
   - Extracts schema from tables using `table.data.grid` approach
   - Fail → `hitl_workshop/`

4. **Stage 4: Generation & Final Validation**
   - **GENERATES validation scripts FROM docling markdown**
   - **GENERATES JSON schemas FROM docling markdown**
   - **GENERATES prompts FROM approved schemas**
   - All artifacts are OUTPUT, not INPUT
   - Pass → `hitl_promotion_candidates/`
   - Fail → `hitl_failed/`

### HITL Directory Structure
```
watch_folders/
├── hitl_review/                    # Current validation target (ONE AT A TIME)
├── hitl_review_queue/              # Queued objects by type
│   ├── problem_objects/
│   ├── behavior_objects/
│   ├── result_objects/
│   └── other_objects/
├── hitl_promotion_candidates/      # Passed validation
├── hitl_approved_for_production/   # Human-approved
├── hitl_failed/                    # Failed validation
├── hitl_rejected/                  # Failed naming convention
└── hitl_workshop/                  # Stage 3 failures for improvement
```

### Object Naming Convention (STRICT)
Files MUST follow this pattern to enter the validation pipeline:
```
{object_type}_*_*_object_model_definition.md
```
Examples:
- ✅ `problem_cost_optimization_v1_object_model_definition.md`
- ✅ `behavior_resource_monitoring_v2_object_model_definition.md`
- ❌ `platform_engineer_001.md` (wrong pattern)

### Single Object Governance Rule
**ONE canonical definition per object type** in the system. The queue management system ensures only one object of each type is processed at a time.

## High-Level Architecture

### Core Components

1. **Object Model (v9.6)** - Seven primary object types:
   - **Problem Objects**: Strategic jobs-to-be-done defining market opportunities
   - **Behavior Objects**: Atomic, testable user actions (instrumentation anchors)
   - **Result Objects**: Measurable outcomes users achieve
   - **User Outcome Objects**: Human impact and value delivered
   - **Flow Objects**: Sequences of behaviors forming user journeys
   - **Insight Objects**: Synthesized patterns from research data
   - **Provenance Objects**: Evidence tracking and source attribution

2. **Processing Pipeline**:
   - **LLM Extraction**: Uses LangChain with Ollama/OpenAI to extract objects
   - **Fit Scoring**: Evaluates objects against project-specific fit templates
   - **Schema Validation**: JSON Schema-based validation for all objects
   - **HITL Workflow**: Human-in-the-loop review for quality assurance

3. **Validation System**:
   - Pure governance layer that validates but doesn't auto-correct
   - Four-stage pipeline with discrete validation scripts
   - Detailed error logging with remediation guidance
   - Queue management with auto-pull logic

### Key Design Principles

1. **Markdown-First**: Human-readable schemas are canonical source
2. **Evidence-Based**: Every object requires supporting quotes and provenance
3. **Atomic Operations**: Objects processed independently for fault tolerance
4. **Governance-First**: Strict validation without auto-correction
5. **Human-in-the-Loop**: Manual approval required for production changes

## Development Workflow

### Typical Development Flow
1. **Research Input**: User scenarios, protocols, qualitative data
2. **AI Processing**: LLM parsing and structuring
3. **Object Generation**: Structured DUX objects with validation
4. **HITL Review**: Four-stage validation pipeline
5. **Artifact Generation**: AUTO-GENERATE schemas, validators, prompts from docling
6. **Human Approval**: Manual review for production deployment
7. **Storage**: Neo4j knowledge graph with vector embeddings

### Generation Flow (Required)
1. Markdown object definition (human-edited)
2. → Docling processing (Stage 3a)
3. → Schema validation (Stage 3b)
4. → AUTO-GENERATE: JSON schemas, validation scripts, prompts
5. → NEVER hand-edit generated artifacts

### Testing Strategy
- **BDD Features**: Business logic validation in Gherkin
- **Schema Tests**: JSON schema compliance
- **Relationship Tests**: Inter-object reference validation
- **Evidence Tests**: Provenance tracking verification

### Slow Bullet Mode (Required)
**Take one atomic unit of work at a time. Don't jump steps or assume context.**

Core principles:
- **One atomic unit per interaction** - Focus on a single Problem, Behavior, or Result
- **Confirm alignment before continuing** - Get explicit confirmation before proceeding
- **Show structure before content** - Present outlines before generating full implementations
- **Ask clarifying questions first** - Understand intent before producing output

## Triple Backlog System

The project maintains three documentation streams:

### 1. INFRASTRUCTURE_INSIGHTS_BACKLOG.md
- **Purpose**: Capture repeatable patterns, prompt evolution, infrastructure improvements
- **Location**: `/docs/infrastructure_as_code/INFRASTRUCTURE_INSIGHTS_BACKLOG.md`

### 2. COACHING_BACKLOG.md
- **Purpose**: Capture teaching moments, craft improvement, redline guidance
- **Location**: Root directory (when created)

### 3. Architecture Documentation
- **Purpose**: System boundaries, architectural decisions
- **Location**: `/docs/` various subdirectories

### Backlog Entry Format
```markdown
### [Insight Title]
**Type**: Coaching | Encoding | Architecture
**Timestamp**: YYYY-MM-DDTHH:MM:SSZ
**Context**: [Triggering moment]
**Description**: [Detailed explanation]
**Next Step**: [Follow-up action]
```

## Integration Points

- **Duckie CLI** generates objects consumed by **Object Model Core**
- **Research Platform** stores and queries objects in **Neo4j**
- **Validation Pipeline** ensures quality across all modules
- **Frontend** provides visual interface to research data
- **GitHub Integration** for issue tracking and PR automation

## Environment Configuration

### Required Environment Variables
```bash
# LLM Configuration (for extraction)
OLLAMA_BASE_URL=http://localhost:11434
LLM=llama3
EMBEDDING_MODEL=sentence_transformer

# Output directories
OUTPUT_DIR=./extraction_results
```

## Git Workflow Recommendations

### Current Branch Status
- **main**: Stable, up to date
- **feature/hitl-docling-breakthrough**: Contains DoclingDocument processing fixes
- **handoff-research-platform**: 20+ commits with HITL improvements (cherry-pick recommended)
- **dux-governance**: DO NOT MERGE - unrelated history, 336 conflicts

### Cherry-Pick Strategy
```bash
# Review commits to cherry-pick
git log main..handoff-research-platform --oneline

# Cherry-pick valuable commits individually
git checkout main
git cherry-pick <commit-hash>
# Test after each cherry-pick
```

## Dev Manager Support

When overwhelmed with complexity, summon Brid (the dev manager agent):
- Helps prioritize tasks using Occam's razor
- Identifies essential vs nice-to-have features
- Provides clear next steps
- Located at: `src/prompts/agents/dev_manager_agent_prompt.md`

## Important Conventions

### File Naming
- Validation scripts: `validate_<object_type>_objects.py` (GENERATED, not hand-written)
- Object files: `<object_type>_<identifier>_object_model_definition.md`
- Error logs: `<timestamp>_<filename>_errors.txt`

## ❌ Common Mistakes to Avoid

1. **Manually fixing validation scripts** - Archive and regenerate from docling
2. **Editing JSON schemas directly** - Edit markdown source, regenerate
3. **Creating prompts by hand** - Generate from approved schemas
4. **Assuming existing files are correct** - Check if generated from current docling
5. **Trying to "fix" outdated code** - Archive it, generate fresh

### Evidence Array Structure
```json
{
  "quote": "Supporting statement from research",
  "attribution": "Source or participant name",
  "participant_id": "P001",
  "source_file": "research/interviews/session.md"
}
```

### Queue Management
- One object per type in review folder
- Auto-pull from queue after processing
- FIFO ordering within type queues
- Manual approval required for production

## DoclingDocument Processing Breakthrough

**CRITICAL FIX**: The DoclingDocument processing now correctly uses `table.data.grid` to extract structured data from markdown tables, replacing the broken regex-based approach.

### Key Discovery
- DoclingDocument stores tables as `table.data.grid` containing TableCell objects
- Successfully extracts Schema Attributes table using structured access
- Generates exploded attribute objects (14 from Problem object)
- Fixed parser at: `watch_folders/hitl_workshop/fixed_docling_parser.py`

### Integration Status
- ✅ HITL Activity 1 Complete - Workshop parser proven
- 🔄 Activity 2 Pending - Canonical workflow decisions needed
- 📋 P0.3 Audit Complete - 5+ scattered prompt locations documented
- 🚀 Feature Branch Ready - `fix/docling-document-processing`

## Prompt Consolidation (P0.3)

**DISCOVERED: 5+ scattered prompt locations requiring consolidation**

1. `docs/97_prompt_library/` - User handling solution in progress
2. `scripts/prompts_from_markdown/` - Most complete set
3. `src/prompt_templates/` - Current target referenced by generators
4. `src/generators/scripts/prompts_from_markdown/` - Partial set
5. Embedded in Python files - Significant logic in generator scripts
6. `test_data/` - Test data, not active prompts

**Consolidation Strategy**: Create unified `src/prompts/` directory structure

## Project Memories

- Markdown is source code - treat it with same rigor as other code
- HITL workflow only accepts .md files in review folder
- Validation pipeline has discrete stages with specific failure routing
- Human approval is NEVER automated for production deployment
- BDD tests prevent regression and validate workflows
- Stage 3a requires docling installed on host machine (not just container)
- DoclingDocument `table.data.grid` is the key to structured data extraction
- Research platform validation tests moved from "DUX Object Model (Core)" folder to main features/
- **ALL validation scripts are GENERATED from docling - NEVER manually created**
- **If validation script has wrong schema - archive it and regenerate**
- **Generation-first principle: If it can be generated, it MUST be generated**
- Coauthored by imstilllearning (noreply@duckie.ernt) and claudette xoxo
