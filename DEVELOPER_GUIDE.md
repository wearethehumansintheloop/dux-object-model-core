# DUX Object Model Core

## 🎯 Mission
The schema foundation and governance system for Declarative UX (DUX) - transforming UX research into executable, testable code through natural language object definitions.

## 🧬 Core Philosophy
**Markdown-first, natural language-centric development**. We believe schemas should be human-readable first, machine-parseable second. Every software artifact decomposes into three molecular components:
- **Problems** 🎯 - User needs and pain points worth solving
- **Behaviors** 🔷 - Atomic, testable user actions  
- **Results** 🟢 - Measurable outcomes and impacts

## 🚀 Quick Start

### For Schema Authors
1. Create your object definition in markdown following the [DUX object template](docs/100_START_HERE/dux_object_template.md)
2. Place it in `watch_folders/hitl_review/` with proper naming: `{object_type}_*_*_object_model_definition.md`
3. Run validation: `./scripts/test_hitl_pipeline.sh`
4. Monitor progress through the HITL pipeline stages

### For Developers
```bash
# Clone the repository
git clone [repository-url]
cd dux-object-model-core

# Install dependencies
pip install -r requirements.txt

# Run the test suite
behave features/

# Start HITL pipeline
python scripts/validation/hitl_pipeline/hitl_orchestrator.py
```

## 📁 Repository Structure

### Canonical Vault (`/canonical_vault/`)
The authoritative source for all DUX object definitions:
- `dux-core/` - Problem, Behavior, Result objects
- `dux-core-junctions/` - Flow, UserOutcome objects  
- `dux-research/` - Data, Frame, Session, Study objects
- `dux-research-junctions/` - Evidence, Insight, Provenance junctions

### HITL Pipeline (`/watch_folders/`)
Human-in-the-Loop validation workflow:
```
hitl_review/ → review_queue/ → workshop/ → validation → promotion_candidates/ → approved/
```

### Components (`/src/dux_component_definitions/`)
UI component specifications that "hire" DUX objects for display:
- Table rows, cards, detail pages
- Consulting slide templates
- API contracts for each view

### Scripts (`/scripts/`)
- `validation/` - 6-stage validation pipeline
- `generators/` - Schema and prompt generation
- `utilities/` - Helper scripts

## 🔄 Core Workflows

### 1. Object Definition Lifecycle
```mermaid
graph LR
    A[Markdown Definition] --> B[HITL Validation]
    B --> C[Schema Generation]
    C --> D[Prompt Generation]
    D --> E[BDD Tests]
    E --> F[Production]
```

### 2. Validation Pipeline Stages
1. **Structure Validation** - Markdown template compliance
2. **Consistency Check** - Content coherence  
3. **Docling Processing** - Parse to structured data
4. **Schema Generation** - Create JSON schemas
5. **Instance Validation** - Test with real data
6. **BDD Generation** - Create test scenarios

### 3. Component System
DUX objects "hire" components to display their data:
- **Browse**: Grid cards for discovery
- **Compare**: Table rows for prioritization
- **Analyze**: Detail pages that double as slides

## 🛠️ Key Technologies
- **Python 3.8+** - Core language
- **Behave** - BDD testing framework
- **Docling** - Markdown parsing
- **JSON Schema** - Validation framework

## 📚 Documentation
- [CLAUDE.md](CLAUDE.md) - AI assistant context
- [HITL Development Pipeline](HITL_DEVELOPMENT_PIPELINE.md) - Detailed workflow
- [Architecture Docs](docs/architecture/) - System design
- [Culture Guide](docs/98_culture/) - Team philosophy

## 🤝 Integration Points
This repository provides:
- **Schemas** → dux-research-platform
- **Validation** → duckie CLI  
- **Components** → dux-white-label-ui
- **Prompts** → AI extraction agents

## 🎯 Current Focus
- Generation-First HITL Pipeline implementation
- Component governance system expansion
- Prompt consolidation initiative
- Docling parser improvements

## 📏 Governance Rules
1. **One canonical definition** per object type
2. **Markdown is source code** - JSON is generated
3. **Strict naming convention** for pipeline entry
4. **Evidence-based validation** required
5. **Natural language first** - always

## 🚦 Status
- **Core Objects**: ✅ Problem, Behavior, Result
- **Junction Objects**: ✅ Flow, UserOutcome  
- **Research Objects**: ✅ Frame, Session, Study
- **Component System**: 🔄 In Progress
- **Full Automation**: 🔄 In Progress

## 🙏 Contributing
1. Follow the [culture guide](docs/98_culture/README.md)
2. Use the HITL pipeline for all changes
3. Write BDD tests for new features
4. Update documentation as you go

## 📝 License
[License details here]

## 🍺 The DUX Promise: Natty Lang
We're cracking open a cold one to the future of software. Just like PBR (Problem-Behavior-Result) is the champagne of beers, Natty Lang (natural language) is the champagne of programming languages. 

No more waiting for engineering to "groom your tickets." No more death by process. No more "but our methodology requires..." 

Ship it in 3 weeks or shut the dux up.

---
*"Natural language is the ultimate programming language. Tastes great, ships fast."* - DUX Team 🦆