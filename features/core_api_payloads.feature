Feature: Core API Request and Response Payloads
  As a Platform Engineer building the extraction pipeline
  I want to define the payload structure for Core API integration
  So that our orchestration system can request Frame-aware prompt canvases

  Background:
    Given the Core API generates Frame-aware agent prompts
    And we're extracting Problems from Joel's GPU monitoring scenario
    And the Frame provides specific context for extraction

  Scenario: POST request payload for Problem object generation
    Given I need to extract Problems from Joel's interview
    When I POST to /api/objects/problem/generate
    Then my request payload should be:
      """
      {
        "frame_type": "resource_optimization",
        "frame_id": "frame_gpu_lifecycle_001",
        "session_metadata": {
          "session_id": "joel_gpu_interview_001",
          "session_type": "user_interview",
          "participant": "Joel Chen",
          "role": "Platform Engineer",
          "date": "2025-01-08",
          "duration_minutes": 45
        },
        "extraction_context": {
          "focus_area": "GPU resource management inefficiencies",
          "key_challenges": [
            "Manual checking of GPU utilization",
            "No visibility into idle resources",
            "Time wasted on resource monitoring"
          ],
          "evidence_snippets": [
            "I spend like 30 minutes every day just SSH-ing into nodes",
            "We have expensive GPU nodes just sitting idle",
            "I have no easy way to know what's actually being used"
          ]
        },
        "job_statement_hints": {
          "user_scenario": [
            "When Joel needs to check GPU utilization across the cluster",
            "When Joel wants to identify idle GPU resources",
            "When Joel needs to reclaim underutilized GPUs"
          ],
          "user_enablement": [
            "Automated GPU monitoring without manual SSH",
            "Real-time visibility dashboard for all GPUs",
            "Proactive alerts for idle resources"
          ],
          "user_outcome": [
            "Save 30 minutes daily on manual checks",
            "Reduce GPU idle time by 50%",
            "Improve cluster utilization from 65% to 80%"
          ]
        },
        "agent_configuration": {
          "extraction_mode": "evidence_based",
          "confidence_threshold": 0.8,
          "include_synthetic_enrichment": true,
          "max_problems_to_extract": 5
        },
        "response_format": {
          "return_as": "docling_document",
          "include_sections": [
            "frame_context",
            "canonical_schema",
            "extraction_prompts",
            "validation_rules",
            "example_problems"
          ]
        }
      }
      """
    And the request headers should include:
      | Header | Value |
      | Content-Type | application/json |
      | X-Frame-Version | 1.0 |
      | X-Request-ID | Extract from correlation ID |

  Scenario: Expected response structure from Core API
    Given Core API processes my Frame-aware request
    When I receive the response
    Then the response should be structured as:
      """
      {
        "status": "success",
        "generated_at": "2025-01-08T10:30:00Z",
        "frame_validation": {
          "frame_compatibility": "valid",
          "canonical_constraints": "satisfied",
          "warnings": []
        },
        "docling_document": {
          "metadata": {
            "object_type": "problem",
            "canonical_version": "9.6",
            "frame_context": "resource_optimization",
            "generation_id": "prob_gen_20250108_103000"
          },
          "prompt_canvas": {
            "extraction_prompt": "You are an expert Problem extractor for GPU resource optimization challenges...",
            "frame_specific_instructions": "Focus on inefficiencies in GPU monitoring and utilization...",
            "canonical_schema": {
              "job_statement": {
                "type": "object",
                "properties": {
                  "user_scenario": {"type": "object", "properties": {"value": "string", "source": "string"}},
                  "user_enablement": {"type": "object", "properties": {"value": "string", "source": "string"}},
                  "user_outcome": {"type": "object", "properties": {"value": "string", "source": "string"}}
                }
              },
              "evidence_ids": {"type": "array", "items": {"type": "string"}},
              "confidence_score": {"type": "number", "minimum": 0, "maximum": 1}
            },
            "frame_examples": [
              {
                "job_statement": {
                  "user_scenario": {
                    "value": "When I need to check which GPUs are being utilized",
                    "source": "evidence"
                  },
                  "user_enablement": {
                    "value": "I want a real-time dashboard showing all GPU status",
                    "source": "synthetic"
                  },
                  "user_outcome": {
                    "value": "So I can make informed decisions about resource allocation",
                    "source": "synthetic"
                  }
                },
                "evidence_ids": ["data_001", "data_002"],
                "confidence_score": 0.92
              }
            ],
            "validation_rules": [
              "job_statement must reference specific GPU/resource challenges",
              "evidence_ids must link to Session data",
              "confidence_score reflects evidence support"
            ],
            "extraction_guidelines": {
              "look_for": [
                "Time wasted on manual tasks",
                "Visibility gaps in resource monitoring",
                "Inefficiencies in current workflows"
              ],
              "avoid": [
                "Generic infrastructure problems",
                "Non-GPU related issues",
                "Organizational policy problems"
              ],
              "enrichment_hints": [
                "Quantify time savings where possible",
                "Link problems to specific user quotes",
                "Consider downstream impacts of problems"
              ]
            }
          },
          "agent_templates": {
            "archivist_enhancement": "When reviewing transcripts, pay special attention to quantified pain points like '30 minutes daily'...",
            "problem_extraction": "Extract Problems that directly relate to GPU lifecycle management and monitoring efficiency...",
            "evidence_linking": "Ensure each Problem traces back to specific quotes or observations in the transcript..."
          }
        },
        "usage_metrics": {
          "tokens_generated": 2847,
          "cache_hit": false,
          "generation_time_ms": 340,
          "llm_calls": 1
        }
      }
      """

  Scenario: Payload for multi-Frame problem extraction
    Given Joel's scenario intersects multiple Frames
    When I need Problems across cost, performance, and developer experience
    Then I POST with multi-Frame context:
      """
      {
        "frame_type": "multi_frame_extraction",
        "frames": [
          {
            "frame_id": "frame_cost_optimization_001",
            "weight": 0.3,
            "focus": "GPU idle time costs"
          },
          {
            "frame_id": "frame_performance_monitoring_001", 
            "weight": 0.5,
            "focus": "Resource utilization visibility"
          },
          {
            "frame_id": "frame_developer_experience_001",
            "weight": 0.2,
            "focus": "Platform engineer workflow"
          }
        ],
        "magnetic_charge_calculation": "weighted_intersection",
        "session_metadata": {
          "session_id": "joel_gpu_interview_001",
          "convergence_expected": true
        }
      }
      """
    And Core returns prompts aware of all Frame intersections
    And extraction focuses on high "magnetic charge" evidence

  Scenario: Minimal payload for quick extraction
    Given I need rapid Problem extraction
    When I send minimal required fields
    Then the POST payload can be:
      """
      {
        "frame_type": "general_problem_extraction",
        "session_metadata": {
          "session_id": "quick_extract_001"
        },
        "response_format": {
          "return_as": "docling_document"
        }
      }
      """
    And Core returns generic Problem extraction prompt
    And no Frame-specific enrichment provided