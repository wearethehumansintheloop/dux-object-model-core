# Validation Structure (Consolidated)
    
This directory contains the consolidated validation structure for DUX Object Model Core.

## 📁 Structure Overview:

### Primary Location: `hitl_pipeline/`
- **HITL Orchestrator**: Complete pipeline workflow
- **Stage Scripts**: Structured validation stages (1, 2, 3a, 3b)
- **Object-Specific**: Behavior, Problem, Result validation stages
- **Integration**: Docling integration with structured table extraction

### Standalone Validators: `./` (this directory)
- **Individual Object Validators**: `validate_*_objects.py`
- **Bulk Operations**: `run_bulk_validation.py`
- **Configuration**: `config.py`

## 🎯 When to Use What:

- **HITL Pipeline**: For schema governance and object promotion workflow
- **Standalone Validators**: For quick individual object validation
- **Bulk Validation**: For validating multiple objects at once

## 📦 Archived:
- `archive_obsolete_duplicates/`: Obsolete duplicate files that were superseded

## 🚀 Primary Entry Points:
- HITL Workflow: `hitl_pipeline/hitl_orchestrator.py`
- Quick Validation: `validate_dux_objects.py`
- Bulk Operations: `run_bulk_validation.py`

Last consolidated: 2025-07-13 14:04:07