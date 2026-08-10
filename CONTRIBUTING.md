# Contributing

## Prerequisites

- [uv](https://docs.astral.sh/uv/) for dependency management

Install dev dependencies:

```bash
uv sync --group dev
```

---

## Schemas

Schemas live under `schemas/datasets/<name>/` as LinkML YAML files.

The Pydantic model at `src/nuh_data/datasets/<name>/model.py` is **generated** from the YAML — never edit it by hand.

### Regenerating after a schema change

```bash
uv run scripts/generate.py
```

Commit both the YAML and the regenerated `model.py` together. CI will fail if they are out of sync.

### Checking sync without regenerating

```bash
cd scripts && uv run check_sync.py
```

### Linting schemas

```bash
uv run linkml lint --ignore-warnings schemas/
```

Warnings about empty `description` fields are expected — per-field documentation is added incrementally. CI uses `--ignore-warnings` so these do not block merges.

> **Note:** You may also see a warning that prefix `ICD` should be `ICF`. This is a false positive in the linter — ICD (International Classification of Diseases) and ICF (International Classification of Functioning) are different standards. Ignore it.

---

## Adding a new dataset

1. Create `schemas/datasets/<name>/` and add `<name>.yaml` (copy the SACT schema as a template).
    - don't use `<name>` for the class name in `classes:` (it will lead to missing `.md` files)
2. Add an entry to `SCHEMA_MAP` in `scripts/generate.py`:
    ```python
   "schemas/datasets/<name>/<name>.yaml": "src/nuh_data/datasets/<name>/model.py",
    ```
3. Create `src/nuh_data/datasets/<name>/__init__.py`:
    ```python
    from .model import *
    ```
4. Add `uv run gen-doc -d docs/datasets/<name> schemas/datasets/<name>/<name>.yaml` to `.github/workflows/publish.docs.yml`
5. Generate and check/test the site locally
    - for each schema, run `uv run gen-doc -d docs/datasets/<name> schemas/datasets/<name>/<name>.yaml`
    - then run `uv run mkdocs serve` to run a local copy of the site
6. Run `uv run python scripts/generate.py` and commit everything together.

---

## CI

Two required checks run on every PR:

| Check       | Command                                  | Fails on                     |
| ----------- | ---------------------------------------- | ---------------------------- |
| Schema lint | `linkml lint --ignore-warnings schemas/` | Schema errors (not warnings) |
| Sync check  | `python scripts/check_sync.py`           | Generated model out of date  |

If the sync check fails, run `uv run python scripts/generate.py` and push the updated `model.py`.

---

## Generated file behaviour in GitHub

`model.py` files are marked as `linguist-generated` in `.gitattributes`, so GitHub collapses them in PR diffs automatically. Reviewers should focus on the YAML schema — the generated Python is a mechanical consequence of it.
