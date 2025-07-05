"""
Synthetic Data Generator for DUX v9.5 Schema
Automatically generates fully synthetic, schema-compliant DUX objects for all object types.
"""

import json
import random
import uuid
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Any, Optional
import argparse


class DUXSyntheticDataGenerator:
    """Generates synthetic DUX v9.5 objects based on schema definitions."""
    
    def __init__(self, schema_path: str = "src/dux_v9.5_split_schema"):
        self.schema_path = Path(schema_path)
        self.schemas = self._load_schemas()
        
        # Sample data pools for realistic generation
        self.personas = [
            "Platform Engineer", "Developer", "DevOps Engineer", "Site Reliability Engineer",
            "System Administrator", "Data Engineer", "Security Engineer", "Cloud Architect",
            "Product Manager", "Engineering Manager", "OpenShift Admin", "Management"
        ]
        
        self.behavior_types = ["Task", "Action", "System"]
        self.evidence_statuses = ["evidence_backed", "evidence_present", "assumptive"]
        self.evidence_types = ["qualitative", "quantitative", "system_log", "user_interview", "report_summary"]
        self.collection_methods = ["interview", "survey"]
        self.confidence_levels = ["high", "medium", "low"]
        
        # Sample problem domains
        self.problem_domains = [
            "cost management", "resource optimization", "observability", "security",
            "developer experience", "platform operations", "data management", "automation"
        ]
        
        # Sample citations and quotes
        self.sample_citations = [
            "P1_DevOps_Team", "P2_Platform_Engineer", "P3_Site_Reliability",
            "P4_Cloud_Architect", "P5_Security_Team", "P6_Data_Team"
        ]
        
        self.sample_quotes = [
            "We need better visibility into resource utilization and cost allocation.",
            "The current process is too manual and error-prone for our scale.",
            "Developer productivity is impacted by the complexity of the tooling.",
            "We lack proper monitoring and alerting for critical infrastructure components.",
            "Security compliance requirements are difficult to maintain consistently.",
            "Data integration across multiple systems is challenging and time-consuming."
        ]
    
    def _load_schemas(self) -> Dict[str, Dict]:
        """Load all DUX v9.5 schema files."""
        schemas = {}
        
        schema_files = [
            "dux_object_behavior.json",
            "dux_object_flow.json", 
            "dux_object_problem.json",
            "dux_object_result.json",
            "dux_object_useroutcome.json"
        ]
        
        for schema_file in schema_files:
            schema_path = self.schema_path / schema_file
            if schema_path.exists():
                with open(schema_path, 'r') as f:
                    object_type = schema_file.replace("dux_object_", "").replace(".json", "")
                    schemas[object_type] = json.load(f)
            else:
                print(f"Warning: Schema file not found: {schema_path}")
        
        return schemas
    
    def _generate_evidence_block(self) -> Dict[str, Any]:
        """Generate a single evidence block following v9.5 schema."""
        quote = random.choice(self.sample_quotes)
        return {
            "quote": quote,
            "citation": f"{random.choice(self.sample_citations)}, Interview Session",
            "provenance_id": f"synthetic_generation_{datetime.now().strftime('%Y%m%d')}",
            "evidence_type": random.choice(self.evidence_types),
            "confidence_level": random.choice(self.confidence_levels)
        }
    
    def _generate_evidence_array(self, count: int = None) -> List[Dict[str, Any]]:
        """Generate an array of evidence blocks."""
        if count is None:
            count = random.randint(1, 3)
        return [self._generate_evidence_block() for _ in range(count)]
    
    def _generate_related_object_ref(self, object_type: str) -> Dict[str, Any]:
        """Generate a related object reference."""
        return {
            "id": f"{object_type.lower()}_{uuid.uuid4().hex[:8]}",
            "name": f"Sample {object_type} Reference"
        }
    
    def generate_problem_object(self, custom_params: Dict = None) -> Dict[str, Any]:
        """Generate a synthetic Problem object."""
        problem_id = f"problem_{uuid.uuid4().hex[:8]}"
        domain = random.choice(self.problem_domains)
        persona = random.choice(self.personas)
        
        # Generate JTBD format description
        situations = [
            f"When {persona.lower()}s need to manage {domain}",
            f"When teams encounter issues with {domain}",
            f"When organizations need to improve {domain}"
        ]
        
        motivations = [
            "I want automated solutions and clear visibility",
            "I want streamlined workflows and reduced manual effort", 
            "I want reliable tools and actionable insights"
        ]
        
        outcomes = [
            "so I can focus on higher-value work and strategic initiatives",
            "so I can deliver better results with confidence and efficiency",
            "so I can meet organizational goals and compliance requirements"
        ]
        
        jtbd = f"{random.choice(situations)}, {random.choice(motivations)}, {random.choice(outcomes)}."
        
        problem = {
            "dux_schema_version": "9.5",
            "object_type": "Problem",
            "id": problem_id,
            "description": jtbd,
            "end_user": [persona],
            "what_is_at_stake": f"Organizational efficiency and {domain} effectiveness",
            "evidence_status": random.choice(self.evidence_statuses),
            "evidence": self._generate_evidence_array(),
            "result_ids": [],
            "behavior_ids": [],
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat()
        }
        
        # Apply custom parameters if provided
        if custom_params:
            problem.update(custom_params)
        
        return problem
    
    def generate_behavior_object(self, custom_params: Dict = None) -> Dict[str, Any]:
        """Generate a synthetic Behavior object."""
        behavior_id = f"behavior_{uuid.uuid4().hex[:8]}"
        persona = random.choice(self.personas)
        domain = random.choice(self.problem_domains)
        
        # Generate user enablement statement
        actions = [
            f"monitor and optimize {domain} metrics",
            f"automate {domain} workflows and processes",
            f"analyze and report on {domain} performance",
            f"configure and manage {domain} settings"
        ]
        
        description = f"{persona} is able to {random.choice(actions)}."
        
        behavior = {
            "dux_schema_version": "9.5", 
            "object_type": "Behavior",
            "id": behavior_id,
            "description": description,
            "behavior_type": random.choice(self.behavior_types),
            "end_user": persona,
            "related_problem_ids": [self._generate_related_object_ref("Problem")],
            "evidence_status": random.choice(self.evidence_statuses),
            "evidence": self._generate_evidence_array(),
            "flow_ids": [],
            "acceptance_criteria": [
                f"System successfully implements: {description}",
                "Implementation is measurable and observable",
                "User can verify the behavior has occurred"
            ],
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat()
        }
        
        # Apply custom parameters if provided
        if custom_params:
            behavior.update(custom_params)
        
        return behavior
    
    def generate_flow_object(self, custom_params: Dict = None) -> Dict[str, Any]:
        """Generate a synthetic Flow object."""
        flow_id = f"flow_{uuid.uuid4().hex[:8]}"
        persona = random.choice(self.personas)
        domain = random.choice(self.problem_domains)
        
        flow = {
            "dux_schema_version": "9.5",
            "object_type": "Flow", 
            "id": flow_id,
            "title": f"{persona} {domain.title()} Workflow",
            "user_scenario": f"Managing {domain} through an end-to-end workflow that ensures efficiency and reliability",
            "behavior_sequence": [
                f"behavior_initiate_{domain.replace(' ', '_')}",
                f"behavior_analyze_{domain.replace(' ', '_')}",
                f"behavior_optimize_{domain.replace(' ', '_')}",
                f"behavior_validate_{domain.replace(' ', '_')}"
            ],
            "end_user": persona,
            "problem_ids": [self._generate_related_object_ref("Problem")],
            "evidence_status": random.choice(self.evidence_statuses),
            "evidence": self._generate_evidence_array(),
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat()
        }
        
        # Apply custom parameters if provided
        if custom_params:
            flow.update(custom_params)
        
        return flow
    
    def generate_result_object(self, custom_params: Dict = None) -> Dict[str, Any]:
        """Generate a synthetic Result object."""
        result_id = f"result_{uuid.uuid4().hex[:8]}"
        persona = random.choice(self.personas)
        domain = random.choice(self.problem_domains)
        
        result = {
            "dux_schema_version": "9.5",
            "object_type": "Result",
            "id": result_id,
            "description": f"Measurable improvement in {domain} efficiency and effectiveness for {persona.lower()}s",
            "end_user": persona,
            "key_signals": [
                f"Reduced time spent on {domain} tasks",
                f"Increased accuracy in {domain} operations", 
                f"Improved user satisfaction with {domain} tools"
            ],
            "derived_from_behavior_signals": True,
            "source_behavior_ids": [self._generate_related_object_ref("Behavior")],
            "signal_discovery_method": "user_behavior_analysis",
            "success_criteria": [
                f"25% reduction in {domain} task completion time",
                f"90% user satisfaction score for {domain} tools",
                f"Zero critical {domain} incidents per month"
            ],
            "outcome_metrics": {
                "efficiency_improvement": "25%",
                "user_satisfaction": "90%",
                "incident_reduction": "100%"
            },
            "evidence_status": random.choice(self.evidence_statuses),
            "evidence": self._generate_evidence_array(),
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat()
        }
        
        # Apply custom parameters if provided
        if custom_params:
            result.update(custom_params)
        
        return result
    
    def generate_useroutcome_object(self, custom_params: Dict = None) -> Dict[str, Any]:
        """Generate a synthetic UserOutcome object."""
        outcome_id = f"outcome_{uuid.uuid4().hex[:8]}"
        persona = random.choice(self.personas)
        domain = random.choice(self.problem_domains)
        
        outcome = {
            "dux_schema_version": "9.5",
            "object_type": "UserOutcome",
            "id": outcome_id,
            "user_scenario": f"As a {persona}, I need efficient {domain} capabilities to achieve organizational goals",
            "outcome_statement": f"Streamlined {domain} processes that enable {persona.lower()}s to work more effectively",
            "target_impact_when_achieved": f"Improved organizational efficiency and {persona.lower()} productivity in {domain}",
            "priority": random.choice(["High", "Medium", "Low"]),
            "related_problem_ids": [self._generate_related_object_ref("Problem")],
            "related_result_ids": [self._generate_related_object_ref("Result")],
            "related_flow_ids": [self._generate_related_object_ref("Flow")], 
            "key_signals": [
                f"Positive feedback from {persona.lower()}s on {domain} tools",
                f"Increased adoption of {domain} best practices",
                f"Reduced escalations related to {domain} issues"
            ],
            "signal_source": "user_feedback_and_analytics",
            "success_criteria": [
                f"80% of {persona.lower()}s report improved {domain} experience",
                f"50% reduction in {domain}-related support tickets",
                f"Consistent usage of {domain} automation tools"
            ],
            "target_metrics": {
                "user_satisfaction": "80%",
                "support_reduction": "50%",
                "automation_adoption": "90%"
            },
            "evidence_status": random.choice(self.evidence_statuses),
            "evidence": self._generate_evidence_array(),
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat()
        }
        
        # Apply custom parameters if provided
        if custom_params:
            outcome.update(custom_params)
        
        return outcome
    
    def generate_object_collection(self, counts: Dict[str, int] = None) -> List[Dict[str, Any]]:
        """Generate a collection of multiple object types."""
        if counts is None:
            counts = {
                "problem": 3,
                "behavior": 5,
                "flow": 2,
                "result": 3,
                "useroutcome": 2
            }
        
        objects = []
        
        for object_type, count in counts.items():
            generator_method = getattr(self, f"generate_{object_type}_object")
            for _ in range(count):
                objects.append(generator_method())
        
        return objects
    
    def save_synthetic_data(self, objects: List[Dict], output_path: str):
        """Save synthetic data to JSON file."""
        output_file = Path(output_path)
        output_file.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(objects, f, indent=2, ensure_ascii=False)
        
        print(f"Generated {len(objects)} synthetic objects saved to: {output_path}")
    
    def validate_against_schema(self, obj: Dict[str, Any]) -> bool:
        """Basic validation check against known schema requirements."""
        object_type = obj.get("object_type", "").lower()
        
        # Check required fields based on object type
        required_fields_map = {
            "problem": ["dux_schema_version", "object_type", "id", "description", "end_user"],
            "behavior": ["dux_schema_version", "object_type", "id", "description", "behavior_type", "end_user"],
            "flow": ["dux_schema_version", "object_type", "id", "title", "user_scenario", "behavior_sequence", "end_user"],
            "result": ["dux_schema_version", "object_type", "id", "description", "end_user"],
            "useroutcome": ["dux_schema_version", "object_type", "id", "user_scenario", "outcome_statement"]
        }
        
        required_fields = required_fields_map.get(object_type, [])
        
        for field in required_fields:
            if field not in obj:
                print(f"Validation error: Missing required field '{field}' in {object_type} object")
                return False
        
        # Check evidence structure if present
        if "evidence" in obj and isinstance(obj["evidence"], list):
            for evidence in obj["evidence"]:
                required_evidence_fields = ["quote", "citation", "provenance_id", "evidence_type", "confidence_level"]
                for field in required_evidence_fields:
                    if field not in evidence:
                        print(f"Validation error: Missing evidence field '{field}'")
                        return False
        
        return True


def main():
    """Main function for command-line usage."""
    parser = argparse.ArgumentParser(description="Generate synthetic DUX v9.5 data")
    parser.add_argument("--output", "-o", default="test_data/generated/synthetic_dux_v9.5_objects.json",
                       help="Output file path")
    parser.add_argument("--problems", type=int, default=3, help="Number of Problem objects to generate")
    parser.add_argument("--behaviors", type=int, default=5, help="Number of Behavior objects to generate")
    parser.add_argument("--flows", type=int, default=2, help="Number of Flow objects to generate")
    parser.add_argument("--results", type=int, default=3, help="Number of Result objects to generate")
    parser.add_argument("--useroutcomes", type=int, default=2, help="Number of UserOutcome objects to generate")
    parser.add_argument("--validate", action="store_true", help="Validate generated objects")
    
    args = parser.parse_args()
    
    # Initialize generator
    generator = DUXSyntheticDataGenerator()
    
    # Generate objects
    counts = {
        "problem": args.problems,
        "behavior": args.behaviors,
        "flow": args.flows,
        "result": args.results,
        "useroutcome": args.useroutcomes
    }
    
    objects = generator.generate_object_collection(counts)
    
    # Validate if requested
    if args.validate:
        print("Validating generated objects...")
        valid_count = 0
        for obj in objects:
            if generator.validate_against_schema(obj):
                valid_count += 1
        
        print(f"Validation complete: {valid_count}/{len(objects)} objects passed validation")
    
    # Save to file
    generator.save_synthetic_data(objects, args.output)
    
    # Print summary
    type_counts = {}
    for obj in objects:
        obj_type = obj.get("object_type", "Unknown")
        type_counts[obj_type] = type_counts.get(obj_type, 0) + 1
    
    print("\nGenerated objects summary:")
    for obj_type, count in type_counts.items():
        print(f"  {obj_type}: {count}")


if __name__ == "__main__":
    main()
