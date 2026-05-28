# HITL Test Plan: TF-IDF Evidence Validation Scripts

**Test Date:** 2026-05-28  
**Tester:** Nick (imstilllearning)  
**Status:** 🟢 Ready for Human Review  

---

## Quick Start

```bash
# Navigate to test directory
cd docs/100_START_HERE

# Run test suite
./run_validation_tests.sh

# Dashboards will open automatically (macOS)
# Or open manually: validation_dashboard.html
```

---

## What You're Testing

**The closed-loop validation pattern** - scripts that validate research citations match source material using TF-IDF vector similarity.

**Why it matters:**
- These are the "validator" scripts in your semantic tuning architecture
- They stay "pure canon" and never bend to the Frame
- They prevent extractor/checker drift by sharing one source of truth

---

## Test Environment

**Location:** `docs/100_START_HERE/`

**Required Files:**
```
✅ tfidf_validation_system.py (main validator)
✅ process_pdf_pymupdf.py (PDF processor)
✅ validation_dashboard.html (results UI)
✅ interactive_vector_explorer.html (vector analysis UI)
✅ requirements.txt (dependencies)
✅ DesignForTimeWellSpentAgentOrientedBots_forReview.pdf (test PDF)
```

**Dependencies:**
- Python 3.x
- scikit-learn >= 1.0.0
- numpy >= 1.20.0
- pandas >= 1.3.0
- PyMuPDF >= 1.26.7

---

## Test Execution Steps

### 1. Pre-Test Checklist

- [ ] Navigate to `docs/100_START_HERE/`
- [ ] Verify Python 3.x is available: `python3 --version`
- [ ] Verify test PDF exists: `ls -lh DesignForTimeWellSpentAgentOrientedBots_forReview.pdf`

### 2. Run Test Suite

```bash
./run_validation_tests.sh
```

**Expected Output:**
```
==========================================
TF-IDF EVIDENCE VALIDATION TEST RUNNER
==========================================

🔍 Checking dependencies...
✅ Dependencies OK

🧹 Cleaning old test results...
✅ Cleaned

==========================================
TEST 1: TF-IDF Validation System
==========================================
Running: python3 tfidf_validation_system.py

TF-IDF VALIDATION SYSTEM
----------------------------------------

STEP 1: Creating sample PDF chunks
  ✓ Created 5 slide chunks

STEP 2: Converting chunks to TF-IDF vectors
  ✓ Vocabulary size: 100 terms

STEP 3: Processing test document
  ✓ Processed 12 highlight entries

STEP 4: Validating highlights
  ✓ Validation complete

STEP 5: Generating dashboard
  ✓ Dashboard data generated

✅ TEST 1 PASSED

==========================================
TEST 2: PDF Processing with PyMuPDF
==========================================
Running: python3 process_pdf_pymupdf.py

📄 Processing PDF with PyMuPDF
  Document has 6 pages
  ✅ Extracted 6 pages/chunks

🔢 Creating TF-IDF vectors with provenance...
  ✅ Created 100-dimensional vectors

✅ TEST 2 PASSED

==========================================
TEST SUMMARY
==========================================

✅ ALL TESTS PASSED

🚀 Opening dashboards in browser...
```

### 3. Review HTML Dashboards

**Dashboard 1: Validation Results** (`validation_dashboard.html`)

This dashboard shows citation validation results:

**What to look for:**
- ✅ **Summary Stats** - Total highlights, overall accuracy, status breakdown
- ✅ **Category Performance** - Accuracy by research category (Method, Concept, Technique, etc.)
- ✅ **Detailed Results** - Each citation with PASS/FAIL status and explanation
- ✅ **Similarity Scores** - Claimed vs. best match (should be high for PASS)
- ✅ **Common Terms** - Overlapping vocabulary between citation and source

**Expected Results (Sample Data):**
```
Total Highlights: 12
Overall Accuracy: 25-30% (intentionally low for testing)
PASS: 3-4 citations
FAIL: 7-8 citations
INVALID_SLIDE_NUMBER: 1 citation
```

**Quality Indicators:**
- 🟢 **PASS** - Similarity >= 50%, correct slide cited
- 🟡 **PASS_WITH_BETTER_MATCH** - Passes threshold but another slide matches better
- 🔴 **FAIL** - Similarity < 50%
- 🔴 **WRONG_CITATION** - High similarity but to different slide

---

**Dashboard 2: Vector Explorer** (`interactive_vector_explorer.html`)

This dashboard visualizes TF-IDF vectors:

**What to look for:**
- ✅ **Vector Heatmap** - Visual representation of active coordinates
- ✅ **Top Terms** - Highest-weighted terms per page/chunk
- ✅ **Coordinate Mapping** - Which words map to which vector positions
- ✅ **Page Comparison** - How different pages differ in vector space

**Quality Indicators:**
- Dense vectors (many active coordinates) = content-rich pages
- Sparse vectors (few active coordinates) = minimal text
- Common terms across pages = consistent vocabulary
- Unique terms = page-specific content

---

## Test Validation Criteria

### ✅ Test PASSES if:

1. **Test Runner Executes Successfully**
   - No Python errors
   - Both Test 1 and Test 2 complete
   - JSON artifacts generated

2. **Validation Dashboard Shows Expected Structure**
   - Summary stats display
   - Detailed results table loads
   - Pass/Fail status visible
   - Similarity scores show percentages

3. **Vector Explorer Shows Expected Structure**
   - Coordinate grid displays
   - Top terms list shows weighted values
   - Heatmap visualization renders

4. **JSON Files Are Valid**
   ```bash
   # Validate JSON syntax
   python3 -m json.tool validation_dashboard.json > /dev/null && echo "✅ Valid JSON"
   python3 -m json.tool pdf_chunks_pymupdf.json > /dev/null && echo "✅ Valid JSON"
   ```

5. **Provenance Chain Is Complete**
   - Each validation result has `claimed_slide`, `claimed_similarity`, `best_match_slide`
   - Each PDF chunk has `provenance.source_file`, `provenance.page_ref`
   - Coordinate dictionary has `coordinate_mapping` with page references

### ❌ Test FAILS if:

- Python import errors (missing dependencies)
- Scripts crash with exceptions
- No JSON files generated
- HTML dashboards don't load in browser
- Validation results missing required fields
- Similarity scores are all 0 or NaN

---

## Known Issues / Expected Behavior

### Low Accuracy (25-30%) is Expected
The sample data uses intentionally mismatched citations to test the validator's ability to detect wrong citations. **This is working as designed.**

### Some Citations Marked FAIL
The system is conservative - it requires 50%+ similarity to pass. Citations with weak term overlap will fail. **This is the desired behavior.**

### Vector Visualizations Show Sparse Patterns
Not all coordinates are active. Most pages use 20-40 out of 100 possible terms. **This is normal TF-IDF sparsity.**

---

## HITL Review Questions

After running tests and reviewing dashboards, answer:

1. **Did the validation report make sense?**
   - Could you understand which citations passed/failed?
   - Were the explanations clear?

2. **Did the similarity scores seem reasonable?**
   - Do high-similarity citations have matching content?
   - Do low-similarity citations look wrong?

3. **Is the provenance chain traceable?**
   - Can you trace a citation back to its source page?
   - Are the page references clear?

4. **Would you trust this validator for production use?**
   - Does it catch wrong citations?
   - Does it correctly validate good citations?

5. **What would make this better?**
   - More detailed explanations?
   - Better visualizations?
   - Different similarity threshold?

---

## Troubleshooting

### Issue: `python3: command not found`
**Fix:** Install Python 3 or use `python` instead of `python3`

### Issue: `ModuleNotFoundError: No module named 'sklearn'`
**Fix:** `pip3 install -r requirements.txt`

### Issue: `PDF not found`
**Fix:** Test 2 will skip automatically. Test 1 uses sample data and will still work.

### Issue: `Permission denied: ./run_validation_tests.sh`
**Fix:** `chmod +x run_validation_tests.sh`

### Issue: Dashboards don't open automatically
**Fix:** Open manually:
```bash
open validation_dashboard.html  # macOS
xdg-open validation_dashboard.html  # Linux
start validation_dashboard.html  # Windows
```

---

## Next Steps After HITL Review

1. **If Tests Pass:**
   - ✅ Mark validation scripts as production-ready
   - ✅ Package into `dux-validators` module
   - ✅ Wire to canonical CRD
   - ✅ Integrate into hitl-core pipeline

2. **If Tests Fail:**
   - Document failure mode
   - Debug root cause
   - Fix and re-run

3. **Feedback Loop:**
   - Note any UX issues in dashboards
   - Suggest improvements to similarity threshold
   - Identify missing features

---

## Sign-Off

**Tester Name:** _________________  
**Date:** _________________  
**Result:** [ ] PASS  [ ] FAIL  [ ] NEEDS REVISION  

**Notes:**
```


```

**Reviewed Artifacts:**
- [ ] validation_dashboard.html
- [ ] interactive_vector_explorer.html
- [ ] validation_dashboard.json
- [ ] pdf_chunks_pymupdf.json
- [ ] pdf_coordinate_dictionary_pymupdf.json
- [ ] pdf_provenance_report_pymupdf.json
