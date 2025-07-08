#!/usr/bin/env python3
"""
Test proper docling configuration for markdown processing
"""

from pathlib import Path
from docling.document_converter import DocumentConverter
from docling.datamodel.base_models import InputFormat

def test_docling_configurations():
    """Test different docling configurations."""
    
    file_path = Path("20250707_130903_problem_object_odi_update.md")
    
    print("🔍 Testing Docling Configurations")
    print("=" * 50)
    
    # Test 1: Default converter (like parse_problem_object.py does)
    print("📋 Test 1: Default DocumentConverter (current approach)")
    try:
        converter_default = DocumentConverter()
        result_default = converter_default.convert(file_path)
        print(f"  ✅ Pages: {len(result_default.document.pages)}")
        print(f"  ✅ Elements: {sum(len(p.elements) for p in result_default.document.pages)}")
    except Exception as e:
        print(f"  ❌ Error: {e}")
    
    # Test 2: Configured converter (like research platform)
    print("\n📋 Test 2: Configured DocumentConverter (research platform approach)")
    try:
        allowed_formats = [InputFormat.MD, InputFormat.PDF, InputFormat.DOCX]
        converter_config = DocumentConverter(allowed_formats=allowed_formats)
        result_config = converter_config.convert(file_path)
        print(f"  ✅ Pages: {len(result_config.document.pages)}")
        print(f"  ✅ Elements: {sum(len(p.elements) for p in result_config.document.pages)}")
    except Exception as e:
        print(f"  ❌ Error: {e}")
    
    # Test 3: Check if TXT format exists
    print("\n📋 Test 3: Check available formats")
    try:
        all_formats = [f for f in dir(InputFormat) if f.isupper()]
        print(f"  📝 All formats: {all_formats}")
        
        # Try to access TXT if it exists
        if hasattr(InputFormat, 'TXT'):
            print(f"  📝 TXT format: {InputFormat.TXT}")
        else:
            print("  ❌ TXT format not available")
            
    except Exception as e:
        print(f"  ❌ Error: {e}")
    
    # Test 4: Force markdown processing
    print("\n📋 Test 4: Try markdown-specific processing")
    try:
        # Check if there are markdown-specific options
        converter_md = DocumentConverter()
        
        # Check converter options
        if hasattr(converter_md, 'format_to_options'):
            md_options = converter_md.format_to_options.get(InputFormat.MD, "No options")
            print(f"  📝 MD options: {md_options}")
        
        # Try manual format specification (if possible)
        result_md = converter_md.convert(file_path)
        doc = result_md.document
        
        print(f"  📊 Origin: {doc.origin}")
        print(f"  📊 Metadata: {getattr(doc, 'metadata', 'No metadata')}")
        
        # Check if document has any text content even without pages
        if hasattr(doc, 'text'):
            print(f"  📝 Raw text length: {len(doc.text) if doc.text else 0}")
        
    except Exception as e:
        print(f"  ❌ Error: {e}")
    
    print("\n🎯 CONCLUSION:")
    print("If all tests show 0 pages/elements, then docling may not be")
    print("designed to parse markdown into structured elements at all!")
    print("This would explain why parse_problem_object.py uses manual regex.")

if __name__ == "__main__":
    test_docling_configurations()