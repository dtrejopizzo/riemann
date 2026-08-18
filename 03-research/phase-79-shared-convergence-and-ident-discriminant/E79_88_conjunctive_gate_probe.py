#!/usr/bin/env python3
"""E79.88 - conjunctive discriminant gate audit.

Tests whether a simple conjunction of three finite predicates separates the
audited zeta regime from the planted controls:

  CLOSE:  |c_N| small
  BAL:    residual package nearly balanced
  GEOM:   cloud geometry in the zeta regime

This is not a theorem-grade criterion. It is an audit turning E79.87's
structural correction into an explicit finite gate.
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


def section_metrics(H, idx, L):
    _mu, _A, db_idx, inner, x = right_transfer_data(H, idx)
    d = [2 * mp.pi * n / L for n in inner]
    db = 2 * mp.pi * db_idx / L
    xv = [x[j] for j in range(x.rows)]
    q = [dj - db for dj in d]
    r = [qj * xj for qj, xj in zip(q, xv)]
    c = 1 - mp.fsum(xv)

    pos_abs = mp.fsum(abs(v) for v in r if v > 0)
    neg_abs = mp.fsum(abs(v) for v in r if v < 0)
    total_abs = pos_abs + neg_abs
    r_net = abs(mp.fsum(r)) / total_abs if total_abs else mp.mpf("0")
    r_pm = pos_abs / neg_abs if neg_abs else mp.inf
    bal_log = finite_log_ratio(pos_abs, neg_abs)

    n = len(d)
    K = mp.matrix(n, n)
    for a in range(n):
        for b in range(n):
            K[a, b] = (d[a] if a == b else mp.mpf("0")) + x[a] * q[b] / c
    eigvals, _ = mp.eig(K)
    kappas = sorted([mp.re(ev) for ev in eigvals], key=lambda t: abs(t), reverse=True)
    outlier = abs(kappas[0])
    second = abs(kappas[1])
    cloud = kappas[1:]
    pos = sorted([v for v in cloud if v > 0], key=abs)
    neg = sorted([-v for v in cloud if v < 0], key=abs)
    defects = [abs(p - n0) / (p + n0) for p, n0 in zip(pos, neg)]
    mean_def = mp.fsum(defects) / len(defects)
    out_frac = outlier / second
    d_norm = mean_def / out_frac

    return {
        "abs_c": abs(c),
        "R_net": r_net,
        "R_pm": r_pm,
        "balance_log_ratio": bal_log,
        "outlier_fraction": out_frac,
        "mean_pair_defect": mean_def,
        "D_N": d_norm,
    }


def predicates(metrics):
    close = metrics["abs_c"] < mp.mpf("1e-5")
    balance = metrics["R_net"] < mp.mpf("1e-6") and metrics["balance_log_ratio"] < 0.1
    geom = metrics["outlier_fraction"] > mp.mpf("5") and metrics["D_N"] < mp.mpf("5e-3")
    return {
        "CLOSE": close,
        "BAL": balance,
        "GEOM": geom,
        "ALL3": close and balance and geom,
    }


def run_case(label, planted, max_n=12, dps=60):
    mp.mp.dps = dps
    Hmax, idxmax, L = build_mp(6, max_n, dps, planted=planted)
    rows = []
    for N in range(8, max_n + 1, 2):
        H, idx = section(Hmax, idxmax, max_n, N)
        metrics = section_metrics(H, idx, L)
        gates = predicates(metrics)
        rows.append(
            {
                "N": N,
                "abs_c": serial(metrics["abs_c"]),
                "R_net": serial(metrics["R_net"]),
                "R_pm": "inf" if metrics["R_pm"] == mp.inf else serial(metrics["R_pm"]),
                "balance_log_ratio": "inf"
                if math.isinf(metrics["balance_log_ratio"])
                else f"{metrics['balance_log_ratio']:.12g}",
                "outlier_fraction": serial(metrics["outlier_fraction"]),
                "mean_pair_defect": serial(metrics["mean_pair_defect"]),
                "D_N": serial(metrics["D_N"]),
                **gates,
            }
        )
    return {
        "label": label,
        "planted": None
        if planted is None
        else {"gamma": planted[0], "beta": planted[1], "strength": planted[2]},
        "rows": rows,
        "summary": {
            "ALL3_count": sum(1 for row in rows if row["ALL3"]),
            "CLOSE_count": sum(1 for row in rows if row["CLOSE"]),
            "BAL_count": sum(1 for row in rows if row["BAL"]),
            "GEOM_count": sum(1 for row in rows if row["GEOM"]),
        },
    }


def main():
    out = {
        "statement": "E79.88 conjunctive discriminant gate audit",
        "parameters": {
            "lambda": 6,
            "max_n": 12,
            "dps": 60,
            "thresholds": {
                "CLOSE_abs_c_lt": "1e-5",
                "BAL_Rnet_lt": "1e-6",
                "BAL_log_ratio_lt": "0.1",
                "GEOM_outlier_fraction_gt": "5",
                "GEOM_DN_lt": "5e-3",
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
        print(
            f"{label:20s} ALL3={case['summary']['ALL3_count']} "
            f"CLOSE={case['summary']['CLOSE_count']} "
            f"BAL={case['summary']['BAL_count']} "
            f"GEOM={case['summary']['GEOM_count']}",
            flush=True,
        )
    out_path = HERE / "E79_88_conjunctive_gate_results.json"
    out_path.write_text(json.dumps(out, indent=2) + "\n", encoding="ascii")
    print(f"WROTE {out_path.name}")


if __name__ == "__main__":
    main()
