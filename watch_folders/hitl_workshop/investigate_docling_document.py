#!/usr/bin/env python3
"""
HITL Workshop: Investigate What DoclingDocument Actually Contains

This script reveals what the DoclingDocument object contains that we're currently ignoring
in parse_problem_object.py. We'll see the structured data that docling extracts.
"""

from pathlib import Path
from docling.document_converter import DocumentConverter
from docling.datamodel.base_models import InputFormat
import json

def investigate_docling_document(file_path: Path):
    """Investigate what DoclingDocument contains vs. current manual parsing."""
    
    print("🔍 HITL Workshop: DoclingDocument Investigation")
    print("=" * 60)
    print(f"📁 File: {file_path.name}")
    print()
    
    # Current approach (what parse_problem_object.py does)
    print("🚨 CURRENT APPROACH (what we're doing wrong):")
    converter = DocumentConverter()
    result = converter.convert(file_path)  # No InputFormat.MD specified!
    
    print(f"✅ DoclingDocument created: {type(result.document)}")
    print(f"📊 Document has {len(result.document.pages)} pages")
    print(f"🔤 Total elements across all pages: {sum(len(page.elements) for page in result.document.pages)}")
    print()
    
    # What we should be doing (docling auto-detects markdown format)
    print("✅ CORRECT APPROACH (what we should do):")
    converter_md = DocumentConverter()
    result_md = converter_md.convert(file_path)  # Docling auto-detects .md format
    
    print(f"✅ DoclingDocument with InputFormat.MD: {type(result_md.document)}")
    print(f"📊 Document has {len(result_md.document.pages)} pages")
    print(f"🔤 Total elements: {sum(len(page.elements) for page in result_md.document.pages)}")
    print()
    
    # Examine page elements in detail
    print("🔍 DOCLING DOCUMENT STRUCTURE ANALYSIS:")
    print("-" * 40)
    
    for page_num, page in enumerate(result_md.document.pages):
        print(f"📄 Page {page_num + 1}:")
        
        for i, element in enumerate(page.elements):
            element_type = type(element).__name__
            
            # Show element type and content preview
            if hasattr(element, 'text'):
                content_preview = element.text[:100] + "..." if len(element.text) > 100 else element.text
                print(f"  {i+1:2d}. {element_type:<20} | {content_preview}")
            else:
                print(f"  {i+1:2d}. {element_type:<20} | [No text content]")
            
            # Special handling for tables
            if 'table' in element_type.lower() or hasattr(element, 'data'):
                print(f"      🔍 TABLE FOUND! Type: {element_type}")
                if hasattr(element, 'data'):
                    print(f"      📊 Table data available: {type(element.data)}")
                    if hasattr(element.data, 'table'):
                        table = element.data.table
                        print(f"      📋 Rows: {len(table.data) if hasattr(table, 'data') else 'Unknown'}")
                        print(f"      📋 Headers: {table.data[0] if hasattr(table, 'data') and len(table.data) > 0 else 'Unknown'}")
            
            # Show first few elements only to avoid spam
            if i >= 10:
                remaining = len(page.elements) - i - 1
                if remaining > 0:
                    print(f"  ... and {remaining} more elements")
                break
        print()
    
    # Try to find schema attributes table specifically
    print("🎯 SCHEMA ATTRIBUTES TABLE SEARCH:")
    print("-" * 40)
    
    schema_table_found = False
    for page in result_md.document.pages:
        for element in page.elements:
            if hasattr(element, 'text') and 'schema attributes' in element.text.lower():
                print(f"📋 Found Schema Attributes section: {type(element).__name__}")
                print(f"📝 Content: {element.text[:200]}...")
                schema_table_found = True
            
            # Look for actual table elements near schema content
            if 'table' in type(element).__name__.lower():
                print(f"📊 Found table element: {type(element).__name__}")
                if hasattr(element, 'data') and hasattr(element.data, 'table'):
                    table = element.data.table
                    if hasattr(table, 'data') and len(table.data) > 0:
                        print(f"📋 Table preview: {table.data[0][:3] if len(table.data[0]) > 3 else table.data[0]}")
                        schema_table_found = True
    
    if not schema_table_found:
        print("❌ No schema attributes table found in structured DoclingDocument")
        print("💡 This explains why we fall back to manual regex parsing!")
    
    print()
    
    # Export document structure for inspection
    doc_export_path = file_path.parent / f"{file_path.stem}_docling_export.json"
    print(f"💾 Exporting DoclingDocument structure to: {doc_export_path.name}")
    
    # Create a simplified export of the document structure
    doc_structure = {
        'file_name': file_path.name,
        'pages': len(result_md.document.pages),
        'total_elements': sum(len(page.elements) for page in result_md.document.pages),
        'elements_by_type': {},
        'page_details': []
    }
    
    for page_num, page in enumerate(result_md.document.pages):
        page_detail = {
            'page_number': page_num + 1,
            'elements': []
        }
        
        for element in page.elements:
            element_type = type(element).__name__
            
            # Count element types
            if element_type not in doc_structure['elements_by_type']:
                doc_structure['elements_by_type'][element_type] = 0
            doc_structure['elements_by_type'][element_type] += 1
            
            # Add element details
            element_detail = {
                'type': element_type,
                'has_text': hasattr(element, 'text'),
                'is_table': 'table' in element_type.lower() or hasattr(element, 'data')
            }
            
            if hasattr(element, 'text'):
                element_detail['text_preview'] = element.text[:100]
            
            page_detail['elements'].append(element_detail)
        
        doc_structure['page_details'].append(page_detail)
    
    with open(doc_export_path, 'w') as f:
        json.dump(doc_structure, f, indent=2)
    
    print("✅ Export complete!")
    print()
    
    # Summary
    print("📋 INVESTIGATION SUMMARY:")
    print("-" * 40)
    print(f"🔧 Current parse_problem_object.py creates DoclingDocument but ignores it")
    print(f"📊 DoclingDocument contains {doc_structure['total_elements']} structured elements")
    print(f"🎯 Element types found: {list(doc_structure['elements_by_type'].keys())}")
    print(f"💡 We should use these structured elements instead of manual regex parsing")
    
    return result_md.document


def main():
    """Run the investigation on our workshop Problem object."""
    
    workshop_file = Path("20250707_130903_problem_object_odi_update.md")
    
    if not workshop_file.exists():
        print(f"❌ Workshop file not found: {workshop_file}")
        print("📁 Current directory contents:")
        for item in Path(".").iterdir():
            print(f"  - {item.name}")
        return
    
    docling_doc = investigate_docling_document(workshop_file)
    
    print()
    print("🎯 NEXT STEPS:")
    print("1. Review the generated JSON export to understand DoclingDocument structure")
    print("2. Identify how to extract Schema Attributes table from structured elements")
    print("3. Rewrite parse_problem_object.py to use DoclingDocument instead of regex")
    print("4. Create proper exploded attribute objects from structured data")


if __name__ == "__main__":
    main()