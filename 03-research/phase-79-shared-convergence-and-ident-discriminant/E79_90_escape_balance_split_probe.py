#!/usr/bin/env python3
"""E79.90 - split audit for CLOSE+BAL => GEOM.

Tests two finite submechanisms:

  CLOSE  -> strong rank-one escape scale
  BAL    -> low internal pair defect

and compares them against the audited geometry regime.
"""

from __future__ import annotations

import json
import math
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


def serial(x: mp.mpf | float, digits: int = 18) -> str:
    return mp.nstr(x, digits)


def finite_log_ratio(num: mp.mpf, den: mp.mpf) -> float:
    if num <= 0 and den <= 0:
        return 0.0
    if num <= 0 or den <= 0:
        return math.inf
    return abs(math.log(float(num / den)))


def row_metrics(H, idx, L):
    _mu, _A, db_idx, inner, x = right_transfer_data(H, idx)
    d = [2 * mp.pi * n / L for n in inner]
    db = 2 * mp.pi * db_idx / L
    xv = [x[j] for j in range(x.rows)]
    q = [dj - db for dj in d]
    r = [qj * xj for qj, xj in zip(q, xv)]
    c = 1 - mp.fsum(xv)
    qTx = mp.fsum(q[j] * xv[j] for j in range(len(q)))

    pos_abs = mp.fsum(abs(v) for v in r if v > 0)
    neg_abs = mp.fsum(abs(v) for v in r if v < 0)
    total_abs = pos_abs + neg_abs
    r_net = abs(mp.fsum(r)) / total_abs if total_abs else mp.mpf("0")
    bal_log = finite_log_ratio(pos_abs, neg_abs)

    n = len(d)
    K = mp.matrix(n, n)
    for a in range(n):
        for b in range(n):
            K[a, b] = (d[a] if a == b else mp.mpf("0")) + x[a] * q[b] / c
    eigvals, _ = mp.eig(K)
    kappas = sorted([mp.re(ev) for ev in eigvals], key=lambda t: abs(t), reverse=True)
    outlier_fraction = abs(kappas[0]) / abs(kappas[1])
    cloud = kappas[1:]
    pos = sorted([v for v in cloud if v > 0], key=abs)
    neg = sorted([-v for v in cloud if v < 0], key=abs)
    defects = [abs(p - n0) / (p + n0) for p, n0 in zip(pos, neg)]
    mean_pair_defect = mp.fsum(defects) / len(defects)
    d_n = mean_pair_defect / outlier_fraction

    escape_scale = abs(qTx / c)
    mesh_radius = max(abs(dj) for dj in d)
    escape_ratio = escape_scale / mesh_radius

    close = abs(c) < mp.mpf("1e-5")
    bal = r_net < mp.mpf("1e-6") and bal_log < 0.1
    geom = outlier_fraction > mp.mpf("5") and d_n < mp.mpf("5e-3")

    strong_escape = escape_ratio > mp.mpf("50")
    low_defect = mean_pair_defect < mp.mpf("0.03")

    return {
        "abs_c": abs(c),
        "R_net": r_net,
        "balance_log_ratio": bal_log,
        "outlier_fraction": outlier_fraction,
        "mean_pair_defect": mean_pair_defect,
        "D_N": d_n,
        "escape_scale": escape_scale,
        "mesh_radius": mesh_radius,
        "escape_ratio": escape_ratio,
        "CLOSE": close,
        "BAL": bal,
        "GEOM": geom,
        "STRONG_ESCAPE": strong_escape,
        "LOW_DEFECT": low_defect,
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
                "R_net": serial(m["R_net"]),
                "balance_log_ratio": "inf"
                if math.isinf(m["balance_log_ratio"])
                else f"{m['balance_log_ratio']:.12g}",
                "outlier_fraction": serial(m["outlier_fraction"]),
                "mean_pair_defect": serial(m["mean_pair_defect"]),
                "D_N": serial(m["D_N"]),
                "escape_scale": serial(m["escape_scale"]),
                "mesh_radius": serial(m["mesh_radius"]),
                "escape_ratio": serial(m["escape_ratio"]),
                "CLOSE": m["CLOSE"],
                "BAL": m["BAL"],
                "GEOM": m["GEOM"],
                "STRONG_ESCAPE": m["STRONG_ESCAPE"],
                "LOW_DEFECT": m["LOW_DEFECT"],
            }
        )
    return {
        "label": label,
        "planted": None
        if planted is None
        else {"gamma": planted[0], "beta": planted[1], "strength": planted[2]},
        "rows": rows,
        "summary": {
            "close_implies_strong_escape_fail_rows": [
                row["N"] for row in rows if row["CLOSE"] and not row["STRONG_ESCAPE"]
            ],
            "bal_implies_low_defect_fail_rows": [
                row["N"] for row in rows if row["BAL"] and not row["LOW_DEFECT"]
            ],
            "geom_without_split_rows": [
                row["N"]
                for row in rows
                if row["GEOM"] and not (row["STRONG_ESCAPE"] and row["LOW_DEFECT"])
            ],
        },
    }


def main():
    out = {
        "statement": "E79.90 escape/balance split audit",
        "parameters": {
            "lambda": 6,
            "max_n": 18,
            "dps": 60,
            "thresholds": {
                "CLOSE_abs_c_lt": "1e-5",
                "BAL_Rnet_lt": "1e-6",
                "BAL_log_ratio_lt": "0.1",
                "GEOM_outlier_fraction_gt": "5",
                "GEOM_DN_lt": "5e-3",
                "STRONG_ESCAPE_escape_ratio_gt": "50",
                "LOW_DEFECT_mean_pair_defect_lt": "0.03",
            },
        },
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
            f"{label:20s} close->esc fails={s['close_implies_strong_escape_fail_rows']} "
            f"bal->def fails={s['bal_implies_low_defect_fail_rows']} "
            f"geom w/o split={s['geom_without_split_rows']}",
            flush=True,
        )
    out_path = HERE / "E79_90_escape_balance_split_results.json"
    out_path.write_text(json.dumps(out, indent=2) + "\n", encoding="ascii")
    print(f"WROTE {out_path.name}")


if __name__ == "__main__":
    main()
