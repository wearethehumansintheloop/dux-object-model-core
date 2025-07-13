"""
Behave environment setup for HITL pipeline tests
"""

import shutil
from pathlib import Path


def before_all(context):
    """Set up test environment before all tests."""
    # Ensure all required directories exist
    directories = [
        "watch_folders/hitl_review",
        "watch_folders/hitl_review_queue",
        "watch_folders/hitl_review_rejected",
        "watch_folders/hitl_rejected",
        "watch_folders/hitl_failed",
        "watch_folders/hitl_workshop",
        "watch_folders/hitl_promotion_candidates"
    ]
    
    for dir_path in directories:
        Path(dir_path).mkdir(parents=True, exist_ok=True)
    
    # Store paths in context for easy access
    context.hitl_paths = {
        'review': Path('watch_folders/hitl_review'),
        'queue': Path('watch_folders/hitl_review_queue'),
        'review_rejected': Path('watch_folders/hitl_review_rejected'),
        'rejected': Path('watch_folders/hitl_rejected'),
        'failed': Path('watch_folders/hitl_failed'),
        'workshop': Path('watch_folders/hitl_workshop'),
        'candidates': Path('watch_folders/hitl_promotion_candidates')
    }


def before_scenario(context, scenario):
    """Clean up before each scenario."""
    # Clean all test files from HITL folders
    for folder_name, folder_path in context.hitl_paths.items():
        if folder_path.exists():
            # Remove test files
            for pattern in ['test_*.md', '*_test_problem_*.md', '*.txt', '*.json']:
                for file in folder_path.glob(pattern):
                    if file.is_file():
                        file.unlink()
            
            # Remove test subdirectories
            for subdir in folder_path.iterdir():
                if subdir.is_dir() and 'test_' in subdir.name:
                    shutil.rmtree(subdir)


def after_scenario(context, scenario):
    """Clean up after scenario if needed."""
    # Could add screenshot or logging on failure
    if scenario.status == "failed":
        print(f"\n❌ Scenario failed: {scenario.name}")
        
        # Print orchestrator output for debugging
        if hasattr(context, 'orchestrator_output'):
            print("\nOrchestrator output:")
            print(context.orchestrator_output)
        
        if hasattr(context, 'orchestrator_errors'):
            print("\nOrchestrator errors:")
            print(context.orchestrator_errors)


def after_all(context):
    """Final cleanup after all tests."""
    # Optional: Archive test results or cleanup
    pass