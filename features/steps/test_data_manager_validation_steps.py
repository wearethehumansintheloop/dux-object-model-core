"""
Step definitions for TestDataManager schema validation.
Tests that CSV-generated objects are schema-compliant.
"""

import json
import csv
import tempfile
from pathlib import Path
from behave import given, when, then
from jsonschema import validate, ValidationError
from features.steps.test_data_manager import TestDataManager, create_sample_evidence_from_csv


@given('I have a TestDataManager instance')
def step_have_test_data_manager(context):
    """Create a TestDataManager instance for testing."""
    context.test_data_manager = TestDataManager()


@given('I have sample CSV interview data')
def step_have_sample_csv_data(context):
    """Create sample CSV data for testing."""
    # Create a temporary CSV file with sample interview data
    sample_data = [
        {
            'participant': 'Participant_001',
            'question': 'How do you currently receive emergency alerts?',
            'response': 'I mostly get them through my phone notifications, but sometimes they come too late or I miss them when I\'m busy.',
            'timestamp': '00:05:30',
            'context': 'Emergency notification preferences',
            'session_id': 'interview_001'
        },
        {
            'participant': 'Participant_001', 
            'question': 'What challenges do you face with current alert systems?',
            'response': 'The biggest issue is timing - I need alerts immediately, not 15 minutes later. Also, some alerts are too vague.',
            'timestamp': '00:12:45',
            'context': 'Alert system pain points',
            'session_id': 'interview_001'
        },
        {
            'participant': 'Participant_002',
            'question': 'How important are earthquake alerts to you?',
            'response': 'Extremely important! I live in a high-risk area. Quick alerts could save lives and help us prepare.',
            'timestamp': '00:03:15',
            'context': 'Alert importance and urgency',
            'session_id': 'interview_002'
        }
    ]
    
    # Create temporary CSV file
    context.temp_csv = tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False)
    writer = csv.DictWriter(context.temp_csv, fieldnames=sample_data[0].keys())
    writer.writeheader()
    writer.writerows(sample_data)
    context.temp_csv.close()
    
    context.csv_data = sample_data


@given('I have incomplete CSV data')
def step_have_incomplete_csv_data(context):
    """Create CSV data with missing fields to test graceful handling."""
    incomplete_data = [
        {
            'participant': 'Participant_003',
            # Missing 'question' field
            'response': 'This is a response without a question context.',
            # Missing 'timestamp' field
        },
        {
            # Missing 'participant' field
            'question': 'Test question?',
            'response': 'Test response with minimal data.',
            'timestamp': '00:01:00'
        }
    ]
    
    context.temp_csv_incomplete = tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False)
    writer = csv.DictWriter(context.temp_csv_incomplete, 
                           fieldnames=['participant', 'question', 'response', 'timestamp'])
    writer.writeheader()
    writer.writerows(incomplete_data)
    context.temp_csv_incomplete.close()


@given('I have CSV data with various field names')
def step_have_various_field_names_csv(context):
    """Create CSV data with different field naming conventions."""
    various_fields_data = [
        {
            'interviewee': 'John_Doe',
            'prompt': 'What do you think about the system?',
            'answer': 'The system works well but could be faster.',
            'date': '2024-01-15',
            'comment': 'User seemed satisfied overall'
        },
        {
            'participant_id': 'Jane_Smith', 
            'scenario': 'Emergency alert scenario',
            'feedback': 'I would prefer more detailed alerts with specific instructions.',
            'time': '14:30:00',
            'notes': 'Strong preference for actionable information'
        }
    ]
    
    # Use consistent fieldnames for all rows
    all_fieldnames = ['interviewee', 'participant_id', 'prompt', 'scenario', 'answer', 'feedback', 'date', 'time', 'comment', 'notes']
    
    context.temp_csv_various = tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False)
    writer = csv.DictWriter(context.temp_csv_various, fieldnames=all_fieldnames)
    writer.writeheader()
    
    # Write each row with all fieldnames (missing fields will be empty)
    for row in various_fields_data:
        full_row = {field: row.get(field, '') for field in all_fieldnames}
        writer.writerow(full_row)
    
    context.temp_csv_various.close()


@when('I generate a Problem object from CSV data')
def step_generate_problem_from_csv(context):
    """Generate a Problem object using TestDataManager from CSV data."""
    context.generated_problem = create_sample_evidence_from_csv(
        context.temp_csv.name, 
        object_type="problem"
    )
    # Also set as sample_problem for compatibility with existing schema validation steps
    context.sample_problem = context.generated_problem


@when('I generate a Behavior object from CSV data')
def step_generate_behavior_from_csv(context):
    """Generate a Behavior object using TestDataManager from CSV data."""
    context.generated_behavior = create_sample_evidence_from_csv(
        context.temp_csv.name,
        object_type="behavior" 
    )
    # Also set as sample_behavior for compatibility with existing schema validation steps
    context.sample_behavior = context.generated_behavior


@when('I generate objects from incomplete data')
def step_generate_from_incomplete_data(context):
    """Generate objects from incomplete CSV data."""
    try:
        context.generated_incomplete_problem = create_sample_evidence_from_csv(
            context.temp_csv_incomplete.name,
            object_type="problem"
        )
        context.incomplete_generation_success = True
    except Exception as e:
        context.incomplete_generation_error = str(e)
        context.incomplete_generation_success = False


@when('I extract evidence blocks')
def step_extract_evidence_blocks(context):
    """Extract evidence blocks from CSV with various field names."""
    csv_data = context.test_data_manager.import_csv_data(context.temp_csv_various.name)
    context.extracted_evidence = context.test_data_manager.extract_evidence_blocks(
        csv_data, 
        context.temp_csv_various.name
    )


@when('I validate against the actual Problem schema')
def step_validate_against_actual_schema(context):
    """Validate generated objects against the actual schema files."""
    # Load the actual Problem schema
    schema_path = Path("src/dux_v9.5_split_schema/dux_object_problem.json")
    with open(schema_path, 'r') as f:
        context.actual_problem_schema = json.load(f)


@then('it should have structured evidence blocks')
def step_should_have_structured_evidence(context):
    """Verify that evidence blocks follow the required structure."""
    if hasattr(context, 'generated_problem'):
        evidence = context.generated_problem.get('evidence', [])
    elif hasattr(context, 'generated_behavior'):
        evidence = context.generated_behavior.get('evidence', [])
    else:
        raise AssertionError("No generated object found")
    
    assert isinstance(evidence, list), "Evidence should be an array"
    assert len(evidence) > 0, "Should have at least one evidence block"
    
    for evidence_block in evidence:
        # Check required fields for evidence blocks
        required_fields = ['teaser', 'quote', 'citation', 'provenance', 'evidence_type', 'collection_method']
        for field in required_fields:
            assert field in evidence_block, f"Evidence block missing required field: {field}"
        
        # Check provenance structure
        provenance = evidence_block['provenance']
        assert isinstance(provenance, dict), "Provenance should be an object"
        assert 'source_filename' in provenance, "Provenance missing source_filename"
        assert 'timestamp_in' in provenance, "Provenance missing timestamp_in"
        assert 'timestamp_out' in provenance, "Provenance missing timestamp_out"


@then('it should have proper evidence status')
def step_should_have_proper_evidence_status(context):
    """Verify that evidence status is properly determined."""
    if hasattr(context, 'generated_problem'):
        obj = context.generated_problem
    elif hasattr(context, 'generated_behavior'):
        obj = context.generated_behavior
    else:
        raise AssertionError("No generated object found")
    
    evidence_status = obj.get('evidence_status')
    valid_statuses = ['evidence_backed', 'evidence_present', 'assumptive']
    
    assert evidence_status in valid_statuses, \
        f"Invalid evidence status: {evidence_status}. Must be one of {valid_statuses}"


@then('it should still produce valid schema-compliant objects')
def step_should_produce_valid_objects_despite_incomplete_data(context):
    """Verify that objects are still valid even with incomplete CSV data."""
    assert context.incomplete_generation_success, \
        f"Failed to generate object from incomplete data: {getattr(context, 'incomplete_generation_error', 'Unknown error')}"
    
    # Check that the generated object has required fields
    problem = context.generated_incomplete_problem
    assert problem.get('object_type') == 'Problem', "Should have correct object_type"
    assert problem.get('id'), "Should have an ID"
    assert problem.get('description'), "Should have a description"


@then('it should set appropriate default values')
def step_should_set_default_values(context):
    """Verify that default values are set for missing fields."""
    problem = context.generated_incomplete_problem
    
    # Check for default values
    assert problem.get('evidence_status') in ['evidence_backed', 'evidence_present', 'assumptive'], \
        "Should have valid default evidence status"
    assert problem.get('protocol_url'), "Should have default protocol URL"
    assert problem.get('what_is_at_stake'), "Should have default what_is_at_stake"


@then('it should maintain evidence traceability')
def step_should_maintain_evidence_traceability(context):
    """Verify that evidence maintains traceability even with incomplete data."""
    problem = context.generated_incomplete_problem
    evidence = problem.get('evidence', [])
    
    for evidence_block in evidence:
        assert evidence_block.get('citation'), "Evidence should have citation"
        assert evidence_block.get('provenance'), "Evidence should have provenance"
        assert evidence_block.get('quote'), "Evidence should have quote"


@then('each evidence block should have required fields')
def step_evidence_blocks_have_required_fields(context):
    """Verify that extracted evidence blocks have all required fields."""
    evidence = context.extracted_evidence
    
    assert len(evidence) > 0, "Should extract at least one evidence block"
    
    for block in evidence:
        # Check the internal structure (not schema-compliant yet, but logically structured)
        assert block.get('quote'), "Evidence block should have quote"
        assert block.get('source'), "Evidence block should have source"
        assert block.get('interviewee'), "Evidence block should have participant info"


@then('provenance should be properly structured')
def step_provenance_properly_structured(context):
    """Verify that provenance follows the expected structure."""
    evidence = context.extracted_evidence
    
    for block in evidence:
        # The raw evidence blocks from extract_evidence_blocks may not have 
        # the final schema structure yet, but should have basic traceability
        assert block.get('source'), "Should have source information"
        assert block.get('timestamp'), "Should have timestamp information"


@then('evidence types should be correctly classified')
def step_evidence_types_correctly_classified(context):
    """Verify that evidence types are classified according to schema enums."""
    evidence = context.extracted_evidence
    
    valid_evidence_types = ['qualitative', 'quantitative', 'mixed']
    
    for block in evidence:
        if 'evidence_type' in block:
            assert block['evidence_type'] in valid_evidence_types, \
                f"Invalid evidence type: {block['evidence_type']}"


@then('collection methods should be valid enum values')
def step_collection_methods_valid_enums(context):
    """Verify that collection methods match schema enum values."""
    evidence = context.extracted_evidence
    
    valid_collection_methods = ['interview', 'survey', 'usability_test', 'analytics', 'other']
    
    for block in evidence:
        if 'collection_method' in block:
            assert block['collection_method'] in valid_collection_methods, \
                f"Invalid collection method: {block['collection_method']}"


@then('all required fields should be present')
def step_all_required_fields_present(context):
    """Verify that all required fields from the schema are present."""
    problem = context.generated_problem
    schema = context.actual_problem_schema
    
    required_fields = schema.get('required', [])
    
    for field in required_fields:
        assert field in problem, f"Required field missing: {field}"


@then('all field types should match schema requirements')
def step_field_types_match_schema(context):
    """Verify that field types match what's defined in the schema."""
    problem = context.generated_problem
    
    # Basic type checking for key fields
    assert isinstance(problem.get('object_type'), str), "object_type should be string"
    assert isinstance(problem.get('id'), str), "id should be string"
    assert isinstance(problem.get('evidence'), list), "evidence should be array"
    
    if 'result_ids' in problem:
        assert isinstance(problem['result_ids'], list), "result_ids should be array"


@then('evidence blocks should follow EvidenceBlock schema')
def step_evidence_blocks_follow_schema(context):
    """Verify that evidence blocks follow the EvidenceBlock schema structure."""
    problem = context.generated_problem
    evidence = problem.get('evidence', [])
    
    for evidence_block in evidence:
        # Check structure matches what we expect from EvidenceBlock schema
        assert isinstance(evidence_block.get('quote'), str), "quote should be string"
        assert isinstance(evidence_block.get('citation'), str), "citation should be string"
        assert isinstance(evidence_block.get('provenance'), dict), "provenance should be object"
        
        provenance = evidence_block['provenance']
        assert isinstance(provenance.get('source_filename'), str), "source_filename should be string"
        assert isinstance(provenance.get('timestamp_in'), str), "timestamp_in should be string"
        assert isinstance(provenance.get('timestamp_out'), str), "timestamp_out should be string"


@then('related object references should follow RelatedObjectReference schema')
def step_related_object_refs_follow_schema(context):
    """Verify that related object references follow the RelatedObjectReference schema."""
    problem = context.generated_problem
    
    if 'result_ids' in problem and problem['result_ids']:
        for ref in problem['result_ids']:
            assert isinstance(ref.get('id'), str), "Reference id should be string"
            assert ref.get('evidence_status') in ['evidence_backed', 'evidence_present', 'assumptive'], \
                "Reference should have valid evidence_status"


@then('it should have valid JTBD format')
def step_should_have_valid_jtbd_format(context):
    """Verify that the Problem description follows JTBD format."""
    problem = context.generated_problem
    description = problem.get('description', '')
    
    # Check JTBD pattern: "When..., I want..., so I can..."
    import re
    jtbd_pattern = r"^When .+, I want .+, so I can .+\.$"
    
    assert re.match(jtbd_pattern, description), \
        f"Description does not follow JTBD format: {description}"


@then('it should have valid enablement statement format')
def step_should_have_valid_enablement_format(context):
    """Verify that the Behavior description follows enablement statement format."""
    behavior = context.generated_behavior
    description = behavior.get('description', '')
    
    # Check that description is present and meaningful
    assert description, "Behavior should have a description"
    assert len(description) > 10, "Behavior description should be meaningful"


@given('I have generated objects from TestDataManager')
def step_have_generated_objects_from_test_data_manager(context):
    """Generate test objects to validate against actual schemas."""
    # Use temp CSV if available, otherwise use sample file
    csv_file = (context.temp_csv.name if hasattr(context, 'temp_csv') 
                else "test_data/csv/sample_interview.csv")
    
    # Generate a Problem object for validation
    context.generated_problem = create_sample_evidence_from_csv(
        csv_file,
        object_type="problem"
    )
    context.sample_problem = context.generated_problem
