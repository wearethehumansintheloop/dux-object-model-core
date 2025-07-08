1# CLAUDE.md - Research Platform Team Implementation Guide

This file provides guidance to Claude Code (claude.ai/code) when helping the Research Platform team implement features in `/dux-research-platform` that consume schemas and infrastructure from DUX Object Model Core.

## 🎯 The Opportunity: Leveraging Automated Schema Infrastructure

The Object Model Core has eliminated manual schema synchronization. Your platform can now consume validated schemas, auto-generated agents, and canonical examples to build robust extraction and synthesis pipelines.

## 🏗️ Architecture Overview: Research Platform Responsibilities

The Research Platform (`/dux-research-platform`) implements the operational side of DUX, consuming schemas from Object Model Core and providing services for research teams.

### What Object Model Core Provides (You Consume)
- **JSON Schemas**: Production-ready validation rules
- **Agent Prompts**: Auto-generated extraction agents
- **Canonical Examples**: Reference implementations
- **Validation Rules**: Programmatic object validation
- **Template Compliance**: Guaranteed structure

### What Research Platform Owns
- **Service Infrastructure**: Neo4j database, API (8504), Bot (8501), Loader (8502), CSV Bot (8506)
- **Instance Creation**: Extracting objects from research data using Core schemas
- **Relationship Logic**: DUX-opinionated object connections in Neo4j
- **magents.py**: Extraction orchestration in `genai-stack/`
- **Knowledge Graph**: Neo4j storage and querying
- **Analytics**: Cross-object pattern discovery and insights
- **LLM Integration**: Ollama, OpenAI, Claude model orchestration
- **RAG Pipeline**: Vector embeddings and semantic search

## 📦 Schema Consumption Interface

### 1. Schema Location & Structure
```python
# Schemas are in Object Model Core: ../dux-object-model-core/src/dux_v9.6_split_schema/
# Format: dux_object_{type}.json

# Example consumption in Research Platform:
import json
from pathlib import Path

def load_schema(object_type: str):
    # Path from Research Platform to Core schemas
    core_path = Path(__file__).parent.parent.parent / "dux-object-model-core"
    schema_path = core_path / f"src/dux_v9.6_split_schema/dux_object_{object_type.lower()}.json"
    with open(schema_path) as f:
        return json.load(f)

# Use in your extraction pipeline
problem_schema = load_schema("problem")
```

### 2. Schema Update Notifications
```python
# Watch for changes in:
# - watch_folders/hitl_approved_for_production/
# - src/dux_v9.6_split_schema/

# When schemas update:
# 1. Object Model Core runs update_schemas.py
# 2. New JSON schemas generated from markdown
# 3. Your platform should re-load schemas
# 4. Update extraction agents accordingly
```

## 🤖 Agent Prompt Integration

### 1. Auto-Generated Prompts Location
```
scripts/prompts_from_markdown/
├── problem_agent_prompt_canvas.md      # "Erin Brockovich of product strategy"
├── behavior_prompt.md                  # Behavior identification
├── result_prompt.md                    # Outcome extraction
├── useroutcome_prompt.md              # Goal synthesis
├── flow_prompt.md                     # Journey mapping
├── provenance_prompt.md               # Evidence extraction
└── insight_prompt.md                  # Pattern synthesis
```

### 2. Runtime Placeholder Injection
```python
# Each prompt has placeholders:
# {{source_text}} - Research artifact content
# {{existing_objects}} - Previously extracted objects

def prepare_agent_prompt(prompt_template: str, source_text: str, existing_objects: list):
    return prompt_template.replace("{{source_text}}", source_text)\
                         .replace("{{existing_objects}}", json.dumps(existing_objects))
```

### 3. Evidence Block Structure
```python
# Prompts expect evidence in this format:
evidence_block = {
    "teaser": "Summary of insight hook",
    "quote": "Direct user quote or paraphrase",
    "citation": "Participant 7, timestamp 00:12:45",
    "provenance_id": "prov_interview_001",
    "evidence_type": "user_research_finding"  # enum from prompt
}
```

## 🔄 Instance Creation Workflow

### 1. Extraction Pipeline
```python
# Your magents.py should:
def extract_dux_objects(source_content: str, object_type: str):
    # 1. Load schema for validation
    schema = load_schema(object_type)
    
    # 2. Load agent prompt
    prompt = load_agent_prompt(object_type)
    
    # 3. Get existing objects for context
    existing = get_existing_objects(object_type)
    
    # 4. Run extraction with LLM
    extracted = llm_extract(prompt, source_content, existing)
    
    # 5. Validate against schema
    validate_object(extracted, schema)
    
    # 6. Store in Neo4j
    store_object(extracted)
```

### 2. Relationship Population
```python
# DUX-opinionated relationships:
# Problem → UserOutcome (via useroutcome_ids)
# UserOutcome → Behavior + Result
# All objects → Provenance (via evidence array)

def populate_relationships(object_instance):
    # Connect to referenced objects
    for provenance_id in object_instance.get("evidence", []):
        create_evidence_relationship(object_instance["id"], provenance_id)
    
    # Type-specific relationships
    if object_instance["object_type"] == "Problem":
        for outcome_id in object_instance.get("useroutcome_ids", []):
            create_problem_outcome_relationship(object_instance["id"], outcome_id)
```

## 📊 Validation Feedback Loop

### 1. Report Extraction Failures
```python
# When instance validation fails:
def report_validation_failure(object_data, error, source_context):
    feedback = {
        "timestamp": datetime.now().isoformat(),
        "object_type": object_data.get("object_type"),
        "error": str(error),
        "source_context": source_context,
        "suggested_schema_change": analyze_failure_pattern(error)
    }
    
    # Log for Object Model Core team
    log_to_feedback_queue(feedback)
```

### 2. Pattern Discovery Reporting
```python
# When you discover new patterns:
def report_pattern_discovery(pattern_type, examples, frequency):
    discovery = {
        "pattern_type": pattern_type,
        "examples": examples,
        "frequency": frequency,
        "potential_schema_impact": assess_schema_impact(pattern_type),
        "timestamp": datetime.now().isoformat()
    }
    
    # Share with Object Model Core for schema evolution
    submit_pattern_discovery(discovery)
```

## 🔐 HITL Integration Points

### 1. Reading Approved Objects
```python
# Production-ready objects are in:
approved_dir = Path("watch_folders/hitl_approved_for_production/")

# Monitor for new approvals:
def watch_for_approved_objects():
    for obj_file in approved_dir.glob("*.md"):
        if is_new_or_updated(obj_file):
            process_approved_object(obj_file)
```

### 2. Training Data Management
```python
# Use canonical examples for training:
def get_training_examples(object_type):
    # 1. Load canonical example from schema
    schema = load_schema(object_type)
    canonical = schema.get("canonical_example")
    
    # 2. Get validated real examples
    validated = get_validated_instances(object_type)
    
    return canonical + validated
```

## 🌐 Natural Language Processing

### 1. Conversational Extraction
```python
# Implement natural language patterns:
def extract_with_context(text, cultural_context=None):
    # Use conversational prompts
    prompt = prepare_conversational_prompt(text)
    
    # Apply cultural adaptation if needed
    if cultural_context:
        prompt = adapt_for_culture(prompt, cultural_context)
    
    # Extract maintaining natural language
    return extract_naturally(prompt, text)
```

### 2. Global Scaling Considerations
```python
# Support multi-region deployment:
config = {
    "preserve_natural_language": True,
    "enable_cultural_adaptation": True,
    "support_async_collaboration": True,
    "timezone_resilient_storage": True
}
```

## 🔗 Evidence Chain Implementation

### 1. Provenance Integration
```python
# Every claim needs evidence:
def create_evidence_chain(claim, source_data):
    # 1. Extract provenance
    provenance = extract_provenance(source_data)
    
    # 2. Store provenance object
    prov_id = store_provenance(provenance)
    
    # 3. Link to claiming object
    claim["evidence"] = [prov_id]
    
    # 4. Calculate evidence maturity
    claim["evidence_maturity"] = calculate_maturity(provenance)
```

### 2. Audit Trail
```python
# Maintain research integrity:
def audit_extraction_process(source, extracted_objects):
    audit_entry = {
        "timestamp": datetime.now().isoformat(),
        "source": source,
        "extracted": [obj["id"] for obj in extracted_objects],
        "schema_versions": get_current_schema_versions(),
        "agent_versions": get_agent_prompt_versions()
    }
    store_audit_trail(audit_entry)
```

## 🚀 Migration Guide

### From Scattered to Centralized
```python
# Old way (avoid):
# - Prompts in multiple locations
# - Manual schema synchronization
# - Duplicate validation logic

# New way (implement):
# - Consume prompts from scripts/prompts_from_markdown/
# - Load schemas from src/dux_v9.6_split_schema/
# - Use Object Model Core validation
```

### Key Migration Steps
1. **Remove duplicate prompt management**
2. **Point to centralized schema location**
3. **Implement schema update watchers**
4. **Use canonical examples for training**
5. **Report failures back to Core team**

## 🎯 Implementation Checklist

- [ ] Schema consumption interface implemented
- [ ] Agent prompt integration complete
- [ ] Instance validation using Core schemas
- [ ] Relationship population logic built
- [ ] Feedback loop for schema improvements
- [ ] HITL integration for approved objects
- [ ] Natural language processing preserved
- [ ] Evidence chain implementation complete
- [ ] Audit trail for research integrity
- [ ] Migration from scattered systems done

## 📚 Key Infrastructure Benefits to Leverage

1. **No Manual Schema Sync** - Always get latest validated schemas
2. **Auto-Generated Agents** - Consistent extraction across studies
3. **Canonical Examples** - Training data included
4. **Validation Guaranteed** - Objects follow template
5. **Natural Language** - Global scaling built-in
6. **Evidence Traceability** - Research integrity maintained

## 🔧 Best Practices

### 1. Schema Consumption
- Cache schemas but watch for updates
- Validate early in extraction pipeline
- Use schema version in audit trails

### 2. Agent Usage
- Inject context appropriately
- Preserve natural language in outputs
- Update when schemas change

### 3. Feedback Loop
- Report all validation failures
- Share pattern discoveries
- Suggest schema enhancements

## 🆘 Collaboration Points

- **Schema questions?** → Object Model Core team
- **Extraction patterns?** → Share with Core for schema evolution
- **Validation failures?** → Report for schema refinement
- **New object types?** → Coordinate with Core team

## 🌟 The Promise Delivered

By leveraging this infrastructure, your platform gets:
- **Consistent extraction** across all research studies
- **Automatic schema updates** without manual sync
- **Research integrity** through evidence chains
- **Global scalability** through natural language
- **Reduced complexity** via centralized management

**Build on solid foundations - the infrastructure handles the complexity!**