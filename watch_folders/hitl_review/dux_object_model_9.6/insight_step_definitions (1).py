# steps/validate_insight_object_steps.py

from behave import given, when, then
import json

@given('a valid Insight JSON object')
def step_given_valid_insight(context):
    with open('fixtures/insight_object.json') as f:
        context.insight = json.load(f)

@when('the system parses the insight_chain field')
def step_when_parse_insight_chain(context):
    context.chain_objects = []
    for item in context.insight.get("insight_chain", []):
        context.chain_objects.append(item)

@then('it should extract Problem, Behavior, and Result objects using their IDs')
def step_then_extract_objects(context):
    required_types = {"Problem", "Behavior", "Result"}
    types_found = {obj.get("object_type") for obj in context.chain_objects}
    assert required_types.issubset(types_found)

@then('each related_object must include its object_type, job_statement, and evidence_maturity')
def step_then_validate_fields(context):
    for obj in context.chain_objects:
        assert obj.get("object_type")
        assert obj.get("job_statement")
        assert obj.get("evidence_maturity")

@then('each related_object must have a list of valid provenance IDs')
def step_then_validate_provenance_links(context):
    for obj in context.chain_objects:
        assert isinstance(obj.get("evidence"), list)
        assert all(isinstance(p_id, str) for p_id in obj["evidence"])

@then('each provenance ID must correspond to a valid Provenance object')
def step_then_check_provenance_validity(context):
    with open('fixtures/provenance_objects.json') as f:
        provenance_list = json.load(f)
        provenance_ids = {p["id"] for p in provenance_list}
    for obj in context.chain_objects:
        for pid in obj.get("evidence", []):
            assert pid in provenance_ids

@then('the score should reflect the weakest evidence_maturity link')
def step_then_score_reflects_weakest(context):
    maturity_order = ["01_assumptive", "02_anecdotal", "03_early_signal", "04_balanced_signal", "05_triangulated"]
    maturity_scores = [maturity_order.index(obj.get("evidence_maturity")) for obj in context.chain_objects]
    weakest = min(maturity_scores)
    context.weakest_score = maturity_order[weakest]
    assert context.weakest_score

@then('annotate if the weakest maturity is below \'03_early_signal\'')
def step_then_annotate_if_weak(context):
    assert context.weakest_score in ["01_assumptive", "02_anecdotal", "03_early_signal"]

@then('each provenance ID must reference a provenance object with a valid evidence_block')
def step_then_validate_evidence_block(context):
    with open('fixtures/provenance_objects.json') as f:
        provenance_list = json.load(f)
    for p in provenance_list:
        block = p.get("evidence_block", {})
        assert block.get("source_filename")
        assert block.get("quote")
        assert block.get("citation")
        assert block.get("evidence_type")

@then('the system should not duplicate entries')
def step_then_no_duplicates(context):
    seen = set()
    for obj in context.chain_objects:
        oid = obj["id"]
        assert oid not in seen
        seen.add(oid)

@then('it should confirm object_type consistency for each ID')
def step_then_type_consistency(context):
    id_type_map = {}
    for obj in context.chain_objects:
        oid = obj["id"]
        otype = obj["object_type"]
        if oid in id_type_map:
            assert id_type_map[oid] == otype
        else:
            id_type_map[oid] = otype
