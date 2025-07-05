## 📘 Fit Template Primer V2: Response Behavior Reference

This primer outlines how the LLM should respond to each user-issued Fit Protocol prompt in Phase 2. It does **not** include the prompts themselves — those are defined in the protocol. Instead, this document defines expected response behavior to support trust, testability, and governance.

---

### 🧩 `load blueprint fit`
**Expected LLM Behavior**:
- Parse the supplied Fit Template object
- Output a summary of expected Problem, Behavior, and Result object patterns
- Optionally tag which object types are prioritized by stakeholder
- Cache structure for cross-reference in later steps

---

### 🧩 `evaluate fit`
**Expected LLM Behavior**:
- Ingest the submitted `.json` array of DUX objects
- For each object:
  - Evaluate against Fit Template criteria
  - Tag object with `fit_matched: true/false`
  - Add `fit_alignment_reason: <explanation>` string
- Generate:
  - Markdown table with object ID, type, match status, and rationale
  - Updated `.json` array for matched objects

---

### 🧩 `summarize matches`
**Expected LLM Behavior**:
- Provide a narrative summary of:
  - Total evaluated vs matched objects
  - Fit quality and thematic alignment
  - Identified gaps or low-confidence areas
- Include counts by object type and tag

---

### 🧩 `export json`
**Expected LLM Behavior**:
- Output `.json` array with only the `fit_matched: true` objects
- Each object should retain:
  - Original fields
  - `fit_alignment_reason`
- Include metadata block with:
  - `total_objects`, `matched_objects`, `generated_at`, `fit_template_version`

---

Use this primer as a test oracle for auditing LLM behavior at each protocol step.
It is implementation-agnostic and applies to all DUX object extractions using a declared Fit Template for insight alignment.

