#!/usr/bin/env python3
"""
Test if docling provides raw text content for markdown
"""

from pathlib import Path
from docling.document_converter import DocumentConverter

def test_docling_text_content():
    """Test accessing raw text content from DoclingDocument."""
    
    file_path = Path("20250707_130903_problem_object_odi_update.md")
    
    print("🔍 Testing Docling Text Content Access")
    print("=" * 50)
    
    converter = DocumentConverter()
    result = converter.convert(file_path)
    doc = result.document
    
    # Explore all attributes of the document
    print("📋 DoclingDocument attributes:")
    attrs = [attr for attr in dir(doc) if not attr.startswith('_')]
    for attr in attrs:
        try:
            value = getattr(doc, attr)
            if callable(value):
                print(f"  🔧 {attr}(): {type(value)}")
            else:
                print(f"  📊 {attr}: {type(value)} = {str(value)[:100]}...")
        except Exception as e:
            print(f"  ❌ {attr}: Error - {e}")
    
    # Try common text access methods
    print("\n📝 Text content access attempts:")
    
    # Method 1: Direct text attribute
    if hasattr(doc, 'text'):
        text = doc.text
        print(f"  📝 doc.text: {type(text)} - Length: {len(text) if text else 0}")
        if text:
            print(f"       Preview: {text[:200]}...")
    
    # Method 2: Export to text
    if hasattr(doc, 'export_to_text'):
        try:
            exported_text = doc.export_to_text()
            print(f"  📝 doc.export_to_text(): {type(exported_text)} - Length: {len(exported_text) if exported_text else 0}")
            if exported_text:
                print(f"       Preview: {exported_text[:200]}...")
        except Exception as e:
            print(f"  ❌ doc.export_to_text(): {e}")
    
    # Method 3: Check if main_text exists
    if hasattr(doc, 'main_text'):
        main_text = doc.main_text
        print(f"  📝 doc.main_text: {type(main_text)} - Length: {len(main_text) if main_text else 0}")
        if main_text:
            print(f"       Preview: {main_text[:200]}...")
    
    # Method 4: Iterate through any text elements
    if doc.pages:
        print("\n📄 Page content:")
        for i, page in enumerate(doc.pages):
            print(f"  Page {i+1}: {len(page.elements)} elements")
    else:
        print("\n❌ No pages - this confirms markdown isn't parsed into page structure")
    
    # Method 5: Check origin for raw content
    if hasattr(doc, 'origin') and hasattr(doc.origin, 'binary_content'):
        print(f"\n📊 Origin binary content available: {hasattr(doc.origin, 'binary_content')}")
    
    print("\n🎯 ANALYSIS:")
    print("If docling provides raw text content, we can use that instead of manual file reading.")
    print("If not, we need to understand why parse_problem_object.py ignores the DoclingDocument.")

if __name__ == "__main__":
    test_docling_text_content()