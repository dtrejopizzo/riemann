#!/usr/bin/env python3
"""Current target non-Eulerian source necessity gate.

This verifier computes the decisive additive pair 20a1@2 and 36a4@2 and
checks that:

1. their standard additive Euler/valuative packets agree exactly;
2. their current target states differ because c_p differs.

Hence any future faithful source upgrade for the current target must add
information beyond that Euler/valuative channel.
"""

from __future__ import annotations

import json
import subprocess
from dataclasses import dataclass
from pathlib import Path


SAGE_BIN = Path("/home/trabajo/miniforge3/bin/sage")


@dataclass(frozen=True)
class Row:
    name: str
    packet: tuple[object, ...]
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
        "v_c4": int(E.c4().valuation(probe)),
        "v_c6": int(E.c6().valuation(probe)),
        "v_disc": int(E.discriminant().valuation(probe)),
        "v_j": int(E.j_invariant().valuation(probe)),
        "kodaira": str(ld.kodaira_symbol()),
        "f_p": int(ld.conductor_valuation()),
        "a_p": int(E.ap(probe)),
        "cp": int(ld.tamagawa_number()),
        "reduction": str(ld.bad_reduction_type()),
        "is_additive": bool(str(ld.bad_reduction_type()) == '0'),
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
    out = []
    for entry in run_sage_json():
        local_factor = "1" if entry["is_additive"] else "nontrivial"
        packet = (
            entry["prime"],
            entry["v_c4"],
            entry["v_c6"],
            entry["v_disc"],
            entry["v_j"],
            entry["kodaira"],
            entry["f_p"],
            entry["a_p"],
            local_factor,
        )
        target = (
            entry["kodaira"],
            str(entry["cp"]),
            entry["reduction"],
        )
        out.append(Row(name=entry["name"], packet=packet, target=target))
    return out


def main() -> None:
    rows = build_rows()
    assert len(rows) == 2

    first, second = rows
    same_packet = first.packet == second.packet
    different_target = first.target != second.target

    print("Real forcing pair:")
    for row in rows:
        print(f"  {row.name}: packet={row.packet}, target={row.target}")

    print()
    if same_packet and different_target:
        print("VERDICT: NO")
        print("Reason: the current target distinguishes c_p while the standard additive Euler/valuative source channel does not.")
    else:
        print("VERDICT: YES")
        print("Reason: this pair does not force a new source channel.")


if __name__ == "__main__":
    main()
