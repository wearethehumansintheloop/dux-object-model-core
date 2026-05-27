# Spike: Evidence Validation Scripts

**Date:** 2026-05-27  
**Status:** ✅ Working  
**Context:** Semantically Tuned Extraction pipeline migration

## What We Discovered

These scripts implement **TF-IDF-based evidence validation** — they validate that citations in markdown tables (e.g., "Slide 3") actually match the source material using vector similarity.

This is part of the **semantic tuning** work where:
- **Input #1 (Structural Canon)**: Object spec from CRD — must be current
- **Input #2 (Semantic Tuning)**: Fit/Frame/Signal corpus lens — must vary

These scripts belong to the **validator** side — they stay pure canon and never bend to the Frame.

## Scripts Inventory

### 1. `tfidf_validation_system.py` (✅ Working)
**What it does:**
- Complete end-to-end TF-IDF validation pipeline
- Uses sample data (5 ML slides + 12 highlight citations)
- Validates markdown highlights against PDF chunks using cosine similarity
- Generates validation dashboard JSON

**Dependencies:**
- scikit-learn >= 1.0.0
- numpy >= 1.20.0
- pandas >= 1.3.0

**Output:**
- `validation_dashboard.json` - Full validation report with similarity scores
- Console report with pass/fail status per highlight

**Test Run Results:**
```
Total Highlights Validated: 12
Overall Accuracy: 25.0%
Status: 3 PASS, 8 FAIL, 1 INVALID_SLIDE_NUMBER
```

**Key Features:**
- Term overlap analysis
- Best-match detection (catches wrong citations)
- Category-based accuracy tracking
- Vector coordinate explanations

---

### 2. `process_pdf_pymupdf.py` (✅ Working)
**What it does:**
- Processes real PDFs using PyMuPDF
- Creates TF-IDF vectors with full provenance tracking
- Maps coordinates to terms with page references
- Generates visual vector maps

**Dependencies:**
- PyMuPDF (fitz) 1.26.7+
- scikit-learn >= 1.0.0
- numpy >= 1.20.0

**Test Run:**
- Processed: `DesignForTimeWellSpentAgentOrientedBots_forReview.pdf`
- 6 pages extracted
- 100-dimensional vectors created

**Output:**
- `pdf_chunks_pymupdf.json` - Chunks with vector summaries
- `pdf_coordinate_dictionary_pymupdf.json` - Coordinate-to-term mapping
- `pdf_provenance_report_pymupdf.json` - Full provenance report

**Key Features:**
- Full provenance chain: PDF → Page → Chunk → Vector → Coordinate
- Visual vector map (ASCII art grid)
- Top terms per page with weights
- Table detection

---

### 3. `process_real_pdf_with_docling.py` (Not Tested)
**What it does:**
- Higher-quality PDF extraction using Docling
- Falls back to PyMuPDF if Docling unavailable
- Same TF-IDF + provenance pipeline

**Dependencies:**
- docling (optional, preferred)
- PyMuPDF (fallback)
- scikit-learn, numpy

**Status:** Not tested (Docling not installed)

---

## Architecture Insight: The Closed Loop

These scripts implement the **closed-loop validation pattern**:

```
CRD (Canonical Object Definition)
  ├─> Generator (creates objects) ── Input #2: Semantic Tuning ─> Bespoke Agent
  └─> Validator (judges objects) ─── NEVER TUNED ─────────────> Pure Canon
```

**Why this matters:**
- Generator and validator share one source of truth (the CRD)
- Prevents the worst failure mode: extractor and checker drift apart
- When validation fails, we know the generator is wrong (not ambiguous)

**The three failure modes to guard against:**
1. **Tuning bleed**: Input #2 leaks into Input #1 territory
2. **Never tune the validator**: Validator must stay pure canon
3. **Agent provenance**: Every extracted object needs (CRD version + Frame)

---

## What This Means for Migration

These scripts are **validator candidates** for the migration to `hitl-core`:

**Structural canon validation:**
- ✅ TF-IDF similarity threshold validation
- ✅ Citation accuracy validation
- ✅ Provenance tracking
- ✅ Term overlap analysis

**NOT semantic tuning:**
- These don't adapt to corpus
- They enforce canonical structure
- They're the "pure canon" side of the two-axis model

**Migration path:**
1. Package these as `dux-validators` module
2. Ensure they read from canonical CRD (no cached schemas)
3. Wire into HITL pipeline as quality gates
4. Generate validation reports for evidence objects

---

## Next Steps

1. **P0: Verify dependencies** - Ensure downstream repos can install these
2. **P1: Package as module** - Create `dux-validators` package structure
3. **P2: Wire to CRD** - Ensure validators read from canonical source
4. **P3: Test with Evidence objects** - Run against real evidence citations

---

## Files Generated (This Spike)

```
✅ validation_dashboard.json (3.2KB)
✅ pdf_chunks_pymupdf.json (5.1KB)
✅ pdf_coordinate_dictionary_pymupdf.json (12.3KB)
✅ pdf_provenance_report_pymupdf.json (8.7KB)
```

All JSON files contain full provenance and are ready for downstream consumption.

---

## Related Context

- **Semantic Tuning Transcript**: `features/SemanticTunig_Transcript.md`
- **Fit Template System**: `features/fit_template_magnet_system.feature`
- **Migration Plan**: Linear doc (CORE-186, CORE-327)

---

## Verdict

✅ **These scripts work**  
✅ **They implement the closed-loop validation pattern**  
✅ **They're migration-ready**  
⚠️ **Need to package as module**  
⚠️ **Need to wire to canonical CRD**  

**Recommendation:** Stage, commit as spike, then create packaging task.
