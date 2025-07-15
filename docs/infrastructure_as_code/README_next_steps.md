# 🔄 Declarative UX CI/CD - Next Steps

This bundle contains the foundational BDD test suite for the Declarative UX experience pipeline, specifically focusing on Chunkee's ingestion and taxonomy translation roles.

## 📦 Included Files

- `experience_pipeline_cicd.feature`: BDD test cases modeling the Chunkee pipeline
- `experience_pipeline_steps.py`: Step definitions to validate Chunkee’s processing
- `README_next_steps.md`: This file

## ✅ Current Status

- Dual-schema pipeline logic defined (DUX + ORCA)
- GRAPHRAG seeding logic articulated
- Validation-ready for `.md` inputs

## 🔜 Recommended Next Steps

1. **Run validation**: Use `.feature` and `.steps.py` to dry run a known `.md` input.
2. **Ingest test data**: Create synthetic `.md` docs to test Chunkee’s output path.
3. **Scaffold ingestion agent**: Begin scripting `chunkee-to-graphrag-ingestion.py`.
4. **Initialize GRAPHRAG schema**: Define Neo4j node/relationship structure.
5. **Evaluate model integration**: Choose LLMs (e.g. LLaMA 3B, Mistral) to assist Chunkee with schema tagging.

---

🧠 _Remember_: Chunkee is the semantic librarian. DUX validates structural alignment. ORCA surfaces domain-specific ontologies.

