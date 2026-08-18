#!/usr/bin/env python3
"""No-go for mod-8 minimal-model residue as a sole predictor of c_p."""

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

            Emin = ld.minimal_model()
            ainvs = tuple(int(a) for a in Emin.ainvs())
            mod8 = tuple(int(a % 8) for a in ainvs)
            rows.append({
                "label": E.label(),
                "cp": int(ld.tamagawa_number()),
                "mod8": mod8,
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
    groups: dict[tuple[int, ...], list[tuple[str, int]]] = defaultdict(list)
    for row in rows:
        groups[tuple(row["mod8"])].append((row["label"], row["cp"]))

    collisions = []
    for mod8, bucket in sorted(groups.items()):
        cp_set = sorted({cp for _, cp in bucket})
        if len(cp_set) > 1:
            collisions.append((mod8, cp_set, bucket[:10]))

    print(f"count = {len(rows)}")
    print(f"mod8_groups = {len(groups)}")
    print("collisions:")
    for mod8, cp_set, bucket in collisions:
        print(f"  mod8={mod8}, cp_set={cp_set}, sample={bucket}")

    print()
    verdict = len(collisions) == 0
    print(f"VERDICT: {'YES' if verdict else 'NO'}")
    if verdict:
        print("Reason: c_p is constant on every mod-8 residue class in the scanned family.")
    else:
        print("Reason: at least one mod-8 residue class contains curves with different c_p.")


if __name__ == "__main__":
    main()
