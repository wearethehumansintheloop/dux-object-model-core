"""
Process PDF with PyMuPDF and create TF-IDF vectors with full traceability
Simplified version that works reliably with PyMuPDF
"""

import os
import json
import numpy as np
import fitz  # PyMuPDF
from sklearn.feature_extraction.text import TfidfVectorizer
from typing import List, Dict, Tuple
from pathlib import Path


def process_pdf_with_pymupdf(pdf_path: str) -> List[Dict]:
    """
    Process PDF using PyMuPDF for reliable extraction with provenance
    """
    print(f"\n📄 Processing PDF with PyMuPDF: {pdf_path}")
    
    chunks = []
    doc = fitz.open(pdf_path)
    
    print(f"  Document has {len(doc)} pages")
    
    for page_num, page in enumerate(doc, start=1):
        print(f"  Processing page {page_num}...")
        
        # Extract text
        text = page.get_text()
        
        # Get page dimensions and metadata
        rect = page.rect
        
        # Extract any tables
        tables = page.find_tables()
        table_content = []
        if tables:
            for table in tables:
                try:
                    table_data = table.extract()
                    table_content.append({
                        'data': table_data,
                        'bbox': table.bbox if hasattr(table, 'bbox') else None
                    })
                except:
                    pass
        
        # Create chunk with full provenance
        chunk = {
            'slide_number': page_num,
            'content': text,
            'metadata': {
                'page_number': page_num,
                'bbox': {
                    'x0': rect.x0,
                    'y0': rect.y0,
                    'x1': rect.x1,
                    'y1': rect.y1,
                    'width': rect.width,
                    'height': rect.height
                },
                'rotation': page.rotation,
                'has_tables': len(table_content) > 0,
                'table_count': len(table_content)
            },
            'provenance': {
                'source_file': os.path.basename(pdf_path),
                'full_path': os.path.abspath(pdf_path),
                'extraction_method': 'pymupdf',
                'page_ref': f"Page {page_num}",
                'page_label': page.get_label() if hasattr(page, 'get_label') else f"Page {page_num}"
            }
        }
        
        if table_content:
            chunk['tables'] = table_content
        
        chunks.append(chunk)
    
    doc.close()
    print(f"  ✅ Extracted {len(chunks)} pages/chunks")
    return chunks


def create_tfidf_vectors_with_provenance(chunks: List[Dict]) -> Tuple[List[Dict], TfidfVectorizer, Dict]:
    """
    Convert chunks to TF-IDF vectors while maintaining full provenance
    """
    print("\n🔢 Creating TF-IDF vectors with provenance...")
    
    # Extract text content
    chunk_texts = [chunk['content'].strip() for chunk in chunks]
    
    # Filter out empty chunks
    valid_chunks = [(i, chunk, text) for i, (chunk, text) in enumerate(zip(chunks, chunk_texts)) if text]
    
    if not valid_chunks:
        print("  ❌ No valid text content found in PDF")
        return chunks, None, None
    
    valid_texts = [text for _, _, text in valid_chunks]
    
    # Create TF-IDF vectorizer
    vectorizer = TfidfVectorizer(
        max_features=100,
        ngram_range=(1, 2),
        min_df=1,
        max_df=0.95,
        stop_words='english',
        lowercase=True,
        token_pattern=r'\b[a-z]{2,}\b'
    )
    
    # Fit and transform
    tfidf_matrix = vectorizer.fit_transform(valid_texts)
    feature_names = vectorizer.get_feature_names_out()
    
    print(f"  📊 Vocabulary size: {len(feature_names)} terms")
    print(f"  📝 Sample terms: {list(feature_names[:10])}")
    
    # Create coordinate dictionary with provenance
    coordinate_dict = {
        'total_dimensions': len(feature_names),
        'pdf_source': chunks[0]['provenance']['source_file'] if chunks else 'unknown',
        'coordinate_mapping': {}
    }
    
    # Map coordinates to words
    for coord, word in enumerate(feature_names):
        coordinate_dict['coordinate_mapping'][coord] = {
            'coordinate': coord,
            'word': word,
            'appears_in_pages': []
        }
    
    # Process each valid chunk and attach vectors
    for idx, (orig_idx, chunk, _) in enumerate(valid_chunks):
        vector = tfidf_matrix[idx].toarray()[0]
        chunk['vector'] = vector
        chunk['feature_names'] = list(feature_names)
        
        # Extract non-zero features with provenance
        non_zero_indices = np.where(vector > 0)[0]
        chunk['active_terms'] = []
        
        for i in non_zero_indices:
            term_info = {
                'term': feature_names[i],
                'weight': float(vector[i]),
                'coordinate': int(i),
                'page_ref': chunk['provenance']['page_ref']
            }
            chunk['active_terms'].append(term_info)
            
            # Track which pages contain this term
            coordinate_dict['coordinate_mapping'][i]['appears_in_pages'].append(
                chunk['slide_number']
            )
        
        chunk['active_terms'].sort(key=lambda x: x['weight'], reverse=True)
        
        # Add vector summary
        chunk['vector_summary'] = {
            'total_coordinates': len(vector),
            'active_coordinates': len(non_zero_indices),
            'top_5_terms': chunk['active_terms'][:5] if chunk['active_terms'] else [],
            'density': len(non_zero_indices) / len(vector) if len(vector) > 0 else 0
        }
    
    print(f"  ✅ Created {len(feature_names)}-dimensional vectors")
    
    return chunks, vectorizer, coordinate_dict


def create_visual_vector_map(chunk: Dict) -> str:
    """
    Create a visual representation of a chunk's vector
    """
    if 'vector' not in chunk:
        return "No vector data available"
    
    vector = chunk['vector']
    visual = []
    
    visual.append("="*80)
    visual.append(f"VECTOR MAP - Page {chunk['slide_number']}")
    visual.append("="*80)
    
    # Show coordinate grid (10x10 for up to 100 dimensions)
    visual.append("\nCOORDINATE GRID:")
    visual.append("-" * 60)
    
    vector_size = len(vector)
    grid_rows = min(10, (vector_size + 9) // 10)
    
    for row in range(grid_rows):
        row_str = ""
        for col in range(10):
            coord = row * 10 + col
            if coord >= vector_size:
                row_str += "  "
                continue
            value = vector[coord]
            if value > 0:
                if value > 0.5:
                    row_str += "█ "
                elif value > 0.3:
                    row_str += "▓ "
                elif value > 0.1:
                    row_str += "▒ "
                else:
                    row_str += "░ "
            else:
                row_str += "· "
        
        start_coord = row * 10
        end_coord = min(start_coord + 9, vector_size - 1)
        visual.append(f"[{start_coord:2d}-{end_coord:2d}] {row_str}")
    
    visual.append("\nLegend: █=high ▓=medium ▒=low ░=very low ·=zero")
    
    # Show top active terms
    if 'active_terms' in chunk:
        visual.append("\nTOP ACTIVE TERMS:")
        visual.append("-" * 60)
        for term_info in chunk['active_terms'][:10]:
            coord = term_info['coordinate']
            term = term_info['term']
            weight = term_info['weight']
            visual.append(f"  [{coord:3d}] '{term:20s}' = {weight:.4f}")
    
    return "\n".join(visual)


def generate_provenance_report(chunks: List[Dict], coordinate_dict: Dict) -> Dict:
    """
    Generate a detailed provenance report
    """
    print("\n📋 Generating Provenance Report...")
    
    if not coordinate_dict:
        return {}
    
    report = {
        'source_document': coordinate_dict['pdf_source'],
        'total_pages': len(chunks),
        'total_dimensions': coordinate_dict['total_dimensions'],
        'extraction_method': chunks[0]['provenance']['extraction_method'] if chunks else 'unknown',
        'page_summaries': [],
        'term_distribution': {},
        'most_common_terms': []
    }
    
    # Analyze each page
    for chunk in chunks:
        if 'vector_summary' in chunk:
            page_summary = {
                'page_number': chunk['slide_number'],
                'content_length': len(chunk['content']),
                'active_coordinates': chunk['vector_summary']['active_coordinates'],
                'vector_density': chunk['vector_summary']['density'],
                'top_terms': [t['term'] for t in chunk['vector_summary']['top_5_terms']],
                'has_tables': chunk['metadata'].get('has_tables', False)
            }
            report['page_summaries'].append(page_summary)
    
    # Analyze term distribution
    for coord_info in coordinate_dict['coordinate_mapping'].values():
        term = coord_info['word']
        pages = coord_info['appears_in_pages']
        if pages:
            report['term_distribution'][term] = {
                'appears_in_pages': list(set(pages)),
                'page_count': len(set(pages)),
                'frequency': len(pages)
            }
    
    # Get most common terms
    if report['term_distribution']:
        report['most_common_terms'] = sorted(
            report['term_distribution'].items(),
            key=lambda x: x[1]['frequency'],
            reverse=True
        )[:20]
    
    return report


def save_results(chunks: List[Dict], coordinate_dict: Dict, report: Dict):
    """
    Save all results with full provenance
    """
    print("\n💾 Saving results...")
    
    # Save chunks (without full vectors for readability)
    chunks_export = []
    for chunk in chunks:
        chunk_export = {
            'page_number': chunk['slide_number'],
            'content_preview': chunk['content'][:500] + '...' if len(chunk['content']) > 500 else chunk['content'],
            'provenance': chunk['provenance'],
            'metadata': chunk['metadata']
        }
        if 'vector_summary' in chunk:
            chunk_export['vector_summary'] = chunk['vector_summary']
        chunks_export.append(chunk_export)
    
    with open('pdf_chunks_pymupdf.json', 'w', encoding='utf-8') as f:
        json.dump(chunks_export, f, indent=2, ensure_ascii=False)
    
    # Save coordinate dictionary
    if coordinate_dict:
        with open('pdf_coordinate_dictionary_pymupdf.json', 'w', encoding='utf-8') as f:
            json.dump(coordinate_dict, f, indent=2, ensure_ascii=False)
    
    # Save report
    if report:
        with open('pdf_provenance_report_pymupdf.json', 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
    
    print("  ✅ Saved pdf_chunks_pymupdf.json")
    if coordinate_dict:
        print("  ✅ Saved pdf_coordinate_dictionary_pymupdf.json")
    if report:
        print("  ✅ Saved pdf_provenance_report_pymupdf.json")


def main():
    """
    Main execution
    """
    pdf_path = "DesignForTimeWellSpentAgentOrientedBots_forReview.pdf"
    
    if not os.path.exists(pdf_path):
        print(f"❌ PDF not found: {pdf_path}")
        return
    
    print("="*80)
    print("PDF TO TF-IDF VECTOR PROCESSING WITH PYMUPDF")
    print("="*80)
    
    # Process PDF
    chunks = process_pdf_with_pymupdf(pdf_path)
    
    # Create vectors
    chunks, vectorizer, coordinate_dict = create_tfidf_vectors_with_provenance(chunks)
    
    if not vectorizer:
        print("❌ Could not create vectors from PDF content")
        return
    
    # Generate report
    report = generate_provenance_report(chunks, coordinate_dict)
    
    # Print summary
    print("\n" + "="*80)
    print("PROVENANCE SUMMARY")
    print("="*80)
    print(f"\n📄 Source: {report['source_document']}")
    print(f"📑 Total Pages: {report['total_pages']}")
    print(f"🔢 Vector Dimensions: {report['total_dimensions']}")
    
    # Show sample page vector maps
    print("\n" + "="*80)
    print("SAMPLE VECTOR VISUALIZATIONS")
    print("="*80)
    
    # Show first 2 pages with content
    for chunk in chunks[:2]:
        if 'vector' in chunk and chunk['content'].strip():
            print(create_visual_vector_map(chunk))
            print()
    
    # Save results
    save_results(chunks, coordinate_dict, report)
    
    print("\n✅ Processing complete!")
    print("📊 Check the JSON files for detailed results")
    print("🔍 Each coordinate position maps to a specific word/phrase")
    print("📍 Full provenance maintained: PDF → Page → Chunk → Vector → Coordinate")
    
    return chunks, vectorizer, coordinate_dict, report


if __name__ == "__main__":
    results = main()
