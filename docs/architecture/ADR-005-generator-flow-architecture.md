# ADR-005: Generator Flow Architecture

## Status
**WIP** (Work in Progress)

## Date
2025-01-15

## Context
The system needs a systematic way to generate prompts, API contracts, and microservice definitions from canonical object definitions. Without a clear generator flow, prompts become inconsistent and drift from canonical sources.

## Decision
Implement a generator flow that transforms canonical markdown definitions into executable artifacts.

### Generator Flow Pipeline
```
Canonical Definitions (markdown) 
  ↓ [docling processing]
Schema Attributes Extraction
  ↓ [explosion process]
Exploded Attribute Objects
  ↓ [prompt generation]
Frame-Aware Prompt Canvas
  ↓ [API contract generation]
Component API Contracts
```

### Key Components

#### 1. Docling Document Processing
- **Breakthrough**: Use `table.data.grid` to access structured table data
- **Process**: Extract Schema Attributes table from canonical markdown
- **Output**: Structured attribute definitions with types and descriptions

#### 2. Exploded Attribute Objects
- **Pattern**: Each attribute becomes an independent microservice
- **Structure**: 
  ```javascript
  {
    "attribute_name": "job_statement",
    "parent_object": "Problem",
    "schema": {validated_from_canonical},
    "canonical_example": {from_approved_definition},
    "validation_rules": {derived_from_schema},
    "relationship_context": "core_attribute_of_problem_object"
  }
  ```

#### 3. Frame-Aware Prompt Generation
- **Core API**: `/api/objects/{type}/generate` with Frame payload
- **Input**: Frame context + canonical definition
- **Output**: DoclingDocument with embedded JSON prompt canvas
- **Format**: Structured markdown with embedded JSON schemas and examples
- **Features**: Frame-specific examples, agent instructions, schema validation

**API Response Format (Docling Markdown + Embedded JSON):**
```markdown
# Problem Object Definition

## Schema Attributes
[Structured table with field definitions]

## Canonical Example
```json
{
  "object_type": "Problem",
  "job_statement": {
    "user_scenario": "When managing GPU resources",
    "user_enablement": "I want visibility",
    "user_outcome": "so I can optimize"
  }
}
```

## Frame-Aware Agent Instructions
[Character prompt with Frame context and embedded JSON examples]
```

This enables:
- **Structured parsing** by extraction agents
- **Schema validation** from embedded JSON
- **Frame-specific examples** in consumable format
- **Docling processing** of structured content

#### 4. API Contract Generation
- **Source**: Canonical Schema Attributes table
- **Process**: Generate contracts for each component type (table-row, grid-card, detail-page)
- **Output**: Precise field specifications with typography rules

### Generator Locations (Current State)
Multiple scattered locations requiring consolidation:
- `scripts/prompts_from_markdown/` (8 files) - Most complete set
- `src/prompt_templates/` (7 files) - Current target
- `docs/97_prompt_library/` (3 files) - User handling
- `src/generators/scripts/prompts_from_markdown/` (6 files) - Partial set

### Canonical → Generator → Prompt Flow
1. **Canonical Vault**: Approved object definitions in markdown
2. **Docling Parser**: Extracts structured data from markdown tables
3. **Attribute Explosion**: Creates microservice-ready attribute objects
4. **Prompt Canvas**: Frame-aware prompt generation with current schema
5. **API Contracts**: Component-specific data requirements

### Schema Propagation
When canonical definitions change, they automatically propagate to:
- JSON schema files (validation pipeline)
- Prompt templates (agent instructions)
- API contracts (component specifications)
- Test data samples (validation examples)

**This eliminates manual schema synchronization across 100+ files.**

## Consequences
### Positive
- Single source of truth for all generated artifacts
- Automatic propagation prevents schema drift
- Frame-aware prompts provide contextual extraction
- Exploded attributes enable microservice architecture
- Docling processing provides structured data extraction

### Negative
- Complex generation pipeline requires maintenance
- Multiple generation targets increase complexity
- Dependency on docling processing stability
- Requires careful management of generation order

## Implementation (WIP)
### Immediate Tasks
- [ ] Consolidate scattered prompt locations into unified `src/prompts/`
- [ ] Fix broken docling parser with `table.data.grid` approach
- [ ] Implement canonical → explosion → prompt pipeline
- [ ] Create Frame-aware prompt generation API
- [ ] Build automatic schema propagation system

### Open Questions
- **Canonical Directory Structure**: Where do exploded attributes live permanently?
- **Generation Timing**: Pre-approval explosion vs post-approval explosion?
- **Integration Points**: How do generated prompts integrate with extraction pipeline?
- **Versioning**: How do we version generated artifacts vs canonical sources?

### Dependencies
- P0.2: Move schemas to `src/dux_v9.6_split_schema/`
- P0.3: Consolidate prompt locations
- P0.4: Establish single entry point for generation pipeline
- DoclingDocument processing fix from workshop

## Notes
This ADR captures the generator flow architecture but requires further refinement as the implementation progresses. The "WIP" status indicates ongoing development of this critical system component.