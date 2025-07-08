# DUX v9.5 Schema Directory Structure

## 📁 Directory Overview

### `src/dux_v9.5_split_schema/` - **SOURCE SCHEMAS** ⭐
**This is the authoritative source of truth for all DUX v9.5 schemas.**

- Edit these files to modify the schema
- These are the schemas that define the DUX object model
- All changes should be made here first

### `src/schema/generated_from_main_schemas/` - **GENERATED OUTPUT** 🔄
**This directory contains COPIES of the main schemas for tool processing.**

- **DO NOT EDIT** files in this directory directly
- Files here are automatically generated/copied from the main schemas
- Used by scripts like `update_prompts_with_schema.py` for prompt generation
- This directory may be empty if generation scripts haven't been run recently

### `src/archive/dux_v9.4_split_schema/` - **HISTORICAL ARCHIVE** 📚
**Previous version schemas kept for reference.**

- Contains v9.4 schemas for migration reference
- Read-only historical reference
- Do not modify these files

## 🔄 How the Generation Works

1. **Source schemas** are maintained in `src/dux_v9.5_split_schema/`
2. **Tools and scripts** copy schemas to `src/schema/generated_from_main_schemas/`
3. **Prompt generation** and other automation reads from the generated directory
4. **This separation** allows tools to have stable references while schemas evolve

## 🚨 If You Don't See Files in `generated_from_main_schemas/`

**Don't panic!** The schemas haven't been deleted. You just need to run the generation script:

```bash
python scripts/update_prompts_with_schema.py
```

This will copy the current schemas from the main directory and generate updated prompts.

## 📝 Making Schema Changes

1. **Edit** files in `src/dux_v9.5_split_schema/`
2. **Run** `python scripts/update_prompts_with_schema.py` to update tools
3. **Test** your changes with the updated prompts
4. **Commit** both the schema changes and generated outputs

---

**Remember**: Always edit the source schemas, never the generated copies!
