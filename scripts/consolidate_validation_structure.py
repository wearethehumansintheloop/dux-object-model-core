#!/usr/bin/env python3
"""
Validation Structure Consolidation Script

Consolidates the duplicated validation structure by:
1. Keeping /scripts/validation/hitl_pipeline/ as the primary location
2. Moving unique/useful files from /scripts/validation/ 
3. Archiving obsolete duplicate files
4. Creating a clean, single validation structure

This resolves the "no bueno" dual structure problem.
"""

import shutil
from pathlib import Path
from datetime import datetime
import json

def analyze_validation_structure():
    """Analyze what we have in each validation directory."""
    
    older_dir = Path("scripts/validation")
    newer_dir = Path("scripts/validation/hitl_pipeline")
    
    analysis = {
        "older_structure": {
            "path": str(older_dir),
            "files": [],
            "unique_files": [],
            "duplicates": []
        },
        "newer_structure": {
            "path": str(newer_dir), 
            "files": [],
            "unique_files": [],
            "duplicates": []
        },
        "consolidation_plan": []
    }
    
    # Get file lists
    older_files = [f.name for f in older_dir.glob("*.py") if f.is_file()]
    newer_files = [f.name for f in newer_dir.glob("*.py") if f.is_file()]
    
    analysis["older_structure"]["files"] = older_files
    analysis["newer_structure"]["files"] = newer_files
    
    # Identify duplicates and unique files
    for file in older_files:
        if file in newer_files:
            analysis["older_structure"]["duplicates"].append(file)
            analysis["newer_structure"]["duplicates"].append(file)
        else:
            analysis["older_structure"]["unique_files"].append(file)
    
    for file in newer_files:
        if file not in older_files:
            analysis["newer_structure"]["unique_files"].append(file)
    
    return analysis

def create_consolidation_plan():
    """Create a plan for consolidating the validation structures."""
    
    # Files to archive (older versions that are superseded)
    files_to_archive = [
        "stage1_structure_validation.py",      # Superseded by hitl_pipeline version
        "stage2_consistency_validation.py",    # Superseded by hitl_pipeline version  
        "stage3a_problem_basic_docling.py"     # Superseded by stage3a_problem_docling_md.py
    ]
    
    # Files to keep in older location (useful standalone validators)
    files_to_keep = [
        "validate_behavior_objects.py",        # Useful standalone validator
        "validate_dux_objects.py",            # Main validation entry point
        "validate_flow_objects.py",           # Useful standalone validator
        "validate_insight_objects.py",        # Useful standalone validator
        "validate_problem_objects.py",        # Useful standalone validator
        "validate_provenance_objects.py",     # Useful standalone validator
        "validate_result_objects.py",         # Useful standalone validator
        "validate_useroutcome_objects.py",    # Useful standalone validator
        "run_bulk_validation.py",             # Bulk validation utility
        "config.py"                           # Configuration file
    ]
    
    return {
        "primary_location": "scripts/validation/hitl_pipeline/",
        "archive_from_older": files_to_archive,
        "keep_in_older": files_to_keep,
        "strategy": "hitl_pipeline_primary_with_standalone_validators"
    }

def execute_consolidation():
    """Execute the consolidation plan."""
    
    print("🧹 Validation Structure Consolidation")
    print("=" * 60)
    
    # Analyze current structure
    analysis = analyze_validation_structure()
    plan = create_consolidation_plan()
    
    print(f"📊 Analysis:")
    print(f"  Older structure: {len(analysis['older_structure']['files'])} files")
    print(f"  Newer structure: {len(analysis['newer_structure']['files'])} files")
    print(f"  Duplicates: {len(analysis['older_structure']['duplicates'])} files")
    print(f"  Unique to older: {len(analysis['older_structure']['unique_files'])} files")
    print(f"  Unique to newer: {len(analysis['newer_structure']['unique_files'])} files")
    
    # Create archive directory
    archive_dir = Path("scripts/validation/archive_obsolete_duplicates")
    archive_dir.mkdir(exist_ok=True)
    
    # Archive obsolete duplicate files
    print(f"\\n📦 Archiving obsolete duplicate files...")
    archived_files = []
    
    for file_name in plan["archive_from_older"]:
        old_path = Path("scripts/validation") / file_name
        if old_path.exists():
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            archive_path = archive_dir / f"{timestamp}_{file_name}"
            
            shutil.move(str(old_path), str(archive_path))
            archived_files.append(f"{file_name} -> {archive_path.name}")
            print(f"  ✅ Archived: {file_name}")
    
    # Create README for the consolidated structure
    readme_content = """# Validation Structure (Consolidated)
    
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

Last consolidated: """ + datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    readme_path = Path("scripts/validation/README.md")
    with open(readme_path, 'w') as f:
        f.write(readme_content)
    
    # Generate consolidation report
    report = {
        "consolidation_timestamp": datetime.now().isoformat(),
        "strategy": plan["strategy"],
        "primary_location": plan["primary_location"],
        "archived_files": archived_files,
        "files_kept": plan["keep_in_older"],
        "analysis": analysis
    }
    
    report_path = archive_dir / f"{datetime.now().strftime('%Y%m%d_%H%M%S')}_consolidation_report.json"
    with open(report_path, 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"\\n✅ Consolidation Complete!")
    print(f"📄 README created: {readme_path}")
    print(f"📊 Report saved: {report_path}")
    print(f"📦 Archived {len(archived_files)} obsolete files")
    
    print(f"\\n🎯 New Structure:")
    print(f"  🔧 Primary: scripts/validation/hitl_pipeline/ (HITL workflow)")
    print(f"  🛠️  Standalone: scripts/validation/ (individual validators)")
    print(f"  📦 Archive: scripts/validation/archive_obsolete_duplicates/")
    
    return report

def main():
    """Run the consolidation."""
    
    # Execute consolidation
    report = execute_consolidation()
    
    print(f"\\n🎉 Validation structure consolidated successfully!")
    print(f"No more 'no bueno' dual structure - clean single hierarchy established.")

if __name__ == "__main__":
    main()
