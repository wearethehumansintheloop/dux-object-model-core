# ADR-001: Component Governance System

## Status
Accepted

## Date
2025-01-15

## Context
DUX needed a systematic approach to govern UI components and their relationship to DUX objects. Without governance, components would be built inconsistently and wouldn't align with the declarative UX principles.

## Decision
Implement a component governance system where DUX objects "hire" UI components for specific jobs.

### Component Architecture
- **Table Row Components**: For comparison/prioritization workflows
- **Grid Card Components**: For discovery/browsing workflows  
- **Detail Page Components**: For deep analysis (doubles as downloadable slides)

### API Contracts + Content Negotiation
Use both API contracts (from canonical definitions) and content negotiation (HTTP Accept headers):

```javascript
// API contracts generated from canonical object definitions
const PROBLEM_CONTRACTS = {
  "table-row": {
    "required_fields": ["job_statement", "opportunity_score", "created_by", "end_user", "updated_at"],
    "typography_rules": {
      "opportunity_score": "bold=evidence, italic=synthetic, —=none"
    }
  },
  "detail-page": {
    "required_fields": ["all_fields"],
    "slide_template": "problem_deep_dive_slide",
    "downloadable": true
  }
}

// Content negotiation implementation
GET /api/objects/problems
Accept: application/vnd.dux.table-row+json    // Returns table row format
Accept: application/vnd.dux.grid-card+json    // Returns card format
Accept: application/vnd.dux.detail-page+json  // Returns slide format
```

### Governance Structure
- **Component Definitions**: `/src/dux_component_definitions/`
- **Markdown-First**: Components follow same governance as DUX objects
- **Canonical Source**: API contracts generated from canonical object definitions
- **Agent Prompts**: Generated from same canonical source for consistency

## Consequences
### Positive
- Consistent component behavior across the design system
- Clear relationship between DUX objects and UI components
- API contracts ensure components get exactly the data they need
- Detail pages double as downloadable slides (lazy architecture)

### Negative
- Additional governance overhead for component definitions
- API complexity with multiple content types per endpoint

## Implementation
- Create component definition markdown files for each component type
- Implement API contract generation from canonical definitions
- Build content negotiation layer in API endpoints
- Integrate with existing HITL validation pipeline