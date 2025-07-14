import sys
import os
import json
from pathlib import Path

# Add both project roots to the Python path to resolve cross-project imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../dux-research-platform')))


from src.app.orchestrators.dux_processor import DUXObjectExtractor

def main():
    # Initialize the processor
    processor = DUXObjectExtractor(
        validation_mode='simple' 
    )

    # Define paths
    # The new transcript path provided by the user
    transcript_path = "/Users/njayanty/Projects/Upstream Contributions/prompt_Tests/20250706_bullextraction_test_100-1000/2024_Q2_UXDR-2879 Generative Study for Resource Optimization_UXDR_2879_P1_Cigna_undefined_DEIDENTIFIED.md"
    
    # Using the same fit template for now
    base_path = Path("/Users/njayanty/Projects/Upstream Contributions/shut_the_dux_up/dux-object-model-core")
    fit_template_path = base_path / "test_data/fit_template_gpu_management.md"
    output_dir = base_path / "output"
    
    # Create output directory if it doesn't exist
    output_dir.mkdir(exist_ok=True)

    # Check if transcript file exists
    if not os.path.exists(transcript_path):
        print(f"Error: Transcript file not found at {transcript_path}")
        return

    # Run the processor
    results = processor.process_transcript(
        transcript_path=transcript_path,
        source_filename=os.path.basename(transcript_path),
        fit_template_path=str(fit_template_path),
        fit_score_threshold=0.7
    )

    # Save the results
    if results:
        saved_path = processor.save_extraction_results(results, str(output_dir))
        print(f"Processing complete. Results saved to: {saved_path}")
        # Print the summary
        print(json.dumps(results.get("summary"), indent=4))
    else:
        print("Processing failed to return results.")

if __name__ == "__main__":
    main()
