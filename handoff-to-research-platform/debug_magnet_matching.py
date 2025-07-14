#!/usr/bin/env python3
"""
Debug script to test magnet matching logic with real data
"""

import json
import re

def extract_objects_from_file(file_path):
    """Extract DUX objects from a markdown file"""
    objects = []
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Find JSON blocks
    json_pattern = r'```json\s*\n(.*?)\n```'
    json_matches = re.findall(json_pattern, content, re.DOTALL)
    
    for json_str in json_matches:
        try:
            obj = json.loads(json_str)
            if 'object_type' in obj:
                objects.append(obj)
        except json.JSONDecodeError:
            continue
    
    return objects

def get_object_description(obj):
    """Get description based on object type"""
    obj_type = obj.get('object_type', '').lower()
    
    if obj_type == 'problem':
        return obj.get('job_statement', '')
    elif obj_type == 'behavior':
        return obj.get('user_enablement', '')
    elif obj_type == 'result':
        return obj.get('target_impact', '')
    elif obj_type == 'insight':
        return obj.get('insight_teaser', '')
    else:
        return obj.get('description', obj.get('job_statement', obj.get('title', '')))

def test_matching():
    """Test the matching logic"""
    
    # Test with multiple files
    test_files = [
        "object_samples/20250704_225732_0001_fit_objects_nubank.md",
        "object_samples/20250705_001026_fit_template_kubeflow.md",
        "objects_RAW/insight_chain_kubeflow2.0.md"
    ]
    
    all_objects = []
    for file_path in test_files:
        try:
            objects = extract_objects_from_file(file_path)
            all_objects.extend(objects)
            print(f"📊 Found {len(objects)} objects in {file_path}")
        except FileNotFoundError:
            print(f"⚠️  File not found: {file_path}")
    
    print(f"\n📊 Total objects to test: {len(all_objects)}")
    
    # Test templates with actual criteria from demo_fit_template_pipeline.py
    templates = {
        "Cost Management": {
            "problem_scope": "cost cloud spend budget forecasting",
            "behavior_constraints": ["cost", "budget", "spend", "forecasting", 
                                   "optimization"],
            "result_requirements": ["cost", "savings", "efficiency", "accurate", 
                                  "deviation"]
        },
        "Operating Models Purpose": {
            "problem_scope": "financial inclusion business transformation",
            "behavior_constraints": ["transformation", "inclusion", "business", 
                                   "organizational"],
            "result_requirements": ["growth", "expansion", "inclusion", 
                                  "customers", "market"]
        },
        "Kubeflow Bella": {
            "problem_scope": "AI ML workflow platform management",
            "behavior_constraints": ["workflow automation", "AI model deployment", 
                                   "platform management"],
            "result_requirements": ["workflow efficiency", "AI adoption", 
                                  "platform stability"]
        }
    }
    
    # Test each object against each template
    for template_name, criteria in templates.items():
        print(f"\n🧲 Testing {template_name} template:")
        print(f"   Problem scope: {criteria['problem_scope']}")
        print(f"   Behavior constraints: {criteria['behavior_constraints']}")
        print(f"   Result requirements: {criteria['result_requirements']}")
        
        matches = 0
        for obj in all_objects:
            obj_type = obj.get('object_type', '')
            obj_desc = get_object_description(obj).lower()
            
            # Test matching logic
            matched = False
            if obj_type == 'Problem' and criteria['problem_scope']:
                matched = criteria['problem_scope'].lower() in obj_desc
            elif obj_type == 'Behavior' and criteria['behavior_constraints']:
                matched = any(constraint.lower() in obj_desc 
                            for constraint in criteria['behavior_constraints'])
            elif obj_type == 'Result' and criteria['result_requirements']:
                matched = any(req.lower() in obj_desc 
                            for req in criteria['result_requirements'])
            
            if matched:
                matches += 1
                print(f"   ✅ MATCH: {obj_type} - {obj.get('id', 'no-id')}")
                print(f"      Description: {obj_desc[:100]}...")
            else:
                # Only show first few misses to avoid spam
                if matches == 0 and len([o for o in all_objects[:5] if o == obj]):
                    print(f"   ❌ NO MATCH: {obj_type} - {obj.get('id', 'no-id')}")
                    print(f"      Description: {obj_desc[:100]}...")
        
        print(f"   📈 Total matches for {template_name}: {matches}/{len(all_objects)}")

if __name__ == "__main__":
    test_matching() 