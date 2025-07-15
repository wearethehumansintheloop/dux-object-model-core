# Problem Grid Card Component Definition

## Component Overview
**Component ID**: `problem_grid_card_v1`  
**Object Type**: Problem  
**Display Type**: Grid Card  
**Purpose**: Enable discovery and quick comparison of multiple problems in a visual grid layout

## Job to be Done
> When I need to browse and discover problems across our portfolio, I want to see key information at a glance in a scannable grid, so that I can identify patterns and select problems for deeper analysis.

## Grid Layout Specifications
```yaml
grid_layout:
  columns:
    desktop: 3
    tablet: 2
    mobile: 1
  card_aspect_ratio: "4:3"
  max_cards_initial: 12
  pagination: infinite_scroll
```

## Card Content Hierarchy

### Card Header
**Attribute**: `what_is_at_stake`  
**Treatment**: Bold, 2 lines max, ellipsis overflow  
**Purpose**: Hook - immediate impact understanding

### Opportunity Score Badge
**Attribute**: `opportunity_score.value`  
**Position**: Top right corner  
**Treatment**: 
  - Color: Green (>10), Yellow (5-10), Red (<5)
  - Typography: Bold (evidence), Italic (synthetic)
  - Display: Large number with small "Opportunity Score" label

### Card Body
**Primary Content**: `job_statement` (concatenated)  
**Treatment**: 3 lines max, ellipsis overflow  
**Structure**:
  - Line 1: `user_scenario.value`
  - Line 2: `user_enablement.value`
  - Line 3: `user_outcome.value`

### Card Footer
**Left Side**: `end_user[0]` (primary persona)  
**Right Side**: `updated_at` (relative time)  
**Treatment**: Small text, muted color

### Visual Indicators
```yaml
visual_indicators:
  evidence_quality:
    position: bottom_border
    high_fidelity: "4px solid green"  # all evidence-based
    mixed_fidelity: "4px solid yellow"  # some synthetic
    hypothesis: "4px solid blue"  # all synthetic
  
  tag_chips:
    position: below_body
    max_shown: 2
    source: tags[0:2]
```

## Interaction Patterns
- **Click**: Navigate to problem detail page
- **Hover**: Expand to show full `job_statement` + evidence count
- **Long press** (mobile): Quick actions menu
- **Keyboard**: Tab navigation, Enter to open

## Grid-Level Features

### Filtering Options
```yaml
filters:
  opportunity_score_range:
    - "Blue Ocean (>10)"
    - "Emerging (5-10)"
    - "Red Ocean (<5)"
  
  evidence_type:
    - "Evidence-based"
    - "Hypothesis"
    - "Mixed"
  
  end_user: dynamic_from_data
  tags: dynamic_from_data
  recency: 
    - "This week"
    - "This month"
    - "This quarter"
```

### Sorting Options
- Opportunity Score (default)
- Recency (updated_at)
- Evidence Quality
- Alphabetical (job_statement)

### Bulk Actions
- Compare selected (up to 4)
- Export selected to slides
- Generate insights report

## Empty States
```yaml
no_results:
  message: "No problems match your filters"
  action: "Adjust filters or create new problem"

no_problems:
  message: "No problems documented yet"
  action: "Import from research or create manually"
```

## Related Components
- **Upgrades to**: `problem_detail_page_component` on click
- **Compares with**: `problem_table_row_component` (list view alternative)
- **Exports to**: Slide templates via detail page

## RAG Enrichment
```yaml
rag_enrichment:
  enabled: false  # Grid cards prioritize speed
  on_hover_preview: true  # Fetch on hover only
  preview_enrichments:
    - full_evidence_count
    - related_problems_count
```

## API Contract
```yaml
endpoint: GET /api/objects/problems
accept_header: application/vnd.dux.grid-card+json
query_params:
  limit: 12
  offset: 0
  sort: opportunity_score_desc
  filters: {
    score_range: [min, max],
    evidence_type: string,
    end_user: string[],
    tags: string[]
  }
response_fields:
  - id
  - what_is_at_stake
  - job_statement
  - opportunity_score
  - end_user[0]
  - tags[0:2]
  - updated_at
```

## Performance Constraints
- **Initial grid load**: < 300ms for 12 cards
- **Image loading**: Lazy load if card has images
- **Interaction response**: < 50ms for hover states
- **Filter/sort**: < 100ms for client-side operations

## Accessibility
- **Grid role**: `grid` with proper ARIA labels
- **Card role**: `gridcell`
- **Keyboard**: Arrow key navigation between cards
- **Screen reader**: Announce "Problem: [stake], Score: [value]"
- **Focus management**: Visible focus ring, trap within grid

## Responsive Behavior
```yaml
mobile:
  - Single column
  - Tap for preview
  - Swipe for next/prev
  
tablet:
  - Two columns
  - Hover preview enabled
  
desktop:
  - Three columns
  - Full hover interactions
  - Keyboard shortcuts enabled
```