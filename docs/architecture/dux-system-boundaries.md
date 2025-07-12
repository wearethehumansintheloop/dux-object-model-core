# DUX System Architecture: Separation of Concerns

**Document Type**: Architecture Decision Record  
**Created**: 2025-07-07  
**Status**: Draft  
**Session**: docling-schema-validation-session  

## Overview

This document defines the architectural boundaries between DUX Object Model Core and DUX Research Platform, establishing clear separation of concerns to prevent scope creep and enable independent evolution.

## System Boundaries

### DUX Object Model Core (Governance)
**Primary Responsibility**: Schema governance and object definition management

**Owns:**
- Object schema definitions and validation rules
- DUX object template compliance
- Schema generation from markdown definitions
- Object definition versioning and promotion workflow
- "Lego piece interface" validation (field types, required fields)
- Canonical object examples and documentation

**Does NOT Own:**
- Object instance creation from real data
- Relationship population between specific object instances
- Business logic for object relationships
- Data extraction from sources (transcripts, surveys, etc.)
- Analytics or synthesis across object instances

**Key Artifacts:**
- Schema JSON files
- Object definition markdown templates
- Validation scripts (Stages 1-4)
- HITL governance workflow
- Docling schema generation pipeline

---

### DUX Research Platform (Extraction & Synthesis)
**Primary Responsibility**: Object instance lifecycle and research operations

**Owns:**
- Object instance creation from data sources
- DUX-opinionated relationship logic between instances
- magents.py extraction orchestration
- Evidence-to-object mapping and population
- Neo4j knowledge graph storage and querying
- Research workflow execution
- Cross-object analytics and pattern discovery
- Report generation and insight synthesis

**Does NOT Own:**
- Schema structure definitions
- Object template validation
- Schema versioning or promotion workflows
- Canonical object examples

**Key Artifacts:**
- Object instances in Neo4j
- Extraction agents and orchestration
- Research workflow implementations
- Analytics and reporting engines
- Vector embeddings and search

---

## Data Flow & Handoff Points

### Schema Definition Flow
```
Object Model Core → Research Platform
1. Schema definitions (JSON) → magents.py validation rules
2. Canonical examples → extraction agent templates
3. Validation rules → instance quality checks
```

### Instance Creation Flow
```
Research Platform → Object Model Core (feedback loop)
1. Extraction patterns → schema enhancement requests
2. Instance validation failures → schema refinement needs
3. Relationship patterns → interface requirement updates
```

## Interface Contracts

### Core → Platform
- **Schema JSON**: Production-ready JSON schemas for validation
- **Canonical Examples**: Reference implementations for extraction
- **Validation Rules**: Programmatic validation logic
- **Template Changes**: Notification of schema evolution

### Platform → Core
- **Schema Feedback**: Enhancement requests from extraction experience
- **Validation Failures**: Instance-level failures requiring schema updates
- **Pattern Discovery**: New relationship patterns requiring interface changes

## Responsibility Matrix

| Concern | Object Model Core | Research Platform |
|---------|------------------|------------------|
| Schema Structure | ✅ Owns | ❌ Consumes |
| Object Instances | ❌ Examples Only | ✅ Owns |
| Field Validation | ✅ Schema Rules | ✅ Instance Data |
| Relationships | ✅ Interface Definition | ✅ Instance Population |
| Evidence Mapping | ✅ Schema Support | ✅ Actual Mapping |
| Template Compliance | ✅ Owns | ❌ Follows |
| Business Logic | ❌ Schema Only | ✅ Owns |
| Analytics | ❌ Not Applicable | ✅ Owns |

## Evolution Paths

### Current State (Army of Two)
- Monolithic validation in Core
- Shared development context
- Direct coordination possible

### Scale Transition (Team Growth)
- API boundaries become critical
- Formal handoff procedures needed
- Independent deployment cycles

### Microservice Future (Enterprise Scale)
- Each object type becomes service
- Event-driven coordination
- Distributed schema management

## Decision Rationale

### Why This Separation?
1. **Single Responsibility**: Each system has one primary concern
2. **Independent Evolution**: Schema and extraction can evolve separately
3. **Scope Prevention**: Clear boundaries prevent feature creep
4. **Team Scaling**: Enables independent team ownership
5. **Technical Debt**: Prevents monolithic coupling

### Key Architectural Principles
- **Governance ≠ Operations**: Schema rules vs instance management
- **Interface Focus**: Define connectors, not connections
- **Evidence Separation**: Schema support vs actual evidence processing
- **Template Centrality**: Core owns the "how to define", Platform owns the "how to extract"

## Implementation Notes

### Validation Pipeline Stages
- **Stages 1-2**: Universal template validation (Core responsibility)
- **Stages 3-4**: Object-specific processing (Core responsibility, Platform consumption)
- **Instance Validation**: Runtime validation (Platform responsibility)

### Schema Evolution Workflow
1. Enhancement identified during extraction (Platform)
2. Schema change proposed (Platform → Core)
3. Schema updated and validated (Core)
4. New schema consumed (Core → Platform)
5. Extraction updated (Platform)

---

**Next Review**: After microservice decomposition planning
**Stakeholders**: Core team, Platform team, Architecture review board