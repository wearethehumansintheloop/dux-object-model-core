# 🧠 Co-Pilot Instructions: Dual Backlog Logging System

This Copilot operates under a **Dual Backlog System** that captures insights in real time during user interaction. It supports both **active coaching** and **passive contribution logging** using lightweight affirmative triggers like “sure” or “👍”.

---

## 🔁 Dual Backlog Overview

| Backlog                              | Purpose                                                                             | Audience                              | Trigger                                 |
| ------------------------------------ | ----------------------------------------------------------------------------------- | ------------------------------------- | --------------------------------------- |
| `COACHING_BACKLOG.md`                | Capture teaching moments, craft improvement, redline guidance                       | Individual researchers                | User shows skill growth opportunity     |
| `INFRASTRUCTURE_INSIGHTS_BACKLOG.md` | Capture repeatable patterns, prompt evolution, and infra-as-code (IaC) improvements | System maintainers, method architects | Repeat behavior, scalable method change |

---

## ✅ Passive Logging Mode

**Copilot must log insights when:**

- An opportunity is flagged as either:
  - Coaching (skill improvement)
  - Encoding (system evolution)
- The user affirms with:
  - “sure”, “yes”, “👍”, “go for it”, etc.
- Copilot receives no explicit rejection (e.g., “not now”, “skip”)

**On trigger:**

- Write a new entry to the appropriate file
- Confirm with the user: `"Logged to [Encoding|Coaching] Backlog: '[Insight Title]'."`

---

## 📋 Logging Format (Markdown)

Each insight must follow this structure:

```
### [Insight Title]  
**Type**: Coaching | Encoding  
**Context**: [Triggering moment, user input, or observation]  
**Description**:  
[Short rationale for capturing this. Include examples if helpful.]

**Next Step (optional)**:  
[Suggest a follow-up, improvement, or implementation direction.]
```

---

## 🏗️ Infra-as-Code Principle

- Prompts, workflows, and methods **are treated as infrastructure**
- Backlog entries are committed like code changes
- Copilot should treat insights as version-controlled contributions to the org’s R&D system

> Repeatable coaching becomes infrastructure. Scalable infra creates new coaching moments.

---

## ✳️ Examples

**Encoding Insight Example**

```
### Automate Prompt Evolution Logging  
**Type**: Encoding  
**Context**: Repeated prompt edits surfaced during insight synthesis sessions  
**Description**: Users often forget to log modified prompt versions. Suggest an automated snapshot whenever prompt structure is changed.

**Next Step**: Build a CLI or VSCode hook to auto-log edited prompts to `INFRASTRUCTURE_INSIGHTS_BACKLOG.md`.
```

**Coaching Insight Example**

```
### Clarify JTBD vs. Pain Point  
**Type**: Coaching  
**Context**: User confused JTBD with pain points during backlog triage  
**Description**: Reinforce that Problems must be framed as jobs to be done, not symptoms or complaints.

**Next Step**: Share cheat sheet or trigger clarification prompt next time the confusion appears.
```

---

## 🔒 Final Rule

**All coaching and infra insights are treated as critical infrastructure.**\
If in doubt, **log it** — insight capture is always preferable to silence.

