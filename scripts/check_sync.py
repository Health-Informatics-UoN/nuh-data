#!/usr/bin/env python3
"""Verify generated Pydantic models are in sync with their LinkML schemas.

Exits 0 if all generated files match, 1 if any are out of sync.
Run 'python scripts/generate.py' to regenerate.
"""
import subprocess
import sys
from pathlib import Path

from generate import GEN_ARGS, SCHEMA_MAP


def check_sync() -> int:
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
            errors.append(f"{schema_path}: generator failed — {result.stderr.strip()}")
            continue

        out = root / output_path
        if not out.exists():
            errors.append(f"{output_path}: file missing — run 'python scripts/generate.py'")
            continue

        if result.stdout != out.read_text():
            errors.append(
                f"{output_path} is out of sync with {schema_path} — "
                f"run 'python scripts/generate.py' to regenerate"
            )

    if errors:
        for e in errors:
            print(f"FAIL: {e}", file=sys.stderr)
        return 1

    print(f"OK: {len(SCHEMA_MAP)} generated file(s) in sync")
    return 0


if __name__ == "__main__":
    sys.exit(check_sync())
