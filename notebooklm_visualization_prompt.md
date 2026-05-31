# NotebookLM Studio Prompt for Kit v3 Gap Analysis

**Date**: 2026-05-27  
**Version**: 2.0 (Optimized for NotebookLM Studio capabilities)  
**Purpose**: Generate multimedia presentations using NotebookLM Studio's advanced features  
**Source Documents**: 
- `codebase_analysis.md` (Upstream DUX patterns - 47KB)
- `kit_v3_gap_analysis.md` (Downstream Kit v3 needs - 62KB)

---

## 🎯 How This Call-and-Response System Works

This is a **prompt command library** for NotebookLM Studio. Each command below is a complete, bespoke prompt you copy/paste into NotebookLM Chat to generate specific Studio outputs.

**Available Commands**:
- `/video-exec` - Executive briefing video (5-7 min)
- `/video-tech` - Technical deep dive video (7-10 min)
- `/video-week1` - Week 1 sprint kickoff video (3-5 min)
- `/audio-arch` - Architecture podcast for tech leads (15 min)
- `/audio-dev` - Developer implementation guide podcast (12 min)
- `/slides-arb` - Architecture Review Board deck (20 slides)
- `/slides-exec` - Executive summary deck (8 slides)
- `/slides-pm` - Project management tracking deck (15 slides)
- `/mindmap-arch` - Component architecture mind map
- `/mindmap-timeline` - 6-week implementation timeline map
- `/infographic-80-20` - Readiness breakdown infographic
- `/infographic-risk` - Risk assessment visual

**How to Use**:
1. Upload `codebase_analysis.md` + `kit_v3_gap_analysis.md` to NotebookLM
2. Find the command you need from the index below
3. Scroll to that command section and copy the entire bespoke prompt
4. Paste into NotebookLM Chat
5. Studio generates the output automatically

---

## 📑 Command Index - Quick Reference

### Video Overviews (Cinematic AI-Narrated Slideshows)
| Command | Audience | Duration | Purpose |
|---------|----------|----------|---------|
| `/video-exec` | C-suite, VPs | 5-7 min | Executive briefing (business focus, ROI) |
| `/video-tech` | Architects, Staff Engineers | 7-10 min | Technical deep dive (implementation details) |
| `/video-week1` | Developers | 3-5 min | Week 1 sprint kickoff (actionable tasks) |

### Audio Overviews (Podcast-Style Conversations)
| Command | Audience | Duration | Purpose |
|---------|----------|----------|---------|
| `/audio-arch` | Tech Directors, Principal Engineers | 15 min | Architecture patterns and decisions |
| `/audio-dev` | Mid-senior Developers | 12 min | Implementation guide (what to build/copy/avoid) |

### PowerPoint Decks (Editable .pptx Exports)
| Command | Audience | Slides | Purpose |
|---------|----------|--------|---------|
| `/slides-arb` | ARB Architects | 20 slides | Full architecture review deck |
| `/slides-exec` | Executives, Board | 8 slides | Business case and investment approval |
| `/slides-pm` | Project Managers | 15 slides | Sprint planning and status tracking |

### Mind Maps (Interactive Visual Node Maps)
| Command | Focus | Export | Purpose |
|---------|-------|--------|---------|
| `/mindmap-arch` | Component architecture | PNG | Technical documentation, onboarding |
| `/mindmap-timeline` | 6-week timeline | PNG | Sprint planning, dependency tracking |

### Infographics (Professional Data Visuals)
| Command | Theme | Export | Purpose |
|---------|-------|--------|---------|
| `/infographic-80-20` | Readiness breakdown | PNG/PDF | Stakeholder updates, proposals |
| `/infographic-risk` | Risk assessment | PNG/PDF | Risk reviews, confidence-building |

---

## 💡 Recommended Workflow by Role

**For Executives**: Start with `/video-exec` → Review `/slides-exec` → Use `/infographic-80-20` for board presentation  
**For Architects**: Start with `/video-tech` → Listen to `/audio-arch` → Review `/slides-arb` → Reference `/mindmap-arch`  
**For Developers**: Watch `/video-week1` → Listen to `/audio-dev` while coding → Reference `/mindmap-timeline` for tasks  
**For Project Managers**: Generate `/slides-pm` → Track with `/mindmap-timeline` → Report with `/infographic-risk`

---

## Instructions for NotebookLM Studio

I'm providing two comprehensive technical analysis documents about the DUX Object Model Core repository and its relationship to the Kit v3 downstream promotion. Please use **NotebookLM Studio features** to create multimedia presentations, mind maps, infographics, and video overviews suitable for executive review, architecture decision-making, and project planning.

### Studio Features to Leverage:
- 🎬 **Video Overviews** - AI-narrated slideshows (Cinematic mode for executive briefing)
- 🧠 **Mind Maps** - Interactive visual node maps (export as PNG images)
- 📊 **Infographics** - Themed structural infographics (highlighting gaps and roadmap)
- 📑 **PowerPoint Export** - Editable .pptx slide decks (customizable for stakeholders)
- 🎙️ **Audio Overviews** - Podcast-style conversational summaries (interactive Q&A)
- 💬 **Interactive Chat** - Deep research queries, quizzes, flashcards, study guides

---

## 📚 Command Library - Bespoke Prompts for Studio

Copy and paste these complete prompts into NotebookLM Chat to generate specific Studio outputs.

---

### `/video-exec` - Executive Briefing Video

**Copy this entire prompt into NotebookLM Chat:**

```
Using the uploaded sources (codebase_analysis.md and kit_v3_gap_analysis.md), create a Cinematic Video Overview for corporate executives and senior leadership.

Title: "Kit v3 Object Promotion - Architecture Review"
Duration: 5-7 minutes
Target Audience: C-suite, VPs, Executive Directors
Tone: Business-focused, emphasize ROI and risk mitigation

Slide Structure:
1. Opening: "Kit v3: Promoting 8 Objects from Upstream to Downstream"
2. The Big Number: "80% Infrastructure Already Production-Ready" (emphasize cost savings)
3. What We're Reusing: 6-stage validation pipeline, Docling parser, Evidence patterns, BDD generation
4. The 20% Gap: 3 critical components - Template System, Hash Validation, ORCA Validators
5. Timeline: 6 weeks from foundation to launch (show weekly milestones)
6. Golden Fixture: CAREERS-171 as reference implementation (explain quality gate)
7. Risk Management: 5 P0 risks identified with mitigation plans in place
8. Success Metrics: 6 launch criteria (Outcome v3 reproducibility, all-8-objects hashes, evidence coverage)
9. Call to Action: Week 1 Foundation Sprint starts Monday (Template + Hash system)

Visual Style: Clean, professional charts. Emphasize numbers (80%, 6 weeks, 8 objects, 5 risks).
Narration Style: Confident, business-savvy, focused on "why this matters" not technical details.
```

**Expected Output**: 5-7 minute video (.mp4) suitable for board presentations

---

### `/video-tech` - Technical Deep Dive Video

**Copy this entire prompt into NotebookLM Chat:**

```
Using the uploaded sources (codebase_analysis.md and kit_v3_gap_analysis.md), create a Cinematic Video Overview for architects and senior developers.

Title: "Kit v3 Architecture - Upstream Patterns and Downstream Implementation"
Duration: 7-10 minutes
Target Audience: Tech Leads, Principal Engineers, Staff Engineers
Tone: Technical, detailed, implementation-focused

Slide Structure:
1. Opening: Architecture overview (upstream DUX core → downstream Kit v3)
2. Validation Pipeline Evolution: 6 stages (upstream) → 9 stages (downstream)
   - Show what's added: Stage 0 (Linear extraction), Stage 2.5 (ORCA), Stage 3.5 (Injection), Stage 4.5 (Byte hash), Stage 5.5 (Structural hash), Stage 7-8
3. The Docling Breakthrough: table.data.grid pattern (NOT regex)
   - Code snippet visual showing correct vs broken approach
4. Deterministic Generation: Why byte-identical hashes matter
   - Template injection with sorted dicts, Jinja2 settings
5. ORCA Meta-Metadata: New validation layer
   - bucket, core_vs_supporting, evidence_requirement, synthetic_allowed
6. Golden Fixture Workflow: CAREERS-171 → Outcome v3
   - Extract → Inject → Hash → Register → Test (3 runs must match)
7. All-8-Objects Sequencing: Outcome → Core Trio → Credential Group → Fit
8. P0 Gap Components: What must be built (template injector, hash calculator, ORCA validators)
9. Week 1 Technical Tasks: Jinja2 templates, byte hash logic, Linear integration

Visual Style: Code snippets, architecture diagrams, technical flowcharts.
Narration Style: Precise, uses correct terminology, explains "how" not just "what".
```

**Expected Output**: 7-10 minute video (.mp4) for architecture review sessions

---

### `/video-week1` - Week 1 Sprint Kickoff Video

**Copy this entire prompt into NotebookLM Chat:**

```
Using the uploaded sources (codebase_analysis.md and kit_v3_gap_analysis.md), create a Cinematic Video Overview for the development team starting Week 1 implementation.

Title: "Week 1 Foundation Sprint - Getting Started with Kit v3"
Duration: 3-5 minutes
Target Audience: Developers assigned to Week 1 Foundation Sprint
Tone: Practical, actionable, motivating

Slide Structure:
1. Sprint Goal: Build the foundation (Template System + Hash Validation + Linear Integration)
2. What We're Building (3 components):
   - Deterministic Template Injector (Jinja2 + sorted dicts)
   - Byte Hash Calculator + Golden Hash Registry
   - Linear Extraction (CAREERS-171 → injection contract JSON)
3. Success Criteria for Week 1:
   - Outcome v3 generated from template
   - Golden hash calculated: sha256:abc123...
   - Hash reproducible across 3 runs (byte-identical)
   - Hash registered in golden_hashes.json
4. Files to Reference:
   - Copy: fixed_docling_parser.py (upstream pattern)
   - Study: stage1_structure_validation.py, stage2_consistency_validation.py
   - Build: inject_canonical_object_deterministic(), calculate_canonical_hash()
5. Day-by-Day Breakdown:
   - Day 1-2: Template system (Jinja2 templates, sorted dict iteration)
   - Day 3-4: Hash system (byte hash, structural hash, registry)
   - Day 5-7: Linear integration, Outcome v3 generation, reproducibility test
6. Blockers to Watch: Non-deterministic rendering, stale cached schema, hand-edited projections
7. Definition of Done: All 3 runs produce sha256:abc123... (golden hash established)

Visual Style: Task checklists, code snippets, file references.
Narration Style: Clear, step-by-step, encouraging.
```

**Expected Output**: 3-5 minute video (.mp4) for sprint planning meeting

---

### `/audio-arch` - Architecture Leadership Podcast

**Copy this entire prompt into NotebookLM Chat:**

```
Using the uploaded sources (codebase_analysis.md and kit_v3_gap_analysis.md), create an Audio Overview in podcast format for architecture leaders.

Title: "Kit v3 Architecture Deep Dive - Patterns, Gaps, and Decisions"
Duration: 15 minutes
Target Audience: Staff Engineers, Principal Architects, Tech Directors
Format: Two-host conversational podcast
Tone: Thoughtful, exploratory, decision-oriented

Discussion Topics (in order):
1. Opening: What is Kit v3 and why does object promotion matter?
2. The 80/20 Discovery: 80% of infrastructure is production-ready
   - What does "production-ready" mean in this context?
   - Which upstream patterns are most valuable?
3. The Docling Breakthrough: table.data.grid vs regex parsing
   - Why was the original parser broken?
   - How does structured extraction solve it?
4. Byte Hash Philosophy: Why canonical governance requires reproducibility
   - What's the difference between byte hash and structural hash?
   - When would byte hash pass but structural hash fail (or vice versa)?
5. ORCA Meta-Metadata: Extending evidence attribution
   - What's new compared to upstream Evidence objects?
   - Why does bucket classification matter?
6. The Golden Fixture Workflow: CAREERS-171 as quality gate
   - How does one object (Outcome v3) validate the entire system?
   - What happens if golden hash doesn't reproduce?
7. Risk Deep Dive: The 5 P0 failure modes
   - Tuning bleed: How semantic tuning could leak into canon
   - Validator overfitting: Why CAREERS-171 is data, not rules
   - Non-deterministic rendering: The sorted dict solution
8. Architecture Decisions Ahead: What ARB needs to review
   - Template scaffold structure (canonical vs run metadata)
   - Injection contract format (ORCA buckets specification)
   - HITL routing logic (hash-aware failure classification)
9. Closing: Week 1 critical path and success criteria

Interactive Moments (users can interrupt to ask):
- "Explain byte hash calculation step-by-step"
- "Give a concrete example of tuning bleed"
- "How does the golden fixture prevent regression?"
- "What if we need to change a canonical section?"
```

**Expected Output**: 15-minute podcast (.mp3) for architecture team listening

---

### `/audio-dev` - Developer Implementation Guide Podcast

**Copy this entire prompt into NotebookLM Chat:**

```
Using the uploaded sources (codebase_analysis.md and kit_v3_gap_analysis.md), create an Audio Overview in podcast format for developers implementing Kit v3.

Title: "Kit v3 Developer Guide - What to Build, Copy, and Avoid"
Duration: 12 minutes
Target Audience: Mid-senior developers assigned to Kit v3 implementation
Format: Two-host conversational podcast
Tone: Practical, code-focused, tutorial-style

Discussion Topics (in order):
1. Opening: Your mission - promote 8 objects with byte-identical validation
2. What to Copy As-Is (80% reusable):
   - stage1_structure_validation.py - markdown template checks
   - stage2_consistency_validation.py - schema ↔ JSON consistency
   - fixed_docling_parser.py - THE breakthrough pattern
   - Walk through: How to use extract_schema_table_from_docling()
3. What to Adapt (10% customization):
   - Stage 3b validators - add Kit v3 object schemas
   - Stage 4 validators - write bespoke validators for 8 objects
   - HITL routing - add hash-aware failure classification
4. What to Build from Scratch (10% new):
   - Deterministic template injector: inject_canonical_object_deterministic()
     Code walkthrough: Jinja2 settings, deep_sort_dict(), line ending normalization
   - Byte hash calculator: calculate_canonical_hash()
     Code walkthrough: Extract canonical sections, SHA256, reproducibility
   - Golden hash registry: GoldenHashRegistry class
     Code walkthrough: register_golden_hash(), validate_against_golden()
   - Linear integration: extract_injection_contract_from_linear()
     Code walkthrough: Fetch issue, parse markdown, extract ORCA buckets
5. What to AVOID (broken patterns):
   - parse_problem_object.py - uses regex, ignores DoclingDocument structure
   - Self-confidence scoring - not evidence-based
   - Corpus-specific schema fields - canon must be invariant
6. Week 1 Implementation Tasks:
   - Day 1-2: Create outcome_v3_template.md (Jinja2), test template rendering
   - Day 3-4: Build hash calculator, test on example markdown
   - Day 5-7: Extract CAREERS-171, inject, calculate golden hash, test 3x
7. Common Pitfalls:
   - Forgetting to sort dict keys (breaks determinism)
   - CRLF line endings (normalize to LF)
   - Including run metadata in canonical sections (timestamp leaks)
8. Testing Your Work:
   - Golden fixture test: Regenerate 3 times, hashes must match
   - Structural hash test: Perturb structure, hash should change
   - Evidence coverage test: All core attributes have evidence
9. Closing: Resources and where to get help

Interactive Moments (users can interrupt to ask):
- "Show me the deep_sort_dict() implementation"
- "How do I debug if byte hash doesn't match?"
- "Which Jinja2 settings ensure deterministic rendering?"
- "Walk through the golden fixture test code"
```

**Expected Output**: 12-minute podcast (.mp3) for developer onboarding

---

### `/slides-arb` - Architecture Review Board Deck

**Copy this entire prompt into NotebookLM Chat:**

```
Using the uploaded sources (codebase_analysis.md and kit_v3_gap_analysis.md), export a PowerPoint presentation for the Architecture Review Board.

Title: "Kit v3 Object Promotion - ARB Architecture Review"
Slide Count: 20 slides
Target Audience: ARB architects (Case, Hugh, Jorge, Chaya, Sophia)
Purpose: Approval to proceed with implementation

Slide Structure:

SECTION 1: EXECUTIVE SUMMARY (Slides 1-3)
1. Title + Agenda
2. The Ask: Approve Kit v3 promotion (8 objects, 6 weeks, 3 P0 gaps to build)
3. TL;DR: 80% reusable, 20% gaps, golden fixture approach validated

SECTION 2: UPSTREAM ANALYSIS (Slides 4-7)
4. DUX Object Model Core - What We Inherit
   - 6-stage validation pipeline (production-ready)
   - Docling structured extraction (breakthrough pattern)
   - Evidence-based validation (no self-confidence)
   - HITL queue management (proven workflow)
5. The Docling Breakthrough: table.data.grid
   - Visual: Code comparison (structured vs regex)
   - Impact: Deterministic, reliable, scales to all 8 objects
6. Upstream Validation Gates
   - Stage 1: Structure (markdown template)
   - Stage 2: Consistency (schema ↔ JSON)
   - Stages 3-6: Processing, validation, generation
7. What's Production-Ready (80%)
   - List: 7 components we copy as-is
   - Confidence level: High (battle-tested in DUX Core)

SECTION 3: GAP ANALYSIS (Slides 8-12)
8. The 20% Gap - What Must Be Built
   - P0 Critical: Template System, Hash Validation, ORCA Validators
   - P1 Quality: Forbidden Vocabulary, BDD Projection, Regression Suite
9. Deterministic Generation Gap
   - Missing: Jinja2 templates, injection API, sorted dict iteration
   - Risk: Non-deterministic rendering breaks byte hash
   - Mitigation: Week 1 priority, clear implementation pattern
10. Hash Validation Gap
    - Missing: Byte hash calculator, structural hash, golden hash registry
    - Risk: No quality gate for canonical governance
    - Mitigation: Golden fixture workflow (CAREERS-171)
11. ORCA Extension Gap
    - Missing: Meta-metadata validator (bucket, core_vs_supporting, evidence_requirement)
    - Risk: Evidence attribution incomplete
    - Mitigation: Extend Stage 2 consistency validation
12. Gap Summary Table
    - Component | Upstream | Downstream | Priority | Effort
    - (Show all 10 key components)

SECTION 4: IMPLEMENTATION PLAN (Slides 13-16)
13. 6-Week Timeline
    - Week 1: Foundation (templates, hashes, Linear)
    - Weeks 2: Validators (ORCA, routing, extension)
    - Weeks 3-5: All-8-Objects (sequential promotion)
    - Week 6: Quality gates (regression, documentation)
14. Golden Fixture Workflow (CAREERS-171 → Outcome v3)
    - Extract from Linear → Injection contract
    - Inject into template → Generated .md
    - Calculate byte hash → sha256:abc123...
    - Register golden hash → Quality gate
    - Test reproducibility → 3 runs must match
15. All-8-Objects Sequencing
    - Phase 1: Outcome (Week 1 golden fixture)
    - Phase 2: User, Skill, Requirement (Weeks 2-3)
    - Phase 3: Credential, Qualification, Standard (Week 4)
    - Phase 4: Fit (Week 5 integration)
16. Success Metrics (6 P0 Criteria)
    - Outcome v3 hash reproducible
    - All 8 objects have golden hashes
    - Deterministic generation (100% stable)
    - ORCA coverage (100% core attributes)
    - Evidence attribution (100% core)
    - Validation pass rate (100% golden fixtures)

SECTION 5: RISK ASSESSMENT (Slides 17-18)
17. P0 Risks (5 Critical)
    - Non-deterministic rendering → Sorted dicts + Jinja2 settings
    - Stale cached schema → Version alignment check
    - Hand-edited projections → Watermarks + pre-commit hooks
    - Tuning bleed → Forbidden vocabulary validator
    - Validator overfitting → Validate against synthetic examples
18. Risk Matrix
    - Impact vs Probability (2x2)
    - Show all 9 risks with mitigation status

SECTION 6: DECISION POINTS (Slides 19-20)
19. ARB Review Questions
    - Is the 80/20 split acceptable?
    - Is golden fixture approach sound?
    - Are P0 gaps buildable in Week 1?
    - Should we proceed with all-8-objects or pilot with Outcome v3?
20. Next Steps + Approval
    - ARB approval by: [DATE]
    - Week 1 sprint starts: [DATE]
    - Outcome v3 golden fixture: [DATE]
    - All-8-objects complete: [DATE]

Speaker Notes: Include detailed technical notes for each slide
Export Format: Editable .pptx with embedded charts and diagrams
```

**Expected Output**: 20-slide PowerPoint deck (.pptx) for ARB review

---

### `/slides-exec` - Executive Summary Deck

**Copy this entire prompt into NotebookLM Chat:**

```
Using the uploaded sources (codebase_analysis.md and kit_v3_gap_analysis.md), export a PowerPoint presentation for executive leadership.

Title: "Kit v3 Object Promotion - Executive Summary"
Slide Count: 8 slides
Target Audience: C-suite, VPs, Board members
Purpose: Business case and investment approval

Slide Structure:

1. TITLE: Kit v3 Object Promotion - Investment Request
   - Subtitle: 8 Objects, 6 Weeks, 80% Reusable Infrastructure

2. THE OPPORTUNITY
   - Promote 8 core objects from upstream to downstream
   - Leverage existing production-ready infrastructure (80%)
   - Build only critical gaps (20%)
   - ROI: Accelerated time-to-market with validated architecture

3. THE 80/20 SPLIT (Visual Emphasis)
   - Large pie chart: 80% Green (Production-Ready), 20% Red (Build)
   - Cost savings: Reusing $X worth of R&D investment
   - Risk reduction: Proven patterns, not experimental

4. WHAT WE'RE BUILDING (3 Critical Components)
   - Template System: Deterministic object generation
   - Hash Validation: Quality gate for canonical governance
   - ORCA Validators: Evidence-based attribution
   - Timeline: Week 1 foundation sprint

5. 6-WEEK TIMELINE
   - Week 1: Foundation (templates + hashes)
   - Weeks 2-5: Promote all 8 objects sequentially
   - Week 6: Quality gates and launch readiness
   - Milestones: Golden fixture, Core trio, All-8-objects

6. RISK MANAGEMENT
   - 5 P0 risks identified with mitigation plans
   - All risks addressable in Week 1-2
   - Golden fixture approach validates quality early

7. SUCCESS METRICS (What "Done" Looks Like)
   - 8/8 objects have stable golden hashes
   - 100% evidence attribution for core attributes
   - Byte-identical regeneration (reproducibility)
   - Regression suite passing (100%)

8. THE ASK + NEXT STEPS
   - Investment: [TEAM SIZE] developers for 6 weeks
   - Decision needed by: [DATE]
   - Sprint starts: [DATE]
   - Expected completion: [DATE]
   - ROI: Production-ready object model for Kit v3

Visual Style: Minimal text, large numbers, clean charts
Tone: Business-focused, ROI-driven, risk-aware
```

**Expected Output**: 8-slide executive deck (.pptx)

---

### `/slides-pm` - Project Management Deck

**Copy this entire prompt into NotebookLM Chat:**

```
Using the uploaded sources (codebase_analysis.md and kit_v3_gap_analysis.md), export a PowerPoint presentation for project tracking.

Title: "Kit v3 Implementation - Project Plan & Status"
Slide Count: 15 slides
Target Audience: Project Managers, Scrum Masters, Engineering Managers
Purpose: Sprint planning, status tracking, blocker management

Slide Structure:

1. TITLE: Kit v3 6-Week Implementation Plan

2. PROJECT OVERVIEW
   - Goal: Promote 8 objects with validated governance
   - Timeline: 6 weeks (foundation → all-8-objects → quality)
   - Team: [SIZE] developers, [ARB ARCHITECTS] reviewers
   - Deliverables: 8 golden fixture objects + validation infrastructure

3. WORK BREAKDOWN (3 Phases)
   - Phase 1: Foundation (Week 1) - 3 P0 components
   - Phase 2: Object Promotion (Weeks 2-5) - 8 objects sequentially
   - Phase 3: Quality Gates (Week 6) - Regression suite

4. WEEK 1 SPRINT PLAN (Foundation)
   - Sprint Goal: Establish golden fixture for Outcome v3
   - Tasks:
     * Build deterministic template injector (2 days)
     * Build byte hash calculator + registry (2 days)
     * Extract CAREERS-171 from Linear (3 days)
     * Test reproducibility (3 runs must match)
   - Definition of Done: sha256:abc123... registered as golden hash

5. WEEK 2 SPRINT PLAN (Validators)
   - Sprint Goal: Extend validation pipeline with ORCA + Hash gates
   - Tasks:
     * Build ORCA meta-metadata validator
     * Build byte hash validation (Stage 4.5)
     * Build structural hash validation (Stage 5.5)
     * Update HITL routing logic

6. WEEKS 3-5 SPRINT PLAN (All-8-Objects)
   - Week 3: User, Skill, Requirement (Core Trio)
   - Week 4: Credential, Qualification, Standard (Credential Group)
   - Week 5: Fit object + cross-object validation
   - Each object: Extract → Template → Inject → Hash → Register

7. WEEK 6 SPRINT PLAN (Quality)
   - Sprint Goal: Launch-ready quality gates
   - Tasks:
     * Build forbidden vocabulary validator
     * Build BDD projection validator
     * Create regression test suite (8 fixtures)
     * Documentation + runbooks

8. DEPENDENCIES & BLOCKERS
   - Week 1 blocks all other work (critical path)
   - Linear API access required (CAREERS-171 extraction)
   - ARB review approval before all-8-objects phase
   - Golden hash must be reproducible (quality gate)

9. RISK REGISTER
   - Risk | Impact | Probability | Mitigation | Owner
   - (Show all 9 risks from gap analysis)

10. SUCCESS METRICS DASHBOARD
    - P0 Metrics (6 launch blockers) - Current status
    - P1 Metrics (5 quality indicators) - Target status
    - Update frequency: Weekly sprint review

11. STATUS TRACKING (Template for Weekly Updates)
    - Completed this week: [TASKS]
    - In progress: [TASKS]
    - Blocked: [BLOCKERS]
    - Next week plan: [TASKS]
    - Risks elevated: [NEW RISKS]

12. RESOURCE ALLOCATION
    - Week 1: 100% team on foundation
    - Weeks 2-5: Parallel tracks (validators + objects)
    - Week 6: Quality focus (regression + docs)
    - ARB bandwidth: 2 hours/week for reviews

13. COMMUNICATION PLAN
    - Daily: Stand-ups (15 min)
    - Weekly: Sprint reviews with ARB
    - Bi-weekly: Executive status update
    - Ad-hoc: Blocker escalation protocol

14. ACCEPTANCE CRITERIA (What "Done" Looks Like)
    - [ ] All 8 objects have golden hashes
    - [ ] Byte hash reproducible across 3 runs
    - [ ] ORCA coverage 100% for core attributes
    - [ ] Evidence attribution 100% for core
    - [ ] Regression suite passing
    - [ ] Documentation complete

15. GO/NO-GO DECISION GATES
    - Gate 1 (End of Week 1): Golden fixture established
    - Gate 2 (End of Week 3): Core trio validated
    - Gate 3 (End of Week 5): All-8-objects complete
    - Gate 4 (End of Week 6): Quality gates passed → LAUNCH

Export Format: Editable .pptx with tracking tables and charts
```

**Expected Output**: 15-slide PM tracking deck (.pptx)

---

### `/mindmap-arch` - Component Architecture Mind Map

**Copy this entire prompt into NotebookLM Chat:**

```
Using the uploaded sources (codebase_analysis.md and kit_v3_gap_analysis.md), create a Mind Map visualization of the Kit v3 component architecture.

Title: "Kit v3 Component Architecture"
Root Node: "Kit v3 Object Promotion"
Layout: Radial (root in center, branches radiating outward)
Export: PNG image (high resolution for documentation)

Primary Branches (Level 1):

1. UPSTREAM PATTERNS (Green nodes)
   - 6-Stage Validation Pipeline
     - Stage 1: Structure Validation
     - Stage 2: Consistency Validation
     - Stage 3: Docling Processing
     - Stage 4: Object Validation
     - Stage 5: BDD Generation
     - Stage 6: Prompt Generation
   - Docling Parser (table.data.grid)
   - Evidence Attribution
   - HITL Queue Management
   - BDD Feature Template

2. GAP COMPONENTS (Red nodes - Must Build)
   - Template System
     - Jinja2 Templates (8 objects)
     - Deterministic Injector
     - Sorted Dict Iteration
   - Hash Validation
     - Byte Hash Calculator
     - Structural Hash
     - Golden Hash Registry
   - ORCA Validators
     - Meta-Metadata Validator
     - Bucket Classification
     - Evidence Requirement Check
   - Linear Integration
     - Extract CAREERS-171
     - Injection Contract Format

3. TARGET OBJECTS (Blue nodes - 8 Objects)
   - Phase 1: Outcome v3 (Golden Fixture)
   - Phase 2: Core Trio
     - User v3
     - Skill v3
     - Requirement v3
   - Phase 3: Credential Group
     - Credential v3
     - Qualification v3
     - Standard v3
   - Phase 4: Fit v3 (Integration)

4. VALIDATION GATES (Purple nodes - Quality)
   - Stage 0: Linear Extraction
   - Stage 2.5: ORCA Validation
   - Stage 3.5: Template Injection
   - Stage 4.5: Byte Hash Gate
   - Stage 5.5: Structural Hash Gate
   - Stage 7: BDD Projection Validation
   - Stage 8: Forbidden Vocabulary

5. RISK MITIGATION (Orange nodes - P0 Risks)
   - Non-deterministic Rendering
     - Jinja2 Settings
     - Sorted Dicts
     - Line Ending Normalization
   - Tuning Bleed Prevention
     - Forbidden Vocabulary Check
     - Separate Extraction Lens
   - Stale Schema Detection
     - Version Alignment Check
   - Hand-Edit Prevention
     - Watermarks
     - Pre-commit Hooks
   - Validator Independence
     - Test with Synthetic Examples

Interactive Features:
- Clickable nodes: Expand to show more detail
- Color coding: Green=Ready, Red=Build, Blue=Target, Purple=Gates, Orange=Risks
- Hover tooltips: Show descriptions from source documents

Use Case: Architecture reviews, onboarding, technical documentation
```

**Expected Output**: Interactive mind map (exportable as PNG)

---

### `/mindmap-timeline` - 6-Week Implementation Timeline Map

**Copy this entire prompt into NotebookLM Chat:**

```
Using the uploaded sources (codebase_analysis.md and kit_v3_gap_analysis.md), create a Mind Map visualization of the 6-week implementation timeline.

Title: "Kit v3 6-Week Implementation Timeline"
Root Node: "6-Week Sprint Plan"
Layout: Hierarchical (top-down or left-right)
Export: PNG image (high resolution)

Primary Branches (Level 1 - Weeks):

1. WEEK 1: FOUNDATION (Purple - Critical Path)
   - Day 1-2: Template System
     - Create outcome_v3_template.md (Jinja2)
     - Build inject_canonical_object_deterministic()
     - Implement deep_sort_dict()
     - Test: Same input → Same output (3 runs)
   - Day 3-4: Hash System
     - Build calculate_canonical_hash()
     - Build calculate_structural_hash()
     - Implement GoldenHashRegistry class
     - Test: Hash stability across regenerations
   - Day 5-7: Linear Integration
     - Build extract_injection_contract_from_linear()
     - Extract CAREERS-171 → injection contract JSON
     - Generate Outcome v3 → Calculate golden hash
     - Register: outcome_v3:sha256:abc123...
   - MILESTONE: Golden Fixture Established

2. WEEK 2: VALIDATION EXTENSIONS (Blue)
   - Day 1-2: ORCA Validators
     - Build validate_orca_metadata() (Stage 2.5)
     - Add ORCA fields to injection contract schema
     - Test against Outcome v3 contract
   - Day 3-4: Hash Validators
     - Build validate_byte_hash() (Stage 4.5)
     - Build validate_structural_hash() (Stage 5.5)
     - Integrate into hitl_orchestrator.py
   - Day 5-7: Routing Logic
     - Extend HITL routing for hash failures
     - Add hash_verification/ queue folder
     - Test full pipeline: Linear → Golden Hash
   - MILESTONE: Extended Pipeline Operational

3. WEEK 3: CORE TRIO (Green - Parallel Track)
   - User v3
     - Template creation
     - Injection from Linear or synthetic
     - Golden hash: user_v3:sha256:...
   - Skill v3
     - Template creation
     - Injection
     - Golden hash: skill_v3:sha256:...
   - Requirement v3
     - Template creation
     - Injection
     - Golden hash: requirement_v3:sha256:...
   - MILESTONE: Core Trio Complete (4/8 objects)

4. WEEK 4: CREDENTIAL GROUP (Green - Parallel Track)
   - Credential v3
     - Template + Injection + Hash
   - Qualification v3
     - Template + Injection + Hash
   - Standard v3
     - Template + Injection + Hash
   - Cross-object validation
     - Evidence references resolve
     - Relationship integrity checks
   - MILESTONE: Credential Group Complete (7/8 objects)

5. WEEK 5: FIT + INTEGRATION (Green)
   - Fit v3
     - Template + Injection + Hash
   - Cross-object evidence validation
   - ORCA relationship graph validation
   - Final integration tests
   - MILESTONE: All-8-Objects Complete

6. WEEK 6: QUALITY GATES (Orange - Launch Prep)
   - Day 1-3: Additional Validators
     - Build validate_forbidden_vocabulary() (Stage 8)
     - Build validate_bdd_projection() (Stage 7)
     - Add watermark system
     - Pre-commit hook for projection integrity
   - Day 4-7: Regression Suite
     - Create regression tests (8 golden fixtures)
     - Add CI/CD pipeline
     - Document validation rules
     - Write operator runbook
   - MILESTONE: Launch Ready

Decision Gates (Diamonds on Timeline):
- Gate 1 (End Week 1): Golden fixture? GO/NO-GO
- Gate 2 (End Week 3): Core trio validated? GO/NO-GO
- Gate 3 (End Week 5): All-8-objects? GO/NO-GO
- Gate 4 (End Week 6): Quality gates passed? LAUNCH

Color Legend:
- Purple = Critical path (Week 1 blocks all)
- Blue = Validation infrastructure
- Green = Object promotion
- Orange = Quality & launch prep
- Diamonds = Decision gates

Use Case: Sprint planning, dependency tracking, status visualization
```

**Expected Output**: Timeline mind map (exportable as PNG)

---

### `/infographic-80-20` - Readiness Breakdown Infographic

**Copy this entire prompt into NotebookLM Chat:**

```
Using the uploaded sources (codebase_analysis.md and kit_v3_gap_analysis.md), create an Infographic showing the 80/20 readiness breakdown.

Title: "Kit v3 Infrastructure Readiness - 80% Production-Ready"
Theme: Technical architecture gap analysis
Style: Clean, professional, data-driven
Export: PNG or PDF (high resolution for presentations)

Visual Hierarchy (Top to Bottom):

1. HEADLINE NUMBER (Dominant)
   - Giant "80%" in green
   - Subtitle: "Production-Ready Infrastructure"
   - Supporting text: "$X worth of R&D investment reusable"

2. THE 80% BREAKDOWN (What We're Reusing)
   Icons + labels for each component:
   - ✅ 6-Stage Validation Pipeline
   - ✅ Docling Structured Parser (breakthrough)
   - ✅ Evidence Attribution Pattern
   - ✅ HITL Queue Management
   - ✅ BDD Feature Generator
   - ✅ Prompt Generator
   - ✅ Canonical Object Templates

3. THE 20% GAP (What We're Building)
   Split into two columns:
   
   LEFT - 10% NEEDS ADAPTATION (Yellow)
   - ⚠️ Stage 3b: Kit v3 schemas
   - ⚠️ Stage 4: Bespoke validators (8 objects)
   - ⚠️ HITL Routing: Hash-aware logic
   
   RIGHT - 10% MUST BUILD NEW (Red)
   - ❌ Template System (Jinja2)
   - ❌ Hash Validation (Byte + Structural)
   - ❌ ORCA Validators
   - ❌ Linear Integration

4. TIMELINE BAR (Visual Progress)
   - 6-week horizontal bar
   - Week 1: Foundation (20% gap components) - Red zone
   - Weeks 2-5: Object promotion (using 80% infrastructure) - Green zone
   - Week 6: Quality gates - Orange zone

5. RISK INDICATOR (Bottom Right)
   - Small box: "5 P0 Risks Identified"
   - All mitigable in Weeks 1-2
   - Mitigation plans in place

6. SUCCESS GATE (Bottom Left)
   - Small box: "6 P0 Launch Criteria"
   - Outcome v3 reproducible
   - All 8 objects validated
   - Evidence coverage 100%

Visual Design Notes:
- Use actual percentages as large numbers
- Color coding: Green (ready), Yellow (adapt), Red (build)
- Icons for each component (gear for pipeline, lock for validation, etc.)
- Clean whitespace, minimal text
- Emphasis on "80% ready" as the dominant message

Use Case: Executive presentations, stakeholder updates, project proposals
```

**Expected Output**: Professional infographic (PNG or PDF)

---

### `/infographic-risk` - Risk Assessment Visual

**Copy this entire prompt into NotebookLM Chat:**

```
Using the uploaded sources (codebase_analysis.md and kit_v3_gap_analysis.md), create an Infographic showing the risk assessment and mitigation strategy.

Title: "Kit v3 Risk Assessment - 5 P0 Risks with Mitigation Plans"
Theme: Risk management and mitigation tracking
Style: Clear, actionable, confidence-building
Export: PNG or PDF (high resolution)

Visual Layout (2x2 Matrix + List):

1. HEADER: Risk Impact-Probability Matrix
   - 2x2 grid: X-axis (Probability: Low → High), Y-axis (Impact: Low → High)
   - Quadrants labeled:
     * Top-Left: High Impact, Low Probability (Monitor)
     * Top-Right: High Impact, High Probability (P0 - Mitigate Now)
     * Bottom-Left: Low Impact, Low Probability (Accept)
     * Bottom-Right: Low Impact, High Probability (P1 - Track)

2. PLOT RISKS ON MATRIX
   Plot as circles with labels:
   
   TOP-RIGHT QUADRANT (P0 - Red circles):
   - Non-deterministic Rendering (large circle)
   - Stale Cached Schema (medium circle)
   - Hand-Edited Projections (medium circle)
   - Tuning Bleed (medium circle)
   - Validator Overfitting (medium circle)
   
   BOTTOM-RIGHT QUADRANT (P1 - Yellow circles):
   - BDD Projection Drift (small circle)
   - Evidence Coverage Gaps (small circle)
   - Cross-Object Reference Breakage (small circle)
   - Template Divergence (small circle)

3. MITIGATION TIMELINE (Horizontal Bar Below Matrix)
   Show when each P0 risk is mitigated:
   - Week 1: Non-deterministic rendering (Jinja2 + sorted dicts) → Green checkmark
   - Week 1: Stale cached schema (version alignment) → Green checkmark
   - Week 2: Tuning bleed (forbidden vocabulary) → Green checkmark
   - Week 6: Hand-edits (watermarks + hooks) → Green checkmark
   - Week 6: Validator overfitting (synthetic tests) → Green checkmark

4. RISK DETAIL CARDS (Right Side)
   For each P0 risk, show compact card:
   
   CARD: Non-Deterministic Rendering
   - Risk: Template renders differently on each run
   - Impact: Byte hash never stable, golden fixture fails
   - Mitigation: Jinja2 settings (trim_blocks, lstrip_blocks) + sorted dicts
   - Owner: Week 1 Foundation Team
   - Status: MITIGATED (Week 1)
   
   (Repeat for all 5 P0 risks)

5. CONFIDENCE METER (Bottom)
   - Large gauge showing: "95% Confidence in Mitigation Plans"
   - Supporting text: "All P0 risks addressable in Weeks 1-2"
   - Green zone: Week 1 foundation work eliminates 80% of risk

Visual Design Notes:
- Red circles for P0 (critical), Yellow for P1 (moderate)
- Green checkmarks for mitigated risks
- Timeline shows risk reduction over 6 weeks
- Cards are scannable (minimal text, bold headlines)
- Confidence meter as visual reassurance

Use Case: Risk review meetings, stakeholder confidence-building, project approvals
```

**Expected Output**: Risk assessment infographic (PNG or PDF)

---

## Detailed Content Specifications for Studio Outputs

The following sections provide detailed guidance on what content to include in each Studio output. Use these as reference when generating the video overview slides, mind map nodes, and infographic elements.

---

## Visualization Requests

### 1. Architecture Flow Diagrams

**Request 1A: Upstream 6-Stage Validation Pipeline**
- Create a horizontal flow diagram showing the 6 stages
- Color code: Green for structure validation (Stages 1-2), Blue for processing (Stage 3), Purple for validation (Stage 4), Orange for generation (Stages 5-6)
- Show decision points (pass/fail) at each stage
- Include HITL routing destinations on failure paths
- Label each stage with primary function and key checks

**Request 1B: Downstream 9-Stage Extended Pipeline**
- Create a comparison diagram showing upstream 6 stages + new 3 stages
- Highlight new stages in red or with dashed borders
- Show where new stages integrate into existing flow
- Mark P0 (critical) vs P1 (quality) stages
- Include Stage 0 (Linear extraction) at the beginning
- Include Stage 2.5 (ORCA validation), Stage 3.5 (Template injection), Stage 4.5 (Byte hash), Stage 5.5 (Structural hash), Stage 7 (BDD projection), Stage 8 (Forbidden vocabulary)

**Request 1C: Docling Extraction Pattern Visualization**
- Create a flowchart showing:
  - Markdown file → DocumentConverter → DoclingDocument object
  - DoclingDocument → doc.tables → table.data.grid
  - table.data.grid[0] = headers, grid[1:] = data rows
  - Data rows → Exploded attribute objects
- Annotate with "BREAKTHROUGH PATTERN" label
- Show contrast with broken regex approach (crossed out)

**Request 1D: HITL Queue Routing Decision Tree**
- Create a decision tree showing routing logic
- Start node: "Validation Results"
- Decision nodes: "Naming OK?", "Structure OK?", "Consistency OK?", "Byte Hash OK?", "Structural Hash OK?"
- End nodes: hitl_rejected, hitl_failed, hitl_workshop, hash_verification, promotion_candidates
- Color code end nodes by severity (red=rejected, orange=failed, yellow=workshop, green=promotion)

---

### 2. Gap Analysis Heatmaps

**Request 2A: Component Readiness Heatmap**
- Create a matrix with rows = components, columns = readiness status
- Components (rows):
  - Validation Pipeline (Stages 1-6)
  - Docling Extraction
  - Template System
  - Hash Validation
  - ORCA Validators
  - Evidence Attribution
  - BDD Generation
  - Prompt Generation
  - HITL Queue Management
  - Deterministic Injection
- Readiness (columns):
  - Production Ready (Green) - ✅ Copy as-is
  - Needs Adaptation (Yellow) - ⚠️ Customize
  - Must Build (Red) - ❌ Build from scratch
- Add percentage in each cell showing completion (e.g., "80% ready")
- Summary row showing overall: 80% production-ready, 10% adaptation, 10% new build

**Request 2B: Priority Heatmap - Impact vs Effort**
- Create a 2D heatmap with axes:
  - X-axis: Implementation Effort (Low → High)
  - Y-axis: Business Impact (Low → High)
- Plot each gap item as a bubble:
  - Size = number of objects affected (1-8)
  - Color = Priority (Red=P0, Yellow=P1)
- Label bubbles with component name
- Quadrants:
  - High Impact, Low Effort = "Quick Wins" (top-left)
  - High Impact, High Effort = "Major Projects" (top-right)
  - Low Impact, Low Effort = "Fill-ins" (bottom-left)
  - Low Impact, High Effort = "Questionable" (bottom-right)

---

### 3. Timeline & Roadmap Visuals

**Request 3A: 6-Week Implementation Timeline**
- Create a Gantt-style timeline showing:
  - Week 1: Foundation (Template System, Hash System, Linear Integration)
  - Week 2: Validation Extensions (ORCA validators, Hash validators, Routing logic)
  - Week 3: Core Trio (User v3, Skill v3, Requirement v3)
  - Week 4: Credential Group (Credential v3, Qualification v3, Standard v3)
  - Week 5: Fit + Integration (Fit v3, Cross-object validation)
  - Week 6: Quality Gates (Forbidden vocab, BDD projection, Regression suite)
- Color bars by priority: Red=P0 (launch blockers), Yellow=P1 (quality)
- Show dependencies with arrows
- Mark milestones with stars: "Golden Fixture", "Core Trio Complete", "All-8-Objects", "Launch Ready"

**Request 3B: All-8-Objects Promotion Schedule**
- Create a stacked bar chart showing 4 phases:
  - Phase 1: Outcome (Week 1) - 1 object
  - Phase 2: Core Trio (Week 2-3) - 3 objects
  - Phase 3: Credential Group (Week 4) - 3 objects
  - Phase 4: Fit (Week 5) - 1 object
- X-axis: Time (weeks)
- Y-axis: Cumulative objects promoted (0-8)
- Color each phase differently
- Annotate with success criteria checkboxes per phase

---

### 4. Risk Matrix & Mitigation

**Request 4A: Risk Impact-Probability Matrix**
- Create a 2x2 matrix with quadrants:
  - X-axis: Probability (Low → High)
  - Y-axis: Impact (Low → High)
- Plot risks as circles:
  - Size = mitigation effort required
  - Color = Priority (Red=P0, Yellow=P1)
- Label each risk with short name
- Risks to plot:
  - P0: Non-deterministic rendering, Stale cached schema, Hand-edited projections, Tuning bleed, Validator tuned to corpus
  - P1: BDD projection drift, Evidence coverage gaps, Cross-object reference breakage, Template divergence
- Add mitigation notes in callout boxes

**Request 4B: Risk Mitigation Timeline**
- Create a timeline showing when each mitigation is implemented:
  - Week 1: Non-deterministic rendering (Jinja2 + sorted dicts)
  - Week 1: Stale cached schema (version alignment check)
  - Week 2: Tuning bleed (forbidden vocabulary validator)
  - Week 6: BDD projection drift (projection validator)
  - Week 6: Hand-edited projections (watermark system + pre-commit hooks)
- Show risks before mitigation (red) and after mitigation (green)

---

### 5. Success Metrics Dashboard

**Request 5A: P0 Must-Pass Criteria Tracker**
- Create a dashboard with 6 key metrics:
  1. Outcome v3 byte hash reproducibility (Target: 3/3 runs identical)
  2. All 8 objects have golden hashes (Target: 8/8 registered)
  3. Deterministic generation (Target: 100% stable)
  4. ORCA meta-metadata coverage (Target: 100% of attributes)
  5. Evidence attribution (Target: 100% of core attributes)
  6. 6-stage validation pass rate (Target: 100% for golden fixtures)
- For each metric:
  - Show target value
  - Show current status (Pending / In Progress / Complete)
  - Show progress bar (0-100%)
  - Color code: Red=Not Started, Yellow=In Progress, Green=Complete

**Request 5B: Quality Indicators (P1) Dashboard**
- Create a dashboard with 5 quality metrics:
  1. BDD projection validity (Target: 100% parse cleanly)
  2. Forbidden vocabulary violations (Target: 0 in canonical sections)
  3. Structural hash stability (Target: No drift)
  4. Cross-object reference integrity (Target: 100% resolve)
  5. Regression test pass rate (Target: 100%)
- For each metric:
  - Show current value vs target
  - Show trend arrow (improving / stable / degrading)
  - Show last updated timestamp

---

### 6. Data Tables & Comparisons

**Request 6A: Upstream vs Downstream Component Comparison**
- Create a table with columns:
  - Component Name
  - Upstream Status (✅/⚠️/❌)
  - Downstream Status (✅/⚠️/❌)
  - Gap Category (No Gap / Needs Adaptation / Must Build)
  - Priority (P0 / P1)
  - Implementation Effort (Low / Medium / High)
- Rows for each component:
  - Stage 1-6 Validation Pipeline
  - Docling Parser
  - Template System
  - Hash Validation
  - ORCA Validators
  - Evidence Attribution
  - BDD Generation
  - Prompt Generation
  - HITL Queues
  - Deterministic Injection
  - Golden Hash Registry
- Summary row showing 80% ready / 10% adapt / 10% build

**Request 6B: Validation Rules Matrix**
- Create a matrix showing what validation rules exist vs needed:
- Columns: Upstream (✅/❌) | Downstream (✅/❌) | Priority (P0/P1)
- Rows:
  - Structure Validation
  - Consistency Validation
  - ORCA Meta-Metadata
  - Forbidden Vocabulary
  - Byte Hash
  - Structural Hash
  - BDD Projection
  - Schema Validation
  - Evidence Attribution
  - Naming Convention
- Color cells: Green=Exists, Yellow=Needs Extension, Red=Must Build

---

### 7. Architecture Patterns Visualization

**Request 7A: Markdown-First Governance Flow**
- Create a flowchart showing the philosophy:
  - Start: "Markdown .md (Canonical Source)"
  - ↓ "DoclingDocument Parser"
  - ↓ "Structured Extraction (table.data.grid)"
  - ↓ "Exploded Attributes"
  - → Fork 1: "JSON Schema Generation"
  - → Fork 2: "BDD Feature Generation"
  - → Fork 3: "Extraction Prompt Generation"
- Annotate: "Natural Language as Infrastructure-as-Code"
- Show that generated artifacts are NEVER hand-edited

**Request 7B: Evidence Attribution Pattern**
- Create a diagram showing evidence flow:
  - Source: "Linear Issue CAREERS-171"
  - ↓ "Extract Evidence Objects"
  - ↓ "Evidence IDs: EV-CAREERS-171-001, EV-CAREERS-171-002, etc."
  - ↓ "Link to Attributes"
  - → "outcome_statement (EV-001)"
  - → "user_id (EV-002)"
  - → "skill_id (EV-003)"
- Show ORCA meta-metadata attached to each evidence link
- Annotate with "No Self-Confidence Scores"

---

### 8. Golden Fixture Workflow

**Request 8A: CAREERS-171 Golden Fixture Establishment**
- Create a step-by-step flowchart:
  1. Extract from Linear → Injection Contract JSON
  2. Validate Injection Contract
  3. Inject into Template → Generated .md
  4. Calculate Byte Hash → sha256:abc123...
  5. Register Golden Hash
  6. Test Reproducibility (3 runs)
  7. ✅ All hashes match → Golden Fixture Established
- Show decision point at step 7: If hashes don't match, loop back to step 3
- Annotate critical success criterion: "Byte-identical across regenerations"

**Request 8B: Golden Fixture Regression Test Flow**
- Create a flowchart showing regression test:
  - Start: "Load Injection Contract"
  - ↓ "Regenerate Object"
  - ↓ "Calculate Hash"
  - ↓ "Compare to Golden Hash"
  - → Branch: Match? → ✅ "Pass - No Drift"
  - → Branch: Mismatch? → ❌ "Fail - Investigate Drift"
  - If fail: → "Structural Hash Check" → "Classify Failure" → "Route to HITL Queue"

---

### 9. Synthesis & Insights

**Request 9A: Executive Summary Visual**
- Create a single-page infographic showing:
  - Top section: "80% Infrastructure Ready" (large number)
  - Middle section: 3 key gaps (Template System, Hash Validation, ORCA Validators)
  - Bottom section: 6-week timeline bar
  - Sidebar: Risk count (5 P0, 4 P1) with mitigation status
- Use colors: Green for ready, Red for gaps, Yellow for in-progress

**Request 9B: Stakeholder Decision Dashboard**
- Create a dashboard answering key questions:
  - "Can we reuse upstream patterns?" → 80% Yes (show breakdown)
  - "What must we build?" → 10% Critical (list P0 items)
  - "When can we launch?" → Week 6 (show milestones)
  - "What are the risks?" → 5 Critical, 4 Moderate (show top 3)
  - "How do we measure success?" → 6 P0 metrics (show current status)

---

## NotebookLM Studio Guidelines

### Studio Workspace Setup
1. **Upload both source documents** to a new NotebookLM notebook:
   - `codebase_analysis.md` (upstream patterns)
   - `kit_v3_gap_analysis.md` (gap analysis)

2. **Open Studio panel** (right side of interface)

3. **Generate outputs in this order**:
   - Start with **Cinematic Video Overview** (executive briefing)
   - Create **Mind Map** (architecture visualization)
   - Generate **Infographic** (80/20 readiness breakdown)
   - Export **PowerPoint deck** (editable presentation)
   - Optional: **Audio Overview** (technical deep dive)

### Studio Output Preferences

**For Video Overviews**:
- Target audience: "Corporate executives and senior architects"
- Complexity level: "Professional/adult audience"
- Duration: 5-7 minutes (concise but comprehensive)
- Tone: Technical but accessible, emphasize business value

**For Mind Maps**:
- Layout: Radial or hierarchical (whichever shows relationships best)
- Node colors: Use color coding standards below
- Export: PNG image at high resolution for documentation
- Interactivity: Enable clickable nodes for deeper exploration

**For Infographics**:
- Theme: "Technical architecture gap analysis"
- Style: Clean, professional, minimal text
- Emphasis: Visual hierarchy (80% dominant, 10% secondary)
- Export: High-resolution PNG or PDF

**For PowerPoint Export**:
- Slide design: Professional theme, minimal animations
- Content density: 1 key concept per slide (avoid text walls)
- Charts/diagrams: Editable shapes (not flattened images)
- Speaker notes: Include detailed talking points

### Color Coding Standards (Apply Across All Outputs)
- 🟢 **Green** = Production-ready, passed, completed, reusable from upstream
- 🟡 **Yellow** = Needs adaptation, in progress, moderate risk, ORCA extensions
- 🔴 **Red** = Must build from scratch, failed, critical risk, P0 gaps
- 🔵 **Blue** = Processing stages, target objects, downstream components
- 🟣 **Purple** = Validation stages, quality gates, testing phases
- 🟠 **Orange** = Generation stages, risk areas, mitigation zones

### Text & Label Guidelines
- **Quantitative first**: Show numbers (80%, 6 weeks, 8 objects, 5 P0 gaps)
- **Concise labels**: Max 5-7 words per heading
- **Action-oriented**: Use verbs (Build, Validate, Extract, Generate)
- **Consistent terminology**: Use exact terms from source documents

---

## Specific Data Points to Extract

### From `codebase_analysis.md`:
- 6-stage validation pipeline details
- DoclingDocument breakthrough pattern
- HITL queue folder structure
- Canonical object template structure
- Evidence object pattern
- BDD feature template format

### From `kit_v3_gap_analysis.md`:
- Stage comparison table (Stages 1-6 vs 0-8)
- Component readiness percentages (80/10/10)
- Risk matrix entries (9 risks total)
- 6-week implementation roadmap
- All-8-objects promotion phases
- Success metrics (6 P0, 5 P1)
- Golden fixture workflow steps

---

## Expected Studio Deliverables

### Primary Studio Outputs (Generate These)
1. 🎬 **Cinematic Video Overview** (.mp4)
   - 5-7 minute executive briefing
   - AI-narrated slideshow covering key findings
   - Professional presentation quality

2. 🧠 **Interactive Mind Map** (exportable as .png)
   - Kit v3 Component Architecture
   - Color-coded nodes (Green=ready, Red=gaps, Blue=targets)
   - Expandable branches for deeper exploration

3. 📊 **Infographic** (.png or .pdf)
   - 80/20 Readiness Breakdown
   - Visual hierarchy emphasizing production-ready percentage
   - Timeline bar and risk indicators

4. 📑 **PowerPoint Deck** (.pptx)
   - 15-20 editable slides
   - Complete architecture review presentation
   - Ready for stakeholder customization

5. 🎙️ **Audio Overview** (.mp3) - *Optional*
   - 10-15 minute podcast-style technical deep dive
   - Two-host conversational format
   - Interactive Q&A capability

### Secondary Outputs (Via Chat Interface)
6. 📋 **Comparison Tables** (markdown/text)
   - Validation stages comparison (6 vs 9)
   - Component readiness matrix
   - Risk assessment summary

7. 🧪 **Study Materials** (text-based)
   - Quiz questions for developers
   - Flashcards for ORCA concepts
   - Study guide for 6-week plan

8. 📝 **Extracted Data** (structured text)
   - Timeline milestones list
   - P0 gaps enumeration
   - Success metrics checklist

**Total**: 5 primary multimedia outputs + 3 secondary text-based materials for comprehensive stakeholder presentation

---

## Usage Instructions for NotebookLM Studio

### Step 1: Create Notebook & Upload Sources
```
1. Go to: https://notebooklm.google.com
2. Click "New Notebook"
3. Click "Add Sources"
4. Upload both files:
   - codebase_analysis.md
   - kit_v3_gap_analysis.md
5. Wait for processing to complete
```

### Step 2: Generate Priority Studio Outputs
```
1. Click "Studio" panel (right side)
2. Start with "Video Overview":
   - Click "Create Video Overview"
   - Select "Cinematic Video Overview"
   - Target audience: "Corporate executives"
   - Wait ~2-5 minutes for generation
   - Preview and export as .mp4

3. Create "Mind Map":
   - Click "Create Mind Map" 
   - Root concept: "Kit v3 Object Promotion"
   - Let NotebookLM auto-generate from sources
   - Expand key branches (Upstream, Gaps, Timeline, Risks)
   - Export as PNG image

4. Generate "Infographic":
   - Click "Create Infographic"
   - Theme: "Gap Analysis"
   - Focus on: "80% ready, 20% gaps"
   - Export as PNG or PDF

5. Export "PowerPoint Deck":
   - Click "Export as PowerPoint"
   - Select slide range (15-20 slides recommended)
   - Download .pptx file
   - Open in PowerPoint/Keynote for final polish
```

### Step 3: Optional Audio Overview
```
1. In Studio panel, click "Create Audio Overview"
2. Select podcast-style (two hosts)
3. Target audience: "Senior developers and architects"
4. Wait ~5-10 minutes for generation
5. Listen and use interactive features:
   - Pause to ask: "Explain byte hash validation in detail"
   - Request: "Focus more on the golden fixture workflow"
   - Ask: "What are the biggest risks in Week 1?"
```

### Step 4: Interactive Deep Dive (Chat Mode)
```
After Studio outputs are generated, use Chat to refine:
- "Create a detailed comparison table of Stages 1-6 vs 0-8"
- "Generate quiz questions for developers on Docling extraction"
- "Build flashcards for ORCA meta-metadata concepts"
- "Create a study guide for the 6-week implementation plan"
```

### Step 5: Review & Share
```
1. Review all Studio outputs for accuracy
2. Export files:
   - Video: .mp4 (for Slack, email, presentations)
   - Mind Map: .png (for documentation, wikis)
   - Infographic: .png/.pdf (for executive decks)
   - PowerPoint: .pptx (for customization and presenting)
3. Share with stakeholders:
   - ARB architects: PowerPoint + Mind Map
   - Executives: Video Overview + Infographic
   - Developers: Audio Overview + Chat study guide
```

---

## Additional Context for NotebookLM

**Project Context**:
- This is an object model promotion from upstream (DUX Core) to downstream (Kit v3)
- The golden fixture is CAREERS-171 (Outcome v3 object)
- Target is 8 objects: Outcome, User, Skill, Requirement, Credential, Qualification, Standard, Fit
- Timeline is 6 weeks with P0 (launch blockers) and P1 (quality gates)
- Key innovation: Byte-identical hash validation for canonical governance

**Technical Philosophy**:
- Markdown-first: Natural language as infrastructure-as-code
- Evidence-based: No self-confidence scores, mandatory attribution
- Deterministic: Same input always produces same byte hash
- Semantic tuning separation: Extraction lens never alters canonical schema

**Critical Success Factors**:
- 80% of infrastructure is reusable from upstream
- 10% needs adaptation (ORCA extensions)
- 10% must be built new (hash validation, deterministic injection)
- Golden fixture must be reproducible byte-for-byte
- All 8 objects must pass validation gates

---

---

## Stakeholder-Specific Studio Workflow

### For Executives & Decision-Makers
**Primary Outputs**:
1. Watch: 🎬 Cinematic Video Overview (5-7 min)
2. Review: 📊 80/20 Readiness Infographic
3. Skim: 📑 PowerPoint Deck (executive summary slides 1-5)

**Key Questions to Ask in Chat**:
- "What's the total cost and timeline to close the 20% gap?"
- "What are the top 3 risks that could delay launch?"
- "Why is CAREERS-171 called the 'golden fixture'?"
- "What happens if we skip the P0 validation gates?"

---

### For Architects & Tech Leads
**Primary Outputs**:
1. Study: 🧠 Component Architecture Mind Map
2. Reference: 📑 Full PowerPoint Deck (all slides)
3. Listen: 🎙️ Audio Overview while reviewing code

**Key Questions to Ask in Chat**:
- "Explain the DoclingDocument table.data.grid breakthrough in detail"
- "Create a detailed comparison of upstream vs downstream validation stages"
- "What's the difference between byte hash and structural hash validation?"
- "Generate a quiz on deterministic template injection requirements"

---

### For Developers Implementing Kit v3
**Primary Outputs**:
1. Study: 🎙️ Audio Overview (technical deep dive)
2. Reference: 🧠 Mind Map (implementation roadmap branch)
3. Checklist: 📋 Chat-generated task list from gap analysis

**Key Questions to Ask in Chat**:
- "Create a checklist for Week 1 Foundation sprint tasks"
- "List all P0 components that must be built from scratch"
- "Generate flashcards for ORCA meta-metadata validation concepts"
- "What files do I copy as-is vs build new for Kit v3?"

---

### For Project Managers
**Primary Outputs**:
1. Present: 📑 PowerPoint Deck (timeline & risk slides)
2. Track: 📊 Infographic (for status updates)
3. Baseline: 📋 Chat-generated milestone checklist

**Key Questions to Ask in Chat**:
- "Create a 6-week sprint plan with clear deliverables"
- "Generate a risk mitigation tracking table"
- "List all success metrics with current status (Pending/In Progress/Complete)"
- "What are the dependencies between the 8 object promotions?"

---

## Tips for Interactive Studio Experience

### Interrupting Audio Overviews
While listening to the podcast-style audio overview, you can pause and ask:
- "Wait, explain that Docling pattern again more slowly"
- "Give me a concrete example of tuning bleed"
- "What's a real-world scenario where byte hash fails?"
- "Focus more on the golden fixture workflow"

### Refining Mind Maps
After initial mind map generation:
- Click nodes to expand: "Show me more detail on Template System gaps"
- Collapse branches: Hide sections you understand well
- Export subsets: Save just the "6-Week Timeline" branch as separate PNG
- Share with annotations: Add notes to specific nodes before exporting

### Customizing Video Overviews
Request variations:
- "Create a shorter 3-minute version for board meeting"
- "Make a developer-focused version emphasizing code patterns"
- "Generate a 'Week 1 Sprint Kickoff' video overview"

---

**Prompt Version**: 2.0 (Revised for NotebookLM Studio)  
**Last Updated**: 2026-05-27  
**Optimized For**: Google NotebookLM Studio features (Video, Audio, Mind Maps, Infographics, PowerPoint)  
**Source Documents**: codebase_analysis.md (47KB), kit_v3_gap_analysis.md (62KB)  
**Primary Audience**: Architecture Review Board (ARB), Kit v3 implementation teams  
**Studio Outputs**: 5 multimedia artifacts + 3 text-based materials
