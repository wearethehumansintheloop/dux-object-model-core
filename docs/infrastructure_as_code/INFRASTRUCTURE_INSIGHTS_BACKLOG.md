### Containerize DUX Core for Cross-Platform Integration
**Type**: Infrastructure
**Context**: Demo needs to connect from localhost:8504 to core services. Currently core is NOT containerized, making integration challenging.
**Description**:
The DUX Object Model Core needs containerization to:
- Enable consistent deployment across environments
- Simplify integration with platform services (running on different ports)
- Support both local development (localhost:8504) and production deployments
- Allow proper network isolation and service discovery
- Facilitate CI/CD pipelines

**Next Step**:
1. Create Dockerfile for core services
2. Add docker-compose.yml for local development stack
3. Configure network bridges for platform<->core communication
4. Document container networking for demos (e.g., platform on :8504 reaching core API)

### Codify Persona-Driven Prompting ("Erin Brockovich" Model)
**Type**: Encoding
**Context**: Emerged from the discussion on how to ensure the strategic intent behind a `Problem` object is understood by the LLM during object extraction.
**Description**:
Instead of just providing a schema and instructions, we cast the LLM into a specific, mission-driven persona (e.g., "Erin Brockovich") with a clear point of view and Job-to-be-Done. This transforms the LLM from a passive transcriber into an active, opinionated analyst, leading to higher-quality, more strategic outputs. The persona acts as a cognitive anchor for the desired analytical style.

**Next Step (optional)**:
Apply this persona-driven model to the prompts for other DUX objects (`Behavior`, `Result`, etc.) to create a consistent "cast of characters" for the extraction pipeline.

### Schema Version Mismatch Technical Debt
**Type**: Infrastructure
**Timestamp**: 2025-07-16T00:00:00Z
**Context**: While fixing the dux-white-label-ui Problems detail page, discovered widespread v9.5 vs v9.6 schema mismatches
**Description**: 
The frontend application is importing from outdated v9.5 schemas while the core system has moved to v9.6 with breaking changes (decomposed job_statement structure). This causes:
- TypeScript build errors when types don't match runtime data
- Runtime errors when accessing properties that have changed structure
- Wasted development time debugging and fixing individual instances instead of systemic issues
- Mock data out of sync with actual schema expectations

Time wasted: ~30 minutes per occurrence tracking down schema version issues, understanding the changes, and implementing fixes. This multiplies across all components using DUX objects.

**Root Cause**: No automated schema version enforcement or migration tooling. Developers must manually update imports and data structures.

**Next Step**: 
1. Create automated schema migration scripts that update imports from v9.5 to v9.6
2. Add CI/CD checks to prevent importing from deprecated schema versions
3. Create a schema version compatibility matrix documentation
4. Consider implementing a schema versioning strategy with proper deprecation warnings
