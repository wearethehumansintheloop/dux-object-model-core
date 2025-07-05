"""
Generator: generate_from_schema.py
Purpose: Auto-generate prompt templates based on split schema files.
"""

import json
from pathlib import Path

def generate_prompt_from_schema(name, schema):
    return f"# Prompt for {name}\nDescribe a {name} object with attributes: {', '.join(schema['properties'].keys())}\n"

def main():
    schema_dir = Path("schemas")
    output_dir = Path("scripts/prompts_from_schema")
    output_dir.mkdir(parents=True, exist_ok=True)

    for schema_file in schema_dir.glob("*.schema.json"):
        name = schema_file.stem
        schema = json.loads(schema_file.read_text())
        prompt = generate_prompt_from_schema(name, schema)
        (output_dir / f"{name}_prompt.txt").write_text(prompt)

if __name__ == "__main__":
    main()
