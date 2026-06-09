#!/usr/bin/env python3
"""Regenerate all Pydantic models from LinkML schemas.

Usage:
    uv run python scripts/generate.py
"""
import subprocess
import sys
from pathlib import Path

# Map from schema YAML → generated Python output
SCHEMA_MAP: dict[str, str] = {
    "schemas/datasets/sact/sact.yaml": "src/nuh_data/datasets/sact/model.py",
    "schemas/datasets/cosd/cosd.yaml": "src/nuh_data/datasets/cosd/model.py",
}

GEN_ARGS = ["gen-pydantic"]


def generate() -> int:
    root = Path(__file__).parent.parent
    errors: list[str] = []

    for schema_path, output_path in SCHEMA_MAP.items():
        result = subprocess.run(
            GEN_ARGS + [schema_path],
            capture_output=True,
            text=True,
            cwd=root,
        )
        if result.returncode != 0:
            errors.append(f"{schema_path}: {result.stderr.strip()}")
            continue

        out = root / output_path
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(result.stdout)
        print(f"  generated {output_path}")

    if errors:
        for e in errors:
            print(f"ERROR: {e}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(generate())
