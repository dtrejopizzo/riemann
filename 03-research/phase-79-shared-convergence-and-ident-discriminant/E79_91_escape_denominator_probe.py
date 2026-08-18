#!/usr/bin/env python3
"""E79.91 - denominator audit for CLOSE => STRONG_ESCAPE.

Audits whether the large escape ratio is driven primarily by small |c| rather
than by a large numerator q^T x. Restricted to the main audited builds
(zeta + planted gamma1) for a lightweight, reproducible check.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
PHASE76 = HERE.parent / "phase-76-normalized-adjugate-arithmetic-lock"
PHASE77 = HERE.parent / "phase-77-weyl-limit-point"
PHASE78 = HERE.parent / "phase-78-build-neutral-lp-and-ident"
for path in (PHASE76, PHASE77, PHASE78):
    sys.path.insert(0, str(path))

from P76_002_mp_entry_audit import build_mp  # noqa: E402
from E78_9_w_quotient_delta_probe import section  # noqa: E402
from E77_3c_two_generator_ident_probe import GAMMA, right_transfer_data  # noqa: E402


def serial(x: mp.mpf, digits: int = 18) -> str:
    return mp.nstr(x, digits)


def row_metrics(H, idx, L):
    _mu, _A, db_idx, inner, x = right_transfer_data(H, idx)
    d = [2 * mp.pi * n / L for n in inner]
    db = 2 * mp.pi * db_idx / L
    xv = [x[j] for j in range(x.rows)]
    q = [dj - db for dj in d]
    c = 1 - mp.fsum(xv)
    qTx = mp.fsum(q[j] * xv[j] for j in range(len(q)))
    mesh = max(abs(v) for v in d)
    escape_ratio = abs(qTx) / (abs(c) * mesh)
    return {
        "abs_c": abs(c),
        "abs_qTx": abs(qTx),
        "mesh_radius": mesh,
        "numerator_mesh_ratio": abs(qTx) / mesh,
        "numerator_mesh2_ratio": abs(qTx) / (mesh**2),
        "escape_ratio": escape_ratio,
    }


def run_case(label, planted, max_n=18, dps=60):
    mp.mp.dps = dps
    Hmax, idxmax, L = build_mp(6, max_n, dps, planted=planted)
    rows = []
    for N in range(8, max_n + 1, 2):
        H, idx = section(Hmax, idxmax, max_n, N)
        m = row_metrics(H, idx, L)
        rows.append(
            {
                "N": N,
                "abs_c": serial(m["abs_c"]),
                "abs_qTx": serial(m["abs_qTx"]),
                "mesh_radius": serial(m["mesh_radius"]),
                "numerator_mesh_ratio": serial(m["numerator_mesh_ratio"]),
                "numerator_mesh2_ratio": serial(m["numerator_mesh2_ratio"]),
                "escape_ratio": serial(m["escape_ratio"]),
            }
        )
    return {
        "label": label,
        "planted": None
        if planted is None
        else {"gamma": planted[0], "beta": planted[1], "strength": planted[2]},
        "rows": rows,
    }


def main():
    out = {
        "statement": "E79.91 denominator audit for CLOSE => STRONG_ESCAPE",
        "parameters": {"lambda": 6, "max_n": 18, "dps": 60},
        "cases": [],
    }
    cases = [
        ("zeta", None),
        ("plant_gamma1_beta030", (GAMMA, "0.30", "5.0")),
    ]
    for label, planted in cases:
        case = run_case(label, planted)
        out["cases"].append(case)
        print(label, "done", flush=True)
    out_path = HERE / "E79_91_escape_denominator_results.json"
    out_path.write_text(json.dumps(out, indent=2) + "\n", encoding="ascii")
    print(f"WROTE {out_path.name}")


if __name__ == "__main__":
    main()
