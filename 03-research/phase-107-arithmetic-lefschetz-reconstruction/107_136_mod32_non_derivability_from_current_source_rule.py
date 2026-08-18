#!/usr/bin/env python3
"""No-go for deriving the mod-32 channel from the current 107.00 source rule."""

from __future__ import annotations

import json
import math
import subprocess
from collections import defaultdict
from pathlib import Path


SAGE_BIN = Path("/home/trabajo/miniforge3/bin/sage")


def run_sage_json() -> list[dict[str, object]]:
    code = r"""
from sage.all import cremona_curves
import json

rows = []
for N in range(11, 2001):
    try:
        curves = cremona_curves([N])
    except Exception:
        continue
    for E in curves:
        for ld in E.local_data():
            p = int(ld.prime().gens_reduced()[0])
            if p != 2:
                continue
            if str(ld.kodaira_symbol()) != 'IV*' or str(ld.bad_reduction_type()) != '0':
                continue

            vals = []
            ok = True
            for obj in [E.c4(), E.c6(), E.discriminant(), E.j_invariant()]:
                v = obj.valuation(2)
                if str(v) == '+Infinity':
                    ok = False
                    break
                vals.append(int(v))
            if not ok:
                continue
            v4, v6, vd, vj = vals
            if (v4, v6, vd, vj, int(ld.conductor_valuation()), int(E.ap(2))) != (4, 6, 8, 4, 2, 0):
                continue

            rows.append({
                "label": E.label(),
                "cp": int(ld.tamagawa_number()),
                "ainvs": tuple(int(a) for a in ld.minimal_model().ainvs()),
            })

print(json.dumps(rows, default=int))
"""
    result = subprocess.run(
        [str(SAGE_BIN), "-c", code],
        check=True,
        capture_output=True,
        text=True,
    )
    return json.loads(result.stdout)


def current_source_rule_packet() -> tuple[object, ...]:
    prime = 2
    return (math.log(prime), math.log(prime), prime ** (-0.5), 0, 1)


def main() -> None:
    rows = run_sage_json()
    packet = current_source_rule_packet()

    mod32_groups: dict[tuple[int, ...], set[int]] = defaultdict(set)
    for row in rows:
        key = tuple(int(a) % 32 for a in row["ainvs"])
        mod32_groups[key].add(int(row["cp"]))

    mixed_mod32 = sum(1 for cps in mod32_groups.values() if len(cps) > 1)

    print(f"ROWS: {len(rows)}")
    print(f"CURRENT_SOURCE_RULE_PACKET: {packet}")
    print(f"MOD32_CLASSES: {len(mod32_groups)}")
    print(f"MIXED_MOD32_CLASSES: {mixed_mod32}")

    sample = sorted((key, sorted(cps)) for key, cps in mod32_groups.items())[:5]
    for key, cps in sample:
        print(f"  mod32={key} -> cp_set={cps}")

    print()
    if len(mod32_groups) > 1 and mixed_mod32 == 0:
        print("VERDICT: NO")
        print("Reason: the current 107.00 finite source-rule packet is constant on the scanned IV* family, while the mod-32 channel is nonconstant and separates c_p.")
    else:
        print("VERDICT: YES")
        print("Reason: the scanned IV* family does not witness non-derivability of the mod-32 channel from the current source rule.")


if __name__ == "__main__":
    main()
