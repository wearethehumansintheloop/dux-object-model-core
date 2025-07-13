"""
Test Data Integration Utilities for DUX Object Model
Handles CSV import, evidence extraction, and test data population
"""

import csv
import json
import re
from pathlib import Path
from typing import Dict, List, Any, Optional
from datetime import datetime


class TestDataManager:
    """Manages test data import and evidence extraction from various sources."""
    
    def __init__(self, base_path: str = "test_data"):
        self.base_path = Path(base_path)
        self.csv_path = self.base_path / "csv"
        self.generated_path = self.base_path / "generated" 
        self.samples_path = self.base_path / "samples"
        
        # Create directories if they don't exist
        for path in [self.base_path, self.csv_path, self.generated_path, self.samples_path]:
            path.mkdir(exist_ok=True)
        
    def import_csv_data(self, csv_file_path: str) -> List[Dict[str, Any]]:
        """Import CSV data and return as list of dictionaries."""
        data = []
        with open(csv_file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Clean up the data
                cleaned_row = {k.strip(): v.strip() if isinstance(v, str) else v 
                              for k, v in row.items() if k}
                data.append(cleaned_row)
        return data
    
    def extract_evidence_blocks(self, interview_data: List[Dict[str, Any]], 
                               source_file: str) -> List[Dict[str, Any]]:
        """Extract evidence blocks from interview/research data."""
        evidence_blocks = []
        
        for idx, row in enumerate(interview_data):
            # Look for common interview/research fields
            quote_fields = ['quote', 'response', 'answer', 'comment', 'feedback']
            context_fields = ['question', 'context', 'scenario', 'situation']
            
            quote = None
            context = None
            
            # Find quote/response content
            for field in quote_fields:
                if field in row and row[field]:
                    quote = row[field]
                    break
            
            # Find context/question content
            for field in context_fields:
                if field in row and row[field]:
                    context = row[field]
                    break
            
            if quote:
                # Create schema-compliant evidence block
                evidence_block = {
                    "teaser": quote[:100] + "..." if len(quote) > 100 else quote,
                    "quote": quote,
                    "citation": f"Interview participant {row.get('participant', row.get('interviewee', 'Anonymous'))}, {source_file}",
                    "provenance": {
                        "source_filename": source_file,
                        "timestamp_in": row.get('timestamp', row.get('date', datetime.now().isoformat())),
                        "timestamp_out": row.get('timestamp', row.get('date', datetime.now().isoformat()))
                    },
                    "evidence_type": "qualitative",
                    "collection_method": "interview"
                }
                evidence_blocks.append(evidence_block)
                
        return evidence_blocks
    
    def create_problem_from_evidence(self, evidence_blocks: List[Dict[str, Any]], 
                                   problem_context: Dict[str, Any]) -> Dict[str, Any]:
        """Create a Problem object populated with real evidence data (v9.5 compliant)."""
        
        # Extract JTBD pattern from evidence or use provided context
        jtbd_description = problem_context.get('description', 
            "When users need earthquake alerts, I want to receive timely notifications, so I can take appropriate safety actions.")
        
        # Ensure JTBD format compliance
        if not re.match(r"^When .+, I want .+, so I can .+\.$", jtbd_description):
            # Auto-format if needed
            jtbd_description = f"When {problem_context.get('situation', 'users encounter this scenario')}, I want {problem_context.get('motivation', 'to achieve their goal')}, so I can {problem_context.get('outcome', 'get the desired result')}."
        
        # Convert evidence blocks to v9.5 format
        v95_evidence = []
        for block in evidence_blocks[:5]:  # Limit to 5 evidence blocks
            v95_block = {
                "quote": block.get("quote", ""),
                "citation": block.get("citation", "Unknown source"),
                "provenance": block.get("provenance", {
                    "source_filename": "test_data_import.csv",
                    "timestamp_in": datetime.now().isoformat(),
                    "timestamp_out": datetime.now().isoformat()
                }),
                "evidence_type": block.get("evidence_type", "qualitative"),
                "collection_method": block.get("collection_method", "interview"),
                "confidence_level": block.get("confidence_level", "medium")
            }
            v95_evidence.append(v95_block)
        
        problem_object = {
            "dux_schema_version": "9.5",
            "object_type": "Problem",
            "id": problem_context.get('id', f"problem_{datetime.now().strftime('%Y%m%d_%H%M%S')}"),
            "evidence_status": self._determine_evidence_status(evidence_blocks),
            "description": jtbd_description,
            "end_user": problem_context.get('end_user', ["General Public", "Emergency Responders"]),
            "what_is_at_stake": problem_context.get('what_is_at_stake', 
                                                  "Safety and emergency preparedness"),
            "result_ids": [],
            "behavior_ids": [],
            "evidence": v95_evidence,
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat()
        }
        
        return problem_object
    
    def create_behavior_from_evidence(self, evidence_blocks: List[Dict[str, Any]], 
                                    behavior_context: Dict[str, Any]) -> Dict[str, Any]:
        """Create a Behavior object populated with real evidence data (v9.5 compliant)."""
        
        # Convert evidence blocks to v9.5 format
        v95_evidence = []
        for block in evidence_blocks[:5]:
            v95_block = {
                "quote": block.get("quote", ""),
                "citation": block.get("citation", "Unknown source"),
                "provenance": block.get("provenance", {
                    "source_filename": "test_data_import.csv",
                    "timestamp_in": datetime.now().isoformat(),
                    "timestamp_out": datetime.now().isoformat()
                }),
                "evidence_type": block.get("evidence_type", "qualitative"),
                "collection_method": block.get("collection_method", "interview"),
                "confidence_level": block.get("confidence_level", "medium")
            }
            v95_evidence.append(v95_block)
        
        # Ensure user enablement format: "[Persona] is able to [action]"
        description = behavior_context.get('description', "User is able to perform tasks efficiently")
        if not re.match(r"^.+ is able to .+$", description):
            persona = behavior_context.get('end_user', 'User')
            action = behavior_context.get('action', 'perform the required task')
            description = f"{persona} is able to {action}."
        
        behavior_object = {
            "dux_schema_version": "9.5",
            "object_type": "Behavior",
            "id": behavior_context.get('id', f"behavior_{datetime.now().strftime('%Y%m%d_%H%M%S')}"),
            "description": description,
            "behavior_type": behavior_context.get('behavior_type', "Task"),
            "end_user": behavior_context.get('end_user', "User"),
            "related_problem_ids": [],
            "evidence_status": self._determine_evidence_status(evidence_blocks),
            "evidence": v95_evidence,
            "flow_ids": [],
            "acceptance_criteria": [
                f"System successfully implements: {description}",
                "Implementation is measurable and observable",
                "User can verify the behavior has occurred"
            ],
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat()
        }
        
        return behavior_object
    
    def create_result_from_evidence(self, evidence_blocks: List[Dict[str, Any]], 
                                  result_context: Dict[str, Any]) -> Dict[str, Any]:
        """Create a Result object populated with real evidence data (v9.5 compliant)."""
        
        # Convert evidence blocks to v9.5 format
        v95_evidence = []
        for block in evidence_blocks[:5]:
            v95_block = {
                "quote": block.get("quote", ""),
                "citation": block.get("citation", "Unknown source"),
                "provenance": block.get("provenance", {
                    "source_filename": "test_data_import.csv",
                    "timestamp_in": datetime.now().isoformat(),
                    "timestamp_out": datetime.now().isoformat()
                }),
                "evidence_type": block.get("evidence_type", "qualitative"),
                "collection_method": block.get("collection_method", "interview"),
                "confidence_level": block.get("confidence_level", "medium")
            }
            v95_evidence.append(v95_block)
        
        result_object = {
            "dux_schema_version": "9.5",
            "object_type": "Result",
            "id": result_context.get('id', f"result_{datetime.now().strftime('%Y%m%d_%H%M%S')}"),
            "description": result_context.get('description', 
                                            "Outcome achieved through user research and development"),
            "end_user": result_context.get('end_user', "User"),
            "key_signals": result_context.get('key_signals', ["Improved user satisfaction"]),
            "derived_from_behavior_signals": result_context.get('derived_from_behavior_signals', True),
            "source_behavior_ids": result_context.get('source_behavior_ids', []),
            "signal_discovery_method": result_context.get('signal_discovery_method', "user_research"),
            "success_criteria": result_context.get('success_criteria', ["Measurable improvement observed"]),
            "outcome_metrics": result_context.get('outcome_metrics', {}),
            "evidence_status": self._determine_evidence_status(evidence_blocks),
            "evidence": v95_evidence,
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat()
        }
        
        return result_object

    def create_flow_from_evidence(self, evidence_blocks: List[Dict[str, Any]], 
                                flow_context: Dict[str, Any]) -> Dict[str, Any]:
        """Create a Flow object populated with real evidence data (v9.5 compliant)."""
        
        # Convert evidence blocks to v9.5 format
        v95_evidence = []
        for block in evidence_blocks[:5]:
            v95_block = {
                "quote": block.get("quote", ""),
                "citation": block.get("citation", "Unknown source"),
                "provenance": block.get("provenance", {
                    "source_filename": "test_data_import.csv",
                    "timestamp_in": datetime.now().isoformat(),
                    "timestamp_out": datetime.now().isoformat()
                }),
                "evidence_type": block.get("evidence_type", "qualitative"),
                "collection_method": block.get("collection_method", "interview"),
                "confidence_level": block.get("confidence_level", "medium")
            }
            v95_evidence.append(v95_block)
        
        flow_object = {
            "dux_schema_version": "9.5",
            "object_type": "Flow",
            "id": flow_context.get('id', f"flow_{datetime.now().strftime('%Y%m%d_%H%M%S')}"),
            "title": flow_context.get('title', "User Workflow"),
            "user_scenario": flow_context.get('user_scenario', 
                                          "User workflow observed during research"),
            "behavior_sequence": flow_context.get('behavior_sequence', []),
            "end_user": flow_context.get('end_user', "User"),
            "problem_ids": flow_context.get('problem_ids', []),
            "evidence_status": self._determine_evidence_status(evidence_blocks),
            "evidence": v95_evidence,
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat()
        }
        
        return flow_object

    def _determine_evidence_status(self, evidence_blocks: List[Dict[str, Any]]) -> str:
        """Determine evidence status based on quantity and quality of evidence."""
        if len(evidence_blocks) >= 2:
            # Check if any evidence contains quantitative data
            has_quantitative = any(
                any(char.isdigit() for char in str(block.get('quote', '')))
                for block in evidence_blocks
            )
            return "evidence_backed" if has_quantitative else "evidence_present"
        elif len(evidence_blocks) >= 1:
            return "evidence_present"
        else:
            return "assumptive"
    
    def save_test_object(self, obj: Dict[str, Any], filename: str) -> Path:
        """Save a test object to JSON file."""
        file_path = self.base_path / filename
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(obj, f, indent=2, ensure_ascii=False)
        return file_path
    
    def load_test_object(self, filename: str) -> Dict[str, Any]:
        """Load a test object from JSON file."""
        file_path = self.base_path / filename
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def analyze_object_relationships(self, obj1: Dict[str, Any], obj2: Dict[str, Any]) -> Dict[str, Any]:
        """Use LLM reasoning to identify potential relationships between two DUX objects."""
        
        # Extract key semantic information for analysis
        obj1_summary = {
            "type": obj1.get("object_type"),
            "id": obj1.get("id"),
            "description": obj1.get("description", ""),
            "evidence_quotes": [e.get("quote", "")[:100] for e in obj1.get("evidence", [])]
        }
        
        obj2_summary = {
            "type": obj2.get("object_type"),
            "id": obj2.get("id"), 
            "description": obj2.get("description", ""),
            "evidence_quotes": [e.get("quote", "")[:100] for e in obj2.get("evidence", [])]
        }
        
        # Analyze semantic relationships
        analysis = {
            "relationship_detected": False,
            "relationship_type": None,
            "confidence": 0.0,
            "reasoning": "",
            "suggested_links": []
        }
        
        # Simple heuristic analysis (could be enhanced with actual LLM calls)
        obj1_text = (obj1_summary["description"] + " " + " ".join(obj1_summary["evidence_quotes"])).lower()
        obj2_text = (obj2_summary["description"] + " " + " ".join(obj2_summary["evidence_quotes"])).lower()
        
        # Look for semantic connections
        shared_concepts = self._find_shared_concepts(obj1_text, obj2_text)
        
        if len(shared_concepts) > 2:
            analysis["relationship_detected"] = True
            analysis["confidence"] = min(0.9, len(shared_concepts) * 0.2)
            analysis["reasoning"] = f"Objects share {len(shared_concepts)} concepts: {shared_concepts[:3]}"
            
            # Determine relationship type based on object types
            if obj1_summary["type"] == "Problem" and obj2_summary["type"] == "Result":
                analysis["relationship_type"] = "problem_contributes_to_result"
                analysis["suggested_links"] = [
                    {"from": obj1_summary["id"], "to": obj2_summary["id"], "field": "result_ids"},
                    {"from": obj2_summary["id"], "to": obj1_summary["id"], "field": "problem_ids"}
                ]
            elif obj1_summary["type"] == "Problem" and obj2_summary["type"] == "Flow":
                analysis["relationship_type"] = "problem_addressed_by_flow"
                analysis["suggested_links"] = [
                    {"from": obj1_summary["id"], "to": obj2_summary["id"], "field": "flow_ids"},
                    {"from": obj2_summary["id"], "to": obj1_summary["id"], "field": "problem_ids"}
                ]
            elif obj1_summary["type"] == "Behavior" and obj2_summary["type"] == "Flow":
                analysis["relationship_type"] = "behavior_within_flow"
                analysis["suggested_links"] = [
                    {"from": obj1_summary["id"], "to": obj2_summary["id"], "field": "flow_ids"}
                ]
        
        return analysis

    def _find_shared_concepts(self, text1: str, text2: str) -> List[str]:
        """Find shared concepts between two text strings."""
        
        # Domain-specific concept keywords for Kubeflow/Container platforms
        concepts = [
            "gpu", "resource", "workspace", "container", "image", "cluster", "monitoring",
            "optimization", "scaling", "performance", "memory", "cpu", "storage",
            "notebook", "jupyter", "vscode", "collaboration", "platform", "deployment",
            "alert", "notification", "workflow", "automation", "management", "admin",
            "user", "experience", "interface", "dashboard", "visibility", "tracking"
        ]
        
        shared = []
        for concept in concepts:
            if concept in text1 and concept in text2:
                shared.append(concept)
                
        return shared

    def create_linked_objects_from_csv(self, csv_path: str, 
                                     obj1_type: str = "problem",
                                     obj2_type: str = "result") -> Dict[str, Any]:
        """Create two related DUX objects and automatically link them."""
        
        manager = TestDataManager()
        
        # Import CSV data
        csv_data = manager.import_csv_data(csv_path)
        
        # Extract evidence blocks
        evidence_blocks = manager.extract_evidence_blocks(csv_data, csv_path)
        
        # Split evidence between the two objects
        obj1_evidence = evidence_blocks[:3]
        obj2_evidence = evidence_blocks[2:5]  # Overlap to show relationship
        
        # Create first object
        if obj1_type.lower() == "problem":
            obj1_context = {
                "id": f"problem_joel_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
                "description": "When cluster administrators need to manage GPU resources efficiently, I want to monitor usage patterns and reclaim idle resources, so I can optimize cost and availability.",
                "end_user": ["Cluster Administrators", "Platform Engineers"],
                "what_is_at_stake": "Resource efficiency and cost optimization"
            }
            obj1 = manager.create_problem_from_evidence(obj1_evidence, obj1_context)
        
        # Create second object  
        if obj2_type.lower() == "result":
            obj2_context = {
                "id": f"result_bella_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
                "description": "Data scientists can successfully launch and manage GPU-enabled workspaces for GenAI model training",
                "result_type": "user_outcome",
                "success_criteria": ["Workspace launch time < 30 seconds", "GPU utilization > 80%", "Zero resource conflicts"]
            }
            obj2 = manager.create_result_from_evidence(obj2_evidence, obj2_context)
        
        # Analyze relationships
        relationship_analysis = manager.analyze_object_relationships(obj1, obj2)
        
        # Apply suggested links if relationship detected
        if relationship_analysis["relationship_detected"]:
            for link in relationship_analysis["suggested_links"]:
                if link["from"] == obj1["id"] and link["field"] in obj1:
                    # Add reference with evidence status
                    if isinstance(obj1[link["field"]], list):
                        obj1[link["field"]].append({
                            "id": link["to"],
                            "evidence_status": obj2["evidence_status"],
                            "description": obj2["description"][:100],
                            "reference_context": f"Auto-linked: {relationship_analysis['reasoning']}"
                        })
                
                if link["from"] == obj2["id"] and link["field"] in obj2:
                    if isinstance(obj2[link["field"]], list):
                        obj2[link["field"]].append({
                            "id": link["to"],
                            "evidence_status": obj1["evidence_status"],
                            "description": obj1["description"][:100],
                            "reference_context": f"Auto-linked: {relationship_analysis['reasoning']}"
                        })
        
        return {
            "object1": obj1,
            "object2": obj2,
            "relationship_analysis": relationship_analysis,
            "linked": relationship_analysis["relationship_detected"]
        }
        

# Example usage functions for BDD steps
def create_sample_evidence_from_csv(csv_path: str, object_type: str = "problem") -> Dict[str, Any]:
    """Create a sample DUX object with evidence from CSV data."""
    manager = TestDataManager()
    
    # Import CSV data
    csv_data = manager.import_csv_data(csv_path)
    
    # Extract evidence blocks
    evidence_blocks = manager.extract_evidence_blocks(csv_data, csv_path)
    
    # Create object based on type
    if object_type.lower() == "problem":
        context = {
            "description": "When emergency situations occur, I want to receive reliable alerts, so I can respond appropriately.",
            "end_user": ["General Public", "Emergency Personnel"],
            "what_is_at_stake": "Public safety and emergency response effectiveness"
        }
        return manager.create_problem_from_evidence(evidence_blocks, context)
    
    elif object_type.lower() == "behavior":
        context = {
            "description": "Users check their phones frequently for emergency notifications",
            "behavior_type": "observed",
            "frequency": "high",
            "context": "Emergency notification scenarios"
        }
        return manager.create_behavior_from_evidence(evidence_blocks, context)
    
    # Add more object types as needed
    else:
        raise ValueError(f"Unsupported object type: {object_type}")


# CSV field mapping configurations for different data sources
CSV_FIELD_MAPPINGS = {
    "shakealert": {
        "quote_fields": ["response", "answer", "quote", "comment"],
        "context_fields": ["question", "prompt", "scenario"],
        "participant_field": "participant_id",
        "timestamp_field": "timestamp"
    },
    "general_interview": {
        "quote_fields": ["response", "transcript", "quote"],
        "context_fields": ["question", "context"],
        "participant_field": "interviewee",
        "timestamp_field": "date"
    }
}


def create_linked_evidence_from_csv(csv_path: str, obj1_type: str = "problem", obj2_type: str = "result") -> Dict[str, Any]:
    """Create two related DUX objects with LLM-assisted relationship detection."""
    manager = TestDataManager()
    return manager.create_linked_objects_from_csv(csv_path, obj1_type, obj2_type)


# Enhanced CSV field mapping configurations for persona-specific data sources
CSV_FIELD_MAPPINGS.update({
    "joel_admin": {
        "quote_fields": ["response", "observation", "issue", "concern"],
        "context_fields": ["scenario", "task", "situation", "problem_context"],
        "participant_field": "admin_id",
        "timestamp_field": "timestamp",
        "focus_areas": ["resource_management", "monitoring", "optimization", "bulk_operations"]
    },
    "bella_datascientist": {
        "quote_fields": ["feedback", "experience", "outcome", "result"],
        "context_fields": ["workflow", "use_case", "experiment", "task"],
        "participant_field": "participant_id", 
        "timestamp_field": "timestamp",
        "focus_areas": ["workspace_setup", "gpu_access", "collaboration", "model_training"]
    }
})
