#!/usr/bin/env python3
"""
Generated validation script for Problem objects
Generated from: docling markdown schema
Generation timestamp: 2025-07-13T18:31:17.468654

This is a Generation-First artifact - DO NOT EDIT MANUALLY
Regenerate from docling markdown if changes are needed
"""

import json
from typing import Dict, List, Any
from jsonschema import validate, ValidationError

# Generated JSON Schema
PROBLEM_SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "$id": "proposal/problem_object_schema.json",
    "title": "Problem Object Schema (Proposal)",
    "type": "object",
    "properties": {
        "object_type": {
            "type": "string",
            "description": "Must be \"Problem\""
        },
        "id": {
            "type": "string",
            "description": "Unique identifier"
        },
        "job_statement": {
            "type": "object",
            "properties": {
                "user_scenario": {
                    "type": "object",
                    "properties": {
                        "value": {
                            "type": "string",
                            "description": "When [situation]..."
                        },
                        "source": {
                            "type": "string",
                            "enum": [
                                "evidence",
                                "synthetic"
                            ]
                        }
                    },
                    "required": [
                        "value",
                        "source"
                    ]
                },
                "user_enablement": {
                    "type": "object",
                    "properties": {
                        "value": {
                            "type": "string",
                            "description": "I want [motivation]..."
                        },
                        "source": {
                            "type": "string",
                            "enum": [
                                "evidence",
                                "synthetic"
                            ]
                        }
                    },
                    "required": [
                        "value",
                        "source"
                    ]
                },
                "user_outcome": {
                    "type": "object",
                    "properties": {
                        "value": {
                            "type": "string",
                            "description": "so I can [outcome]"
                        },
                        "source": {
                            "type": "string",
                            "enum": [
                                "evidence",
                                "synthetic"
                            ]
                        }
                    },
                    "required": [
                        "value",
                        "source"
                    ]
                }
            },
            "required": [
                "user_scenario",
                "user_enablement",
                "user_outcome"
            ],
            "description": "JTBD decomposed into user_scenario, user_enablement, user_outcome with evidence tracking"
        },
        "evidence": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "provenance_id": {
                        "type": "string",
                        "description": "Reference to Provenance object"
                    },
                    "supports_fields": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        },
                        "description": "Fields this evidence supports"
                    }
                },
                "required": [
                    "provenance_id",
                    "supports_fields"
                ]
            },
            "description": "Array of evidence mappings with provenance_id and supported fields"
        },
        "end_user": {
            "type": "array",
            "items": {
                "type": "string"
            },
            "description": "User personas or roles who experience this problem"
        },
        "what_is_at_stake": {
            "type": "string",
            "description": "What users lose or risk if this problem isn't solved"
        },
        "protocol_url": {
            "type": "string",
            "description": "URL to protocol, methodology, or research documentation"
        },
        "result_ids": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "string"
                    },
                    "reference_context": {
                        "type": "string"
                    }
                },
                "required": [
                    "id"
                ]
            },
            "description": "Envisioned results from solving this problem (with id and reference_context)"
        },
        "useroutcome_ids": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "string"
                    },
                    "reference_context": {
                        "type": "string"
                    }
                },
                "required": [
                    "id"
                ]
            },
            "description": "User outcomes that solve this problem (with id and reference_context)"
        },
        "flow_ids": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "string"
                    },
                    "reference_context": {
                        "type": "string"
                    }
                },
                "required": [
                    "id"
                ]
            },
            "description": "Flows that address how this problem is solved (with id and reference_context)"
        },
        "opportunity_score": {
            "type": "object",
            "properties": {
                "value": {
                    "type": "number",
                    "description": "ODI opportunity score value"
                },
                "importance": {
                    "type": "number",
                    "description": "How important is this to users (1-10)"
                },
                "satisfaction": {
                    "type": "number",
                    "description": "How satisfied are users currently (1-10)"
                },
                "value_source": {
                    "type": "string",
                    "enum": [
                        "evidence",
                        "synthetic"
                    ],
                    "description": "Source of the value score"
                },
                "importance_source": {
                    "type": "string",
                    "enum": [
                        "evidence",
                        "synthetic"
                    ],
                    "description": "Source of the importance score"
                },
                "satisfaction_source": {
                    "type": "string",
                    "enum": [
                        "evidence",
                        "synthetic"
                    ],
                    "description": "Source of the satisfaction score"
                }
            },
            "required": [
                "value",
                "importance",
                "satisfaction",
                "value_source",
                "importance_source",
                "satisfaction_source"
            ],
            "description": "ODI opportunity score with value, importance, satisfaction, and source tracking (evidence/synthetic)"
        },
        "tags": {
            "type": "array",
            "items": {
                "type": "string"
            },
            "description": "System-derived tags"
        },
        "created_at": {
            "type": "string",
            "description": "Creation timestamp"
        },
        "updated_at": {
            "type": "string",
            "description": "Last update timestamp"
        }
    },
    "required": [
        "object_type",
        "id",
        "job_statement",
        "evidence"
    ]
}

def validate_problem_instance(instance: Dict[str, Any]) -> Dict[str, Any]:
    """Validate a problem instance against the generated schema."""
    errors = []
    
    # JSON Schema validation
    try:
        validate(instance=instance, schema=PROBLEM_SCHEMA)
    except ValidationError as e:
        errors.append(f"Schema validation error: {e.message}")
    
    # Custom validations for problem
    # Validate job_statement decomposition
    if 'job_statement' in instance:
        js = instance['job_statement']
        if isinstance(js, dict):
            for field in ['user_scenario', 'user_enablement', 'user_outcome']:
                if field in js and isinstance(js[field], dict):
                    if 'value' not in js[field]:
                        errors.append(f"job_statement.{field} missing value")
                    if 'source' not in js[field]:
                        errors.append(f"job_statement.{field} missing source")
    
    # Validate evidence array
    if 'evidence' in instance and isinstance(instance['evidence'], list):
        for i, evidence in enumerate(instance['evidence']):
            if isinstance(evidence, dict):
                if 'provenance_id' not in evidence:
                    errors.append(f"evidence[{i}] missing provenance_id")
                if 'supports_fields' not in evidence:
                    errors.append(f"evidence[{i}] missing supports_fields")
    
    return {
        'valid': len(errors) == 0,
        'errors': errors
    }

if __name__ == "__main__":
    # Example usage
    import sys
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as f:
            instance = json.load(f)
        result = validate_problem_instance(instance)
        if result['valid']:
            print("✅ Validation passed")
        else:
            print(f"❌ Validation failed with {len(result['errors'])} errors:")
            for error in result['errors']:
                print(f"  - {error}")
