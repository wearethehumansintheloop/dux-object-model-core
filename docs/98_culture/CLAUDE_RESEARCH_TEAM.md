# CLAUDE.md - Research Team Guide

This file provides guidance to Claude Code (claude.ai/code) when helping research teams use the DUX Object Model Core infrastructure.

## 🎯 The Promise: Weekend-Free Research

**What we solved**: No more weekend debugging sessions from schema synchronization failures. The infrastructure handles all the complexity so you can focus on research insights.

## 🚀 Quick Start: Your First Object Validation

```bash
# 1. Create your research object following the template
# 2. Place it in the entry point
cp my_problem_definition.md watch_folders/hitl_review/

# 3. Run validation (it handles all 4 stages automatically)
python scripts/validation/validate_dux_objects.py

# 4. Check results
# ✅ Success → watch_folders/hitl_promotion_candidates/
# ❌ Failed → watch_folders/hitl_failed/ (with clear error messages)
```

## 📋 Naming Your Files (This is STRICT!)

Your file MUST follow this pattern:
```
{object_type}_*_*_object_model_definition.md
```

### ✅ Good Examples
- `problem_user_onboarding_v1_object_model_definition.md`
- `behavior_search_filtering_draft_object_model_definition.md`
- `result_revenue_increase_2025_object_model_definition.md`

### ❌ Bad Examples (Will Be Rejected)
- `user_onboarding_problem.md` ← Wrong pattern
- `problem_definition.md` ← Missing middle section and suffix
- `Problem_User_Onboarding_v1_object_model_definition.md` ← Must be lowercase

## 🗂️ Where Files Go (The Journey)

```
Your object's journey through validation:

1. hitl_review/ ← You put files here
       ↓
2. hitl_review_queue/{type}_objects/ ← Auto-sorted by type
       ↓
3. [4-Stage Validation Pipeline Runs]
       ↓
4a. hitl_promotion_candidates/ ← Success! Ready for production
    OR
4b. hitl_failed/ ← Failed with helpful error logs
```

## 📝 The Sacred Template

Every object MUST follow this structure (found in `docs/100_START_HERE/dux_object_template.md`):

```markdown
# [EMOJI] [Object Name] Object

## 🎯 Purpose & Strategic Role
What this object does and why it matters in the DUX ecosystem

## 🧠 "What would you say... you do here?"
> When I need to [situation], I want to [goal], so that I can [outcome].

## 💡 Why the [Object Name] Object Matters
- Clear benefit #1
- Clear benefit #2
- Clear benefit #3
- Clear benefit #4

## 📋 Schema Attributes
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| object_type | string | Yes | Must match object type exactly |
| id | string | Yes | Must follow naming pattern |
| [your fields] | [types] | Yes/No | Clear descriptions |

## 📦 Canonical Example (Schema-Compliant)
```json
{
  "object_type": "YourType",
  "id": "yourtype_example_001",
  // ... rest of your valid example
}
```

## 🔗 Structural Role & Usage Notes
- How this connects to other objects
- Important constraints
- Usage guidance
```

## 🌐 Why Natural Language Matters

DUX uses **natural language as scaling technology**:
- Write in plain, conversational language
- Your insights will work across cultures and time zones
- Technical teams can understand user needs clearly
- Global teams can adapt insights to local contexts

**Remember**: You write in markdown (human-friendly) → System generates JSON (machine-friendly)

## 🔧 Essential Commands

### Daily Use
```bash
# Validate your objects
cd scripts/validation
python validate_dux_objects.py

# Check validation for specific types
python validate_problem_objects.py
python validate_behavior_objects.py
```

### See What's Valid
```bash
# Run full governance check
cd scripts/governance
python run_all_governance.py
```

### When Schemas Update
```bash
# This regenerates JSON from markdown definitions
python scripts/update_schemas.py
```

## 🤖 Your Objects Generate AI Agents!

When you create an object definition, the system automatically generates extraction agents:

- **Problem object** → Problem extraction agent that thinks like "Erin Brockovich of product strategy"
- **Behavior object** → Behavior identification agent
- **Result object** → Outcome extraction agent
- **Flow object** → Journey mapping agent

These agents use YOUR schema to extract consistent data from research artifacts.

## 🎯 Object ID Patterns

Each object type has a specific ID pattern:

| Type | Pattern | Example |
|------|---------|---------|
| Problem | `problem_*` | `problem_onboarding_friction_001` |
| Behavior | `behavior_*` | `behavior_search_products_001` |
| Result | `result_*` | `result_conversion_increase_001` |
| Flow | `flow_*` | `flow_purchase_journey_001` |
| UserOutcome | `useroutcome_*` | `useroutcome_easy_checkout_001` |
| Provenance | `prov_*` | `prov_interview_transcript_001` |
| Insight | `insight_*` | `insight_payment_friction_001` |

## 🚨 When Things Go Wrong

### Validation Failed?
1. Check `watch_folders/hitl_failed/your_file_name_errors.txt`
2. Error messages tell you exactly what's wrong
3. Common fixes:
   - Missing required fields
   - Wrong field types
   - Template structure not followed
   - Invalid JSON in canonical example

### Can't Find Your File?
- Check it matches naming convention exactly
- Look in `hitl_rejected/` if naming was wrong
- Check `hitl_review_queue/` for processing status

### Schema Seems Wrong?
- Schemas are auto-generated from markdown in `DUX Object Model (Core)/src/dux_v9.6_split_schema/`
- Never edit JSON directly - edit the markdown source
- Run `python scripts/update_schemas.py` after markdown changes

## 🎨 Cursor Rules for Optimal Workflow

```bash
# For research workflows
cp .cursorrules.research .cursorrules

# For development/debugging
cp .cursorrules.development .cursorrules
```

These give you context-aware AI assistance matched to your current task.

## 📊 Understanding Validation Results

After validation, check these files:
- `validation_results/valid_objects.json` - What passed
- `validation_results/invalid_objects.json` - What failed and why
- Individual error logs in `hitl_failed/` - Detailed error messages

## 🌟 The Magic: What This Gives You

1. **No Manual Schema Sync** - Define once in markdown, propagates everywhere
2. **Instant Validation** - Know immediately if your object is valid
3. **Clear Error Messages** - No cryptic failures, just clear guidance
4. **Version Control** - Full git integration for collaboration
5. **Global Scale** - Natural language works across all cultures
6. **AI Agents** - Your definitions become extraction agents automatically

## 🎯 Your Daily Workflow

1. **Morning**: Pull latest changes, check governance status
2. **Create Objects**: Follow template, use clear natural language
3. **Validate Often**: Run validation after each object
4. **Check Errors**: Read error logs, they're your friend
5. **Iterate**: Fix issues, re-validate until green
6. **Celebrate**: Your validated objects are production-ready!

## 🆘 Getting Help

- **Template questions?** → `docs/100_START_HERE/dux_object_template.md`
- **Naming rules?** → `docs/infrastructure_as_code/GOVERNANCE_NAMING_CONVENTIONS.md`
- **Architecture?** → `docs/architecture/dux-system-boundaries.md`
- **Examples?** → Look in `hitl_promotion_candidates/` for validated objects

## 🚀 Remember the Promise

This infrastructure means you spend time on research insights, not debugging schema synchronization. The system catches errors early, provides clear feedback, and ensures your research objects work globally.

**Welcome to weekend-free research!**