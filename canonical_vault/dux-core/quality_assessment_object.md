# OOUX ORCA Analysis: BDD Quality Assessment Domain

## Executive Summary

The BDD Quality Assessment domain models the systematic evaluation of BDD scenarios against a 4-layer quality model (Functional, Reliable, Usable, Delightful - the "Pizza" metaphor). This analysis identifies 5 core objects: QUALITY_ASSESSMENT, QUALITY_LAYER, ISSUE, SCENARIO, and FEATURE. The domain enables scenario authors to understand quality gaps, viewers to monitor overall health, and the system to enforce quality gates in CI/CD pipelines.

---

## STEP 1: Noun Extraction

### Comprehensive Noun List (Alphabetical)

From `bdd-quality-linter.py`, `bdd_coverage.py`, `quality-report.json`, and `bdd-reference-architecture.md`:

acceptance_criteria, analysis, anti_pattern, assertion, assessment, attribute, author,
average_quality_score, baseline, behavior, benchmark, billing, business_impact,
capability, cheese, ci_cd, codebase, complete_slice, compliance, configuration,
connection, constraint, context, coverage, criteria, crust, dashboard, data_type,
delight, delight_moment, delightful_layer, domain_language, element, email,
empty_feature, enablement, enablement_syntax, engineer, error, evaluation,
evidence, example, execution, execution_result, execution_status, feature,
feature_assessment, feature_file, feature_lint, file, file_path, finding,
fix_suggestion, flow, format, functional_layer, generated_at, gherkin,
given_step, hierarchy, human_behavior, impact, improvement, indicator, info,
infrastructure, issue, issue_summary, issue_type, jargon, jargon_term, job,
journey, json, just_crust, keyword, lab, latency, layer, layer_count,
layer_presence, layer_score, leading_indicator, level, line_number, lint,
linter, linter_version, location, markdown, measurable, measurable_criteria,
measurable_pattern, message, metadata, metric, mde, name, notification,
observable, observation, observer, opa, outcome, output, owner,
partial_slice, pass_fail, pattern, pepperoni, percentage, persona,
pipeline, pizza, platform, policy, privacy, problem, progress,
quality, quality_gate, quality_hierarchy, quality_layer, quality_report,
quality_score, quality_standard, recommendation, reference, reliable_layer,
report, requirement, result, reviewer, role, rule, sauce, scenario,
scenario_lint, scenario_name, score, scoring, section, severity, signal,
slice, soft_fail, source, specification, spiffe, standard, status, step,
step_count, step_definition, step_text, structure, style, subject,
success_criteria, suggestion, summary, syntax, system, tag, target,
technical_benchmark, technical_jargon, template, test, then_step,
threshold, timestamp, tool, total_score, tracking, transfer,
trigger, type, unrealistic_example, usable_layer, user, user_enablement,
validation, value, viewer, warning, when_step, workspace, wow_factor, zero_knowledge

---

## STEP 2: PILLAR ONE - OBJECTS

### Core Objects Identified (5 Objects)

From the extracted nouns, I identify 5 core objects that serve as anchors of understanding:

```
Core Objects:

1. QUALITY_ASSESSMENT - The primary evaluation artifact produced by the linter for a single scenario.
   Value: This is the core deliverable - it tells authors whether their scenario meets quality standards and provides actionable improvement guidance.

2. QUALITY_LAYER - One of the four quality dimensions (Functional, Reliable, Usable, Delightful) that compose an assessment.
   Value: Enables granular understanding of WHERE quality gaps exist within the pizza metaphor hierarchy.

3. ISSUE - A specific quality finding (error, warning, info) discovered during assessment.
   Value: Provides actionable, prioritized guidance for authors to fix specific problems.

4. SCENARIO - The BDD scenario being assessed (the subject of evaluation).
   Value: The unit of work that authors create and viewers monitor - the thing being measured.

5. FEATURE - The BDD feature file containing multiple scenarios.
   Value: Enables aggregate quality views and feature-level assessments for dashboard reporting.
```

**Why These Are Core Objects:**
- QUALITY_ASSESSMENT is the primary artifact (what gets created, stored, displayed)
- QUALITY_LAYER provides the dimensional structure (the "pizza" metaphor implementation)
- ISSUE provides the actionable feedback (what users act upon)
- SCENARIO is the subject being assessed (without it, no assessment exists)
- FEATURE provides aggregation (dashboard shows feature-level summaries)

**Rejected as Objects (These Are Attributes or Relationships):**
- score, quality_score, total_score -> attributes of QUALITY_ASSESSMENT
- severity, message, suggestion -> attributes of ISSUE
- step, step_text -> attributes of SCENARIO (or child collection)
- recommendation -> calculated content derived from ISSUE aggregation
- linter -> the system/actor, not a domain object

---

## STEP 3: PILLAR TWO - RELATIONSHIPS

### Object Relationship Map

```
FEATURE (1) <--contains-- (many) SCENARIO
  Description: A feature file contains multiple scenarios
  Navigation: Feature detail page shows all scenarios; Scenario shows parent feature
  Cardinality: Required - every scenario belongs to exactly one feature

SCENARIO (1) <--has-- (1) QUALITY_ASSESSMENT
  Description: Each scenario has exactly one current quality assessment
  Navigation: Scenario detail shows its assessment; Assessment links back to scenario
  Cardinality: 1:1 (each scenario produces exactly one assessment per linting run)
  Note: Historical assessments are immutable; new runs create new assessments

QUALITY_ASSESSMENT (1) <--composed of-- (4) QUALITY_LAYER
  Description: Every assessment evaluates all 4 quality layers
  Navigation: Assessment detail shows all 4 layer scores
  Cardinality: Fixed at 4 (Functional, Reliable, Usable, Delightful)
  Note: Delightful is feature-level only in current implementation (always 0 for scenarios)

QUALITY_ASSESSMENT (1) <--has many-- (0..n) ISSUE
  Description: An assessment may have zero or more issues discovered
  Navigation: Assessment shows all issues; Issue belongs to one assessment
  Cardinality: 0 to many (perfect scenarios have 0 issues)

QUALITY_LAYER (1) <--has many-- (0..n) ISSUE
  Description: Issues are categorized by which layer they affect
  Navigation: Layer detail shows its issues; Issue belongs to one layer
  Cardinality: 0 to many per layer

FEATURE (1) <--has-- (1) FEATURE_ASSESSMENT (aggregated)
  Description: Feature-level metrics are calculated from scenario assessments
  Navigation: Feature shows aggregate quality score, complete slice count
  Cardinality: Calculated relationship (not stored separately)
```

### Relationship Diagram

```
                    FEATURE
                       |
                       | contains (1:many)
                       v
                   SCENARIO
                       |
                       | has (1:1)
                       v
              QUALITY_ASSESSMENT
                    /     \
       composed_of /       \ has_many
          (1:4)   /         \ (0:n)
                 v           v
          QUALITY_LAYER    ISSUE
                 |          /
                 | has_many/
                 | (0:n)  /
                 v       v
                ISSUE (categorized by layer)
```

### Open Questions for Stakeholders

1. **Assessment Versioning**: Should we track assessment history over time (assessment_v1, assessment_v2 for same scenario)?
   - Current: Linter produces point-in-time assessment
   - Potential: Track improvement over time with `previous_assessment_id`

2. **Delightful Layer at Scenario vs Feature Level**: The code shows Delightful is feature-level only (always 0 for scenarios). Should we:
   - Keep as-is (3 layers for scenarios, 4 for features)?
   - Add scenario-level delight markers (enablement syntax detection)?

3. **Step as Object**: Should STEP be a first-class object?
   - Current: Steps are attributes/collections within Scenario
   - Potential: Step-level quality assessment (currently only step counts are tracked)

---

## STEP 4: PILLAR THREE - CALLS-TO-ACTION

### CTAs Organized by Object and Role

```
QUALITY_ASSESSMENT CTAs:

  Author Role (BDD Scenario Writer):
    Primary CTAs:
      - View assessment results (see quality score, layer breakdown)
      - View issues list (understand what needs fixing)
      - Export to markdown (generate human-readable report)

    Secondary CTAs:
      - Compare with previous assessment (track improvement)
      - Copy assessment ID (for CI/CD integration)

    Relationship CTAs:
      - Navigate to scenario (jump to source .feature file)
      - Navigate to feature (see aggregate context)

  Viewer Role (Team Lead, Dashboard Consumer):
    Primary CTAs:
      - View aggregate quality (feature-level or repo-level summary)
      - Filter by status (PASS/SOFT_FAIL/FAIL)
      - Sort by quality score (find worst scenarios)

    Secondary CTAs:
      - Export report (generate stakeholder summary)
      - Track trends (quality over time - future capability)

  System Role (CI/CD Pipeline):
    Primary CTAs:
      - Generate assessment (run linter on scenario)
      - Validate pass/fail (quality gate check)
      - Emit status (return exit code for pipeline)

    Relationship CTAs:
      - Aggregate to feature (calculate feature-level metrics)
      - Aggregate to report (generate full repository report)

---

QUALITY_LAYER CTAs:

  Author Role:
    Primary CTAs:
      - View layer score (0-25 points per layer)
      - View layer presence (boolean: does this scenario have this layer?)
      - View layer issues (issues specific to this layer)

    Secondary CTAs:
      - View layer definition (what does "Usable" mean?)
      - View improvement suggestions (how to add this layer)

  Viewer Role:
    Primary CTAs:
      - Filter scenarios by missing layer (show all missing "Reliable")
      - View layer distribution (how many scenarios have each layer?)

---

ISSUE CTAs:

  Author Role:
    Primary CTAs:
      - View issue details (message, severity, suggestion)
      - Apply suggestion (act on the fix recommendation)
      - Dismiss issue (mark as won't-fix with reason - future capability)

    Secondary CTAs:
      - View similar issues (other scenarios with same issue type)
      - Request clarification (unclear suggestion - future capability)

  Viewer Role:
    Primary CTAs:
      - View issues summary (error/warning/info counts)
      - Filter by severity (show only errors)
      - View top issues (most common across codebase)

  System Role:
    Primary CTAs:
      - Categorize issue (assign layer, type, severity)
      - Generate suggestion (create actionable fix recommendation)

---

SCENARIO CTAs:

  Author Role:
    Primary CTAs:
      - View scenario source (original Gherkin text)
      - Edit scenario (modify to address issues - external action)
      - Re-lint scenario (regenerate assessment after edit)

    Secondary CTAs:
      - View scenario history (past assessments - future capability)
      - Clone scenario (duplicate as starting point)

  Viewer Role:
    Primary CTAs:
      - View scenario status (pass/fail/soft_fail)
      - Navigate to feature (see siblings)

---

FEATURE CTAs:

  Author Role:
    Primary CTAs:
      - View feature summary (aggregate score, scenario count)
      - View scenario list (all scenarios in feature)
      - Identify gaps (scenarios needing improvement)

  Viewer Role:
    Primary CTAs:
      - Sort features by quality (find worst features)
      - Filter by status (show failing features)
      - View complete slice percentage (MDE compliance metric)

    Secondary CTAs:
      - Export feature report (stakeholder summary)
      - Compare features (relative quality across codebase)
```

---

## STEP 5: PILLAR FOUR - ATTRIBUTES

### QUALITY_ASSESSMENT Attributes

```yaml
QUALITY_ASSESSMENT:

  Identity Attributes:
    - assessment_id: string (UUID, required)
      Description: Unique identifier for this assessment instance
      Example: "qa_2025-01-26_scenario-001"

  State Attributes:
    - status: enum (PASS | SOFT_FAIL | FAIL, required)
      Description: Overall quality gate result
      Business Rule: FAIL if errors > 0; SOFT_FAIL if warnings > 10; else PASS

    - is_complete_slice: boolean (required)
      Description: Whether scenario achieves MDE (all quality layers present)
      Business Rule: True if layers_present >= 3 AND total_score >= 80

    - is_just_crust: boolean (required)
      Description: Anti-pattern indicator - technical only, no user value
      Business Rule: True if layers_present <= 1 OR (usable_score == 0 AND total_score < 50)

    - layers_present: string (required)
      Description: Human-readable layer count
      Format: "X/4" where X is 0-4
      Example: "3/4"

    - assessment_text: string (required)
      Description: Human-readable quality assessment
      Values: "Complete Slice (MDE)" | "Mostly Complete (missing 1 layer)" |
              "Partial Slice (missing multiple layers)" | "Just the Crust (technical only)"

  Calculated Attributes:
    - quality_score: integer (0-100, required)
      Description: Total quality score across all layers
      Calculation: functional_score + reliable_score + usable_score + delightful_score

    - functional_score: integer (0-25, required)
      Description: Functional layer score (has assertions)
      Calculation: 0 if no Then steps; 15 if 1 Then; 25 if 2+ Then steps

    - reliable_score: integer (0-25, required)
      Description: Reliable layer score (measurable criteria)
      Calculation: Based on presence of measurable patterns (times, percentages, counts)

    - usable_score: integer (0-25, required)
      Description: Usable layer score (domain language, not jargon)
      Calculation: 25 minus penalties for technical jargon and placeholder names

    - delightful_score: integer (0-25, required)
      Description: Delightful layer score (user enablement, JTBD mapping)
      Note: Currently always 0 for scenarios (feature-level only)

    - error_count: integer (required)
      Description: Count of ERROR severity issues

    - warning_count: integer (required)
      Description: Count of WARNING severity issues

    - info_count: integer (required)
      Description: Count of INFO severity issues

  Descriptive Attributes:
    - quality_layers: object (required)
      Description: Boolean presence map for each layer
      Schema: { functional: bool, reliable: bool, usable: bool, delightful: bool }

    - scores: object (required)
      Description: Per-layer score breakdown
      Schema: { functional: int, reliable: int, usable: int, delightful: int }

  Relational Attributes:
    - scenario_id: string (required)
      Description: Foreign key to SCENARIO being assessed

    - scenario_name: string (required)
      Description: Denormalized scenario name for display

    - feature_id: string (required)
      Description: Foreign key to parent FEATURE

    - feature_name: string (required)
      Description: Denormalized feature name for display

    - issues: [ISSUE] (required)
      Description: Array of issues found during assessment
      Cardinality: 0 to many

  Metadata:
    - generated_at: ISO timestamp (required)
      Description: When the assessment was created

    - linter_version: string (optional)
      Description: Version of bdd-quality-linter that produced this assessment

    - source_file: string (optional)
      Description: Path to the behave-results.json used as input
```

### QUALITY_LAYER Attributes

```yaml
QUALITY_LAYER:

  Identity Attributes:
    - layer_id: enum (functional | reliable | usable | delightful, required)
      Description: Layer identifier matching pizza metaphor

    - layer_name: string (required)
      Description: Human-readable layer name
      Values: "Functional" | "Reliable" | "Usable" | "Delightful"

  State Attributes:
    - is_present: boolean (required)
      Description: Whether this layer is achieved in the assessment

    - layer_score: integer (0-25, required)
      Description: Points awarded for this layer (0-25 scale)

  Descriptive Attributes:
    - layer_description: string (required)
      Description: What this layer measures
      Examples:
        - Functional: "Has assertions (Then steps verify something)"
        - Reliable: "Has measurable criteria (<2 seconds, >98% success rate)"
        - Usable: "Uses domain language (not technical jargon)"
        - Delightful: "Maps to JTBD, includes user satisfaction metrics"

    - pizza_metaphor: string (required)
      Description: Pizza component mapping
      Values: "Crust" | "Sauce" | "Cheese" | "Pepperoni"

    - required_for_mde: boolean (required)
      Description: Whether this layer is required for MDE compliance
      Business Rule: All 4 layers required (value is always true)

  Relational Attributes:
    - assessment_id: string (required)
      Description: Foreign key to parent QUALITY_ASSESSMENT

    - issues: [ISSUE] (optional)
      Description: Issues categorized under this layer
```

### ISSUE Attributes

```yaml
ISSUE:

  Identity Attributes:
    - issue_id: string (UUID, optional - may be ephemeral)
      Description: Unique identifier for this issue instance

  State Attributes:
    - severity: enum (ERROR | WARNING | INFO, required)
      Description: Issue severity level
      Business Rules:
        - ERROR: Blocking issues (missing assertions, empty features)
        - WARNING: Improvement opportunities (no measurable criteria, technical jargon)
        - INFO: Suggestions (non-atomic steps, placeholder names)

  Descriptive Attributes:
    - type: string (required)
      Description: Issue classification code
      Values: "missing_assertions" | "incomplete_gwt_structure" | "no_measurable_criteria" |
              "non_atomic_steps" | "technical_jargon" | "unrealistic_examples" |
              "missing_user_enablement" | "empty_feature" | "emotional_language_no_proxy"

    - message: string (required)
      Description: Human-readable issue description
      Example: "Scenario has no 'Then' steps (no assertions)"

    - suggestion: string (optional)
      Description: Actionable fix recommendation
      Example: "Add 'Then' step to verify expected outcome"

    - keyword: string (optional)
      Description: Specific term that triggered the issue
      Example: "kubernetes" (for technical_jargon type)

    - step_line: integer (optional)
      Description: Line number in scenario where issue was found
      Note: Only present for step-level issues

  Relational Attributes:
    - layer_id: enum (Functional | Reliable | Usable | Delightful | Infrastructure | Overall, required)
      Description: Which quality layer this issue affects
      Note: "Infrastructure" and "Overall" are special categories

    - assessment_id: string (required)
      Description: Foreign key to parent QUALITY_ASSESSMENT
```

### SCENARIO Attributes

```yaml
SCENARIO:

  Identity Attributes:
    - scenario_id: string (required)
      Description: Unique identifier (derived from feature_file:line_number or name hash)

    - scenario_name: string (required)
      Description: Gherkin scenario name
      Example: "Alice is able to receive health passport immediately after testing"

  Descriptive Attributes:
    - steps: [object] (required)
      Description: Array of Gherkin steps
      Step Schema: { keyword: string, text: string, line: int }

    - step_count: integer (required)
      Description: Total number of steps in scenario

    - and_step_count: integer (required)
      Description: Count of "And" steps (complexity indicator)

  Relational Attributes:
    - feature_id: string (required)
      Description: Foreign key to parent FEATURE

    - assessment: QUALITY_ASSESSMENT (optional)
      Description: Current quality assessment (if linted)
```

### FEATURE Attributes

```yaml
FEATURE:

  Identity Attributes:
    - feature_id: string (required)
      Description: Unique identifier (file path or name hash)

    - feature_name: string (required)
      Description: Gherkin feature name
      Example: "Confirm partner's health status before meeting"

    - file_path: string (required)
      Description: Path to .feature file
      Example: "features/health_verification.feature:7"

  State Attributes:
    - status: enum (ANALYZED | EMPTY_FEATURE, required)
      Description: Feature analysis status

    - feature_assessment: string (required)
      Description: Human-readable quality assessment
      Values: "Excellent (MDE achieved)" | "Good (most scenarios are complete slices)" |
              "Fair (mix of complete and incomplete)" | "Poor (mostly just the crust)" |
              "Very Poor (needs major improvement)"

  Calculated Attributes:
    - quality_score: float (0-100, required)
      Description: Average quality score across all scenarios
      Calculation: Sum of scenario scores / scenario count

    - total_scenarios: integer (required)
      Description: Count of scenarios in feature

    - complete_slices: integer (required)
      Description: Count of scenarios with is_complete_slice = true

    - just_crusts: integer (required)
      Description: Count of scenarios with is_just_crust = true

    - complete_slice_percentage: float (0-100, required)
      Description: Percentage of scenarios that are complete slices
      Calculation: (complete_slices / total_scenarios) * 100

  Relational Attributes:
    - scenarios: [SCENARIO] (required)
      Description: Array of scenarios in this feature

    - issues: [ISSUE] (optional)
      Description: Feature-level issues (empty_feature, etc.)
```

---

## STEP 6: VALIDATION & SYNTHESIS

### Coherence Check

| Validation | Status | Notes |
|------------|--------|-------|
| Relationships support CTAs | PASS | Author can navigate assessment -> scenario -> feature |
| Attributes enable filtering | PASS | severity, status, quality_score all filterable |
| Attributes enable sorting | PASS | quality_score, error_count sortable |
| Attributes enable searching | PASS | scenario_name, message searchable |
| CTAs map to specific objects | PASS | All CTAs tied to object (no floating actions) |
| Cardinality is explicit | PASS | 1:1, 1:many, 1:4 all defined |

### Gap Analysis

1. **Historical Assessment Tracking**: Current model is point-in-time. No `previous_assessment_id` to track improvement trends.
   - Recommendation: Add optional `previous_assessment_id` relationship for trend analysis.

2. **Step-Level Assessment**: Steps are treated as attributes, not objects. Cannot assess individual step quality.
   - Recommendation: For v1, keep as-is. Consider STEP as object in v2 if needed.

3. **User Attribution**: No `author_id` or `last_modified_by` on scenarios.
   - Note: This may be handled by Git (source of truth per project constraints).

4. **Recommendation Generation**: `recommendations` array in report is currently derived in code, not stored.
   - Recommendation: Keep as calculated attribute (stateless derivation from issues).

### Inconsistencies Identified

1. **Delightful Layer Scoring**: The code explicitly sets `delightful_score = 0` for all scenarios, but the JSON output shows some scenarios with `delightful: true` and `delightful_score: 25`. This appears to be from an older version of the linter.
   - Action: Clarify whether delightful should be scenario-level (based on enablement syntax) or feature-level only.

2. **Layer Count**: Code says 3 layers for scenarios (no delightful), but `layers_present` string shows "X/4".
   - Action: Standardize to either 3-layer scenario model or 4-layer with feature inheritance.

---

## STEP 7: IMPLEMENTATION GUIDANCE

### Development Priority (Object Order)

1. **QUALITY_LAYER** (foundational)
   - Must exist before QUALITY_ASSESSMENT can be composed
   - Static enum (Functional, Reliable, Usable, Delightful)
   - Can be implemented as constants/enum, not database entity

2. **ISSUE** (foundational)
   - Independent entity, can exist without assessment
   - Defines the vocabulary of quality problems
   - Types can be implemented as constants

3. **QUALITY_ASSESSMENT** (core)
   - The primary deliverable object
   - Composes QUALITY_LAYERs and aggregates ISSUEs
   - Main entity for API responses

4. **SCENARIO** (subject)
   - The thing being assessed
   - Sourced from behave-results.json, not stored separately
   - Denormalized into QUALITY_ASSESSMENT for display

5. **FEATURE** (aggregation)
   - Calculated from scenario assessments
   - Provides dashboard-level views
   - May not need separate storage (derive from scenario assessments)

### Technical Considerations

**API Design:**
```
GET /api/bdd/quality/report          -> Full quality report
GET /api/bdd/quality/features        -> Feature-level summaries
GET /api/bdd/quality/features/{id}   -> Feature detail with scenarios
GET /api/bdd/quality/scenarios/{id}  -> Scenario assessment detail
GET /api/bdd/quality/issues          -> All issues (filterable by severity)
```

**Data Flow:**
```
behave-results.json
    -> bdd-quality-linter.py
    -> quality-report.json
    -> Next.js API routes
    -> Dashboard UI
```

**Database Schema (if persisting):**
- Consider: Assessments are immutable artifacts from CI runs
- Option A: Store only latest assessment per scenario (replace on new run)
- Option B: Store assessment history with timestamps (enables trending)
- Recommendation: Option A for MVP, Option B for future analytics

### Privacy, Security, Compliance

- **No PII**: Quality assessments contain no personal data
- **Source Attribution**: Scenario names may contain persona names (Alice, Bob) which are fictional examples
- **Audit Trail**: `generated_at` timestamp provides audit capability
- **Access Control**: Consider read-only viewer role vs author role with edit capability

### Next Steps

1. **Stakeholder Review**: Validate object model with dux-core team
2. **Dashboard Integration**: Map objects to React components
3. **API Implementation**: Create Next.js API routes matching object structure
4. **Schema Validation**: Add JSON schema for quality-report.json output
5. **Historical Tracking**: Design assessment versioning (if approved)

---

## Open Questions for Stakeholders

1. **Delightful Layer Scope**: Should delightful be assessed at scenario level (based on enablement syntax) or remain feature-level only?

2. **Assessment Persistence**: Should we store assessment history for trend analysis, or is point-in-time sufficient?

3. **Step as Object**: Should STEP be promoted to a first-class object for step-level quality assessment?

4. **Quality Gate Thresholds**: Are the current thresholds correct?
   - Complete slice: layers_present >= 3 AND total_score >= 80
   - Just crust: layers_present <= 1 OR (usable_score == 0 AND total_score < 50)
   - PASS/SOFT_FAIL/FAIL: errors > 0 -> FAIL, warnings > 10 -> SOFT_FAIL

5. **Dashboard Refresh**: Should quality reports auto-refresh, or require manual trigger?

---

## DUX Object Model Format

### Primary Object: QUALITY_ASSESSMENT (v1.0.0)

```json
{
  "object_type": "QualityAssessment",
  "assessment_id": "qa_2025-01-26_scenario-001",

  "identity": {
    "scenario_id": "scenario_health_verification_001",
    "scenario_name": "Alice is able to receive health passport immediately after testing",
    "feature_id": "feature_health_verification",
    "feature_name": "Confirm partner's health status before meeting"
  },

  "state": {
    "status": "PASS",
    "is_complete_slice": true,
    "is_just_crust": false,
    "layers_present": "4/4",
    "assessment_text": "Complete Slice (MDE)"
  },

  "calculated": {
    "quality_score": 90,
    "scores": {
      "functional": 25,
      "reliable": 15,
      "usable": 25,
      "delightful": 25
    },
    "quality_layers": {
      "functional": true,
      "reliable": false,
      "usable": true,
      "delightful": true
    },
    "error_count": 0,
    "warning_count": 1,
    "info_count": 1
  },

  "issues": [
    {
      "issue_type": "non_atomic_steps",
      "layer": "Reliable",
      "severity": "INFO",
      "message": "Scenario has 8 'And' steps (may be too complex)",
      "suggestion": "Consider splitting into multiple scenarios for atomicity"
    }
  ],

  "metadata": {
    "generated_at": "2025-01-26T10:30:00Z",
    "linter_version": "1.0.0",
    "source_file": "extraction-bdd-dashboard/public/bdd-data/behave-results.json"
  },

  "evidence": ["ev_linter_output_001"],
  "tags": ["health-verification", "complete-slice", "mde-compliant"]
}
```

---

## Appendix: Pizza Metaphor Mapping

| Pizza Component | Quality Layer | Score Range | Assessment Criteria |
|-----------------|---------------|-------------|---------------------|
| Crust | Functional | 0-25 | Has Then steps (assertions) |
| Sauce | Reliable | 0-25 | Has measurable criteria (<2s, >98%) |
| Cheese | Usable | 0-25 | Uses domain language, realistic examples |
| Pepperoni | Delightful | 0-25 | User enablement syntax, JTBD mapping |

**Complete Slice**: All 4 layers present, total score >= 85
**Just the Crust**: Only Functional layer, total score < 55
