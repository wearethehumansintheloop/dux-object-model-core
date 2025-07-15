Feature: Researcher extracts insights from user interviews
  As Maya, a UX Researcher
  I want to extract insights from Joel's GPU monitoring interview
  So that I can prove the $468K platform improvement opportunity to leadership

  Background:
    Given Maya has conducted a 45-minute interview with Joel about GPU management
    And Joel mentioned "I spend 30 minutes daily SSH-ing into nodes"
    And Maya has selected the "GPU Resource Optimization" Frame

  Scenario: Maya runs extraction on Joel's interview
    Given Maya has saved Joel's interview transcript as "joel_gpu_interview.md"
    When Maya runs the extraction command:
      """
      python magnets_frame_api.py \
        --frame_path frames/gpu_resource_optimization.md \
        --transcript joel_gpu_interview.md \
        --session_id joel_001
      """
    Then Maya sees "Extracting Problems related to GPU resource management..."
    And after 2 minutes, Maya sees "3 Problems extracted"
    And the Problems include Joel's daily 30-minute time waste
    And extracted files appear in "output/hitl_review/problems/"

  Scenario: Maya reviews extracted Problems for quality
    Given extraction has completed
    When Maya opens "output/hitl_review/problems/problem_gpu_monitor_001.json"
    Then Maya sees:
      """
      {
        "job_statement": {
          "user_scenario": "When I need to check GPU utilization",
          "user_enablement": "I want real-time visibility",
          "user_outcome": "So I don't waste 30 minutes daily"
        },
        "evidence_ids": ["data_001"],
        "confidence": 0.92
      }
      """
    And Maya thinks "Yes! This captures Joel's exact pain point"
    And Maya moves the file to "approved/" folder

  Scenario: Maya's extraction fails due to missing Core API
    Given Core API is not running
    When Maya runs the extraction command
    Then Maya sees error: "Failed to connect to Core API at http://localhost:8504"
    And Maya sees suggestion: "Run 'docker compose up core-api' first"
    And no partial extractions are saved
    And Maya knows exactly how to fix the issue

  Scenario: Maya extracts from multiple interviews in a batch
    Given Maya has 5 interview transcripts about GPU management
    When Maya runs extraction on all transcripts
    Then each transcript processes separately
    And Maya sees progress: "Processing interview 3 of 5..."
    And all extractions use the same GPU Optimization Frame
    And Maya can review all results in one HITL folder