#!/bin/bash
# Quick test runner for HITL pipeline

echo "🧪 Running HITL Pipeline Tests"
echo "=============================="

# Create test directories
echo "📁 Creating test directories..."
mkdir -p watch_folders/{hitl_review,hitl_review_queue,hitl_review_rejected}
mkdir -p watch_folders/{hitl_rejected,hitl_failed,hitl_workshop,hitl_promotion_candidates}

# Clean existing test files
echo "🧹 Cleaning test files..."
find watch_folders -name "test_*.md" -type f -delete
find watch_folders -name "*_test_problem_*.md" -type f -delete
find watch_folders -name "*_errors.txt" -type f -delete
find watch_folders -name "*_rejection.txt" -type f -delete
find watch_folders -name "*_queue_note.txt" -type f -delete
find watch_folders -name "*_workshop_notes.txt" -type f -delete

# Run specific scenarios if provided
if [ "$1" ]; then
    echo "🎯 Running scenario: $1"
    behave tests/features/hitl_pipeline.feature -n "$1"
else
    echo "🏃 Running all HITL tests..."
    behave tests/features/hitl_pipeline.feature
fi

echo ""
echo "✅ Test run complete!"