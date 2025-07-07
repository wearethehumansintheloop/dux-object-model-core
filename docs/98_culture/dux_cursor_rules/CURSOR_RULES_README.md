# Cursor Rules System for DUX Projects

## Overview

This repository uses a **flavored cursor rules system** to optimize human-AI collaboration for Declarative UX (DUX) research and development. Each flavor tailors collaboration patterns, automation, and quality standards to a specific context—making it easy to scale best practices across teams and projects.

## Flavors

- **.cursorrules.base** — Core DUX method and dual backlog system. Always included.
- **.cursorrules.research** — Research database, ingestion, and evidence chain patterns.
- **.cursorrules.embedding** — Embedding generation, validation, and troubleshooting workflows.
- **.cursorrules.development** — Rapid prototyping, debugging, and code quality enforcement.

## How to Use

1. **Select a flavor for your current workflow:**
   - For research data ingestion/validation: `cp .cursorrules.research .cursorrules`
   - For embedding automation: `cp .cursorrules.embedding .cursorrules`
   - For rapid development: `cp .cursorrules.development .cursorrules`
   - The base rules are always included by each flavor.

2. **Switch flavors as your context changes:**
   - You can swap flavors at any time to match your current focus.
   - For CI/CD or automation, set the appropriate flavor before running scripts.

3. **Extend for new projects:**
   - Copy `.cursorrules.base` and add a new flavor file (e.g., `.cursorrules.testing` for BDD/test automation).
   - Use the `include: .cursorrules.base` directive to inherit core patterns.
   - Add or override sections as needed for your domain.

## Why Use Flavors?

- **Context-aware guidance:** Each flavor brings the right patterns and automation for the task at hand.
- **Scalability:** New teams can adopt DUX best practices by picking the right flavor.
- **Sustainability:** Patterns and insights are version-controlled and easy to update.
- **Socialization:** Share this README and the flavor files with other teams to spread effective vibecoding.

## Example: Adding a New Flavor

1. Create `.cursorrules.testing`:
   ```markdown
   # Cursor Rules: Testing Flavor
   include: .cursorrules.base
   ## Testing Patterns
   - Write BDD scenarios in stakeholder language
   - Validate edge cases for research integrity
   - ...
   ```
2. Switch to testing mode:
   ```sh
   cp .cursorrules.testing .cursorrules
   ```

## Questions or Contributions?
- Open an issue or PR to suggest new flavors or improvements.
- Reach out to the DUX method maintainers for guidance.

---

**Vibecoding = Human creativity + AI systematic thinking.**

_Share these rules to help your team scale research integrity and software velocity!_ 