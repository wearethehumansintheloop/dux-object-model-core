### Codify Persona-Driven Prompting ("Erin Brockovich" Model)
**Type**: Encoding
**Context**: Emerged from the discussion on how to ensure the strategic intent behind a `Problem` object is understood by the LLM during object extraction.
**Description**:
Instead of just providing a schema and instructions, we cast the LLM into a specific, mission-driven persona (e.g., "Erin Brockovich") with a clear point of view and Job-to-be-Done. This transforms the LLM from a passive transcriber into an active, opinionated analyst, leading to higher-quality, more strategic outputs. The persona acts as a cognitive anchor for the desired analytical style.

**Next Step (optional)**:
Apply this persona-driven model to the prompts for other DUX objects (`Behavior`, `Result`, etc.) to create a consistent "cast of characters" for the extraction pipeline.
