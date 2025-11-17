#!/bin/bash

# Comprehensive evaluation script untuk model goto

source /Users/dzulfaqoralidipangegara/Documents/GitHub/tool-calling-bfcl/berkeley-function-call-leaderboard/.venv/bin/activate

cd /Users/dzulfaqoralidipangegara/Documents/GitHub/tool-calling-bfcl/berkeley-function-call-leaderboard

echo "=================================="
echo "🚀 BFCL Comprehensive Evaluation"
echo "=================================="
echo ""

# Categories untuk tool-calling evaluation
CATEGORIES=(
    "simple_python"
    "multiple"
    "parallel"
    "parallel_multiple"
    "live_simple"
    "live_multiple"
    "live_parallel"
)

echo "📊 Evaluating model: goto"
echo "📋 Categories: ${CATEGORIES[@]}"
echo ""

# Run evaluation untuk semua kategori
for category in "${CATEGORIES[@]}"; do
    echo "🔍 Evaluating category: $category"
    bfcl evaluate --model goto --test-category "$category"
    echo "✅ Completed: $category"
    echo ""
done

echo "=================================="
echo "✨ Evaluation selesai!"
echo "📁 Results tersimpan di: score/data_*.csv"
echo "=================================="
