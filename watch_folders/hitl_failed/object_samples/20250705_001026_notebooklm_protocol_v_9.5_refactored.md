# 📝 DUX v9.5 NotebookLM Protocol (Refactored for Live Use)

**Protocol Version:** v9.5-20240610-1  
**Session Log:** [Paste session notes here as you go]  
**Schema Compliance:** DUX v9.5 with proper field names and evidence maturity tiers

---

## 🔖 Quick Reference: DUX v9.5 Schema Requirements

### Required Fields by Object Type:
- **Problem**: `object_type`, `id`, `job_statement` (JTBD format), `evidence_maturity`, `evidence`
- **Behavior**: `object_type`, `id`, `user_enablement` (enablement format), `behavior_type`, `signals`, `acceptance_criteria`, `evidence_maturity`, `evidence`
- **Result**: `object_type`, `id`, `target_impact`, `success_criteria`, `evidence_maturity`, `evidence`
- **Flow**: `object_type`, `id`, `title`, `behavior_sequence`, `evidence_maturity`, `evidence`
- **UserOutcome**: `object_type`, `id`, `outcome_statement`, `evidence_maturity`, `evidence`
- **Provenance**: `object_type`, `id`, `evidence_block` (source_filename, timestamp_in, timestamp_out, quote, citation, evidence_type)

### ⚠️ CRITICAL: Simultaneous Provenance Extraction
**Every DUX object extraction MUST include simultaneous Provenance object creation** with:
- Direct quotes with precise timestamps
- Complete source attribution
- Evidence type classification
- Citation format: "Who said it, when, and where"

### Evidence Maturity Tiers (v9.5):
- `01_assumptive` - Inferred, no direct support
- `02_anecdotal` - 1-2 qualitative signals  
- `03_early_signal` - Recurring signal, no quant
- `04_balanced_signal` - Qualitative + quantitative
- `05_triangulated` - Cross-method validation

---

## 🗂️ Extraction Block Template

### 1. Data Priority & Source Context

**Data Priority:** [e.g., Study Log, Roadmap, Survey, etc.]  
**Source(s):** [List files, transcripts, etc.]  
**Extraction Target:** [Problem/Behavior/Result/Flow/UserOutcome]  
**Evidence Focus:** [What kind of evidence are you looking for?]  
**Citation Format:** [e.g., [Participant, Source, Timestamp]]

---

### 2. Extraction Prompt

> **Prompt:**  
> [Paste the exact prompt here with v9.5 schema requirements inline]

---

### 3. Live Log (Paste as you go)

- **Timestamp:**  
- **Researcher:**  
- **Protocol Version:**  
- **Prompt Used:**  
- **Notes/Evidence:**  
- **Decisions/Edits:**  
- **Object Extracted:**  
- **Provenance Objects Created:** [List all provenance IDs created]  
- **Evidence Maturity:**  
- **Cross-References:**  
- **Schema Compliance Check:** [Y/N, notes]

---

### 4. Researcher Decision Gate

- [ ] Satisfied, proceed to next extraction
- [ ] Needs revision/clarification
- [ ] Flag for follow-up

---

## 🌀 Example: Extraction Block (Behavior Object)

### 1. Data Priority & Source Context

**Data Priority:** Study Log  
**Source(s):** RHOAIUXR_Notebooks2.0_Exploration__UXDR4247_Study Log  
**Extraction Target:** Behavior  
**Evidence Focus:** Collaboration behaviors between platform and data science teams  
**Citation Format:** [Participant, Study Log, Page/Section]

---

### 2. Extraction Prompt

> **Prompt:**  
> Extract atomic Behaviors that are digitally observable at 1000+ user scale, compliant with DUX v9.5 schema:
> - Format: '[Persona] is able to [task/action]' (use `user_enablement` field)
> - Map to Given/When/Then BDD constructs
> - Focus on collaboration behaviors
> - Acceptance criteria must be testable
> - Evidence maturity tier required (01_assumptive to 05_triangulated)
> - Add signals array for measurable behaviors
> - Required fields: object_type, id, user_enablement, behavior_type, signals, acceptance_criteria, evidence_maturity, evidence

---

### 3. Live Log

- **Timestamp:** 2024-06-10 10:15am  
- **Researcher:** [Your Name]  
- **Protocol Version:** v9.5-20240610-1  
- **Prompt Used:** Behavior Extraction  
- **Notes/Evidence:** "Platform admin is able to assign resource quotas to data science teams" [P3, Study Log, Section 2.1]  
- **Decisions/Edits:** Added signal: resource_quota_assigned_event  
- **Object Extracted:**  
  ```json
  {
    "object_type": "Behavior",
    "id": "behavior_20240610_01",
    "user_enablement": "Platform admin is able to assign resource quotas to data science teams",
    "behavior_type": "Task",
    "signals": ["resource_quota_assigned_event"],
    "acceptance_criteria": ["Quota assigned and visible in dashboard"],
    "evidence_maturity": "03_early_signal",
    "evidence": ["provenance_20240610_01"]
  }
  ```
- **Provenance Objects Created:**  
  ```json
  {
    "object_type": "Provenance",
    "id": "provenance_20240610_01",
    "evidence_block": {
      "source_filename": "RHOAIUXR_Notebooks2.0_Exploration__UXDR4247_Study Log.md",
      "participant_id": "P3",
      "timestamp_in": "Section 2.1",
      "timestamp_out": "Section 2.1",
      "teaser": "Platform admin describes resource quota assignment process",
      "quote": "When we need to assign resource quotas to data science teams, we currently have to go through multiple approval layers which slows down the process significantly.",
      "citation": "Participant 3, Study Log Section 2.1, RHOAIUXR_Notebooks2.0_Exploration__UXDR4247_Study Log.md",
      "evidence_type": "user_research_finding"
    }
  }
  ```
- **Evidence Maturity:** 03_early_signal  
- **Cross-References:** Problem: problem_20240610_01  
- **Schema Compliance Check:** Y

---

### 4. Researcher Decision Gate

- [x] Satisfied, proceed to next extraction

---

## 📋 NotebookLM Export Format (Markdown-Embedded JSON)

### Template for NotebookLM Output:

```markdown
# DUX v9.5 Extraction Results

## Session Metadata
- **Protocol Version:** v9.5-20240610-1
- **Extraction Date:** 2024-06-10
- **Sources Used:** [List sources]
- **Evidence Quality Summary:**
  - 05_triangulated: [count] objects
  - 04_balanced_signal: [count] objects
  - 03_early_signal: [count] objects
  - 02_anecdotal: [count] objects
  - 01_assumptive: [count] objects

## Extracted Objects

### Problem Objects
```json
{
  "object_type": "Problem",
  "id": "problem_example_001",
  "job_statement": "When managing platform costs, I want visibility into consumption patterns, so I can optimize resources effectively.",
  "end_user": ["Platform Engineer", "Cost Manager"],
  "what_is_at_stake": "Uncontrolled cost growth without visibility",
  "evidence_maturity": "04_balanced_signal",
  "evidence": ["provenance_001", "provenance_002"]
}
```

### Behavior Objects
```json
{
  "object_type": "Behavior", 
  "id": "behavior_example_001",
  "user_enablement": "Platform admin is able to generate cost reports",
  "behavior_type": "Task",
  "signals": ["cost_report_generated_event"],
  "acceptance_criteria": ["Report generated within 30 seconds"],
  "evidence_maturity": "03_early_signal",
  "evidence": ["provenance_003"]
}
```

### Provenance Objects (Evidence Trackers)
```json
{
  "object_type": "Provenance",
  "id": "provenance_001",
  "evidence_block": {
    "source_filename": "interview_transcript_p7.md",
    "participant_id": "participant_7",
    "timestamp_in": "00:12:00",
    "timestamp_out": "00:12:45",
    "teaser": "User describes cost visibility challenges",
    "quote": "We have no way to see where our platform costs are going. It's like flying blind when making optimization decisions.",
    "citation": "Participant 7, timestamp 00:12:45, interview_transcript_p7.md",
    "evidence_type": "user_research_finding"
  }
}
```

## Cross-Object Relationships
[List relationships between objects]

## Evidence Gaps Requiring Additional Research
[List areas needing more validation]
```

---

## 🧩 How to Use This Protocol

1. **Duplicate Extraction Block** for each prompt/data source
2. **Keep all requirements visible** in each block
3. **Use Live Log section** for real-time notes and evidence
4. **Export using markdown-embedded JSON** format for NotebookLM compatibility
5. **Version control** by updating protocol version number for each iteration

---

## 🛠️ Next Steps

Would you like me to:
1. **Create a complete refactored protocol file** with pre-filled blocks for your current data sources?
2. **Update the cognitive primer** to fix the schema compliance issues?
3. **Create a NotebookLM export template** that you can copy-paste directly?

Let me know which would be most helpful for your usability testing workflow! 