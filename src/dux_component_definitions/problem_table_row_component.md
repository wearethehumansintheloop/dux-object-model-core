# Problem Table Row Component Definition

## Component Overview
**Component ID**: `problem_table_row_v1`  
**Object Type**: Problem  
**Display Type**: Table Row  
**Purpose**: Enable quick scanning and prioritization of multiple problems

## Job to be Done
> When I need to compare multiple problems for prioritization decisions, I want to see the most critical attributes in a scannable row format, so that I can quickly identify which problems deserve immediate attention.

## Required Attributes
| Attribute | Source Path | Display Treatment | Purpose |
|-----------|-------------|-------------------|----------|
| job_statement | `job_statement.user_scenario.value + job_statement.user_enablement.value + job_statement.user_outcome.value` | Concatenated with spaces | Primary problem description |
| opportunity_score | `opportunity_score.value` | Typographic: **bold** (evidence), *italic* (synthetic), — (none) | Prioritization metric |
| created_by | `metadata.created_by` | Plain text | Freshness indicator |
| end_user | `end_user[0]` (first item) | Plain text | Primary audience |
| updated_at | `updated_at` | Relative time (e.g., "2 days ago") | Recency |

## Visual Hierarchy
```yaml
primary:
  - job_statement: 
      max_chars: 120
      truncation: ellipsis
      
secondary:
  - opportunity_score:
      alignment: right
      width: fixed (80px)
  - end_user:
      width: fixed (120px)
      
metadata:
  - created_by:
      width: fixed (100px)
  - updated_at:
      width: fixed (100px)
      format: relative_time
```

## Typography Rules
```yaml
opportunity_score_treatment:
  evidence_based: 
    condition: "all sources = 'evidence'"
    treatment: "font-weight: bold"
  predictive:
    condition: "any source = 'synthetic'"
    treatment: "font-style: italic"
  no_score:
    condition: "value is null"
    treatment: "display: '—'"
```

## Interaction Patterns
- **Click**: Navigate to problem detail page
- **Hover**: Show preview tooltip with `what_is_at_stake`
- **Sort**: Enable on all columns
- **Filter**: Enable on `end_user`, `opportunity_score` ranges

## RAG Enrichment
```yaml
rag_enrichment:
  enabled: false  # Table rows don't need RAG enrichment
  reason: "Performance - table views should load instantly"
```

## API Contract
```yaml
endpoint: GET /api/objects/problems
accept_header: application/vnd.dux.table-row+json
response_fields:
  - id
  - job_statement
  - opportunity_score
  - end_user
  - updated_at
  - metadata.created_by
```

## Responsive Behavior
```yaml
mobile:
  visible_fields: 
    - job_statement (truncated to 60 chars)
    - opportunity_score
  hidden_fields:
    - created_by
    - end_user
    - updated_at
    
tablet:
  visible_fields:
    - job_statement (truncated to 90 chars)
    - opportunity_score
    - end_user
  hidden_fields:
    - created_by
    - updated_at
    
desktop:
  visible_fields: all
```

## Accessibility
- **Role**: `row` within `table`
- **Screen reader**: Announce "Problem: [job_statement], Score: [opportunity_score with context]"
- **Keyboard**: Arrow keys for navigation, Enter to open detail
- **Focus**: Visible focus ring on hover/tab

## Performance Constraints
- **Initial load**: 50 rows max
- **Pagination**: Infinite scroll after initial load
- **Load time target**: < 200ms for initial render
- **No RAG calls**: Direct API response only

## Slide Template Compatibility
**Not applicable** - Table rows are for application UIs, not slide generation

## Available Slide Templates for Problem Objects
*Other Problem components can use these consulting slide templates:*

- **Matrix2x2**: Plot problems by Opportunity Score vs Feasibility/Effort
- **ComparativeAnalysis**: Show current vs desired state gaps
- **DataVizSplit**: Display problem frequency/severity metrics
- **JourneyMap**: Show where problems occur in user journey
- **InsightsMultiChart**: Compare problem patterns across segments