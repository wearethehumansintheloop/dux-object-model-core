# Setting Up Claude Code as Your Research Platform Dev Manager

A comprehensive guide for establishing Claude as a persistent development manager for research platform teams working with complex schema infrastructure.

## Overview

This guide shows how to create a consistent AI development manager using Claude Code by separating **persistent agent identity** from **dynamic sprint context**. Perfect for teams working with evolving infrastructure, multiple backlogs, and complex integration requirements.

## Why This Approach Works

### Traditional Problem
- Generic AI coding assistance lacks project context
- Inconsistent responses across development sessions  
- No understanding of team responsibilities or architecture
- Context gets lost between conversations

### Our Solution
**Two-layer context system:**
1. **Persistent Agent Profile** - Role, architecture knowledge, standards (rarely changes)
2. **Dynamic Sprint Context** - Current goals, tickets, blockers (updates weekly)

**Result:** Consistent "dev manager" behavior focused on immediate deliverables.

## Prerequisites

- Claude Code installed and configured
- Access to your project repository
- Basic understanding of your team's architecture and workflow

## Step 1: Create Context Structure

```bash
# From your project root
mkdir -p .claude

# Create the two core files
touch .claude/agent-profile.md
touch .claude/current-sprint.md
```

## Step 2: Build Your Agent Profile

Create `.claude/agent-profile.md` with these sections:

### Essential Components
```markdown
# Agent Profile: [Your Team] Development Manager

## Role Definition
- Your team's specific responsibilities
- Management philosophy and approach
- Collaboration style and priorities

## Infrastructure Knowledge  
- Current system architecture
- Known limitations and transition states
- Integration points with other teams/systems

## Team Responsibilities
- What your team owns vs. what you consume
- Service boundaries and interfaces
- Key technologies and frameworks

## Implementation Patterns
- Standard code patterns for your domain
- Architecture principles
- Quality standards and practices

## Backlog Management
- How you organize work (e.g., triple backlog system)
- Prioritization principles
- Cross-functional considerations
```

### Example: Research Platform Agent Profile
```markdown
## Team Responsibilities

### What Research Platform Owns
- Service Infrastructure: Neo4j database, API endpoints
- Instance Creation: Extract objects from research data
- Knowledge Graph: Storage and querying
- LLM Integration: Model orchestration

### What We Consume  
- JSON Schemas: From Object Model Core
- Agent Prompts: Auto-generated extraction agents
- Validation Rules: Schema compliance

## Backlog Management

### Triple Backlog System
1. **UX-Infrastructure as Code**: Pipeline reliability, DevOps
2. **Coaching (LLM-Assisted)**: Natural language features, user guidance  
3. **Architecture**: System design, technical debt, scalability
```

## Step 3: Create Sprint Context Template

Create `.claude/current-sprint.md` for dynamic work tracking:

```markdown
# Current Sprint: [Sprint Name]
**Sprint Dates**: [Dates]
**Sprint Goal**: [One sentence objective]

## Active Tickets

### 🏗️ UX-Infrastructure as Code
- [ ] **[Ticket Name]**
  - Backlog: UX-Infrastructure
  - File: `path/to/file.py`
  - Description and acceptance criteria

### 🤖 Coaching/LLM-Assisted  
- [ ] **[Ticket Name]**
  - Backlog: Coaching
  - Dependencies or special considerations

### 🏛️ Architecture
- [ ] **[Ticket Name]**
  - Backlog: Architecture
  - Cross-backlog dependencies noted

## Current Focus Area
What you're actively working on right now

## Immediate Blockers/Decisions  
- [ ] Decision needed: [Specific choice required]
- [ ] Blocker: [What's preventing progress]

## Acceptance Criteria
Clear success metrics for this sprint

## Backlog Considerations
- Cross-backlog dependencies
- Post-sprint impact on other backlogs
```

## Step 4: Usage Patterns

### Basic Usage
```bash
# Include both context files
claude --include-file .claude/agent-profile.md --include-file .claude/current-sprint.md "Help me implement the schema loader"

# Agent-only for architectural questions
claude --include-file .claude/agent-profile.md "How should we handle schema validation errors?"

# Sprint-only for immediate work
claude --include-file .claude/current-sprint.md "What should I work on next?"
```

### Create Helper Scripts

**Option 1: Simple wrapper**
```bash
# claude-dev.sh
#!/bin/bash
claude --include-file .claude/agent-profile.md --include-file .claude/current-sprint.md "$@"
```

**Option 2: Context selector**
```bash
# claude-ctx.sh
#!/bin/bash
case "$1" in
  "agent") claude --include-file .claude/agent-profile.md "${@:2}" ;;
  "sprint") claude --include-file .claude/current-sprint.md "${@:2}" ;;
  "full") claude --include-file .claude/agent-profile.md --include-file .claude/current-sprint.md "${@:2}" ;;
  *) echo "Usage: $0 {agent|sprint|full} [prompt]" ;;
esac
```

Usage:
```bash
./claude-ctx.sh full "help with schema implementation"
./claude-ctx.sh agent "review our architecture decisions"
./claude-ctx.sh sprint "what's my next task?"
```

## Step 5: Maintenance Workflow

### Weekly Sprint Updates
```bash
# Update sprint context
vim .claude/current-sprint.md

# Update:
# - Sprint dates and goals
# - Active tickets and priorities  
# - Current blockers and decisions
# - Acceptance criteria
```

### Monthly Agent Profile Reviews
```bash
# Review agent profile
vim .claude/agent-profile.md

# Consider updating:
# - Infrastructure knowledge (if architecture changed)
# - Team responsibilities (if scope changed)
# - Implementation patterns (if standards evolved)
# - Backlog structure (if process changed)
```

### Version Control Best Practices
```bash
# Track changes but keep sensitive info out
echo ".claude/secrets.md" >> .gitignore

# Commit context files for team sharing
git add .claude/agent-profile.md .claude/current-sprint.md
git commit -m "Update dev manager context for Sprint X"
```

## Advanced Patterns

### Team-Specific Profiles
```bash
# Different profiles for different team members
.claude/
├── agent-profile-backend.md
├── agent-profile-frontend.md  
├── agent-profile-devops.md
└── current-sprint.md
```

### Project-Specific Context
```bash
# Multiple projects with shared agent profile
.claude/
├── agent-profile.md              # Shared team identity
├── project-a-sprint.md           # Project A current work
├── project-b-sprint.md           # Project B current work
└── architecture-decisions.md     # Cross-project considerations
```

### Integration Context
```bash
# Include external system context
claude --include-file .claude/agent-profile.md \
       --include-file .claude/current-sprint.md \
       --include-file .claude/external-apis.md \
       "help me integrate with the new schema API"
```

## Benefits Realized

### Consistent Behavior
- Claude remembers your team's role and responsibilities
- Consistent architectural guidance across sessions
- Maintains context about ongoing infrastructure transitions

### Focused Development
- Sprint context keeps Claude aligned with immediate goals
- Clear priorities and acceptance criteria
- Blockers and decisions surfaced automatically

### Scalable Process
- Easy onboarding for new team members
- Shareable context across the team
- Evolution of agent knowledge over time

### Quality Assurance
- Built-in code standards and architectural principles
- Cross-backlog dependency awareness
- Research integrity and audit trail considerations

## Example Session

```bash
$ ./claude-dev.sh "I need to implement schema loading for the DUX objects"

> I understand you're working on the schema loader implementation from your UX-Infrastructure backlog. Based on your current sprint context, this is a Priority 1 item that other tickets depend on.

> Given the infrastructure transition state, I recommend implementing the temporary path approach first:

> ```python
> def load_schema(object_type: str):
>     # Using temporary archive location during Core cleanup
>     core_path = Path(__file__).parent.parent.parent / "dux-object-model-core"
>     schema_path = core_path / f"docs/99_archive/schema_backup_20250707/dux_v9.6_split_schema/dux_object_{object_type.lower()}.json"
>     
>     try:
>         with open(schema_path) as f:
>             return json.load(f)
>     except FileNotFoundError:
>         # Graceful failure during transition
>         logger.warning(f"Schema not found for {object_type} at {schema_path}")
>         return None
> ```

> This addresses your acceptance criteria for graceful failure and configurable paths. Should we also add the configuration system for the future path updates?
```

## Troubleshooting

### Claude Seems Generic
- **Check**: Are you including the agent profile file?
- **Fix**: Always use `--include-file .claude/agent-profile.md`

### Responses Not Sprint-Focused  
- **Check**: Is your current sprint context up to date?
- **Fix**: Update `.claude/current-sprint.md` with current goals

### Context Too Long
- **Check**: Are your files too verbose?
- **Fix**: Focus on essential context, break into smaller files

### Inconsistent Between Sessions
- **Check**: Are you using the same context files?
- **Fix**: Use helper scripts to ensure consistency

## Team Adoption Tips

1. **Start Simple**: Begin with basic agent profile, add complexity over time
2. **Share Context**: Commit context files for team consistency  
3. **Regular Reviews**: Update context in sprint retrospectives
4. **Document Decisions**: Capture architectural decisions in agent profile
5. **Iterate**: Refine based on what works for your team

## Conclusion

This two-layer context system transforms Claude Code from a generic coding assistant into a knowledgeable team member who understands your architecture, priorities, and current goals. The separation of persistent identity from dynamic work context creates consistency while maintaining focus on immediate deliverables.

The result: more productive development sessions, better architectural decisions, and reduced context switching overhead.