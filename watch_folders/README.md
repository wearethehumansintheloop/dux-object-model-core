# 🤝 Human-in-the-Loop (HITL) Watch Folders

This system enables collaborative workflows between humans and AI for the DUX Object Model project.

## 📁 Folder Structure

```
watch_folders/
├── hitl_review/      → Drop files here for AI analysis & review prompts
├── hitl_feedback/    → Drop completed human responses here  
├── hitl_processed/   → Archive of processed files
└── README.md         → This file
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

## 🔄 Workflow Example

1. **You:** Drop `new_schema.json` in `hitl_review/`
2. **AI:** Creates analysis and review prompt in `hitl_sessions/review_[timestamp]_new_schema/`
3. **You:** Review AI analysis, fill out `human_response_template.md`
4. **You:** Drop completed response in `hitl_feedback/`
5. **AI:** Processes feedback and creates next steps in `hitl_sessions/feedback_[timestamp]/`

## 📋 Use Cases

### Schema Updates
- Drop new/modified schema files for validation
- AI checks DUX v9.5 compliance and suggests improvements

### Test Data Creation  
- Drop test data for validation
- AI validates structure and evidence requirements

### Documentation Review
- Drop documentation for alignment checking
- AI compares against object model guide

### Prompt Template Work
- Drop prompt templates for review
- AI checks against current schemas

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
