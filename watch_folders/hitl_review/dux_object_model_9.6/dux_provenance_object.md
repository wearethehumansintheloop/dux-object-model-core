&#x20;&#x20;

### 🧬 Object Type: `Provenance`

Represents a traceable, timestamped, and participant-attributed molecule composed of evidence attributes (atoms) used to support DUX objects like Problem, Behavior, Result, and Insight.

---

### 🔐 Required Fields

| Field               | Type                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |   |   |
| ------------------- | ------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | - | - |
| `object_type`       | `string` (const: `Provenance`) | Object type discriminator                                                                                                                                                                                                                                                                                                                                                                                                                                                   |   |   |
| `id`                | `string`                       | Unique identifier for this provenance record                                                                                                                                                                                                                                                                                                                                                                                                                                |   |   |
| `source_filename`   | `string`                       | Name of the source file (e.g., transcript or dataset)                                                                                                                                                                                                                                                                                                                                                                                                                       |   |   |
| `timestamp_in`      | `string`                       | Start time or location within source                                                                                                                                                                                                                                                                                                                                                                                                                                        |   |   |
| `timestamp_out`     | `string`                       | End time or location within source                                                                                                                                                                                                                                                                                                                                                                                                                                          |   |   |
| `evidence_maturity` | `string` (enum)                | System-derived evidence quality tier:  - Tiered signal of evidence maturity based on quantity and diversity of linked provenance: - `01_assumptive`: inferred or phase-recommended with no direct support - `02_anecdotal`: 1–2 qualitative signals, low pattern confidence - `03_early_signal`: recurring signal, no quant support - `04_balanced_signal`: blend of qualitative and quantitative support - `05_triangulated`: strong pattern with cross-method validation  |   |   |
| `evidence_block`    | `array`                        | Required array of grouped evidence units — minimum 1 entry to instantiate Provenance object                                                                                                                                                                                                                                                                                                                                                                                 |   |   |

---

### 🔬 Evidence Array (Grouped Attributes)

**Field:** `evidence_block` (array of objects)

Each object includes:

- `teaser`: summary hook
- `quote`: direct quote or paraphrased user statement
- `citation`: formatted attribution (e.g., "Participant 7, timestamp 00:12:45")
- `provenance_id`: backlink to this Provenance object
- `evidence_type`: enum: `pull_quote`, `business_directive`, `user_research_finding`, `trend_insight`, `product_slide`, `design_presentation`, `architectural_doc`
- `confidence_level`: enum: `high`, `medium`

All fields are **required** in each `evidence_block` entry.

---

### 🏷️ Optional Fields

- `evidence_teaser`: Optional summary of insight hook for pain point, stat, or finding — this may also serve as the generated 'insight story header' when multiple core objects are chained (Problem, Key Behavior, Result) and have discrete and related provenance objects attributed. 
- `tags`: System-derived tags from DUX scan (not manually added)
- `created_at`, `updated_at`: Timestamps

---

### 🔗 Usage Context

- Linked via `provenance_id` in DUX objects
- Aggregated to derive Insight object `evidence_maturity`
- Governs auditability and traceability of synthesized claims

---

### 🧠 Notes

- `EvidenceBlock` is a view within `Provenance`, not a standalone molecule
- Atoms = individual attribute values (e.g. `quote`, `confidence_level`), not objects
- Molecules = any composite object traceable to atomic provenance
- **Deprecated Evidence Status **
- **Added Evidence-maturity attribute Rationale:** Enables progressive maturity modeling for insights. Replaces static classification with a signal evolution framework grounded in traceable, multi-method evidence accumulation. Supports automation, sequencing, and prioritization logic.

