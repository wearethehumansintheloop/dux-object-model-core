# 🔒 Canonical Object Vault

## ⚠️ SACRED DIRECTORY - HANDLE WITH EXTREME CARE ⚠️

This is the **canonical vault** containing the authoritative object definitions for the DUX Object Model. These definitions are the source of truth for all generation, validation, and extraction activities.

## 🛡️ Protection Rules

1. **NO DIRECT MODIFICATIONS** - Only the HITL pipeline can update these files
2. **MANDATORY BACKUPS** - Every update triggers automatic backup to `_backups/`
3. **AUDIT TRAIL** - All changes logged with timestamp and source
4. **VERSION CONTROL** - Git tracks all changes with meaningful commits
5. **ACCESS CONTROL** - Only approved automation can write here

## 📁 Structure

```
canonical_vault/
├── problem/              # Canonical Problem object definition
├── behavior/             # Canonical Behavior object definition  
├── result/               # Canonical Result object definition
├── useroutcome/          # Canonical UserOutcome object definition
├── flow/                 # Canonical Flow object definition
├── provenance/           # Canonical Provenance object definition
├── insight/              # Canonical Insight object definition
└── _backups/             # Timestamped backups before updates
    ├── problem/
    ├── behavior/
    └── ...
```

## 🔄 Update Workflow

```
HITL Approval → Backup Current → Validate New → Update Canonical → Trigger Generation
```

## 📋 Each Canonical Definition Contains

Following the DUX Object Template:
- 🎯 Purpose & Strategic Role
- 🧠 "What would you say... you do here?"
- 💡 Why the Object Matters
- 📋 Schema Attributes (Source of Truth)
- 📦 Canonical Example
- 🔗 Structural Role & Usage Notes

## 🚨 Emergency Procedures

### Rollback Process
```bash
# List available backups
ls canonical_vault/_backups/problem/

# Restore from backup
cp canonical_vault/_backups/problem/20250108_100000_problem_object.md canonical_vault/problem/problem_object.md
```

### Validation Before Update
```bash
# Run HITL validation
python scripts/validation/hitl_pipeline/hitl_orchestrator.py <candidate_file>

# Only if all stages pass, proceed with update
```

## 🔐 Security Notes

- This directory should be read-only in production
- Write access only through automated pipelines
- Consider filesystem-level protections
- Monitor all access attempts

## 📊 Current Canonical Versions

| Object Type | Version | Last Updated | Update Count |
|-------------|---------|--------------|--------------|
| Problem     | -       | -            | 0            |
| Behavior    | -       | -            | 0            |
| Result      | -       | -            | 0            |
| UserOutcome | -       | -            | 0            |
| Flow        | -       | -            | 0            |
| Provenance  | -       | -            | 0            |
| Insight     | -       | -            | 0            |

---

**Remember**: The canonical vault is sacred. Treat it with the respect it deserves.