#!/usr/bin/env python3
"""Witness that local minimal-model residue data separates the forcing pair."""

from __future__ import annotations

import json
import subprocess
from dataclasses import dataclass
from pathlib import Path


SAGE_BIN = Path("/home/trabajo/miniforge3/bin/sage")


@dataclass(frozen=True)
class Row:
    name: str
    ainvs: tuple[int, int, int, int, int]
    mod8: tuple[int, int, int, int, int]
    target: tuple[str, ...]


def run_sage_json() -> list[dict[str, object]]:
    code = r"""
from sage.all import EllipticCurve
import json

rows = []
for label, probe in [('20a1', 2), ('36a4', 2)]:
    E = EllipticCurve(label)
    ld = E.local_data(probe)
    Emin = ld.minimal_model()
    ainvs = tuple(int(a) for a in Emin.ainvs())
    rows.append({
        "name": f"{label}@{probe}",
        "ainvs": ainvs,
        "mod8": tuple(int(a % 8) for a in ainvs),
        "target": (
            str(ld.kodaira_symbol()),
            str(int(ld.tamagawa_number())),
            str(ld.bad_reduction_type()),
        ),
    })

print(json.dumps(rows))
"""
    result = subprocess.run(
        [str(SAGE_BIN), "-c", code],
        check=True,
        capture_output=True,
        text=True,
    )
    return json.loads(result.stdout)


def build_rows() -> list[Row]:
    rows = []
    for entry in run_sage_json():
        rows.append(
            Row(
                name=entry["name"],
                ainvs=tuple(entry["ainvs"]),
                mod8=tuple(entry["mod8"]),
                target=tuple(entry["target"]),
            )
        )
    return rows


def main() -> None:
    rows = build_rows()
    assert len(rows) == 2

    first, second = rows
    separated = first.mod8 != second.mod8

    print("Real forcing pair:")
    for row in rows:
        print(f"  {row.name}: ainvs={row.ainvs}, mod8={row.mod8}, target={row.target}")

    print()
    print(f"VERDICT: {'YES' if separated else 'NO'}")
    if separated:
        print("Reason: the local minimal-model residue channel separates the pair.")
    else:
        print("Reason: the local minimal-model residue channel does not separate the pair.")


if __name__ == "__main__":
    main()
