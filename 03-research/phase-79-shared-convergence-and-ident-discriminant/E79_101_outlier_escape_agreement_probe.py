#!/usr/bin/env python3
"""E79.101 - extend the outlier/escape agreement audit to N=18.

This probe recomputes only the quantities needed to compare:

    outlier_abs / escape_scale

on the same three builds used across the E79.8x-E79.10x ladder.
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

GAMMA2 = "21.022039638771554992"


def serial(x: mp.mpf, digits: int = 18) -> str:
    return mp.nstr(x, digits)


def row_metrics(H, idx, L):
    _mu, _A, db_idx, inner, x = right_transfer_data(H, idx)
    d = [2 * mp.pi * n / L for n in inner]
    db = 2 * mp.pi * db_idx / L
    xv = [x[j] for j in range(x.rows)]
    q = [dj - db for dj in d]
    c = 1 - mp.fsum(xv)
    qtx = mp.fsum(q[j] * xv[j] for j in range(len(q)))

    n = len(d)
    K = mp.matrix(n, n)
    for a in range(n):
        for b in range(n):
            K[a, b] = (d[a] if a == b else mp.mpf("0")) + x[a] * q[b] / c
    eigvals, _ = mp.eig(K)
    kappas = sorted([mp.re(ev) for ev in eigvals], key=lambda t: abs(t), reverse=True)
    outlier_abs = abs(kappas[0])
    second_abs = abs(kappas[1])
    escape_scale = abs(qtx / c)
    mesh_radius = max(abs(dj) for dj in d)
    return {
        "outlier_abs": outlier_abs,
        "second_abs": second_abs,
        "escape_scale": escape_scale,
        "mesh_radius": mesh_radius,
        "outlier_over_escape": outlier_abs / escape_scale,
        "spectral_reading": mp.sqrt(outlier_abs * second_abs) / mesh_radius,
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
                "outlier_abs": serial(m["outlier_abs"]),
                "second_abs": serial(m["second_abs"]),
                "escape_scale": serial(m["escape_scale"]),
                "mesh_radius": serial(m["mesh_radius"]),
                "outlier_over_escape": serial(m["outlier_over_escape"]),
                "spectral_reading": serial(m["spectral_reading"]),
            }
        )
    vals = [mp.mpf(r["outlier_over_escape"]) for r in rows]
    mean_val = mp.fsum(vals) / len(vals)
    spread = (max(vals) - min(vals)) / mean_val if mean_val else mp.mpf("0")
    return {
        "label": label,
        "planted": None
        if planted is None
        else {"gamma": planted[0], "beta": planted[1], "strength": planted[2]},
        "rows": rows,
        "summary": {
            "min_outlier_over_escape": serial(min(vals)),
            "max_outlier_over_escape": serial(max(vals)),
            "mean_outlier_over_escape": serial(mean_val),
            "relative_spread": serial(spread),
        },
    }


def main():
    out = {
        "statement": "E79.101 extended outlier/escape agreement audit",
        "parameters": {"lambda": 6, "max_n": 18, "dps": 60},
        "cases": [],
    }
    cases = [
        ("zeta", None),
        ("plant_gamma1_beta030", (GAMMA, "0.30", "5.0")),
        ("plant_gamma2_beta030", (GAMMA2, "0.30", "5.0")),
    ]
    for label, planted in cases:
        case = run_case(label, planted)
        out["cases"].append(case)
        s = case["summary"]
        print(
            f"{label:20s} out/esc="
            f"{s['min_outlier_over_escape']}..{s['max_outlier_over_escape']} "
            f"spread={s['relative_spread']}",
            flush=True,
        )
    out_path = HERE / "E79_101_outlier_escape_agreement_results.json"
    out_path.write_text(json.dumps(out, indent=2) + "\n", encoding="ascii")
    print(f"WROTE {out_path.name}")


if __name__ == "__main__":
    main()
