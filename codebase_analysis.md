# DUX Object Model Core - Comprehensive Codebase Analysis

**Generated**: 2026-05-27  
**Purpose**: Upstream architecture patterns for Kit v3 downstream promotion  
**Scope**: Object model governance, validation pipeline, template generation

---

## 1. Project Overview

### Project Type
**Object Model Governance Repository** - Defines and validates canonical schema definitions for the DUX (Declarative UX) framework.

### Core Mission
- Maintain canonical object model definitions as markdown source of truth
- Validate object structure through 6-stage HITL pipeline
- Generate JSON schemas, BDD features, and extraction prompts from canonical sources
- Enforce single-canonical-definition governance per object type

### Tech Stack
- **Language**: Python 3.12+
- **Core Libraries**: 
  - `docling` - Structured markdown parsing (table.data.grid breakthrough)
  - `jsonschema` - Schema validation
  - `behave` - BDD test framework
  - `jinja2` - Template rendering
- **Architecture**: Pipeline-based validation with HITL queue management

### Architecture Pattern
**Markdown-First Schema Governance** with deterministic generation:
```
Canonical .md → Docling Parse → Exploded Attributes → JSON Schema Generation → BDD Projection
```

---

## 2. Directory Structure Analysis

### `/canonical_vault/` - Canonical Object Definitions
**Purpose**: Single source of truth for all DUX object schemas

**Structure**:
```
canonical_vault/
├── dux-core/                    # Core HITL objects
│   ├── problem_object.md        # JTBD problem definition
│   ├── behavior_object.md       # Observable user actions
│   ├── result_object.md         # Business outcomes
│   ├── user_outcome_object.md   # Junction: behavior + result
│   ├── flow_object.md           # Sequential behavior chains
│   ├── evidence_object.md       # Research attribution
│   └── quality_assessment_object.md
├── dux-core-junctions/          # Many-to-many relationships
├── dux-research/                # Research object types
└── dux-research-junctions/
```

**Key Pattern**: Each object follows template structure:
1. 🎯 Purpose & Strategic Role (canonical)
2. 🧠 "What would you say you do here?" (JTBD statement)
3. 💡 Why the Object Matters (canonical bullets)
4. 📋 Schema Attributes (canonical table - byte-locked)
5. 📦 Canonical Example (canonical JSON - byte-locked)
6. 🔗 Structural Role & Usage Notes (canonical)

### `/scripts/validation/hitl_pipeline/` - 6-Stage Validation Pipeline
**Purpose**: Multi-stage validation with HITL queue routing

**Stages**:
```
Stage 1: Structure Validation (stage1_structure_validation.py)
  - Required sections present
  - Schema Attributes table structure
  - JSON block presence

Stage 2: Consistency Validation (stage2_consistency_validation.py)
  - Schema table ↔ JSON example consistency
  - Type compatibility
  - Required fields validation

Stage 3a: Docling Processing (stage3a_problem_docling_md.py)
  - DoclingDocument structured parsing
  - table.data.grid extraction (NOT regex)
  - Exploded attribute generation

Stage 3b: Schema Validation (stage3b_*_schema_validation.py)
  - Object-specific schema compliance
  - Type-specific validation rules

Stage 4: Object Instance Validation (stage4_object_validation.py)
  - Bespoke object validation per type
  - Routes to promotion_candidates/ or hitl_failed/

Stage 5: BDD Generator (stage5_bdd_generator.py)
  - Generates .feature files from canonical objects
  - YAML front matter with object graph
  - Gherkin scenarios from behaviors

Stage 6: Prompt Generator (stage6_prompt_generator.py)
  - Generates extraction prompts
  - Frame-aware agent instructions
  - Think-aloud protocol templates
```

**Orchestrator**: `hitl_orchestrator.py` coordinates all stages and HITL routing

### `/scripts/docling/` - Structured Parsing (BREAKTHROUGH)
**Purpose**: Extract schema tables from markdown using structured data

**Key File**: `fixed_docling_parser.py`
**Breakthrough Pattern**:
```python
# CORRECT: Use table.data.grid (structured data)
for table in doc.tables:
    if hasattr(table, 'data') and table.data and hasattr(table.data, 'grid'):
        grid = table.data.grid
        headers = [cell.text.strip() for cell in grid[0]]
        for row in grid[1:]:
            row_dict = {headers[j]: row[j].text.strip() for j in range(len(headers))}
            attributes.append(row_dict)
```

**Functions**:
- `explore_docling_structure()` - Analyzes document structure
- `extract_schema_table_from_docling()` - Extracts Schema Attributes table
- `generate_exploded_attribute_objects()` - Creates individual attribute objects

### `/watch_folders/` - HITL Queue Management
**Purpose**: Human-in-the-loop validation workflow routing

**Queue Structure**:
```
watch_folders/
├── hitl_review/              # Entry point (new objects)
├── hitl_review_queue/        # Queued by object type
│   ├── problem_objects/
│   ├── behavior_objects/
│   └── result_objects/
├── hitl_workshop/            # Objects needing fixes (refinement)
├── hitl_failed/              # Failed validation (major rework)
├── hitl_rejected/            # Wrong naming convention
├── hitl_promotion_candidates/ # Passed all stages
└── hitl_approved_for_production/ # Final canonical

```

**Naming Convention** (STRICT):
```
{object_type}_*_*_object_model_definition.md

✅ problem_cost_optimization_v1_object_model_definition.md
❌ problem_object.md (missing suffix)
```

### `/features/` - BDD Test Specifications
**Purpose**: Executable test scenarios using Behave framework

**Structure**:
```
features/
├── *.feature                    # Gherkin feature files
├── steps/                       # Python step definitions
│   ├── signal_flow_validation_steps.py
│   ├── useroutcome_derivation_validation_steps.py
│   ├── fit_template_magnet_steps.py
│   └── research_platform_validation_steps.py
└── environment.py
```

**Pattern**: Features carry full object graph in YAML front matter (see hitl_feature_template.md)

### `/docs/100_START_HERE/` - Core Documentation
**Purpose**: Canonical templates and validation guides

**Key Files**:
- `hitl_feature_template.md` - BDD feature file standard
- `evidence_object_defintion.md` - Evidence attribution pattern
- `natural_language_centricity_guide.md` - Philosophy

### `/test_data/` - Test Fixtures
**Purpose**: Synthetic and real data samples for validation

---

## 3. File-by-File Breakdown

### Core Validation Scripts

#### `hitl_orchestrator.py` (23KB)
**Purpose**: Main pipeline coordinator
**Functions**:
- Processes files through all 6 stages sequentially
- Routes failures to appropriate HITL queues
- Enforces single canonical definition rule
- Manages auto-pull from type-specific queues

**Key Logic**:
```python
def process_file(file_path):
    # Stage 1: Structure
    result1 = validate_structure(file_path)
    if not result1['valid']:
        route_to_hitl_failed(file_path, result1)
        return
    
    # Stage 2: Consistency
    result2 = validate_consistency(file_path)
    if not result2['valid']:
        route_to_hitl_workshop(file_path, result2)
        return
    
    # Stage 3a: Docling Parse
    result3 = parse_with_docling(file_path)
    if not result3['success']:
        route_to_hitl_failed(file_path, result3)
        return
    
    # Stages 4-6: Object validation, BDD generation, Prompt generation
    # ...
    
    # Success: Move to promotion candidates
    route_to_promotion_candidates(file_path)
```

#### `stage1_structure_validation.py` (6KB)
**Purpose**: Markdown template structure validation
**Validates**:
- Required sections present (6 canonical sections)
- Schema Attributes table structure
- JSON block presence in Canonical Example
- Object type in title

**Key Functions**:
- `validate_dux_template_structure()` - Main structure check
- `validate_schema_attributes_table()` - Table format validation
- `validate_canonical_example()` - JSON block validation

#### `stage2_consistency_validation.py` (9KB)
**Purpose**: Schema table ↔ JSON example consistency
**Validates**:
- Required fields in JSON match schema table
- No orphaned JSON fields
- Type compatibility between table and example

**Key Functions**:
- `extract_schema_attributes()` - Parse markdown table
- `extract_json_example()` - Parse JSON block
- `validate_schema_json_consistency()` - Cross-check logic
- `validate_type_compatibility()` - Type checking

#### `fixed_docling_parser.py` (14KB) - **CRITICAL BREAKTHROUGH**
**Purpose**: Structured markdown parsing using DoclingDocument
**Why Critical**: Replaces broken regex parsing with structured data access

**Key Discovery**:
```python
# Tables stored as table.data.grid, NOT as pages/elements
for table in doc.tables:
    grid = table.data.grid  # TableCell objects in 2D array
    headers = [cell.text.strip() for cell in grid[0]]
    for row in grid[1:]:
        attribute_data = {headers[j]: row[j].text for j in range(len(headers))}
```

**Functions**:
- `explore_docling_structure()` - Debug/analysis tool
- `extract_schema_table_from_docling()` - Main extraction
- `generate_exploded_attribute_objects()` - Create individual attribute files
- `save_exploded_objects()` - Write exploded outputs

**Output**: Individual JSON files per attribute (e.g., `job_statement_attribute.json`)

#### `stage5_bdd_generator.py` (15KB)
**Purpose**: Generate .feature files from canonical objects
**Generates**:
- YAML front matter with object graph
- Gherkin scenarios from Behavior objects
- Evidence attribution in comments
- Issue tracking placeholders

#### `stage6_prompt_generator.py` (7KB)
**Purpose**: Generate extraction prompts from canonical objects
**Generates**:
- Frame-aware agent instructions
- Think-aloud protocol templates
- Embedded JSON schemas for validation
- ORCA-compliant extraction guidance

### Configuration & Documentation

#### `CLAUDE.md` (Root)
**Purpose**: AI assistant guidance for repository
**Contains**:
- Commit message convention
- BDD test commands
- HITL pipeline workflow
- Object naming conventions
- Development principles

#### `docs/100_START_HERE/hitl_feature_template.md` (425 lines)
**Purpose**: Canonical BDD feature file template
**Defines**:
- YAML front matter structure (UserFlow, Problem, Result, UserOutcome, Behaviors)
- Gherkin scenario format
- Evidence attribution pattern
- Issue tracking integration (GitHub, Linear, Jira)
- Linter validation rules

**Key Pattern**: Feature file IS the PR body IS the issue IS the spec

---

## 4. Architecture Deep Dive

### Overall Application Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                   MARKDOWN-FIRST GOVERNANCE                  │
│              (Natural Language as Infrastructure)            │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  CANONICAL VAULT (Source of Truth)                          │
│  ├── problem_object.md (byte-locked canonical sections)     │
│  ├── behavior_object.md                                     │
│  └── result_object.md                                       │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  6-STAGE HITL VALIDATION PIPELINE                           │
│  ┌──────────────────────────────────────────────────────┐  │
│  │ Stage 1: Structure Validation (markdown only)        │  │
│  │   → Required sections, table format, JSON presence   │  │
│  └──────────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────────┐  │
│  │ Stage 2: Consistency Validation (markdown only)      │  │
│  │   → Schema ↔ JSON consistency, type checking         │  │
│  └──────────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────────┐  │
│  │ Stage 3a: Docling Processing (structured parse)      │  │
│  │   → table.data.grid extraction, exploded attributes  │  │
│  └──────────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────────┐  │
│  │ Stage 3b: Schema Validation (object-specific)        │  │
│  │   → Problem/Behavior/Result schema compliance        │  │
│  └──────────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────────┐  │
│  │ Stage 4: Object Instance Validation                  │  │
│  │   → Bespoke validation per object type               │  │
│  └──────────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────────┐  │
│  │ Stage 5: BDD Generator → .feature files              │  │
│  └──────────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────────┐  │
│  │ Stage 6: Prompt Generator → extraction prompts       │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                              │
              ┌───────────────┴───────────────┐
              ▼                               ▼
┌──────────────────────────┐   ┌──────────────────────────┐
│  HITL ROUTING            │   │  GENERATED ARTIFACTS     │
│  ├── promotion_candidates│   │  ├── *.json schemas      │
│  ├── hitl_workshop       │   │  ├── *.feature files     │
│  ├── hitl_failed         │   │  └── *_prompt.md         │
│  └── hitl_rejected       │   │                          │
└──────────────────────────┘   └──────────────────────────┘
```

### Data Flow & Request Lifecycle

**1. Object Submission Flow**:
```
Developer writes .md → hitl_review/ → hitl_orchestrator.py
  → Stage 1-6 sequential validation
  → Success: promotion_candidates/
  → Failure: hitl_failed/ or hitl_workshop/ (with error log)
```

**2. Docling Extraction Flow**:
```
Markdown file → DocumentConverter()
  → DoclingDocument object
  → doc.tables (TableItem objects)
  → table.data.grid (TableCell 2D array)
  → Extract headers from grid[0]
  → Extract rows from grid[1:]
  → Generate exploded attribute objects
  → Write individual JSON files
```

**3. BDD Generation Flow**:
```
Canonical object.md → Parse YAML front matter equivalent
  → Extract Behavior objects
  → Generate Gherkin scenarios
  → Inject evidence attribution
  → Write .feature file with object graph
```

### Key Design Patterns

**1. Single Canonical Definition Pattern**
- ONE object definition per type in system
- If promotion_candidates/ or approved_for_production/ has existing definition, reject new submission
- System boundary: Core defines schemas, Platform creates instances

**2. Markdown-First Schema Governance**
- Markdown `.md` files are canonical source
- JSON schemas are **generated artifacts** (not hand-maintained)
- Philosophy: Natural language as infrastructure-as-code

**3. Structured Data Extraction (Breakthrough)**
- Use DoclingDocument structured API (table.data.grid)
- NEVER fall back to regex parsing of exported text
- Structured access is deterministic and reliable

**4. HITL Queue Routing**
- Failure type determines queue destination:
  - Naming convention fail → `hitl_rejected/`
  - Structural fail → `hitl_failed/`
  - Refinement needed → `hitl_workshop/`
  - All stages passed → `promotion_candidates/`

**5. Evidence-Based Validation**
- Every claim requires evidence attribution
- No self-reported confidence scores
- Evidence objects with provenance tracking
- Quality scoring based on evidence completeness

**6. Deterministic Generation**
- All dict iterations use `sorted()`
- Template rendering with `trim_blocks=True, lstrip_blocks=True`
- Line endings normalized (always LF)
- Same input ALWAYS produces same byte hash

---

## 5. Environment & Setup Analysis

### Required Dependencies
From `requirements.txt`:
```
docling>=1.0.0         # Structured markdown parsing
behave>=1.2.6          # BDD testing framework
jsonschema>=4.17.0     # Schema validation
jinja2>=3.1.2          # Template rendering
neo4j>=5.12.0          # Graph database (downstream)
langchain>=0.1.0       # LLM integration (downstream)
```

### Installation & Setup Process
```bash
# 1. Clone repository
git clone <repo-url>
cd dux-object-model-core

# 2. Create virtual environment
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run BDD tests
behave features/

# 5. Run HITL validation pipeline
python scripts/validation/hitl_pipeline/hitl_orchestrator.py

# 6. Test individual stages
python scripts/validation/hitl_pipeline/stage1_structure_validation.py
```

### Development Workflow
```
1. Create/edit object definition in watch_folders/hitl_review/
2. Ensure naming convention: {object_type}_*_*_object_model_definition.md
3. Run validation pipeline: ./scripts/test_hitl_pipeline.sh
4. Review errors in hitl_failed/ error logs
5. Fix issues and resubmit
6. Object moves to promotion_candidates/ when all stages pass
7. Manual approval promotes to canonical_vault/
```

### Production Deployment Strategy
- **Git-based**: Canonical vault in git repository
- **Branch strategy**: Main branch = production canonical definitions
- **PR review**: All canonical changes via pull request
- **CI/CD**: Behave tests run on every PR
- **Downstream sync**: JSON schemas auto-generated on merge

---

## 6. Technology Stack Breakdown

### Core Technologies

| Component | Technology | Version | Purpose |
|-----------|-----------|---------|---------|
| **Runtime** | Python | 3.12+ | Core validation scripts |
| **Markdown Parser** | Docling | 1.0+ | Structured markdown extraction |
| **Schema Validator** | jsonschema | 4.17+ | JSON schema compliance |
| **BDD Framework** | Behave | 1.2.6+ | Gherkin test execution |
| **Template Engine** | Jinja2 | 3.1.2+ | Deterministic rendering |
| **Graph DB** | Neo4j | 5.12+ | Instance storage (downstream) |
| **LLM Framework** | LangChain | 0.1+ | Extraction agents (downstream) |

### Build & Validation Tools
- **Test Runner**: `behave` (BDD scenarios)
- **Linter**: Custom validators in Python
- **Hash Calculator**: `hashlib.sha256` (byte-level canonical hash)
- **Diff Calculator**: `hashlib.md5` (structural hash for classification)

### Deployment Technologies
- **Version Control**: Git
- **CI/CD**: Behave tests in pipeline
- **Artifact Generation**: Python scripts (deterministic)

---

## 7. Visual Architecture Diagram

### High-Level System Architecture

```
                    UPSTREAM: DUX Object Model Core
┌────────────────────────────────────────────────────────────────┐
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐  │
│  │         CANONICAL VAULT (Git Repository)                │  │
│  │  ┌───────────────┐  ┌───────────────┐  ┌─────────────┐ │  │
│  │  │ Problem.md    │  │ Behavior.md   │  │ Result.md   │ │  │
│  │  │ (v9.6.1)      │  │ (v9.6.1)      │  │ (v9.6.1)    │ │  │
│  │  │ BYTE-LOCKED   │  │ BYTE-LOCKED   │  │ BYTE-LOCKED │ │  │
│  │  └───────────────┘  └───────────────┘  └─────────────┘ │  │
│  └─────────────────────────────────────────────────────────┘  │
│                          │                                     │
│                          ▼                                     │
│  ┌─────────────────────────────────────────────────────────┐  │
│  │         HITL VALIDATION PIPELINE (6 Stages)             │  │
│  │                                                          │  │
│  │  Stage 1  │  Stage 2  │  Stage 3  │  Stage 4           │  │
│  │  Structure│Consistency│  Docling  │  Object            │  │
│  │  ─────────┼───────────┼───────────┼──────────          │  │
│  │  Sections │ Table ↔   │table.data.│ Bespoke            │  │
│  │  Tables   │ JSON      │   grid    │ Validator          │  │
│  │  JSON     │ Types     │ Explosion │ Per Type           │  │
│  │                                                          │  │
│  │  Stage 5           │  Stage 6                           │  │
│  │  BDD Generator     │  Prompt Generator                  │  │
│  │  ──────────────────┼─────────────────                  │  │
│  │  .feature files    │  *_prompt.md                       │  │
│  │  Gherkin scenarios │  Frame-aware agents                │  │
│  └─────────────────────────────────────────────────────────┘  │
│                          │                                     │
│              ┌───────────┴───────────┐                         │
│              ▼                       ▼                         │
│  ┌──────────────────┐   ┌──────────────────────────┐         │
│  │ HITL QUEUES      │   │ GENERATED ARTIFACTS       │         │
│  │ ────────────     │   │ ───────────────────       │         │
│  │ • review/        │   │ • *.json (schemas)        │         │
│  │ • workshop/      │   │ • *.feature (BDD)         │         │
│  │ • failed/        │   │ • *_prompt.md (extraction)│         │
│  │ • promotion/     │   │ • explosion_summary.json  │         │
│  └──────────────────┘   └──────────────────────────┘         │
│                                                                 │
└────────────────────────────────────────────────────────────────┘
                              │
                              │ Consumes schemas
                              │
                              ▼
┌────────────────────────────────────────────────────────────────┐
│               DOWNSTREAM: DUX Research Platform                 │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  Neo4j Graph Database                                    │  │
│  │  ───────────────────                                     │  │
│  │  • Problem instances (from research)                     │  │
│  │  • Behavior instances (from transcripts)                 │  │
│  │  • Result instances (from analysis)                      │  │
│  │  • Evidence relationships                                 │  │
│  └──────────────────────────────────────────────────────────┘  │
│                              │                                  │
│                              ▼                                  │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  LLM Extraction Agents (Llama/Claude)                    │  │
│  │  ────────────────────────────                            │  │
│  │  • Problem Extractor (Erin Brockovich)                   │  │
│  │  • Behavior Extractor (Columbo)                          │  │
│  │  • Result Extractor (Billy Beane)                        │  │
│  └──────────────────────────────────────────────────────────┘  │
└────────────────────────────────────────────────────────────────┘
```

### Component Relationships

```
┌────────────────────────────────────────────────────────────────┐
│                   FILE FLOW THROUGH PIPELINE                    │
└────────────────────────────────────────────────────────────────┘

  problem_cost_optimization_v1_object_model_definition.md
                      │
                      ▼
         [hitl_review/] (Entry Point)
                      │
                      ▼
         ┌────────────────────────┐
         │  hitl_orchestrator.py  │
         │  (Coordinator)         │
         └────────────────────────┘
                      │
          ┌───────────┴───────────┐
          │                       │
          ▼                       ▼
    ✅ PASS ALL              ❌ FAIL ANY
    STAGES 1-6               STAGE
          │                       │
          ▼                       ▼
[promotion_candidates/]    ┌──────────────┐
                           │  hitl_failed/│ (structural)
                           │  hitl_workshop/│ (refinement)
                           │  hitl_rejected/│ (naming)
                           └──────────────┘
```

### Data Flow: Markdown → Structured Data

```
┌─────────────────────────────────────────────────────────────┐
│  DOCLING STRUCTURED EXTRACTION (Breakthrough Pattern)       │
└─────────────────────────────────────────────────────────────┘

  problem_object.md (Markdown File)
          │
          ▼
  ┌──────────────────────┐
  │ DocumentConverter()  │  ← Docling library
  └──────────────────────┘
          │
          ▼
  ┌──────────────────────┐
  │  DoclingDocument     │
  │  ───────────────     │
  │  • doc.tables        │  ← TableItem objects
  │  • doc.texts         │  ← TextItem objects
  │  • doc.groups        │  ← ListGroup objects
  └──────────────────────┘
          │
          ▼
  ┌──────────────────────┐
  │ table.data.grid      │  ← 2D array of TableCell objects
  │ ─────────────────    │
  │ grid[0] = headers    │
  │ grid[1:] = data rows │
  └──────────────────────┘
          │
          ▼
  ┌──────────────────────────────────────┐
  │  Exploded Attribute Objects          │
  │  ──────────────────────────          │
  │  • job_statement_attribute.json      │
  │  • opportunity_score_attribute.json  │
  │  • evidence_attribute.json           │
  │  • end_user_attribute.json           │
  │  • what_is_at_stake_attribute.json   │
  │  ... (14 total for Problem object)   │
  └──────────────────────────────────────┘
```

---

## 8. Key Insights & Recommendations

### Strengths

✅ **Markdown-First Philosophy**
- Human-readable canonical definitions
- AI collaboration as first-class citizen
- Natural language as infrastructure-as-code

✅ **Structured Extraction Breakthrough**
- `table.data.grid` pattern eliminates regex fragility
- Deterministic and repeatable
- Structured data access vs text parsing

✅ **6-Stage Validation Pipeline**
- Clear separation of concerns
- Fail-fast with specific error messages
- HITL routing based on failure classification

✅ **Evidence-Based Governance**
- No self-reported confidence scores
- Mandatory evidence attribution
- Quality metrics tied to evidence completeness

✅ **Single Canonical Definition Rule**
- Prevents schema drift
- Clear source of truth
- System boundary enforcement (Core vs Platform)

### Areas for Enhancement

⚠️ **Missing: Byte Hash Validation**
Current implementation lacks:
- Canonical byte hash calculation
- Golden hash registry
- Drift detection on regeneration
- Deterministic template injection

**Recommendation**: Implement Section H tools from gap analysis:
```python
class GoldenHashRegistry:
    def register_golden_hash(object_type, version, byte_hash)
    def validate_against_golden(object_type, version, generated_file)
```

⚠️ **Missing: Template Scaffold System**
Current implementation lacks:
- Deterministic template injector
- Separation of canonical vs run-metadata sections
- Jinja2 templates with sorted dict iteration
- Hash-bearing section identification

**Recommendation**: Create `templates/` directory with reusable scaffolds

⚠️ **Missing: ORCA Meta-Metadata Validation**
Current implementation lacks:
- `bucket` validation (object, relationship, cta, attribute)
- `core_vs_supporting` classification
- `evidence_requirement` levels
- `synthetic_allowed` flags

**Recommendation**: Add ORCA validators to Stage 2 consistency checks

⚠️ **Missing: Forbidden Vocabulary Validator**
Current implementation lacks protection against:
- Corpus-specific tuning leaks (`optimized_for`, `tuned_for`)
- Self-confidence terms (`confidence`, `estimated`)
- Non-deterministic qualifiers (`approximately`)

**Recommendation**: Add vocabulary validator to Stage 1 structure checks

⚠️ **Incomplete: BDD Projection Validation**
Stage 5 generates .feature files but doesn't validate:
- Generated scenarios match ORCA CTAs
- Evidence IDs resolve to canonical evidence array
- Watermark integrity for generated projections

**Recommendation**: Add Stage 7: Projection Validation

### Security Considerations

🔒 **PII Handling**
- All research data with PII stays local (Neo4j local instance)
- No cloud sync for graph database
- Git repos with PII must be private
- Llama via Ollama for local-first extraction

🔒 **Canonical Integrity**
- Byte hash prevents tampering
- Git history provides audit trail
- PR review required for canonical changes
- Structural hash detects corruption

### Performance Optimization Opportunities

⚡ **Parallel Stage Execution**
Currently sequential; could parallelize:
- Stage 1 + Stage 2 (both markdown-only, no dependencies)
- Stage 5 + Stage 6 (both generation, independent outputs)

⚡ **Caching Docling Results**
- DoclingDocument parsing is expensive
- Cache parsed structure keyed by file hash
- Invalidate cache only when source .md changes

⚡ **Batch Processing**
- Process multiple files in hitl_review/ in batch
- Parallelize across object types
- Report aggregated results

### Maintainability Suggestions

📋 **Centralize Validation Rules**
- Extract magic strings to constants
- Create `validation_rules.py` module
- Version validation rules alongside object schemas

📋 **Add Regression Tests**
- Golden fixture test suite (Problem, Behavior, Result)
- Byte hash reproducibility tests
- Structural hash stability tests

📋 **Documentation Automation**
- Auto-generate validation rule docs from code
- Auto-generate architecture diagrams from pipeline stages
- Auto-generate CHANGELOG from git commits

---

## 9. Downstream Integration Points

### Kit v3 Promotion Requirements

Based on upstream analysis, Kit v3 downstream promotion needs:

**Required Upstream Patterns** (Copy These):
1. 6-stage validation pipeline structure
2. DoclingDocument `table.data.grid` extraction pattern
3. HITL queue routing logic
4. Markdown-first template structure
5. Evidence-based validation pattern

**Required New Tools** (Build These):
1. Byte hash registry (`GoldenHashRegistry`)
2. Deterministic template injector (`inject_canonical_object_deterministic`)
3. Linear → injection contract extractor (`extract_injection_contract_from_linear`)
4. ORCA meta-metadata validator
5. Forbidden vocabulary validator
6. BDD projection validator

**Avoided Patterns** (Don't Copy):
1. Manual regex parsing (use Docling structured API)
2. Self-confidence scoring
3. Corpus-specific schema fields
4. Monolithic object definitions

---

## 10. Conclusion

The DUX Object Model Core repository provides a solid foundation for markdown-first schema governance with a robust 6-stage validation pipeline. The **Docling breakthrough** (`table.data.grid` pattern) is production-ready and should be adopted by Kit v3 downstream.

**Critical Success Factors for Kit v3 Promotion**:
1. ✅ Adopt Docling structured extraction (NOT regex)
2. ✅ Implement byte hash + structural hash dual-gate system
3. ✅ Separate canonical sections from run metadata
4. ✅ Establish golden fixture workflow with CAREERS-171 Outcome v3
5. ✅ Build deterministic template injection pipeline
6. ✅ Add ORCA meta-metadata validation
7. ✅ Enforce forbidden vocabulary checks
8. ✅ Validate BDD projections against canonical source

**Next Steps**:
1. Review Section H code patterns from gap analysis
2. Create `templates/outcome_v3_template.md` scaffold
3. Extract CAREERS-171 Linear issue → injection contract JSON
4. Implement `GoldenHashRegistry` class
5. Run Outcome v3 through full validation pipeline
6. Establish golden hash for Outcome v3
7. Replicate for remaining 7 objects (User, Skill, Requirement, Credential, Qualification, Standard, Fit)

---

**Document Version**: 1.0  
**Last Updated**: 2026-05-27  
**Upstream Repository**: dux-object-model-core  
**Downstream Target**: Kit v3 (hitl-skills project)  
**Primary Contact**: Architecture Review Board (ARB)
