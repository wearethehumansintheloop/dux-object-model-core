# HITL Development Pipeline Documentation

## Overview

The Human-in-the-Loop (HITL) development pipeline implements **markdown-as-source-code** philosophy for DUX schema governance. This system eliminates manual weekend schema checking across 100+ files by establishing markdown schemas as the canonical source with automated validation and propagation.

## Core Philosophy

- **Markdown schemas are canonical** (not JSON)
- **Natural language centricity** with JSON as backward compatibility
- **Agent prompts require .md format** for LLM processing
- **Four-stage validation** with manual control points
- **One object per folder** queue management logic

## Four-Stage Validation Pipeline

### Stage 1: Structure & Template Validation
**Script**: `scripts/validation/stage1_structure_validation.py`
**Purpose**: Validates markdown template structure (markdown-only)

**Validations**:
- Required sections present (Purpose & Strategic Role, Schema Attributes, etc.)
- Schema Attributes table structure
- Canonical Example JSON block exists
- Object type in title matches template

**Output**: Pass → Stage 2 | Fail → `hitl_failed/`

### Stage 2: Consistency Validation
**Script**: Integrated validation (no separate script found)
**Purpose**: Content consistency and quality checks (markdown-only)

**Validations**:
- Cross-reference validation
- Content quality metrics
- Structural integrity checks

**Output**: Pass → Stage 3a | Fail → `hitl_workshop/`

### Stage 3a: Lightweight Docling Integration
**Script**: `stage3a_problem_basic_docling.py` (referenced)
**Purpose**: Parse markdown into Docling document structure

**Process**:
- Efficient processing - no wasted cycles on bad markdown
- Parse markdown file into Docling DocumentConverter format
- Extract attribute table and embedded JSON schema
- Create Docling markdown object with embedded JSON

**Output**: Pass → Stage 3b | Fail → `hitl_workshop/`

### Stage 3b: Schema Generation & Validation
**Purpose**: Validate against canonical governance schema

**Process**:
- Validate Docling object against governance schema definition
- Check DUX object template structure compliance
- Ensure relationship fields present for cross-object references
- Natural language first validation with JSON backward compatibility

**Output**: Pass → Stage 4 | Fail → `hitl_workshop/`

### Stage 4: JSON Schema Validation & Queue Management
**Script**: `scripts/validation/validate_dux_objects.py`
**Purpose**: Production-ready validation with queue management

**Process**:
- Take promotion candidate in Docling markdown form
- Explode object into Docling objects for each attribute
- Validate against 'doclingified' canonical governance JSON schema
- Cut JSON files as required
- Manage queue system with auto-pull logic

**Queue Management Logic**:
```python
def pull_next_from_queue(processed_filename: str):
    # Determine object type from filename
    if "problem" in processed_filename.lower():
        queue_dir = Path("watch_folders/hitl_review_queue/problem_objects")
    elif "behavior" in processed_filename.lower():
        queue_dir = Path("watch_folders/hitl_review_queue/behavior_objects")
    # ... etc for each object type
    
    # Get oldest file from queue (by timestamp)
    queue_files = sorted(queue_dir.glob("*.md"))
    if queue_files:
        # Move to review folder with clean name
        # Auto-queue next object of same type
```

**Output**: Pass → `hitl_promotion_candidates/` | Fail → `hitl_failed/`

## Watch Folder Workflow

### Directory Structure
```
watch_folders/
├── hitl_review/                    # Current validation target (one object max)
├── hitl_review_queue/              # Queued objects by type
│   ├── problem_objects/
│   ├── behavior_objects/
│   ├── result_objects/
│   └── other_objects/
├── hitl_workshop/                  # LLM collaboration for improvements
├── hitl_failed/                    # Validation failures with error logs
├── hitl_promotion_candidates/      # Passed validation, awaiting approval
├── hitl_approved_for_production/   # Human-approved (NEVER automated)
└── hitl_rejected/                  # Human-rejected with reasons
```

### One Object Per Folder Logic

**Rule**: Review folder can only contain **one object of each type** at a time

**Implementation**:
1. When object completes validation (pass/fail), system checks queue
2. Auto-pulls oldest queued object of same type 
3. Prevents queue backup and ensures orderly processing
4. Timestamp-based FIFO ordering within type queues

### Queue Management Features

**Auto-Pull Trigger Points**:
- Object passes validation → move to promotion candidates → pull next
- Object fails validation → move to failed → pull next
- Human approval → move to approved → pull next

**Cleanup Logic**:
```python
def cleanup_old_failures(failed_dir: Path, current_filename: str):
    # Remove old failure files for same object type
    # Keep only latest failure per object type
    # Prevent accumulation of failed attempts
```

## Manual Control Points

### Stage 4 → Approved: NEVER Automated
**Reason**: Massive system impact requires human oversight
**Process**: 
- Promotion candidates await human review
- Manual approval required for production deployment
- Human can reject back to queue with feedback

### Human Review Criteria
- Content quality and strategic alignment
- Cross-object relationship validation
- Production readiness assessment
- System impact evaluation

## Integration with Schema Governance

### Canonical Source Flow
1. **Edit**: Markdown schemas in `src/dux_v9.6_split_schema/`
2. **Submit**: Copy to HITL review queue
3. **Validate**: 4-stage pipeline processing
4. **Approve**: Human validation for production
5. **Deploy**: Automated JSON generation and system updates

### Agent Prompt Integration
- All agent prompts consume markdown schemas
- Docling integration enables structured parsing
- Natural language priority with JSON fallback
- Global collaboration through plain language

## Discrete Validation Scripts

### Current Implementation
- **Stage 1**: `stage1_structure_validation.py` - Template validation
- **Stage 2**: Integrated (needs separate script)
- **Stage 3a**: `stage3a_problem_basic_docling.py` - Docling parsing  
- **Stage 4**: `validate_dux_objects.py` - Full validation + queue management

### Missing Components
- Standalone Stage 2 consistency validation script
- Stage 3b governance schema validation script
- Integration orchestrator for full pipeline

## Error Handling & Recovery

### Validation Failures
- Timestamped error logs with specific validation failures
- Automatic cleanup of old failures per object type
- Clear remediation guidance for resubmission

### Queue Recovery
- System maintains queue state across restarts
- Timestamp-based ordering ensures FIFO processing
- Manual queue manipulation possible for urgent changes

## Benefits of This System

### For Development Team
- Eliminates manual weekend schema checking
- Automated validation catches issues early
- Clear workflow for schema changes
- Natural language collaboration with global teams

### For System Integrity
- Four-stage validation ensures quality
- Manual approval prevents massive system changes
- Queue management prevents processing conflicts
- Complete audit trail for all changes

## Usage Examples

### Adding New Schema Field
1. Edit `problem_object.md` in canonical source
2. Copy to `hitl_review_queue/problem_objects/`
3. System auto-processes through 4 stages
4. Human approves for production deployment
5. Automated JSON generation and propagation

### Workflow Recovery
1. Check `hitl_failed/` for validation errors
2. Review error logs for specific issues
3. Fix markdown and resubmit to queue
4. System auto-processes corrected version

## Monitoring & Maintenance

### Key Metrics
- Queue depth by object type
- Validation failure rates by stage
- Time to approval for changes
- System propagation success rates

### Regular Tasks
- Monitor queue depths for bottlenecks
- Review failed validation patterns
- Update validation rules as schemas evolve
- Clean up old processed files

---

**Next Steps**: Reference this documentation in CLAUDE.md for DUX core platform team development workflow.