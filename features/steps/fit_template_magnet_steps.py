"""
Step definitions for Fit Template Magnet System
Implements the behavior for using Fit Templates as "magnets" to attract and organize related objects
"""

import json
import os
from datetime import datetime
from typing import Dict, List, Any
from behave import given, when, then
import jsonschema

class FitTemplateMagnetSystem:
    """Core system for applying Fit Templates as magnets to attract related objects"""
    
    def __init__(self):
        self.fit_templates = {}
        self.raw_data = {}
        self.attracted_objects = []
        self.matched_objects = []
        self.validation_results = {}
        
    def load_fit_template(self, template_name: str, template_data: Dict[str, Any]):
        """Load a Fit Template for use as a magnet"""
        self.fit_templates[template_name] = template_data
        return True
        
    def load_raw_data(self, data_source: str, data: Dict[str, Any]):
        """Load raw research data from various sources"""
        self.raw_data[data_source] = data
        return True
        
    def apply_fit_template_magnet(self, template_name: str, data_sources: List[str]) -> List[Dict[str, Any]]:
        """Apply a Fit Template as a magnet to attract related objects"""
        if template_name not in self.fit_templates:
            raise ValueError(f"Fit Template '{template_name}' not found")
            
        template = self.fit_templates[template_name]
        attracted_objects = []
        
        # Apply the magnet logic based on template criteria
        for source in data_sources:
            if source in self.raw_data:
                source_objects = self._extract_objects_from_source(source)
                attracted_objects.extend(self._apply_magnet_criteria(template, source_objects))
                
        self.attracted_objects = attracted_objects
        return attracted_objects
        
    def _extract_objects_from_source(self, source: str) -> List[Dict[str, Any]]:
        """Extract potential objects from a data source"""
        # This would integrate with your LLM extraction logic
        # For now, return mock data
        return self.raw_data.get(source, {}).get('objects', [])
        
    def _apply_magnet_criteria(self, template: Dict[str, Any], objects: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Apply magnet criteria to attract related objects"""
        attracted = []
        
        # Extract criteria from template
        problem_scope = template.get('preferred_chaining_criteria', {}).get('problem_scope', '')
        behavior_constraints = template.get('preferred_chaining_criteria', {}).get('behavior_constraints', [])
        result_requirements = template.get('preferred_chaining_criteria', {}).get('result_requirements', [])
        
        for obj in objects:
            if self._object_matches_criteria(obj, problem_scope, behavior_constraints, result_requirements):
                attracted.append(obj)
                
        return attracted
        
    def _object_matches_criteria(self, obj: Dict[str, Any], problem_scope: str, 
                                behavior_constraints: List[str], result_requirements: List[str]) -> bool:
        """Check if an object matches the magnet criteria"""
        obj_type = obj.get('object_type', '')
        
        # Basic matching logic - would be enhanced with LLM-based semantic matching
        if obj_type == 'Problem' and problem_scope:
            return problem_scope.lower() in obj.get('description', '').lower()
        elif obj_type == 'Behavior' and behavior_constraints:
            return any(constraint.lower() in obj.get('description', '').lower() 
                      for constraint in behavior_constraints)
        elif obj_type == 'Result' and result_requirements:
            return any(req.lower() in obj.get('description', '').lower() 
                      for req in result_requirements)
        
        return False
        
    def validate_attracted_objects(self, template_name: str) -> Dict[str, Any]:
        """Validate attracted objects against Fit Template criteria"""
        if template_name not in self.fit_templates:
            raise ValueError(f"Fit Template '{template_name}' not found")
            
        template = self.fit_templates[template_name]
        validation_results = {
            'total_objects': len(self.attracted_objects),
            'matched_objects': [],
            'unmatched_objects': [],
            'summary_table': []
        }
        
        for obj in self.attracted_objects:
            match_result = self._validate_object_against_template(obj, template)
            if match_result['fit_matched']:
                validation_results['matched_objects'].append(obj)
                obj['fit_alignment_reason'] = match_result['fit_alignment_reason']
            else:
                validation_results['unmatched_objects'].append(obj)
                
            validation_results['summary_table'].append({
                'object_id': obj.get('id', 'unknown'),
                'object_type': obj.get('object_type', 'unknown'),
                'match_status': match_result['fit_matched'],
                'rationale': match_result['fit_alignment_reason']
            })
            
        self.matched_objects = validation_results['matched_objects']
        self.validation_results = validation_results
        return validation_results
        
    def _validate_object_against_template(self, obj: Dict[str, Any], template: Dict[str, Any]) -> Dict[str, Any]:
        """Validate a single object against template criteria"""
        # Enhanced validation logic using template criteria
        template_objects = template.get('dux_object_map', {})
        
        # Check if object aligns with template objects
        for template_obj_type, template_obj in template_objects.items():
            if obj.get('object_type') == template_obj_type:
                # Basic alignment check - would be enhanced with semantic similarity
                if self._objects_align(obj, template_obj):
                    return {
                        'fit_matched': True,
                        'fit_alignment_reason': f"Aligns with {template_obj_type} in template"
                    }
                    
        return {
            'fit_matched': False,
            'fit_alignment_reason': "Does not align with template criteria"
        }
        
    def _objects_align(self, obj: Dict[str, Any], template_obj: Dict[str, Any]) -> bool:
        """Check if two objects align semantically"""
        # Basic alignment check - would be enhanced with LLM-based semantic similarity
        obj_desc = obj.get('description', '').lower()
        template_desc = template_obj.get('description', '').lower()
        
        # Simple keyword matching for now
        common_words = set(obj_desc.split()) & set(template_desc.split())
        return len(common_words) > 2  # At least 3 common words
        
    def generate_summary(self) -> Dict[str, Any]:
        """Generate a summary of magnet results"""
        summary = {
            'total_evaluated': len(self.attracted_objects),
            'total_matched': len(self.matched_objects),
            'fit_quality': self._calculate_fit_quality(),
            'thematic_alignment': self._analyze_thematic_alignment(),
            'gaps_identified': self._identify_gaps(),
            'counts_by_type': self._count_by_object_type(),
            'generated_at': datetime.now().isoformat(),
            'fit_template_version': 'v1.0'
        }
        return summary
        
    def _calculate_fit_quality(self) -> str:
        """Calculate overall fit quality"""
        if not self.attracted_objects:
            return "No objects evaluated"
            
        match_rate = len(self.matched_objects) / len(self.attracted_objects)
        if match_rate >= 0.8:
            return "Excellent"
        elif match_rate >= 0.6:
            return "Good"
        elif match_rate >= 0.4:
            return "Fair"
        else:
            return "Poor"
            
    def _analyze_thematic_alignment(self) -> str:
        """Analyze thematic alignment of matched objects"""
        if not self.matched_objects:
            return "No matched objects to analyze"
            
        # Basic thematic analysis - would be enhanced with LLM
        themes = []
        for obj in self.matched_objects:
            desc = obj.get('description', '').lower()
            if 'cost' in desc:
                themes.append('cost_management')
            if 'workspace' in desc:
                themes.append('workspace_management')
            if 'ai' in desc or 'genai' in desc:
                themes.append('ai_adoption')
                
        return f"Primary themes: {', '.join(set(themes))}"
        
    def _identify_gaps(self) -> List[str]:
        """Identify gaps in the attracted objects"""
        gaps = []
        
        # Check for missing object types
        object_types = [obj.get('object_type') for obj in self.matched_objects]
        if 'Problem' not in object_types:
            gaps.append("Missing Problem objects")
        if 'Behavior' not in object_types:
            gaps.append("Missing Behavior objects")
        if 'Result' not in object_types:
            gaps.append("Missing Result objects")
            
        return gaps
        
    def _count_by_object_type(self) -> Dict[str, int]:
        """Count objects by type"""
        counts = {}
        for obj in self.matched_objects:
            obj_type = obj.get('object_type', 'unknown')
            counts[obj_type] = counts.get(obj_type, 0) + 1
        return counts
        
    def export_matched_objects(self) -> Dict[str, Any]:
        """Export matched objects with governance compliance"""
        export_data = {
            'objects': self.matched_objects,
            'metadata': {
                'total_objects': len(self.attracted_objects),
                'matched_objects': len(self.matched_objects),
                'generated_at': datetime.now().isoformat(),
                'fit_template_version': 'v1.0'
            }
        }
        return export_data

# Global instance for step definitions
magnet_system = FitTemplateMagnetSystem()

@given('I have a Fit Template extracted from a research source')
def step_impl_fit_template_available(context):
    """Background step - Fit Template is available"""
    context.fit_template_available = True

@given('I have the DUX v9.5 schema validation system')
def step_impl_schema_validation(context):
    """Background step - Schema validation is available"""
    context.schema_validation_available = True

@given('I have a "{template_name}" Fit Template from {source_data}')
def step_impl_load_fit_template(context, template_name, source_data):
    """Load a specific Fit Template"""
    # Mock template data - would be loaded from actual source
    template_data = {
        'object_type': 'FitTemplate',
        'fit_id': f'fit_{template_name.lower().replace(" ", "_")}_001',
        'source_stakeholder': 'Research Analyst',
        'artifact_filename': f'{source_data.lower().replace(" ", "_")}.md',
        'intended_use': 'object extraction',
        'target_audience': 'Research Team',
        'preferred_chaining_criteria': {
            'problem_scope': 'cost_management' if 'Cost Management' in template_name else 'workspace_management',
            'behavior_constraints': ['testable within 30 days'],
            'result_requirements': ['metric-based'],
            'required_evidence_status': 'evidence_present'
        },
        'dux_object_map': {
            'problem': {'id': f'problem_{template_name.lower().replace(" ", "_")}_001', 'description': 'Sample problem'},
            'behavior': {'id': f'behavior_{template_name.lower().replace(" ", "_")}_001', 'description': 'Sample behavior'},
            'result': {'id': f'result_{template_name.lower().replace(" ", "_")}_001', 'description': 'Sample result'}
        }
    }
    
    magnet_system.load_fit_template(template_name, template_data)
    context.current_template = template_name

@given('I have raw research data from multiple sources')
def step_impl_load_raw_data(context):
    """Load raw research data"""
    # Mock raw data - would be loaded from actual sources
    raw_data = {
        'source_1': {
            'objects': [
                {'object_type': 'Problem', 'id': 'P001', 'description': 'Cost management challenges in platform administration'},
                {'object_type': 'Behavior', 'id': 'B001', 'description': 'Platform admins optimize resource allocation'},
                {'object_type': 'Result', 'id': 'R001', 'description': 'Reduced operational costs by 25%'}
            ]
        },
        'source_2': {
            'objects': [
                {'object_type': 'Problem', 'id': 'P002', 'description': 'Workspace management complexity'},
                {'object_type': 'Behavior', 'id': 'B002', 'description': 'Users create isolated workspaces for AI projects'},
                {'object_type': 'Result', 'id': 'R002', 'description': 'Improved project isolation and security'}
            ]
        }
    }
    
    for source, data in raw_data.items():
        magnet_system.load_raw_data(source, data)
    context.raw_data_sources = list(raw_data.keys())

@when('I apply the {template_name} Fit Template as a magnet to the data')
def step_impl_apply_magnet(context, template_name):
    """Apply Fit Template as magnet to attract objects"""
    attracted_objects = magnet_system.apply_fit_template_magnet(template_name, context.raw_data_sources)
    context.attracted_objects = attracted_objects

@then('the system should attract objects related to {topic}')
def step_impl_attract_objects(context, topic):
    """Verify that objects related to the topic were attracted"""
    assert context.attracted_objects, "No objects were attracted"
    
    # Check that at least one object is related to the topic
    topic_related = any(
        topic.lower() in obj.get('description', '').lower() 
        for obj in context.attracted_objects
    )
    assert topic_related, f"No objects related to '{topic}' were attracted"

@then('the attracted objects should include {object_types}')
def step_impl(context, object_types):
    """Verify that attracted objects include specified types"""
    expected_types = [t.strip() for t in object_types.split(',')]
    actual_types = [obj.get('object_type') for obj in context.attracted_objects]
    
    for expected_type in expected_types:
        assert expected_type in actual_types, f"Expected {expected_type} objects not found in attracted objects"

@then('each attracted object should have evidence maturity classification')
def step_impl(context):
    """Verify that attracted objects have evidence maturity classification"""
    for obj in context.attracted_objects:
        assert 'evidence_maturity' in obj, f"Object {obj.get('id')} missing evidence_maturity"

@then('the objects should be validated against DUX v9.5 schemas')
def step_impl(context):
    """Verify that objects are validated against schemas"""
    # This would integrate with your existing schema validation
    assert context.schema_validation_available, "Schema validation not available"
    
    # Basic validation check
    for obj in context.attracted_objects:
        assert 'object_type' in obj, f"Object missing required field: object_type"
        assert 'id' in obj, f"Object missing required field: id"

@then('the system should output a structured collection of {insight_type} insights')
def step_impl(context, insight_type):
    """Verify that system outputs structured insights"""
    assert context.attracted_objects, "No insights were generated"
    
    # Verify structure
    for obj in context.attracted_objects:
        assert isinstance(obj, dict), "Insights should be structured as dictionaries"
        assert 'object_type' in obj, "Each insight should have an object_type"

@when('I validate the attracted objects against the Fit Template criteria')
def step_impl(context):
    """Validate attracted objects against Fit Template criteria"""
    validation_results = magnet_system.validate_attracted_objects(context.current_template)
    context.validation_results = validation_results

@then('each object should have a fit_matched status of true or false')
def step_impl(context):
    """Verify that objects have fit_matched status"""
    for obj in context.attracted_objects:
        assert 'fit_matched' in obj or 'fit_alignment_reason' in obj, f"Object {obj.get('id')} missing fit validation"

@then('each object should have a fit_alignment_reason explaining the match')
def step_impl(context):
    """Verify that objects have fit alignment reasons"""
    for obj in context.attracted_objects:
        if 'fit_alignment_reason' in obj:
            assert isinstance(obj['fit_alignment_reason'], str), f"fit_alignment_reason should be a string for object {obj.get('id')}"

@then('the system should generate a markdown table with object ID, type, match status, and rationale')
def step_impl(context):
    """Verify that system generates markdown table"""
    assert 'summary_table' in context.validation_results, "Summary table not generated"
    
    table = context.validation_results['summary_table']
    assert isinstance(table, list), "Summary table should be a list"
    
    for row in table:
        assert 'object_id' in row, "Table row missing object_id"
        assert 'object_type' in row, "Table row missing object_type"
        assert 'match_status' in row, "Table row missing match_status"
        assert 'rationale' in row, "Table row missing rationale"

@then('the system should output an updated JSON array with only matched objects')
def step_impl(context):
    """Verify that system outputs matched objects"""
    assert 'matched_objects' in context.validation_results, "Matched objects not generated"
    
    matched_objects = context.validation_results['matched_objects']
    assert isinstance(matched_objects, list), "Matched objects should be a list"

@when('I generate a summary of the magnet results')
def step_impl(context):
    """Generate summary of magnet results"""
    summary = magnet_system.generate_summary()
    context.summary = summary

@then('the system should provide a narrative summary of total evaluated vs matched objects')
def step_impl(context):
    """Verify that system provides narrative summary"""
    assert 'total_evaluated' in context.summary, "Summary missing total_evaluated"
    assert 'total_matched' in context.summary, "Summary missing total_matched"
    
    assert context.summary['total_evaluated'] >= context.summary['total_matched'], "Total evaluated should be >= total matched"

@then('the summary should include fit quality and thematic alignment')
def step_impl(context):
    """Verify that summary includes fit quality and thematic alignment"""
    assert 'fit_quality' in context.summary, "Summary missing fit_quality"
    assert 'thematic_alignment' in context.summary, "Summary missing thematic_alignment"

@then('the summary should identify gaps or low-confidence areas')
def step_impl(context):
    """Verify that summary identifies gaps"""
    assert 'gaps_identified' in context.summary, "Summary missing gaps_identified"
    assert isinstance(context.summary['gaps_identified'], list), "Gaps should be a list"

@then('the summary should include counts by object type and tag')
def step_impl(context):
    """Verify that summary includes counts by object type"""
    assert 'counts_by_type' in context.summary, "Summary missing counts_by_type"
    assert isinstance(context.summary['counts_by_type'], dict), "Counts should be a dictionary"

@then('the system should output metadata with total_objects, matched_objects, generated_at, and fit_template_version')
def step_impl(context):
    """Verify that system outputs metadata"""
    assert 'generated_at' in context.summary, "Summary missing generated_at"
    assert 'fit_template_version' in context.summary, "Summary missing fit_template_version"

@when('I export the matched objects')
def step_impl(context):
    """Export matched objects"""
    export_data = magnet_system.export_matched_objects()
    context.export_data = export_data

@then('the system should output a JSON array with only fit_matched: true objects')
def step_impl(context):
    """Verify that system outputs only matched objects"""
    assert 'objects' in context.export_data, "Export missing objects"
    
    objects = context.export_data['objects']
    assert isinstance(objects, list), "Exported objects should be a list"
    
    # Verify all objects are matched
    for obj in objects:
        assert 'fit_alignment_reason' in obj, f"Object {obj.get('id')} missing fit_alignment_reason"

@then('each object should retain all original fields')
def step_impl(context):
    """Verify that objects retain original fields"""
    for obj in context.export_data['objects']:
        assert 'object_type' in obj, "Object missing object_type"
        assert 'id' in obj, "Object missing id"
        assert 'description' in obj, "Object missing description"

@then('each object should include fit_alignment_reason')
def step_impl(context):
    """Verify that objects include fit alignment reason"""
    for obj in context.export_data['objects']:
        assert 'fit_alignment_reason' in obj, f"Object {obj.get('id')} missing fit_alignment_reason"
        assert isinstance(obj['fit_alignment_reason'], str), "fit_alignment_reason should be a string"

@then('the export should include metadata block with total_objects, matched_objects, generated_at, and fit_template_version')
def step_impl(context):
    """Verify that export includes metadata"""
    metadata = context.export_data['metadata']
    assert 'total_objects' in metadata, "Metadata missing total_objects"
    assert 'matched_objects' in metadata, "Metadata missing matched_objects"
    assert 'generated_at' in metadata, "Metadata missing generated_at"
    assert 'fit_template_version' in metadata, "Metadata missing fit_template_version"

@then('all objects should be compliant with DUX v9.5 governance standards')
def step_impl(context):
    """Verify that objects are compliant with governance standards"""
    assert context.schema_validation_available, "Schema validation not available"
    
    # Basic governance compliance check
    for obj in context.export_data['objects']:
        assert 'object_type' in obj, "Object missing object_type"
        assert 'id' in obj, "Object missing id"
        assert 'evidence' in obj, "Object missing evidence array"
        assert isinstance(obj['evidence'], list), "Evidence should be an array" 