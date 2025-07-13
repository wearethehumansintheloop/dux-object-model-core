#!/usr/bin/env python3
"""
Manual test runner for HITL pipeline (when behave is not available)
"""

import sys
import shutil
import subprocess
from pathlib import Path
from datetime import datetime

# Add scripts to path
sys.path.append(str(Path(__file__).parent.parent / "scripts" / "validation" / "hitl_pipeline"))


def setup_test_folders():
    """Create and clean test folders."""
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
        Path(folder).mkdir(parents=True, exist_ok=True)
        # Clean existing test files
        folder_path = Path(folder)
        for file in folder_path.glob("test_*.md"):
            file.unlink()
        for file in folder_path.glob("*.txt"):
            file.unlink()
    
    print("✅ Test folders created and cleaned")


def test_reject_non_markdown():
    """Test: Reject non-markdown files"""
    print("\n🧪 Test 1: Reject non-markdown files")
    
    # Create a non-markdown file
    test_file = Path("watch_folders/hitl_review/test_file.txt")
    test_file.write_text("This is not a markdown file")
    
    # Run orchestrator
    result = subprocess.run(
        ["python3", "scripts/validation/hitl_pipeline/hitl_orchestrator.py", str(test_file)],
        capture_output=True,
        text=True
    )
    
    # Check results
    if "Only .md files are accepted" in result.stdout:
        print("  ✅ Non-markdown file correctly rejected")
    else:
        print("  ❌ Failed to reject non-markdown file")
        print(f"  Output: {result.stdout}")
    
    # Verify file moved to rejected
    if list(Path("watch_folders/hitl_rejected").glob("*test_file.txt")):
        print("  ✅ File moved to hitl_rejected")
    else:
        print("  ❌ File not found in hitl_rejected")


def test_invalid_naming():
    """Test: Reject files with invalid naming conventions"""
    print("\n🧪 Test 2: Reject invalid naming conventions")
    
    # Create file with invalid name
    test_file = Path("watch_folders/hitl_review/invalid-name-test.md")
    test_file.write_text("# Invalid Name Test")
    
    # Run orchestrator
    result = subprocess.run(
        ["python3", "scripts/validation/hitl_pipeline/hitl_orchestrator.py", str(test_file)],
        capture_output=True,
        text=True
    )
    
    # Check results
    if "File name does not follow naming conventions" in result.stdout:
        print("  ✅ Invalid name correctly rejected")
    else:
        print("  ❌ Failed to reject invalid name")
    
    # Verify file moved to rejected
    if list(Path("watch_folders/hitl_rejected").glob("*invalid-name-test.md")):
        print("  ✅ File moved to hitl_rejected")
    else:
        print("  ❌ File not found in hitl_rejected")


def test_stage1_failure():
    """Test: Stage 1 structure validation failure"""
    print("\n🧪 Test 3: Stage 1 structure validation failure")
    
    # Create invalid Problem object
    test_file = Path("watch_folders/hitl_review/test_problem_invalid.md")
    content = """# Problem Object

Missing required sections
"""
    test_file.write_text(content)
    
    # Run orchestrator
    result = subprocess.run(
        ["python3", "scripts/validation/hitl_pipeline/hitl_orchestrator.py", str(test_file)],
        capture_output=True,
        text=True
    )
    
    # Check results
    if "Stage 1 Failed" in result.stdout:
        print("  ✅ Stage 1 validation correctly failed")
    else:
        print("  ❌ Stage 1 should have failed")
        print(f"  Output: {result.stdout}")
    
    # Verify file moved to failed
    if list(Path("watch_folders/hitl_failed").glob("*test_problem_invalid.md")):
        print("  ✅ File moved to hitl_failed")
    else:
        print("  ❌ File not found in hitl_failed")


def test_successful_validation():
    """Test: Successful validation to promotion candidates"""
    print("\n🧪 Test 4: Successful validation")
    
    # Create valid Problem object with decomposed job_statement
    test_file = Path("watch_folders/hitl_review/test_problem_valid.md")
    content = """# 🧩 Problem Object

## 🎯 Purpose & Strategic Role
A Problem object represents a job to be done (JTBD) worth solving.

## 🧠 "What would you say... you do here?"
> When I need to test, I want validation, so I can ensure quality.

## 💡 Why the Problem Object Matters
- Frames opportunities at the right level
- Provides structure for scoring

## 📋 Schema Attributes
| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| object_type | string | Yes | Must be "Problem" |
| id | string | Yes | Unique identifier |
| job_statement | object | Yes | JTBD decomposed |
| evidence | [object] | Yes | Evidence array |

## 📦 Canonical Example (Schema-Compliant)
```json
{
  "object_type": "Problem",
  "id": "problem_001",
  "job_statement": {
    "user_scenario": "When testing",
    "user_enablement": "I want validation",
    "user_outcome": "so I can ensure quality"
  },
  "evidence": [
    {
      "provenance_id": "test_001",
      "supports_fields": ["job_statement"]
    }
  ]
}
```

## 🔗 Structural Role & Usage Notes
- Anchors strategic investment decisions
- Must be evidence-backed
"""
    test_file.write_text(content)
    
    # Run orchestrator
    result = subprocess.run(
        ["python3", "scripts/validation/hitl_pipeline/hitl_orchestrator.py", str(test_file)],
        capture_output=True,
        text=True
    )
    
    # Check results
    if "All stages passed" in result.stdout:
        print("  ✅ All validation stages passed")
    else:
        print("  ❌ Validation should have succeeded")
        print(f"  Output: {result.stdout}")
    
    # Verify file moved to candidates
    if list(Path("watch_folders/hitl_promotion_candidates").glob("*test_problem_valid.md")):
        print("  ✅ File moved to hitl_promotion_candidates")
    else:
        print("  ❌ File not found in hitl_promotion_candidates")


def test_one_object_per_folder():
    """Test: One object per folder constraint"""
    print("\n🧪 Test 5: One object per folder constraint")
    
    # First, place a problem object in workshop
    existing_file = Path("watch_folders/hitl_workshop/existing_problem_object.md")
    existing_file.write_text("# 🧩 Problem Object\n\nExisting object")
    
    # Create another problem object that will go to workshop
    test_file = Path("watch_folders/hitl_review/test_problem_duplicate.md")
    content = """# 🧩 Problem Object

## 🎯 Purpose & Strategic Role
Test purpose

## 🧠 "What would you say... you do here?"
> Test JTBD

## 💡 Why the Problem Object Matters
- Test

## 📋 Schema Attributes
| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| object_type | string | Yes | Must be "Problem" |
| id | string | Yes | Unique identifier |
| job_statement | string | Yes | JTBD statement |
| evidence | [object] | Yes | Evidence array |

## 📦 Canonical Example (Schema-Compliant)
```json
{
  "object_type": "Problem",
  "id": "problem_001",
  "job_statement": "Test statement",
  "evidence": [{"provenance_id": "test", "supports_fields": ["job_statement"]}]
}
```

## 🔗 Structural Role & Usage Notes
- Test
"""
    test_file.write_text(content)
    
    # Run orchestrator
    result = subprocess.run(
        ["python3", "scripts/validation/hitl_pipeline/hitl_orchestrator.py", str(test_file)],
        capture_output=True,
        text=True
    )
    
    # Check results
    if "Moving to review queue" in result.stdout and "Workshop already contains problem object" in result.stdout:
        print("  ✅ One-object-per-folder constraint enforced")
    else:
        print("  ❌ Should have enforced folder constraint")
        print(f"  Output: {result.stdout}")
    
    # Verify file moved to queue
    if list(Path("watch_folders/hitl_review_queue").glob("*test_problem_duplicate.md")):
        print("  ✅ File moved to hitl_review_queue")
    else:
        print("  ❌ File not found in hitl_review_queue")


def main():
    """Run all tests."""
    print("🚀 HITL Pipeline Manual Test Runner")
    print("=" * 50)
    
    # Setup
    setup_test_folders()
    
    # Run tests
    test_reject_non_markdown()
    test_invalid_naming()
    test_stage1_failure()
    test_successful_validation()
    test_one_object_per_folder()
    
    print("\n" + "=" * 50)
    print("✅ Test suite complete!")


if __name__ == "__main__":
    main()