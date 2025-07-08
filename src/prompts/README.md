# DUX Prompts Directory - Unified Location

This is the **canonical location** for all DUX prompts. All prompts have been consolidated here to maintain a single source of truth.

## Directory Structure

```
src/prompts/
├── agents/          # Agent-specific prompts for extraction
├── templates/       # Object template prompts  
└── library/         # Archived and experimental prompts
```

## Prompt Types

### 🤖 Agent Prompts (`/agents/`)
Prompts that define agent behavior for object extraction:
- `problem_agent_prompt.md` - Erin Brockovich-style Problem extraction
- `behavior_agent_prompt.md` - Behavior object extraction
- `result_agent_prompt.md` - Result object extraction
- `archivist_prompt.md` - Evidence and provenance tracking
- `advocate_prompt.md` - User advocacy agent
- `dev_manager_agent_prompt.md` - Development coordination

### 📝 Template Prompts (`/templates/`)
Schema-based templates for each object type:
- `problem_prompt.md` - Problem object template
- `behavior_prompt.md` - Behavior object template
- `result_prompt.md` - Result object template
- `useroutcome_prompt.md` - UserOutcome object template
- `flow_prompt.md` - Flow object template
- `provenance_prompt.md` - Provenance object template
- `insight_prompt.md` - Insight object template

### 📚 Prompt Library (`/library/`)
Historical and experimental prompts:
- Canvas archives - Previous prompt iterations
- Persona experiments (Columbo, Beane, etc.)
- Architecture prompts

## Usage Guidelines

1. **Natural Language First**: All prompts should prioritize human readability
2. **Schema Compliance**: Templates must align with canonical object schemas
3. **Version Control**: Use git history for prompt evolution tracking
4. **No Duplication**: This is the ONLY location for prompts

## Prompt Generation Flow

```
Canonical Object Definition (Markdown)
    ↓
Schema Generation
    ↓
Template Prompt Generation
    ↓
Agent Prompt Contextualization
```

## Migration Notes

All prompts have been migrated from:
- `/workspace/agent_prompts/` → `/agents/`
- `/workspace/src/prompt_templates/` → `/templates/`
- `/workspace/docs/97_prompt_library/` → `/library/`
- Various scattered locations → appropriate subdirectory

Last consolidation: 2025-01-08
Maintained by: Dev Manager Agent