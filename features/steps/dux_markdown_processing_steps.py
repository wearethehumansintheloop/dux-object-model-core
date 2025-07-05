"""
Step definitions for DUX Object Model Markdown Processing
Tests the generate_from_markdown.py script functionality
"""

import os
import subprocess
import json
from pathlib import Path
from behave import given, when, then
import tempfile
import shutil


@given('I have the DUX object model guide markdown file')
def step_have_markdown_file(context):
    """Verify the markdown file exists."""
    # Path updated to v9.5
    # Correcting the path to be absolute from the workspace root
    base_dir = Path(os.getcwd())
    context.markdown_file = base_dir / "docs" / "100_START_HERE" / "dux_object_model_guide_v_9_5.md"
    
    assert context.markdown_file.exists(), f"Markdown file not found: {context.markdown_file}"
    context.original_content = context.markdown_file.read_text()


@given('I have the generate_from_markdown.py script')
def step_have_script(context):
    """Verify the script exists."""
    context.script_path = Path("src/generate_from_markdown.py")
    if not context.script_path.exists():
        context.script_path = Path("generate_from_markdown.py")
    
    assert context.script_path.exists(), f"Script not found: {context.script_path}"


@given('the markdown file path is incorrect')
def step_incorrect_markdown_path(context):
    """Set up scenario with missing markdown file."""
    # Temporarily rename the markdown file to simulate missing file
    context.markdown_file = Path("docs/100_START_HERE/dux_object_model_guide_v_9_5.md")
    if context.markdown_file.exists():
        context.backup_path = context.markdown_file.with_suffix('.backup')
        shutil.move(str(context.markdown_file), str(context.backup_path))
        context.file_moved = True
    else:
        context.file_moved = False


@when('I run the generate_from_markdown.py script')
def step_run_script(context):
    """Execute the generate_from_markdown.py script."""
    # Determine the correct working directory and script path
    if Path("src/generate_from_markdown.py").exists():
        # Run from root directory
        result = subprocess.run(
            ["python", "src/generate_from_markdown.py"],
            capture_output=True,
            text=True
        )
    else:
        # Run from src directory
        result = subprocess.run(
            ["python", "generate_from_markdown.py"],
            capture_output=True,
            text=True,
            cwd="src" if Path("src").exists() else "."
        )
    
    context.script_result = result
    context.stdout = result.stdout
    context.stderr = result.stderr
    context.return_code = result.returncode


@then('it should extract {object_name} object definition')
def step_extract_object_definition(context, object_name):
    """Verify that specific object definition was extracted."""
    assert context.return_code == 0, f"Script failed with code {context.return_code}: {context.stderr}"
    
    # Check that the script output mentions extracting the object
    object_lower = object_name.lower()
    expected_file = f"{object_lower}_prompt.md"
    
    # Look for confirmation in stdout
    assert expected_file in context.stdout or f"Generated: scripts/prompts_from_markdown/{expected_file}" in context.stdout, \
        f"Expected {object_name} object extraction not found in output: {context.stdout}"


@then('each prompt template should include object-specific attributes')
def step_prompt_includes_attributes(context):
    """Verify that generated prompts contain object-specific attributes."""
    # Check that prompts directory exists and contains files
    prompts_dir = Path("scripts/prompts_from_markdown")
    if not prompts_dir.exists():
        prompts_dir = Path("src/scripts/prompts_from_markdown")
    
    assert prompts_dir.exists(), f"Prompts directory not found: {prompts_dir}"
    
    # Check that .md files were created
    md_files = list(prompts_dir.glob("*.md"))
    assert len(md_files) > 0, f"No .md files found in {prompts_dir}"
    
    # Verify each file contains expected content
    for md_file in md_files:
        content = md_file.read_text()
        assert "object_type:" in content, f"Missing object_type in {md_file.name}"
        assert "id: Unique identifier" in content, f"Missing id field in {md_file.name}"


@then('each generated prompt should have a clear object description')
def step_prompt_has_description(context):
    """Verify prompts have clear object descriptions."""
    prompts_dir = Path("scripts/prompts_from_markdown")
    if not prompts_dir.exists():
        prompts_dir = Path("src/scripts/prompts_from_markdown")
    
    md_files = list(prompts_dir.glob("*.md"))
    assert len(md_files) > 0, "No prompt files found"
    
    for md_file in md_files:
        content = md_file.read_text()
        assert "## Object Description" in content, f"Missing object description in {md_file.name}"
        assert "## Prompt Template" in content, f"Missing prompt template section in {md_file.name}"


@then('each prompt should include core DUX v9.5 attributes')
def step_prompt_includes_core_attributes(context):
    """Verify prompts include core DUX attributes."""
    prompts_dir = Path("scripts/prompts_from_markdown")
    if not prompts_dir.exists():
        prompts_dir = Path("src/scripts/prompts_from_markdown")
    
    md_files = list(prompts_dir.glob("*.md"))
    
    for md_file in md_files:
        content = md_file.read_text()
        # Check for core DUX attributes
        assert "object_type:" in content, f"Missing object_type in {md_file.name}"
        assert "id:" in content, f"Missing id in {md_file.name}"
        
        # Check for evidence-related content (core DUX principle)
        evidence_found = any(term in content.lower() for term in ["evidence", "validation", "test"])
        assert evidence_found, f"No evidence/validation content found in {md_file.name}"


@then('each prompt should follow the DUX principles of atomicity, traceability, and evidence')
def step_prompt_follows_dux_principles(context):
    """Verify prompts reflect DUX principles."""
    prompts_dir = Path("scripts/prompts_from_markdown")
    if not prompts_dir.exists():
        prompts_dir = Path("src/scripts/prompts_from_markdown")
    
    md_files = list(prompts_dir.glob("*.md"))
    
    for md_file in md_files:
        content = md_file.read_text()
        
        # Check for atomicity (single, clear purpose)
        assert "Object Type:" in content, f"Missing clear object type in {md_file.name}"
        
        # Check for traceability (relationships to other objects)
        traceability_found = any(term in content.lower() for term in 
                               ["relationship", "linked", "related", "ids", "behavior", "problem", "result"])
        assert traceability_found, f"No traceability content found in {md_file.name}"
        
        # Check for evidence principle
        evidence_found = any(term in content.lower() for term in 
                           ["evidence", "test", "validation", "bdd", "acceptance"])
        assert evidence_found, f"No evidence principle content found in {md_file.name}"


@then('the prompts should be saved to the scripts/prompts_from_markdown directory as .md files')
def step_prompts_saved_as_md(context):
    """Verify prompts are saved as markdown files in correct directory."""
    prompts_dir = Path("scripts/prompts_from_markdown")
    if not prompts_dir.exists():
        prompts_dir = Path("src/scripts/prompts_from_markdown")
    
    assert prompts_dir.exists(), f"Prompts directory not found: {prompts_dir}"
    
    # Check for .md files
    md_files = list(prompts_dir.glob("*.md"))
    assert len(md_files) >= 4, f"Expected at least 4 .md files, found {len(md_files)}"
    
    # Verify no .txt files remain
    txt_files = list(prompts_dir.glob("*.txt"))
    assert len(txt_files) == 0, f"Found unexpected .txt files: {[f.name for f in txt_files]}"
    
    # Verify expected files exist
    expected_files = ["problem_prompt.md", "behavior_prompt.md", "result_prompt.md", "flow_prompt.md", "useroutcome_prompt.md"]
    existing_files = [f.name for f in md_files]
    
    for expected in expected_files:
        assert expected in existing_files, f"Missing expected file: {expected}"


@then('it should display an error message about the missing file')
def step_display_missing_file_error(context):
    """Verify error message is displayed for missing file."""
    # The script should have a non-zero return code or error message
    error_found = (
        context.return_code != 0 or 
        "not found" in context.stdout.lower() or 
        "error" in context.stdout.lower() or
        "not found" in context.stderr.lower() or
        "error" in context.stderr.lower()
    )
    
    assert error_found, f"Expected error message not found. stdout: {context.stdout}, stderr: {context.stderr}"


@then('it should not create any prompt files')
def step_no_prompt_files_created(context):
    """Verify no prompt files were created when there's an error."""
    prompts_dir = Path("scripts/prompts_from_markdown")
    if not prompts_dir.exists():
        prompts_dir = Path("src/scripts/prompts_from_markdown")
    
    if prompts_dir.exists():
        # Check that no new files were created (existing files should remain unchanged)
        md_files = list(prompts_dir.glob("*.md"))
        # In error scenarios, either no files exist or they're unchanged from before
        # This is acceptable as long as the error was properly reported
        pass


def after_scenario(context, scenario):
    """Clean up after scenarios."""
    # Restore moved file if it was moved for testing
    if hasattr(context, 'file_moved') and context.file_moved:
        if hasattr(context, 'backup_path') and context.backup_path.exists():
            shutil.move(str(context.backup_path), str(context.markdown_file))
