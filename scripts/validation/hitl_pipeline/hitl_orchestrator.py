#!/usr/bin/env python3
"""
HITL Pipeline Orchestrator
Manages the complete 4-stage validation pipeline with proper file routing

Pipeline Flow:
- Stage 1 Fail → hitl_failed/
- Stage 2 Fail → hitl_failed/  
- Stage 3a Fail → hitl_workshop/
- Stage 3b Fail → hitl_workshop/
- Stage 4 Pass → hitl_promotion_candidates/
- Stage 4 Fail → hitl_failed/
"""

import shutil
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, Optional

# Import stage validators
from stage1_structure_validation import validate_dux_template_structure
from stage2_consistency_validation import validate_consistency
from stage3a_problem_docling_md import process_problem_to_docling_md
from stage3b_problem_schema_validation import process_stage3b_validation


def check_naming_convention(file_path: Path) -> tuple[bool, str]:
    """
    Check if file follows naming conventions.
    
    Returns:
        (is_valid, object_type) tuple
    """
    filename = file_path.stem.lower()
    
    # Expected patterns from GOVERNANCE_NAMING_CONVENTIONS.md
    valid_object_types = ['behavior', 'flow', 'insight', 'problem', 'provenance', 'result', 'useroutcome']
    
    # Check if filename contains a valid object type
    for obj_type in valid_object_types:
        if obj_type in filename:
            return True, obj_type
    
    return False, ""


def move_to_rejected(file_path: Path, reason: str):
    """Move file to hitl_rejected for naming convention violations."""
    rejected_dir = Path("watch_folders/hitl_rejected")
    rejected_dir.mkdir(exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    rejected_filename = f"{timestamp}_{file_path.name}"
    rejected_path = rejected_dir / rejected_filename
    
    # Move file
    shutil.move(file_path, rejected_path)
    
    # Create rejection log
    rejection_log_path = rejected_dir / f"{timestamp}_{file_path.stem}_rejection.txt"
    with open(rejection_log_path, 'w') as f:
        f.write(f"HITL Rejection Report\n")
        f.write(f"====================\n\n")
        f.write(f"Timestamp: {datetime.now().isoformat()}\n")
        f.write(f"Original file: {file_path.name}\n")
        f.write(f"Rejection reason: {reason}\n")
        f.write(f"\nExpected naming patterns:\n")
        f.write(f"- File should contain one of: behavior, flow, insight, problem, provenance, result, useroutcome\n")
        f.write(f"- Example: 20250707_problem_object_description.md\n")
    
    print(f"  ❌ Rejected (naming): {rejected_path.name}")
    print(f"  📝 Rejection log: {rejection_log_path.name}")


def check_folder_constraints(target_dir: Path, object_type: str) -> tuple[bool, str]:
    """
    Check if folder already contains an object of the same type.
    
    Returns:
        (can_add, existing_file) tuple
    """
    if not target_dir.exists():
        return True, ""
    
    # Check for existing objects of same type
    existing_files = list(target_dir.glob("*.md"))
    for file in existing_files:
        if object_type in file.name.lower() and not file.name.endswith("_docling.md"):
            return False, file.name
    
    return True, ""


def move_to_failed(file_path: Path, stage: str, errors: list):
    """Move file to hitl_failed with error log."""
    failed_dir = Path("watch_folders/hitl_failed")
    failed_dir.mkdir(exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    failed_filename = f"{timestamp}_{file_path.name}"
    failed_path = failed_dir / failed_filename
    
    # Move file
    shutil.move(file_path, failed_path)
    
    # Create error log
    error_log_path = failed_dir / f"{timestamp}_{file_path.stem}_errors.txt"
    with open(error_log_path, 'w') as f:
        f.write(f"HITL Validation Failed at Stage: {stage}\n")
        f.write(f"Timestamp: {datetime.now().isoformat()}\n")
        f.write(f"Original file: {file_path.name}\n")
        f.write("\nErrors:\n")
        for error in errors:
            f.write(f"- {error}\n")
    
    print(f"  ❌ Moved to failed: {failed_path.name}")
    print(f"  📝 Error log: {error_log_path.name}")
    
    # Clean up any intermediate files
    cleanup_intermediate_files(file_path)


def move_to_workshop(file_path: Path, stage: str, errors: list, docling_path: Optional[Path] = None):
    """Move file to hitl_workshop for LLM collaboration."""
    workshop_dir = Path("watch_folders/hitl_workshop")
    workshop_dir.mkdir(exist_ok=True)
    
    # Check folder constraints
    _, object_type = check_naming_convention(file_path)
    can_add, existing_file = check_folder_constraints(workshop_dir, object_type)
    if not can_add:
        print(f"  ⚠️  Workshop already contains {object_type} object: {existing_file}")
        print(f"  ⚠️  Moving to rejected instead")
        move_to_rejected(file_path, f"Workshop folder already contains {object_type} object: {existing_file}")
        if docling_path and docling_path.exists():
            docling_path.unlink()
        return
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    workshop_filename = f"{timestamp}_{file_path.name}"
    workshop_path = workshop_dir / workshop_filename
    
    # Move original file
    shutil.move(file_path, workshop_path)
    
    # Move docling file if it exists
    if docling_path and docling_path.exists():
        docling_workshop_path = workshop_dir / f"{timestamp}_{docling_path.name}"
        shutil.move(docling_path, docling_workshop_path)
        print(f"  📄 Moved Docling: {docling_workshop_path.name}")
    
    # Create workshop notes
    notes_path = workshop_dir / f"{timestamp}_{file_path.stem}_workshop_notes.txt"
    with open(notes_path, 'w') as f:
        f.write(f"HITL Workshop Notes\n")
        f.write(f"==================\n\n")
        f.write(f"Failed at Stage: {stage}\n")
        f.write(f"Timestamp: {datetime.now().isoformat()}\n")
        f.write(f"Original file: {file_path.name}\n")
        f.write("\nIssues to Address:\n")
        for error in errors:
            f.write(f"- {error}\n")
        f.write("\nWorkshop Tasks:\n")
        if stage == "3a":
            f.write("- Fix markdown structure for Docling parsing\n")
            f.write("- Ensure Schema Attributes table is properly formatted\n")
        elif stage == "3b":
            f.write("- Update JSON schema generation to include nested structures\n")
            f.write("- Ensure evidence and opportunity_score have proper property definitions\n")
            f.write("- Consider if job_statement should be object with 3 components\n")
    
    print(f"  🔧 Moved to workshop: {workshop_path.name}")
    print(f"  📝 Workshop notes: {notes_path.name}")


def move_to_candidates(file_path: Path, validation_results: Dict[str, Any]):
    """Move validated file to promotion candidates."""
    candidates_dir = Path("watch_folders/hitl_promotion_candidates")
    candidates_dir.mkdir(exist_ok=True)
    
    # Check folder constraints
    _, object_type = check_naming_convention(file_path)
    can_add, existing_file = check_folder_constraints(candidates_dir, object_type)
    if not can_add:
        print(f"  ⚠️  Candidates already contains {object_type} object: {existing_file}")
        print(f"  ⚠️  Moving to rejected instead")
        move_to_rejected(file_path, f"Candidates folder already contains {object_type} object: {existing_file}")
        cleanup_intermediate_files(file_path)
        return
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    candidate_filename = f"{timestamp}_{file_path.name}"
    candidate_path = candidates_dir / candidate_filename
    
    # Move file
    shutil.move(file_path, candidate_path)
    
    # Create validation summary
    summary_path = candidates_dir / f"{timestamp}_{file_path.stem}_validation_summary.json"
    with open(summary_path, 'w') as f:
        import json
        json.dump({
            "file": file_path.name,
            "timestamp": datetime.now().isoformat(),
            "stages_passed": ["stage1", "stage2", "stage3a", "stage3b", "stage4"],
            "validation_results": validation_results
        }, f, indent=2)
    
    print(f"  ✅ Promoted to candidates: {candidate_path.name}")
    
    # Clean up intermediate files
    cleanup_intermediate_files(file_path)


def cleanup_intermediate_files(original_path: Path):
    """Clean up intermediate files like docling markdown."""
    # Remove docling file if exists
    docling_path = original_path.parent / f"{original_path.stem}_docling.md"
    if docling_path.exists():
        docling_path.unlink()
        print(f"  🗑️  Cleaned up: {docling_path.name}")


def run_stage1_validation(file_path: Path) -> Dict[str, Any]:
    """Run Stage 1 structure validation."""
    print(f"\n▶️  Stage 1: Structure Validation")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    errors = validate_dux_template_structure(content)
    
    if errors:
        print(f"  ❌ Stage 1 Failed: {len(errors)} errors")
        return {"passed": False, "errors": errors}
    
    print(f"  ✅ Stage 1 Passed")
    return {"passed": True, "errors": []}


def run_stage2_validation(file_path: Path) -> Dict[str, Any]:
    """Run Stage 2 consistency validation."""
    print(f"\n▶️  Stage 2: Consistency Validation")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    result = validate_consistency(content)
    
    if not result['valid']:
        print(f"  ❌ Stage 2 Failed: {len(result['errors'])} errors")
        return {"passed": False, "errors": result['errors']}
    
    print(f"  ✅ Stage 2 Passed")
    return {"passed": True, "errors": []}


def run_stage3a_validation(file_path: Path) -> Dict[str, Any]:
    """Run Stage 3a Docling conversion."""
    print(f"\n▶️  Stage 3a: Docling Markdown Conversion")
    
    result = process_problem_to_docling_md(file_path)
    
    if not result['success']:
        print(f"  ❌ Stage 3a Failed at: {result['stage']}")
        return {
            "passed": False, 
            "errors": result['errors'],
            "docling_path": None
        }
    
    print(f"  ✅ Stage 3a Passed")
    return {
        "passed": True, 
        "errors": [],
        "docling_path": Path(result['output_path'])
    }


def run_stage3b_validation(docling_path: Path) -> Dict[str, Any]:
    """Run Stage 3b schema validation."""
    print(f"\n▶️  Stage 3b: Schema Validation")
    
    result = process_stage3b_validation(docling_path)
    
    if not result['success']:
        print(f"  ❌ Stage 3b Failed at: {result['stage']}")
        return {"passed": False, "errors": result['errors']}
    
    print(f"  ✅ Stage 3b Passed")
    return {"passed": True, "errors": [], "json_schema": result['json_schema']}


def run_stage4_validation(file_path: Path, json_schema: Dict[str, Any]) -> Dict[str, Any]:
    """Run Stage 4 explosion and final validation."""
    print(f"\n▶️  Stage 4: Explosion & Final Validation")
    
    # For now, we'll import the existing validation
    sys.path.append(str(Path(__file__).parent.parent))
    from validate_dux_objects import process_markdown_file, validate_dux_object
    
    result = process_markdown_file(file_path)
    
    if not result['valid']:
        print(f"  ❌ Stage 4 Failed: {len(result['errors'])} errors")
        return {"passed": False, "errors": result['errors']}
    
    print(f"  ✅ Stage 4 Passed")
    return {"passed": True, "errors": [], "validation_result": result}


def process_problem_object(file_path: Path):
    """Process a Problem object through the complete HITL pipeline."""
    print(f"\n{'='*60}")
    print(f"🔄 HITL Pipeline: {file_path.name}")
    print(f"{'='*60}")
    
    # Check naming convention first
    is_valid_name, object_type = check_naming_convention(file_path)
    if not is_valid_name:
        move_to_rejected(file_path, "File name does not follow naming conventions")
        return
    
    print(f"  ✓ Naming convention valid (type: {object_type})")
    
    # Stage 1
    stage1_result = run_stage1_validation(file_path)
    if not stage1_result['passed']:
        move_to_failed(file_path, "Stage 1", stage1_result['errors'])
        return
    
    # Stage 2
    stage2_result = run_stage2_validation(file_path)
    if not stage2_result['passed']:
        move_to_failed(file_path, "Stage 2", stage2_result['errors'])
        return
    
    # Stage 3a
    stage3a_result = run_stage3a_validation(file_path)
    if not stage3a_result['passed']:
        move_to_workshop(file_path, "Stage 3a", stage3a_result['errors'])
        return
    
    docling_path = stage3a_result['docling_path']
    
    # Stage 3b
    stage3b_result = run_stage3b_validation(docling_path)
    if not stage3b_result['passed']:
        move_to_workshop(file_path, "Stage 3b", stage3b_result['errors'], docling_path)
        return
    
    # Stage 4
    stage4_result = run_stage4_validation(file_path, stage3b_result['json_schema'])
    if not stage4_result['passed']:
        move_to_failed(file_path, "Stage 4", stage4_result['errors'])
        cleanup_intermediate_files(file_path)
        return
    
    # All stages passed - move to candidates
    move_to_candidates(file_path, stage4_result['validation_result'])
    
    print(f"\n✅ Pipeline Complete: All stages passed!")


def main():
    """Run HITL pipeline orchestrator."""
    print("🚀 HITL Pipeline Orchestrator")
    print("=============================")
    
    if len(sys.argv) > 1:
        # Process specific file
        file_path = Path(sys.argv[1])
        if not file_path.exists():
            print(f"❌ File not found: {file_path}")
            return
        
        process_problem_object(file_path)
    
    else:
        # Process all Problem objects in review folder
        review_dir = Path("watch_folders/hitl_review")
        if not review_dir.exists():
            print(f"❌ Review directory not found: {review_dir}")
            return
        
        problem_files = [
            f for f in review_dir.glob("*.md") 
            if "problem" in f.name.lower() and not f.name.endswith("_docling.md")
        ]
        
        if not problem_files:
            print("📭 No Problem object files found in review")
            return
        
        for file_path in problem_files:
            process_problem_object(file_path)


if __name__ == "__main__":
    main()