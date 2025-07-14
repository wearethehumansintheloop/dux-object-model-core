# Development Backlog

This file tracks development tasks, feature requests, and bug fixes for the DUX Object Model (Core) project.

---

### Tasks

- [ ] **Implement a validation pipeline for agent prompts.**
  - **Description:** Create an automated process to ensure that the example outputs within each agent's prompt file (e.g., `archivist_prompt.md`) are valid against their corresponding JSON schemas (e.g., `provenance_schema.json`).
  - **Rationale:** This prevents prompt drift and ensures that agents are always trained on valid, up-to-date examples. It improves the reliability of the entire pipeline by treating prompts as first-class source code with their own quality checks.
  - **Acceptance Criteria:**
    - A script is created that can parse a given prompt markdown file.
    - The script successfully extracts the example JSON block from the prompt.
    - The script validates the extracted JSON against the relevant schema file.
    - This validation check is integrated into the CI/CD pipeline to fail the build if a prompt contains an invalid example.
