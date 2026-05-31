# Migration Proposal: TF-IDF Citation Validator → Standalone Validation Service

## Executive Summary

Extract the TF-IDF citation validation scripts from `dux-object-model-core` and package as a **standalone validation service** that acts as a quality gate between research extraction and downstream applications.

**Current State**: TF-IDF validator operates as spike scripts in `docs/100_START_HERE/`  
**Proposed State**: Standalone microservice consumed by dux-research-platform, career-roadmap-debugger, and other ORCA schema consumers  
**Primary Use Case**: Post-extraction citation validation before Neo4j storage

---

## What We're Migrating

### Source Files (dux-object-model-core/docs/100_START_HERE/)

1. **tfidf_validation_system.py** (Core validator)
   - TF-IDF vectorization of PDF chunks and markdown highlights
   - Cosine similarity calculation for citation validation
   - Dashboard data generation

2. **process_pdf_pymupdf.py** (PDF processor)
   - PyMuPDF-based text extraction
   - Coordinate mapping (page, bbox)
   - TF-IDF vector generation with provenance

3. **process_real_pdf_with_docling.py** (Docling integration)
   - Higher-quality extraction via Docling
   - PyMuPDF fallback
   - Same TF-IDF + provenance output

4. **Supporting Artifacts**
   - `validation_dashboard.html` (Results UI)
   - `interactive_vector_explorer.html` (Vector inspection UI)
   - `run_validation_tests.sh` (Test runner)
   - `HITL_TEST_PLAN.md` (Human validation protocol)
   - `PIPELINE_FOR_FIVE_YEAR_OLDS.md` (Documentation)

---

## Why This Matters

### Problem Statement

**dux-research-platform** extracts Problem, Behavior, and Result objects from research transcripts using LLMs (magents.py). These objects include evidence citations that claim to trace back to source materials (PDFs, transcripts, recordings). However, **there's no validation** between extraction and storage.

**Without citation validation**:
1. ❌ Hallucinated evidence enters the knowledge graph
2. ❌ Downstream apps (career-roadmap-debugger) consume unvalidated objects
3. ❌ ORCA schema consumers can't trust provenance chains
4. ❌ Research integrity compromised

**With TF-IDF citation validator as quality gate**:
1. ✅ Citations verified against source PDFs before storage
2. ✅ Only validated objects flow to Neo4j
3. ✅ Downstream apps receive pre-validated, trustworthy data
4. ✅ Complete provenance chain: PDF → chunk → citation → object

### Business Impact

- **Research Integrity**: Prevents hallucinated evidence in production DUX objects
- **Downstream Trust**: Apps like career-roadmap-debugger consume validated objects
- **ORCA Schema Quality**: Evidence citations meet schema expectations
- **Compliance Ready**: Auditable provenance for regulated industries
- **Multi-Consumer Architecture**: Standalone service supports multiple applications

---

## Integration Architecture

### Standalone Validation Service Model

```
┌─────────────────────────────────────────────────────────────┐
│ Research Extraction (dux-research-platform)                  │
│ └─ magents.py: Extracts Problem/Behavior/Result objects     │
└──────────────────────┬──────────────────────────────────────┘
                       │ HTTP POST /validate
                       ▼
┌─────────────────────────────────────────────────────────────┐
│ TF-IDF Citation Validator (Standalone Service)              │ ← NEW
│ ├─ FastAPI REST API on port 8505                            │
│ ├─ vectorize_pdf_chunks() (TF-IDF per chunk)                │
│ ├─ validate_citations() (cosine similarity)                 │
│ └─ Returns: ValidationResult with PASS/WARN/FAIL            │
└──────────────────────┬──────────────────────────────────────┘
                       │ Validated objects only
                       ▼
┌─────────────────────────────────────────────────────────────┐
│ Neo4j Knowledge Graph (port 7687)                           │
│ └─ Stores: Only objects that passed citation validation     │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│ Downstream Application Consumers                             │
│ ├─ career-roadmap-debugger (ORCA schema consumer)           │
│ ├─ dux-white-label-ui (React frontend)                      │
│ └─ Future applications consuming DUX objects                 │
└─────────────────────────────────────────────────────────────┘
```

### Service API Contract

```python
# POST /validate/citations
{
  "citations": [
    {
      "citation_id": "uuid-123",
      "text": "Platform engineers spend 40% of time on security reviews",
      "claimed_source": "interview_joel_gpu.pdf",
      "claimed_chunk_id": "abc123def456",
      "object_type": "Problem",
      "object_id": "problem-cost-optimization-v1"
    }
  ],
  "source_pdfs": [
    {
      "pdf_path": "s3://research-sources/interview_joel_gpu.pdf",
      "doc_hash": "sha256:def789..."
    }
  ]
}

# Response
{
  "validation_results": [
    {
      "citation_id": "uuid-123",
      "status": "PASS",  # PASS | WARN | FAIL
      "similarity_score": 0.87,
      "matched_chunk_id": "abc123def456",
      "confidence": "high",
      "provenance": {
        "page": 3,
        "bbox": [100, 200, 400, 250],
        "source_text": "Our platform engineers are spending approximately 40% of their time..."
      }
    }
  ],
  "summary": {
    "total": 1,
    "passed": 1,
    "warned": 0,
    "failed": 0
  }
}
```

### Data Flow

```
┌──────────────┐
│  Source PDF  │
└──────┬───────┘
       │
       ▼
┌──────────────────────────────────────────────────────────┐
│ 1. Docling Converter (existing Pre-processor)            │
│    → Extracts text chunks with charspan provenance       │
└──────┬───────────────────────────────────────────────────┘
       │
       ▼
┌──────────────────────────────────────────────────────────┐
│ 2. chunk_id.py (existing Hash service)                   │
│    → SHA-256(canonical_text | self_ref | doc_hash)       │
└──────┬───────────────────────────────────────────────────┘
       │
       ▼
┌──────────────────────────────────────────────────────────┐
│ 3. vectorize_pdf_chunks() (NEW - TF-IDF service)         │
│    → Generates TF-IDF vector per chunk                   │
│    → Stores: {chunk_id, tfidf_vector, provenance}        │
└──────┬───────────────────────────────────────────────────┘
       │
       ▼
┌──────────────────────────────────────────────────────────┐
│ 4. LLM generates citations (external process)            │
│    → Produces: [{text, claimed_chunk_id, source_doc}]    │
└──────┬───────────────────────────────────────────────────┘
       │
       ▼
┌──────────────────────────────────────────────────────────┐
│ 5. validate_attribution() (NEW - TF-IDF validator)       │
│    → Vectorizes citation text                            │
│    → Computes cosine similarity vs. claimed chunk        │
│    → Returns: PASS (>0.7) | WARN (0.4-0.7) | FAIL (<0.4) │
└──────┬───────────────────────────────────────────────────┘
       │
       ▼
┌──────────────────────────────────────────────────────────┐
│ 6. generate_dashboard() (NEW - Results UI)               │
│    → HTML dashboard with color-coded results             │
│    → Interactive vector explorer                         │
└──────────────────────────────────────────────────────────┘
```

---

## Technical Specifications

### Module Structure (New Standalone Repo)

```
dux-citation-validator/  (NEW REPO)
├── src/
│   └── citation_validator/
│       ├── __init__.py
│       ├── api.py                     # FastAPI service (port 8505)
│       ├── tfidf_validator.py         # Core TF-IDF logic
│       ├── pdf_processor.py           # Docling + PyMuPDF
│       ├── chunk_id.py                # Deterministic ID generation
│       └── models.py                  # Pydantic models
├── tests/
│   ├── test_tfidf_validator.py
│   ├── test_pdf_processor.py
│   └── test_api.py
├── dashboards/
│   ├── validation_dashboard.html      # Results UI
│   └── interactive_vector_explorer.html
├── docs/
│   ├── API.md                         # REST API documentation
│   ├── DEPLOYMENT.md                  # Docker/K8s deployment
│   └── INTEGRATION_GUIDE.md           # How to consume this service
├── docker-compose.yml                 # Local dev environment
├── Dockerfile
├── requirements.txt
└── README.md
```

### Integration with Existing Services

```python
# dux-research-platform/src/magnets_frame_api.py (UPDATED)

import requests

def extract_and_store_objects(transcript_path, source_pdfs):
    # Step 1: Extract objects with LLM
    extracted_objects = extract_problems_behaviors_results(transcript_path)
    
    # Step 2: Call citation validation service
    validation_response = requests.post(
        "http://citation-validator:8505/validate/citations",
        json={
            "citations": [
                {
                    "citation_id": obj.id,
                    "text": obj.evidence.text,
                    "claimed_source": obj.evidence.source,
                    "claimed_chunk_id": obj.evidence.chunk_id,
                    "object_type": obj.type,
                    "object_id": obj.id
                }
                for obj in extracted_objects
            ],
            "source_pdfs": [{"pdf_path": pdf} for pdf in source_pdfs]
        }
    )
    
    # Step 3: Filter objects based on validation
    validation_results = validation_response.json()["validation_results"]
    validated_objects = [
        obj for obj in extracted_objects
        if validation_results[obj.id]["status"] == "PASS"
    ]
    
    # Step 4: Store in Neo4j
    store_objects_in_graph(validated_objects)
    
    return validated_objects
```

### API Contract

```python
# tfidf_citation_validator.py

def vectorize_pdf_chunks(
    pdf_path: str,
    doc_hash: str,
) -> dict[str, TFIDFChunk]:
    """Generate TF-IDF vectors for all chunks in a PDF.
    
    Returns:
        {chunk_id: TFIDFChunk(chunk_id, vector, provenance)}
    """
    pass

def validate_attribution(
    citation_text: str,
    claimed_chunk_id: str,
    chunk_vectors: dict[str, TFIDFChunk],
    threshold: float = 0.7,
) -> ValidationResult:
    """Validate a citation against its claimed source chunk.
    
    Returns:
        ValidationResult(
            status="PASS" | "WARN" | "FAIL",
            similarity_score=float,
            matched_chunk_id=str,
            confidence=float,
        )
    """
    pass
```

### Extended Data Models

```python
# verbatim_source_validator/models.py (extend existing)

@dataclass(slots=True)
class TFIDFChunk(SourceChunk):
    """SourceChunk extended with TF-IDF vector."""
    tfidf_vector: np.ndarray
    vocabulary: dict[str, int]  # term → index mapping
    
@dataclass(slots=True)
class CitationValidationResult(ValidationResult):
    """ValidationResult extended with TF-IDF similarity."""
    similarity_score: float
    similarity_status: str  # "PASS" | "WARN" | "FAIL"
    top_matches: list[tuple[str, float]]  # [(chunk_id, score), ...]
```

---

## Dependencies

### Python Packages (Add to hitl-drift requirements.txt)

```
scikit-learn>=1.3.0  # TF-IDF vectorization
numpy>=1.24.0        # Vector operations
pandas>=2.0.0        # Dashboard data processing
PyMuPDF>=1.23.0      # PDF coordinate extraction (fallback)
```

**Note**: Docling is already installed in hitl-drift for `drift_detect.py`.

---

## Migration Plan

### Phase 1: Core Validator (1 week)

**Deliverables**:
- [ ] Copy `tfidf_validation_system.py` → `scripts/tfidf_citation_validator.py`
- [ ] Refactor to use existing `chunk_id.py` for deterministic IDs
- [ ] Wire to `verbatim_source_validator.ingest.chunks_from_docling_items()`
- [ ] Add `TFIDFChunk` model to `verbatim_source_validator/models.py`
- [ ] Write pytest suite (`test_tfidf_citation_validator.py`)

**Acceptance Criteria**:
- TF-IDF vectorization produces deterministic outputs for same input
- Integration with `chunk_id` system maintains ID stability
- Test coverage ≥ 80%

### Phase 2: PDF Coordinate Mapping (1 week)

**Deliverables**:
- [ ] Copy `process_pdf_pymupdf.py` → `scripts/process_pdf_with_tfidf.py`
- [ ] Integrate with Phase 1 TF-IDF validator
- [ ] Extend provenance to include `(page, bbox)` coordinates
- [ ] Docling-first extraction with PyMuPDF fallback

**Acceptance Criteria**:
- Every chunk carries PDF coordinates (page, x0, y0, x1, y1)
- Coordinate accuracy verified against ground truth annotations
- Docling → PyMuPDF fallback works seamlessly

### Phase 3: Dashboards & HITL (1 week)

**Deliverables**:
- [ ] Copy `validation_dashboard.html` → `dashboards/validation_dashboard.html`
- [ ] Copy `interactive_vector_explorer.html` → `dashboards/interactive_vector_explorer.html`
- [ ] Update dashboard to consume new API outputs
- [ ] Migrate `HITL_TEST_PLAN.md` → `docs/HITL_TEST_PLAN_TFIDF.md`
- [ ] Migrate `PIPELINE_FOR_FIVE_YEAR_OLDS.md` → `docs/TFIDF_CITATION_VALIDATION.md`

**Acceptance Criteria**:
- Dashboard displays color-coded validation results (PASS=green, WARN=yellow, FAIL=red)
- Vector explorer visualizes chunk similarity space
- HITL testers can execute validation workflow per documented plan

### Phase 4: Integration Testing (1 week)

**Deliverables**:
- [ ] End-to-end BDD scenario: PDF → chunks → vectors → validation → dashboard
- [ ] Compare TF-IDF alignment vs. `drift_detect.py` difflib alignment
- [ ] Performance benchmarks (time, memory) for large PDFs (100+ pages)
- [ ] Integration with existing `drift_detect.py` pipeline

**Acceptance Criteria**:
- Full pipeline runs successfully on 3+ real research PDFs
- TF-IDF validator identifies correct chunk matches with ≥90% accuracy
- Performance: <10 seconds for 50-page PDF processing
- Dashboard generates in <2 seconds

---

## Alignment with Existing Tickets

| **Linear Ticket** | **Status** | **Relation to TF-IDF Migration** |
|-------------------|------------|----------------------------------|
| **DRIFT-37** | In Progress | EU AI Act Article 13 — parent epic |
| **DRIFT-38** | In Progress | WORDS axis — `drift_detect.py` provides this |
| **DRIFT-39** | In Progress | SOURCE axis — **TF-IDF validator implements this** |
| **DRIFT-40** | In Progress | PLACE axis — **PyMuPDF coordinates implement this** |
| **DRIFT-41** | In Progress | MEANING axis — TF-IDF baseline, future embeddings (DRIFT-46) |
| **DRIFT-42** | Blocked | Pre-processor — Docling already exists |
| **DRIFT-43** | Blocked | Hash service — `chunk_id.py` already exists |
| **DRIFT-44** | In Review | Drift verb harvest — cherry-pick complete |
| **DRIFT-45** | Blocked | TF-IDF microservice — **this migration enables refactoring** |
| **DRIFT-46** | Backlog | Embeddings — TF-IDF provides baseline to compare against |
| **DRIFT-47** | In Review | Docling round-trip test — validates end-to-end pipeline |

**Key Insight**: DRIFT-42 and DRIFT-43 are marked "Blocked" but **already exist**. This migration proposal unblocks DRIFT-45 by proving the TF-IDF validator works.

---

## Risks & Mitigations

| **Risk** | **Impact** | **Mitigation** |
|----------|-----------|----------------|
| TF-IDF is slower than difflib for large docs | Medium | Benchmark first; consider FAISS indexing for >1000 chunks |
| Cosine similarity thresholds may need tuning | Medium | HITL testing with real research data; document threshold rationale |
| PyMuPDF coordinates may not match Docling charspans | High | Cross-validate coordinates; fall back to charspan when bbox unavailable |
| Existing `drift_detect.py` users might not need citation validation | Low | Keep TF-IDF validator as optional module; doesn't break existing workflows |

---

## Success Metrics

1. **Technical**:
   - TF-IDF validator correctly identifies ≥90% of valid citations (PASS)
   - False positive rate <5% (FAIL when citation is actually valid)
   - Processing time <10s per 50-page PDF

2. **Integration**:
   - Zero breaking changes to existing `drift_detect.py` or `chunk_id.py` APIs
   - All existing pytest tests continue passing
   - New TF-IDF tests achieve ≥80% coverage

3. **Usability**:
   - HITL testers can execute validation workflow in <5 minutes
   - Dashboard provides actionable insights (color-coded, sortable, filterable)
   - Documentation enables new team members to run pipeline without assistance

---

## Open Questions

1. **Threshold Tuning**: What cosine similarity threshold should we use?
   - Current: PASS ≥0.7, WARN 0.4-0.7, FAIL <0.4
   - Needs: HITL testing with real research citations

2. **Hybrid Validation**: Should we run both TF-IDF and difflib alignment?
   - Benefit: Cross-validation increases confidence
   - Cost: 2x processing time

3. **Storage**: Where do we persist TF-IDF vectors long-term?
   - Option A: JSON files (like current Docling exports)
   - Option B: SQLite database
   - Option C: Neo4j (if integrating with research platform)

4. **API Design**: Should TF-IDF validator be synchronous or async?
   - Current: Synchronous (simple, blocking)
   - Future: Async for batch processing?

---

## Recommendation

**Proceed with migration in 4 phases over 4 weeks.**

**Rationale**:
1. ✅ Infrastructure already exists (Docling, chunk_id, SourceChunk)
2. ✅ TF-IDF validator proven working (spike complete, test runner operational)
3. ✅ Completes the 4-axis verification system (DRIFT-37 → DRIFT-41)
4. ✅ Unblocks DRIFT-45 (TF-IDF microservice refactoring)

**Next Step**: Create Linear ticket "DRIFT-XX: Migrate TF-IDF citation validator to hitl-drift" with this proposal as description.

---

## Appendix: File Manifest

### Files to Migrate

```
Source: dux-object-model-core/docs/100_START_HERE/
├── tfidf_validation_system.py           → scripts/tfidf_citation_validator.py
├── process_pdf_pymupdf.py               → scripts/process_pdf_with_tfidf.py
├── process_real_pdf_with_docling.py     → scripts/process_pdf_with_docling_tfidf.py
├── validation_dashboard.html            → dashboards/validation_dashboard.html
├── interactive_vector_explorer.html     → dashboards/interactive_vector_explorer.html
├── run_validation_tests.sh              → scripts/run_tfidf_validation.sh
├── HITL_TEST_PLAN.md                    → docs/HITL_TEST_PLAN_TFIDF.md
├── PIPELINE_FOR_FIVE_YEAR_OLDS.md       → docs/TFIDF_CITATION_VALIDATION.md
└── README_SPIKE_VALIDATION_SCRIPTS.md   → docs/TFIDF_MIGRATION_NOTES.md
```

### Generated Artifacts (Not Migrated)

```
# These are test outputs — regenerate in hitl-drift
docs/100_START_HERE/
├── pdf_chunks_pymupdf.json
├── pdf_coordinate_dictionary_pymupdf.json
├── pdf_provenance_report_pymupdf.json
├── validation_dashboard.json
├── coordinate_dictionary.json
└── *.docling.json
```

---

**Proposal Author**: Claude (AI Assistant)  
**Proposal Date**: 2026-05-30  
**Target Repo**: `wearethehumansintheloop/hitl-drift`  
**Source Repo**: `shut-the-dux-up/dux-object-model-core`  
**Approval Required**: hitl-drift team lead  
**Estimated Effort**: 4 weeks (1 week per phase)
