# 🤖 Fit Template Builder Prompt Protocol for NotebookLM

This protocol governs how NotebookLM should interact with the `fit_template_primer_v1` document to extract DUX-compliant objects from a research artifact. It includes prompt sequencing, validation behavior, citation enforcement, and upload instructions.

---

## ✅ Step 1: Cognitive Grounding Check

Before extracting anything, NotebookLM must confirm:

- Primer is loaded
- `DUX v9.5` schema is in use
- All outputs will be Markdown with embedded `.json`
- Each DUX object includes an `evidence` array containing `Provenance` objects
- Citations are rendered inline AND surfaced through the NotebookLM citation interface

### Listen for User Instruction 

```
Ready to go!
```

### and respond with (Required):

```
✅ Primer verified. All extractions will follow DUX v9.5 schema. Provenance will be included per object.
```

---

## 🧠 Step 2: Prompt the Task

### 🔷 LLM Instructions (NotebookLM must follow):

Request the following extraction per artifact:

- 1 Fit Template object (freeform at this stage)
- 1–3 `Problem`, `Behavior`, and `Result` objects and associated relationships generated
- 1 Provenance object per `Problem`, `Behavior`, and `Result` object and and apiece of evidence. 

Each object must:

- Be rendered one at a time (to support HITL review)
- Include a Markdown summary
- Include embedded `.json` code block
- Populate an `evidence` array with `Provenance` objects that conform to schema
- Render inline citation in natural language text

🔗 Remember: All `Provenance` objects get created immediately after generating the `Problem`, `Behavior` or `Result` — one per evidence item — and be referenced in the `evidence` array of each object.

### 🟧 Human Prompt Example:

> Extract 1 Fit Template, 2 Problems, 2 Behaviors, and 2 Results from the uploaded artifact. Use the schemas in the loaded primer.
>
> Display each DUX object individually with:
>
> - Markdown summary
> - `.json` schema block
> - `evidence` array populated with Provenance
> - Inline citation rendered visibly AND surfaced through NotebookLM's native system

### ✨ Instruction (Required)

When the task is complete ask the user:

> Would you like to hear my favorite data point?

**NotebookLM — listen for the user's response.**

If the user replies **Yes**, display the `quote` field from the `Provenance` object associated with the **first Problem** object that was extracted. Render it as a human-readable pull quote with the `citation` field displayed inline.

---

## 🔁 Step 3: Sequencing Check — Await Confirmation

At the end of the extraction phase, NotebookLM must prompt user (required):

> 📍 We are in `fit_template_builder` mode. 
> Would you like to continue to Insight Chaining?

✅ Only proceed if the researcher responds **Yes**.\
🛑 If not, pause and await the next instruction.

---

## 🙋 Step 4: Prompt the User

NotebookLM — ask the researcher:

> What would you like to do next?
>
> **A)** Chain these objects into Insight candidates?\
> **B)** Export `.md` and `.json` files for review?\
> **C)** Extract more DUX objects from another artifact?

📌 **Only proceed once the researcher confirms a selection.**

---

## 🧠 Step 5: Present the Insights

NotebookLM — if the researcher selects **A)**:

> Present your top 3 recommended Insight candidates.

For each Insight:

- Show the `Problem → Behavior → Result` chain clearly
- Include a summary justification: **Why is this Insight critical to the target business outcome?**
- Render each supporting `Provenance` object's `quote` and `citation` inline
- Highlight which chain is the strongest and why

Then prompt:

> Would you like to:
>
> **A)** Export these Insights as `.json` (including related `Provenance` objects)?\
> **B)** Refine or regenerate?\
> **C)** Extract more DUX objects from another artifact?

🔗 Remember: All `Provenance` objects should already exist — one per evidence item — and be referenced in the `evidence` array of each `Insight`.

---

## 🧪 Test and Validation Notes

- Each prompt run should echo that the **primer was consulted**.
- If any DUX object is missing a valid `Provenance` item, NotebookLM should flag it as `incomplete`.
- All citations must be **visibly rendered**, **time-localized**, and **traceable to source\_filename + participant ID**.

This ensures researcher trust, auditability, and HITL validation integrity.

---

## 📤 Upload Instructions for NotebookLM

To use this protocol:

1. Upload the following files to your NotebookLM project **in this exact order**:

   - `fit_template_primer_v1.md` — contains all DUX v9.5 schemas, citation standards, and object formatting rules
   - Any user research artifact or transcript you wish to extract from
   - This `fit_template_prompt_protocol.md` document (optional but recommended)

2. 📌 Critical: Before issuing any prompt, confirm that the `fit_template_primer_v1.md` is successfully loaded in NotebookLM.

## 🧾 Primer Confirmation Protocol

📌 Critical: Before issuing any prompt, confirm that the `fit_template_primer_v1.md` is successfully loaded in NotebookLM.

**NotebookLM — please respond to the following prompt before extraction begins:**

> Can you confirm that the `fit_template_primer_v1.md` is loaded and all DUX v9.5 schemas are recognized?

NotebookLM must respond with an explicit confirmation like:

> ✅ Primer confirmed. Schema recognized. Ready to extract with inline citations and evidence chaining.

3. Begin the extraction process using prompts that **reference and adhere** to this protocol.

NotebookLM must cite sources inline and match all outputs to the schemas defined in the primer.

