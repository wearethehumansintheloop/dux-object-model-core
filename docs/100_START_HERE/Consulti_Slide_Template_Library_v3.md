# Consulting Slide Template Library (v3.0 - Evidence-Based Schema)

## Schema Overview
This template library follows the Evidence Object model with structured validation, 
citation requirements, and metadata tracking for reliable slide generation.

## How to Use
1. Upload this template into Notebook LM or other System prompt to extract structured slide data
for content design. 

2. Use this as the Human in the Loop Prompt

### Prompt: Slide Generation (Template-Driven)
**Objective:** Extract insights and generate complete slides using full template schema with embedded evidence.
**Process:**
1. **Extract Stories:** Analyze sources for distinct insights about data scientist workflows, challenges, expectations. Each insight becomes one slide.
2. **Template Selection:** For each story/insight, choose appropriate template (matrix, timeline, process, journeymap, dataviz, demographics, insights, techstack, comparative).
3. **Complete Slides:** Generate full slides with:
   - Complete markdown front matter (object_type, template_id, citation, supporting_evidence, etc.)
   - Slide content matching template structure
   - Evidence objects embedded in supporting_evidence array
4. **Output Format:** List of individual slides in markdown format, each a complete template with:
   - Full schema compliance
   - Evidence backing with citations
   - Ready for slide processor
**Deliverable:** List of complete, evidence-backed slides covering all extractable stories from sources.


## Basic Templates

### 1. Matrix 2x2 Template
```yaml
---
object_type: "slide_template"
template_id: "ST-20250819-matrix2x2"
slide_type: "matrix"
title: "Strategic Initiative Prioritization"
layout: "matrix"
component: "matrix2x2"
xAxisLabel: "Feasibility"
yAxisLabel: "Impact"
supporting_evidence:
  - evidence_id: "EV-20240715-strategy01"
    synthesized_finding: "High-impact initiatives with high feasibility deliver 3x faster ROI than complex transformational projects"
    finding_prevalence: "Consistent across 15 strategic planning sessions"
    applications_of_evidence: ["strategic prioritization", "resource allocation"]
    pull_quote: "We need to focus on quick wins that don't require massive organizational change"
    pull_quote_attribution:
      source_pid: "workshop_participant_07"
      source_artifact_name: "Strategic Planning Workshop Q3 2024"
      page_reference: "slide 12"
      source_authors: "Strategy Team"
      source_created_on: "2024-07-15"
      source_artifact_trace_endpoint: "./workshops/strategy-q3-2024.pptx"
citation:
  source_artifact_name: "Strategic Planning Workshop Q3 2024"
  page_reference: "slide 12"
  source_authors: "Strategy Team"
  source_created_on: "2024-07-15"
  source_artifact_trace_endpoint: "./workshops/strategy-q3-2024.pptx"
required_fields: ["title", "xAxisLabel", "yAxisLabel", "supporting_evidence", "citation"]
optional_fields: ["subtitle", "insight", "source_note"]
_template_metadata:
  schema_version: "v3.0"
  generated_by: "template_processor_v3"
  validation_status: "validated"
  last_updated: "2024-08-19"
---
```

# Strategic Initiative Prioritization
## Impact vs Feasibility

### High Impact, High Feasibility
- Quick wins initiative
- Scale fast opportunity
- Low-hanging fruit

### High Impact, Low Feasibility  
- Major strategic bet
- Long-term investment
- Transformational project

### Low Impact, High Feasibility
- Maintenance task
- Easy implementation
- Operational improvement

### Low Impact, Low Feasibility
- Avoid or minimize
- Resource drain
- Legacy system

> Insight: Focus on high-impact, high-feasibility quadrant for immediate results
> Source: Internal Strategy Review 2024


### 2. Timeline Template
```yaml
---
object_type: "slide_template"
template_id: "ST-20250819-timeline"
slide_type: "timeline"
title: "Project Timeline"
layout: "timeline"
component: "timeline"
time_period: "Q1-Q4 2024"
citation:
  source_artifact_name: "Project Management Plan 2024"
  page_reference: "section 3.2"
  source_authors: "PMO Team"
  source_created_on: "2024-01-15"
  source_artifact_trace_endpoint: "./pmo/project-plan-2024.pdf"
required_fields: ["title", "time_period", "phases", "citation"]
optional_fields: ["subtitle", "deliverables", "milestones"]
_template_metadata:
  schema_version: "v3.0"
  generated_by: "template_processor_v3"
  validation_status: "validated"
  last_updated: "2024-08-19"
---
```

# Project Timeline
## Q1-Q4 Implementation Roadmap

### Phase 1: Foundation
**Date:** Q1 2024
**Description:** Infrastructure setup and team onboarding
**Deliverables:** Core platform, initial team training

### Phase 2: Development  
**Date:** Q2 2024
**Description:** Feature development and testing phase
**Deliverables:** MVP features, quality assurance

### Phase 3: Launch
**Date:** Q3 2024  
**Description:** Production deployment and user rollout
**Deliverables:** Live system, user documentation

### Phase 4: Scale
**Date:** Q4 2024
**Description:** Performance optimization and expansion
**Deliverables:** Full feature set, performance metrics

> Source: Project Management Office


### 3. Process Flow Template
```yaml
---
object_type: "slide_template"
template_id: "ST-20250819-processflow"
slide_type: "process"
title: "Customer Onboarding Process"
layout: "process"
component: "processflow"
process_stages: 3
citation:
  source_artifact_name: "Customer Success Playbook"
  page_reference: "chapter 2"
  source_authors: "Customer Success Team"
  source_created_on: "2024-06-01"
  source_artifact_trace_endpoint: "./customer-success/onboarding-playbook.pdf"
required_fields: ["title", "process_stages", "phase_descriptions", "citation"]
optional_fields: ["subtitle", "success_criteria", "timelines"]
_template_metadata:
  schema_version: "v3.0"
  generated_by: "template_processor_v3"
  validation_status: "validated"
  last_updated: "2024-08-19"
---
```

# Customer Onboarding Process
## Three-Step Implementation

### Discovery Phase
- Initial consultation
- Requirements gathering
- Stakeholder alignment
- Technical assessment

### Implementation Phase
- System configuration
- Data migration
- User training
- Testing procedures

### Optimization Phase
- Performance monitoring
- Feedback collection
- Process refinement
- Success measurement

> Source: Customer Success Team Analysis


### 4. Journey Map Template
```yaml
---
object_type: "slide_template"
template_id: "ST-20250819-journeymap"
slide_type: "journeymap"
title: "Customer Experience Journey"
layout: "journeymap"
component: "journeymap"
journey_stages: ["awareness", "consideration", "purchase", "onboarding", "advocacy"]
citation:
  source_artifact_name: "Customer Experience Research 2024"
  page_reference: "findings section"
  source_authors: "UX Research Team"
  source_created_on: "2024-05-20"
  source_artifact_trace_endpoint: "./research/cx-research-2024.pdf"
required_fields: ["title", "journey_stages", "pain_points", "citation"]
optional_fields: ["subtitle", "opportunities", "touchpoints"]
_template_metadata:
  schema_version: "v3.0"
  generated_by: "template_processor_v3"
  validation_status: "validated"
  last_updated: "2024-08-19"
---
```

# Customer Experience Journey
## Pain Points Along the Customer Path

### High Priority Pain Points
- Account setup complexity
- Documentation gaps
- Support response time

### Medium Priority Pain Points  
- Feature discovery
- Integration challenges
- Training resources
- Mobile experience

> Insight: Addressing top 3 pain points could improve satisfaction by 40%
> Source: Customer Feedback Survey 2024


### 5. Data Visualization Split Template
```yaml
---
object_type: "slide_template"
template_id: "ST-20250819-datavizsplit"
slide_type: "dataviz"
title: "Revenue Growth Analysis"
layout: "dataviz"
component: "datavizsplit"
questionWord: "What"
chartType: "waterfall"
data_source_type: "financial_analysis"
citation:
  source_artifact_name: "Q4 Financial Analysis Report"
  page_reference: "revenue projections table"
  source_authors: "Finance Team"
  source_created_on: "2024-01-31"
  source_artifact_trace_endpoint: "./finance/q4-analysis-2024.xlsx"
required_fields: ["title", "chartType", "data_points", "citation"]
optional_fields: ["subtitle", "numerical_goal", "insights"]
_template_metadata:
  schema_version: "v3.0"
  generated_by: "template_processor_v3"
  validation_status: "validated"
  last_updated: "2024-08-19"
---
```

# What will improve [area of strategic initiative]?
## Revenue Growth Analysis

**Numerical Goal:** $2.5M additional revenue by Q4 2024

### Chart Data
- **Base Revenue:** Current baseline
- **Cost Reduction:** 8% improvement from operational efficiency
- **Market Expansion:** 12% improvement from new segments  
- **Product Innovation:** 5% improvement from new features

### Cost Reduction Initiatives
**Description:** Operational efficiency and automation savings through process optimization and technology investments.

### Market Expansion Strategy
**Description:** New geographic markets and customer segments including emerging markets and enterprise clients.

### Product Innovation Pipeline
**Description:** New feature development and premium offerings to increase average revenue per customer.

> Insight: Market expansion provides highest ROI with 12% revenue impact
> Source: Finance Team Analysis Q4 2024


## Advanced Templates

### 6. Survey Demographics Template
```yaml
---
object_type: "slide_template"
template_id: "ST-20250819-demographics"
slide_type: "demographics"
title: "Survey Demographics"
layout: "demographics"
component: "surveydemographics"
sampleSize: 201
survey_type: "industry_benchmark"
citation:
  source_artifact_name: "Industry Survey Results 2024"
  page_reference: "demographics section"
  source_authors: "Research Team"
  source_created_on: "2024-04-10"
  source_artifact_trace_endpoint: "./surveys/industry-benchmark-2024.pdf"
required_fields: ["title", "sampleSize", "demographic_breakdowns", "citation"]
optional_fields: ["subtitle", "survey_methodology", "confidence_interval"]
_template_metadata:
  schema_version: "v3.0"
  generated_by: "template_processor_v3"
  validation_status: "validated"
  last_updated: "2024-08-19"
---
```

# Survey Demographics
## Participant Breakdown (N=201)

### Company Types (N= / %)
- **Integrated Oil Company (IOC):** 80 / 40%
- **Independent:** 81 / 40% 
- **National Oil Company (NOC):** 20 / 10%
- **Oilfield Equipment Services:** 20 / 10%

### Geographic Regions (N= / %)
- **Europe:** 70 / 35%
- **USA:** 48 / 24%
- **Canada:** 32 / 16%
- **Middle East:** 20 / 10%
- **India:** 13 / 6%
- **Latin America:** 10 / 5%
- **China:** 6 / 3%
- **Australia/New Zealand:** 2 / 1%

### Executive Roles (N= / %)
- **Chief Financial Officer:** 40 / 20%
- **Chief Operating Officer:** 40 / 20%
- **Chief Strategy Officer:** 40 / 20%
- **Chief Marketing Officer:** 40 / 20%
- **CIO/CTO/CDO:** 20 / 10%
- **Chief Innovation Officer:** 12 / 6%
- **Chief Mobility Officer:** 9 / 5%

### Company Revenue Distribution
**Chart:** Donut chart showing revenue segments
- **>$10B:** 100 participants (50%)
- **$1B-$10B:** 60 participants (30%)
- **$500M-$999M:** 30 participants (15%)
- **$100M-$499M:** 11 participants (5%)

> Source: Oil and Gas Reinvention Index 2022


### 7. Insights Multi-Chart Template
```yaml
---
object_type: "slide_template"
template_id: "ST-20250819-insightsmultichart"
slide_type: "insights"
title: "Market Leadership Analysis"
layout: "insights"
component: "insightsmultichart"
comparison_type: "leaders_vs_laggards"
citation:
  source_artifact_name: "Market Research Analysis 2024"
  page_reference: "executive summary"
  source_authors: "Market Intelligence Team"
  source_created_on: "2024-03-25"
  source_artifact_trace_endpoint: "./market-research/analysis-2024.pdf"
required_fields: ["title", "comparison_type", "key_insights", "citation"]
optional_fields: ["subtitle", "supporting_context", "chart_specifications"]
_template_metadata:
  schema_version: "v3.0"
  generated_by: "template_processor_v3"
  validation_status: "validated"
  last_updated: "2024-08-19"
---
```

# Expectations for returns are more achievable
## Leaders vs Laggards Performance Analysis

### Main Insight
One of the most interesting findings in last year's survey was the extraordinary optimism leaders felt about their reinvention strategies. They believed their actions would drive margin improvements of at least 7%, revenue growth of at least 11%, and ESG improvements of 27%. Laggards were much more modest in their expectations.

### Supporting Context
This year, all energy companies are rethinking the benefits of reinvention. We believe they are settling on more achievable expectations, borne of pragmatic and holistic actions.

### Performance Comparison Charts
**Chart Title:** Percentage of respondents expecting >10% improvement over the next three years

#### Margin Growth Expectations
- **Leaders:** 5% minimum expectation
- **Laggards:** 3% minimum expectation  
- **Multiplier:** 1.5X advantage
- **Metric:** margin growth

#### Revenue Growth Expectations  
- **Leaders:** 5% minimum expectation
- **Laggards:** 2% minimum expectation
- **Multiplier:** 2.8X advantage
- **Metric:** revenue growth

#### ESG Improvement Expectations
- **Leaders:** 11% minimum expectation
- **Laggards:** 5% minimum expectation
- **Multiplier:** 2.4X advantage  
- **Metric:** ESG improvement

> Insight: Leaders consistently set higher expectations across all business metrics
> Source: Energy Industry Survey 2022


### 8. Technology Stack Template
```yaml
---
object_type: "slide_template"
template_id: "ST-20250819-techstack"
slide_type: "techstack"
title: "Cloud Architecture Framework"
layout: "techstack"
component: "techstack"
stack_layers: 5
architecture_type: "cloud_native"
citation:
  source_artifact_name: "Enterprise Architecture Guidelines"
  page_reference: "section 4.3"
  source_authors: "Architecture Team"
  source_created_on: "2024-02-28"
  source_artifact_trace_endpoint: "./architecture/enterprise-guidelines.pdf"
required_fields: ["title", "stack_layers", "layer_descriptions", "citation"]
optional_fields: ["subtitle", "technology_choices", "implementation_notes"]
_template_metadata:
  schema_version: "v3.0"
  generated_by: "template_processor_v3"
  validation_status: "validated"
  last_updated: "2024-08-19"
---
```

# There are distinct CSPs moves that capitalize on their 'permission space' to expand across the value chain
## Defining Technology Roles in Digital Transformation

### The Technology Stack
**Stack Layers (bottom to top):**
- **Infrastructure:** Compute, Storage, Network, Security foundations
- **Software & Platforms:** Databases, Analytics, Integration, APIs  
- **Digital Identity:** Identity, Ownership, Authenticity, Digital Twin
- **Economy:** Creators, Products, Market Structures, Payments
- **Experience:** Discovery, Behaviors, Policy, Content, Services

### Permission Space Details
**Layer Breakdown:**
- **Infrastructure Layer:** Devices | Network | Compute
- **Platform Layer:** 3D Platforms | Data Platforms | Interchange Tools & Standards  
- **Identity Layer:** Identity | Ownership | Authenticity | Digital Twin
- **Economy Layer:** Creators | Products | Market Structures | Payments
- **Experience Layer:** Discovery | Behaviors | Policy | Content | Services | Assets

### CSP Opportunity Matrix
**Strategic Positioning:**
- **Performance Player:** High execution, established market
- **Orchestrator:** Platform integration capabilities
- **Disruptor:** Innovation-focused market entry

> Source: Enterprise Architecture Review 2024


### 9. Comparative Analysis Template
```yaml
---
object_type: "slide_template"
template_id: "ST-20250819-comparative"
slide_type: "comparative"
title: "Trust Impact on Customer Retention"
layout: "comparative"
component: "comparativeanalysis"
comparison_groups: ["trusters", "neutral", "distrusters"]
analysis_type: "retention_behavior"
citation:
  source_artifact_name: "Customer Trust Benchmark Study"
  page_reference: "retention analysis chapter"
  source_authors: "Customer Research Team"
  source_created_on: "2024-06-15"
  source_artifact_trace_endpoint: "./research/trust-benchmark-2024.pdf"
required_fields: ["title", "comparison_groups", "key_findings", "citation"]
optional_fields: ["subtitle", "methodology", "statistical_significance"]
_template_metadata:
  schema_version: "v3.0"
  generated_by: "template_processor_v3"
  validation_status: "validated"
  last_updated: "2024-08-19"
---
```

# Trust
## How Trust Affects Customer Loyalty and Retention Behavior

### Figure 1: Provider Trust Impact
**Research Question:** People who trust their providers are the most likely to stay with them

**Trust Distribution:**
- **Overall Retention:** 61%
- **Trusters:** 84% retention rate
- **Neutral:** 24% retention rate  
- **Distrusters:** 12% retention rate
- **Industry Average:** 17%

**Chart Type:** Donut chart with bar breakdown
**Source:** 2021 Accenture Patient Experience Benchmark

### Figure 2: Payer Trust Analysis  
**Research Question:** Trusters are more likely than neutrals and distrusters to stay with their payers

**Retention Comparison:**
- **Overall Retention:** 55%
- **Trusters:** 76% retention rate
- **Neutral:** 36% retention rate
- **Distrusters:** 19% retention rate  
- **Industry Average:** 34%

**Chart Type:** Donut chart with bar breakdown
**Source:** 2022 Accenture Consumer Payer Experience Benchmark Survey

### Key Insight
Trusters are five times more likely to stay with their providers than all other categories, and they are almost seven times more likely to stay than those who don't trust their providers at all.

> Source: Healthcare Experience Research 2022


## Schema Validation Rules

### Slide Type Enums (Required Validation)
```yaml
slide_type:
  enum: ["matrix", "timeline", "process", "journeymap", "dataviz", "demographics", "insights", "techstack", "comparative"]
  description: "Validates slide type for processor selection"

layout:
  enum: ["matrix", "timeline", "process", "journeymap", "dataviz", "demographics", "insights", "techstack", "comparative"]
  description: "Must match slide_type for consistency"

component:
  enum: ["matrix2x2", "timeline", "processflow", "journeymap", "datavizsplit", "surveydemographics", "insightsmultichart", "techstack", "comparativeanalysis"]
  description: "Specific component implementation"
```

## Template Usage Guide (v3.0)

### Quick Start
1. Copy the appropriate template with full YAML front matter
2. Validate all required_fields are present
3. Update citation object with accurate source attribution
4. Replace placeholder content with validated data
5. Run through schema validator before processing

### Required Schema Fields
- **object_type:** Always "slide_template" for validation
- **template_id:** Unique identifier (ST-[timestamp]-[type])
- **slide_type:** Must match enum validation list
- **title:** Main slide headline
- **citation:** Complete citation object with all 5 required fields
- **required_fields:** Array of mandatory content fields
- **_template_metadata:** Processing and validation tracking

### Citation Object Requirements
Every template MUST include a complete citation object:
```yaml
citation:
  source_artifact_name: "[Document Title]"
  page_reference: "[Specific Location]"
  source_authors: "[Author Names]"
  source_created_on: "[YYYY-MM-DD]"
  source_artifact_trace_endpoint: "[File Path/URL]"
```

### Content Guidelines (Evidence-Based)
- Use **### headers** for main sections with structured data
- Add **- bullet points** with quantified claims where possible
- Include **> blockquotes** for insights with source validation
- Reference citation object in content using `source_authors` and `source_created_on`
- Always provide traceability to source materials

### Schema Compliance
- **Required field validation:** All `required_fields` must be present in content
- **Enum constraints:** slide_type, layout, and component must match approved values
- **Citation completeness:** All 5 citation fields are mandatory
- **Metadata tracking:** _template_metadata enables processing pipeline integration
- **Version control:** schema_version tracks template evolution

### Common Patterns (Schema-Driven)
- **Comparison slides:** Use `comparison_type` and `comparison_groups` fields
- **Process slides:** Define `process_stages` count and sequential phase descriptions
- **Data slides:** Specify `chartType` and `data_source_type` for validation
- **Strategic slides:** Include `applications_of_evidence` array for outcome tracking
- **All slides:** Maintain citation traceability and source validation

### Template Customization (v3.0 Rules)
Templates can be customized within schema constraints:
- **Section headers:** Must align with `required_fields` validation
- **Content structure:** Follow template-specific field requirements
- **Citation updates:** Always update full citation object when changing sources
- **Metadata tracking:** Update `last_updated` when making modifications
- **Enum compliance:** slide_type/layout/component changes must use approved values

### Processing Pipeline Integration
```yaml
_template_metadata:
  schema_version: "v3.0"  # Enables v3.0 processor selection
  generated_by: "template_processor_v3"  # Processing tool identification
  validation_status: "validated"  # Schema compliance confirmation
  last_updated: "2024-08-19"  # Change tracking
```

### Migration from v2.x Templates
1. Add `object_type: "slide_template"` to front matter
2. Create complete `citation` object for all sources
3. Define `required_fields` and `optional_fields` arrays
4. Add `_template_metadata` object
5. Validate `slide_type` against enum constraints

The schema processor enforces structure while maintaining presentation flexibility.