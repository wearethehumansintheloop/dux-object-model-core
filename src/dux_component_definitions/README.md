# DUX Component Definitions

## Overview
This directory contains the canonical component definitions for the DUX design system. These components are "hired" by DUX objects to present information in specific contexts.

## Core Concepts

### Components vs Objects
- **DUX Objects** (Problem, Behavior, Result) = The data/content
- **Components** = The presentation layer that displays object data
- Components don't own data, they specify which attributes to display and how

### Hiring Model
Each component can be "hired" by one or more object types to do a specific job:
- A Problem object might hire a Table Row to enable comparison
- The same Problem might hire a Detail Page to enable deep analysis
- Components are multi-purpose and context-aware

## Component Categories

### 1. Core Display Components
- **Table Row** - Scannable list views for comparison
- **Grid Card** - Visual discovery and browsing
- **Detail Page** - Deep dive with multiple layout options

### 2. Consulting Slide Layouts (via Detail Page)
- Matrix2x2 - Prioritization matrices
- DataVizSplit - Charts + analysis
- ProcessFlow - Sequential processes
- JourneyMap - Pain point analysis
- Timeline - Evolution over time
- SurveyDemographics - Evidence visualization
- InsightsMultiChart - Multi-metric comparisons
- TechStack - Architecture diagrams
- ComparativeAnalysis - Side-by-side metrics

## File Naming Convention
```
{object_type}_{display_type}_component.md
```
Examples:
- `problem_table_row_component.md`
- `behavior_process_flow_component.md`
- `result_insights_chart_component.md`

## Component Definition Structure

Each component definition includes:
1. **Component Overview** - ID, object type, purpose
2. **Job to be Done** - When/why this component gets hired
3. **Required Attributes** - Which object fields are needed
4. **Visual Hierarchy** - How information is prioritized
5. **Interaction Patterns** - User actions supported
6. **RAG Enrichment** - When/how to fetch additional data
7. **API Contract** - Exact endpoint and response format
8. **Performance Constraints** - Load time requirements
9. **Accessibility** - WCAG compliance specs
10. **Slide Template Compatibility** - Which layouts work with this data

## Governance

### Component definitions are:
- **Version controlled** - Follow semantic versioning
- **Validated** - Must comply with component schema
- **API contracts** - Define exact data requirements
- **Design tokens** - Reference DUX design system

### Change Process:
1. Update component definition in this directory
2. Version bump (major for breaking changes)
3. Update API to support new contract
4. Frontend implements based on spec
5. Validate generated output

## Current Status

### Completed:
- ✅ Problem object components (3 types)
- ✅ Component object model template

### In Progress:
- 🔄 Behavior object components
- 🔄 Result object components
- 🔄 Validation pipeline for components

### Planned:
- 📋 Flow object components
- 📋 UserOutcome object components
- 📋 Insight object components

## Integration Points

### API Service
Components drive API response shapes via Accept headers:
```
GET /api/objects/problems
Accept: application/vnd.dux.table-row+json
```

### Frontend
Components provide complete specs for implementation including:
- Exact attributes needed
- Visual treatments (bold/italic/colors)
- Responsive behaviors
- Interaction patterns

### Slide Generator
Detail page components include slide template mappings for auto-generation of presentation decks.

## Best Practices

1. **One job per component** - Each component should do one thing well
2. **Explicit attribute mapping** - Never assume which fields to use
3. **Performance first** - Specify load time targets
4. **Accessibility built-in** - Not an afterthought
5. **Version everything** - Components evolve like APIs

## Questions?
See CLAUDE.md for overall project context or contact the DUX Object Model Core team.