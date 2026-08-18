#!/usr/bin/env python3
"""E79.85 - root-cloud symmetry audit for the secular package.

For each audited section, build the K_N spectrum and measure:

  - outlier_fraction = |kappa_max| / second-largest |kappa|
  - pair_symmetry_defect on the remaining cloud after removing the farthest
    outlier: positives and negatives are paired by increasing magnitude and
    compared through |p-n|/(p+n).

The goal is to test whether the residual-balance regime from E79.84 is already
visible as a near-symmetry of the finite spectral cloud.
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
sys.path.insert(0, str(PHASE76))
sys.path.insert(0, str(PHASE77))
sys.path.insert(0, str(PHASE78))

from P76_002_mp_entry_audit import build_mp  # noqa: E402
from E78_9_w_quotient_delta_probe import section  # noqa: E402
from E77_3c_two_generator_ident_probe import GAMMA, right_transfer_data  # noqa: E402

GAMMA2 = "21.022039638771554992"


def serial(x: mp.mpf, digits: int = 18) -> str:
    return mp.nstr(x, digits)


def kappas_for_section(H, idx, L):
    _mu, _A, db_idx, inner, x = right_transfer_data(H, idx)
    d = [2 * mp.pi * n / L for n in inner]
    db = 2 * mp.pi * db_idx / L
    n = len(d)
    xv = mp.matrix([x[j] for j in range(n)])
    q = mp.matrix([d[j] - db for j in range(n)])
    c = 1 - mp.fsum(x[j] for j in range(n))
    K = mp.matrix(n, n)
    for a in range(n):
        for b in range(n):
            K[a, b] = (d[a] if a == b else mp.mpf("0")) + xv[a] * q[b] / c
    eigvals, _ = mp.eig(K)
    return [mp.re(ev) for ev in eigvals]


def symmetry_stats(kappas):
    ordered = sorted(kappas, key=lambda t: abs(t), reverse=True)
    outlier = ordered[0]
    second = ordered[1] if len(ordered) > 1 else mp.mpf("0")
    cloud = ordered[1:]
    pos = sorted([v for v in cloud if v > 0], key=abs)
    neg = sorted([-v for v in cloud if v < 0], key=abs)
    pairs = min(len(pos), len(neg))
    defects = []
    for j in range(pairs):
        p = pos[j]
        n = neg[j]
        defects.append(abs(p - n) / (p + n))
    mean_def = mp.fsum(defects) / len(defects) if defects else mp.mpf("0")
    max_def = max(defects) if defects else mp.mpf("0")
    unpaired = abs(len(pos) - len(neg))
    return {
        "outlier_abs": abs(outlier),
        "second_abs": abs(second),
        "outlier_fraction": abs(outlier) / max(abs(second), mp.mpf("1e-30")),
        "pair_count": pairs,
        "positive_count": len(pos),
        "negative_count": len(neg),
        "unpaired_count": unpaired,
        "mean_pair_defect": mean_def,
        "max_pair_defect": max_def,
    }


def run_case(label, planted, max_n=12, dps=60):
    mp.mp.dps = dps
    Hmax, idxmax, L = build_mp(6, max_n, dps, planted=planted)
    rows = []
    for N in range(8, max_n + 1, 2):
        H, idx = section(Hmax, idxmax, max_n, N)
        stats = symmetry_stats(kappas_for_section(H, idx, L))
        rows.append(
            {
                "N": N,
                "outlier_abs": serial(stats["outlier_abs"]),
                "second_abs": serial(stats["second_abs"]),
                "outlier_fraction": serial(stats["outlier_fraction"]),
                "pair_count": stats["pair_count"],
                "positive_count": stats["positive_count"],
                "negative_count": stats["negative_count"],
                "unpaired_count": stats["unpaired_count"],
                "mean_pair_defect": serial(stats["mean_pair_defect"]),
                "max_pair_defect": serial(stats["max_pair_defect"]),
            }
        )
    return {
        "label": label,
        "planted": None
        if planted is None
        else {"gamma": planted[0], "beta": planted[1], "strength": planted[2]},
        "rows": rows,
        "summary": {
            "max_mean_pair_defect": serial(max(mp.mpf(r["mean_pair_defect"]) for r in rows)),
            "min_mean_pair_defect": serial(min(mp.mpf(r["mean_pair_defect"]) for r in rows)),
            "max_outlier_fraction": serial(max(mp.mpf(r["outlier_fraction"]) for r in rows)),
            "min_outlier_fraction": serial(min(mp.mpf(r["outlier_fraction"]) for r in rows)),
        },
    }


def main():
    out = {
        "statement": "E79.85 cloud symmetry bridge audit",
        "parameters": {"lambda": 6, "max_n": 12, "dps": 60},
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
            f"{label:20s} mean-def band="
            f"{case['summary']['min_mean_pair_defect']}..{case['summary']['max_mean_pair_defect']} "
            f"outlier-frac band={case['summary']['min_outlier_fraction']}..{case['summary']['max_outlier_fraction']}",
            flush=True,
        )
    out_path = HERE / "E79_85_cloud_symmetry_bridge_results.json"
    out_path.write_text(json.dumps(out, indent=2) + "\n", encoding="ascii")
    print(f"WROTE {out_path.name}")


if __name__ == "__main__":
    main()
