#!/usr/bin/env python3
"""
Debug the table structure to understand why we can't extract the Schema Attributes table
"""

from pathlib import Path
from docling.document_converter import DocumentConverter
import json

def deep_debug_table_structure():
    """Deep dive into the table structure."""
    
    file_path = Path("20250707_130903_problem_object_odi_update.md")
    
    print("🔍 Deep Debug: Table Structure Analysis")
    print("=" * 60)
    
    converter = DocumentConverter()
    result = converter.convert(file_path)
    doc = result.document
    
    print(f"📊 Found {len(doc.tables)} tables")
    
    for i, table in enumerate(doc.tables):
        print(f"\n📋 TABLE {i} DEEP ANALYSIS:")
        print(f"  Type: {type(table).__name__}")
        print(f"  Ref: {getattr(table, 'self_ref', 'No ref')}")
        
        # Examine all attributes of the table
        table_attrs = [attr for attr in dir(table) if not attr.startswith('_')]
        print(f"  Attributes: {table_attrs}")
        
        for attr in ['data', 'content', 'text', 'cells', 'rows']:
            if hasattr(table, attr):
                value = getattr(table, attr)
                print(f"  {attr}: {type(value)} = {str(value)[:200]}...")
                
                # If it's the data attribute, dive deeper
                if attr == 'data' and value:
                    print(f"    Data type: {type(value)}")
                    data_attrs = [a for a in dir(value) if not a.startswith('_')]
                    print(f"    Data attributes: {data_attrs}")
                    
                    # Check common data structures
                    for data_attr in ['table', 'rows', 'cells', 'grid', 'content']:
                        if hasattr(value, data_attr):
                            data_value = getattr(value, data_attr)
                            print(f"    {data_attr}: {type(data_value)} = {str(data_value)[:100]}...")
                            
                            # If this is the actual table data, dive even deeper
                            if data_attr == 'table' and data_value:
                                print(f"      Table type: {type(data_value)}")
                                table_attrs = [a for a in dir(data_value) if not a.startswith('_')]
                                print(f"      Table attributes: {table_attrs}")
                                
                                for table_attr in ['data', 'rows', 'cells']:
                                    if hasattr(data_value, table_attr):
                                        final_value = getattr(data_value, table_attr)
                                        print(f"      {table_attr}: {type(final_value)}")
                                        if hasattr(final_value, '__len__'):
                                            print(f"        Length: {len(final_value)}")
                                        if isinstance(final_value, (list, tuple)) and len(final_value) > 0:
                                            print(f"        First item: {final_value[0]}")
                                            print(f"        First item type: {type(final_value[0])}")
                                            if len(final_value) > 1:
                                                print(f"        Second item: {final_value[1]}")
    
    # Also check if we can export the table to different formats
    print(f"\n📄 DOCUMENT EXPORT OPTIONS:")
    try:
        # Try to get HTML to see table structure
        html_export = doc.export_to_html()
        print(f"  HTML export length: {len(html_export)}")
        
        # Look for table tags in HTML
        if '<table' in html_export.lower():
            print("  ✅ Found <table> tags in HTML export")
            # Extract just the table part
            import re
            table_matches = re.findall(r'<table.*?</table>', html_export, re.DOTALL | re.IGNORECASE)
            for j, table_html in enumerate(table_matches):
                print(f"  📋 Table {j} HTML: {table_html[:200]}...")
        else:
            print("  ❌ No <table> tags found in HTML export")
            
    except Exception as e:
        print(f"  ❌ HTML export error: {e}")
    
    try:
        # Try markdown export
        md_export = doc.export_to_markdown()
        print(f"  Markdown export length: {len(md_export)}")
        
        # Look for markdown table syntax
        if '|' in md_export:
            print("  ✅ Found pipe characters (possible table) in markdown export")
            # Extract lines with pipes
            lines_with_pipes = [line for line in md_export.split('\n') if '|' in line]
            print(f"  📋 Lines with pipes: {len(lines_with_pipes)}")
            for line in lines_with_pipes[:5]:  # First 5 lines
                print(f"    {line}")
        else:
            print("  ❌ No pipe characters found in markdown export")
            
    except Exception as e:
        print(f"  ❌ Markdown export error: {e}")

if __name__ == "__main__":
    deep_debug_table_structure()