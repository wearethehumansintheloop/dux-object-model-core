# ADR-003: Context Window Management Strategy

## Status
Accepted

## Date
2025-01-15

## Context
LLMs frequently lose context during long extraction sessions, leading to redundant work, degraded quality, and "rework spirals" where the model keeps revising the same content without progress.

## Decision
Implement context window management through think-aloud log analysis and HITL pipeline boundaries.

### Context Degradation Detection
Think-aloud logs provide diagnostic capability to detect:
- Agent repeating earlier work
- Forgetting previously extracted objects
- Circular reasoning patterns
- Quality degradation over session length
- Generic reasoning replacing specific evidence attribution

### HITL as Context Boundaries
The Human-in-the-Loop pipeline serves dual purpose:
1. **Quality validation** of extracted objects
2. **Natural breakpoints** for context window management

Each HITL stage creates a natural session boundary that prevents context degradation.

### Automatic Session Chunking
When context degradation detected through think-aloud analysis:
1. Automatically chunk sessions at HITL stage boundaries
2. Prevent rework spiral where LLM keeps revising same content
3. Maintain extraction quality through fresh context windows

### Diagnostic Patterns
```
// Early in session (good context)
ADVOCATE (V.O): "The user explicitly states 'GPU costs are killing our budget' which is a clear problem..."

// Later in session (degraded context)  
ADVOCATE (V.O): "There seems to be a problem with resources... users need better management..."
[No specific quote, generic reasoning]
```

## Consequences
### Positive
- Early warning system for context exhaustion
- Quantifiable metrics for context health
- Prevents redundant LLM work and token waste
- Maintains consistent extraction quality

### Negative
- Additional monitoring overhead
- Complexity in detecting degradation patterns
- May require more human intervention in chunking

## Implementation
- Build context window monitoring dashboard
- Implement think-aloud log analysis for degradation detection
- Create automatic session chunking triggers
- Integrate with existing HITL pipeline stages