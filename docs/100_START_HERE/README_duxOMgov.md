# DUX Object Model

## Data Loader Script Location

The canonical script for loading DUX test data into the Research Platform (e.g., Neo4j) is:

```
/DUX Research Platform/scripts/load_test_data.py
```

- This script is maintained in the DUX Research Platform repository, not in the Object Model repo.
- It is responsible for loading synthetic or sample DUX objects into the platform database for testing, development, or CI/CD.
- If the DUX Object Model schema changes, ensure the loader script is updated accordingly in the Research Platform repo.
- Do **not** run or maintain this script in the Object Model repo; always use the version in the platform repo. 