#!/usr/bin/env python3
"""
Step definitions for HITL Pipeline BDD tests
"""

import json
import os
import shutil
import time
from datetime import datetime
from pathlib import Path
from behave import given, when, then
import subprocess


@given('the HITL folders exist')
def step_ensure_folders_exist(context):
    """Ensure all HITL folders exist."""
    for row in context.table:
        folder_path = Path(row['folder'])
        folder_path.mkdir(parents=True, exist_ok=True)
        assert folder_path.exists(), f"Failed to create {folder_path}"


@given('the folders are empty')
def step_clean_folders(context):
    """Clean all HITL folders."""
    folders = [
        "watch_folders/hitl_review",
        "watch_folders/hitl_review_queue", 
        "watch_folders/hitl_review_rejected",
        "watch_folders/hitl_rejected",
        "watch_folders/hitl_failed",
        "watch_folders/hitl_workshop",
        "watch_folders/hitl_promotion_candidates"
    ]
    
    for folder in folders:
        folder_path = Path(folder)
        if folder_path.exists():
            # Remove all files in the folder
            for file in folder_path.glob("*"):
                if file.is_file():
                    file.unlink()
                elif file.is_dir():
                    shutil.rmtree(file)


@given('a "{filename}" exists in {folder}')
def step_place_file_in_folder(context, filename, folder):
    """Place a file in a specific folder."""
    folder_path = Path(f"watch_folders/{folder}")
    file_path = folder_path / filename
    
    # Create a valid Problem object for testing
    content = """# 🧩 Problem Object

## 🎯 Purpose & Strategic Role
Test object

## 🧠 "What would you say... you do here?"
> Test JTBD

## 💡 Why the Problem Object Matters
- Test

## 📋 Schema Attributes
| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| object_type | string | Yes | Must be "Problem" |

## 📦 Canonical Example (Schema-Compliant)
```json
{"object_type": "Problem"}
```

## 🔗 Structural Role & Usage Notes
- Test
"""
    
    with open(file_path, 'w') as f:
        f.write(content)
    
    assert file_path.exists(), f"Failed to create {file_path}"


@when('I drop "{filename}" into {folder}')
def step_drop_file(context, filename, folder):
    """Drop a file into a folder."""
    folder_path = Path(f"watch_folders/{folder}")
    file_path = folder_path / filename
    
    # Create file with minimal content
    with open(file_path, 'w') as f:
        f.write("# Test file\n")
    
    # Store file path for later assertions
    context.test_file = file_path
    context.test_filename = filename
    
    # Run the orchestrator
    result = subprocess.run(
        ["python3", "scripts/validation/hitl_pipeline/hitl_orchestrator.py", str(file_path)],
        capture_output=True,
        text=True
    )
    
    context.orchestrator_output = result.stdout
    context.orchestrator_errors = result.stderr


@when('I drop a Problem object without required sections into {folder}')
def step_drop_invalid_problem(context, folder):
    """Drop an invalid Problem object."""
    folder_path = Path(f"watch_folders/{folder}")
    filename = f"test_problem_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
    file_path = folder_path / filename
    
    # Use the content from the feature file
    with open(file_path, 'w') as f:
        f.write(context.text)
    
    context.test_file = file_path
    context.test_filename = filename
    
    # Run the orchestrator
    result = subprocess.run(
        ["python3", "scripts/validation/hitl_pipeline/hitl_orchestrator.py", str(file_path)],
        capture_output=True,
        text=True
    )
    
    context.orchestrator_output = result.stdout
    context.orchestrator_errors = result.stderr


@when('I drop a Problem object with schema-JSON mismatch into {folder}')
def step_drop_problem_with_mismatch(context, folder):
    """Drop a Problem object with schema-JSON mismatch."""
    folder_path = Path(f"watch_folders/{folder}")
    filename = f"test_problem_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
    file_path = folder_path / filename
    
    with open(file_path, 'w') as f:
        f.write(context.text)
    
    context.test_file = file_path
    context.test_filename = filename
    
    # Run the orchestrator
    result = subprocess.run(
        ["python3", "scripts/validation/hitl_pipeline/hitl_orchestrator.py", str(file_path)],
        capture_output=True,
        text=True
    )
    
    context.orchestrator_output = result.stdout
    context.orchestrator_errors = result.stderr


@when('I drop a valid Problem object with string job_statement into {folder}')
def step_drop_problem_with_string_job(context, folder):
    """Drop a valid Problem object with string job_statement."""
    folder_path = Path(f"watch_folders/{folder}")
    filename = f"test_problem_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
    file_path = folder_path / filename
    
    with open(file_path, 'w') as f:
        f.write(context.text)
    
    context.test_file = file_path
    context.test_filename = filename
    
    # Run the orchestrator
    result = subprocess.run(
        ["python3", "scripts/validation/hitl_pipeline/hitl_orchestrator.py", str(file_path)],
        capture_output=True,
        text=True
    )
    
    context.orchestrator_output = result.stdout
    context.orchestrator_errors = result.stderr


@when('I drop a fully valid Problem object into {folder}')
def step_drop_valid_problem(context, folder):
    """Drop a fully valid Problem object."""
    folder_path = Path(f"watch_folders/{folder}")
    filename = f"test_problem_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
    file_path = folder_path / filename
    
    with open(file_path, 'w') as f:
        f.write(context.text)
    
    context.test_file = file_path
    context.test_filename = filename
    
    # Run the orchestrator
    result = subprocess.run(
        ["python3", "scripts/validation/hitl_pipeline/hitl_orchestrator.py", str(file_path)],
        capture_output=True,
        text=True
    )
    
    context.orchestrator_output = result.stdout
    context.orchestrator_errors = result.stderr


@when('the pipeline starts processing')
def step_pipeline_starts(context):
    """Pipeline already started in previous steps."""
    # Give pipeline time to move files
    time.sleep(0.5)


@when('the pipeline processes it through to Stage 3b failure')
def step_process_to_stage3b(context):
    """Process file knowing it will fail at Stage 3b."""
    # The orchestrator was already run in the drop step
    pass


@then('the file should be moved to {destination}')
def step_check_file_moved(context, destination):
    """Check if file was moved to destination folder."""
    dest_folder = Path(f"watch_folders/{destination}")
    
    # Look for the file in destination (may have timestamp prefix)
    found = False
    for file in dest_folder.glob("*.md"):
        if context.test_filename in file.name or file.stem.endswith(context.test_file.stem):
            found = True
            context.moved_file = file
            break
    
    assert found, f"File not found in {destination}. Files: {list(dest_folder.glob('*.md'))}"


@then('the file should not exist in {folder}')
def step_check_file_not_exists(context, folder):
    """Check that file doesn't exist in folder."""
    folder_path = Path(f"watch_folders/{folder}")
    file_path = folder_path / context.test_filename
    
    assert not file_path.exists(), f"File still exists in {folder}"


@then('the file should exist in one of the destination folders')
def step_check_file_in_any_destination(context):
    """Check that file exists in one of the destination folders."""
    destinations = [
        "hitl_rejected",
        "hitl_failed", 
        "hitl_workshop",
        "hitl_promotion_candidates",
        "hitl_review_queue"
    ]
    
    found = False
    for dest in destinations:
        dest_folder = Path(f"watch_folders/{dest}")
        for file in dest_folder.glob("*.md"):
            if context.test_filename in file.name or file.stem.endswith(context.test_file.stem):
                found = True
                break
        if found:
            break
    
    assert found, "File not found in any destination folder"


@then('the rejection reason should contain "{expected_text}"')
def step_check_rejection_reason(context, expected_text):
    """Check rejection log contains expected text."""
    rejected_dir = Path("watch_folders/hitl_rejected")
    
    # Find the rejection log
    log_files = list(rejected_dir.glob("*_rejection.txt"))
    assert len(log_files) > 0, "No rejection log found"
    
    # Check the most recent log
    latest_log = max(log_files, key=lambda p: p.stat().st_mtime)
    
    with open(latest_log, 'r') as f:
        content = f.read()
    
    assert expected_text in content, f"Expected '{expected_text}' not found in rejection log"


@then('the error log should contain "{expected_text}"')
def step_check_error_log(context, expected_text):
    """Check error log contains expected text."""
    failed_dir = Path("watch_folders/hitl_failed")
    
    # Find error logs
    log_files = list(failed_dir.glob("*_errors.txt"))
    assert len(log_files) > 0, "No error log found"
    
    # Check the most recent log
    latest_log = max(log_files, key=lambda p: p.stat().st_mtime)
    
    with open(latest_log, 'r') as f:
        content = f.read()
    
    assert expected_text in content, f"Expected '{expected_text}' not found in error log"


@then('the queue note should contain "{expected_text}"')
def step_check_queue_note(context, expected_text):
    """Check queue note contains expected text."""
    queue_dir = Path("watch_folders/hitl_review_queue")
    
    # Find queue notes
    note_files = list(queue_dir.glob("*_queue_note.txt"))
    assert len(note_files) > 0, "No queue note found"
    
    # Check the most recent note
    latest_note = max(note_files, key=lambda p: p.stat().st_mtime)
    
    with open(latest_note, 'r') as f:
        content = f.read()
    
    assert expected_text in content, f"Expected '{expected_text}' not found in queue note"


@then('the workshop notes should contain "{expected_text}"')
def step_check_workshop_notes(context, expected_text):
    """Check workshop notes contain expected text."""
    workshop_dir = Path("watch_folders/hitl_workshop")
    
    # Find workshop notes
    note_files = list(workshop_dir.glob("*_workshop_notes.txt"))
    assert len(note_files) > 0, "No workshop notes found"
    
    # Check the most recent note
    latest_note = max(note_files, key=lambda p: p.stat().st_mtime)
    
    with open(latest_note, 'r') as f:
        content = f.read()
    
    assert expected_text in content, f"Expected '{expected_text}' not found in workshop notes"


@then('the validation summary should show all stages passed')
def step_check_validation_summary(context):
    """Check validation summary shows all stages passed."""
    candidates_dir = Path("watch_folders/hitl_promotion_candidates")
    
    # Find validation summary
    summary_files = list(candidates_dir.glob("*_validation_summary.json"))
    assert len(summary_files) > 0, "No validation summary found"
    
    # Check the most recent summary
    latest_summary = max(summary_files, key=lambda p: p.stat().st_mtime)
    
    with open(latest_summary, 'r') as f:
        summary = json.load(f)
    
    expected_stages = ["stage1", "stage2", "stage3a", "stage3b", "stage4"]
    assert summary.get("stages_passed") == expected_stages, f"Not all stages passed: {summary.get('stages_passed')}"


@then('the pipeline should identify object type as "{expected_type}"')
def step_check_object_type(context, expected_type):
    """Check that pipeline correctly identified object type."""
    assert expected_type in context.orchestrator_output, f"Object type '{expected_type}' not found in output"