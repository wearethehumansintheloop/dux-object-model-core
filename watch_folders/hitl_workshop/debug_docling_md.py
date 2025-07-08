#!/usr/bin/env python3
"""
Debug why docling isn't parsing our markdown file
"""

from pathlib import Path
from docling.document_converter import DocumentConverter
import traceback

def debug_docling_parsing():
    """Debug docling markdown parsing."""
    
    file_path = Path("20250707_130903_problem_object_odi_update.md")
    
    print("🔍 Debug: Docling Markdown Parsing")
    print("=" * 50)
    
    # Check file exists and size
    if not file_path.exists():
        print(f"❌ File not found: {file_path}")
        return
    
    file_size = file_path.stat().st_size
    print(f"📁 File: {file_path.name}")
    print(f"📊 Size: {file_size} bytes")
    
    # Try to read file content
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        print(f"📝 Content length: {len(content)} characters")
        print(f"📝 First 200 chars: {content[:200]}...")
        print()
    except Exception as e:
        print(f"❌ Error reading file: {e}")
        return
    
    # Try docling conversion with detailed error handling
    try:
        print("🔄 Converting with DocumentConverter...")
        converter = DocumentConverter()
        
        # Enable debug/verbose if available
        print(f"📋 Converter type: {type(converter)}")
        
        result = converter.convert(file_path)
        
        print(f"✅ Conversion result: {type(result)}")
        print(f"📊 Document: {type(result.document)}")
        print(f"📊 Pages: {len(result.document.pages)}")
        
        if hasattr(result, 'status'):
            print(f"📊 Status: {result.status}")
        if hasattr(result, 'errors'):
            print(f"📊 Errors: {result.errors}")
        if hasattr(result, 'warnings'):
            print(f"📊 Warnings: {result.warnings}")
        
        # Check document details
        doc = result.document
        print(f"📊 Document title: {getattr(doc, 'title', 'No title')}")
        print(f"📊 Document origin: {getattr(doc, 'origin', 'No origin')}")
        
        if doc.pages:
            for i, page in enumerate(doc.pages):
                print(f"📄 Page {i+1}: {len(page.elements)} elements")
                for j, element in enumerate(page.elements[:3]):  # First 3 elements
                    print(f"  Element {j+1}: {type(element).__name__}")
                    if hasattr(element, 'text'):
                        preview = element.text[:50] + "..." if len(element.text) > 50 else element.text
                        print(f"    Text: {preview}")
        else:
            print("❌ No pages found in document")
        
    except Exception as e:
        print(f"❌ Docling conversion failed: {e}")
        print("📄 Full traceback:")
        traceback.print_exc()
    
    # Try alternative approaches
    print("\n🔄 Testing alternative approaches...")
    
    # Test with specific file types
    try:
        from docling.datamodel.base_models import InputFormat
        print(f"📋 Available formats: {[f for f in dir(InputFormat) if f.isupper()]}")
        print(f"📋 MD format value: {InputFormat.MD}")
    except Exception as e:
        print(f"❌ Error with InputFormat: {e}")

if __name__ == "__main__":
    debug_docling_parsing()