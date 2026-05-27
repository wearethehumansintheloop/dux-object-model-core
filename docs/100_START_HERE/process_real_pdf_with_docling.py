"""
Process Real PDF with Docling and TF-IDF Vector Analysis
Demonstrates actual PDF to vector conversion with full traceability
"""

import os
import json
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from typing import List, Dict, Tuple
from pathlib import Path

# Try to import Docling, fall back to PyMuPDF if not available
try:
    from docling.document_converter import DocumentConverter
    from docling.datamodel.base_models import InputFormat
    from docling.datamodel.pipeline_options import PdfPipelineOptions
    DOCLING_AVAILABLE = True
    print("✅ Using Docling for PDF processing")
except ImportError:
    DOCLING_AVAILABLE = False
    print("⚠️ Docling not available, trying PyMuPDF...")
    try:
        import fitz  # PyMuPDF
        PYMUPDF_AVAILABLE = True
        print("✅ Using PyMuPDF for PDF processing")
    except ImportError:
        PYMUPDF_AVAILABLE = False
        print("❌ Neither Docling nor PyMuPDF available")


def process_pdf_with_docling(pdf_path: str) -> List[Dict]:
    """
    Process PDF using Docling for high-quality extraction with provenance
    """
    print(f"\n📄 Processing PDF with Docling: {pdf_path}")
    
    # Convert PDF using the newer Docling API
    converter = DocumentConverter()
    result = converter.convert(pdf_path)
    
    # Extract chunks with full provenance
    chunks = []
    
    # Check if result has document attribute
    if hasattr(result, 'document'):
        doc = result.document
    else:
        doc = result
    
    # Try to get pages or export as markdown
    if hasattr(doc, 'pages') and doc.pages:
        # Process by pages
        for page_num, page in enumerate(doc.pages, start=1):
            print(f"  Processing page {page_num}...")
            
            # Extract page content
            if hasattr(page, 'export_to_markdown'):
                page_content = page.export_to_markdown()
            elif hasattr(page, 'text'):
                page_content = page.text
            else:
                page_content = str(page)
            
            # Extract metadata with provenance
            chunk = {
                'slide_number': page_num,
                'content': page_content,
                'docling_metadata': {
                    'page_number': page_num,
                    'bbox': page.bbox if hasattr(page, 'bbox') else None,
                    'extraction_confidence': getattr(page, 'confidence', 1.0),
                    'has_tables': len(page.tables) > 0 if hasattr(page, 'tables') else False,
                    'has_pictures': len(page.pictures) > 0 if hasattr(page, 'pictures') else False,
                    'hierarchical_structure': page.get_hierarchy() if hasattr(page, 'get_hierarchy') else None
                },
                'provenance': {
                    'source_file': os.path.basename(pdf_path),
                    'full_path': os.path.abspath(pdf_path),
                    'extraction_method': 'docling',
                    'page_ref': f"Page {page_num}"
                }
            }
            
            # Add table information if present
            if hasattr(page, 'tables') and page.tables:
                chunk['tables'] = []
                for table in page.tables:
                    chunk['tables'].append({
                        'content': table.to_markdown() if hasattr(table, 'to_markdown') else str(table),
                        'bbox': table.bbox if hasattr(table, 'bbox') else None
                    })
            
            # Add picture information if present
            if hasattr(page, 'pictures') and page.pictures:
                chunk['pictures'] = []
                for pic in page.pictures:
                    chunk['pictures'].append({
                        'caption': pic.caption if hasattr(pic, 'caption') else None,
                        'bbox': pic.bbox if hasattr(pic, 'bbox') else None
                    })
            
            chunks.append(chunk)
    else:
        # Fallback: export entire document as markdown
        print("  Processing document as single chunk...")
        if hasattr(doc, 'export_to_markdown'):
            content = doc.export_to_markdown()
        elif hasattr(doc, 'text'):
            content = doc.text
        else:
            content = str(doc)
        
        # Split content by common page markers if possible
        # This is a simple heuristic - could be improved
        pages = content.split('\n\n\n')  # Common page break pattern
        
        for page_num, page_content in enumerate(pages, start=1):
            if page_content.strip():  # Skip empty pages
                chunk = {
                    'slide_number': page_num,
                    'content': page_content,
                    'docling_metadata': {
                        'page_number': page_num,
                        'extraction_confidence': 1.0,
                        'note': 'Document processed as whole, pages estimated'
                    },
                    'provenance': {
                        'source_file': os.path.basename(pdf_path),
                        'full_path': os.path.abspath(pdf_path),
                        'extraction_method': 'docling',
                        'page_ref': f"Page {page_num} (estimated)"
                    }
                }
                chunks.append(chunk)
    
    print(f"  ✅ Extracted {len(chunks)} pages/chunks")
    return chunks


def process_pdf_with_pymupdf(pdf_path: str) -> List[Dict]:
    """
    Fallback: Process PDF using PyMuPDF if Docling is not available
    """
    print(f"\n📄 Processing PDF with PyMuPDF: {pdf_path}")
    
    chunks = []
    doc = fitz.open(pdf_path)
    
    for page_num, page in enumerate(doc, start=1):
        print(f"  Processing page {page_num}...")
        
        # Extract text
        text = page.get_text()
        
        # Get page dimensions
        rect = page.rect
        
        chunk = {
            'slide_number': page_num,
            'content': text,
            'pymupdf_metadata': {
                'page_number': page_num,
                'bbox': {
                    'x0': rect.x0,
                    'y0': rect.y0,
                    'x1': rect.x1,
                    'y1': rect.y1
                },
                'width': rect.width,
                'height': rect.height,
                'extraction_method': 'pymupdf'
            },
            'provenance': {
                'source_file': os.path.basename(pdf_path),
                'full_path': os.path.abspath(pdf_path),
                'extraction_method': 'pymupdf',
                'page_ref': f"Page {page_num}"
            }
        }
        
        # Extract tables (basic detection)
        tables = page.find_tables()
        if tables:
            chunk['tables'] = []
            for table in tables:
                chunk['tables'].append({
                    'content': table.extract(),
                    'bbox': table.bbox
                })
        
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
    tfidf_matrix = vectorizer.fit_transform(chunk_texts)
    feature_names = vectorizer.get_feature_names_out()
    
    # Create coordinate dictionary with provenance
    coordinate_dict = {
        'total_dimensions': len(feature_names),
        'pdf_source': chunks[0]['provenance']['source_file'] if chunks else 'unknown',
        'coordinate_mapping': {}
    }
    
    for coord, word in enumerate(feature_names):
        coordinate_dict['coordinate_mapping'][coord] = {
            'coordinate': coord,
            'word': word,
            'appears_in_pages': []
        }
    
    # Process each chunk and attach vectors
    for idx, chunk in enumerate(chunks):
        vector = tfidf_matrix[idx].toarray()[0]
        chunk['vector'] = vector
        chunk['feature_names'] = feature_names
        
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
            'density': len(non_zero_indices) / len(vector)
        }
    
    print(f"  ✅ Created {len(feature_names)}-dimensional vectors")
    print(f"  📊 Vocabulary size: {len(feature_names)} terms")
    
    return chunks, vectorizer, coordinate_dict


def generate_provenance_report(chunks: List[Dict], coordinate_dict: Dict):
    """
    Generate a detailed provenance report
    """
    print("\n📋 Generating Provenance Report...")
    
    report = {
        'source_document': coordinate_dict['pdf_source'],
        'total_pages': len(chunks),
        'total_dimensions': coordinate_dict['total_dimensions'],
        'extraction_method': chunks[0]['provenance']['extraction_method'] if chunks else 'unknown',
        'page_summaries': [],
        'term_distribution': {},
        'coordinate_usage': {}
    }
    
    # Analyze each page
    for chunk in chunks:
        page_summary = {
            'page_number': chunk['slide_number'],
            'content_length': len(chunk['content']),
            'active_coordinates': chunk['vector_summary']['active_coordinates'],
            'vector_density': chunk['vector_summary']['density'],
            'top_terms': [t['term'] for t in chunk['vector_summary']['top_5_terms']],
            'has_tables': chunk.get('tables', []) != [],
            'has_pictures': chunk.get('pictures', []) != []
        }
        report['page_summaries'].append(page_summary)
    
    # Analyze term distribution across pages
    for coord_info in coordinate_dict['coordinate_mapping'].values():
        term = coord_info['word']
        pages = coord_info['appears_in_pages']
        if pages:
            report['term_distribution'][term] = {
                'appears_in_pages': pages,
                'page_count': len(set(pages)),
                'frequency': len(pages)
            }
    
    # Sort terms by frequency
    report['most_common_terms'] = sorted(
        report['term_distribution'].items(),
        key=lambda x: x[1]['frequency'],
        reverse=True
    )[:20]
    
    return report


def save_results(chunks: List[Dict], coordinate_dict: Dict, report: Dict, output_dir: str = "."):
    """
    Save all results with full provenance
    """
    print("\n💾 Saving results...")
    
    # Save chunks with vectors (excluding the actual vector arrays for readability)
    chunks_export = []
    for chunk in chunks:
        chunk_export = {
            'page_number': chunk['slide_number'],
            'content_preview': chunk['content'][:200] + '...' if len(chunk['content']) > 200 else chunk['content'],
            'provenance': chunk['provenance'],
            'vector_summary': chunk['vector_summary'],
            'metadata': chunk.get('docling_metadata') or chunk.get('pymupdf_metadata')
        }
        chunks_export.append(chunk_export)
    
    with open(f"{output_dir}/pdf_chunks_with_provenance.json", 'w') as f:
        json.dump(chunks_export, f, indent=2)
    
    # Save coordinate dictionary
    with open(f"{output_dir}/pdf_coordinate_dictionary.json", 'w') as f:
        json.dump(coordinate_dict, f, indent=2)
    
    # Save provenance report
    with open(f"{output_dir}/pdf_provenance_report.json", 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"  ✅ Saved pdf_chunks_with_provenance.json")
    print(f"  ✅ Saved pdf_coordinate_dictionary.json")
    print(f"  ✅ Saved pdf_provenance_report.json")


def print_provenance_summary(report: Dict):
    """
    Print a summary of the provenance report
    """
    print("\n" + "="*80)
    print("PROVENANCE SUMMARY")
    print("="*80)
    
    print(f"\n📄 Source: {report['source_document']}")
    print(f"📑 Total Pages: {report['total_pages']}")
    print(f"🔢 Vector Dimensions: {report['total_dimensions']}")
    print(f"🔧 Extraction Method: {report['extraction_method']}")
    
    print("\n📊 Page Statistics:")
    for page in report['page_summaries'][:5]:  # Show first 5 pages
        print(f"  Page {page['page_number']}:")
        print(f"    - Content length: {page['content_length']} chars")
        print(f"    - Active coordinates: {page['active_coordinates']}/{report['total_dimensions']}")
        print(f"    - Vector density: {page['vector_density']:.2%}")
        print(f"    - Top terms: {', '.join(page['top_terms'][:3])}")
    
    print("\n🔝 Most Common Terms Across Document:")
    for term, info in report['most_common_terms'][:10]:
        print(f"  '{term}': appears on {info['page_count']} pages")


def main():
    """
    Main execution function
    """
    # PDF path - update this to your PDF location
    pdf_path = "DesignForTimeWellSpentAgentOrientedBots_forReview.pdf"
    
    # Check if PDF exists
    if not os.path.exists(pdf_path):
        print(f"❌ PDF not found: {pdf_path}")
        print("Please ensure the PDF is in the current directory or update the path.")
        return
    
    print("="*80)
    print("PDF TO TF-IDF VECTOR PROCESSING WITH FULL PROVENANCE")
    print("="*80)
    
    # Process PDF
    if DOCLING_AVAILABLE:
        chunks = process_pdf_with_docling(pdf_path)
    elif PYMUPDF_AVAILABLE:
        chunks = process_pdf_with_pymupdf(pdf_path)
    else:
        print("❌ No PDF processing library available. Please install docling or pymupdf.")
        return
    
    if not chunks:
        print("❌ No content extracted from PDF")
        return
    
    # Create TF-IDF vectors with provenance
    chunks, vectorizer, coordinate_dict = create_tfidf_vectors_with_provenance(chunks)
    
    # Generate provenance report
    report = generate_provenance_report(chunks, coordinate_dict)
    
    # Print summary
    print_provenance_summary(report)
    
    # Save results
    save_results(chunks, coordinate_dict, report)
    
    print("\n✅ Processing complete! Check the generated JSON files for full details.")
    
    return chunks, vectorizer, coordinate_dict, report


if __name__ == "__main__":
    chunks, vectorizer, coordinate_dict, report = main()
