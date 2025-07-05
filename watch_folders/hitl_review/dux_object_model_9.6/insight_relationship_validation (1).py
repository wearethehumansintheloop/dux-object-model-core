# Insight Relationship Validation (.feature in Markdown)

## Feature: Validate Insight Object relationships

### Scenario: Validate full Insight chain linkage and evidence propagation
- **Given** a valid Insight JSON object  
- **When** the system parses the `insight_chain` field  
- **Then** it should extract Problem, Behavior, and Result objects using their IDs  
- **And** each `related_object` must include its `object_type`, `job_statement`, and `evidence_maturity`  
- **And** each `related_object` must have a list of valid Provenance IDs  
- **And** each Provenance ID must correspond to a valid Provenance object

### Scenario: Validate fit_score inference based on evidence_maturity
- **Given** an Insight object with linked Problem, Behavior, and Result  
- **When** the `fit_score` is calculated  
- **Then** the score should reflect the weakest `evidence_maturity` link  
- **And** annotate if the weakest maturity is below `'03_early_signal'`

### Scenario: Validate inline provenance rendering eligibility
- **Given** `related_objects` include provenance arrays  
- **Then** each Provenance ID must reference a Provenance object with a valid `evidence_block`  
- **And** the `evidence_block` must include `source_filename`, `quote`, `citation`, and `evidence_type`

### Scenario: Validate uniqueness and consistency across related_objects
- **Given** an Insight object with a related Problem already included  
- **When** another object with same ID appears  
- **Then** the system should not duplicate entries  
- **And** it should confirm `object_type` consistency for each ID
