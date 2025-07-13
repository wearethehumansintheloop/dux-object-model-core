import argparse
import os
import json
import yaml
import requests
import uuid

def call_ollama(prompt: str, model_name: str, base_url: str) -> dict:
    """
    Sends a prompt to the Ollama API and returns the parsed JSON response.
    """
    api_url = f"{base_url.rstrip('/')}/api/generate"
    payload = {
        "model": model_name,
        "prompt": prompt,
        "stream": False,
        "format": "json"
    }
    print(f"Querying Ollama with model {model_name}...")
    try:
        response = requests.post(api_url, json=payload, timeout=300)
        response.raise_for_status()
        
        response_data = response.json()
        llm_output_str = response_data.get("response", "{}")
        
        print(f"LLM Raw Response String: {llm_output_str}") # Add this line for debugging
        return json.loads(llm_output_str)
    except requests.exceptions.RequestException as e:
        print(f"Error calling Ollama API: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON from LLM response: {e}")
        print(f"Raw response was: {llm_output_str}")
        return None

def main():
    """
    Main function to run the extraction pipeline.
    """
    parser = argparse.ArgumentParser(description="Extract structured objects from text using an LLM.")
    parser.add_argument("--prompt_template_path", required=True, help="Path to the prompt template file.")
    parser.add_argument("--source_transcript_path", required=True, help="Path to the source transcript file.")
    parser.add_argument("--output_dir", required=True, help="Directory to save the output YAML files.")
    parser.add_argument("--chunk_size", type=int, default=2000, help="Size of text chunks to process.")
    parser.add_argument("--ollama_model_name", required=True, help="Name of the Ollama model to use (e.g., 'llama3').")
    parser.add_argument("--ollama_base_url", required=True, help="Base URL of the Ollama API.")
    args = parser.parse_args()

    # --- 1. Load Inputs ---
    print("Loading prompt template and source transcript...")
    with open(args.prompt_template_path, 'r') as f:
        prompt_template = f.read()
    with open(args.source_transcript_path, 'r') as f:
        transcript = f.read()

    # --- 2. Prepare Output Directory ---
    output_problem_dir = os.path.join(args.output_dir, "problems")
    os.makedirs(output_problem_dir, exist_ok=True)
    print(f"Output will be saved to: {output_problem_dir}")

    # --- 3. Process Transcript in Chunks ---
    chunks = [transcript[i:i + args.chunk_size] for i in range(0, len(transcript), args.chunk_size)]
    print(f"Transcript split into {len(chunks)} chunks.")

    for i, chunk in enumerate(chunks):
        print(f"\n--- Processing Chunk {i+1}/{len(chunks)} ---")
        
        full_prompt = prompt_template.replace("{{source_text}}", chunk).replace("{{existing_objects}}", "[]")
        
        # --- 4. Call LLM ---
        extracted_data = call_ollama(full_prompt, args.ollama_model_name, args.ollama_base_url)

        problems = []
        if extracted_data:
            if 'problems' in extracted_data and isinstance(extracted_data['problems'], list):
                problems = extracted_data['problems']
            elif isinstance(extracted_data, dict) and extracted_data.get('object_type') == 'Problem':
                # Handle the case where a single problem object is returned
                problems = [extracted_data]

        if not problems:
            print("No valid 'problems' data extracted from this chunk.")
            continue

        # --- 5. Save Extracted Objects ---
        print(f"LLM extracted {len(problems)} Problem object(s) from this chunk.")
        for problem in problems:
            # If the LLM didn't assign an ID, create one.
            problem_id = problem.get('id', f"problem_{uuid.uuid4().hex[:8]}")
            problem['id'] = problem_id

            # --- Create Markdown Content ---
            md_content = []
            md_content.append(f"# Problem: {problem.get('name', 'N/A')}")
            md_content.append(f"\n**ID:** `{problem_id}`")
            if 'description' in problem:
                md_content.append(f"\n## Description\n{problem['description']}")
            if 'evidence' in problem and isinstance(problem['evidence'], list):
                md_content.append("\n## Evidence")
                for ev in problem['evidence']:
                    md_content.append(f"- {ev}")
            
            md_content.append("\n## Raw JSON Object")
            md_content.append("```json")
            md_content.append(json.dumps(problem, indent=4))
            md_content.append("```")

            # --- Save as Markdown file ---
            file_path = os.path.join(output_problem_dir, f"{problem_id}.md")
            with open(file_path, 'w') as f:
                f.write("\n".join(md_content))
            print(f"  - Saved {file_path}")

    print("\nExtraction pipeline finished.")

if __name__ == "__main__":
    main()