# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**DUX Object Model Core** is an open-source framework for transforming qualitative UX research data into structured, testable, and executable design specifications. It implements a declarative approach to UX design through seven core object types: Problem, Behavior, Result, User Outcome, Flow, Insight, and Provenance.

## Common Development Commands

### Environment Setup
```bash
# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
# or
venv\Scripts\activate  # On Windows

# Install dependencies
pip install -r requirements.txt
```

### Testing
```bash
# Run all BDD tests
behave features/

# Run specific feature file
behave features/dux_schema_validation.feature -f plain

# Run a single test scenario
behave features/dux_schema_validation.feature -n "Scenario name"
```

### Validation and Governance
```bash
# Run all governance validations (master script)
python scripts/governance/run_all_governance.py

# Run bulk validation on JSON objects
python scripts/validation/run_bulk_validation.py <input_json_path>

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

# Test the extraction pipeline with predefined test data
python scripts/test_pipeline.py
```

### Schema Management
```bash
# Update schemas to new version
python scripts/update_schemas.py

# Generate prompts from updated schemas
python scripts/update_prompts_with_schema.py
python scripts/generate_notebooklm_prompts.py
```

## High-Level Architecture

### Core Components

1. **Object Model (v9.6)** - Seven interconnected object types:
   - **Problem Objects**: Strategic jobs-to-be-done defining market opportunities
   - **Behavior Objects**: Atomic, testable user actions (instrumentation anchors)
   - **Result Objects**: Measurable outcomes users achieve
   - **User Outcome Objects**: Human impact and value delivered
   - **Flow Objects**: Sequences of behaviors forming user journeys
   - **Insight Objects**: Synthesized patterns from research data
   - **Provenance Objects**: Evidence tracking and source attribution

2. **Processing Pipeline**:
   - **LLM Extraction**: Uses LangChain with Ollama/OpenAI to extract objects from transcripts
   - **Fit Scoring**: Evaluates objects against project-specific fit templates
   - **Schema Validation**: JSON Schema-based validation for all objects
   - **HITL Workflow**: Human-in-the-loop review for quality assurance

3. **Validation System**:
   - Pure governance layer that validates but doesn't auto-correct
   - Schema compliance checking
   - Evidence structure validation
   - Duplicate handling
   - Detailed error logging

### Key Design Principles

1. **Schema-Driven**: All objects must pass JSON schema validation
2. **Evidence-Based**: Every object requires supporting quotes and provenance
3. **Atomic Operations**: Objects processed independently for fault tolerance
4. **Governance-First**: Strict validation without auto-correction
5. **Human-in-the-Loop**: Review workflow for quality assurance

### Directory Structure

```
/workspace/
├── object_schemas/           # Current v9.6 JSON schemas
├── object_definitions/       # Markdown documentation for each object type
├── agent_prompts/           # LLM prompts for object extraction
├── scripts/
│   ├── validation/          # Individual object validation scripts
│   ├── governance/          # Master governance runner
│   └── utilities/           # Shared utilities
├── features/                # BDD test scenarios (Gherkin)
│   └── steps/              # Step definitions for tests
├── src/
│   ├── app/orchestrators/   # Main processing pipeline
│   └── prompt_templates/    # Schema-based prompt generation
├── extraction_pipelines/    # LLM-based extraction logic
└── watch_folders/          # HITL review workflow
    ├── hitl_review/        # Drop candidate objects here
    ├── hitl_failed/        # Quarantined invalid objects
    └── hitl_approved/      # Validated objects
```

### Development Workflow

1. **Research Data Processing**:
   - Upload transcript to extraction pipeline
   - LLM extracts DUX objects with fit scoring
   - Objects saved to `watch_folders/hitl_review/`

2. **Validation Pipeline**:
   - Run validation scripts on review folder
   - Invalid objects → `hitl_failed/` with error logs
   - Valid objects → ready for canonical storage

3. **Evidence Requirements**:
   - Every object needs a provenance_id
   - Teaser quote object with attribution
   - Source file reference

### Error Handling Patterns

- Validation scripts create timestamped backups
- Failed objects quarantined with detailed error logs
- Duplicate handling prevents reprocessing
- Clear error messages guide corrections

### Testing Strategy

- **BDD Features**: Business logic validation in Gherkin
- **Schema Tests**: JSON schema compliance
- **Relationship Tests**: Inter-object reference validation
- **Evidence Tests**: Provenance tracking verification

### Important Conventions from Cursor Rules

1. **File Naming**: 
   - Validation scripts: `validate_<object_type>_objects.py`
   - Object files: `<object_type>_<identifier>.json`

2. **Schema Management**:
   - Always create backups before updating
   - Run BDD tests after schema changes
   - Use semantic versioning

3. **Evidence Array Structure**:
   ```json
   {
     "quote": "Supporting statement from research",
     "attribution": "Source or participant name",
     "participant_id": "P001",
     "source_file": "research/interviews/session.md"
   }
   ```

4. **Performance Considerations**:
   - Process objects in batches
   - Implement duplicate handling
   - Cache frequently accessed schemas

### Integration Points

- **LangChain**: LLM orchestration
- **Ollama/OpenAI**: Object extraction
- **Neo4j**: Graph database for relationships (future)
- **Milvus**: Vector embeddings (future)
- **Watchdog**: File monitoring for HITL workflow