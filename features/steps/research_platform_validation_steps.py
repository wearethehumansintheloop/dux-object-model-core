from behave import given, when, then
import os
import json
import re
from datetime import datetime
from pathlib import Path

# Sample research platform objects for testing
SAMPLE_SESSION = {
    "object_type": "Session",
    "id": "session_001",
    "session_type": "user_interview",
    "session_date": "2025-01-07T14:30:00Z",
    "duration_minutes": 45,
    "participant_count": 1,
    "researcher_id": "researcher_sarah",
    "session_location": "Zoom Meeting Room A",
    "session_notes": "Interview with cluster admin about GPU management challenges",
    "session_status": "completed",
    "data_ids": ["data_001", "data_002", "data_003"],
    "study_id": "study_gpu_management_2025",
    "tags": ["cluster_admin", "gpu_management", "user_interview"],
    "created_at": "2025-01-07T14:25:00Z",
    "updated_at": "2025-01-07T16:15:00Z"
}

SAMPLE_DATA = {
    "object_type": "Data",
    "id": "data_001",
    "data_type": "user_quote",
    "content": "I spend at least 30 minutes every morning just trying to figure out which GPUs are actually being used and which ones are just sitting idle. It's incredibly frustrating.",
    "source_session_id": "session_001",
    "timestamp_in": "00:12:45",
    "timestamp_out": "00:13:20",
    "participant_id": "participant_007",
    "researcher_notes": "Participant showed visible frustration when discussing this topic",
    "confidence_level": "high",
    "data_tags": ["gpu_management", "frustration", "time_waste"],
    "report_id": "report_gpu_management_2025",
    "transcript_id": "transcript_session_001",
    "tags": ["cluster_admin", "gpu_management", "user_quote"],
    "created_at": "2025-01-07T16:20:00Z",
    "updated_at": "2025-01-07T16:20:00Z"
}

SAMPLE_FRAME = {
    "object_type": "Frame",
    "id": "frame_001",
    "frame_name": "Admin Efficiency & Productivity",
    "frame_description": "Analyzes evidence through the lens of administrative efficiency, focusing on time savings, workflow optimization, and productivity gains for platform administrators.",
    "strategic_context": "Improving platform administrator productivity to reduce operational overhead and increase satisfaction",
    "analysis_questions": [
        "How much time do admins spend on routine tasks?",
        "What are the biggest productivity blockers?",
        "Which workflows could be automated or streamlined?",
        "What would success look like for admin efficiency?"
    ],
    "frame_type": "user_experience",
    "priority_level": "high",
    "stakeholder_audience": ["product_managers", "platform_team", "executive_leadership"],
    "success_criteria": [
        "Identified specific time-wasting activities",
        "Quantified productivity impact",
        "Generated actionable improvement opportunities"
    ],
    "gallery_id": "gallery_admin_efficiency_2025",
    "related_frames": ["frame_002", "frame_003"],
    "tags": ["admin_efficiency", "productivity", "user_experience"],
    "created_at": "2025-01-07T10:00:00Z",
    "updated_at": "2025-01-07T10:00:00Z"
}

SAMPLE_STUDY = {
    "object_type": "Study",
    "id": "study_gpu_management_2025",
    "study_name": "GPU Management Efficiency Study 2025",
    "study_description": "Comprehensive study of cluster administrator workflows and pain points related to GPU resource management and monitoring.",
    "research_objective": "Understand the current challenges and opportunities for improving GPU management efficiency for platform administrators.",
    "study_type": "exploratory",
    "target_participants": ["cluster_administrators", "platform_engineers", "devops_engineers"],
    "planned_sessions": 12,
    "completed_sessions": 8,
    "study_status": "in_progress",
    "start_date": "2025-01-01T00:00:00Z",
    "end_date": "2025-02-28T23:59:59Z",
    "session_ids": ["session_001", "session_002", "session_003", "session_004", "session_005", "session_006", "session_007", "session_008"],
    "researcher_ids": ["researcher_sarah", "researcher_mike"],
    "study_notes": "Focus on understanding daily workflows, pain points, and opportunities for automation in GPU management.",
    "tags": ["gpu_management", "cluster_admin", "efficiency_study"],
    "created_at": "2024-12-15T10:00:00Z",
    "updated_at": "2025-01-07T18:00:00Z"
}

SAMPLE_REPORT = {
    "object_type": "Report",
    "id": "report_gpu_management_2025",
    "report_name": "GPU Management User Research Report 2025",
    "report_description": "Comprehensive analysis of cluster administrator workflows and pain points related to GPU resource management, based on 8 user interviews and observations.",
    "report_type": "user_research_analysis",
    "source_study_id": "study_gpu_management_2025",
    "data_count": 47,
    "report_status": "published",
    "created_by": "researcher_sarah",
    "data_ids": ["data_001", "data_002", "data_003", "data_004", "data_005", "data_006", "data_007", "data_008"],
    "report_structure": [
        "Executive Summary",
        "Methodology",
        "Key Findings",
        "Pain Points Analysis",
        "Opportunity Areas",
        "Recommendations"
    ],
    "key_findings": [
        "Admins spend 30+ minutes daily on manual GPU monitoring",
        "Current tools lack real-time visibility into resource utilization",
        "Frustration levels are high due to inefficient workflows"
    ],
    "report_url": "https://company.com/reports/gpu_management_2025.pdf",
    "tags": ["gpu_management", "user_research", "cluster_admin"],
    "created_at": "2025-01-07T19:00:00Z",
    "updated_at": "2025-01-07T19:00:00Z"
}

SAMPLE_REPORT_GALLERY = {
    "object_type": "ReportGallery",
    "id": "gallery_admin_efficiency_2025",
    "gallery_name": "Admin Efficiency & Productivity Gallery 2025",
    "gallery_description": "Strategic analysis gallery focused on improving platform administrator efficiency, productivity, and satisfaction through workflow optimization and tool improvements.",
    "strategic_theme": "Platform Administrator Efficiency",
    "gallery_type": "user_experience",
    "target_audience": ["product_managers", "platform_team", "executive_leadership"],
    "frame_count": 5,
    "gallery_status": "active",
    "created_by": "strategist_jane",
    "frame_ids": ["frame_001", "frame_002", "frame_003", "frame_004", "frame_005"],
    "strategic_objectives": [
        "Reduce admin time spent on routine tasks by 50%",
        "Improve admin satisfaction scores by 25%",
        "Increase platform utilization efficiency by 30%"
    ],
    "success_metrics": [
        "Time savings per admin per day",
        "Admin satisfaction survey scores",
        "Platform resource utilization rates"
    ],
    "gallery_notes": "Focus on identifying high-impact opportunities for workflow automation and tool improvements that directly impact admin productivity.",
    "tags": ["admin_efficiency", "productivity", "workflow_optimization"],
    "created_at": "2025-01-01T09:00:00Z",
    "updated_at": "2025-01-07T20:00:00Z"
}

SAMPLE_PROVENANCE_JUNCTION = {
    "object_type": "ProvenanceJunction",
    "id": "provenance_junction_001",
    "session_id": "session_001",
    "data_id": "data_001",
    "evidence_maturity": "03_early_signal",
    "evidence_block": [
        {
            "teaser": "User expresses frustration with GPU management workflow",
            "quote": "I spend at least 30 minutes every morning just trying to figure out which GPUs are actually being used and which ones are just sitting idle. It's incredibly frustrating.",
            "citation": "Participant 7, timestamp 00:12:45",
            "provenance_id": "provenance_junction_001",
            "evidence_type": "user_research_finding",
            "confidence_level": "high"
        }
    ],
    "evidence_teaser": "Users struggle with GPU utilization monitoring and waste significant time on manual resource tracking",
    "confidence_score": 0.85,
    "triangulation_count": 1,
    "last_validation_date": "2025-01-07T16:30:00Z",
    "validation_status": "validated",
    "tags": ["gpu_management", "user_frustration", "time_waste"],
    "created_at": "2025-01-07T16:25:00Z",
    "updated_at": "2025-01-07T16:30:00Z"
}

SAMPLE_EVIDENCE_JUNCTION = {
    "object_type": "EvidenceJunction",
    "id": "evidence_junction_001",
    "session_id": "session_001",
    "frame_id": "frame_001",
    "teaser_quote": "I spend at least 30 minutes every morning just trying to figure out which GPUs are actually being used and which ones are just sitting idle. It's incredibly frustrating.",
    "quote_attribution": "Participant 7, Admin Efficiency Interview, 00:12:45",
    "evidence_summary": "Cluster admin reports spending 30+ minutes daily on manual GPU utilization monitoring, indicating significant productivity waste in routine administrative tasks.",
    "strategic_insights": [
        "Manual GPU monitoring consumes significant admin time daily",
        "Current tools lack real-time visibility into resource utilization",
        "Admin frustration suggests opportunity for workflow automation"
    ],
    "relevance_score": 0.95,
    "analysis_notes": "This session provides strong evidence for the admin efficiency frame, with clear quantification of time waste and emotional impact.",
    "key_findings": [
        "Daily time investment: 30+ minutes",
        "Primary pain point: lack of visibility",
        "Emotional impact: high frustration level"
    ],
    "follow_up_questions": [
        "What tools are currently being used for monitoring?",
        "How many other admins face similar challenges?",
        "What would an ideal monitoring solution look like?"
    ],
    "tags": ["admin_efficiency", "gpu_management", "productivity_waste"],
    "created_at": "2025-01-07T17:00:00Z",
    "updated_at": "2025-01-07T17:00:00Z"
}

SAMPLE_INSIGHT_JUNCTION = {
    "object_type": "InsightJunction",
    "id": "insight_junction_001",
    "evidence_id": "evidence_junction_001",
    "frame_id": "frame_001",
    "fit_score": 0.92,
    "insight_teaser": "Admin efficiency is significantly impacted by manual GPU monitoring workflows that consume 30+ minutes daily.",
    "insight_story_block": [
        "Cluster administrators spend a substantial portion of their daily routine manually monitoring GPU utilization.",
        "This manual process is both time-consuming and frustrating, indicating a clear opportunity for workflow optimization.",
        "The high fit score suggests this evidence directly addresses the admin efficiency frame's strategic objectives."
    ],
    "strategic_impact": "This insight suggests a high-priority opportunity to improve admin productivity through automated GPU monitoring tools, potentially saving 30+ minutes per admin per day.",
    "confidence_level": "high",
    "actionability_score": 0.88,
    "priority_level": "high",
    "related_insights": ["insight_junction_002", "insight_junction_003"],
    "implementation_notes": "Consider developing automated GPU monitoring dashboard with real-time utilization metrics and idle resource alerts.",
    "tags": ["admin_efficiency", "gpu_management", "productivity_optimization"],
    "created_at": "2025-01-07T17:30:00Z",
    "updated_at": "2025-01-07T17:30:00Z"
}

@given('I have sample research platform objects')
def step_impl(context):
    """Load sample research platform objects for testing."""
    context.sample_objects = {
        'session': SAMPLE_SESSION,
        'data': SAMPLE_DATA,
        'frame': SAMPLE_FRAME,
        'study': SAMPLE_STUDY,
        'report': SAMPLE_REPORT,
        'report_gallery': SAMPLE_REPORT_GALLERY,
        'provenance_junction': SAMPLE_PROVENANCE_JUNCTION,
        'evidence_junction': SAMPLE_EVIDENCE_JUNCTION,
        'insight_junction': SAMPLE_INSIGHT_JUNCTION
    }

@given('I have a Session object schema')
def step_impl(context):
    """Load Session object schema."""
    session_schema_file = os.path.join(context.schema_root, "dux_object_session.json")
    assert os.path.exists(session_schema_file), f"Session schema not found at {session_schema_file}"
    with open(session_schema_file, 'r') as f:
        context.session_schema = json.load(f)

@given('I have a Data object schema')
def step_impl(context):
    """Load Data object schema."""
    data_schema_file = os.path.join(context.schema_root, "dux_object_data.json")
    assert os.path.exists(data_schema_file), f"Data schema not found at {data_schema_file}"
    with open(data_schema_file, 'r') as f:
        context.data_schema = json.load(f)

@given('I have a Frame object schema')
def step_impl(context):
    """Load Frame object schema."""
    frame_schema_file = os.path.join(context.schema_root, "dux_object_frame.json")
    assert os.path.exists(frame_schema_file), f"Frame schema not found at {frame_schema_file}"
    with open(frame_schema_file, 'r') as f:
        context.frame_schema = json.load(f)

@given('I have a Study object schema')
def step_impl(context):
    """Load Study object schema."""
    study_schema_file = os.path.join(context.schema_root, "dux_object_study.json")
    assert os.path.exists(study_schema_file), f"Study schema not found at {study_schema_file}"
    with open(study_schema_file, 'r') as f:
        context.study_schema = json.load(f)

@given('I have a Report object schema')
def step_impl(context):
    """Load Report object schema."""
    report_schema_file = os.path.join(context.schema_root, "dux_object_report.json")
    assert os.path.exists(report_schema_file), f"Report schema not found at {report_schema_file}"
    with open(report_schema_file, 'r') as f:
        context.report_schema = json.load(f)

@given('I have a Report Gallery object schema')
def step_impl(context):
    """Load Report Gallery object schema."""
    gallery_schema_file = os.path.join(context.schema_root, "dux_object_report_gallery.json")
    assert os.path.exists(gallery_schema_file), f"Report Gallery schema not found at {gallery_schema_file}"
    with open(gallery_schema_file, 'r') as f:
        context.gallery_schema = json.load(f)

@given('I have a Provenance Junction object schema')
def step_impl(context):
    """Load Provenance Junction object schema."""
    provenance_junction_schema_file = os.path.join(context.schema_root, "dux_object_provenance_junction.json")
    assert os.path.exists(provenance_junction_schema_file), f"Provenance Junction schema not found at {provenance_junction_schema_file}"
    with open(provenance_junction_schema_file, 'r') as f:
        context.provenance_junction_schema = json.load(f)

@given('I have an Evidence Junction object schema')
def step_impl(context):
    """Load Evidence Junction object schema."""
    evidence_junction_schema_file = os.path.join(context.schema_root, "dux_object_evidence_junction.json")
    assert os.path.exists(evidence_junction_schema_file), f"Evidence Junction schema not found at {evidence_junction_schema_file}"
    with open(evidence_junction_schema_file, 'r') as f:
        context.evidence_junction_schema = json.load(f)

@given('I have an Insight Junction object schema')
def step_impl(context):
    """Load Insight Junction object schema."""
    insight_junction_schema_file = os.path.join(context.schema_root, "dux_object_insight_junction.json")
    assert os.path.exists(insight_junction_schema_file), f"Insight Junction schema not found at {insight_junction_schema_file}"
    with open(insight_junction_schema_file, 'r') as f:
        context.insight_junction_schema = json.load(f)

@when('I validate a sample Session object')
def step_impl(context):
    """Validate the sample Session object against its schema."""
    context.validation_result = validate_object_against_schema(
        context.sample_objects['session'], 
        context.session_schema
    )

@when('I validate a sample Data object')
def step_impl(context):
    """Validate the sample Data object against its schema."""
    context.validation_result = validate_object_against_schema(
        context.sample_objects['data'], 
        context.data_schema
    )

@when('I validate a sample Frame object')
def step_impl(context):
    """Validate the sample Frame object against its schema."""
    context.validation_result = validate_object_against_schema(
        context.sample_objects['frame'], 
        context.frame_schema
    )

@when('I validate a sample Study object')
def step_impl(context):
    """Validate the sample Study object against its schema."""
    context.validation_result = validate_object_against_schema(
        context.sample_objects['study'], 
        context.study_schema
    )

@when('I validate a sample Report object')
def step_impl(context):
    """Validate the sample Report object against its schema."""
    context.validation_result = validate_object_against_schema(
        context.sample_objects['report'], 
        context.report_schema
    )

@when('I validate a sample Report Gallery object')
def step_impl(context):
    """Validate the sample Report Gallery object against its schema."""
    context.validation_result = validate_object_against_schema(
        context.sample_objects['report_gallery'], 
        context.gallery_schema
    )

@when('I validate a sample Provenance Junction object')
def step_impl(context):
    """Validate the sample Provenance Junction object against its schema."""
    context.validation_result = validate_object_against_schema(
        context.sample_objects['provenance_junction'], 
        context.provenance_junction_schema
    )

@when('I validate a sample Evidence Junction object')
def step_impl(context):
    """Validate the sample Evidence Junction object against its schema."""
    context.validation_result = validate_object_against_schema(
        context.sample_objects['evidence_junction'], 
        context.evidence_junction_schema
    )

@when('I validate a sample Insight Junction object')
def step_impl(context):
    """Validate the sample Insight Junction object against its schema."""
    context.validation_result = validate_object_against_schema(
        context.sample_objects['insight_junction'], 
        context.insight_junction_schema
    )

# Validation helper function
def validate_object_against_schema(obj, schema):
    """Basic schema validation (simplified version without jsonschema library)."""
    errors = []
    
    # Check required fields
    required_fields = schema.get('required', [])
    for field in required_fields:
        if field not in obj:
            errors.append(f"Missing required field: {field}")
        elif obj[field] is None or obj[field] == "":
            errors.append(f"Required field '{field}' cannot be empty")
    
    # Check object_type
    if 'object_type' in obj and 'object_type' in schema.get('properties', {}):
        expected_type = schema['properties']['object_type'].get('enum', [])
        if obj['object_type'] not in expected_type:
            errors.append(f"object_type must be one of {expected_type}")
    
    # Check ID pattern
    if 'id' in obj and 'id' in schema.get('properties', {}):
        id_pattern = schema['properties']['id'].get('pattern', '')
        if id_pattern and not re.match(id_pattern, obj['id']):
            errors.append(f"ID must match pattern: {id_pattern}")
    
    return len(errors) == 0, errors

# Then steps for validation results
@then('it should pass Session schema validation')
def step_impl(context):
    """Assert that Session validation passed."""
    is_valid, errors = context.validation_result
    assert is_valid, f"Session validation failed: {errors}"

@then('it should pass Data schema validation')
def step_impl(context):
    """Assert that Data validation passed."""
    is_valid, errors = context.validation_result
    assert is_valid, f"Data validation failed: {errors}"

@then('it should pass Frame schema validation')
def step_impl(context):
    """Assert that Frame validation passed."""
    is_valid, errors = context.validation_result
    assert is_valid, f"Frame validation failed: {errors}"

@then('it should pass Study schema validation')
def step_impl(context):
    """Assert that Study validation passed."""
    is_valid, errors = context.validation_result
    assert is_valid, f"Study validation failed: {errors}"

@then('it should pass Report schema validation')
def step_impl(context):
    """Assert that Report validation passed."""
    is_valid, errors = context.validation_result
    assert is_valid, f"Report validation failed: {errors}"

@then('it should pass Report Gallery schema validation')
def step_impl(context):
    """Assert that Report Gallery validation passed."""
    is_valid, errors = context.validation_result
    assert is_valid, f"Report Gallery validation failed: {errors}"

@then('it should pass Provenance Junction schema validation')
def step_impl(context):
    """Assert that Provenance Junction validation passed."""
    is_valid, errors = context.validation_result
    assert is_valid, f"Provenance Junction validation failed: {errors}"

@then('it should pass Evidence Junction schema validation')
def step_impl(context):
    """Assert that Evidence Junction validation passed."""
    is_valid, errors = context.validation_result
    assert is_valid, f"Evidence Junction validation failed: {errors}"

@then('it should pass Insight Junction schema validation')
def step_impl(context):
    """Assert that Insight Junction validation passed."""
    is_valid, errors = context.validation_result
    assert is_valid, f"Insight Junction validation failed: {errors}"

# Field-specific validation steps
@then('it should have a valid session_type')
def step_impl(context):
    """Assert that session_type is valid."""
    session = context.sample_objects['session']
    assert 'session_type' in session, "Session should have session_type"
    assert session['session_type'] in ['user_interview', 'observation', 'survey', 'workshop'], "Invalid session_type"

@then('it should have a valid session_status')
def step_impl(context):
    """Assert that session_status is valid."""
    session = context.sample_objects['session']
    assert 'session_status' in session, "Session should have session_status"
    assert session['session_status'] in ['scheduled', 'in_progress', 'completed', 'cancelled'], "Invalid session_status"

@then('it should have positive duration_minutes')
def step_impl(context):
    """Assert that duration_minutes is positive."""
    session = context.sample_objects['session']
    assert 'duration_minutes' in session, "Session should have duration_minutes"
    assert session['duration_minutes'] > 0, "duration_minutes should be positive"

@then('it should have positive participant_count')
def step_impl(context):
    """Assert that participant_count is positive."""
    session = context.sample_objects['session']
    assert 'participant_count' in session, "Session should have participant_count"
    assert session['participant_count'] > 0, "participant_count should be positive"

@then('it should reference a valid researcher_id')
def step_impl(context):
    """Assert that researcher_id is present."""
    session = context.sample_objects['session']
    assert 'researcher_id' in session, "Session should have researcher_id"
    assert session['researcher_id'], "researcher_id should not be empty"

@then('it should have a valid data_type')
def step_impl(context):
    """Assert that data_type is valid."""
    data = context.sample_objects['data']
    assert 'data_type' in data, "Data should have data_type"
    assert data['data_type'] in ['quote', 'observation', 'metric', 'finding'], "Invalid data_type"

@then('it should have non-empty content')
def step_impl(context):
    """Assert that content is not empty."""
    data = context.sample_objects['data']
    assert 'content' in data, "Data should have content"
    assert data['content'], "content should not be empty"

@then('it should reference a valid source_session_id')
def step_impl(context):
    """Assert that source_session_id is valid."""
    data = context.sample_objects['data']
    assert 'source_session_id' in data, "Data should have source_session_id"
    assert data['source_session_id'].startswith('session_'), "source_session_id should start with 'session_'"

@then('it should have a valid confidence_level')
def step_impl(context):
    """Assert that confidence_level is valid."""
    data = context.sample_objects['data']
    assert 'confidence_level' in data, "Data should have confidence_level"
    assert data['confidence_level'] in ['low', 'medium', 'high'], "Invalid confidence_level"

@then('it should have valid timestamp_in and timestamp_out')
def step_impl(context):
    """Assert that timestamps are valid."""
    data = context.sample_objects['data']
    assert 'timestamp_in' in data, "Data should have timestamp_in"
    assert 'timestamp_out' in data, "Data should have timestamp_out"
    assert data['timestamp_in'], "timestamp_in should not be empty"
    assert data['timestamp_out'], "timestamp_out should not be empty"

@then('it should have a valid frame_name')
def step_impl(context):
    """Assert that frame_name is valid."""
    frame = context.sample_objects['frame']
    assert 'frame_name' in frame, "Frame should have frame_name"
    assert frame['frame_name'], "frame_name should not be empty"

@then('it should have non-empty frame_description')
def step_impl(context):
    """Assert that frame_description is not empty."""
    frame = context.sample_objects['frame']
    assert 'frame_description' in frame, "Frame should have frame_description"
    assert frame['frame_description'], "frame_description should not be empty"

@then('it should have at least one analysis_question')
def step_impl(context):
    """Assert that analysis_questions has at least one item."""
    frame = context.sample_objects['frame']
    assert 'analysis_questions' in frame, "Frame should have analysis_questions"
    assert len(frame['analysis_questions']) > 0, "analysis_questions should have at least one item"

@then('it should have a valid priority_level')
def step_impl(context):
    """Assert that priority_level is valid."""
    frame = context.sample_objects['frame']
    assert 'priority_level' in frame, "Frame should have priority_level"
    assert frame['priority_level'] in ['high', 'medium', 'low'], "Invalid priority_level"

@then('it should have a valid frame_type')
def step_impl(context):
    """Assert that frame_type is valid."""
    frame = context.sample_objects['frame']
    assert 'frame_type' in frame, "Frame should have frame_type"
    assert frame['frame_type'] in ['user_experience', 'business_impact', 'technical_feasibility'], "Invalid frame_type"

# Additional validation steps for other objects...
# (Continuing with similar patterns for Study, Report, Report Gallery, and Junction objects)

@then('it should have a valid study_name')
def step_impl(context):
    """Assert that study_name is valid."""
    study = context.sample_objects['study']
    assert 'study_name' in study, "Study should have study_name"
    assert study['study_name'], "study_name should not be empty"

@then('it should have non-empty study_description')
def step_impl(context):
    """Assert that study_description is not empty."""
    study = context.sample_objects['study']
    assert 'study_description' in study, "Study should have study_description"
    assert study['study_description'], "study_description should not be empty"

@then('it should have at least one target_participant')
def step_impl(context):
    """Assert that target_participants has at least one item."""
    study = context.sample_objects['study']
    assert 'target_participants' in study, "Study should have target_participants"
    assert len(study['target_participants']) > 0, "target_participants should have at least one item"

@then('it should have positive planned_sessions')
def step_impl(context):
    """Assert that planned_sessions is positive."""
    study = context.sample_objects['study']
    assert 'planned_sessions' in study, "Study should have planned_sessions"
    assert study['planned_sessions'] > 0, "planned_sessions should be positive"

@then('it should have non-negative completed_sessions')
def step_impl(context):
    """Assert that completed_sessions is non-negative."""
    study = context.sample_objects['study']
    assert 'completed_sessions' in study, "Study should have completed_sessions"
    assert study['completed_sessions'] >= 0, "completed_sessions should be non-negative"

@then('it should have a valid study_status')
def step_impl(context):
    """Assert that study_status is valid."""
    study = context.sample_objects['study']
    assert 'study_status' in study, "Study should have study_status"
    assert study['study_status'] in ['planning', 'in_progress', 'completed', 'on_hold'], "Invalid study_status"

@then('it should have at least one researcher_id')
def step_impl(context):
    """Assert that researcher_ids has at least one item."""
    study = context.sample_objects['study']
    assert 'researcher_ids' in study, "Study should have researcher_ids"
    assert len(study['researcher_ids']) > 0, "researcher_ids should have at least one item"

# Report validation steps
@then('it should have a valid report_name')
def step_impl(context):
    """Assert that report_name is valid."""
    report = context.sample_objects['report']
    assert 'report_name' in report, "Report should have report_name"
    assert report['report_name'], "report_name should not be empty"

@then('it should have non-empty report_description')
def step_impl(context):
    """Assert that report_description is not empty."""
    report = context.sample_objects['report']
    assert 'report_description' in report, "Report should have report_description"
    assert report['report_description'], "report_description should not be empty"

@then('it should have a valid report_type')
def step_impl(context):
    """Assert that report_type is valid."""
    report = context.sample_objects['report']
    assert 'report_type' in report, "Report should have report_type"
    assert report['report_type'] in ['transcript', 'dataset', 'analysis', 'summary'], "Invalid report_type"

@then('it should have non-negative data_count')
def step_impl(context):
    """Assert that data_count is non-negative."""
    report = context.sample_objects['report']
    assert 'data_count' in report, "Report should have data_count"
    assert report['data_count'] >= 0, "data_count should be non-negative"

@then('it should have a valid report_status')
def step_impl(context):
    """Assert that report_status is valid."""
    report = context.sample_objects['report']
    assert 'report_status' in report, "Report should have report_status"
    assert report['report_status'] in ['draft', 'in_review', 'published', 'archived'], "Invalid report_status"

@then('it should have a valid created_by')
def step_impl(context):
    """Assert that created_by is valid."""
    report = context.sample_objects['report']
    assert 'created_by' in report, "Report should have created_by"
    assert report['created_by'], "created_by should not be empty"

# Report Gallery validation steps
@then('it should have a valid gallery_name')
def step_impl(context):
    """Assert that gallery_name is valid."""
    gallery = context.sample_objects['report_gallery']
    assert 'gallery_name' in gallery, "Report Gallery should have gallery_name"
    assert gallery['gallery_name'], "gallery_name should not be empty"

@then('it should have non-empty gallery_description')
def step_impl(context):
    """Assert that gallery_description is not empty."""
    gallery = context.sample_objects['report_gallery']
    assert 'gallery_description' in gallery, "Report Gallery should have gallery_description"
    assert gallery['gallery_description'], "gallery_description should not be empty"

@then('it should have a valid strategic_theme')
def step_impl(context):
    """Assert that strategic_theme is valid."""
    gallery = context.sample_objects['report_gallery']
    assert 'strategic_theme' in gallery, "Report Gallery should have strategic_theme"
    assert gallery['strategic_theme'], "strategic_theme should not be empty"

@then('it should have at least one target_audience')
def step_impl(context):
    """Assert that target_audience has at least one item."""
    gallery = context.sample_objects['report_gallery']
    assert 'target_audience' in gallery, "Report Gallery should have target_audience"
    assert len(gallery['target_audience']) > 0, "target_audience should have at least one item"

@then('it should have non-negative frame_count')
def step_impl(context):
    """Assert that frame_count is non-negative."""
    gallery = context.sample_objects['report_gallery']
    assert 'frame_count' in gallery, "Report Gallery should have frame_count"
    assert gallery['frame_count'] >= 0, "frame_count should be non-negative"

@then('it should have a valid gallery_status')
def step_impl(context):
    """Assert that gallery_status is valid."""
    gallery = context.sample_objects['report_gallery']
    assert 'gallery_status' in gallery, "Report Gallery should have gallery_status"
    assert gallery['gallery_status'] in ['active', 'archived', 'in_development'], "Invalid gallery_status"

@then('it should have at least one strategic_objective')
def step_impl(context):
    """Assert that strategic_objectives has at least one item."""
    gallery = context.sample_objects['report_gallery']
    assert 'strategic_objectives' in gallery, "Report Gallery should have strategic_objectives"
    assert len(gallery['strategic_objectives']) > 0, "strategic_objectives should have at least one item"

# Junction object validation steps
@then('it should reference a valid session_id')
def step_impl(context):
    """Assert that session_id is valid."""
    provenance_junction = context.sample_objects['provenance_junction']
    assert 'session_id' in provenance_junction, "Provenance Junction should have session_id"
    assert provenance_junction['session_id'].startswith('session_'), "session_id should start with 'session_'"

@then('it should reference a valid data_id')
def step_impl(context):
    """Assert that data_id is valid."""
    provenance_junction = context.sample_objects['provenance_junction']
    assert 'data_id' in provenance_junction, "Provenance Junction should have data_id"
    assert provenance_junction['data_id'].startswith('data_'), "data_id should start with 'data_'"

@then('it should have a valid evidence_maturity level')
def step_impl(context):
    """Assert that evidence_maturity is valid."""
    provenance_junction = context.sample_objects['provenance_junction']
    assert 'evidence_maturity' in provenance_junction, "Provenance Junction should have evidence_maturity"
    valid_levels = ['01_assumptive', '02_anecdotal', '03_early_signal', '04_balanced_signal', '05_triangulated']
    assert provenance_junction['evidence_maturity'] in valid_levels, f"Invalid evidence_maturity: {provenance_junction['evidence_maturity']}"

@then('it should have at least one evidence_block')
def step_impl(context):
    """Assert that evidence_block has at least one item."""
    provenance_junction = context.sample_objects['provenance_junction']
    assert 'evidence_block' in provenance_junction, "Provenance Junction should have evidence_block"
    assert len(provenance_junction['evidence_block']) > 0, "evidence_block should have at least one item"

@then('it should have a confidence_score between 0.0 and 1.0')
def step_impl(context):
    """Assert that confidence_score is in valid range."""
    provenance_junction = context.sample_objects['provenance_junction']
    assert 'confidence_score' in provenance_junction, "Provenance Junction should have confidence_score"
    score = provenance_junction['confidence_score']
    assert 0.0 <= score <= 1.0, f"confidence_score should be between 0.0 and 1.0, got {score}"

@then('it should have a valid validation_status')
def step_impl(context):
    """Assert that validation_status is valid."""
    provenance_junction = context.sample_objects['provenance_junction']
    assert 'validation_status' in provenance_junction, "Provenance Junction should have validation_status"
    valid_statuses = ['pending', 'validated', 'needs_review', 'invalid']
    assert provenance_junction['validation_status'] in valid_statuses, f"Invalid validation_status: {provenance_junction['validation_status']}"

# Evidence Junction validation steps
@then('it should reference a valid frame_id')
def step_impl(context):
    """Assert that frame_id is valid."""
    evidence_junction = context.sample_objects['evidence_junction']
    assert 'frame_id' in evidence_junction, "Evidence Junction should have frame_id"
    assert evidence_junction['frame_id'].startswith('frame_'), "frame_id should start with 'frame_'"

@then('it should have a non-empty teaser_quote')
def step_impl(context):
    """Assert that teaser_quote is not empty."""
    evidence_junction = context.sample_objects['evidence_junction']
    assert 'teaser_quote' in evidence_junction, "Evidence Junction should have teaser_quote"
    assert evidence_junction['teaser_quote'], "teaser_quote should not be empty"

@then('it should have a valid quote_attribution')
def step_impl(context):
    """Assert that quote_attribution is valid."""
    evidence_junction = context.sample_objects['evidence_junction']
    assert 'quote_attribution' in evidence_junction, "Evidence Junction should have quote_attribution"
    assert evidence_junction['quote_attribution'], "quote_attribution should not be empty"

@then('it should have at least one strategic_insight')
def step_impl(context):
    """Assert that strategic_insights has at least one item."""
    evidence_junction = context.sample_objects['evidence_junction']
    assert 'strategic_insights' in evidence_junction, "Evidence Junction should have strategic_insights"
    assert len(evidence_junction['strategic_insights']) > 0, "strategic_insights should have at least one item"

@then('it should have a relevance_score between 0.0 and 1.0')
def step_impl(context):
    """Assert that relevance_score is in valid range."""
    evidence_junction = context.sample_objects['evidence_junction']
    assert 'relevance_score' in evidence_junction, "Evidence Junction should have relevance_score"
    score = evidence_junction['relevance_score']
    assert 0.0 <= score <= 1.0, f"relevance_score should be between 0.0 and 1.0, got {score}"

# Insight Junction validation steps
@then('it should reference a valid evidence_id')
def step_impl(context):
    """Assert that evidence_id is valid."""
    insight_junction = context.sample_objects['insight_junction']
    assert 'evidence_id' in insight_junction, "Insight Junction should have evidence_id"
    assert insight_junction['evidence_id'].startswith('evidence_junction_'), "evidence_id should start with 'evidence_junction_'"

@then('it should have a fit_score between 0.0 and 1.0')
def step_impl(context):
    """Assert that fit_score is in valid range."""
    insight_junction = context.sample_objects['insight_junction']
    assert 'fit_score' in insight_junction, "Insight Junction should have fit_score"
    score = insight_junction['fit_score']
    assert 0.0 <= score <= 1.0, f"fit_score should be between 0.0 and 1.0, got {score}"

@then('it should have a non-empty insight_teaser')
def step_impl(context):
    """Assert that insight_teaser is not empty."""
    insight_junction = context.sample_objects['insight_junction']
    assert 'insight_teaser' in insight_junction, "Insight Junction should have insight_teaser"
    assert insight_junction['insight_teaser'], "insight_teaser should not be empty"

@then('it should have at least one insight_story_block')
def step_impl(context):
    """Assert that insight_story_block has at least one item."""
    insight_junction = context.sample_objects['insight_junction']
    assert 'insight_story_block' in insight_junction, "Insight Junction should have insight_story_block"
    assert len(insight_junction['insight_story_block']) > 0, "insight_story_block should have at least one item"

@then('it should have a valid confidence_level')
def step_impl(context):
    """Assert that confidence_level is valid."""
    insight_junction = context.sample_objects['insight_junction']
    assert 'confidence_level' in insight_junction, "Insight Junction should have confidence_level"
    assert insight_junction['confidence_level'] in ['low', 'medium', 'high'], "Invalid confidence_level"

@then('it should have an actionability_score between 0.0 and 1.0')
def step_impl(context):
    """Assert that actionability_score is in valid range."""
    insight_junction = context.sample_objects['insight_junction']
    assert 'actionability_score' in insight_junction, "Insight Junction should have actionability_score"
    score = insight_junction['actionability_score']
    assert 0.0 <= score <= 1.0, f"actionability_score should be between 0.0 and 1.0, got {score}"

@then('it should have a valid priority_level')
def step_impl(context):
    """Assert that priority_level is valid."""
    insight_junction = context.sample_objects['insight_junction']
    assert 'priority_level' in insight_junction, "Insight Junction should have priority_level"
    assert insight_junction['priority_level'] in ['high', 'medium', 'low'], "Invalid priority_level" 