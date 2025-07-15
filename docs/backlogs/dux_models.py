from typing import List, Dict, Optional, Literal
from datetime import datetime
from pydantic import BaseModel, Field

class DuxObject(BaseModel):
    """Base model for all DUX objects."""
    id: str = Field(..., description="Unique identifier for the object.")
    name: str = Field(..., description="Human-readable name of the object.")
    description: str = Field(..., description="Detailed description of the object.")
    tags: Optional[List[str]] = Field(None, description="Categorization tags for the object.")
    updated_at: datetime = Field(..., description="Timestamp of the last update.")
    created_at: Optional[datetime] = Field(None, description="Timestamp of creation.")
    object_type: Optional[str] = Field(None, description="Type of the DUX object (e.g., 'Problem', 'Behavior').")

class ProvenanceEvidenceBlock(BaseModel):
    """Details for an evidence block within Provenance."""
    source_filename: str = Field(..., description="Filename of the source document.")
    participant_id: str = Field(..., description="Identifier of the participant, if applicable.")
    timestamp_in: str = Field(..., description="Start timestamp within the source (e.g., '00:02:14').")
    timestamp_out: str = Field(..., description="End timestamp within the source (e.g., '00:03:45').")
    teaser: Optional[str] = Field(None, description="Short summary or teaser of the evidence.")
    quote: str = Field(..., description="Direct quote or key finding from the source.")
    citation: str = Field(..., description="Full citation for the evidence.")
    evidence_type: str = Field(..., description="Type of evidence (e.g., 'pull_quote', 'user_research_finding').")

class Provenance(BaseModel):
    """Represents a first-class Provenance object."""
    object_type: Literal["Provenance"] = "Provenance"
    id: str = Field(..., description="Unique identifier for the provenance record.")
    evidence_block: ProvenanceEvidenceBlock = Field(..., description="Details of the evidence block.")
    created_at: datetime = Field(..., description="Timestamp of creation.")

class Problem(DuxObject):
    """Represents a Problem object."""
    object_type: Literal["Problem"] = "Problem"
    job_statement: str = Field(..., description="Job-to-be-Done statement for the problem.")
    end_user: List[str] = Field(..., description="List of end-user personas affected by the problem.")
    what_is_at_stake: str = Field(..., description="Description of the risks or losses associated with the problem.")
    protocol_url: str = Field(..., description="URL to the research protocol or related document.")
    evidence_teaser: str = Field(..., description="A short, compelling quote or finding summarizing the evidence.")
    evidence_maturity: str = Field(..., description="Maturity level of the evidence (e.g., '04_balanced').")
    evidence: List[str] = Field(..., description="List of Provenance IDs linked to this problem.")
    result_ids: List[Dict[str, str]] = Field(..., description="List of related Result IDs with context.")
    useroutcome_ids: List[Dict[str, str]] = Field(..., description="List of related UserOutcome IDs with context.")
    flow_ids: List[Dict[str, str]] = Field(..., description="List of related Flow IDs with context.")
    # Optional fields for compatibility with old cards
    opportunity_score: Optional[float] = None
    importance: Optional[float] = None
    satisfaction: Optional[float] = None

class Behavior(DuxObject):
    """Represents a Behavior object."""
    end_user: str = Field(..., description="The end-user persona performing this behavior.")
    test_status: Literal["passing", "failing", "in-progress"] = Field(..., description="Current test status of the behavior.")
    state: Literal["released", "in_ci", "stub"] = Field(..., description="Current development state of the behavior.")
    percent_steps_passing: float = Field(..., description="Percentage of associated test steps that are passing.")
    key: Optional[bool] = Field(None, description="Indicates if this is a key behavior.")
    acceptance_criteria: List[str] = Field(..., description="List of acceptance criteria for the behavior.")
    linked_issue_ids: List[str] = Field(..., description="List of linked issue IDs (e.g., JIRA tickets).")
    user_enablement: Optional[str] = Field(None, description="How the user is enabled by this behavior.")
    behavior_type: Optional[str] = Field(None, description="Type of behavior (e.g., 'system_action', 'organizational_process').")
    signals: Optional[List[str]] = Field(None, description="Key signals or indicators related to the behavior.")

class Result(DuxObject):
    """Represents a Result object."""
    owner_team: str = Field(..., description="Team responsible for this result.")
    state: Literal["passing", "failing", "in_progress", "blocked"] = Field(..., description="Current state of the result.")
    percent_behaviors_passing: float = Field(..., description="Percentage of linked behaviors that are passing.")
    outcome_metrics: Dict[str, str] = Field(..., description="Key metrics and their values for this result.")
    success_criteria: List[str] = Field(..., description="List of success criteria for the result.")
    behavior_ids: List[str] = Field(..., description="List of Behavior IDs linked to this result.")
    target_impact: Optional[str] = Field(None, description="Description of the target impact of this result.")

class Persona(DuxObject):
    """Represents a Persona object."""
    role: str = Field(..., description="Role of the persona.")
    goals: List[str] = Field(..., description="List of primary goals for the persona.")
    frustrations: List[str] = Field(..., description="List of primary frustrations for the persona.")
    key_behaviors: List[str] = Field(..., description="List of key behaviors associated with the persona.")

class Journey(DuxObject):
    """Represents a Journey object (deprecated, replaced by Flow)."""
    persona_id: str = Field(..., description="ID of the persona associated with this journey.")
    entry_point: str = Field(..., description="Description of the entry point into the journey.")
    steps: List[Dict[str, str]] = Field(..., description="List of steps in the journey, each with name and description.")
    success_metrics: List[str] = Field(..., description="List of success metrics for the journey.")

class Insight(DuxObject):
    """Represents an Insight object."""
    insight_story_block: str = Field(..., description="Human-readable, editable prose of the insight story.")
    problem_id: str = Field(..., description="ID of the linked Problem object.")
    behavior_id: str = Field(..., description="ID of the linked Behavior object.")
    result_id: str = Field(..., description="ID of the linked Result object.")
    user_outcome_id: str = Field(..., description="ID of the linked UserOutcome object.")
    evidence_maturity: Literal["01_assumptive", "02_anecdotal", "03_early", "04_balanced", "05_triangulated"] = Field(..., description="Maturity level of the insight's evidence.")
    insight_teaser: Optional[str] = Field(None, description="A short, compelling teaser for the insight.")
    insight_chain: Optional[List[str]] = Field(None, description="Ordered list of object IDs forming the insight chain.")
    related_objects: Optional[List[Dict[str, str]]] = Field(None, description="List of related objects with their types.")

class UserOutcome(DuxObject):
    """Represents a UserOutcome object."""
    object_type: Literal["UserOutcome"] = "UserOutcome"
    end_user: str = Field(..., description="The end-user persona benefiting from this outcome.")
    source_behavior_ids: List[str] = Field(..., description="List of Behavior IDs that contribute to this outcome.")
    key_signals: List[str] = Field(..., description="List of key signals indicating the outcome's achievement.")
    outcome_metrics: Dict[str, str] = Field(..., description="Key metrics and their values for this user outcome.")

class Flow(DuxObject):
    """Represents a Flow object."""
    object_type: Literal["Flow"] = "Flow"
    user_scenario: str = Field(..., description="A short narrative describing the user's situation and goal for this flow.")
    flow_type: Literal["golden_path", "edge_case", "recovery"] = Field(..., description="Type of flow.")
    linked_problem_ids: List[str] = Field(..., description="List of Problem IDs linked to this flow.")
    linked_user_outcome_ids: List[str] = Field(..., description="List of UserOutcome IDs linked to this flow.")
    behavior_sequence: List[str] = Field(..., description="Ordered list of Behavior IDs in the flow sequence.")

# Example usage (for FastAPI integration)
if __name__ == "__main__":
    # This part would typically be in your FastAPI app file (e.g., main.py)
    # from fastapi import FastAPI
    # app = FastAPI()

    # @app.get("/problems/{problem_id}", response_model=Problem)
    # async def get_problem(problem_id: str):
    #     # Fetch problem from DB
    #     return Problem(
    #         id=problem_id,
    #         name="Example Problem",
    #         description="This is an example problem.",
    #         updated_at=datetime.now(),
    #         job_statement="When I need to do X, I want to do Y, so I can achieve Z.",
    #         end_user=["Developer"],
    #         what_is_at_stake="Lost productivity",
    #         protocol_url="http://example.com/protocol",
    #         evidence_teaser="Users report difficulty with X.",
    #         evidence_maturity="04_balanced",
    #         evidence=["prov_123"],
    #         result_ids=[{"id": "res_456", "reference_context": "Context for result"}],
    #         useroutcome_ids=[{"id": "uo_789", "reference_context": "Context for outcome"}],
    #         flow_ids=[{"id": "flow_001", "reference_context": "Context for flow"}],
    #     )

    print("Pydantic models for DUX objects defined. You can import these into your FastAPI application.")
    print("\nExample Problem Model Schema:")
    print(Problem.schema_json(indent=2))
