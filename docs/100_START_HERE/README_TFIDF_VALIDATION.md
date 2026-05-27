# TF-IDF Validation System for DUX

## Overview
This system provides **explainable vector matching** for validating research highlights against PDF source documents using TF-IDF vectors. Unlike dense embeddings, each of the 100 vector coordinates directly maps to a specific term, making validation completely transparent.

## Architecture

### 1. **PDF → Chunks → Vectors (Source of Truth)**
```
PDF Document → Docling → Slide Chunks → TF-IDF Vectors (100 dimensions)
```
- Each PDF slide becomes one chunk
- Each chunk gets a 100-dimensional TF-IDF vector
- Terms are ranked by importance across the corpus

### 2. **Test Document → Validation**
```
Markdown Table (Highlights + Citations) → Parse → Transform → Compare
```
- Highlights are transformed using the SAME fitted vectorizer
- Citations are validated against claimed slide numbers
- Mismatches are flagged for human review

## Key Features

### 🎯 100% Explainability
- **Each coordinate = specific term**: Coordinate 35 might be "neural networks"
- **Transparent weights**: See exact TF-IDF scores for each term
- **Clear provenance**: Track from highlight → slide → page → bounding box

### 🔍 Validation Statuses
- **PASS**: Highlight matches claimed slide (similarity ≥ threshold)
- **FAIL**: Poor match with claimed slide
- **WRONG_CITATION**: Better match exists on different slide
- **INVALID_SLIDE_NUMBER**: Referenced slide doesn't exist

### 📊 Dashboard Visualization
- **Vector heatmap**: 100-cell grid showing term weights
- **Term clouds**: Top contributing terms for each highlight
- **Similarity bars**: Visual representation of match strength
- **Provenance trails**: Complete citation validation chain

## Usage with Real Docling

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
pip install docling  # For real PDF processing
```

### Step 2: Modify for Docling Integration
```python
from docling.document_converter import DocumentConverter
from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import PdfPipelineOptions

def process_pdf(pdf_path):
    # Configure Docling
    pipeline_options = PdfPipelineOptions()
    pipeline_options.do_ocr = False  # Disable if not needed
    pipeline_options.do_table_structure = True
    
    # Convert PDF
    converter = DocumentConverter(
        pipeline_options=pipeline_options,
        input_format=InputFormat.PDF
    )
    
    result = converter.convert(pdf_path)
    
    # Extract chunks with full provenance
    chunks = []
    for page_num, page in enumerate(result.document.pages, start=1):
        chunk = {
            'slide_number': page_num,
            'content': page.export_to_markdown(),
            'docling_metadata': {
                'page_bbox': page.bbox,
                'tables': page.tables,
                'pictures': page.pictures,
                'hierarchical_structure': page.get_hierarchy()
            }
        }
        chunks.append(chunk)
    
    return chunks
```

### Step 3: Run Validation
```python
# Process source PDF
chunks = process_pdf("research_presentation.pdf")
chunks, vectorizer = process_pdf_to_chunk_vectors(chunks)

# Load test document
test_markdown = load_markdown_highlights("highlights.md")
test_entries = process_test_document(test_markdown, vectorizer)

# Validate
results = validate_highlights_against_chunks(test_entries, chunks)
```

## Test Document Format

Your markdown test document should follow this format:

```markdown
| Highlight | Citation | Category |
|-----------|----------|----------|
| Key finding about user behavior | Slide 3, Page 3 | Finding |
| Method X was used for analysis | Slide 7, Page 7 | Method |
| 85% of users preferred option A | Slide 12, Page 12 | Metric |
```

## Validation Thresholds

### Default Settings
- **Similarity threshold**: 0.5 (50% match required)
- **Vocabulary size**: 100 terms (top TF-IDF features)
- **N-gram range**: (1, 2) for unigrams and bigrams

### Adjusting for Your Domain
```python
vectorizer = TfidfVectorizer(
    max_features=100,      # Increase for more granularity
    ngram_range=(1, 3),    # Include trigrams for technical domains
    min_df=1,              # Include rare terms for small corpora
    max_df=0.95,           # Exclude too-common terms
    stop_words='english',  # Remove for technical content
)
```

## Interpreting Results

### Similarity Scores
- **> 0.85**: Strong match - high confidence
- **0.5 - 0.85**: Moderate match - review recommended
- **< 0.5**: Weak match - likely incorrect citation

### Common Issues
1. **Low similarity across all highlights**: Vocabulary mismatch between source and test
2. **Wrong citations**: Highlights matching different slides than claimed
3. **Missing terms**: Important domain terms not in top 100 features

## Dashboard Features

### Load Results
1. Run `python3 tfidf_validation_system.py`
2. Open `validation_dashboard.html`
3. Load `validation_dashboard.json`

### Visual Elements
- **Overall accuracy gauge**: Percentage of validated highlights
- **Status breakdown**: Distribution of PASS/FAIL/WRONG_CITATION
- **Category performance**: Accuracy by highlight category
- **Vector visualization**: 100-cell grid with hover details
- **Term clouds**: Weighted term display for each highlight

## Integration with DUX Workflow

### 1. Research Protocol → PDF
```
UX Research Protocol → Presentation → PDF Export
```

### 2. PDF → Validated Chunks
```
PDF → Docling → Chunks → TF-IDF Vectors → Validation
```

### 3. Human-in-the-Loop Review
```
Failed Validations → HITL Review → Corrected Citations → Re-validation
```

### 4. Canonical Storage
```
Validated Chunks → Evergreen Feature Store → Graph Database
```

## Advanced Features

### Multi-Document Validation
```python
# Process multiple PDFs
all_chunks = []
for pdf in pdf_files:
    chunks = process_real_pdf(pdf)
    all_chunks.extend(chunks)

# Create unified vectorizer
all_chunks, vectorizer = process_pdf_to_chunk_vectors(all_chunks)
```

### Cross-Study Synthesis
```python
# Validate highlights across multiple studies
study_results = {}
for study_id, study_chunks in studies.items():
    results = validate_highlights_against_chunks(
        test_entries, 
        study_chunks[study_id]
    )
    study_results[study_id] = results
```

## Troubleshooting

### Issue: Low similarity scores
**Solution**: Adjust vocabulary size or n-gram range

### Issue: Missing domain terms
**Solution**: Remove stop words or use custom vocabulary

### Issue: Inconsistent citations
**Solution**: Standardize citation format in test documents

## Next Steps

1. **Integrate with Docling**: Replace simulated chunks with real PDF processing
2. **Add picture grounding**: Validate visual element references
3. **Implement table validation**: Check table-specific citations
4. **Build API endpoint**: Create REST API for validation service
5. **Connect to Evergreen**: Store validated chunks in feature store

## Contact
For questions about the DUX framework: nicholasjayantylearnsatgmail.com
