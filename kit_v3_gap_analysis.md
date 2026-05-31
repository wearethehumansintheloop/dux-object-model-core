# Kit v3 Object Promotion - Gap Analysis Report

**Generated**: 2026-05-27  
**Upstream**: DUX Object Model Core (v9.6.1)  
**Downstream**: Kit v3 (HITL Skills - ORCA Attributes Promotion)  
**Golden Fixture**: CAREERS-171 (Outcome v3)  
**Target Objects**: 8 (Outcome, User, Skill, Requirement, Credential, Qualification, Standard, Fit)

---

## Executive Summary

This gap analysis compares the **upstream DUX object-model-core governance patterns** against the **downstream Kit v3 promotion requirements** for the `orca-attributes` skill. The analysis identifies what upstream patterns are production-ready (✅), what needs to be built (🔨), and what must be avoided (❌).

**Key Finding**: Upstream has 80% of required infrastructure, but lacks critical deterministic generation and byte-hash validation components needed for canonical governance.

---

## 1. Validation Pipeline - Stage Comparison

### Upstream: DUX 6-Stage Pipeline

| Stage | Purpose | Status | Kit v3 Applicability |
|-------|---------|--------|---------------------|
| **Stage 1** | Structure Validation | ✅ Production | ✅ Use As-Is |
| **Stage 2** | Consistency Validation | ✅ Production | ⚠️ Needs ORCA Extensions |
| **Stage 3a** | Docling Processing | ✅ Production | ✅ Use As-Is (Breakthrough) |
| **Stage 3b** | Schema Validation | ✅ Production | ⚠️ Needs Kit v3 Schemas |
| **Stage 4** | Object Instance Validation | ✅ Production | ⚠️ Needs Bespoke Validators |
| **Stage 5** | BDD Generator | ✅ Production | ✅ Use As-Is |
| **Stage 6** | Prompt Generator | ✅ Production | ✅ Use As-Is |

### Downstream: Kit v3 Required Additions

| Stage | Purpose | Status | Implementation Priority |
|-------|---------|--------|----------------------|
| **Stage 0** | Linear → Injection Contract | ❌ Missing | 🔥 P0 (Must Build) |
| **Stage 2.5** | ORCA Meta-Metadata Validation | ❌ Missing | 🔥 P0 (Must Build) |
| **Stage 3.5** | Deterministic Template Injection | ❌ Missing | 🔥 P0 (Must Build) |
| **Stage 4.5** | Byte Hash Validation | ❌ Missing | 🔥 P0 (Must Build) |
| **Stage 5.5** | Structural Hash Validation | ❌ Missing | 🔥 P0 (Must Build) |
| **Stage 7** | BDD Projection Validation | ❌ Missing | 🟡 P1 (Should Build) |
| **Stage 8** | Forbidden Vocabulary Check | ❌ Missing | 🟡 P1 (Should Build) |

### GAP SUMMARY - Validation Pipeline

```
┌──────────────────────────────────────────────────────────────────┐
│  UPSTREAM (DUX Core) - 6 Stages                                  │
│  ───────────────────────────────────                             │
│  ✅ Structure validation (markdown)                              │
│  ✅ Consistency validation (schema ↔ JSON)                       │
│  ✅ Docling processing (table.data.grid)                         │
│  ✅ Schema validation (object-specific)                          │
│  ✅ Object instance validation (bespoke)                         │
│  ✅ BDD generation (.feature files)                              │
│  ✅ Prompt generation (extraction prompts)                       │
└──────────────────────────────────────────────────────────────────┘
                              ▼
                      [ GAP ANALYSIS ]
                              ▼
┌──────────────────────────────────────────────────────────────────┐
│  DOWNSTREAM (Kit v3) - 9 Stages (6 existing + 3 new)            │
│  ────────────────────────────────────────────────                │
│  ❌ Stage 0: Linear → Injection Contract Extractor               │
│  ✅ Stage 1: Structure validation (reuse upstream)               │
│  ✅ Stage 2: Consistency validation (reuse upstream)             │
│  ❌ Stage 2.5: ORCA Meta-Metadata Validation (NEW)               │
│  ✅ Stage 3a: Docling processing (reuse upstream)                │
│  ❌ Stage 3.5: Deterministic Template Injection (NEW)            │
│  ⚠️ Stage 3b: Schema validation (adapt for Kit v3 schemas)      │
│  ⚠️ Stage 4: Object instance validation (8 new validators)       │
│  ❌ Stage 4.5: Byte Hash Validation (NEW - P0 CRITICAL)          │
│  ❌ Stage 5.5: Structural Hash Validation (NEW - P0)             │
│  ✅ Stage 5: BDD generation (reuse upstream)                     │
│  ✅ Stage 6: Prompt generation (reuse upstream)                  │
│  ❌ Stage 7: BDD Projection Validation (NEW - P1)                │
│  ❌ Stage 8: Forbidden Vocabulary Check (NEW - P1)               │
└──────────────────────────────────────────────────────────────────┘

LEGEND:
  ✅ Production-ready upstream pattern (copy/reuse)
  ⚠️ Upstream pattern exists but needs Kit v3 customization
  ❌ Missing component (must build from scratch)
  🔥 P0 = Must build before Outcome v3 golden fixture
  🟡 P1 = Should build before all-8-objects promotion
```

---

## 2. Docling Extraction - Pattern Comparison

### Upstream: Fixed Docling Parser (Production-Ready ✅)

**Location**: `scripts/docling/fixed_docling_parser.py`

**Key Breakthrough**:
```python
# Structured data access (NOT regex)
for table in doc.tables:
    if hasattr(table, 'data') and table.data and hasattr(table.data, 'grid'):
        grid = table.data.grid  # 2D array of TableCell objects
        headers = [cell.text.strip() for cell in grid[0]]
        
        for row in grid[1:]:
            row_dict = {}
            for j, cell in enumerate(row):
                if j < len(headers):
                    row_dict[headers[j]] = cell.text.strip()
            
            attributes.append(row_dict)
```

**Functions**:
- ✅ `explore_docling_structure()` - Debug/analysis
- ✅ `extract_schema_table_from_docling()` - Main extraction
- ✅ `generate_exploded_attribute_objects()` - Individual attribute files
- ✅ `save_exploded_objects()` - Write outputs

### Downstream: Kit v3 Required Adaptation

**New Function Needed**:
```python
def extract_injection_contract_from_linear(issue_key: str) -> Dict[str, Any]:
    """
    Extract reviewed facts from CAREERS-171 Linear issue.
    Parse Linear markdown body → DoclingDocument → Injection Contract JSON
    """
    # 1. Fetch issue from Linear MCP
    issue = linear_mcp.get_issue(issue_key)
    
    # 2. Parse Linear markdown body using DoclingDocument
    converter = DocumentConverter()
    result = converter.convert_string(issue.body, format='markdown')
    doc = result.document
    
    # 3. Extract Schema Attributes table using table.data.grid
    schema_data = extract_schema_table_from_docling(doc)
    
    # 4. Extract ORCA buckets from issue front matter
    orca_buckets = extract_orca_buckets(issue.body)
    
    # 5. Build injection contract
    return {
        "object_type": extract_object_type(issue.title),
        "version": "3.0.0",
        "orca_buckets": orca_buckets,
        "evidence_coverage": extract_evidence_coverage(schema_data),
        "hitl_review_metadata": {
            "reviewed_by": issue.assignee,
            "review_date": issue.updated_at,
            "linear_issue": issue_key,
            "pizza_score": extract_pizza_score(issue)
        }
    }
```

### GAP SUMMARY - Docling Extraction

| Component | Upstream | Downstream | Gap Status |
|-----------|----------|------------|------------|
| **DoclingDocument Parser** | ✅ `fixed_docling_parser.py` | ✅ Reuse as-is | ✅ No Gap |
| **table.data.grid Pattern** | ✅ Production-ready | ✅ Reuse as-is | ✅ No Gap |
| **Exploded Attributes** | ✅ `generate_exploded_attribute_objects()` | ✅ Reuse as-is | ✅ No Gap |
| **Linear Integration** | ❌ Not applicable | ❌ Must build | 🔥 P0 GAP |
| **ORCA Bucket Extraction** | ❌ Missing | ❌ Must build | 🔥 P0 GAP |
| **Injection Contract Format** | ❌ Missing | ❌ Must build | 🔥 P0 GAP |

---

## 3. Template System - Pattern Comparison

### Upstream: Canonical Object Template Structure (✅)

**Example**: `canonical_vault/dux-core/problem_object.md`

**Template Sections**:
```markdown
# 🟡 Problem Object (v9.6.1)

## 🎯 Purpose & Strategic Role       [CANONICAL]
## 🧠 What would you say you do here? [CANONICAL]
## 💡 Why the Problem Object Matters   [CANONICAL]
## 📋 Schema Attributes                [CANONICAL - byte-locked table]
## 📦 Canonical Example                [CANONICAL - byte-locked JSON]
## 🔗 Structural Role & Usage Notes    [CANONICAL]
```

**Strengths**:
- ✅ Clear section structure
- ✅ Emoji-based section identifiers (easy to parse)
- ✅ Markdown table for schema attributes
- ✅ JSON block for canonical example
- ✅ Consistent across all object types

**Weaknesses**:
- ❌ No separation of canonical vs run-metadata
- ❌ No deterministic injection mechanism
- ❌ No template file (only examples)
- ❌ No hash-bearing section identification

### Downstream: Kit v3 Required Template System

**New Structure**:
```markdown
# {ObjectType} Object (v{version})

## 🎯 Purpose & Strategic Role
<!-- CANONICAL SECTION - Part of byte hash -->
{injected_purpose_text}

## 🧠 What would you say you do here?
<!-- CANONICAL SECTION - Part of byte hash -->
> {injected_job_statement}

## 💡 Why the {ObjectType} Object Matters
<!-- CANONICAL SECTION - Part of byte hash -->
{injected_bullets}

## 📋 Schema Attributes
<!-- CANONICAL SECTION - Part of byte hash -->
| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
{injected_attribute_rows}

## 📦 Canonical Example
<!-- CANONICAL SECTION - Part of byte hash -->
```json
{injected_json_example}
```

## 🔗 Structural Role & Usage Notes
<!-- CANONICAL SECTION - Part of byte hash -->
{injected_usage_notes}

---

## 🔍 HITL Review Report
<!-- NON-CANONICAL - Excluded from byte hash -->
<!-- Generated on: {run_timestamp} -->
<!-- Validated by: {validator} -->
<!-- Stage: {stage_name} -->
<!-- Pizza Score: {pizza_score}/100 -->
<!-- Evidence Coverage: {evidence_count}/{total_attributes} -->

## 🧪 Validation History
<!-- NON-CANONICAL - Excluded from byte hash -->
<!-- Append-only log -->
- {timestamp}: {event_description}
```

**New Components Needed**:
1. ❌ Jinja2 template files (`templates/outcome_v3_template.md`)
2. ❌ Deterministic injector (`inject_canonical_object_deterministic()`)
3. ❌ Hash calculation logic (`calculate_canonical_hash()`)
4. ❌ Section boundary markers (canonical vs run-metadata)

### GAP SUMMARY - Template System

| Component | Upstream | Downstream | Gap Status |
|-----------|----------|------------|------------|
| **Template Structure** | ✅ Consistent across objects | ✅ Reuse structure | ✅ No Gap |
| **Section Identifiers** | ✅ Emoji-based (parseable) | ✅ Reuse as-is | ✅ No Gap |
| **Jinja2 Templates** | ❌ No template files | ❌ Must create | 🔥 P0 GAP |
| **Deterministic Injection** | ❌ No injector | ❌ Must build | 🔥 P0 GAP |
| **Hash Calculation** | ❌ No hash logic | ❌ Must build | 🔥 P0 GAP |
| **Canonical vs Metadata** | ❌ No separation | ❌ Must implement | 🔥 P0 GAP |

---

## 4. Validation Rules - Pattern Comparison

### Upstream: Stage 1 Structure Validation (✅)

**File**: `scripts/validation/hitl_pipeline/stage1_structure_validation.py`

**Current Checks**:
```python
required_sections = {
    "Purpose & Strategic Role": r"## 🎯 Purpose & Strategic Role",
    "What would you say": r"## 🧠 \"What would you say",
    "Why the Object Matters": r"## 💡 Why the .* Object Matters",
    "Schema Attributes": r"## 📋 Schema Attributes",
    "Canonical Example": r"## 📦 Canonical Example",
    "Structural Role": r"## 🔗 Structural Role"
}
```

**Strengths**:
- ✅ Checks required sections present
- ✅ Validates table structure
- ✅ Validates JSON block presence
- ✅ Type-agnostic (works for all object types)

### Upstream: Stage 2 Consistency Validation (✅)

**File**: `scripts/validation/hitl_pipeline/stage2_consistency_validation.py`

**Current Checks**:
```python
def validate_schema_json_consistency(schema_attrs, json_example):
    # Check required fields in JSON
    for attr_name, attr_info in schema_attrs.items():
        if attr_info['required'].lower() == 'yes':
            if attr_name not in json_example:
                errors.append(f"Required field '{attr_name}' missing")
    
    # Check no orphaned JSON fields
    for json_field in json_example.keys():
        if json_field not in schema_attrs:
            errors.append(f"JSON field '{json_field}' not in schema")
    
    # Check type compatibility
    for attr_name, attr_info in schema_attrs.items():
        if attr_name in json_example:
            if not validate_type_compatibility(attr_info['type'], json_example[attr_name]):
                errors.append(f"Type mismatch for '{attr_name}'")
```

**Strengths**:
- ✅ Schema ↔ JSON consistency checks
- ✅ Type compatibility validation
- ✅ Required field enforcement

### Downstream: Kit v3 Required Additional Validators

**New Validator 1: ORCA Meta-Metadata (Stage 2.5)**
```python
def validate_orca_metadata(injection_contract: Dict) -> List[str]:
    errors = []
    
    required_orca_fields = {
        'bucket': ['object', 'relationship', 'cta', 'attribute'],
        'core_vs_supporting': ['core', 'supporting'],
        'evidence_requirement': ['mandatory', 'recommended', 'optional'],
        'synthetic_allowed': [True, False]
    }
    
    for attr in injection_contract['orca_buckets']['attributes']:
        if 'orca_meta' not in attr:
            errors.append(f"Attribute {attr['name']} missing orca_meta")
            continue
        
        meta = attr['orca_meta']
        for field, allowed_values in required_orca_fields.items():
            if field not in meta:
                errors.append(f"Missing orca_meta.{field}")
            elif meta[field] not in allowed_values:
                errors.append(f"Invalid {field}: {meta[field]}")
    
    return errors
```

**New Validator 2: Forbidden Vocabulary (Stage 8)**
```python
FORBIDDEN_TERMS = [
    'confidence',       # No self-reported confidence
    'self_score',       # No self-scoring
    'estimated',        # Must be evidence-backed or synthetic
    'approximately',    # Be precise
    'tuned_for',        # No corpus-specific tuning in canon
    'optimized_for',    # Canon is invariant
    'corpus_specific'   # No corpus leaks
]

def validate_forbidden_vocabulary(content: str) -> List[str]:
    errors = []
    for term in FORBIDDEN_TERMS:
        if re.search(rf'\b{term}\b', content, re.IGNORECASE):
            errors.append(f"Forbidden term: '{term}' (violates canonical invariance)")
    return errors
```

**New Validator 3: Byte Hash (Stage 4.5)**
```python
def validate_byte_hash(file_path: Path, expected_hash: str) -> Dict[str, Any]:
    # Extract canonical sections (exclude run metadata)
    canonical_content = extract_canonical_sections(file_path)
    
    # Calculate byte hash
    actual_hash = hashlib.sha256(canonical_content.encode('utf-8')).hexdigest()
    
    return {
        "passed": actual_hash == expected_hash,
        "actual": actual_hash,
        "expected": expected_hash,
        "failure_mode": "byte_hash_mismatch" if actual_hash != expected_hash else None
    }
```

**New Validator 4: Structural Hash (Stage 5.5)**
```python
def validate_structural_hash(file_path: Path, golden_structure: Dict) -> Dict[str, Any]:
    # Extract structural elements
    structure = {
        'section_count': count_canonical_sections(file_path),
        'table_headers': extract_table_headers(file_path),
        'attribute_names': extract_attribute_names(file_path),
        'required_count': count_required_attributes(file_path),
        'json_keys': extract_json_keys(file_path)
    }
    
    # Calculate structural hash
    structural_hash = hashlib.md5(
        json.dumps(structure, sort_keys=True).encode()
    ).hexdigest()
    
    # Compare against golden
    if structural_hash != golden_structure['hash']:
        diff = deep_diff(structure, golden_structure)
        return {
            "passed": False,
            "structural_hash": structural_hash,
            "diff_classification": classify_structural_diff(diff),
            "hitl_route": determine_hitl_route(diff)
        }
    
    return {"passed": True, "structural_hash": structural_hash}
```

### GAP SUMMARY - Validation Rules

| Validator | Upstream | Downstream | Gap Status |
|-----------|----------|------------|------------|
| **Structure (Stage 1)** | ✅ Production-ready | ✅ Reuse as-is | ✅ No Gap |
| **Consistency (Stage 2)** | ✅ Production-ready | ✅ Reuse as-is | ✅ No Gap |
| **ORCA Meta-Metadata** | ❌ Not applicable | ❌ Must build | 🔥 P0 GAP |
| **Forbidden Vocabulary** | ❌ Missing | ❌ Must build | 🟡 P1 GAP |
| **Byte Hash** | ❌ Missing | ❌ Must build | 🔥 P0 GAP |
| **Structural Hash** | ❌ Missing | ❌ Must build | 🔥 P0 GAP |
| **BDD Projection** | ❌ Not validated | ❌ Must build | 🟡 P1 GAP |

---

## 5. Deterministic Generation - Pattern Comparison

### Upstream: No Deterministic Generation System (❌)

**Current State**:
- ✅ Markdown examples exist (`canonical_vault/`)
- ❌ No template files (Jinja2)
- ❌ No injection API
- ❌ No hash calculation
- ❌ No reproducibility guarantee

**Implication**: Upstream objects are hand-authored, not generated from reviewed facts.

### Downstream: Kit v3 Required Generation System

**Component 1: Jinja2 Template Files**
```jinja2
{# templates/outcome_v3_template.md #}
# {{ object_type }} Object (v{{ version }})

## 🎯 Purpose & Strategic Role
{{ purpose_text }}

## 🧠 What would you say you do here?
> {{ job_statement }}

## 💡 Why the {{ object_type }} Object Matters
{% for bullet in why_matters_bullets -%}
- {{ bullet }}
{% endfor %}

## 📋 Schema Attributes
| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
{% for attr in sorted_attributes -%}
| {{ attr.name }} | {{ attr.type }} | {{ attr.required }} | {{ attr.description }} |
{% endfor %}

## 📦 Canonical Example
```json
{{ canonical_json | tojson(indent=2, sort_keys=True) }}
```

## 🔗 Structural Role & Usage Notes
{{ usage_notes }}
```

**Component 2: Deterministic Injector**
```python
def inject_canonical_object_deterministic(
    contract: Dict[str, Any],
    template_path: Path
) -> str:
    from jinja2 import Environment, FileSystemLoader, select_autoescape
    
    # Create Jinja2 environment with deterministic settings
    env = Environment(
        loader=FileSystemLoader(template_path.parent),
        autoescape=select_autoescape(),
        trim_blocks=True,           # Deterministic whitespace
        lstrip_blocks=True,         # Deterministic whitespace
        keep_trailing_newline=True  # Stable EOF
    )
    
    template = env.get_template(template_path.name)
    
    # CRITICAL: Sort all dict keys for deterministic iteration
    sorted_contract = deep_sort_dict(contract)
    
    # Render
    rendered = template.render(**sorted_contract)
    
    # Normalize line endings (always LF, never CRLF)
    rendered = rendered.replace('\r\n', '\n')
    
    return rendered

def deep_sort_dict(d: Dict) -> Dict:
    """Recursively sort all dict keys."""
    if isinstance(d, dict):
        return {k: deep_sort_dict(v) for k, v in sorted(d.items())}
    elif isinstance(d, list):
        return [deep_sort_dict(item) for item in d]
    else:
        return d
```

**Component 3: Golden Hash Registry**
```python
class GoldenHashRegistry:
    def __init__(self, registry_path: Path):
        self.registry_path = registry_path
        self.registry = self.load_registry()
    
    def register_golden_hash(
        self,
        object_type: str,
        version: str,
        byte_hash: str
    ):
        """Store golden hash for object type."""
        key = f"{object_type}_v{version}"
        self.registry[key] = {
            "hash": byte_hash,
            "registered_at": datetime.now().isoformat(),
            "status": "golden"
        }
        self.save_registry()
    
    def validate_against_golden(
        self,
        object_type: str,
        version: str,
        generated_file: Path
    ) -> Dict[str, Any]:
        """Validate generated file matches golden hash."""
        key = f"{object_type}_v{version}"
        
        if key not in self.registry:
            return {
                "valid": False,
                "error": f"No golden hash registered for {key}"
            }
        
        expected_hash = self.registry[key]['hash']
        actual_hash = calculate_canonical_hash(generated_file)
        
        return {
            "valid": actual_hash == expected_hash,
            "expected": expected_hash,
            "actual": actual_hash,
            "drift": None if actual_hash == expected_hash else {
                "diff": calculate_diff(expected_hash, actual_hash)
            }
        }
```

### GAP SUMMARY - Deterministic Generation

| Component | Upstream | Downstream | Gap Status |
|-----------|----------|------------|------------|
| **Template Files** | ❌ None | ❌ Must create 8 templates | 🔥 P0 GAP |
| **Jinja2 Environment** | ❌ No injector | ❌ Must build | 🔥 P0 GAP |
| **Deterministic Rendering** | ❌ No guarantee | ❌ Must implement | 🔥 P0 GAP |
| **Sorted Dict Iteration** | ❌ Not enforced | ❌ Must implement | 🔥 P0 GAP |
| **Canonical Hash Calc** | ❌ No implementation | ❌ Must build | 🔥 P0 GAP |
| **Golden Hash Registry** | ❌ No registry | ❌ Must build | 🔥 P0 GAP |
| **Drift Detection** | ❌ No tracking | ❌ Must build | 🟡 P1 GAP |

---

## 6. HITL Queue Management - Pattern Comparison

### Upstream: Queue Structure (✅)

**Location**: `watch_folders/`

**Queue Folders**:
```
watch_folders/
├── hitl_review/              # Entry point ✅
├── hitl_review_queue/        # Type-specific queues ✅
│   ├── problem_objects/
│   ├── behavior_objects/
│   └── result_objects/
├── hitl_workshop/            # Refinement needed ✅
├── hitl_failed/              # Major rework ✅
├── hitl_rejected/            # Naming violations ✅
├── hitl_promotion_candidates/ # Passed all stages ✅
└── hitl_approved_for_production/ # Final canonical ✅
```

**Routing Logic** (from `hitl_orchestrator.py`):
```python
def route_validation_failure(file_path, validation_results):
    # Naming convention fail
    if not matches_naming_convention(file_path.name):
        return move_to('hitl_rejected/', file_path)
    
    # Structural fail (Stage 1 or 3)
    if not validation_results['structure']['valid']:
        return move_to('hitl_failed/', file_path)
    
    # Consistency fail (Stage 2)
    if not validation_results['consistency']['valid']:
        return move_to('hitl_workshop/', file_path)
    
    # All passed
    return move_to('promotion_candidates/', file_path)
```

**Strengths**:
- ✅ Clear separation of failure types
- ✅ Type-specific queues for parallel processing
- ✅ Auto-pull logic from queues
- ✅ Error logs stored alongside failed objects

### Downstream: Kit v3 Required Extensions

**New Queue Folders**:
```
watch_folders/
├── linear_extraction/        # NEW: Extracted contracts from Linear
├── injection_staging/        # NEW: Ready for template injection
├── hash_verification/        # NEW: Awaiting golden hash validation
└── (existing folders from upstream)
```

**Enhanced Routing Logic**:
```python
def route_kit_v3_validation_failure(
    file_path: Path,
    byte_hash_result: Dict,
    structural_hash_result: Dict,
    orca_errors: List[str],
    vocab_errors: List[str]
):
    # Naming convention fail → rejected
    if not matches_naming_convention(file_path.name):
        return move_to('hitl_rejected/', file_path)
    
    # Byte hash pass but ORCA/vocab issues → workshop
    if byte_hash_result['passed'] and (orca_errors or vocab_errors):
        return move_to('hitl_workshop/', file_path)
    
    # Structural hash fail → failed (major rework)
    if not structural_hash_result['passed']:
        return move_to('hitl_failed/', file_path)
    
    # Byte hash fail but structure OK → hash_verification (investigate drift)
    if not byte_hash_result['passed'] and structural_hash_result['passed']:
        return move_to('hash_verification/', file_path)
    
    # All passed → promotion
    return move_to('promotion_candidates/', file_path)
```

### GAP SUMMARY - HITL Queue Management

| Component | Upstream | Downstream | Gap Status |
|-----------|----------|------------|------------|
| **Queue Folders** | ✅ 7 folders | ⚠️ Need 3 additional | 🟡 P1 GAP |
| **Routing Logic** | ✅ Production-ready | ⚠️ Needs hash-aware routing | 🔥 P0 GAP |
| **Error Logging** | ✅ Works well | ✅ Reuse as-is | ✅ No Gap |
| **Auto-Pull** | ✅ Implemented | ✅ Reuse as-is | ✅ No Gap |
| **Naming Convention** | ✅ Enforced | ✅ Reuse as-is | ✅ No Gap |

---

## 7. Evidence & ORCA Attribution - Pattern Comparison

### Upstream: Evidence Object Pattern (✅)

**File**: `canonical_vault/dux-core/evidence_object.md`

**Structure**:
```json
{
  "object_type": "Evidence",
  "evidence_id": "EV-001",
  "provenance_id": "PROV-001",
  "pull_quote": "Direct quote from source",
  "reference_context": "job_statement",
  "timestamp": "2025-01-07T10:30:00Z",
  "attribution": "Interview with Sarah, Data Scientist"
}
```

**Strengths**:
- ✅ Direct evidence attribution
- ✅ Pull quote for traceability
- ✅ Reference context (which field it supports)
- ✅ Provenance linkage

**Weaknesses**:
- ❌ No ORCA bucket classification
- ❌ No core vs supporting distinction
- ❌ No evidence requirement level
- ❌ No synthetic flag

### Downstream: Kit v3 ORCA-Enhanced Evidence

**Enhanced Structure**:
```json
{
  "object_type": "Evidence",
  "evidence_id": "EV-CAREERS-171-001",
  "provenance_id": "PROV-LINEAR-CAREERS-171",
  "pull_quote": "Data scientists spend 40% of time managing credentials",
  "reference_context": "outcome_statement",
  "timestamp": "2026-05-27T13:00:00Z",
  "attribution": "CAREERS-171 review by case-arb-architect",
  "orca_meta": {
    "bucket": "attribute",
    "core_vs_supporting": "core",
    "evidence_requirement": "mandatory",
    "synthetic_allowed": false
  },
  "supports_attributes": [
    {
      "attribute_name": "outcome_statement",
      "object_type": "Outcome",
      "object_id": "outcome_v3",
      "fit_score": 0.95
    }
  ]
}
```

**New Fields**:
- `orca_meta` - ORCA bucket classification
- `supports_attributes` - Multi-attribute support tracking
- `fit_score` - Evidence-attribute fit quality

### GAP SUMMARY - Evidence & ORCA Attribution

| Component | Upstream | Downstream | Gap Status |
|-----------|----------|------------|------------|
| **Evidence Object** | ✅ Basic structure | ⚠️ Needs ORCA extensions | 🔥 P0 GAP |
| **Provenance Tracking** | ✅ Works well | ✅ Reuse as-is | ✅ No Gap |
| **Pull Quotes** | ✅ Implemented | ✅ Reuse as-is | ✅ No Gap |
| **ORCA Classification** | ❌ Missing | ❌ Must add | 🔥 P0 GAP |
| **Synthetic Flag** | ❌ Missing | ❌ Must add | 🔥 P0 GAP |
| **Multi-Attribute Support** | ❌ Single-field only | ❌ Must extend | 🟡 P1 GAP |

---

## 8. Golden Fixture Workflow - CAREERS-171 Promotion

### Upstream: No Golden Fixture Workflow (❌)

**Current State**:
- ✅ Example objects exist in `canonical_vault/`
- ❌ No concept of "golden fixture"
- ❌ No byte-hash baseline
- ❌ No regression test suite using fixtures

### Downstream: Kit v3 CAREERS-171 Golden Fixture Workflow

**Phase 1: Establish Golden Fixture**
```bash
# Step 1: Extract CAREERS-171 from Linear
python scripts/kit_v3/extract_linear_issue.py \
  --issue CAREERS-171 \
  --output outcome_v3_injection_contract.json

# Step 2: Validate injection contract
python scripts/kit_v3/validate_injection_contract.py \
  outcome_v3_injection_contract.json

# Step 3: Inject into template (deterministic generation)
python scripts/kit_v3/inject_canonical_object.py \
  --contract outcome_v3_injection_contract.json \
  --template templates/outcome_v3_template.md \
  --output outcome_v3_object_model_definition.md

# Step 4: Calculate golden byte hash
python scripts/kit_v3/calculate_canonical_hash.py \
  outcome_v3_object_model_definition.md
# Output: sha256:abc123def456... (GOLDEN HASH)

# Step 5: Register golden hash
python scripts/kit_v3/register_golden_hash.py \
  --object-type Outcome \
  --version 3.0.0 \
  --hash sha256:abc123def456...

# Step 6: Validate reproducibility (run 3 times)
for i in {1..3}; do
  python scripts/kit_v3/inject_canonical_object.py \
    --contract outcome_v3_injection_contract.json \
    --template templates/outcome_v3_template.md \
    --output test_run_${i}.md
  
  python scripts/kit_v3/calculate_canonical_hash.py test_run_${i}.md
done
# All 3 hashes MUST match sha256:abc123def456...
```

**Phase 2: Use Golden Fixture for Validation**
```python
def test_outcome_v3_regeneration():
    """Regression test: Outcome v3 regenerates to golden hash."""
    
    # Load injection contract
    contract = load_injection_contract('outcome_v3_injection_contract.json')
    
    # Regenerate object
    generated = inject_canonical_object_deterministic(
        contract,
        Path('templates/outcome_v3_template.md')
    )
    
    # Write to temp file
    temp_file = Path('/tmp/outcome_v3_test.md')
    temp_file.write_text(generated)
    
    # Calculate hash
    actual_hash = calculate_canonical_hash(temp_file)
    
    # Validate against golden
    registry = GoldenHashRegistry('golden_hashes.json')
    result = registry.validate_against_golden('Outcome', '3.0.0', temp_file)
    
    assert result['valid'], f"Hash mismatch: {result['actual']} != {result['expected']}"
```

### GAP SUMMARY - Golden Fixture Workflow

| Component | Upstream | Downstream | Gap Status |
|-----------|----------|------------|------------|
| **Golden Fixture Concept** | ❌ Not defined | ❌ Must establish | 🔥 P0 GAP |
| **CAREERS-171 Extraction** | ❌ N/A | ❌ Must build | 🔥 P0 GAP |
| **Reproducibility Test** | ❌ No test | ❌ Must build | 🔥 P0 GAP |
| **Hash Registry** | ❌ No registry | ❌ Must build | 🔥 P0 GAP |
| **Regression Suite** | ❌ No fixtures | ❌ Must build | 🟡 P1 GAP |

---

## 9. All-8-Objects Promotion Plan

### Staged Rollout Strategy

**Phase 1: Golden Fixture (Week 1)**
```
CAREERS-171 → Outcome v3 → Golden Hash Established

Success Criteria:
✅ Byte hash reproducible across 3 runs
✅ Structural hash stable
✅ BDD projection generates valid .feature
✅ Evidence coverage 100% (14/14 attributes)
✅ ORCA meta-metadata complete
✅ No forbidden vocabulary
```

**Phase 2: Core Trio (Week 2-3)**
```
User Object → user_v3:sha256:...
Skill Object → skill_v3:sha256:...
Requirement Object → requirement_v3:sha256:...

Success Criteria (per object):
✅ Golden hash established
✅ Templates reusable from Outcome v3
✅ Validation gates all pass
✅ Evidence attribution complete
```

**Phase 3: Credential Group (Week 4)**
```
Credential Object → credential_v3:sha256:...
Qualification Object → qualification_v3:sha256:...
Standard Object → standard_v3:sha256:...

Success Criteria (per object):
✅ Junction pattern validation (if applicable)
✅ Relationship tracking working
✅ Cross-object references resolve
```

**Phase 4: Fit Object (Week 5)**
```
Fit Object → fit_v3:sha256:...

Success Criteria:
✅ All 8 objects have stable golden hashes
✅ Cross-object evidence references resolve
✅ ORCA relationship graph complete
✅ BDD projections for all 8 generate cleanly
```

### Parallel vs Sequential Decisions

**Parallel Processing** (can run concurrently):
- Phase 2 Core Trio (User, Skill, Requirement) - no dependencies
- Template creation for all 8 objects
- ORCA meta-metadata definition for all attributes

**Sequential Processing** (must complete in order):
- Phase 1 MUST complete before Phase 2 (golden fixture validates approach)
- Byte hash validation MUST work before structural hash
- Template injection MUST be deterministic before golden hash registration
- Evidence attribution MUST be complete before BDD generation

---

## 10. Risk Matrix & Mitigation

### Critical Risks (🔥 P0)

| Risk | Impact | Probability | Mitigation |
|------|--------|-------------|------------|
| **Non-deterministic template rendering** | Byte hash never stable | High | Use Jinja2 with `trim_blocks`, `lstrip_blocks`, sorted dicts |
| **Stale cached schema** | Generated artifacts based on old version | Medium | Add schema version alignment check in Stage 0 |
| **Hand-edited generated projections** | Traceability broken | High | Add watermarks, pre-commit hooks, projection validation |
| **Tuning bleed** | Corpus-specific patterns leak into canon | Medium | Forbidden vocabulary validator, separate extraction lens |
| **Validator tuned to corpus** | Overfitted to CAREERS-171 patterns | Medium | Validate against synthetic examples, not just fixtures |

### Moderate Risks (🟡 P1)

| Risk | Impact | Probability | Mitigation |
|------|--------|-------------|------------|
| **BDD projection drift** | Generated .feature doesn't match canon | Low | Stage 7 projection validator, watermark checks |
| **Evidence coverage gaps** | Some attributes lack evidence | Medium | Pre-promotion evidence audit, mandatory coverage threshold |
| **Cross-object reference breakage** | Evidence IDs don't resolve | Low | Cross-object integrity validator |
| **Template divergence** | 8 object templates drift apart | Medium | Shared template base, DRY principles |

---

## 11. Implementation Roadmap

### Week 1: Foundation (P0 Must-Haves)

**Day 1-2: Template System**
- [ ] Create `templates/outcome_v3_template.md` (Jinja2)
- [ ] Build `inject_canonical_object_deterministic()`
- [ ] Implement `deep_sort_dict()` for deterministic iteration
- [ ] Test: Same input → Same output (3 runs)

**Day 3-4: Hash System**
- [ ] Build `calculate_canonical_hash()` (byte-level)
- [ ] Build `calculate_structural_hash()` (classification)
- [ ] Implement `GoldenHashRegistry` class
- [ ] Test: Hash stability across regenerations

**Day 5-7: Linear Integration**
- [ ] Build `extract_injection_contract_from_linear()`
- [ ] Extract CAREERS-171 → `outcome_v3_injection_contract.json`
- [ ] Validate injection contract structure
- [ ] Generate Outcome v3 → Calculate golden hash
- [ ] Register golden hash: `outcome_v3:sha256:...`

### Week 2: Validation Extensions (P0)

**Day 1-2: ORCA Validators**
- [ ] Build `validate_orca_metadata()` (Stage 2.5)
- [ ] Add ORCA fields to injection contract schema
- [ ] Test against Outcome v3 injection contract

**Day 3-4: Hash Validators**
- [ ] Build `validate_byte_hash()` (Stage 4.5)
- [ ] Build `validate_structural_hash()` (Stage 5.5)
- [ ] Integrate into `hitl_orchestrator.py`
- [ ] Test against Outcome v3 golden fixture

**Day 5-7: Routing Logic**
- [ ] Extend HITL routing for hash failures
- [ ] Add `hash_verification/` queue folder
- [ ] Update error logging for hash drift
- [ ] Test full pipeline: Linear → Golden Hash validation

### Week 3-5: All-8-Objects Promotion (P0)

**Week 3: Core Trio**
- [ ] User v3: template, injection, golden hash
- [ ] Skill v3: template, injection, golden hash
- [ ] Requirement v3: template, injection, golden hash

**Week 4: Credential Group**
- [ ] Credential v3: template, injection, golden hash
- [ ] Qualification v3: template, injection, golden hash
- [ ] Standard v3: template, injection, golden hash

**Week 5: Fit + Integration**
- [ ] Fit v3: template, injection, golden hash
- [ ] Cross-object evidence validation
- [ ] ORCA relationship graph validation
- [ ] Final integration tests

### Week 6: Quality Gates (P1)

**Day 1-3: Additional Validators**
- [ ] Build `validate_forbidden_vocabulary()` (Stage 8)
- [ ] Build `validate_bdd_projection()` (Stage 7)
- [ ] Add watermark system for generated projections
- [ ] Pre-commit hook for projection integrity

**Day 4-7: Regression Suite**
- [ ] Create regression test suite using all 8 golden fixtures
- [ ] Add CI/CD pipeline for regression tests
- [ ] Document validation rules and error codes
- [ ] Write operator runbook for HITL queue management

---

## 12. Success Metrics

### P0 Must-Pass Criteria (Launch Blockers)

| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| **Outcome v3 byte hash reproducibility** | 3/3 runs identical | TBD | ⏳ Pending |
| **All 8 objects have golden hashes** | 8/8 registered | TBD | ⏳ Pending |
| **Deterministic generation** | 100% stable | TBD | ⏳ Pending |
| **ORCA meta-metadata coverage** | 100% of attributes | TBD | ⏳ Pending |
| **Evidence attribution** | 100% of core attributes | TBD | ⏳ Pending |
| **6-stage validation pass rate** | 100% for golden fixtures | TBD | ⏳ Pending |

### P1 Quality Indicators (Post-Launch)

| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| **BDD projection validity** | 100% parse cleanly | TBD | ⏳ Pending |
| **Forbidden vocabulary violations** | 0 in canonical sections | TBD | ⏳ Pending |
| **Structural hash stability** | No drift across regenerations | TBD | ⏳ Pending |
| **Cross-object reference integrity** | 100% resolve | TBD | ⏳ Pending |
| **Regression test pass rate** | 100% with golden fixtures | TBD | ⏳ Pending |

---

## 13. Conclusion & Recommendations

### What We Can Reuse from Upstream (80% of Infrastructure)

✅ **Production-Ready Components**:
1. 6-stage validation pipeline structure (Stages 1-6)
2. DoclingDocument `table.data.grid` extraction pattern
3. HITL queue management and routing logic
4. Markdown-first template structure
5. Evidence object pattern (needs ORCA extensions)
6. BDD generator (Stage 5)
7. Prompt generator (Stage 6)

### What We Must Build from Scratch (20% Critical Gap)

🔥 **P0 Must-Haves Before Outcome v3 Golden Fixture**:
1. Linear → Injection Contract extractor (Stage 0)
2. Deterministic template injection system
3. Byte hash calculation and validation (Stage 4.5)
4. Structural hash calculation and validation (Stage 5.5)
5. Golden Hash Registry
6. ORCA meta-metadata validator (Stage 2.5)
7. Jinja2 template files (8 objects)

🟡 **P1 Should-Haves Before All-8-Objects Promotion**:
1. Forbidden vocabulary validator (Stage 8)
2. BDD projection validator (Stage 7)
3. Watermark system for generated projections
4. Regression test suite using golden fixtures
5. Enhanced HITL routing for hash failures

### Critical Success Factors

1. **Determinism is Non-Negotiable**: Same input ALWAYS produces same byte hash
2. **Semantic Tuning NEVER Alters Canon**: Extraction lens is separate from object schema
3. **Generated Projections Are Reproducible**: No hand-maintained copies, always regenerate from canonical source
4. **CAREERS-171 Is Fixture, Not Ruleset**: Fixtures are data inputs, not validation logic
5. **Evidence-Based Governance**: No self-confidence, mandatory attribution, synthetic flags when needed

### Recommended First Steps

1. **Week 1 Sprint**: Build deterministic template injection + byte hash validation
2. **Week 1 Milestone**: Outcome v3 golden hash established and reproducible
3. **Week 2 Checkpoint**: ORCA validators integrated, Outcome v3 passes all gates
4. **Week 3-5 Execution**: Roll out remaining 7 objects following golden fixture pattern
5. **Week 6 Hardening**: Add P1 validators, regression suite, documentation

---

**Gap Analysis Version**: 1.0  
**Last Updated**: 2026-05-27  
**Upstream Source**: dux-object-model-core (v9.6.1)  
**Downstream Target**: Kit v3 (HITL Skills - ORCA Attributes)  
**Primary Reviewer**: Architecture Review Board (ARB)  
**Next Review**: After Outcome v3 Golden Fixture Established

---

## Appendix A: Quick Reference - What to Copy vs Build

### ✅ Copy These Files As-Is

```
FROM: dux-object-model-core/
├── scripts/validation/hitl_pipeline/stage1_structure_validation.py
├── scripts/validation/hitl_pipeline/stage2_consistency_validation.py
├── scripts/validation/hitl_pipeline/stage5_bdd_generator.py
├── scripts/validation/hitl_pipeline/stage6_prompt_generator.py
├── scripts/docling/fixed_docling_parser.py
├── docs/100_START_HERE/hitl_feature_template.md
└── canonical_vault/dux-core/*.md (as reference examples)

TO: kit-v3-hitl-skills/
├── validation/stage1_structure_validation.py
├── validation/stage2_consistency_validation.py
├── validation/stage5_bdd_generator.py
├── validation/stage6_prompt_generator.py
├── extraction/docling_parser.py
├── templates/hitl_feature_template.md
└── examples/*.md
```

### 🔨 Build These New Components

```
kit-v3-hitl-skills/
├── extraction/
│   └── linear_to_injection_contract.py         # NEW: Extract CAREERS-171
├── injection/
│   ├── deterministic_injector.py               # NEW: Jinja2 + sorted dicts
│   └── hash_calculator.py                      # NEW: Byte + structural hash
├── validation/
│   ├── stage0_linear_extraction.py             # NEW: Pre-validation
│   ├── stage2_5_orca_metadata_validation.py    # NEW: ORCA checks
│   ├── stage3_5_template_injection.py          # NEW: Deterministic gen
│   ├── stage4_5_byte_hash_validation.py        # NEW: Golden hash check
│   ├── stage5_5_structural_hash_validation.py  # NEW: Drift detection
│   ├── stage7_bdd_projection_validation.py     # NEW: Projection integrity
│   └── stage8_forbidden_vocabulary.py          # NEW: Corpus leak prevention
├── registry/
│   └── golden_hash_registry.py                 # NEW: Hash storage
└── templates/
    ├── outcome_v3_template.md                  # NEW: Jinja2 template
    ├── user_v3_template.md                     # NEW: Jinja2 template
    ├── skill_v3_template.md                    # NEW: Jinja2 template
    ├── requirement_v3_template.md              # NEW: Jinja2 template
    ├── credential_v3_template.md               # NEW: Jinja2 template
    ├── qualification_v3_template.md            # NEW: Jinja2 template
    ├── standard_v3_template.md                 # NEW: Jinja2 template
    └── fit_v3_template.md                      # NEW: Jinja2 template
```

### ❌ Explicitly Avoid These Patterns

```
DO NOT COPY:
- scripts/docling/parse_problem_object.py       # Broken regex parser
- Any hand-authored JSON schemas                 # Generated artifacts only
- Self-confidence scoring patterns               # Not evidence-based
- Corpus-specific schema fields                  # Canon is invariant
```

---

## Appendix B: CAREERS-171 Extraction Example

### Input: Linear Issue CAREERS-171

```markdown
# Outcome v3 Object Definition

## Purpose & Strategic Role
An Outcome object represents a validated achievement that proves a User has 
developed a Skill to meet a Requirement as measured against a Standard.

## What would you say you do here?
> When I need to validate that a data scientist can safely query production 
databases without manual credential management, I want evidence of successful 
autonomous access with full audit trail, so I can certify their security 
qualification with confidence.

## Why the Outcome Object Matters
- Provides evidence-based certification (not self-reported competency)
- Enables skill verification through observable signals
- Supports audit requirements for compliance
- Links user achievement to business-critical capabilities

## Schema Attributes
| Attribute | Type | Required | Description | ORCA Meta |
|-----------|------|----------|-------------|-----------|
| object_type | string | Yes | Must be "Outcome" | bucket:object, core:true |
| outcome_id | string | Yes | Unique identifier | bucket:attribute, core:true |
| outcome_statement | string | Yes | [Persona] is able to [task] | bucket:attribute, core:true, evidence:mandatory |
| user_id | string | Yes | Reference to User object | bucket:relationship, core:true |
| skill_id | string | Yes | Reference to Skill object | bucket:relationship, core:true |
| requirement_id | string | Yes | Reference to Requirement object | bucket:relationship, core:true |
| evidence | [object] | Yes | Array of evidence objects | bucket:attribute, core:true, evidence:mandatory |
| ... | ... | ... | ... | ... |

## Canonical Example
```json
{
  "object_type": "Outcome",
  "outcome_id": "outcome_careers_171_golden",
  "outcome_statement": "Data Scientist is able to query fraud database without handling credentials",
  "user_id": "user_sarah_ds",
  "skill_id": "skill_autonomous_db_access",
  "requirement_id": "req_secure_data_access",
  "evidence": [
    {
      "provenance_id": "EV-CAREERS-171-001",
      "supports_fields": ["outcome_statement"],
      "pull_quote": "Observed 47 successful database queries with zero manual credential handling"
    }
  ]
}
```
```

### Output: Injection Contract JSON

```json
{
  "object_type": "Outcome",
  "version": "3.0.0",
  "orca_buckets": {
    "objects": ["Outcome", "User", "Skill", "Requirement"],
    "relationships": [
      {"from": "User", "to": "Outcome", "via": "achieves"},
      {"from": "Outcome", "to": "Skill", "via": "demonstrates"},
      {"from": "Outcome", "to": "Requirement", "via": "satisfies"}
    ],
    "ctas": ["achieve", "validate", "evidence", "certify"],
    "attributes": [
      {
        "name": "outcome_statement",
        "type": "string",
        "required": true,
        "description": "[Persona] is able to [task]",
        "orca_meta": {
          "bucket": "attribute",
          "core_vs_supporting": "core",
          "evidence_requirement": "mandatory",
          "synthetic_allowed": false
        },
        "examples": [
          {
            "value": "Data Scientist is able to query fraud database without handling credentials",
            "source": "CAREERS-171",
            "context": "golden fixture"
          }
        ]
      }
      // ... more attributes
    ]
  },
  "evidence_coverage": {
    "total_attributes": 14,
    "evidence_backed": 14,
    "synthetic_acceptable": 0,
    "evidence_objects": ["EV-CAREERS-171-001", "EV-CAREERS-171-002"]
  },
  "hitl_review_metadata": {
    "reviewed_by": "case-arb-architect",
    "review_date": "2026-05-27",
    "pizza_score": 92,
    "linear_issue": "CAREERS-171"
  }
}
```

---

## Appendix C: NotebookLM Visualization Prompt

**Prompt for NotebookLM**:

> I'm providing two comprehensive analysis documents about the DUX Object Model Core repository and a gap analysis for Kit v3 downstream promotion:
>
> 1. `codebase_analysis.md` - Complete analysis of upstream patterns
> 2. `kit_v3_gap_analysis.md` - Gap analysis comparing upstream to downstream needs
>
> Please create visual representations showing:
>
> **Architecture Diagrams**:
> - Upstream 6-stage validation pipeline flow
> - Downstream 9-stage extended pipeline (with new stages highlighted)
> - HITL queue routing decision tree
> - Docling extraction pattern (table.data.grid breakthrough)
>
> **Gap Analysis Visuals**:
> - Heatmap: Green=Production Ready, Yellow=Needs Adaptation, Red=Must Build
> - Timeline: 6-week implementation roadmap with milestones
> - Risk matrix: Impact vs Probability for all identified risks
> - Success metrics dashboard: P0 must-pass criteria tracking
>
> **Data Tables**:
> - Component comparison table: Upstream vs Downstream (80/20 breakdown)
> - Validation rules matrix: What exists vs what's needed
> - All-8-objects promotion schedule
> - Golden fixture test results (when available)
>
> Please generate these visualizations in a format suitable for stakeholder review and architecture decision-making.

---

**End of Gap Analysis Report**
