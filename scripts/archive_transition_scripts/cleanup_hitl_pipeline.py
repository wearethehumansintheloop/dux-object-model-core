#!/usr/bin/env python3
"""
HITL Pipeline Cleanup Script

This script organizes and cleans up the HITL pipeline folders to restore proper operation.
It handles:
1. Moving experimental debug scripts to archive
2. Resolving duplicate object conflicts  
3. Clearing stuck queue items
4. Organizing validation results
"""

import shutil
from pathlib import Path
from datetime import datetime
import json

def create_cleanup_report():
    """Generate a cleanup report showing what will be cleaned."""
    
    base_path = Path("watch_folders")
    report = {
        "timestamp": datetime.now().isoformat(),
        "cleanup_actions": [],
        "file_counts": {},
        "conflicts": []
    }
    
    # Count files in each directory
    folders_to_check = [
        "hitl_workshop",
        "hitl_promotion_candidates", 
        "hitl_review_queue",
        "hitl_failed",
        "hitl_review",
        "hitl_archive"
    ]
    
    for folder in folders_to_check:
        folder_path = base_path / folder
        if folder_path.exists():
            md_files = list(folder_path.glob("*.md"))
            py_files = list(folder_path.glob("*.py"))
            json_files = list(folder_path.glob("*.json"))
            txt_files = list(folder_path.glob("*.txt"))
            
            report["file_counts"][folder] = {
                "markdown": len(md_files),
                "python": len(py_files), 
                "json": len(json_files),
                "text": len(txt_files),
                "total": len(md_files) + len(py_files) + len(json_files) + len(txt_files)
            }
    
    return report

def archive_workshop_debug_scripts():
    """Move experimental debug scripts to archive."""
    
    workshop_path = Path("watch_folders/hitl_workshop")
    archive_path = Path("watch_folders/hitl_archive/workshop_experiments")
    archive_path.mkdir(parents=True, exist_ok=True)
    
    # Scripts to archive (experimental/debug only)
    scripts_to_archive = [
        "debug_docling_md.py",
        "debug_table_structure.py", 
        "test_docling_config.py",
        "investigate_docling_document.py",
        "fixed_docling_parser.py"  # This was superseded by proper pipeline
    ]
    
    archived_files = []
    
    for script_name in scripts_to_archive:
        script_path = workshop_path / script_name
        if script_path.exists():
            # Create timestamped archive name
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            archive_name = f"{timestamp}_{script_name}"
            archive_file = archive_path / archive_name
            
            shutil.move(str(script_path), str(archive_file))
            archived_files.append(f"{script_name} -> {archive_name}")
    
    return archived_files

def resolve_duplicate_objects():
    """Resolve duplicate object conflicts in promotion candidates.
    
    Note: This handles canonical schema definitions, not sample instances.
    Sample instances should be processed through the pipeline normally.
    """
    
    candidates_path = Path("watch_folders/hitl_promotion_candidates")
    
    # Find canonical schema objects by type (these contain full schema definitions)
    problem_objects = list(candidates_path.glob("*problem_object*.md"))
    behavior_objects = list(candidates_path.glob("*behavior_object*.md"))
    result_objects = list(candidates_path.glob("*result_object*.md"))
    
    conflicts = []
    
    # Check for multiple objects of same type
    if len(problem_objects) > 1:
        conflicts.append({
            "type": "problem",
            "count": len(problem_objects),
            "files": [p.name for p in problem_objects]
        })
    
    if len(behavior_objects) > 1:
        conflicts.append({
            "type": "behavior", 
            "count": len(behavior_objects),
            "files": [b.name for b in behavior_objects]
        })
    
    if len(result_objects) > 1:
        conflicts.append({
            "type": "result",
            "count": len(result_objects), 
            "files": [r.name for r in result_objects]
        })
    
    return conflicts

def clear_stuck_queue_items():
    """Clear items stuck in review queue due to conflicts."""
    
    queue_path = Path("watch_folders/hitl_review_queue")
    archive_path = Path("watch_folders/hitl_archive/stuck_queue_items")
    archive_path.mkdir(parents=True, exist_ok=True)
    
    # Items with queue notes are stuck due to conflicts
    queue_notes = list(queue_path.glob("*_queue_note.txt"))
    stuck_objects = []
    
    for note_file in queue_notes:
        # Find corresponding object file
        base_name = note_file.name.replace("_queue_note.txt", "")
        object_file = queue_path / f"{base_name}.md"
        
        if object_file.exists():
            # Move both files to archive
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            
            archived_object = archive_path / f"{timestamp}_{object_file.name}"
            archived_note = archive_path / f"{timestamp}_{note_file.name}"
            
            shutil.move(str(object_file), str(archived_object))
            shutil.move(str(note_file), str(archived_note))
            
            stuck_objects.append({
                "original": object_file.name,
                "archived_as": archived_object.name,
                "note_archived_as": archived_note.name
            })
    
    return stuck_objects

def organize_validation_summaries():
    """Organize validation summary JSON files."""
    
    candidates_path = Path("watch_folders/hitl_promotion_candidates")
    summaries_path = Path("watch_folders/hitl_archive/validation_summaries")
    summaries_path.mkdir(parents=True, exist_ok=True)
    
    # Move validation summary JSON files to organized location
    summary_files = list(candidates_path.glob("*_validation_summary.json"))
    organized_summaries = []
    
    for summary_file in summary_files:
        # Keep summary with object but also create organized copy
        organized_copy = summaries_path / summary_file.name
        shutil.copy2(str(summary_file), str(organized_copy))
        organized_summaries.append(summary_file.name)
    
    return organized_summaries

def cleanup_docling_generated_files():
    """Clean up temporary docling-generated files."""
    
    workshop_path = Path("watch_folders/hitl_workshop")
    temp_files = []
    
    # Find docling temporary files
    docling_files = list(workshop_path.glob("*_docling.md"))
    docling_exports = list(workshop_path.glob("*_docling_export.json"))
    exploded_dirs = list(workshop_path.glob("*_exploded_attributes"))
    
    for file in docling_files + docling_exports:
        if file.exists():
            file.unlink()
            temp_files.append(file.name)
    
    for dir in exploded_dirs:
        if dir.exists():
            shutil.rmtree(str(dir))
            temp_files.append(f"{dir.name}/ (directory)")
    
    return temp_files

def relocate_extracted_sample_instances():
    """Identify and relocate extracted sample instances to proper validation flow.
    
    These are object instances extracted by the research platform that need
    validation against our schemas, then sent back to research platform.
    They don't belong in the HITL pipeline (which is for schema governance).
    """
    
    candidates_path = Path("watch_folders/hitl_promotion_candidates")
    queue_path = Path("watch_folders/hitl_review_queue")
    validation_path = Path("handoff-to-research-platform/extracted_instances_for_validation")
    validation_path.mkdir(parents=True, exist_ok=True)
    
    relocated_instances = []
    
    # Check both promotion candidates and review queue for sample instances
    all_md_files = list(candidates_path.glob("*.md")) + list(queue_path.glob("*.md"))
    
    for file_path in all_md_files:
        if file_path.name == "README.md":
            continue
            
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Identify sample instances by checking if they start with JSON
            # (extracted instances are typically JSON format, not schema definitions)
            is_sample_instance = (
                content.strip().startswith('```json') or 
                content.strip().startswith('{') or
                ('object_type' in content and 'Schema Attributes' not in content)
            )
            
            # Also check for platform engineer, developer, or other real scenario names
            # (these indicate extracted instances from real transcripts)
            contains_real_scenario = any(keyword in file_path.name.lower() for keyword in [
                'platform_engineer', 'developer', 'cigna', 'resource_request',
                'gpu_management', 'tcoa', 'efficiency'
            ])
            
            if is_sample_instance or contains_real_scenario:
                # This is an extracted sample instance, not a schema definition
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                new_name = f"{timestamp}_extracted_{file_path.name}"
                new_path = validation_path / new_name
                
                shutil.move(str(file_path), str(new_path))
                
                relocated_instances.append({
                    "original": file_path.name,
                    "relocated_to": new_name,
                    "reason": "extracted_sample_instance"
                })
                
        except Exception as e:
            print(f"  ⚠️ Error processing {file_path.name}: {e}")
    
    return relocated_instances

def identify_schema_vs_instance_conflicts():
    """Identify files that are schema definitions vs sample instances.
    
    This helps clarify what belongs in HITL pipeline (schemas) vs 
    research platform validation flow (extracted instances).
    """
    
    candidates_path = Path("watch_folders/hitl_promotion_candidates")
    analysis = {
        "schema_definitions": [],
        "sample_instances": [],
        "ambiguous": []
    }
    
    for file_path in candidates_path.glob("*.md"):
        if file_path.name == "README.md":
            continue
            
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Schema definitions have these characteristics
            has_schema_table = 'Schema Attributes' in content
            has_purpose_section = 'Purpose & Strategic Role' in content
            has_usage_notes = 'Usage Notes' in content
            has_canonical_example = 'Canonical Example' in content
            
            # Sample instances have these characteristics  
            starts_with_json = content.strip().startswith('```json') or content.strip().startswith('{')
            has_real_scenario_data = any(keyword in content.lower() for keyword in [
                'platform engineer', 'developer request', 'cigna', 'gpu management'
            ])
            
            if has_schema_table and has_purpose_section:
                analysis["schema_definitions"].append({
                    "file": file_path.name,
                    "confidence": "high",
                    "indicators": ["schema_table", "purpose_section"]
                })
            elif starts_with_json or has_real_scenario_data:
                analysis["sample_instances"].append({
                    "file": file_path.name,
                    "confidence": "high", 
                    "indicators": ["json_format", "real_scenario_data"]
                })
            else:
                analysis["ambiguous"].append({
                    "file": file_path.name,
                    "reason": "unclear_format"
                })
                
        except Exception as e:
            analysis["ambiguous"].append({
                "file": file_path.name,
                "reason": f"read_error: {e}"
            })
    
    return analysis

def main():
    """Run the complete cleanup process."""
    
    print("🧹 HITL Pipeline Cleanup")
    print("=" * 50)
    
    # Generate cleanup report
    print("📊 Generating cleanup report...")
    report = create_cleanup_report()
    
    print(f"\n📋 Current State:")
    for folder, counts in report["file_counts"].items():
        print(f"  {folder}: {counts['total']} files ({counts['markdown']} MD, {counts['python']} PY)")
    
    # Perform cleanup actions
    print(f"\n� Relocating extracted sample instances...")
    relocated_instances = relocate_extracted_sample_instances()
    for instance in relocated_instances:
        print(f"  ✅ Relocated: {instance['original']} -> handoff folder")
    
    print(f"\n🔍 Analyzing schema vs instance files...")
    analysis = identify_schema_vs_instance_conflicts()
    print(f"  📋 Schema definitions: {len(analysis['schema_definitions'])}")
    print(f"  📋 Sample instances: {len(analysis['sample_instances'])}")
    print(f"  📋 Ambiguous files: {len(analysis['ambiguous'])}")
    
    print(f"\n�🗂️  Archiving workshop debug scripts...")
    archived_scripts = archive_workshop_debug_scripts()
    for script in archived_scripts:
        print(f"  ✅ {script}")
    
    print(f"\n🔍 Checking for duplicate schema objects...")
    conflicts = resolve_duplicate_objects()
    if conflicts:
        print("  ⚠️  Found conflicts:")
        for conflict in conflicts:
            print(f"    {conflict['type']}: {conflict['count']} schema objects")
            for file in conflict['files']:
                print(f"      - {file}")
    else:
        print("  ✅ No schema conflicts found")
    
    print(f"\n🚫 Clearing stuck queue items...")
    stuck_items = clear_stuck_queue_items()
    for item in stuck_items:
        print(f"  ✅ Archived: {item['original']}")
    
    print(f"\n📋 Organizing validation summaries...")
    summaries = organize_validation_summaries()
    print(f"  ✅ Organized {len(summaries)} validation summaries")
    
    print(f"\n🧽 Cleaning temporary files...")
    temp_files = cleanup_docling_generated_files()
    for file in temp_files:
        print(f"  ✅ Removed: {file}")
    
    print(f"\n🔄 Relocating extracted sample instances...")
    relocated_instances = relocate_extracted_sample_instances()
    for instance in relocated_instances:
        print(f"  ✅ Relocated: {instance['original']} to {instance['relocated_to']}")
    
    # Save cleanup report
    report["cleanup_results"] = {
        "archived_scripts": len(archived_scripts),
        "conflicts_found": len(conflicts),
        "stuck_items_cleared": len(stuck_items),
        "summaries_organized": len(summaries),
        "temp_files_cleaned": len(temp_files),
        "relocated_instances": len(relocated_instances)
    }
    
    report_path = Path("watch_folders/hitl_archive/cleanup_reports")
    report_path.mkdir(parents=True, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_file = report_path / f"{timestamp}_cleanup_report.json"
    
    with open(report_file, 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"\n✅ Cleanup complete!")
    print(f"📄 Report saved: {report_file}")
    print(f"\n🎯 Next Steps:")
    print("  1. Review schema conflicts and decide which canonical definitions to keep")
    print("  2. Research platform should validate extracted instances from handoff folder") 
    print("  3. Run HITL pipeline to process schema governance items")
    print("  4. Check pipeline flows smoothly for schema validation workflow")

if __name__ == "__main__":
    main()
