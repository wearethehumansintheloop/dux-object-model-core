# DUX Object Model Pipeline: Handoff Package

**Date:** July 7, 2025
**Prepared By:** GitHub Copilot

---

## 1. Project Vision & Core Objective

The primary goal of this project is to build and refine a modular, agent-based DUX (Design User Experience) object extraction and synthesis pipeline. This pipeline transforms raw qualitative research data (transcripts, artifacts) into structured, validated, and evidence-backed DUX objects (Problems, Behaviors, Results, etc.).

A core principle of this initiative is to treat all components as source code—including prompts, schemas, and model configurations—to be version-controlled, tested, and managed with CI/CD and robust change management practices.

---

## 2. Summary of Work Completed

Over the recent development cycle, we have made significant progress in building the foundational components of the pipeline.

*   **Environment Configuration:**
    *   Confirmed a local Ollama LLM instance is running and operational.
    *   Established `llama3` as the default model for both language generation and embedding tasks.

*   **Core Pipeline Refactoring (`src/app/orchestrators/dux_processor.py`):**
    *   **Switched to Ollama Embeddings:** All embedding and semantic similarity calculations have been refactored to use `OllamaEmbeddings` via the `langchain_community` library, removing the dependency on `sentence-transformers`. This allows the entire pipeline to run on a local LLM.
    *   **Programmatic `fit_score` Calculation:** Implemented a system to programmatically calculate a `fit_score` for each extracted object. This score, based on the cosine similarity between the object's embedding and a "fit template" embedding, measures its alignment with the research goals.
    *   **Enforced Evidence-Backing:** The pipeline now ensures every extracted Problem, Behavior, and Result object is linked to a `Provenance` object. This `Provenance` object contains the specific quote from the transcript that serves as direct evidence, making all insights traceable.
    *   **"Teacher-Judge" Validation Mode:** A more rigorous, optional validation mode has been implemented. After an object is generated (by the "teacher" LLM), a second LLM call (the "judge") validates its accuracy and faithfulness against the source transcript. Objects that fail this check are routed for human review.
    *   **HITL Review & Success Criteria:**
        *   Objects with a `fit_score` below a configurable threshold (e.g., 0.7) are automatically saved to a separate directory for Human-in-the-Loop (HITL) review.
        *   The pipeline now evaluates each run against success criteria, flagging outputs that suggest over-extraction (>150 objects) or low yield (<25 objects).
        *   An "evidence density" metric (evidence items per hour of transcript) has been added to the summary logs to serve as a benchmark for tuning prompt and RAG effectiveness.

---

## 3. Current State & Key Artifacts

The project is composed of two main repositories: `dux-object-model-core` and `dux-research-platform`. The core logic resides in `dux-object-model-core`.

*   **`src/app/orchestrators/dux_processor.py`**: The main orchestrator containing the core pipeline logic described above.
*   **`scripts/test_pipeline.py`**: The primary script for executing an end-to-end run of the pipeline. **This is the main entry point for testing.**
*   **`object_definitions/`**: Contains the canonical JSON schemas for all DUX objects.
*   **`agent_prompts/`**: Contains the markdown-based prompt blueprints for each extraction agent.
*   **`test_data/`**: Contains sample data, including the `fit_template_gpu_management.md` fit template and the `joel_bella_gpu_management.json` sample transcript.
*   **`docs/DEV_BACKLOG.md`**: The official backlog for future development tasks.

---

## 4. Immediate Next Steps (Work in Progress)

The pipeline is functionally complete but is currently blocked by Python environment issues. The next developer's first priority should be to resolve these blockers.

*   **🔴 PRIORITY #1: Resolve `ModuleNotFoundError`**
    *   **Problem:** When running `scripts/test_pipeline.py`, the execution fails with a `ModuleNotFoundError`. This is caused by incorrect import paths between the `dux-object-model-core` and `dux-research-platform` projects.
    *   **Location of Errors:** The primary files involved are `scripts/test_pipeline.py` and `core/chains.py`.
    *   **Required Action:** Adjust the `sys.path` in `scripts/test_pipeline.py` and correct the import statements in the `core` directory to use the appropriate relative or absolute paths that allow the two projects to resolve each other's modules.

*   **🟡 PRIORITY #2: Complete the End-to-End Test Run**
    *   **Goal:** Successfully run the pipeline on the target transcript.
    *   **Transcript Path:** `/Users/njayanty/Projects/Upstream Contributions/prompt_Tests/20250706_bullextraction_test_100-1000/2024_Q2_UXDR-2879 Generative Study for Resource Optimization_UXDR_2879_P1_Cigna_undefined_DEIDENTIFIED.md`
    *   **Expected Outcome:** The script should run to completion, producing an `extraction_summary.json` and several `_objects.json` files in the `output` directory. The console should print the final summary JSON.

---

## 5. Future Work & Development Backlog

Once the pipeline is running, the following tasks from `docs/DEV_BACKLOG.md` should be prioritized:

*   **Implement a validation pipeline for agent prompts:**
    *   **Description:** Create an automated script to parse the example JSON within each agent prompt file and validate it against the corresponding schema.
    *   **Rationale:** This will prevent prompt drift and ensure agents are always trained on valid examples, improving system reliability. This should be integrated into a CI/CD check.

---

## 6. How to Run the Pipeline

To run the pipeline, follow these steps:

1.  **Start the Local LLM:**
    *   Ensure your Ollama server is running.
    *   Make sure the `llama3` model is pulled and available. You can check with `ollama list`.

2.  **Execute the Test Script:**
    *   Open a terminal in the `dux-object-model-core` project root.
    *   Run the following command:
        ```bash
        python3 scripts/test_pipeline.py
        ```

3.  **Review the Output:**
    *   If successful, the script will print "Processing complete." and the path to the results directory.
    *   The final summary JSON will be printed to the console.
    *   The output files will be located in the `/Users/njayanty/Projects/Upstream Contributions/shut_the_dux_up/dux-object-model-core/output/` directory, within a timestamped subfolder.
