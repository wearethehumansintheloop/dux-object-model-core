#!/usr/bin/env python3
"""
HITL Workshop: Fixed DoclingDocument-Based Parser

This implements the CORRECT approach using DoclingDocument's structured data:
- Uses doc.tables for Schema Attributes table (instead of regex)
- Uses doc.texts for structured text elements
- Uses doc.groups for organized content
- Creates proper exploded attribute objects

This replaces the broken parse_problem_object.py approach.
"""

import json
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from docling.document_converter import DocumentConverter

def explore_docling_structure(doc) -> Dict[str, Any]:
    """
    Explore the complete DoclingDocument structure for debugging and understanding.
    
    This function analyzes what docling extracts from markdown:
    - Tables: Structured table data (our main target for Schema Attributes)
    - Texts: Text elements like headers, paragraphs
    - Groups: Organizational structures like lists
    
    Returns:
        Dict containing analysis of all structured elements found
    """
    
    structure = {
        'tables': [],
        'texts': [],
        'groups': [],
        'export_text_length': 0,
        'raw_analysis': {}
    }
    
    # Extract full text content using docling's export method
    # This gives us the complete markdown content as processed text
    try:
        full_text = doc.export_to_text()
        structure['export_text_length'] = len(full_text) if full_text else 0
    except Exception as e:
        structure['export_text_error'] = str(e)
    
    # Analyze tables - this is our primary target for Schema Attributes extraction
    # Docling parses markdown tables into structured TableItem objects
    for i, table in enumerate(doc.tables):
        table_info = {
            'index': i,
            'type': type(table).__name__,
            'ref': getattr(table, 'self_ref', 'No ref'),  # Internal docling reference
            'has_data': hasattr(table, 'data'),           # Check if table has structured data
            'content_layer': getattr(table, 'content_layer', 'No layer')  # Docling content organization
        }
        
        # Attempt to extract actual table data through various possible structures
        # Different docling versions might organize table data differently
        if hasattr(table, 'data') and table.data:
            try:
                # Strategy 1: Look for nested table.data.table structure
                if hasattr(table.data, 'table'):
                    table_data = table.data.table
                    if hasattr(table_data, 'data') and table_data.data:
                        table_info['rows'] = len(table_data.data)
                        table_info['first_row'] = table_data.data[0] if table_data.data else None
                        table_info['all_data'] = table_data.data[:5]  # Sample data for inspection
                
                # Strategy 2: Look for direct rows structure
                elif hasattr(table.data, 'rows'):
                    table_info['rows'] = len(table.data.rows)
                    table_info['first_row'] = table.data.rows[0] if table.data.rows else None
                
                # Strategy 3: Examine data object structure for unknown formats
                else:
                    table_info['data_type'] = type(table.data).__name__
                    table_info['data_attrs'] = [attr for attr in dir(table.data) if not attr.startswith('_')]
                    
            except Exception as e:
                table_info['data_error'] = str(e)
        
        structure['tables'].append(table_info)
    
    # Analyze text elements - headers, paragraphs, etc.
    # These might contain Schema Attributes section headers or content
    for i, text in enumerate(doc.texts[:10]):  # Limit to first 10 for performance
        text_info = {
            'index': i,
            'type': type(text).__name__,                  # TitleItem, TextItem, etc.
            'ref': getattr(text, 'self_ref', 'No ref'),   # Internal docling reference
            'text_preview': getattr(text, 'text', 'No text')[:100] if hasattr(text, 'text') else 'No text attr'
        }
        structure['texts'].append(text_info)
    
    # Analyze groups - organizational structures like lists, sections
    # These show how docling organizes the document structure
    for i, group in enumerate(doc.groups[:5]):  # Limit to first 5 for performance
        group_info = {
            'index': i,
            'type': type(group).__name__,                    # ListGroup, etc.
            'ref': getattr(group, 'self_ref', 'No ref'),     # Internal docling reference
            'children_count': len(getattr(group, 'children', [])),  # How many child elements
            'content_layer': getattr(group, 'content_layer', 'No layer')  # Docling organization layer
        }
        structure['groups'].append(group_info)
    
    return structure


def extract_schema_table_from_docling(doc) -> Optional[Dict[str, Any]]:
    """
    Extract Schema Attributes table using DoclingDocument's structured data.
    
    KEY BREAKTHROUGH: DoclingDocument stores tables as structured TableItem objects
    with table.data.grid containing TableCell objects, NOT as pages/elements.
    This replaces manual regex parsing with proper structured data access.
    
    Returns:
        Dict with headers, attributes array, and source info if table found
    """
    
    print("🔍 Searching for Schema Attributes table in DoclingDocument...")
    
    # Strategy 1: Use table.data.grid (the breakthrough discovery!)
    # Each table has a .data.grid property containing rows of TableCell objects
    for i, table in enumerate(doc.tables):
        print(f"📊 Examining table {i}: {type(table).__name__}")
        
        if hasattr(table, 'data') and table.data and hasattr(table.data, 'grid'):
            grid = table.data.grid
            print(f"  📋 Found table grid with {len(grid)} rows x {len(grid[0]) if grid else 0} cols")
            
            if len(grid) > 0 and len(grid[0]) >= 3:
                # Extract headers from first row
                headers = []
                for cell in grid[0]:
                    if hasattr(cell, 'text'):
                        headers.append(cell.text.strip())
                    else:
                        headers.append(str(cell).strip())
                
                print(f"  📝 Headers: {headers}")
                
                # Check if this looks like Schema Attributes table
                if any('attribute' in header.lower() for header in headers):
                    print("  ✅ Found Schema Attributes table!")
                    
                    # Extract data rows (skip header row)
                    attributes = []
                    for row in grid[1:]:
                        if len(row) >= len(headers):
                            row_dict = {}
                            for j, cell in enumerate(row):
                                if j < len(headers):
                                    cell_text = cell.text.strip() if hasattr(cell, 'text') else str(cell).strip()
                                    row_dict[headers[j]] = cell_text
                            
                            # Only add if has attribute name
                            if row_dict.get('Attribute') and row_dict.get('Attribute').strip():
                                attributes.append(row_dict)
                    
                    return {
                        'headers': headers,
                        'attributes': attributes,
                        'source': f'docling_table_{i}_grid'
                    }
    
    # Strategy 2: Use table markdown export as fallback
    print("📝 Trying table markdown export...")
    
    for i, table in enumerate(doc.tables):
        try:
            if hasattr(table, 'export_to_markdown'):
                table_md = table.export_to_markdown()
                if table_md and '|' in table_md and 'attribute' in table_md.lower():
                    print(f"  📝 Found table via markdown export")
                    
                    # Parse markdown table
                    lines = [line.strip() for line in table_md.split('\n') if line.strip()]
                    table_lines = [line for line in lines if '|' in line and not line.startswith('|--')]
                    
                    if len(table_lines) >= 2:  # Header + at least one data row
                        # Parse header
                        headers = [cell.strip() for cell in table_lines[0].split('|') if cell.strip()]
                        
                        # Parse data rows
                        attributes = []
                        for line in table_lines[1:]:
                            cells = [cell.strip() for cell in line.split('|') if cell.strip()]
                            if len(cells) >= len(headers):
                                row_dict = {}
                                for j, header in enumerate(headers):
                                    if j < len(cells):
                                        row_dict[header] = cells[j]
                                if row_dict.get('Attribute'):
                                    attributes.append(row_dict)
                        
                        return {
                            'headers': headers,
                            'attributes': attributes,
                            'source': f'docling_table_{i}_markdown'
                        }
                        
        except Exception as e:
            print(f"  ❌ Markdown export error: {e}")
    
    print("❌ No Schema Attributes table found in structured DoclingDocument")
    return None


def generate_exploded_attribute_objects(schema_data: Dict[str, Any], doc) -> List[Dict[str, Any]]:
    """
    Generate individual exploded objects for each schema attribute.
    
    This creates the "explosion" - converting a single schema table into 
    individual objects for each attribute (job_statement, opportunity_score, etc.)
    Each exploded object contains the attribute definition plus metadata.
    """
    
    exploded_objects = []
    
    if not schema_data or 'attributes' not in schema_data:
        return exploded_objects
    
    for attr in schema_data['attributes']:
        attr_name = attr.get('Attribute', 'unknown')
        attr_type = attr.get('Type', 'unknown')
        is_required = attr.get('Required', '').lower() == 'yes'
        description = attr.get('Description', '')
        
        # Create individual attribute object
        attr_object = {
            'attribute_name': attr_name,
            'type': attr_type,
            'required': is_required,
            'description': description,
            'source_document': doc.name,
            'extraction_method': 'docling_structured',
            'docling_metadata': {
                'source_table': schema_data.get('source', 'unknown'),
                'total_attributes': len(schema_data['attributes']),
                'document_origin': str(doc.origin)
            }
        }
        
        # Add type-specific processing
        if attr_name == 'job_statement' and 'decomposed' in description.lower():
            attr_object['structure'] = 'decomposed'
            attr_object['components'] = ['user_scenario', 'user_enablement', 'user_outcome']
            attr_object['source_tracking'] = True
            
        elif attr_name == 'opportunity_score':
            attr_object['structure'] = 'odi_scoring'
            attr_object['components'] = ['value', 'importance', 'satisfaction']
            attr_object['source_tracking'] = True
            attr_object['scoring_range'] = {
                'value': '1-20',
                'importance': '1-10', 
                'satisfaction': '1-10'
            }
            
        elif attr_name == 'evidence':
            attr_object['structure'] = 'array_of_objects'
            attr_object['components'] = ['provenance_id', 'supports_fields']
            
        exploded_objects.append(attr_object)
    
    return exploded_objects


def process_problem_object_with_docling(file_path: Path) -> Dict[str, Any]:
    """
    Process Problem object using proper DoclingDocument structured approach.
    
    This is the CORRECT implementation that uses DoclingDocument's structured data.
    """
    print(f"🔧 Processing Problem object with DoclingDocument: {file_path.name}")
    print("=" * 60)
    
    try:
        # Create DoclingDocument (this part was always working)
        converter = DocumentConverter()
        result = converter.convert(file_path)
        doc = result.document
        
        print(f"✅ DoclingDocument created: {type(doc)}")
        print(f"📊 Document name: {doc.name}")
        print(f"📊 Origin: {doc.origin}")
        
        # Explore the structure first
        structure = explore_docling_structure(doc)
        print(f"\n📋 Document structure:")
        print(f"  📊 Tables: {len(structure['tables'])}")
        print(f"  📝 Texts: {len(structure['texts'])}")
        print(f"  📦 Groups: {len(structure['groups'])}")
        print(f"  📄 Full text length: {structure['export_text_length']}")
        
        # Extract Schema Attributes table using structured approach
        schema_data = extract_schema_table_from_docling(doc)
        
        if not schema_data:
            return {
                'success': False,
                'stage': 'schema_extraction',
                'errors': ['Schema Attributes table not found in DoclingDocument structure'],
                'structure_analysis': structure,
                'docling_document': doc
            }
        
        print(f"\n✅ Schema table extracted:")
        print(f"  📋 Headers: {schema_data['headers']}")
        print(f"  📋 Attributes: {len(schema_data['attributes'])}")
        print(f"  📋 Source: {schema_data['source']}")
        
        # Generate exploded attribute objects (the explosion!)
        exploded_objects = generate_exploded_attribute_objects(schema_data, doc)
        
        print(f"\n🎯 Generated {len(exploded_objects)} exploded attribute objects:")
        for obj in exploded_objects[:5]:  # Show first 5
            print(f"  🔧 {obj['attribute_name']} ({obj['type']}) - Required: {obj['required']}")
        
        return {
            'success': True,
            'stage': 'completed',
            'errors': [],
            'schema_data': schema_data,
            'exploded_objects': exploded_objects,
            'structure_analysis': structure,
            'docling_document': doc,
            'full_text': doc.export_to_text(),
            'processing_method': 'docling_structured'
        }
        
    except Exception as e:
        return {
            'success': False,
            'stage': 'docling_conversion',
            'errors': [f"DoclingDocument processing failed: {str(e)}"],
            'docling_document': None
        }


def save_exploded_objects(exploded_objects: List[Dict[str, Any]], base_path: Path):
    """Save exploded attribute objects as individual files."""
    
    exploded_dir = base_path.parent / f"{base_path.stem}_exploded_attributes"
    exploded_dir.mkdir(exist_ok=True)
    
    print(f"\n💾 Saving {len(exploded_objects)} exploded objects to: {exploded_dir.name}")
    
    for obj in exploded_objects:
        attr_name = obj['attribute_name']
        filename = f"{attr_name}_attribute.json"
        filepath = exploded_dir / filename
        
        with open(filepath, 'w') as f:
            json.dump(obj, f, indent=2)
        
        print(f"  📄 Saved: {filename}")
    
    # Save summary
    summary = {
        'total_attributes': len(exploded_objects),
        'source_document': exploded_objects[0]['source_document'] if exploded_objects else 'unknown',
        'extraction_timestamp': str(Path().cwd()),
        'attributes': [obj['attribute_name'] for obj in exploded_objects]
    }
    
    summary_path = exploded_dir / "explosion_summary.json"
    with open(summary_path, 'w') as f:
        json.dump(summary, f, indent=2)
    
    print(f"  📋 Summary: explosion_summary.json")
    
    return exploded_dir


def main():
    """Test the fixed DoclingDocument approach."""
    
    print("🚀 HITL Workshop: Fixed DoclingDocument Parser")
    print("=" * 70)
    
    file_path = Path("20250707_130903_problem_object_odi_update.md")
    
    if not file_path.exists():
        print(f"❌ File not found: {file_path}")
        return
    
    # Process with correct DoclingDocument approach
    result = process_problem_object_with_docling(file_path)
    
    print(f"\n📋 PROCESSING RESULTS:")
    print(f"✅ Success: {result['success']}")
    print(f"🎯 Stage: {result['stage']}")
    
    if result['errors']:
        print(f"❌ Errors ({len(result['errors'])}):") 
        for error in result['errors']:
            print(f"  - {error}")
    
    if result['success'] and result.get('exploded_objects'):
        # Save exploded objects
        exploded_dir = save_exploded_objects(result['exploded_objects'], file_path)
        
        print(f"\n🎉 SUCCESS! This is the breakthrough we needed:")
        print(f"  ✅ DoclingDocument parsed markdown structure correctly")
        print(f"  ✅ Schema Attributes table extracted without regex")
        print(f"  ✅ {len(result['exploded_objects'])} exploded attribute objects created")
        print(f"  ✅ Individual attribute files saved in: {exploded_dir.name}")
        print(f"\n📁 Next: Review exploded objects and integrate into Stage 3 pipeline")
    
    else:
        print("\n❌ Processing failed - need to debug table extraction")
        if result.get('structure_analysis'):
            print("📊 Available structure analysis for debugging")


if __name__ == "__main__":
    main()