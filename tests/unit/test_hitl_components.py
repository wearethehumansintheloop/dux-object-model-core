#!/usr/bin/env python3
"""
Unit tests for HITL pipeline components
Run with: pytest tests/unit/test_hitl_components.py
"""

import pytest
import tempfile
from pathlib import Path
import sys
import json

# Add the validation scripts to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts" / "validation" / "hitl_pipeline"))

from stage1_structure_validation import validate_dux_template_structure
from stage2_consistency_validation import extract_schema_attributes, extract_json_example, validate_schema_json_consistency
from stage3a_problem_docling_md import extract_schema_table_from_markdown, generate_json_schema_from_table
from hitl_orchestrator import check_naming_convention


class TestStage1Structure:
    """Test Stage 1 structure validation."""
    
    def test_valid_problem_structure(self):
        """Test valid Problem object structure."""
        content = """# 🧩 Problem Object

## 🎯 Purpose & Strategic Role
Test purpose

## 🧠 "What would you say... you do here?"
> Test JTBD

## 💡 Why the Problem Object Matters
- Test matters

## 📋 Schema Attributes
| Attribute | Type | Required |
|-----------|------|----------|
| test | string | Yes |

## 📦 Canonical Example (Schema-Compliant)
```json
{"test": "value"}
```

## 🔗 Structural Role & Usage Notes
- Test notes
"""
        errors = validate_dux_template_structure(content)
        assert len(errors) == 0
    
    def test_missing_required_section(self):
        """Test missing required section."""
        content = """# 🧩 Problem Object

## 🎯 Purpose & Strategic Role
Test purpose

## 📋 Schema Attributes
| Attribute | Type | Required |
|-----------|------|----------|
| test | string | Yes |
"""
        errors = validate_dux_template_structure(content)
        assert len(errors) > 0
        assert any("What would you say" in error for error in errors)
    
    def test_invalid_header_emoji(self):
        """Test invalid header emoji."""
        content = """# 🎮 Problem Object

## 🎯 Purpose & Strategic Role
Test purpose
"""
        errors = validate_dux_template_structure(content)
        assert len(errors) > 0
        assert any("Invalid header emoji" in error for error in errors)


class TestStage2Consistency:
    """Test Stage 2 consistency validation."""
    
    def test_extract_schema_attributes(self):
        """Test schema attribute extraction."""
        content = """## 📋 Schema Attributes
| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| id | string | Yes | Unique ID |
| name | string | No | Object name |
"""
        attrs = extract_schema_attributes(content)
        assert attrs is not None
        assert len(attrs['attributes']) == 2
        assert attrs['attributes'][0]['Attribute'] == 'id'
        assert attrs['attributes'][0]['Type'] == 'string'
        assert attrs['attributes'][0]['Required'] == 'Yes'
    
    def test_extract_json_example(self):
        """Test JSON example extraction."""
        content = """## 📦 Canonical Example
```json
{
  "id": "test_001",
  "name": "Test Object"
}
```
"""
        json_obj = extract_json_example(content)
        assert json_obj is not None
        assert json_obj['id'] == 'test_001'
        assert json_obj['name'] == 'Test Object'
    
    def test_consistency_validation(self):
        """Test schema-JSON consistency validation."""
        schema_attrs = {
            'attributes': [
                {'Attribute': 'id', 'Type': 'string', 'Required': 'Yes'},
                {'Attribute': 'name', 'Type': 'string', 'Required': 'No'}
            ]
        }
        
        # Valid JSON
        json_obj = {'id': 'test_001', 'name': 'Test'}
        errors = validate_schema_json_consistency(schema_attrs, json_obj)
        assert len(errors) == 0
        
        # Missing required field
        json_obj = {'name': 'Test'}
        errors = validate_schema_json_consistency(schema_attrs, json_obj)
        assert len(errors) > 0
        assert any("Required field 'id' missing" in error for error in errors)
        
        # Extra field not in schema
        json_obj = {'id': 'test_001', 'extra': 'field'}
        errors = validate_schema_json_consistency(schema_attrs, json_obj)
        assert len(errors) > 0
        assert any("'extra' not defined in schema" in error for error in errors)


class TestStage3aGeneration:
    """Test Stage 3a JSON schema generation."""
    
    def test_generate_simple_schema(self):
        """Test generating simple JSON schema from table."""
        schema_data = {
            'attributes': [
                {'Attribute': 'id', 'Type': 'string', 'Required': 'Yes', 'Description': 'Unique ID'},
                {'Attribute': 'count', 'Type': 'number', 'Required': 'No', 'Description': 'Item count'}
            ]
        }
        
        json_schema = generate_json_schema_from_table(schema_data)
        
        assert json_schema['type'] == 'object'
        assert 'id' in json_schema['properties']
        assert 'count' in json_schema['properties']
        assert 'id' in json_schema['required']
        assert 'count' not in json_schema['required']
        assert json_schema['properties']['id']['type'] == 'string'
        assert json_schema['properties']['count']['type'] == 'number'
    
    def test_generate_complex_schema(self):
        """Test generating schema with complex nested objects."""
        schema_data = {
            'attributes': [
                {'Attribute': 'job_statement', 'Type': 'object', 'Required': 'Yes', 'Description': 'JTBD'},
                {'Attribute': 'evidence', 'Type': '[object]', 'Required': 'Yes', 'Description': 'Evidence array'},
                {'Attribute': 'tags', 'Type': '[string]', 'Required': 'No', 'Description': 'Tags'}
            ]
        }
        
        json_schema = generate_json_schema_from_table(schema_data)
        
        # Check job_statement has nested structure
        assert json_schema['properties']['job_statement']['type'] == 'object'
        assert 'user_scenario' in json_schema['properties']['job_statement']['properties']
        
        # Check evidence array structure
        assert json_schema['properties']['evidence']['type'] == 'array'
        assert json_schema['properties']['evidence']['items']['type'] == 'object'
        assert 'provenance_id' in json_schema['properties']['evidence']['items']['properties']
        
        # Check simple array
        assert json_schema['properties']['tags']['type'] == 'array'
        assert json_schema['properties']['tags']['items']['type'] == 'string'


class TestNamingConvention:
    """Test naming convention validation."""
    
    def test_valid_object_names(self):
        """Test valid object type detection."""
        test_cases = [
            ("problem_financial_001.md", True, "problem"),
            ("behavior_user_action.md", True, "behavior"), 
            ("20250707_insight_analysis.md", True, "insight"),
            ("result_efficiency_metric.md", True, "result"),
            ("provenance_survey_q3.md", True, "provenance"),
            ("useroutcome_goal_achieved.md", True, "useroutcome"),
            ("flow_checkout_process.md", True, "flow")
        ]
        
        for filename, expected_valid, expected_type in test_cases:
            is_valid, obj_type = check_naming_convention(Path(filename))
            assert is_valid == expected_valid, f"Failed for {filename}"
            if expected_valid:
                assert obj_type == expected_type, f"Wrong type for {filename}: got {obj_type}, expected {expected_type}"
    
    def test_invalid_object_names(self):
        """Test invalid object names."""
        test_cases = [
            "invalid_name.md",
            "test_file.md",
            "random_document.md",
            "my-file.md",
            "data.md"
        ]
        
        for filename in test_cases:
            is_valid, obj_type = check_naming_convention(Path(filename))
            assert not is_valid, f"Should be invalid: {filename}"
            assert obj_type == "", f"Should have empty type: {filename}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])