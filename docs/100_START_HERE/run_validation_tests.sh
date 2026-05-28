#!/bin/bash
# Test Runner for TF-IDF Evidence Validation Scripts
# Location: docs/100_START_HERE/
# Usage: ./run_validation_tests.sh

set -e

echo "=========================================="
echo "TF-IDF EVIDENCE VALIDATION TEST RUNNER"
echo "=========================================="
echo ""

# Check we're in the right directory
if [ ! -f "tfidf_validation_system.py" ]; then
    echo "❌ Error: Must run from docs/100_START_HERE/ directory"
    echo "   Run: cd docs/100_START_HERE && ./run_validation_tests.sh"
    exit 1
fi

# Check Python dependencies
echo "🔍 Checking dependencies..."
python3 -c "import sklearn, numpy, pandas" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "❌ Missing dependencies. Installing..."
    pip3 install -r requirements.txt
fi
echo "✅ Dependencies OK"
echo ""

# Clean old results
echo "🧹 Cleaning old test results..."
rm -f validation_dashboard.json
rm -f pdf_chunks_pymupdf.json
rm -f pdf_coordinate_dictionary_pymupdf.json
rm -f pdf_provenance_report_pymupdf.json
echo "✅ Cleaned"
echo ""

# Test 1: TF-IDF Validation System (with sample data)
echo "=========================================="
echo "TEST 1: TF-IDF Validation System"
echo "=========================================="
echo "Running: python3 tfidf_validation_system.py"
echo ""
python3 tfidf_validation_system.py
TEST1_EXIT=$?
echo ""

if [ $TEST1_EXIT -eq 0 ]; then
    echo "✅ TEST 1 PASSED - validation_dashboard.json created"
else
    echo "❌ TEST 1 FAILED - Exit code: $TEST1_EXIT"
    exit 1
fi
echo ""

# Test 2: PDF Processing with PyMuPDF (requires PDF)
echo "=========================================="
echo "TEST 2: PDF Processing with PyMuPDF"
echo "=========================================="

if [ -f "DesignForTimeWellSpentAgentOrientedBots_forReview.pdf" ]; then
    echo "Running: python3 process_pdf_pymupdf.py"
    echo ""
    python3 process_pdf_pymupdf.py
    TEST2_EXIT=$?
    echo ""
    
    if [ $TEST2_EXIT -eq 0 ]; then
        echo "✅ TEST 2 PASSED - PDF processing artifacts created"
    else
        echo "❌ TEST 2 FAILED - Exit code: $TEST2_EXIT"
        exit 1
    fi
else
    echo "⚠️  TEST 2 SKIPPED - PDF file not found"
    echo "   (This is OK for basic validation testing)"
fi
echo ""

# Summary
echo "=========================================="
echo "TEST SUMMARY"
echo "=========================================="
echo ""
echo "Generated Artifacts:"
ls -lh validation_dashboard.json 2>/dev/null && echo "  ✅ validation_dashboard.json"
ls -lh pdf_chunks_pymupdf.json 2>/dev/null && echo "  ✅ pdf_chunks_pymupdf.json"
ls -lh pdf_coordinate_dictionary_pymupdf.json 2>/dev/null && echo "  ✅ pdf_coordinate_dictionary_pymupdf.json"
ls -lh pdf_provenance_report_pymupdf.json 2>/dev/null && echo "  ✅ pdf_provenance_report_pymupdf.json"
echo ""

echo "HTML Dashboards Available:"
echo "  📊 validation_dashboard.html - Main validation results"
echo "  🔍 interactive_vector_explorer.html - Vector analysis"
echo ""

# Open dashboards if on macOS
if [[ "$OSTYPE" == "darwin"* ]]; then
    echo "🚀 Opening dashboards in browser..."
    open validation_dashboard.html
    sleep 1
    open interactive_vector_explorer.html
else
    echo "📁 Open these files in your browser to review:"
    echo "   file://$(pwd)/validation_dashboard.html"
    echo "   file://$(pwd)/interactive_vector_explorer.html"
fi

echo ""
echo "✅ ALL TESTS PASSED"
echo ""
echo "Next Steps:"
echo "  1. Review validation_dashboard.html for validation results"
echo "  2. Review interactive_vector_explorer.html for vector analysis"
echo "  3. Check JSON files for programmatic access"
echo ""
