#!/usr/bin/env python3
"""Threshold gate for residue-depth separation in the IV* p=2 family."""

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
for N in range(11, 501):
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

            ainvs = tuple(int(a) for a in ld.minimal_model().ainvs())
            rows.append({
                "label": E.label(),
                "cp": int(ld.tamagawa_number()),
                "ainvs": ainvs,
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


def main() -> None:
    rows = run_sage_json()
    first_clean_modulus = None

    for m in range(1, 9):
        mod = 2**m
        groups: dict[tuple[int, ...], set[int]] = defaultdict(set)
        for row in rows:
            key = tuple(int(a % mod) for a in row["ainvs"])
            groups[key].add(int(row["cp"]))
        mixed_groups = sum(1 for cps in groups.values() if len(cps) > 1)
        print(f"mod {mod:<3} groups {len(groups):<3} mixed_groups {mixed_groups}")
        if first_clean_modulus is None and mixed_groups == 0:
            first_clean_modulus = mod

    print()
    if first_clean_modulus is not None:
        print("VERDICT: YES")
        print(f"Reason: the first tested residue modulus with no mixed c_p classes is {first_clean_modulus}.")
    else:
        print("VERDICT: NO")
        print("Reason: mixed c_p classes persist through every tested residue modulus.")


if __name__ == "__main__":
    main()
