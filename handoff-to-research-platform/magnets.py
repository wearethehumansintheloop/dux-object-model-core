# magnets.py

# This script is like a digital research assistant. It reads through research transcripts
# and other documents to find and organize important pieces of information, which we call
# "DUX objects." Think of it as a magnet that pulls out specific, valuable insights
# from a sea of text.

# The process works in a few stages:
# 1.  **Molecular Extraction:** We first pull out the smallest, most fundamental pieces
#     of information (like "Problems" people face or "Behaviors" they exhibit).
#     We call these "molecular" objects.
# 2.  **Junction Synthesis:** Next, we combine these small pieces into more complex
#     understandings, creating "Insight" objects that connect the dots. We call these
#     "junction" objects.
# 3.  **Validation:** Finally, we check all the information we've gathered against a
#     "Fit Template." This template acts like a quality check, ensuring that the
#     insights are relevant to our research goals.

# Everything this script produces is meant to be reviewed by a person (that's you!).
# We call this "Human-in-the-Loop" (HITL), and it's a core part of making sure our
# automated analysis is accurate and helpful.

import argparse
import os
import json
import requests
import uuid
from typing import List, Dict, Any

# The docling library has been removed to simplify the script and resolve import errors.
# We will use standard Python libraries for file handling.

def call_ollama(prompt: str, model_name: str, base_url: str) -> str:
    """
    Sends a prompt to the Ollama API and returns the raw string response.

    This function is our way of talking to the Large Language Model (LLM).
    We send it a carefully crafted prompt, and it sends back its "thoughts".
    The response is expected to contain a screenplay-style "think-aloud"
    section followed by a JSON object.
    """
    api_url = f"{base_url.rstrip('/')}/api/generate"
    payload = {
        "model": model_name,
        "prompt": prompt,
        "stream": False,
        # We are not using json format anymore as the screenplay format is not valid json
    }
    print(f"Querying Ollama with model {model_name}...")
    try:
        response = requests.post(api_url, json=payload, timeout=600)
        response.raise_for_status()
        
        response_data = response.json()
        llm_output_str = response_data.get("response", "")
        
        return llm_output_str
    except requests.exceptions.RequestException as e:
        print(f"Error calling Ollama API: {e}")
        return ""
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON from LLM response: {e}")
        print(f"Raw response was: {response.text}")
        return ""

def parse_agent_response(response_str: str, agent_name: str) -> (str, Dict[str, Any]):
    """
    Parses the combined screenplay and JSON output from an agent.

    Args:
        response_str: The raw string response from the Ollama API.
        agent_name: The name of the agent (e.g., 'ARCHIVIST').

    Returns:
        A tuple containing the screenplay log and the parsed JSON object.
    """
    log_entry = f"--- {agent_name} Log ---\n"
    json_object = {}

    # Find the end of the screenplay section
    end_scene_marker = "[END SCENE]"
    marker_pos = response_str.find(end_scene_marker)

    if marker_pos != -1:
        screenplay_part = response_str[:marker_pos + len(end_scene_marker)].strip()
        json_part = response_str[marker_pos + len(end_scene_marker):].strip()
        log_entry += f"{screenplay_part}\n"
    else:
        # If no marker, assume the whole response is a log or an error
        log_entry += f"No [END SCENE] marker found. Treating entire response as log.\n{response_str}\n"
        json_part = "{}"

    # Attempt to parse the JSON part
    try:
        json_object = json.loads(json_part)
    except json.JSONDecodeError:
        log_entry += f"--- JSON PARSE ERROR ---\nCould not decode JSON from the agent's response.\nRaw JSON part: {json_part}\n"

    
    log_entry += "--- End Log ---\n"
    return log_entry, json_object

# ...existing code...
def save_objects_to_disk(objects: List[Dict[str, Any]], output_dir: str, object_type_name: str):
    """
    Saves a list of DUX objects to a specified directory for HITL review.
    Each object is now saved as a standard .json file.

    This is our "Human-in-the-Loop" (HITL) step. Instead of just trusting the AI
    completely, we save its suggestions to a special folder for a person to review.
    This ensures quality and gives us a chance to correct any mistakes or
    misinterpretations.
    """
    if not objects:
        return

    review_dir = os.path.join(output_dir, "hitl_review")
    specific_output_dir = os.path.join(review_dir, f"{object_type_name.lower()}s")
    os.makedirs(specific_output_dir, exist_ok=True)

    print(f"--- Saving {len(objects)} CANDIDATE {object_type_name} objects in JSON format to {specific_output_dir} ---")
    for obj in objects:
        obj_id = obj.get('id', f"{object_type_name.lower()}_{uuid.uuid4().hex[:8]}")
        obj['id'] = obj_id

        # Serialize the object directly to a .json file
        file_path = os.path.join(specific_output_dir, f"{obj_id}.json")
        with open(file_path, 'w') as f:
            json.dump(obj, f, indent=4)
        print(f"  - Saved {file_path}")


def run_molecular_extraction_agent(
    prompt_template: str,
    transcript: str,
    existing_objects: List[Dict[str, Any]],
    chunk_size: int,
    model_name: str,
    base_url: str,
    object_type_name: str
) -> List[Dict[str, Any]]:
    """
    Runs a molecular extraction agent (e.g., Problem, Behavior) over a transcript.

    This is the first stage of our analysis. We take a long transcript and break it
    into smaller, more manageable chunks. For each chunk, we ask the AI to find
    specific, "atomic" pieces of information, like a user's problem or a specific
    behavior. We call these "molecular" objects because they're the basic
    building blocks of our understanding.
    """
    print(f"\n===== Running Molecular Extraction for: {object_type_name} ======")
    chunks = [transcript[i:i + chunk_size] for i in range(0, len(transcript), chunk_size)]
    print(f"Transcript split into {len(chunks)} chunks.")

    all_extracted_objects = list(existing_objects) # Start with existing objects

    for i, chunk in enumerate(chunks):
        print(f"\n--- Processing Chunk {i+1}/{len(chunks)} for {object_type_name}s ---")
        
        existing_objects_str = json.dumps(all_extracted_objects)
        full_prompt = prompt_template.replace("{{transcript}}", chunk).replace("{{existing_objects}}", existing_objects_str)
        
        llm_response_str = call_ollama(full_prompt, model_name, base_url)
        extracted_data = json.loads(llm_response_str)

        if not extracted_data:
            print("No valid data extracted from this chunk.")
            continue
        
        # Normalize response to a list of objects
        objects_in_chunk = []
        if isinstance(extracted_data, list):
            objects_in_chunk = extracted_data
        elif isinstance(extracted_data, dict) and f"{object_type_name.lower()}s" in extracted_data:
            objects_in_chunk = extracted_data[f"{object_type_name.lower()}s"]
        
        if not objects_in_chunk:
            print(f"No new {object_type_name} objects to process in this chunk.")
            continue
            
        print(f"LLM extracted {len(objects_in_chunk)} {object_type_name} object(s) from this chunk.")
        for obj in objects_in_chunk:
            if obj not in all_extracted_objects:
                 all_extracted_objects.append(obj)

    return all_extracted_objects

def run_synthesis_agent(
    prompt_template: str,
    molecular_objects: Dict[str, List[Dict[str, Any]]],
    model_name: str,
    base_url: str,
    object_type_name: str
) -> List[Dict[str, Any]]:
    """
    Runs a synthesis agent (e.g., Insight Architect) to create junction objects.

    This is where we start connecting the dots. After we've extracted the small,
    "molecular" objects (like Problems and Behaviors), this function feeds them
    to a more specialized AI agent. This "Insight Architect" looks for patterns
    and relationships between the smaller pieces to create a bigger picture,
    which we call an "Insight" or a "junction" object.
    """
    print(f"\n===== Running Synthesis for: {object_type_name} ======")
    
    # Replace placeholders for each type of molecular object
    full_prompt = prompt_template
    for obj_type, obj_list in molecular_objects.items():
        full_prompt = full_prompt.replace(f"{{{{{obj_type}}}}}", json.dumps(obj_list))

    llm_response_str = call_ollama(full_prompt, model_name, base_url)
    extracted_data = json.loads(llm_response_str)
    
    # Normalize response to a list of objects
    synthesized_objects = []
    if isinstance(extracted_data, list):
        synthesized_objects = extracted_data
    elif isinstance(extracted_data, dict) and f"{object_type_name.lower()}s" in extracted_data:
        synthesized_objects = extracted_data[f"{object_type_name.lower()}s"]
    elif isinstance(extracted_data, dict) and extracted_data.get("object_type") == object_type_name:
         synthesized_objects = [extracted_data]

    print(f"LLM synthesized {len(synthesized_objects)} {object_type_name} object(s).")
    return synthesized_objects


def run_validator_agent(
    prompt_template: str,
    objects_to_validate: List[Dict[str, Any]],
    fit_template_content: str,
    model_name: str,
    base_url: str,
    object_type_name: str
) -> List[Dict[str, Any]]:
    """
    Runs the Validator Agent to compare extracted objects against a Fit Template.

    This is our quality control step. A "Fit Template" defines what we're looking
    for in our research—our goals and hypotheses. This function takes each object
    the AI has found and asks another specialized agent, the "Validator," to check
    if it fits our template. This helps us filter out irrelevant information and
    focus on what really matters for our project.
    """
    print(f"\n===== Running Validation for: {object_type_name} ======")
    if not objects_to_validate:
        print(f"No {object_type_name} objects to validate.")
        return []

    # The fit_template_content is now passed in directly as a string.
    validated_objects = []
    for obj in objects_to_validate:
        print(f"  - Validating {object_type_name} ID: {obj.get('id', 'N/A')}")
        
        object_str = json.dumps(obj)
        full_prompt = prompt_template.replace("{{fit_template}}", fit_template_content).replace("{{object_to_validate}}", object_str)

        llm_response_str = call_ollama(full_prompt, model_name, base_url)
        
        try:
            validation_result = json.loads(llm_response_str)
            obj['fit_matched'] = validation_result.get('fit_matched', False)
            obj['fit_alignment_reason'] = validation_result.get('fit_alignment_reason', 'No reason provided by validator.')
            print(f"    - Matched: {obj['fit_matched']}")
        except json.JSONDecodeError:
            print(f"    - Error decoding validation response for object {obj.get('id', 'N/A')}.")
            obj['fit_matched'] = False
            obj['fit_alignment_reason'] = 'Error during validation process.'
        
        validated_objects.append(obj)
        
    return validated_objects

def run_user_flow_agent(
    prompt_template: str,
    molecular_objects: Dict[str, List[Dict[str, Any]]],
    model_name: str,
    base_url: str
) -> Dict[str, Any]:
    """
    Runs the User Flow agent to generate a user flow object.
    """
    print(f"\n===== Running User Flow Agent ======")
    
    # The prompt expects a single dictionary of all molecular objects.
    molecular_objects_str = json.dumps(molecular_objects)
    full_prompt = prompt_template.replace("{{molecular_objects}}", molecular_objects_str)

    llm_response_str = call_ollama(full_prompt, model_name, base_url)
    
    try:
        user_flow_object = json.loads(llm_response_str)
        print(f"LLM generated a User Flow titled: {user_flow_object.get('title', 'Untitled')}")
        return user_flow_object
    except json.JSONDecodeError:
        print("Error decoding User Flow response.")
        return {}


def main():
    """
    Main orchestration function to run the DUX extraction and synthesis pipeline.

    This is the conductor of our orchestra. It sets up the whole process,
    loads all the necessary files (like prompts and transcripts), and then calls
    the different agents in the right order: first extraction, then synthesis,
    and finally validation. It finishes by saving all the results for a human
    to review.
    """
    parser = argparse.ArgumentParser(description="Run the DUX object extraction and synthesis pipeline.")
    # --- Agent Prompts ---
    parser.add_argument("--provenance_prompt_path", required=True, help="Path to the Archivist prompt template.")
    parser.add_argument("--problem_prompt_path", required=True, help="Path to the Problem Agent prompt template.")
    parser.add_argument("--behavior_prompt_path", required=True, help="Path to the Behavior Agent prompt template.")
    parser.add_argument("--result_prompt_path", required=True, help="Path to the Result Agent prompt template.")
    parser.add_argument("--insight_prompt_path", required=True, help="Path to the Insight Architect prompt template.")
    parser.add_argument("--validator_prompt_path", required=True, help="Path to the Validator Agent prompt template.")
    parser.add_argument("--user_flow_prompt_path", required=True, help="Path to the User Flow Agent prompt template.")
    # --- Inputs & Outputs ---
    parser.add_argument("--source_transcript_path", required=True, help="Path to the source transcript file.")
    parser.add_argument("--output_dir", required=True, help="Directory to save the output objects.")
    parser.add_argument("--fit_template_path", help="Path to the Fit Template markdown file for validation.")
    # --- Config ---
    parser.add_argument("--chunk_size", type=int, default=4000, help="Size of text chunks for molecular extraction.")
    parser.add_argument("--ollama_model_name", required=True, help="Name of the Ollama model to use.")
    parser.add_argument("--ollama_base_url", required=True, help="Base URL of the Ollama API.")
    args = parser.parse_args()

    # --- 0. Setup HITL Directories ---
    print("Setting up directories for Human-in-the-Loop (HITL) review...")
    hitl_review_dir = os.path.join(args.output_dir, "hitl_review")
    canonical_storage_dir = os.path.join(args.output_dir, "canonical_storage")
    os.makedirs(hitl_review_dir, exist_ok=True)
    os.makedirs(canonical_storage_dir, exist_ok=True)
    pipeline_log_path = os.path.join(args.output_dir, "pipeline_log.txt")
    print(f"  - Candidate objects will be saved to: {hitl_review_dir}")
    print(f"  - Approved objects should be moved to: {canonical_storage_dir}")
    print(f"  - Full pipeline log will be saved to: {pipeline_log_path}")

    with open(pipeline_log_path, 'w') as f:
        f.write("DUX PIPELINE LOG\n===================\n")

    # --- 1. Load All Inputs ---
    print("\nLoading prompts and source transcript...")
    with open(args.provenance_prompt_path, 'r') as f:
        provenance_prompt_template = f.read()
    with open(args.problem_prompt_path, 'r') as f:
        problem_prompt_template = f.read()
    with open(args.behavior_prompt_path, 'r') as f:
        behavior_prompt_template = f.read()
    with open(args.result_prompt_path, 'r') as f:
        result_prompt_template = f.read()
    with open(args.insight_prompt_path, 'r') as f:
        insight_prompt_template = f.read()
    with open(args.validator_prompt_path, 'r') as f:
        validator_prompt_template = f.read()
    with open(args.user_flow_prompt_path, 'r') as f:
        user_flow_prompt_template = f.read()

    fit_template_content = ""
    if args.fit_template_path:
        print(f"Loading Fit Template from: {args.fit_template_path}")
        try:
            with open(args.fit_template_path, 'r') as f:
                fit_template_content = f.read()
            print("Fit Template loaded.")
        except FileNotFoundError:
            print(f"Warning: Fit Template file not found at {args.fit_template_path}")

    print(f"Loading source transcript: {args.source_transcript_path}")
    try:
        with open(args.source_transcript_path, 'r') as f:
            transcript = f.read()
        print("Transcript loaded.")
    except FileNotFoundError:
        print(f"Error: Source transcript not found at {args.source_transcript_path}")
        return

    # --- 2. Stage 1: Event-Driven Molecular Extraction (Chunk by Chunk) ---
    print("\n===== Stage 1: Event-Driven Molecular Extraction =====")
    chunks = [transcript[i:i + args.chunk_size] for i in range(0, len(transcript), args.chunk_size)]
    print(f"Transcript split into {len(chunks)} chunks.")

    all_provenance_objects = []
    all_problem_objects = []
    all_behavior_objects = []
    all_result_objects = []

    for i, chunk in enumerate(chunks):
        chunk_log = f"\n\n--- Processing Chunk {i+1}/{len(chunks)} ---\n"
        print(chunk_log)

        # == Archivist Agent: Always runs first ==
        prompt = provenance_prompt_template.replace("{{transcript}}", chunk)
        response_str = call_ollama(prompt, args.ollama_model_name, args.ollama_base_url)
        log, provenance_obj = parse_agent_response(response_str, "ARCHIVIST")
        
        chunk_log += log

        if provenance_obj and provenance_obj.get('object_type') == 'Provenance':
            # Assign a new ID and add source URI
            provenance_obj['id'] = f"provenance_{uuid.uuid4().hex[:8]}"
            provenance_obj['source_uri'] = args.source_transcript_path
            all_provenance_objects.append(provenance_obj)
            chunk_log += f"Successfully created Provenance object: {provenance_obj['id']}\n"
            
            tags = provenance_obj.get('tags', [])
            chunk_log += f"Archivist tags: {tags}\n"

            # Event-driven calls based on tags
            # We pass the single provenance object as a list for consistency
            current_evidence = [provenance_obj]

            # == Advocate Agent (if 'problem' tag exists) ==
            if any('problem' in tag.lower() for tag in tags):
                prompt = problem_prompt_template.replace("{{transcript}}", chunk).replace("{{existing_objects}}", json.dumps(current_evidence))
                response_str = call_ollama(prompt, args.ollama_model_name, args.ollama_base_url)
                log, problem_data = parse_agent_response(response_str, "ADVOCATE")
                chunk_log += log
                if problem_data and 'problems' in problem_data:
                    all_problem_objects.extend(problem_data['problems'])
                    chunk_log += f"Advocate created {len(problem_data['problems'])} Problem object(s).\n"

            # == Behavior Agent (if 'behavior' tag exists) ==
            if any('behavior' in tag.lower() for tag in tags):
                prompt = behavior_prompt_template.replace("{{transcript}}", chunk).replace("{{existing_objects}}", json.dumps(current_evidence))
                response_str = call_ollama(prompt, args.ollama_model_name, args.ollama_base_url)
                log, behavior_data = parse_agent_response(response_str, "BEHAVIOR")
                chunk_log += log
                if behavior_data and 'behaviors' in behavior_data:
                    all_behavior_objects.extend(behavior_data['behaviors'])
                    chunk_log += f"Behavior agent created {len(behavior_data['behaviors'])} Behavior object(s).\n"

            # == Result Agent (if 'result' tag exists) ==
            if any('result' in tag.lower() for tag in tags):
                # Result agent might need problems and behaviors as context
                all_molecular_so_far = {
                    "provenance": current_evidence,
                    "problems": all_problem_objects,
                    "behaviors": all_behavior_objects
                }
                prompt = result_prompt_template.replace("{{transcript}}", chunk).replace("{{existing_objects}}", json.dumps(all_molecular_so_far))
                response_str = call_ollama(prompt, args.ollama_model_name, args.ollama_base_url)
                log, result_data = parse_agent_response(response_str, "RESULT")
                chunk_log += log
                if result_data and 'results' in result_data:
                    all_result_objects.extend(result_data['results'])
                    chunk_log += f"Result agent created {len(result_data['results'])} Result object(s).\n"

        else:
            chunk_log += "Archivist failed to create a valid Provenance object for this chunk. Skipping other agents.\n"

        
        with open(pipeline_log_path, 'a') as f:
            f.write(chunk_log)


    # --- 3. Stage 2: Junction Object Synthesis ---
    print("\n\n===== Stage 2: Junction Object Synthesis =====")
    molecular_objects = {
        "provenance_objects": all_provenance_objects,
        "problem_objects": all_problem_objects,
        "behavior_objects": all_behavior_objects,
        "result_objects": all_result_objects
    }

    insight_objects = run_synthesis_agent(
        prompt_template=insight_prompt_template,
        molecular_objects=molecular_objects,
        model_name=args.ollama_model_name,
        base_url=args.ollama_base_url,
        object_type_name="Insight"
    )

    # --- 4a. Stage 2b: User Flow Synthesis ---
    print("\n\n===== Stage 2b: User Flow Synthesis =====")
    user_flow_object = run_user_flow_agent(
        prompt_template=user_flow_prompt_template,
        molecular_objects=molecular_objects,
        model_name=args.ollama_model_name,
        base_url=args.ollama_base_url
    )

    # --- 4. Stage 3: Validation against Fit Template ---
    print("\n\n===== Stage 3: Validation against Fit Template =====")
    if fit_template_content:
        problem_objects = run_validator_agent(
            prompt_template=validator_prompt_template,
            objects_to_validate=all_problem_objects,
            fit_template_content=fit_template_content,
            model_name=args.ollama_model_name,
            base_url=args.ollama_base_url,
            object_type_name="Problem"
        )
        behavior_objects = run_validator_agent(
            prompt_template=validator_prompt_template,
            objects_to_validate=all_behavior_objects,
            fit_template_content=fit_template_content,
            model_name=args.ollama_model_name,
            base_url=args.ollama_base_url,
            object_type_name="Behavior"
        )
        result_objects = run_validator_agent(
            prompt_template=validator_prompt_template,
            objects_to_validate=all_result_objects,
            fit_template_content=fit_template_content,
            model_name=args.ollama_model_name,
            base_url=args.ollama_base_url,
            object_type_name="Result"
        )
        insight_objects = run_validator_agent(
            prompt_template=validator_prompt_template,
            objects_to_validate=insight_objects,
            fit_template_content=fit_template_content,
            model_name=args.ollama_model_name,
            base_url=args.ollama_base_url,
            object_type_name="Insight"
        )
    else:
        # If no fit template, use the original lists
        problem_objects = all_problem_objects
        behavior_objects = all_behavior_objects
        result_objects = all_result_objects


    # --- 5. Save All Pipeline Outputs for Human Review ---
    print("\n\n===== Stage 4: Saving All Outputs =====")
    save_objects_to_disk(all_provenance_objects, args.output_dir, "Provenance")
    save_objects_to_disk(problem_objects, args.output_dir, "Problem")
    save_objects_to_disk(behavior_objects, args.output_dir, "Behavior")
    save_objects_to_disk(result_objects, args.output_dir, "Result")
    save_objects_to_disk(insight_objects, args.output_dir, "Insight")
    if user_flow_object:
        save_objects_to_disk([user_flow_object], args.output_dir, "UserFlow")

    print("\nPipeline finished. Please review the contents of the output directory.")


if __name__ == "__main__":
    main()