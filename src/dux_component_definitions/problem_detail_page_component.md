# Problem Detail Page Component Definition

## Component Overview
**Component ID**: `problem_detail_page_v1`  
**Object Type**: Problem  
**Display Type**: Detail Page  
**Purpose**: Present comprehensive problem analysis through multiple visualization formats

## Job to be Done
> When I need to deeply understand a problem and communicate its priority to stakeholders, I want to view it through multiple analytical lenses, so that I can make evidence-based decisions about where to invest resources.

## Slide Template Compatibility & Jobs to be Done

### 1. InsightsMultiChart ⭐ (Primary)
**Job to be Done**: When I need to highlight problems 'worth solving', I want to force rank problems by their job statement's opportunity score, so that my team knows which opportunities are being well served and which opportunities are underserved.

**Attribute Mappings**:
```yaml
title: "Blue Ocean vs Red Ocean Opportunities"
main_insight: aggregate(what_is_at_stake)
blue_ocean_filter: opportunity_score.value > 10
red_ocean_filter: opportunity_score.value < 5
chart_label: job_statement (truncated to 50 chars)
chart_value: opportunity_score.value
multiplier: avg(blue_ocean) / avg(red_ocean)
```

### 2. ComparativeAnalysis ⭐ (Secondary)
**Job to be Done**: When I need to show market gaps, I want to display what customers are currently hiring to get the job done, so that I can express the value of addressing unmet JTBDs.

**Attribute Mappings**:
```yaml
title: job_statement.user_scenario.value
figure1_title: "Current Solutions"
figure1_data: what_is_at_stake
figure1_metric: opportunity_score.satisfaction
figure2_title: "Desired Outcome"
figure2_data: job_statement.user_outcome.value
figure2_metric: opportunity_score.importance
key_insight: "Gap between importance ({importance}) and satisfaction ({satisfaction})"
```

### 3. SurveyDemographics
**Job to be Done**: When I need to validate problem importance, I want to show the survey data behind opportunity scores, so that stakeholders trust the prioritization is evidence-based.

**Attribute Mappings**:
```yaml
title: "Evidence Base for {job_statement}"
sample_size: count(evidence)
demographics:
  - category: "End Users"
    data: end_user (with counts)
  - category: "Evidence Sources"
    data: evidence.provenance_id (grouped by type)
  - category: "Score Distribution"
    data: opportunity_score (importance vs satisfaction scatter)
source: protocol_url
```

### 4. Timeline
**Job to be Done**: When I need to show problem escalation, I want to illustrate how a problem starts small and scales over time, so that we understand what's at stake if we don't act.

**Attribute Mappings**:
```yaml
title: "Evolution of {job_statement}"
phases:
  - phase: "Problem Emerges"
    description: job_statement.user_scenario.value
    impact: "Low"
  - phase: "Problem Scales"
    description: "Expanding to {count(end_user)} user groups"
    impact: "Medium"
  - phase: "Critical Mass"
    description: what_is_at_stake
    impact: "High - Score: {opportunity_score.value}"
  - phase: "Future State"
    description: job_statement.user_outcome.value
    impact: "Resolution"
```

### 5. JourneyMap
**Job to be Done**: When I need to trace problem origins, I want to show how upstream issues create downstream symptoms, so that we solve root causes not just symptoms.

**Attribute Mappings**:
```yaml
title: "Problem Journey: {job_statement}"
pain_points:
  high_priority:
    - point: job_statement.user_scenario.value
      score: opportunity_score.value
      location: "upstream"
  medium_priority:
    - point: what_is_at_stake
      score: opportunity_score.importance
      location: "downstream"
insight: "Root cause in {user_scenario} creates {what_is_at_stake}"
```

### 6. TechStack (Situational)
**Job to be Done**: When I need to explain technical constraints, I want to show how architecture problems impact users, so that technical debt gets proper prioritization.

**Attribute Mappings**:
```yaml
title: "Technical Architecture Impact"
layers:
  - layer: "User Experience"
    components: end_user
    problem_impact: job_statement.user_outcome.value
  - layer: "Application"
    components: "Affected Systems" (from tags)
    problem_impact: job_statement.user_enablement.value
  - layer: "Infrastructure"
    components: "Root Cause" (from evidence)
    problem_impact: what_is_at_stake
```

## Templates NOT Recommended for Problems
- **ProcessFlow**: Better suited for Behavior objects (user action sequences)
- **Matrix2x2**: While feasible, typically used for solution prioritization rather than problem analysis
- **DataVizSplit**: Better for Result objects showing measurable outcomes

## Required Attributes for All Templates
| Attribute | Purpose |
|-----------|---------|
| job_statement | Primary problem description |
| opportunity_score | Prioritization metric |
| what_is_at_stake | Impact/consequences |
| evidence | Validation and source data |
| end_user | Affected personas |

## RAG Enrichment
```yaml
rag_enrichment:
  enabled: true
  enrichments:
    - evidence_expansion: "Fetch full context from provenance_ids"
    - similar_problems: "Find related problems for comparison"
    - solution_mapping: "Identify what's currently hired for this JTBD"
    - trend_analysis: "Show problem evolution over time"
```

## API Contract
```yaml
endpoint: GET /api/objects/problems/{id}/detail
accept_header: application/vnd.dux.detail-page+json
query_params:
  layout: [insightsmultichart|comparative|survey|timeline|journey|techstack]
  include_related: boolean
  enrich_evidence: boolean
```

## Performance Constraints
- **Initial load**: Core problem data < 100ms
- **RAG enrichment**: Async load < 2s
- **Slide generation**: < 500ms per template
- **Download generation**: < 1s for PDF/PPT