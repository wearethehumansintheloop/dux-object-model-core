# NotebookLM Quick Commands

**How to use**: Upload this file to NotebookLM, then reference commands in chat  
**Example**: "Use `/video-exec` from this file to create executive video"  
**Full prompt library**: See `notebooklm_visualization_prompt.md` for detailed versions

---

## 🧬 How to Write Effective Commands: Canon vs Tuning

**Core Principle**: Studio outputs are **structurally canonical** (consistent design system) but **semantically tuned** (audience/output-specific).

### Studio Interface Quick Reference

Each Studio output type has different tuning knobs:

| Output Type | Built-in Tuning Knobs | Custom Prompt |
|-------------|----------------------|---------------|
| **Video** | Format (Explainer/Brief), Visual Style (9 options), Language | What to feature, audience, tone |
| **Audio** | Format (Deep Dive/Brief/Critique/Debate), Length, Language | What hosts should focus on |
| **Slides** | Format (Detailed/Presenter), Length, Language | Slide structure, audience |
| **Mind Map** | None | Topic and branch structure |
| **Infographic** | Orientation, Visual Style (6+ options), Detail Level, Language | Theme, visual structure |
| **Data Table** | Language only | Table structure, columns |
| **Report** | Format (10+ templates like Briefing Doc, Study Guide, Blog Post) | Content focus |

### What Stays Fixed (Canon Axis)
These elements are defined in `notebooklm_persona_config.md` and `tokens.css` - **don't redefine them in commands**:
- ✅ **Design System**: Purple/Blue/Green/Amber palette
- ✅ **Typography**: XL → LG → MD → SM hierarchy
- ✅ **Spacing**: 2XL margins, LG gaps, MD padding
- ✅ **Evidence Rules**: All claims cite sources

### What You Should Tune (Tuning Axis)

**1. Built-in Tuning Knobs** (click to set in Studio):
- 📊 **Format**: Explainer vs Brief, Detailed Deck vs Presenter Slides, Deep Dive vs Critique
- 🎨 **Visual Style**: Auto-select, Classic, Whiteboard, Kawaii, Anime, Watercolor, Clay, Editorial
- 📏 **Length**: Short, Default, Long
- 🖼️ **Orientation**: Landscape, Portrait, Square
- 📝 **Level of Detail**: Concise, Standard, Detailed

**2. Custom Prompt Field** (what you type):
- 🎯 **Audience**: C-suite (ROI focus) vs Architects (technical depth) vs Developers (implementation)
- 🎯 **Tone**: Business-savvy vs Engineering-precise vs Conversational
- 🎯 **Emphasis**: What numbers/facts to highlight (80% ready vs 6 weeks vs 5 risks)
- 🎯 **Output Structure**: Slide order, narrative flow, what to feature

### Examples of Good Tuning

**For Executives** (emphasize business value):
```
"Emphasize ROI and cost savings. Lead with '80% infrastructure reuse = $X avoided cost.'
Focus on timeline (6 weeks), risk mitigation, and go/no-go decision points.
Minimize technical jargon. Use business metrics."
```

**For Architects** (emphasize technical depth):
```
"Focus on implementation patterns: DoclingDocument parsing, hash validation gates, 
template injection architecture. Include code structure examples and architecture diagrams.
Emphasize what to copy vs adapt vs build from scratch."
```

**For Developers** (emphasize actionable tasks):
```
"Break down into sprint-ready tasks. Show concrete file paths, function names, 
and acceptance criteria. Use CAREERS-171 golden fixture as reference implementation.
Include what passes/fails validation."
```

### ❌ Avoid Tuning Bleed

**DON'T redefine the design system**:
- ❌ "For executives, use red for completed items instead of green"
- ❌ "Use a different font family for technical audiences"
- ❌ "Make the color palette warmer/cooler for this output"

**DO specify semantic emphasis**:
- ✅ "For executives, emphasize cost savings prominently"
- ✅ "For developers, lead with actionable tasks"
- ✅ "For architects, focus on patterns to copy"

---

## 🎬 Video Commands (Copy & Paste)

### `/video-exec` - Executive Briefing (5-7 min)

**Studio Interface Settings**:
- **Format**: ✅ Explainer (comprehensive overview)
- **Visual Style**: 🎨 Classic (professional, business-appropriate)
- **Language**: English

**Custom Prompt Field** (paste this):
```
Create executive briefing video for C-suite and VPs focused on business ROI and risk mitigation.

Target Audience: C-suite, VPs, Board of Directors
Purpose: Investment approval and timeline commitment

Key Slides Structure:
1. Opening: "80% Infrastructure Already Production-Ready" (emphasize $X cost savings avoided)
2. What We're Reusing: 6-stage validation, Docling parser, Evidence patterns, BDD generation
3. The 20% Gap: 3 critical components - Template System, Hash Validation, ORCA Validators
4. Timeline: 6 weeks from foundation to launch (show weekly milestones)
5. Risk Management: 5 P0 risks identified with mitigation plans in place
6. Success Metrics: 6 launch criteria (Outcome v3 reproducibility, all-8-objects hashes)
7. Call to Action: Week 1 Foundation Sprint starts Monday

Emphasis: Lead with numbers (80%, 6 weeks, 8 objects, 5 risks). Focus on "why this matters" not technical details. Business-confident tone.

Apply design system from notebooklm_persona_config.md (purple/blue/green/amber palette).
```

---

### `/video-tech` - Technical Deep Dive (7-10 min)

```
Using the uploaded sources (codebase_analysis.md and kit_v3_gap_analysis.md), create a Cinematic Video Overview for architects.

Title: "Kit v3 Architecture - Upstream Patterns and Downstream Implementation"
Target: Tech Leads, Principal Engineers
Focus: Implementation details, patterns, code structure

Key Slides:
1. Architecture overview (upstream DUX → downstream Kit v3)
2. Validation Pipeline: 6 stages → 9 stages evolution
3. DoclingDocument structured parsing breakthrough
4. Template system architecture (Jinja2 + deep_sort_dict)
5. Hash validation gates (byte-identical + structural)
6. ORCA meta-metadata pattern
7. Evidence attribution system
8. BDD generation pipeline
9. What to copy vs adapt vs avoid

Style: Code snippets, architecture diagrams, technical depth
Tone: Engineering-focused, implementation-ready
```

---

### `/video-week1` - Sprint Kickoff (3-5 min)

```
Using the uploaded sources (codebase_analysis.md and kit_v3_gap_analysis.md), create a Video Overview for developers starting Week 1.

Title: "Week 1 Sprint - Foundation Components"
Target: Development team
Focus: Actionable tasks, clear deliverables

Key Slides:
1. Week 1 Goal: Template System + Hash Validation working end-to-end
2. Task Breakdown: 5 core tasks with owners
3. CAREERS-171 as reference (Outcome v3 golden fixture)
4. Acceptance Criteria: Byte-identical hash passes
5. What You'll Build Today (concrete file paths, functions)

Style: Task lists, code examples, file structure
Tone: Actionable, developer-friendly, sprint-ready
```

---

## 🎙️ Audio Commands (Copy & Paste)

### `/audio-arch` - Architecture Podcast (15 min)

**Studio Interface Settings**:
- **Format**: ✅ Deep Dive (lively conversation between two hosts)
- **Length**: 📏 Default
- **Language**: English

**Custom Prompt Field** (paste this):
```
Create architecture discussion podcast for Tech Directors and Principal Engineers.

Format: Two senior engineers discussing Kit v3 architecture patterns like a design review meeting.

Discussion Topics:
1. Why 80% reuse is significant (upstream DUX patterns are mature)
2. The DoclingDocument breakthrough (table.data.grid vs regex parsing)
3. Markdown-first philosophy (natural language as code)
4. Deterministic generation challenges (Jinja2, deep_sort_dict)
5. Hash validation as quality gate (byte-identical vs structural)
6. ORCA meta-metadata pattern (bucket, core_vs_supporting)
7. Evidence attribution requirements
8. Risk mitigation strategies (5 P0 risks identified)
9. Golden fixture workflow (CAREERS-171 → all 8 objects)

Tone: Conversational but precise. Like two senior engineers discussing architecture trade-offs over coffee. Not a presentation - a peer discussion with technical depth.

Apply persona from notebooklm_persona_config.md.
```

---

### `/audio-dev` - Developer Guide (12 min)

```
Using the uploaded sources (codebase_analysis.md and kit_v3_gap_analysis.md), create an Audio Overview for developers implementing Kit v3.

Title: "Kit v3 Implementation Guide - Developer Walkthrough"
Target: Mid-senior developers building the system
Format: Tutorial-style podcast

Guide Topics:
1. What to copy directly from upstream (validation scripts, docling parser)
2. What to adapt (template structure, hash gates)
3. What to build from scratch (ORCA validators)
4. How to use CAREERS-171 as reference
5. Template injector architecture (injection contract → Jinja2 → .md)
6. Hash validation workflow (generate → hash → compare → route)
7. HITL queue management (promotion flow)
8. Testing strategy (golden fixture as source of truth)

Tone: Practical, implementation-focused, like a senior dev pairing session
```

---

## 📊 PowerPoint Commands (Copy & Paste)

### `/slides-arb` - Architecture Review Board (20 slides)

**Studio Interface Settings**:
- **Format**: ✅ Detailed Deck (comprehensive with full text)
- **Length**: 📏 Default
- **Language**: English

**Custom Prompt Field** (paste this):
```
Create PowerPoint deck for Architecture Review Board (ARB) - technical leadership review.

Target Audience: ARB Architects, Technical Leadership
Purpose: Formal architecture review and approval
Slide Count: 20 slides with technical depth

Deck Structure:
1. Title: Kit v3 Object Model Promotion - ARB Review
2. Executive Summary (80% reuse, 20% build, 6 weeks)
3. Upstream Patterns Overview (DUX object-model-core)
4. Downstream Needs (Kit v3 requirements)
5-8. Gap Analysis by Component (Validation, Docling, Template, Hash)
9. Detailed Architecture (validation pipeline flowchart)
10. DoclingDocument structured parsing pattern
11. Template system design (injection contract + Jinja2)
12. Hash validation gates (byte-identical + structural)
13. ORCA meta-metadata schema
14. Evidence attribution requirements
15. Golden fixture workflow (CAREERS-171 → all 8 objects)
16. Risk assessment (5 P0 risks + mitigation plans)
17. Phased roadmap (6 weeks, 3 phases)
18. Success criteria (6 launch gates)
19. Open questions for ARB review
20. Next steps and decision points

Style: Technical diagrams, code snippets, architecture flowcharts. Include presenter notes for each slide.

Apply design system from notebooklm_persona_config.md and tokens.css (purple/blue/green/amber palette).
```

---

### `/slides-exec` - Executive Summary (8 slides)

```
Using the uploaded sources (codebase_analysis.md and kit_v3_gap_analysis.md), create a PowerPoint deck for executive leadership.

Title: "Kit v3 Investment Case - Executive Briefing"
Target: C-suite, Board of Directors
Slides: 8 slides, business-focused

Deck Structure:
1. Title: Kit v3 Object Model Promotion
2. The Ask: 6 weeks, 3 FTE engineers, $X investment
3. The Value: 80% infrastructure reuse = $Y R&D cost avoided
4. What We're Building: 8 object definitions with full lifecycle
5. Timeline: 6 weeks to production-ready system
6. Risk Management: 5 identified risks, all mitigated
7. Success Metrics: 6 measurable launch criteria
8. Go/No-Go Decision: Recommend approval

Style: Large numbers, business charts, ROI focus
Export: Board-ready .pptx with presenter notes
```

---

### `/slides-pm` - Project Management (15 slides)

```
Using the uploaded sources (codebase_analysis.md and kit_v3_gap_analysis.md), create a PowerPoint deck for project tracking.

Title: "Kit v3 Sprint Planning - PM Dashboard"
Target: Project Managers, Scrum Masters
Slides: 15 slides with task breakdowns

Deck Structure:
1. Title: Kit v3 Project Plan
2. Overall Timeline (6 weeks, 3 phases)
3. Phase 1: Foundation (Weeks 1-2) - Task breakdown
4. Phase 2: Scale (Weeks 3-4) - Task breakdown
5. Phase 3: Launch (Weeks 5-6) - Task breakdown
6. Critical Path: Template → Hash → ORCA → All 8
7. Dependencies: What blocks what
8. Resource Allocation (FTE per week)
9. Risk Register (5 P0 risks + owners)
10. Milestone Checklist (Golden fixture → Outcome → User/Skill → etc)
11. Quality Gates (6 launch criteria)
12. Status Dashboard Template (for weekly updates)
13. Blockers & Open Issues (tracking sheet)
14. Success Metrics (how to measure progress)
15. Sprint Planning Template (for daily standups)

Style: Gantt charts, task lists, status indicators
Export: Editable .pptx for weekly updates
```

---

## 🧠 Mind Map Commands (Copy & Paste)

### `/mindmap-arch` - Component Architecture

**Studio Interface Settings**:
- Just the topic field (no other settings for mind maps)

**Topic Field** (paste this):
```
Kit v3 Architecture - Component Relationships

Root Node: Kit v3 Object Model System

Create branches showing:

1. Upstream Components (DUX object-model-core) - use GREEN for production-ready
   - Validation Pipeline (6 stages)
   - Docling Parser (structured extraction with table.data.grid)
   - Evidence Patterns (attribution system)
   - BDD Generation (feature files)

2. Downstream Needs (Kit v3 requirements) - use BLUE for in-progress
   - Template System (injection + Jinja2)
   - Hash Validation (byte-identical + structural)
   - ORCA Validators (meta-metadata)
   - 9-Stage Pipeline (extended validation)

3. Gap Components (What to Build) - use PURPLE for validation needed
   - Template Injector
   - Hash Comparator
   - ORCA Attribute Validators
   - Evidence Coverage Checker

4. Integration Points (How they connect) - use AMBER for attention
   - CAREERS-171 (golden fixture)
   - All 8 Objects (promotion sequence: Outcome → User → Skill → Requirement → Credential → Qualification → Standard → Fit)
   - HITL Queues (validation routing)

Apply color coding from notebooklm_persona_config.md: Green=ready, Blue=in-progress, Purple=validation, Amber=attention.

Export as PNG for technical documentation.
```

---

### `/mindmap-timeline` - 6-Week Implementation

```
Using the uploaded sources (codebase_analysis.md and kit_v3_gap_analysis.md), create a Mind Map showing the 6-week implementation timeline.

Title: "Kit v3 Timeline - 6 Weeks to Launch"
Root Node: Kit v3 Implementation Plan

Branches by Phase:
- Phase 1: Foundation (Weeks 1-2)
  - Week 1: Template System + Hash Validation
    - Build Jinja2 template injector
    - Build hash comparator
    - Test with CAREERS-171
  - Week 2: ORCA Validators
    - Build attribute validators
    - Build evidence coverage checker
    - Golden fixture passes
- Phase 2: Scale (Weeks 3-4)
  - Week 3: First 4 Objects
    - Outcome v3 (golden fixture)
    - User v3
    - Skill v3
    - Requirement v3
  - Week 4: Remaining 4 Objects
    - Credential v3
    - Qualification v3
    - Standard v3
    - Fit v3
- Phase 3: Launch (Weeks 5-6)
  - Week 5: Integration Testing
  - Week 6: Production Deployment

Dependencies:
- Template must complete before any objects
- Hash must complete before validation
- Golden fixture must pass before scaling

Color Coding:
- Blue nodes: Current week
- Green nodes: Completed
- Orange nodes: At risk
- Red nodes: Blocked

Export: PNG image for sprint planning
```

---

## 📈 Infographic Commands (Copy & Paste)

### `/infographic-80-20` - Readiness Breakdown

**Studio Interface Settings**:
- **Orientation**: 🖼️ Landscape (for presentations)
- **Visual Style**: 🎨 Auto-select (or Editorial for professional look)
- **Level of Detail**: 📝 Standard
- **Language**: English

**Custom Prompt Field** (paste this):
```
Create infographic showing Kit v3 readiness - 80% production-ready infrastructure reuse.

Theme: Infrastructure reuse analysis for stakeholder presentations
Purpose: Show investment value and timeline advantage

Visual Structure:
1. Hero Number: 80% (large, prominent, use green from design system)
   Subtext: "$X worth of R&D investment reusable"

2. Production-Ready Components (Green Section):
   - ✅ 6-Stage Validation Pipeline
   - ✅ DoclingDocument Structured Parsing
   - ✅ Evidence Attribution System
   - ✅ BDD Generation Pipeline
   - ✅ HITL Queue Management
   - ✅ Schema Validation Gates

3. The 20% Gap (Purple Section - validation needed):
   - 🔨 Template Injector System
   - 🔨 Hash Validation Comparator
   - 🔨 ORCA Attribute Validators

4. Timeline Impact:
   6 weeks to bridge 20% gap vs 6 months if starting from scratch
   5x faster time to market

5. ROI Calculation:
   $Y development cost avoided through reuse

Style: Large numbers lead, pie chart or horizontal bars for breakdown, component checklist with status indicators.

Apply design system from notebooklm_persona_config.md (green=ready, purple=building, amber=attention).
```

---

### `/infographic-risk` - Risk Assessment

```
Using the uploaded sources (codebase_analysis.md and kit_v3_gap_analysis.md), create an Infographic showing the risk assessment.

Title: "Kit v3 Risk Management - 5 P0 Risks Identified"
Theme: Risk mitigation and confidence-building

Visual Structure:
1. Risk Summary: 5 P0 Risks, All Mitigated

2. Risk Matrix (2x2 grid):
   - High Impact / High Likelihood: 2 risks
     - Tuning Bleed (mitigation: canon-only validator)
     - Nondeterministic Formatting (mitigation: deep_sort_dict)
   - High Impact / Low Likelihood: 3 risks
     - Validator tuned to corpus (mitigation: golden fixture)
     - Stale cached schema (mitigation: byte hash gate)
     - Hand-edited projections (mitigation: BDD generation)

3. Mitigation Status:
   - ✅ 5/5 risks have mitigation plans
   - ✅ 5/5 mitigations tested with CAREERS-171
   - ✅ 0 unmitigated risks

4. Confidence Score:
   HIGH CONFIDENCE (backed by evidence)
   - Golden fixture proves reproducibility
   - Byte-identical hash proves determinism
   - 80% reuse proves maturity

Style: Risk matrix, status indicators, confidence badges
Export: High-res PNG for risk reviews
```

---

## 🚀 Quick Start

### Step 1: Configure Notebook
1. Click **Configure Chat** → **Custom**
2. Paste instructions from `notebooklm_persona_config.md`
3. Save

### Step 2: Upload Files to NotebookLM
- `codebase_analysis.md` (your data)
- `kit_v3_gap_analysis.md` (your data)
- `notebooklm_quick_commands.md` (this file)
- `tokens.css` (optional design system)

### Step 3: Run Commands in Chat
Type in NotebookLM chat:
- "Use `/video-exec` to create executive video"
- "Generate PowerPoint using `/slides-arb`"
- "Create architecture mind map with `/mindmap-arch`"

NotebookLM will reference the uploaded .md files automatically.

---

**Architecture**:
- **Notebook Config** → `notebooklm_persona_config.md` (persona/style)
- **Source Files** → Upload .md files (any length)
- **Chat Commands** → Reference uploaded files by name
- **Design System** → `tokens.css` (purple/blue/green/amber)

**File Versions**:
- This file: Quick commands (~500 lines)
- Full library: `notebooklm_visualization_prompt.md` (1577 lines)
- Config: `notebooklm_persona_config.md` (notebook-level settings)
