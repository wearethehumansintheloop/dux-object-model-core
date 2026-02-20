# 📝 Secondary Evidence Object (v9.6.1 - Gold Standard for Traceability)

## 🎯 Purpose & Strategic Role
The Evidence object captures secondary evidence from external research sources, product strategies, and industry reports that support UX decision-making. It serves as the foundation for evidence-based design decisions by providing structured access to validated research findings with full source traceability.

## 🧠 "What would you say... you do here?"
When I need to validate a design decision with external research, I want to reference structured evidence with clear attribution, so that I can make informed UX choices backed by credible sources.

## 💡 Why the Evidence Object Matters

- Provides structured access to secondary research findings for evidence-based design
- Maintains complete source traceability for research compliance and validation
- Enables cross-referencing of findings across multiple research sources
- Supports automated evidence synthesis and pattern recognition across studies

## 🔗 Structural Role and Usage Notes
- Foundation for our "Source-Type-Driven Validation" architecture.
- The `source_type` field allows our pipeline to dynamically select the correct specialized validation script.
- The mandatory, structured `citation` object ensures every piece of evidence is explicitly and traceably sourced.
- The optional `pull_quote_attribution` is a fully self-contained, portable object, enabling its use in future "evidence arrays".

## 📋 Schema Attributes

| Attribute | Type | Required | Description |
|---|---|---|---|
| object_type | string | Yes | Object type discriminator, always "evidence". |
| evidence_id | string | Yes | Unique identifier. Format: `EV-[timestamp]-[hash]`. |
| **source_type** | **string (enum)** | **Yes** | **Drives validator selection. Must be one of: `user research report`, `product strategy document`, `interview_transcript`, `discovery_notes`, `industry analyst report`, `qualitative_user_model_artifact`, `product requirements doc`.** |
| user_role | string | Yes | Who this evidence impacts. **Future**: This will be an enum validated against the Canonical Role Library. |
| applications_of_evidence | array | Yes | How this evidence supports product development. |
| synthesized_finding | string | Yes | Core insight extracted from the source. |
| finding_prevalence | string | Yes | How widespread or significant this finding is. |
| **citation** | **`Citation` object** | **Yes** | **A structured, self-contained object with all source attribution info.** |
| pull_quote | string | No | Optional, verbatim quote for illustration. |
| pull_quote_attribution | `PullQuoteAttribution` object | No | Structured attribution for the pull_quote. Required if pull_quote exists. |
| tags | array | No | Development traceability tags (GitHub issues, PRs, commits, Jira tickets, status indicators) |
| created_at | string | No | Creation timestamp. |
| updated_at | string | No | Last update timestamp. |

### Citation Schema
| Attribute | Type | Required | Description |
|---|---|---|---|
| source_artifact_name | string | Yes | The name of the source document. |
| page_reference | string | Yes | Specific page(s) for the finding (e.g., 'pg. 17'). |
| source_authors | string | Yes | Author(s) of the source (e.g., 'Tom Chan, ...'). |
| source_created_on | string | Yes | When the source was created (e.g., '2024-03-15'). |
| source_artifact_trace_endpoint | string | Yes | URI or filename to the source location. |

### PullQuoteAttribution Schema
| Attribute | Type | Required | Description |
|---|---|---|---|
| source_pid | string | Yes | Participant ID as cited in the source. |
| source_artifact_name | string | Yes | The name of the source document. |
| page_reference | string | Yes | Specific page number for the verbatim quote. |
| source_authors | string | Yes | Author(s) of the source. |
| source_created_on | string | Yes | When the source was created. |
| source_artifact_trace_endpoint | string | Yes | URI or filename to the source location. |

## 📦 Canonical Example (Comprehensive - All Tables)
```json
{
  "object_type": "evidence",
  "evidence_id": "EV-20250101-abc123",
  "source_type": "user research report",
  "user_role": "data scientist",
  "applications_of_evidence": [
    "user behavior",
    "user pain point"
  ],
  "synthesized_finding": "Users struggle with complex data preparation workflows",
  "finding_prevalence": "Users struggle with complex data preparation workflows",
  "citation": {
    "source_artifact_name": "RHODS User Interview Report Q1 2024",
    "page_reference": "pg. 23",
    "source_authors": "Sarah Chen, UX Research Team",
    "source_created_on": "2024-03-15",
    "source_artifact_trace_endpoint": "https://research.redhat.com/reports/rhods-q1-2024.pdf"
  },
  "pull_quote": "The data prep takes forever and I never know if I'm doing it right",
  "pull_quote_attribution": {
    "source_pid": "EV-20250101-abc123",
    "source_artifact_name": "RHODS User Interview Report Q1 2024",
    "page_reference": "pg. 23",
    "source_authors": "Sarah Chen, UX Research Team",
    "source_created_on": "2024-03-15",
    "source_artifact_trace_endpoint": "https://research.redhat.com/reports/rhods-q1-2024.pdf"
  },
  "tags": [
    "secondary evidence",
    "user research"
  ],
  "created_at": "2024-03-15",
  "updated_at": "example_updated_at",
  "_docling_metadata": {
    "generated_by": "stage3a_comprehensive_processor",
    "schema_version": "v2.2",
    "tables_processed": 3,
    "total_attributes": 24,
    "validation_status": "ready_for_stage3b"
  }
}
```
## 🔧 Generated JSON Schema (Proposal)
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "codebook/evidence_object_schema_validated.json",
  "title": "Evidence Object Schema (Validated)",
  "type": "object",
  "properties": {
    "object_type": {
      "type": "string",
      "const": "evidence",
      "description": "Object type discriminator"
    },
    "evidence_id": {
      "type": "string",
      "description": "Validated evidence field: evidence_id"
    },
    "source_type": {
      "type": "string",
      "description": "Validated evidence field: source_type"
    },
    "user_role": {
      "type": "string",
      "description": "Validated evidence field: user_role"
    },
    "applications_of_evidence": {
      "type": "array",
      "items": {
        "type": "string",
        "enum": [
          "user goal",
          "behavior",
          "success criteria",
          "success metric",
          "user pain point",
          "system limitation",
          "workflow pattern",
          "tool preference"
        ]
      },
      "description": "Ways evidence supports product development elements"
    },
    "synthesized_finding": {
      "type": "string",
      "description": "Validated evidence field: synthesized_finding"
    },
    "finding_prevalence": {
      "type": "string",
      "description": "Validated evidence field: finding_prevalence"
    },
    "citation": {
      "type": "object",
      "properties": {
        "source_artifact_name": {
          "type": "string",
          "description": "Citation field: source_artifact_name"
        },
        "page_reference": {
          "type": "string",
          "description": "Citation field: page_reference"
        },
        "source_authors": {
          "type": "string",
          "description": "Citation field: source_authors"
        },
        "source_created_on": {
          "type": "string",
          "description": "Citation field: source_created_on"
        },
        "source_artifact_trace_endpoint": {
          "type": "string",
          "description": "Citation field: source_artifact_trace_endpoint"
        }
      },
      "required": [
        "source_artifact_name",
        "page_reference",
        "source_authors",
        "source_created_on",
        "source_artifact_trace_endpoint"
      ]
    },
    "pull_quote": {
      "type": "string",
      "description": "Validated evidence field: pull_quote"
    },
    "pull_quote_attribution": {
      "type": "object",
      "properties": {
        "source_pid": {
          "type": "string",
          "description": "PullQuoteAttribution field: source_pid"
        },
        "source_artifact_name": {
          "type": "string",
          "description": "PullQuoteAttribution field: source_artifact_name"
        },
        "page_reference": {
          "type": "string",
          "description": "PullQuoteAttribution field: page_reference"
        },
        "source_authors": {
          "type": "string",
          "description": "PullQuoteAttribution field: source_authors"
        },
        "source_created_on": {
          "type": "string",
          "description": "PullQuoteAttribution field: source_created_on"
        },
        "source_artifact_trace_endpoint": {
          "type": "string",
          "description": "PullQuoteAttribution field: source_artifact_trace_endpoint"
        }
      },
      "required": [
        "source_pid",
        "source_artifact_name",
        "page_reference",
        "source_authors",
        "source_created_on",
        "source_artifact_trace_endpoint"
      ]
    },
    "tags": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Validated evidence field: tags"
    },
    "created_at": {
      "type": "string",
      "description": "Validated evidence field: created_at"
    },
    "updated_at": {
      "type": "string",
      "description": "Validated evidence field: updated_at"
    }
  },
  "required": [
    "object_type",
    "evidence_id",
    "source_type",
    "user_role",
    "applications_of_evidence",
    "synthesized_finding",
    "finding_prevalence",
    "citation"
  ]
}
```

## 🔧 Comprehensive Docling Metadata
- **Format**: Comprehensive Docling-enhanced Evidence Object Definition
- **Generated by**: Stage 3a Comprehensive Evidence Processor
- **Tables Processed**: Main Schema + Citation + PullQuoteAttribution
- **Total Attributes**: 24
- **Validation Status**: Ready for Stage 3b
- **Schema Compliance**: All discovered attributes included
