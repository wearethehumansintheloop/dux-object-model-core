"""
TF-IDF Validation System for PDF Chunks vs Markdown Highlights
Complete working example with sample data
"""

import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from typing import List, Dict, Tuple, Any
import json
from datetime import datetime
import re


# ============================================================================
# PART 1: PDF CHUNK PROCESSING (Simulated Docling Output)
# ============================================================================

def create_sample_pdf_chunks() -> List[Dict]:
    """
    Simulate Docling output: PDF slides converted to chunks
    In production, this would use actual Docling library
    """
    chunks = [
        {
            'slide_number': 1,
            'content': """
                Introduction to Machine Learning
                This presentation covers fundamental concepts of ML including
                supervised learning, unsupervised learning, and reinforcement learning.
                We will explore neural networks, decision trees, and clustering algorithms.
            """,
            'docling_metadata': {
                'page_bbox': {'l': 0, 't': 0, 'r': 1024, 'b': 768},
                'extraction_confidence': 0.98
            }
        },
        {
            'slide_number': 2,
            'content': """
                Supervised Learning Methods
                Classification and regression are the two main types of supervised learning.
                Common algorithms include linear regression, logistic regression,
                support vector machines, and random forests. Training requires labeled data.
            """,
            'docling_metadata': {
                'page_bbox': {'l': 0, 't': 0, 'r': 1024, 'b': 768},
                'extraction_confidence': 0.97
            }
        },
        {
            'slide_number': 3,
            'content': """
                Neural Network Architecture
                Deep learning uses multiple layers of neurons. Key components include
                input layer, hidden layers, output layer, activation functions,
                backpropagation algorithm, and gradient descent optimization.
                Convolutional networks excel at image processing tasks.
            """,
            'docling_metadata': {
                'page_bbox': {'l': 0, 't': 0, 'r': 1024, 'b': 768},
                'extraction_confidence': 0.99
            }
        },
        {
            'slide_number': 4,
            'content': """
                Data Preprocessing Techniques
                Feature scaling, normalization, handling missing values, encoding categorical
                variables, feature selection, dimensionality reduction using PCA.
                Data quality directly impacts model performance and accuracy.
            """,
            'docling_metadata': {
                'page_bbox': {'l': 0, 't': 0, 'r': 1024, 'b': 768},
                'extraction_confidence': 0.96
            }
        },
        {
            'slide_number': 5,
            'content': """
                Model Evaluation Metrics
                Accuracy, precision, recall, F1-score for classification tasks.
                Mean squared error, mean absolute error, R-squared for regression.
                Cross-validation techniques prevent overfitting. Confusion matrix
                provides detailed performance breakdown.
            """,
            'docling_metadata': {
                'page_bbox': {'l': 0, 't': 0, 'r': 1024, 'b': 768},
                'extraction_confidence': 0.98
            }
        }
    ]
    return chunks


def process_pdf_to_chunk_vectors(chunks: List[Dict]) -> Tuple[List[Dict], TfidfVectorizer]:
    """
    Convert PDF chunks to TF-IDF vectors
    """
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
        token_pattern=r'\b[a-z]{2,}\b'  # Only words with 2+ letters
    )
    
    # Fit and transform chunks
    tfidf_matrix = vectorizer.fit_transform(chunk_texts)
    feature_names = vectorizer.get_feature_names_out()
    
    # Attach vectors and feature info to chunks
    for idx, chunk in enumerate(chunks):
        vector = tfidf_matrix[idx].toarray()[0]
        chunk['vector'] = vector
        chunk['feature_names'] = feature_names
        
        # Extract non-zero features for explainability
        non_zero_indices = np.where(vector > 0)[0]
        chunk['active_terms'] = [
            {
                'term': feature_names[i],
                'weight': float(vector[i]),
                'coordinate': int(i)
            }
            for i in non_zero_indices
        ]
        chunk['active_terms'].sort(key=lambda x: x['weight'], reverse=True)
    
    return chunks, vectorizer


# ============================================================================
# PART 2: TEST DOCUMENT PROCESSING (Markdown Table with Citations)
# ============================================================================

def create_sample_test_document() -> str:
    """
    Create a sample markdown table with highlights and citations
    """
    return """
| Highlight | Citation | Category |
|-----------|----------|----------|
| Neural networks use backpropagation and gradient descent for optimization | Slide 3 | Method |
| Supervised learning includes classification and regression tasks | Slide 2 | Concept |
| Feature scaling and normalization are critical preprocessing steps | Slide 4 | Technique |
| Confusion matrix helps evaluate classification performance | Slide 5 | Metric |
| Random forests are ensemble learning methods | Slide 2 | Algorithm |
| Deep learning requires multiple hidden layers | Slide 3 | Architecture |
| Cross-validation prevents model overfitting | Slide 5 | Validation |
| PCA is used for dimensionality reduction | Slide 4 | Technique |
| Unsupervised learning includes clustering algorithms | Slide 1 | Concept |
| Mean squared error measures regression performance | Slide 5 | Metric |
| Support vector machines can handle non-linear data | Slide 7 | Algorithm |
| Convolutional networks are designed for image processing | Slide 3 | Application |
"""


def parse_markdown_table(markdown_content: str) -> List[Dict]:
    """
    Parse markdown table into structured data
    """
    lines = markdown_content.strip().split('\n')
    highlights = []
    
    for line in lines[2:]:  # Skip header and separator
        if '|' in line:
            parts = [p.strip() for p in line.split('|')[1:-1]]  # Remove empty first/last
            if len(parts) >= 3:
                highlights.append({
                    'Highlight': parts[0],
                    'Citation': parts[1],
                    'Category': parts[2]
                })
    
    return highlights


def parse_citation(citation: str) -> Dict:
    """
    Extract slide/page number from citation
    """
    # Match patterns like "Slide 3", "Page 3", "Slide 3, Page 3"
    slide_match = re.search(r'Slide\s+(\d+)', citation, re.IGNORECASE)
    page_match = re.search(r'Page\s+(\d+)', citation, re.IGNORECASE)
    
    return {
        'slide_number': int(slide_match.group(1)) if slide_match else None,
        'page_number': int(page_match.group(1)) if page_match else None,
        'raw_citation': citation
    }


def process_test_document(markdown_content: str, fitted_vectorizer: TfidfVectorizer) -> List[Dict]:
    """
    Process test document highlights into vectors
    """
    highlights = parse_markdown_table(markdown_content)
    test_entries = []
    
    for highlight in highlights:
        citation_info = parse_citation(highlight['Citation'])
        
        # Transform highlight text using fitted vectorizer
        highlight_vector = fitted_vectorizer.transform([highlight['Highlight']]).toarray()[0]
        
        # Extract non-zero terms
        feature_names = fitted_vectorizer.get_feature_names_out()
        non_zero_indices = np.where(highlight_vector > 0)[0]
        non_zero_terms = [
            {
                'term': feature_names[i],
                'weight': float(highlight_vector[i]),
                'coordinate': int(i)
            }
            for i in non_zero_indices
        ]
        non_zero_terms.sort(key=lambda x: x['weight'], reverse=True)
        
        test_entry = {
            'highlight_text': highlight['Highlight'],
            'claimed_slide': citation_info['slide_number'],
            'category': highlight.get('Category', 'Unknown'),
            'vector': highlight_vector,
            'non_zero_terms': non_zero_terms
        }
        test_entries.append(test_entry)
    
    return test_entries


# ============================================================================
# PART 3: VALIDATION LOGIC
# ============================================================================

def calculate_term_overlap(test_entry: Dict, chunk: Dict) -> Dict:
    """
    Calculate detailed term overlap between highlight and chunk
    """
    test_terms = {t['term']: t['weight'] for t in test_entry['non_zero_terms']}
    chunk_terms = {t['term']: t['weight'] for t in chunk['active_terms']}
    
    common_terms = set(test_terms.keys()) & set(chunk_terms.keys())
    
    overlap_details = {
        'common_terms': list(common_terms),
        'common_term_count': len(common_terms),
        'test_unique_terms': list(set(test_terms.keys()) - common_terms),
        'chunk_unique_terms': list(set(chunk_terms.keys()) - common_terms)[:10],  # Limit for display
        'weighted_overlap': sum(test_terms[t] * chunk_terms[t] for t in common_terms) if common_terms else 0
    }
    
    return overlap_details


def generate_explanation(test_entry: Dict, chunk: Dict, similarity: float) -> str:
    """
    Generate human-readable explanation for validation result
    """
    overlap = calculate_term_overlap(test_entry, chunk)
    
    if similarity >= 0.85:
        explanation = f"Strong match (similarity: {similarity:.3f}). "
        explanation += f"Found {overlap['common_term_count']} common terms including: "
        explanation += f"{', '.join(overlap['common_terms'][:5])}"
    elif similarity >= 0.5:
        explanation = f"Moderate match (similarity: {similarity:.3f}). "
        explanation += f"Found {overlap['common_term_count']} common terms. "
        if overlap['test_unique_terms']:
            explanation += f"Highlight contains unique terms: {', '.join(overlap['test_unique_terms'][:3])}"
    else:
        explanation = f"Weak match (similarity: {similarity:.3f}). "
        explanation += f"Only {overlap['common_term_count']} common terms. "
        explanation += "Consider reviewing the citation."
    
    return explanation


def validate_highlights_against_chunks(
    test_entries: List[Dict], 
    slide_chunks: List[Dict], 
    similarity_threshold: float = 0.5
) -> List[Dict]:
    """
    Validate that highlights match their cited slide chunks
    """
    validation_results = []
    
    for test_entry in test_entries:
        claimed_slide = test_entry['claimed_slide']
        
        if claimed_slide and claimed_slide <= len(slide_chunks):
            claimed_chunk = slide_chunks[claimed_slide - 1]
            
            # Calculate similarity with claimed chunk
            similarity = cosine_similarity(
                test_entry['vector'].reshape(1, -1),
                claimed_chunk['vector'].reshape(1, -1)
            )[0][0]
            
            # Find best matching chunk
            all_similarities = []
            for idx, chunk in enumerate(slide_chunks):
                sim = cosine_similarity(
                    test_entry['vector'].reshape(1, -1),
                    chunk['vector'].reshape(1, -1)
                )[0][0]
                all_similarities.append({
                    'slide': idx + 1,
                    'similarity': float(sim)
                })
            
            best_match = max(all_similarities, key=lambda x: x['similarity'])
            
            # Determine validation status
            if similarity >= similarity_threshold:
                if best_match['slide'] == claimed_slide:
                    validation_status = 'PASS'
                else:
                    validation_status = 'PASS_WITH_BETTER_MATCH'
            else:
                if best_match['similarity'] >= similarity_threshold:
                    validation_status = 'WRONG_CITATION'
                else:
                    validation_status = 'FAIL'
            
            result = {
                'highlight': test_entry['highlight_text'],
                'category': test_entry['category'],
                'claimed_slide': claimed_slide,
                'claimed_similarity': float(similarity),
                'best_match_slide': best_match['slide'],
                'best_match_similarity': best_match['similarity'],
                'validation_status': validation_status,
                'explanation': generate_explanation(test_entry, claimed_chunk, similarity),
                'term_overlap': calculate_term_overlap(test_entry, claimed_chunk),
                'top_highlight_terms': test_entry['non_zero_terms'][:5]
            }
        else:
            result = {
                'highlight': test_entry['highlight_text'],
                'category': test_entry['category'],
                'claimed_slide': claimed_slide,
                'validation_status': 'INVALID_SLIDE_NUMBER',
                'explanation': f"Slide {claimed_slide} does not exist (document has {len(slide_chunks)} slides)"
            }
        
        validation_results.append(result)
    
    return validation_results


# ============================================================================
# PART 4: DASHBOARD DATA GENERATION
# ============================================================================

def generate_validation_dashboard(
    validation_results: List[Dict], 
    slide_chunks: List[Dict], 
    test_entries: List[Dict]
) -> Dict:
    """
    Generate comprehensive dashboard data for visualization
    """
    # Calculate summary statistics
    status_counts = {}
    for result in validation_results:
        status = result['validation_status']
        status_counts[status] = status_counts.get(status, 0) + 1
    
    # Calculate accuracy by category
    category_stats = {}
    for result in validation_results:
        category = result.get('category', 'Unknown')
        if category not in category_stats:
            category_stats[category] = {'total': 0, 'passed': 0}
        category_stats[category]['total'] += 1
        if result['validation_status'] in ['PASS', 'PASS_WITH_BETTER_MATCH']:
            category_stats[category]['passed'] += 1
    
    # Prepare vector visualization data
    vector_explanations = []
    for result, test_entry in zip(validation_results, test_entries):
        # Create coordinate map for visualization
        coordinate_map = []
        for i in range(100):
            value = float(test_entry['vector'][i])
            if value > 0:
                # Find the term for this coordinate
                term = None
                for t in test_entry['non_zero_terms']:
                    if t['coordinate'] == i:
                        term = t['term']
                        break
                coordinate_map.append({
                    'coordinate': i,
                    'value': value,
                    'term': term,
                    'is_active': True
                })
            else:
                coordinate_map.append({
                    'coordinate': i,
                    'value': 0,
                    'term': None,
                    'is_active': False
                })
        
        vector_explanations.append({
            'highlight': result['highlight'],
            'validation_status': result['validation_status'],
            'coordinate_map': coordinate_map,
            'top_terms': test_entry['non_zero_terms'][:10]
        })
    
    dashboard_data = {
        'summary': {
            'total_highlights': len(validation_results),
            'status_breakdown': status_counts,
            'overall_accuracy': sum(1 for r in validation_results 
                                   if r['validation_status'] in ['PASS', 'PASS_WITH_BETTER_MATCH']) / len(validation_results),
            'category_stats': category_stats
        },
        'detailed_results': validation_results,
        'vector_explanations': vector_explanations,
        'slide_coverage': {
            'total_slides': len(slide_chunks),
            'referenced_slides': len(set(r['claimed_slide'] for r in validation_results if r.get('claimed_slide'))),
            'slide_hit_map': {}
        },
        'timestamp': datetime.now().isoformat()
    }
    
    # Calculate slide hit map
    for result in validation_results:
        if result.get('claimed_slide'):
            slide = result['claimed_slide']
            if slide not in dashboard_data['slide_coverage']['slide_hit_map']:
                dashboard_data['slide_coverage']['slide_hit_map'][slide] = 0
            dashboard_data['slide_coverage']['slide_hit_map'][slide] += 1
    
    return dashboard_data


def print_validation_report(dashboard_data: Dict):
    """
    Print a formatted validation report with improved readability
    """
    # Use simple separators for better readability
    print("\n")
    print("TF-IDF VALIDATION REPORT")
    print("-" * 50)
    
    summary = dashboard_data['summary']
    print(f"\nTotal Highlights Validated: {summary['total_highlights']}")
    print(f"Overall Accuracy: {summary['overall_accuracy']:.1%}")
    
    print("\nSTATUS BREAKDOWN:")
    for status, count in summary['status_breakdown'].items():
        # Use cleaner status names
        status_display = status.replace('_', ' ').title()
        print(f"  • {status_display}: {count}")
    
    print("\nACCURACY BY CATEGORY:")
    for category, stats in summary['category_stats'].items():
        accuracy = stats['passed'] / stats['total'] if stats['total'] > 0 else 0
        print(f"  • {category}: {stats['passed']}/{stats['total']} ({accuracy:.1%})")
    
    print("\n")
    print("DETAILED VALIDATION RESULTS")
    print("-" * 50)
    
    for idx, result in enumerate(dashboard_data['detailed_results'], 1):
        # Use cleaner status display
        status_display = result['validation_status'].replace('_', ' ').title()
        
        print(f"\n[{idx}] STATUS: {status_display}")
        
        # Truncate long highlights more gracefully
        highlight = result['highlight']
        if len(highlight) > 80:
            highlight = highlight[:77] + "..."
        print(f"    Highlight: {highlight}")
        
        print(f"    Category: {result['category']}")
        print(f"    Claimed Slide: {result['claimed_slide']}")
        
        if 'claimed_similarity' in result:
            # Format similarity scores more clearly
            sim_score = result['claimed_similarity']
            best_sim = result['best_match_similarity']
            print(f"    Similarity Score: {sim_score:.1%}")
            print(f"    Best Match: Slide {result['best_match_slide']} (score: {best_sim:.1%})")
        
        print(f"    Explanation: {result['explanation']}")
        
        if 'term_overlap' in result and result['term_overlap']['common_terms']:
            terms = ', '.join(result['term_overlap']['common_terms'][:5])
            print(f"    Common Terms: {terms}")


def export_dashboard_json(dashboard_data: Dict, filename: str = "validation_dashboard.json"):
    """
    Export dashboard data to JSON for visualization
    """
    # Convert numpy arrays to lists for JSON serialization
    def convert_to_serializable(obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        elif isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, dict):
            return {k: convert_to_serializable(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [convert_to_serializable(item) for item in obj]
        return obj
    
    serializable_data = convert_to_serializable(dashboard_data)
    
    with open(filename, 'w') as f:
        json.dump(serializable_data, f, indent=2)
    
    print(f"\nDashboard data exported to {filename}")


# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    """
    Run the complete TF-IDF validation pipeline
    """
    print("\nTF-IDF VALIDATION SYSTEM")
    print("-" * 40)
    
    # Step 1: Create sample PDF chunks (simulating Docling output)
    print("\nSTEP 1: Creating sample PDF chunks")
    chunks = create_sample_pdf_chunks()
    print(f"  ✓ Created {len(chunks)} slide chunks")
    
    # Step 2: Process chunks to vectors
    print("\nSTEP 2: Converting chunks to TF-IDF vectors")
    chunks, vectorizer = process_pdf_to_chunk_vectors(chunks)
    vocab_size = len(vectorizer.get_feature_names_out())
    print(f"  ✓ Vocabulary size: {vocab_size} terms")
    
    # Show sample terms in a cleaner format
    sample_terms = list(vectorizer.get_feature_names_out()[:5])
    terms_str = ', '.join(f'"{term}"' for term in sample_terms)
    print(f"  ✓ Sample terms: {terms_str}...")
    
    # Step 3: Create and process test document
    print("\nSTEP 3: Processing test document")
    test_markdown = create_sample_test_document()
    test_entries = process_test_document(test_markdown, vectorizer)
    print(f"  ✓ Processed {len(test_entries)} highlight entries")
    
    # Step 4: Validate highlights against chunks
    print("\nSTEP 4: Validating highlights")
    validation_results = validate_highlights_against_chunks(test_entries, chunks)
    print(f"  ✓ Validation complete")
    
    # Step 5: Generate dashboard data
    print("\nSTEP 5: Generating dashboard")
    dashboard_data = generate_validation_dashboard(validation_results, chunks, test_entries)
    print(f"  ✓ Dashboard data generated")
    
    # Step 6: Print report
    print_validation_report(dashboard_data)
    
    # Step 7: Export for visualization
    export_dashboard_json(dashboard_data)
    
    # Show sample vector explanation with cleaner formatting
    print("\n")
    print("SAMPLE VECTOR EXPLANATION")
    print("-" * 40)
    
    sample_explanation = dashboard_data['vector_explanations'][0]
    
    # Clean up the highlight display
    highlight_text = sample_explanation['highlight']
    if len(highlight_text) > 60:
        highlight_text = highlight_text[:57] + "..."
    
    # Clean up status display
    status = sample_explanation['validation_status'].replace('_', ' ').title()
    
    print(f"\nHighlight: {highlight_text}")
    print(f"Status: {status}")
    print("\nTop Contributing Terms:")
    
    for i, term in enumerate(sample_explanation['top_terms'][:5], 1):
        weight_pct = term['weight'] * 100
        print(f"  {i}. \"{term['term']}\" (weight: {weight_pct:.1f}%)")
    
    return dashboard_data, chunks, test_entries, vectorizer


if __name__ == "__main__":
    dashboard_data, chunks, test_entries, vectorizer = main()
