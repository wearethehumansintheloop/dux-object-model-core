#!/usr/bin/env python3
"""
Schema-aware prompt generator for DUX v9.5 objects.
Updates prompts to include actual schema definitions and v9.5 evidence requirements.
Version: v9.5.1 - Schema path updated, version tracking added
Generated: 2025-07-01
"""

import json
import shutil
from pathlib import Path

def load_schema(schema_path):
    """Load and return a DUX object schema."""
    with open(schema_path, 'r') as f:
        return json.load(f)

def generate_evidence_template():
    """Generate the v9.5 evidence structure template based on actual meta schema."""
    return '''## Required Evidence Structure (v9.5):
```json
"evidence": [
  {
    "teaser": "Brief summary or hook that captures the essence of this evidence",
    "quote": "Direct quote or summary from source material",
    "citation": "Who said it, when, and where (e.g. 'Participant 7, timestamp 00:12:45, interview_transcript_p7.md')",
    "provenance": {
      "source_filename": "source_file_name",
      "timestamp_in": "start_timestamp",
      "timestamp_out": "end_timestamp"
    },
    "evidence_type": "qualitative|quantitative|system_log|user_interview|report_summary",
    "collection_method": "interview|survey",
    "confidence_level": "high|medium|low"
  }
]
```'''

def extract_schema_properties(schema, object_type):
    """Extract comprehensive properties from schema for prompt generation."""
    properties = schema.get('properties', {})
    required = schema.get('required', [])
    
    # Core fields present in all objects
    core_fields = ['object_type', 'id', 'evidence_status']
    
    # Get object-specific fields with detailed information
    exclude_fields = {'object_type', 'id', 'evidence', 'evidence_status', 'tags', 'created_at', 'updated_at'}
    
    specific_fields = []
    required_fields = []
    conditional_fields = []
    enum_fields = []
    
    for field, definition in properties.items():
        if field not in exclude_fields:
            desc = definition.get('description', '')
            field_type = definition.get('type', 'unknown')
            
            # Check if field is required
            if field in required:
                required_fields.append(f"- **{field}** ({field_type}): {desc}")
            else:
                specific_fields.append(f"- **{field}** ({field_type}): {desc}")
            
            # Check for enums
            if 'enum' in definition:
                enum_values = ', '.join(definition['enum'])
                enum_fields.append(f"- **{field}**: {enum_values}")
            
            # Check for pattern validation
            if 'pattern' in definition:
                pattern = definition['pattern']
                specific_fields.append(f"  - Pattern: `{pattern}`")
    
    # Check for conditional requirements (if/then)
    if 'if' in schema:
        if_condition = schema['if']
        then_requirement = schema.get('then', {})
        conditional_fields.append(f"- If {if_condition}, then {then_requirement}")
    
    return {
        'core_fields': core_fields,
        'required_fields': required_fields,
        'specific_fields': specific_fields,
        'enum_fields': enum_fields,
        'conditional_fields': conditional_fields
    }

def update_prompt_with_schema(prompt_path, schema_path, object_type):
    """Update a prompt file to include schema-aware information."""
    
    # Load the schema
    schema = load_schema(schema_path)
    schema_info = extract_schema_properties(schema, object_type)
    
    # Generate enum section if applicable
    enum_section = ""
    if schema_info['enum_fields']:
        enum_section = f"""
### Allowed Values:
{'\n'.join(schema_info['enum_fields'])}
"""
    
    # Generate conditional section if applicable
    conditional_section = ""
    if schema_info['conditional_fields']:
        conditional_section = f"""
### Conditional Requirements:
{'\n'.join(schema_info['conditional_fields'])}
"""

    # Load the original prompt content
    with open(prompt_path, 'r') as f:
        original_prompt = f.read()

    # Define the new content to be injected
    schema_injection = f"""
## Schema Information
**Schema Reference:** `{schema_path}`

### Core Required Attributes:
- object_type: "{object_type}"
- id: Unique identifier
- evidence_status: "evidence_backed", "evidence_present", or "assumptive"

### Required {object_type}-Specific Fields:
{chr(10).join(schema_info['required_fields'])}

### Optional {object_type}-Specific Fields:
{chr(10).join(schema_info['specific_fields'])}

{enum_section}

{conditional_section}
"""

    # Replace the old schema section with the new one
    # This is a simple replacement, assuming a marker like "## Prompt Template"
    # A more robust solution would use more specific markers
    
    start_marker = "## Prompt Template"
    end_marker = "## Required Evidence Structure (v9.5):"
    
    start_index = original_prompt.find(start_marker)
    end_index = original_prompt.find(end_marker)
    
    if start_index != -1 and end_index != -1:
        new_prompt = (original_prompt[:start_index + len(start_marker)] +
                      '\n' + schema_injection + '\n' +
                      original_prompt[end_index:])
    else:
        # If markers are not found, append to the end
        new_prompt = original_prompt + '\n' + schema_injection

    # Write the updated prompt back to the file
    with open(prompt_path, 'w') as f:
        f.write(new_prompt)
    print(f"Updated prompt: {prompt_path}")

def main():
    """Main function to drive prompt generation."""
    
    # Define paths relative to the script's location
    script_dir = Path(__file__).parent
    base_dir = script_dir.parent.parent  # Assuming script is in src/generators
    
    schema_dir = base_dir / 'src' / 'dux_v9.5_split_schema'
    prompt_dir = base_dir / 'src' / 'prompt_templates'

    # Mapping of object types to their schema and prompt files
    object_map = {
        'Behavior': 'dux_object_behavior.json',
        'Flow': 'dux_object_flow.json',
        'Problem': 'dux_object_problem.json',
        'Result': 'dux_object_result.json',
        'UserOutcome': 'dux_object_useroutcome.json',
        'Provenance': 'dux_object_provenance.json'
    }

    for object_type, schema_file in object_map.items():
        schema_path = schema_dir / schema_file
        prompt_path = prompt_dir / f"{object_type.lower()}_prompt.md"
        
        if schema_path.exists() and prompt_path.exists():
            update_prompt_with_schema(prompt_path, str(schema_path), object_type)
        else:
            if not schema_path.exists():
                print(f"Schema not found: {schema_path}")
            if not prompt_path.exists():
                print(f"Prompt not found: {prompt_path}")

if __name__ == "__main__":
    main()
