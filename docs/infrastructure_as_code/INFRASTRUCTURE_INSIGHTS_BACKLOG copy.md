# 🏗️ Infrastructure Insights Backlog

This file captures repeatable patterns, prompt evolution, and infrastructure-as-code improvements discovered during development.

---

### Two-Stage Extraction Architecture Pattern
**Type**: Encoding  
**Timestamp**: 2025-07-07T13:30:00Z  
**Session**: docling-schema-validation-session  
**Context**: Docling parsing revealed job_statement decomposition needs evidence vs synthetic tracking per component  
**Description**: Extraction pipelines require dual-agent architecture: (1) Evidence Scraper Agent extracts verifiable data from sources, (2) Synthetic Injection Agent fills gaps with LLM hypotheses. This maintains evidence integrity, enables source tracking, and supports color-coding for transparency.

**Next Step**: Document this pattern as canonical extraction architecture for all DUX object types. Update agent prompt templates to reflect two-stage process.

---

### Evidence-Based Object Generation Orchestration Pattern
**Type**: Encoding  
**Timestamp**: 2025-07-07T13:35:00Z  
**Session**: docling-schema-validation-session  
**Context**: Refined understanding of archivist → advocate agent workflow with keyword matching and gap analysis  
**Description**: Non-LLM extraction orchestration: (1) Source parser scans transcript for canonical attribute keywords, (2) Keyword matching against fit template for user_scenario/user_enablement/user_outcome, (3) Gap analysis - requires evidence for user_scenario + one other component, (4) Promotion logic - 3 gaps = no promotion, (5) Cross-object generation - evidence triggers creation of linked Behavior (user_enablement) or Result (success_criteria constrained to 4 target impact types: revenue increase, ACV increase, cost reduction, profit increase).

**Next Step**: Config step for cost-conscious teams in magents.py extraction orchestrator. Implement 'fit' feature with dual modes: non-LLM based fit vs. LLM assisted fit for budget flexibility.

---

### Pipeline Separation: Governance vs Extraction vs Synthesis
**Type**: Encoding  
**Timestamp**: 2025-07-07T14:15:00Z  
**Session**: docling-schema-validation-session  
**Context**: Clarified scope boundaries between object model governance and operational pipelines  
**Description**: Three distinct pipeline responsibilities: (1) **Object Model Governance** - validates schema structure, required fields exist, field types correct, "lego piece interfaces" only; (2) **Extraction Pipeline** (magents.py) - creates object instances, DUX-opinionated relationship logic, populates relationship fields with actual IDs, "lego building"; (3) **Synthesis Pipeline** - analyzes existing instances, discovers patterns across relationships, generates reports/insights, analytics-level processing. Governance validates schema quality, NOT business logic or instance relationships.

**Next Step**: Document clear scope boundaries in governance validation architecture. Prevent scope creep into extraction/synthesis concerns.

---