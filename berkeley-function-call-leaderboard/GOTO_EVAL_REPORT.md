# 📊 GoTo Model Evaluation Report - BFCL v4

## Executive Summary

Model: **GoToCompany/gemma3-27b-sahabat-instruct**
Handler: OpenAI Completions (API-based)
Mode: Prompt mode (non-function-calling model)
Evaluation Date: 2025-11-17

---

## 🎯 Overall Results

| Metric | Value |
|--------|-------|
| **Average Accuracy** | **86.55%** |
| **Best Performing Category** | Live Parallel (93.75%) |
| **Weakest Category** | Live Multiple (73.12%) |
| **Total Test Cases Evaluated** | 2,377 |

---

## 📈 Detailed Results by Category

### Non-Live (Mock API) Categories

| Category | Accuracy | Test Cases | Notes |
|----------|----------|-----------|-------|
| **simple_python** | 95.00% | 400 | Standard Python functions - Excellent |
| **multiple** | 92.00% | 200 | Multiple function calls in one request |
| **parallel** | 92.50% | 200 | Parallel function execution |
| **parallel_multiple** | 91.00% | 200 | Parallel + Multiple combinations |
| **Non-Live Average** | **92.63%** | **1,000** | ✅ Highly Reliable |

### Live (Real API) Categories

| Category | Accuracy | Test Cases | Notes |
|----------|----------|-----------|-------|
| **live_simple** | 84.50% | 258 | Real API calls - simple case |
| **live_multiple** | 73.12% | 1,003 | Real API calls - multiple functions ⚠️ |
| **live_parallel** | 93.75% | 16 | Real API calls - parallel execution |
| **Live Average** | **83.79%** | **1,277** | ⚠️ Performance drop with live APIs |

---

## 🔍 Key Findings

### ✅ Strengths

1. **Excellent Non-Live Performance (92.63%)**
   - Consistently high accuracy across mock API scenarios
   - Reliable for standard tool-calling tasks
   - Good at handling complexity (parallel + multiple)

2. **Outstanding Parallel Execution**
   - live_parallel: 93.75%
   - parallel: 92.50%
   - Model excels at coordinating independent function calls

3. **Solid Multiple Function Handling**
   - multiple: 92.00%
   - parallel_multiple: 91.00%
   - Capable of orchestrating complex tool interactions

### ⚠️ Areas for Improvement

1. **Real API Performance Degradation**
   - Non-live avg: 92.63% vs Live avg: 83.79% (-8.84%)
   - This suggests issues with:
     - Error handling from real APIs
     - Retry logic
     - Response parsing from actual endpoints

2. **Live Multiple Functions (73.12%)**
   - Largest gap from expected performance
   - 1,003 test cases show consistent pattern
   - Likely issues:
     - Managing state across multiple API calls
     - Handling partial failures
     - Timeout handling

3. **Live Simple (84.50%)**
   - Still solid, but shows API reliability concerns
   - More challenging than mock scenarios

---

## 💡 Recommendations for Mentor Discussion

### 1. Model Strengths to Highlight
- ✅ 95% accuracy on standard Python tool-calling
- ✅ 92%+ consistency across multiple and parallel scenarios
- ✅ Excellent at logical reasoning for function selection

### 2. Areas Needing Work
- ⚠️ Real API integration and error handling
- ⚠️ Performance on complex live scenarios with multiple functions
- ⚠️ Latency and timeout management

### 3. Comparison Baseline
- Non-live categories show what model CAN do (92.63%)
- Live categories show production readiness (83.79%)
- Gap suggests: **API integration improvements needed**

### 4. Next Steps
- [ ] Investigate live_multiple failures (analyze error patterns)
- [ ] Implement better error recovery mechanisms
- [ ] Add logging for API interaction debugging
- [ ] Consider fine-tuning on real API scenarios

---

## 📁 Detailed Results Location

- **Overall Leaderboard**: `score/data_overall.csv`
- **Non-Live Details**: `score/data_non_live.csv`
- **Live API Details**: `score/data_live.csv`
- **Raw Responses**: `result/goto/{live,non_live}/BFCL_v4_*_result.json`

---

## 🚀 Reproduction Commands

### Generate Results
```bash
cd berkeley-function-call-leaderboard
source .venv/bin/activate

# For individual categories
bfcl generate --model goto --test-category simple_python
bfcl generate --model goto --test-category multiple
bfcl generate --model goto --test-category parallel
bfcl generate --model goto --test-category parallel_multiple
bfcl generate --model goto --test-category live_simple
bfcl generate --model goto --test-category live_multiple
bfcl generate --model goto --test-category live_parallel

# Or all at once (takes ~1.5 hours)
bfcl generate --model goto --test-category all
```

### Evaluate Results
```bash
bfcl evaluate --model goto --test-category simple_python,multiple,parallel,parallel_multiple,live_simple,live_multiple,live_parallel
```

### View Results
```bash
# CSV format
cat score/data_overall.csv
cat score/data_non_live.csv
cat score/data_live.csv

# JSON responses
ls -lah result/goto/*/
```

---

Generated: 2025-11-17
Model: GoTo (Sahabat AI by GoToCompany)
Framework: BFCL v4 (Berkeley Function Calling Leaderboard)
