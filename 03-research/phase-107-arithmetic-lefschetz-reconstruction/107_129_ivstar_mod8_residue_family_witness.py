#!/usr/bin/env python3
"""Family witness for mod-8 local minimal-model residues in the IV* p=2 family."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path


SAGE_BIN = Path("/home/trabajo/miniforge3/bin/sage")


def run_sage_json() -> dict[str, object]:
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
                "ainvs": ainvs,
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
    rows = json.loads(result.stdout)
    cp_set = sorted({row["cp"] for row in rows})
    mod8_classes = sorted({tuple(row["mod8"]) for row in rows})
    return {
        "count": len(rows),
        "rows": rows,
        "cp_set": cp_set,
        "mod8_classes": mod8_classes,
    }


def main() -> None:
    payload = run_sage_json()

    print(f"count = {payload['count']}")
    print(f"cp_set = {payload['cp_set']}")
    print(f"mod8_classes = {payload['mod8_classes']}")
    print("sample_rows:")
    for row in payload["rows"][:12]:
        print(f"  {row['label']}: cp={row['cp']}, mod8={tuple(row['mod8'])}, ainvs={tuple(row['ainvs'])}")

    print()
    verdict = payload["count"] > 1 and len(payload["cp_set"]) > 1 and len(payload["mod8_classes"]) > 1
    print(f"VERDICT: {'YES' if verdict else 'NO'}")
    if verdict:
        print("Reason: the mod-8 minimal-model residue channel persists across a real family sharing one coarse IV* local packet.")
    else:
        print("Reason: no nontrivial family-level residue pattern was detected in the scanned range.")


if __name__ == "__main__":
    main()
