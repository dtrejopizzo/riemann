#!/usr/bin/env python3
"""E79.3e - interior remainder after removing the active outer layer.

Starting from the common-cloud term

    ZERO_N^common(sigma)
      = sum_{j<=d_N} common_terms_j(sigma),
    common_terms_j(sigma) = P_sigma(kappa_j^(N+2)) - P_sigma(kappa_j^(N)),

with roots ordered by increasing |kappa|, E79.3d measured the minimal outer
thickness m_theta(N) needed so that the last m_theta shells capture a fraction
theta of |ZERO_N^common|.

This probe keeps that exact minimal thickness and measures the leftover
interior remainder

    REM_{N,theta}(sigma) = ZERO_N^common(sigma) - OUTER_{N,m_theta}(sigma).
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
from E77_3c_two_generator_ident_probe import GAMMA, right_transfer_data  # noqa: E402
from E78_9_w_quotient_delta_probe import section  # noqa: E402

SIGMAS = [mp.mpf("1.0"), mp.mpf("2.0")]
THRESHOLDS = [mp.mpf("0.5"), mp.mpf("0.9"), mp.mpf("0.99")]


def threshold_key(t):
    return mp.nstr(t, 12)


def p_kernel(a, sigma):
    return 2 * sigma / (a * a + sigma * sigma)


def kappas_for_section(H, idx, L):
    _, _, db_idx, inner, x = right_transfer_data(H, idx)
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
    return sorted([mp.re(ev) for ev in eigvals], key=lambda z: abs(z))


def min_outer_thickness(shell_prefixes_from_edge, total_abs, threshold):
    if total_abs == 0:
        return None
    for m, val in enumerate(shell_prefixes_from_edge, start=1):
        if abs(val) / total_abs >= threshold:
            return m
    return None


def run_case(label, planted, lam_int=6, max_n=18, dps=60):
    mp.mp.dps = dps
    H, idx, L = build_mp(lam_int, max_n, dps, planted=planted)
    cache = {}

    def get_kappas(n):
        if n not in cache:
            Hn, idxn = section(H, idx, max_n, n)
            cache[n] = kappas_for_section(Hn, idxn, L)
        return cache[n]

    rows = []
    for n in range(8, max_n - 1, 2):
        k_n = get_kappas(n)
        k_m = get_kappas(n + 2)
        dim_common = min(len(k_n), len(k_m))
        row = {"N": n, "dim_common": dim_common, "sigmas": {}}
        for sigma in SIGMAS:
            common_terms = [p_kernel(k_m[j], sigma) - p_kernel(k_n[j], sigma) for j in range(dim_common)]
            total = mp.fsum(common_terms)
            outer_prefixes = []
            running = mp.mpf("0")
            for j in range(dim_common):
                running += common_terms[dim_common - 1 - j]
                outer_prefixes.append(running)

            thresholds = {}
            for t in THRESHOLDS:
                m = min_outer_thickness(outer_prefixes, abs(total), t)
                if m is None:
                    thresholds[threshold_key(t)] = None
                    continue
                outer = outer_prefixes[m - 1]
                remainder = total - outer
                thresholds[threshold_key(t)] = {
                    "m": m,
                    "fraction_of_dim": m / dim_common,
                    "outer": mp.nstr(outer, 12),
                    "remainder": mp.nstr(remainder, 12),
                    "abs_remainder_over_common": None if total == 0 else mp.nstr(abs(remainder / total), 12),
                    "N_abs_remainder": mp.nstr(n * abs(remainder), 12),
                    "N2_abs_remainder": mp.nstr((n**2) * abs(remainder), 12),
                }

            row["sigmas"][str(sigma)] = {
                "common_total": mp.nstr(total, 12),
                "thresholds": thresholds,
            }
        rows.append(row)
        s1 = row["sigmas"]["1.0"]["thresholds"]
        t90 = s1[threshold_key(mp.mpf("0.9"))]
        t99 = s1[threshold_key(mp.mpf("0.99"))]
        print(
            f"{label:5s} N={n:2d} "
            f"r90={None if t90 is None else t90['remainder']:>14s} "
            f"N*r90={None if t90 is None else t90['N_abs_remainder']:>12s} "
            f"r99={None if t99 is None else t99['remainder']:>14s} "
            f"N*r99={None if t99 is None else t99['N_abs_remainder']:>12s}",
            flush=True,
        )
    return {"label": label, "L": mp.nstr(L, 20), "dps": dps, "rows": rows}


def main():
    out = {"statement": "E79.3e interior remainder after removing the active outer layer", "cases": []}
    for label, planted in [("zeta", None), ("plant", (GAMMA, "0.30", "5.0"))]:
        out["cases"].append(run_case(label, planted))
    out_path = HERE / "E79_3E_interior_remainder_results.json"
    out_path.write_text(json.dumps(out, indent=2) + "\n", encoding="ascii")
    print(f"WROTE {out_path.name}")


if __name__ == "__main__":
    main()
