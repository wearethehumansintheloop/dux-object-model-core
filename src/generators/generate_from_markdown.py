"""
Generator: generate_from_markdown.py v9.5
Purpose: Extract prompt templates from DUX v9.5 object model guide markdown definitions.
Schema-aware generation with version tracking.
"""

from pathlib import Path
import re

def extract_prompts_from_markdown(md_text, version="v9.4"):
    """Extract DUX object definitions and create prompt templates."""
    prompts = {}
    
    # Extract core object definitions (Problem, Behavior, Result)
    core_object_pattern = r"^### (Problem|Behavior|Result)\s*\n(.+?)(?=^###|\Z)"
    
    for match in re.finditer(core_object_pattern, md_text, re.DOTALL | re.MULTILINE):
        object_name, body = match.groups()
        
        # Extract the first meaningful line as description
        lines = [line.strip() for line in body.strip().splitlines() if line.strip() and not line.startswith("**")]
        description = lines[0] if lines else f"DUX {version} {object_name} object definition"
        
        # Create a detailed prompt template for DUX objects
        prompt_content = f"""# DUX {version} {object_name} Object Prompt Template

## Object Description
{description}

## Prompt Template
Create a {object_name} object that follows the DUX {version} specification:

**Object Type:** {object_name}
**Purpose:** {description}

Please define the following core attributes:
- object_type: "{object_name}"
- id: Unique identifier
- description: Clear, specific description following DUX v9.4 format
- evidence: Supporting evidence for this {object_name.lower()}
- evidence_status: "evidence_backed", "evidence_present", or "assumptive"

{object_name}-specific attributes (refer to schema):
{_extract_object_attributes(body, object_name)}

Ensure the {object_name.lower()} follows DUX {version} principles:
- Atomicity: Each object serves a single, clear purpose
- Traceability: Clear relationships to other objects
- Evidence-backed: Supported by concrete evidence
"""
        
        prompts[object_name.lower()] = prompt_content
    
    # Extract Junction Objects (Flow, UserOutcome) - updated for v9.5
    junction_pattern = r"^### (Flow|UserOutcome).*?\n(.+?)(?=^###|\Z)"
    
    for match in re.finditer(junction_pattern, md_text, re.DOTALL | re.MULTILINE):
        object_name, body = match.groups()
        
        lines = [line.strip() for line in body.strip().splitlines() if line.strip() and not line.startswith("**")]
        description = lines[0] if lines else f"DUX {version} {object_name} junction object"
        
        # Handle Flow and UserOutcome objects (v9.5 no longer has Journey)
        prompt_content = f"""# DUX {version} {object_name} Object Prompt Template

## Object Description
{description}

## Prompt Template
Create a {object_name} object (Junction Object) that follows the DUX {version} specification:

**Object Type:** {object_name}
**Category:** Junction Object (Relationship/Experience)
**Purpose:** {description}

Please define the following core attributes:
- object_type: "{object_name}"
- id: Unique identifier
- Junction-specific relationships and orchestration fields

{object_name}-specific attributes (refer to schema):
{_extract_object_attributes(body, object_name)}

Junction Object principles:
- Orchestration: Manages relationships between core objects
- Experience flow: Defines user experience sequences  
- Evidence aggregation: Inherits evidence from linked objects
"""
        
        prompts[object_name.lower()] = prompt_content
    
    return prompts

def _extract_object_attributes(body_text, object_name):
    """Extract key attributes mentioned in the object definition."""
    # Look for attribute mentions in the body text
    attributes = []
    
    # Common patterns to look for
    attribute_patterns = [
        r"- `(\w+)`:",
        r"\*\*(\w+)\*\*:",
        r"(\w+_\w+):",
        r"`(\w+_\w+)`"
    ]
    
    for pattern in attribute_patterns:
        matches = re.findall(pattern, body_text)
        attributes.extend(matches)
    
    # Remove duplicates and common words
    unique_attrs = list(set(attr for attr in attributes 
                           if attr not in ['object_type', 'id', 'description', 'evidence']))
    
    if unique_attrs:
        return "- " + "\n- ".join(unique_attrs[:10])  # Limit to first 10
    else:
        return f"- Additional {object_name.lower()}-specific fields as defined in the schema"

def main():
    # Handle running from either root directory or src directory
    md_paths = [
        Path("docs/dux_object_model_guide_v_9_5.md"),  # v9.5 guide from root
        Path("src/dux_object_model_guide_v9.4.md"),    # Legacy v9.4 from root  
        Path("dux_object_model_guide_v9.4.md")         # Legacy from src
    ]
    
    md_path = None
    for path in md_paths:
        if path.exists():
            md_path = path
            break
    
    if md_path is None:
        print("Error: No DUX object model guide found. Looking for:")
        for path in md_paths:
            print(f"  - {path}")
        return
        
    output_dir = Path("scripts/prompts_from_markdown")
    output_dir.mkdir(parents=True, exist_ok=True)

    md_text = md_path.read_text()
    
    # Determine version from path
    version = "v9.5" if "v_9_5" in str(md_path) else "v9.4"
    
    prompts = extract_prompts_from_markdown(md_text, version)

    print(f"Extracted {len(prompts)} prompt templates from {md_path} ({version})")
    
    for name, prompt in prompts.items():
        output_file = output_dir / f"{name}_prompt.md"
        output_file.write_text(prompt)
        print(f"  ✓ Generated: {output_file}")
    
    print(f"\nAll prompt templates saved to: {output_dir}")

if __name__ == "__main__":
    main()
