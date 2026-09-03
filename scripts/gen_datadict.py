#!/usr/bin/env python3
"""Generate per-dataset data dictionary CSVs from LinkML schemas, in multiple formats.

Walks the fields on each dataset's tree_root class once, then projects that
into every registered output format. To add a format, add an entry to FORMATS
mapping a name to (fieldnames, row-mapper).

Usage:
    uv run python scripts/gen_datadict.py [output_dir]

Writes <dataset>-<format>.csv for every dataset in SCHEMA_MAP x every format
in FORMATS to output_dir (default: dist/), e.g. sact-datadict.csv,
sact-metadataworks.csv, cosd-datadict.csv, cosd-metadataworks.csv.
"""
import csv
import sys
from pathlib import Path
from typing import Callable

from linkml_runtime.utils.schemaview import SchemaView

from generate import SCHEMA_MAP

Record = dict[str, str]


def cardinality(slot) -> str:
    lower = 1 if slot.required else 0
    upper = "*" if slot.multivalued else 1
    return f"{lower}..{upper}"


def permitted_values(sv: SchemaView, range_name: str) -> str:
    enum = sv.get_enum(range_name, strict=False)
    if enum is None:
        return ""
    parts = []
    for pv_name, pv in enum.permissible_values.items():
        desc = (pv.description or "").strip()
        parts.append(f"{pv_name}: {desc}" if desc else pv_name)
    return " | ".join(parts)


def build_records(schema_path: str, root: Path) -> list[Record]:
    """One record per field on the schema's tree_root class(es), carrying both
    field-level and owning-class-level detail so any output format can project
    the parts it needs."""
    sv = SchemaView(str(root / schema_path))
    tree_roots = [c for c in sv.all_classes().values() if c.tree_root]
    if not tree_roots:
        raise ValueError(f"{schema_path}: no tree_root class found")

    records = []
    for cls in tree_roots:
        class_description = (cls.description or "").strip()
        for slot_name in sv.class_slots(cls.name):
            slot = sv.induced_slot(slot_name, cls.name)
            records.append(
                {
                    "class_name": cls.name,
                    "class_description": class_description,
                    "field": slot.name,
                    "type": slot.range,
                    "cardinality": cardinality(slot),
                    "description": (slot.description or "").strip(),
                    "permitted_values": permitted_values(sv, slot.range),
                }
            )
    return records


# Each format is (fieldnames in output order, mapper from a build_records() record to a CSV row).
FORMATS: dict[str, tuple[list[str], Callable[[Record], Record]]] = {
    "datadict": (
        ["field", "type", "cardinality", "description", "permitted_values"],
        lambda r: {
            "field": r["field"],
            "type": r["type"],
            "cardinality": r["cardinality"],
            "description": r["description"],
            "permitted_values": r["permitted_values"],
        },
    ),
    # MetadataWorks import format: table name/description repeated on every row.
    "metadataworks": (
        ["Table Name", "Table Description", "Column Name", "Column Description", "Data Type"],
        lambda r: {
            "Table Name": r["class_name"],
            "Table Description": r["class_description"],
            "Column Name": r["field"],
            "Column Description": r["description"],
            "Data Type": r["type"],
        },
    ),
}


def generate(out_dir: Path) -> int:
    root = Path(__file__).parent.parent
    out_dir.mkdir(parents=True, exist_ok=True)

    for schema_path in SCHEMA_MAP:
        dataset_name = Path(schema_path).stem
        records = build_records(schema_path, root)

        for format_name, (fieldnames, row_mapper) in FORMATS.items():
            out_path = out_dir / f"{dataset_name}-{format_name}.csv"
            with out_path.open("w", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(row_mapper(r) for r in records)
            print(f"  wrote {out_path} ({len(records)} rows)")

    return 0


if __name__ == "__main__":
    out_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).parent.parent / "dist"
    sys.exit(generate(out_dir))
