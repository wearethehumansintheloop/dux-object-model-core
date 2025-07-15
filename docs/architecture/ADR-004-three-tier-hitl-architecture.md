# ADR-004: Three-Tier HITL Architecture

## Status
Accepted

## Date
2025-01-15

## Context
The system needed clear separation of concerns for different types of human validation. A single HITL pipeline created confusion about responsibilities and led to validation chaos.

## Decision
Implement three distinct Human-in-the-Loop validation pipelines with clear ownership boundaries.

### 1. Object Model Governance HITL (dux-object-model-core)
- **Purpose**: Schema evolution and canonical definitions
- **Metaphor**: "Lego piece interfaces" - how objects should be structured
- **Queue**: `watch_folders/hitl_*` directories with 4-stage validation
- **Responsibility**: Ensuring object schemas are correct and consistent

### 2. Research Content HITL (dux-research-platform)
- **Purpose**: Instance validation and quality control
- **Metaphor**: "Lego building" - validating actual research instances
- **Process**: Frame-driven extraction with character agents
- **Responsibility**: Ensuring extracted research objects meet quality standards

### 3. Implementation Testing HITL (duckie)
- **Purpose**: BDD scenarios and GitHub integration
- **Metaphor**: "Lego instructions" - testing implementation scenarios
- **Output**: Behave tests and GitHub issues
- **Responsibility**: Ensuring implementation scenarios work as expected

### Separation Benefits
- Prevents validation chaos by clearly defining what each pipeline validates
- Creates clear ownership boundaries between teams
- Enables parallel validation workflows
- Scales to handle complexity of research platform with multiple use cases

### Pipeline Interactions
- **Core** provides canonical definitions to **Platform** for extraction
- **Platform** provides validated instances to **Duckie** for testing
- **Duckie** provides implementation feedback to **Core** for schema improvements

## Consequences
### Positive
- Clear separation of concerns prevents validation conflicts
- Scalable architecture for multiple teams and use cases
- Parallel validation workflows improve efficiency
- Clear ownership boundaries reduce confusion

### Negative
- Additional coordination complexity between pipelines
- Potential for gaps between pipeline boundaries
- More infrastructure to maintain

## Implementation
- Document clear responsibilities for each pipeline
- Create handoff protocols between pipelines
- Implement monitoring for pipeline health
- Build coordination mechanisms for cross-pipeline issues