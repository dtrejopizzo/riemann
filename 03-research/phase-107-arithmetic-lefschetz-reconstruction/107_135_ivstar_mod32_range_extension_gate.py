#!/usr/bin/env python3
"""Range-extension gate for mod-32 residue separation in the IV* p=2 family."""

from __future__ import annotations

import json
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


def main() -> None:
    rows = run_sage_json()

    results = []
    for mod in (16, 32, 64):
        groups: dict[tuple[int, ...], set[int]] = defaultdict(set)
        for row in rows:
            key = tuple(int(a) % mod for a in row["ainvs"])
            groups[key].add(int(row["cp"]))
        mixed = sum(1 for cps in groups.values() if len(cps) > 1)
        results.append((mod, len(groups), mixed))

    print(f"ROWS: {len(rows)}")
    for mod, groups, mixed in results:
        print(f"mod {mod} groups {groups} mixed {mixed}")

    print()
    mod32 = next(item for item in results if item[0] == 32)
    if mod32[2] == 0:
        print("VERDICT: YES")
        print("Reason: mod-32 residue still has no mixed c_p classes on the scanned IV* family through conductor 2000.")
    else:
        print("VERDICT: NO")
        print("Reason: the extended scanned IV* family contains a mod-32 residue class with mixed c_p values.")


if __name__ == "__main__":
    main()
