# Development Backlog

This file tracks development tasks, feature requests, and bug fixes for the DUX Object Model (Core) project.

---

### Tasks

- [ ] **Ensure BDD test suite available for all stepped workflows**
  - **Description:** Implement comprehensive BDD (Behavior-Driven Development) test coverage for all multi-stage workflows in the system, similar to the HITL pipeline tests.
  - **Rationale:** BDD tests provide regression prevention, clear documentation of expected behavior, and enable confident refactoring. They serve as living documentation that validates workflow orchestration logic.
  - **Acceptance Criteria:**
    - Create `.feature` files for each major workflow (e.g., HITL pipeline, schema generation, object validation)
    - Implement step definitions in `tests/features/steps/` following Behave conventions
    - Include scenarios for happy paths, error conditions, and edge cases
    - Add CI/CD integration to run BDD tests on pull requests and merges
    - Create manual test runners for environments without Behave installed
    - Document how to write and maintain BDD tests for new workflows
  - **Priority:** High
  - **Added:** 2025-07-08

- [ ] **Implement a validation pipeline for agent prompts.**
  - **Description:** Create an automated process to ensure that the example outputs within each agent's prompt file (e.g., `archivist_prompt.md`) are valid against their corresponding JSON schemas (e.g., `provenance_schema.json`).
  - **Rationale:** This prevents prompt drift and ensures that agents are always trained on valid, up-to-date examples. It improves the reliability of the entire pipeline by treating prompts as first-class source code with their own quality checks.
  - **Acceptance Criteria:**
    - A script is created that can parse a given prompt markdown file.
    - The script successfully extracts the example JSON block from the prompt.
    - The script validates the extracted JSON against the relevant schema file.
    - This validation check is integrated into the CI/CD pipeline to fail the build if a prompt contains an invalid example.
