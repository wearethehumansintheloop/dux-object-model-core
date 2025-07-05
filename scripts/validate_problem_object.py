import re
import json
from datetime import datetime
from pathlib import Path
import jsonschema

# Paths
HITL_REVIEW_DIR = Path("watch_folders/hitl_review/dux_object_model_9.6")
FAILED_DIR = HITL_REVIEW_DIR.parent / "HITL-failed"
SCHEMA_PATH = Path(
    "DUX Object Model (Core)/src/dux_v9.6_split_schema/dux_object_problem.json"
)

# Ensure failed dir exists
FAILED_DIR.mkdir(exist_ok=True)

# Load schema
with open(SCHEMA_PATH) as f:
    schema = json.load(f)


def extract_json_from_markdown(md_text):
    # Look for the first JSON code block in the markdown
    match = re.search(r'```json\s*(\{[\s\S]+?\})\s*```', md_text)
    if match:
        try:
            return json.loads(match.group(1))
        except Exception:
            return None
    return None


def validate_file(md_path):
    with open(md_path) as f:
        md_text = f.read()
    obj = extract_json_from_markdown(md_text)
    if not obj:
        return False, ["No valid JSON object found in markdown."]
    try:
        jsonschema.validate(obj, schema)
        return True, []
    except jsonschema.ValidationError as e:
        return False, [e.message]


def main():
    for md_file in HITL_REVIEW_DIR.glob("*problem*.md"):
        if not md_file.is_file():
            continue
        valid, errors = validate_file(md_file)
        if valid:
            print(f"PASS: {md_file.name}")
            continue
        # Prepare rejection
        timestamp = datetime.now().strftime("%Y%m%dT%H%M%S")
        new_name = (
            f"{md_file.stem}-review-{timestamp}-rejected.md"
        )
        failed_path = FAILED_DIR / new_name
        # Add error notes to top
        with open(md_file) as f:
            original = f.read()
        note = (
            f"<!--\nVALIDATION FAILED: {errors[0]}\nFile rejected at {timestamp}\n-->\n\n"
        )
        with open(failed_path, "w") as f:
            f.write(note + original)
        print(
            f"FAIL: {md_file.name} → {failed_path.name}"
        )
        md_file.unlink()  # Remove original


if __name__ == "__main__":
    main() 