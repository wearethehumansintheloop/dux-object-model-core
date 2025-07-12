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
