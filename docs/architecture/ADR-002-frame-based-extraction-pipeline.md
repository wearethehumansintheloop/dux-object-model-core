# ADR-002: Frame-Based Extraction Pipeline

## Status
Accepted

## Date
2025-01-15

## Context
The research platform needed a systematic way to extract structured DUX objects from unstructured research data. Previous manual extraction processes were inconsistent and didn't scale.

## Decision
Implement a Frame-based extraction pipeline using character-driven agents with think-aloud protocols.

### Character Agent Architecture
- **Archivist**: Creates Data objects from transcript chunks
- **Advocate (Erin Brockovich)**: Extracts Problem objects with JTBD format
- **Columbo**: Identifies observable Behavior objects with signals
- **Beane (Billy Beane)**: Defines measurable Result objects with success criteria

### Think-Aloud Protocol
Agents use screenplay-style reasoning for explainability:
```
ADVOCATE (V.O)
[Character reasoning about the evidence]
[Analysis of why this is a problem]
[END SCENE]
{
  "problems": [extracted_objects]
}
```

### Frame-Aware Prompt Generation
- **Core API** generates Frame-specific prompts via `/api/objects/{type}/generate`
- **Orchestration Agent** manages pipeline triggers and agent coordination
- **Canonical Source**: All prompts generated from canonical object definitions

### Revised Evidence Architecture
1. **NO SESSION OBJECT, NO Provenance Object** - Data holds its own 'Session Attribute'
2. **Data × DUX Core Object = Frame Junction Object** (unique attribute: Protocol Attribute)
3. **Data × Frame = Evidence Junction Object** (many-to-many)
4. **Evidence × Frame = Insight Junction Object** (many-to-many)
5. **Universal Evidence Attribute** - Every CORE OBJECT & JUNCTION OBJECT has evidence attribute containing: IDs, pull quote/teaser, reference context, timestamp, attribution/citation

## Consequences
### Positive
- Consistent extraction quality through character-driven reasoning
- Full traceability through evidence attributes on every object
- Explainable AI through think-aloud protocols
- Scalable Frame-based approach for different research contexts

### Negative
- Complex pipeline coordination between multiple agents
- Dependency on LLM context window management
- Requires character prompt maintenance

## Implementation
- Build Orchestration Agent for pipeline management
- Create character-specific prompt templates
- Implement Frame-aware prompt generation API
- Integrate with context window monitoring system