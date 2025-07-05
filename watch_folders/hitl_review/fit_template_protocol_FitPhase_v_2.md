## 🧪 ROSwell Phase 2 Protocol: Evaluating Fit as Insight Engine

### 🎯 Purpose
This phase evaluates whether a **Fit Template–driven pipeline** can synthesize research data into high-fidelity insight chains, serving as **UX infrastructure-as-code** for a second-level system challenge.

---

### 🔁 Protocol Overview

#### Inputs:
- Canonical Fit Template (`ROS_BlueprintFitTemplate.md`)
- 4–8 research artifacts or pre-extracted DUX objects

#### Steps:

### 🧩 Step 1: Load Fit Template
**User Prompt**: 
> `load blueprint fit`

**LLM Response**:
- Confirms receipt of Fit Template
- Outputs summary of expected Problem, Behavior, and Result objects expected
- Caches structure for use in matching

---

### 🧩 Step 2: Submit Extracted DUX Objects
**User Prompt**:
> `evaluate fit`

**LLM Response**:
- Ingests DUX objects
- For each object:
  - Identifies whether the object fits any element of the Fit Template
  - Adds `fit_matched: true/false`
  - Adds `fit_alignment_reason: <freeform>`

Returns:
- Markdown table of matches
- `.json` array with tagged objects (fit-matched only)

---

### 🧩 Step 3: Request Summary
**User Prompt**:
> `summarize matches`

**LLM Response**:
- Narrative summary of:
  - How many matched
  - What themes emerged
  - What gaps or mismatches were observed

---

### 🧩 Step 4: Export Results
**User Prompt**:
> `export json`

**LLM Response**:
- Returns clean, match-tagged `.json` array ready for dataframe use
- Object type counts + stats

---

### 🔧 Prompts Summary (Call & Response)

| User Prompt         | LLM Behavior                                                                 |
|---------------------|------------------------------------------------------------------------------|
| `load blueprint fit`| Accept and summarize Fit Template expectations                               |
| `evaluate fit`      | Analyze submitted DUX objects and tag with fit info                          |
| `summarize matches` | Provide narrative insight into which objects matched and why                 |
| `export json`       | Return `.json` object array (fit-matched only, tagged)                       |

Next step: I’ll update the **Fit Template Primer** to reflect only the expected response behavior when those prompts are used. Say the word. ✅

