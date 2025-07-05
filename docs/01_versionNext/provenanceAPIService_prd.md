# Provenance API Service - Product Requirements Document

## Executive Summary
**Problem**: Research evidence is scattered across transcripts, surveys, and documents with no systematic way to quantify, anonymize, or reference it for product decisions.

**Solution**: Internal API service that serves anonymized, quantified research data through a simple REST interface.

**Success Metrics**: 
- 100% evidence attribution in DUX objects
- <2 second API response times
- Zero PII exposure in API responses

## Core Requirements

### 1. Evidence Custodian Service
- **Anonymization Engine**: Convert participant names → P001, P002 format
- **Evidence Aggregation**: Count instances, confidence levels, participant coverage
- **Source Attribution**: Track filename, timestamps, collection method
- **Ethical Compliance**: Only serve data with proper consent/clearance

### 2. Simple REST API
```
GET /evidence/summary                    # Total counts, confidence distribution
GET /evidence/by-object/{object_id}      # Evidence backing specific DUX object
GET /evidence/by-participant-role/{role} # Evidence from specific personas
GET /evidence/search?q={query}           # Search across evidence citations
```

### 3. Dashboard Interface
- **Research Overview**: Total evidence, participant count, confidence metrics
- **Evidence Quality**: Verification rates, confidence distribution
- **Coverage Analysis**: Which objects/personas have strong evidence backing
- **Export Capability**: CSV/JSON downloads for further analysis

## Technical Architecture

### Data Model (Simplified Provenance Object)
```json
{
  "id": "prov_001",
  "source_filename": "interview_p001.md",
  "timestamp_in": "00:05:30",
  "timestamp_out": "00:06:15", 
  "participant_id": "P001",
  "context": "pre-prototype interview",
  "linked_object_ids": ["behavior_001", "problem_002"]
}
```

### Security & Privacy
- **No raw quotes** in API responses (aggregated data only)
- **Participant anonymization** at ingestion
- **Consent verification** before data inclusion
- **Access controls** for internal team use only

## Implementation Plan

### Phase 1: Core API (Sprint 1)
- Basic Provenance object schema
- Evidence ingestion pipeline
- Simple REST endpoints
- Anonymization layer

### Phase 2: Dashboard (Sprint 2) 
- React dashboard with charts
- Evidence quality metrics
- Export functionality
- Mobile responsive design

### Phase 3: Integration (Sprint 3)
- DUX object schema updates to reference provenance
- BDD test validation
- Automated evidence linking
- Performance optimization

## Success Criteria
- [ ] All DUX objects can reference evidence through provenance_id
- [ ] Dashboard displays real research data without PII
- [ ] API responds <2s for all endpoints
- [ ] 100% evidence has ethical clearance verification
- [ ] Test suite validates all provenance relationships

## Dependencies
- v9.5 schema validation completion
- Test data cleanup and anonymization
- BDD test suite updates for provenance validation

## Timeline: 3 Sprints (6 weeks)
- Sprint 1: Core API + schema (2 weeks)
- Sprint 2: Dashboard + visualization (2 weeks) 
- Sprint 3: Integration + testing (2 weeks)

**CURRENT STATUS**: Feature scoped, moving to roadmap. Focus returns to v9.5 validation and test suite completion.