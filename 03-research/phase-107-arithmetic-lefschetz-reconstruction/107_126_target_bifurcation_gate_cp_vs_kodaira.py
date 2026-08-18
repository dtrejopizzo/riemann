#!/usr/bin/env python3
"""Target bifurcation gate on the real pair 20a1@2 / 36a4@2."""

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
    target_cp: tuple[str, ...]
    target_kod: tuple[str, ...]


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
                target_cp=(entry["kodaira"], str(entry["cp"]), entry["reduction"]),
                target_kod=(entry["kodaira"],),
            )
        )
    return rows


def main() -> None:
    rows = build_rows()
    assert len(rows) == 2

    first, second = rows
    same_source = first.source_packet == second.source_packet
    cp_verdict = not (same_source and first.target_cp != second.target_cp)
    kod_verdict = not (same_source and first.target_kod != second.target_kod)

    print("Real pair:")
    for row in rows:
        print(
            f"  {row.name}: source={row.source_packet}, "
            f"target_cp={row.target_cp}, target_kod={row.target_kod}"
        )

    print()
    print(f"TARGET_WITH_CP: {'YES' if cp_verdict else 'NO'}")
    print(f"TARGET_KODAIRA_ONLY: {'YES' if kod_verdict else 'NO'}")


if __name__ == "__main__":
    main()
