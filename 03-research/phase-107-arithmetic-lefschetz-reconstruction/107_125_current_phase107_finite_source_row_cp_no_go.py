#!/usr/bin/env python3
"""No-go for the current Phase 107 finite source row against c_p.

The current finite source row exposed by 107_03--107_04 at the first
connected return level is

    (Z_{p,1}, (1,p), p^(-1/2), log p)

This verifier checks that on the real forcing pair 20a1@2 and 36a4@2,
that packet agrees while the current target state differs via c_p.
"""

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
        "kodaira": str(ld.kodaira_symbol()),
        "cp": int(ld.tamagawa_number()),
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


def source_packet(prime: int) -> tuple[object, ...]:
    return (f"Z_{{{prime},1}}", (1, prime), prime ** (-0.5), math.log(prime))


def build_rows() -> list[Row]:
    rows = []
    for entry in run_sage_json():
        rows.append(
            Row(
                name=entry["name"],
                source_packet=source_packet(entry["prime"]),
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
        print("Reason: the current Phase 107 finite source row identifies the pair, while the current target distinguishes c_p.")
    else:
        print("VERDICT: YES")
        print("Reason: this pair does not obstruct the current finite source row.")


if __name__ == "__main__":
    main()
