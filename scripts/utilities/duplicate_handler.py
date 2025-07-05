#!/usr/bin/env python3
"""
Duplicate Handling Utilities for DUX Object Validation Scripts

This module provides shared functions for identifying and filtering duplicate objects
across all validation scripts, ensuring only the most recent version of each object
is processed.
"""

from pathlib import Path
from typing import List


def extract_object_id_from_filename(filename: str) -> str:
    """Extract object ID from filename pattern like '20250705_001358_user_outcome_object_model.md'."""
    # Remove timestamp prefix and file extension
    base_name = filename.replace('.md', '')
    
    # Extract the object identifier part (after timestamp)
    parts = base_name.split('_')
    if len(parts) >= 4:  # timestamp format: YYYYMMDD_HHMMSS
        # Skip timestamp parts and get the object identifier
        object_parts = parts[2:]  # Skip YYYYMMDD and HHMMSS
        return '_'.join(object_parts)
    
    return base_name


def get_timestamp_from_filename(filename: str) -> str:
    """Extract timestamp from filename pattern like '20250705_001358_user_outcome_object_model.md'."""
    parts = filename.split('_')
    if len(parts) >= 2:
        return f"{parts[0]}_{parts[1]}"  # YYYYMMDD_HHMMSS
    return ""


def filter_duplicate_files(files: List[Path]) -> List[Path]:
    """Filter out duplicate files, keeping only the most recent version of each object."""
    object_files = {}  # object_id -> (timestamp, file_path)
    
    for file_path in files:
        if not file_path.name.endswith('.md'):
            continue
            
        object_id = extract_object_id_from_filename(file_path.name)
        timestamp = get_timestamp_from_filename(file_path.name)
        
        if object_id in object_files:
            existing_timestamp, existing_file = object_files[object_id]
            # Keep the more recent timestamp
            if timestamp > existing_timestamp:
                object_files[object_id] = (timestamp, file_path)
        else:
            object_files[object_id] = (timestamp, file_path)
    
    # Return only the most recent file for each object
    return [file_path for timestamp, file_path in object_files.values()]


def get_duplicate_summary(files: List[Path]) -> str:
    """Generate a summary of duplicate filtering results."""
    all_markdown_files = [f for f in files if f.name.endswith('.md')]
    unique_files = filter_duplicate_files(all_markdown_files)
    
    total_files = len(all_markdown_files)
    unique_objects = len(unique_files)
    duplicates_removed = total_files - unique_objects
    
    if duplicates_removed > 0:
        return f"📁 Found {total_files} total files, processing {unique_objects} unique objects ({duplicates_removed} duplicates filtered)"
    else:
        return f"📁 Found {total_files} files, no duplicates detected" 