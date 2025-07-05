#!/usr/bin/env python3
"""
Script to add duplicate handling to all validation scripts
"""

import os
import re
from pathlib import Path

def update_validation_script(script_path: Path):
    """Add duplicate handling imports and logic to a validation script."""
    print(f"Updating {script_path.name}...")
    
    # Read the script
    with open(script_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Add import if not already present
    if 'from duplicate_handler import' not in content:
        # Find the import section and add our import
        import_pattern = r'(from typing import.*?)(\n\n)'
        replacement = r'\1\nfrom duplicate_handler import filter_duplicate_files, get_duplicate_summary\2'
        content = re.sub(import_pattern, replacement, content, flags=re.DOTALL)
    
    # Update the main function to use duplicate filtering
    if 'all_markdown_files = list(review_dir.rglob("*.md"))' not in content:
        # Find the markdown files section
        files_pattern = r'(markdown_files = list\(review_dir\.rglob\("\.\*\.md"\)\)\n    if not markdown_files:\n        print\("📭 No markdown files found in review directory"\)\n        return\n    \n    print\(f"📁 Found \{len\(markdown_files\)\} markdown files"\))'
        replacement = '''all_markdown_files = list(review_dir.rglob("*.md"))
    if not all_markdown_files:
        print("📭 No markdown files found in review directory")
        return
    
    # Filter out duplicates, keeping only the most recent version of each object
    markdown_files = filter_duplicate_files(all_markdown_files)
    
    print(get_duplicate_summary(all_markdown_files))'''
        content = re.sub(files_pattern, replacement, content)
    
    # Write back the updated content
    with open(script_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ Updated {script_path.name}")

def main():
    """Update all validation scripts."""
    scripts_dir = Path(".")
    
    # Find all validation scripts
    validation_scripts = [
        f for f in scripts_dir.glob("validate_*.py") 
        if f.name != "validate_dux_objects.py"  # Skip the master script
    ]
    
    print(f"Found {len(validation_scripts)} validation scripts to update:")
    for script in validation_scripts:
        print(f"  - {script.name}")
    
    print("\nUpdating scripts...")
    for script in validation_scripts:
        update_validation_script(script)
    
    print("\n✅ All validation scripts updated with duplicate handling!")

if __name__ == "__main__":
    main() 