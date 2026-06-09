"""Regenerate Pydantic models from LinkML schemas.

Run with: uv run python scripts/generate.py
Requires: uv sync --group dev
"""

import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

SCHEMAS = [
    (
        ROOT / "schemas/datasets/sact/sact.yaml",
        ROOT / "src/nuh_data/datasets/sact/model.py",
    ),
]


def main() -> None:
    for schema, output in SCHEMAS:
        result = subprocess.run(
            ["gen-pydantic", str(schema)],
            capture_output=True,
            text=True,
            check=True,
        )
        output.write_text(result.stdout)
        print(f"Generated {output.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
