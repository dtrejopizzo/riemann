#!/usr/bin/env python3
"""No-go for the current 107.00 finite local source-rule vocabulary."""

from __future__ import annotations

import json
import math
import subprocess
from dataclasses import dataclass
from pathlib import Path


SAGE_BIN = Path("/home/trabajo/miniforge3/bin/sage")


@dataclass(frozen=True)
class Row:
    name: str
    source_packet: tuple[object, ...]
    target: tuple[str, ...]


def run_sage_json() -> list[dict[str, object]]:
    code = r"""
from sage.all import EllipticCurve
import json

rows = []
for label, probe in [('20a1', 2), ('36a4', 2)]:
    E = EllipticCurve(label)
    ld = None
    for item in E.local_data():
        if int(item.prime().gens_reduced()[0]) == probe:
            ld = item
            break
    if ld is None:
        raise RuntimeError(f"missing local data for {label}@{probe}")

    rows.append({
        "name": f"{label}@{probe}",
        "prime": int(probe),
        "a_p": int(E.ap(probe)),
        "cp": int(ld.tamagawa_number()),
        "kodaira": str(ld.kodaira_symbol()),
        "reduction": str(ld.bad_reduction_type()),
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


def source_packet(prime: int, a_p: int, reduction: str) -> tuple[object, ...]:
    local_factor = 1 if reduction == "0" else "nontrivial"
    return (math.log(prime), math.log(prime), prime ** (-0.5), a_p, local_factor)


def build_rows() -> list[Row]:
    rows = []
    for entry in run_sage_json():
        rows.append(
            Row(
                name=entry["name"],
                source_packet=source_packet(entry["prime"], entry["a_p"], entry["reduction"]),
                target=(entry["kodaira"], str(entry["cp"]), entry["reduction"]),
            )
        )
    return rows


def main() -> None:
    rows = build_rows()
    assert len(rows) == 2

    first, second = rows
    same_source = first.source_packet == second.source_packet
    different_target = first.target != second.target

    print("Real forcing pair:")
    for row in rows:
        print(f"  {row.name}: source={row.source_packet}, target={row.target}")

    print()
    if same_source and different_target:
        print("VERDICT: NO")
        print("Reason: the current 107.00 finite local source-rule vocabulary identifies the pair, while the current target distinguishes c_p.")
    else:
        print("VERDICT: YES")
        print("Reason: this pair does not obstruct the current rule-level finite local vocabulary.")


if __name__ == "__main__":
    main()
