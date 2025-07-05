# 🤝 Human-in-the-Loop (HITL) Watch Folders

This system enables collaborative workflows between humans and AI for the DUX Object Model project.

## 📁 Folder Structure

```
watch_folders/
├── hitl_review/                    → Drop files here for architectural review
├── hitl_workshop/                  → Workshop objects with LLM for improvements
├── hitl_failed/                    → Objects that failed validation
├── hitl_approved_for_production/   → Objects ready for production deployment
└── README.md                       → This file
```

## 🚀 Quick Start

1. **Start the HITL watcher:**
   ```bash
   python scripts/hitl_watcher.py --start
   ```

2. **Drop a file** in `hitl_review/` to trigger AI analysis

3. **Review the AI analysis** in the generated session folder

4. **Fill out the human response** template

5. **Drop your response** in `hitl_feedback/` for AI processing

## 🔄 IaC Workflow Example

1. **You:** Drop `new_schema.json` in `hitl_review/`
2. **System:** Performs architectural review against governance standards (no AI)
3. **If failed:** Object moves to `hitl_failed/` with error details
4. **If needs work:** Move to `hitl_workshop/` for LLM collaboration
5. **If approved:** Object moves to `hitl_approved_for_production/`
6. **Production:** Object is deployed to live DUX object model

## 📋 Use Cases

### Architectural Review
- Drop new objects in `hitl_review/` for architectural review
- System reviews against DUX v9.6 schemas and naming conventions (no AI)

### LLM Workshop
- Move objects to `hitl_workshop/` for collaborative improvement
- Work with LLM to refine object structure and content

### Production Deployment
- Approved objects in `hitl_approved_for_production/` are ready for live use
- Objects become part of canonical DUX object model

### Quality Control
- Failed objects in `hitl_failed/` show architectural review errors
- Review and fix before resubmitting to review

## 🎯 Benefits vs Blind Automation

- **Human oversight** on all changes
- **Collaborative decision-making** 
- **Context-aware** analysis
- **Quality control** before implementation
- **Learning feedback loops** between human and AI

## 📝 Session Artifacts

Each HITL cycle creates timestamped session folders with:
- Original file
- AI analysis and review prompt  
- Human response template
- AI next steps and recommendations
- Implementation guidance

## 🔧 Commands

```bash
# Start HITL watcher
python scripts/hitl_watcher.py --start

# View recent sessions
ls -la hitl_sessions/

# Clean up old processed files
find watch_folders/hitl_processed/ -mtime +30 -delete
```

---

**Ready to collaborate?** Start the watcher and drop your first file! 🚀
