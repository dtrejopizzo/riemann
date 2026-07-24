#!/usr/bin/env python3
"""E79.3i - effective edge width inside the active outer layer.

The raw edge budget of E79.3g/3h uses the crude count m_theta(N) of shells in
the active outer layer. This probe asks whether the deeper shells are weak
enough that the *effective* width is much smaller than the raw shell count.

For the first m_theta shells from the edge, define weights from the N^2-scaled
shell amplitudes and compare:

    raw width      = m_theta,
    effective width = sum_r weight_r / max_r weight_r,
    relative mass   = effective width / m_theta.
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
THRESHOLDS = [mp.mpf("0.9"), mp.mpf("0.99")]


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


def run_case(label, planted, lam_int=6, max_n=26, dps=60):
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
            scaled_terms = []
            for j in range(dim_common):
                term = common_terms[dim_common - 1 - j]
                running += term
                outer_prefixes.append(running)
                scaled_terms.append(abs((n**2) * term))

            thresholds = {}
            for t in THRESHOLDS:
                m = min_outer_thickness(outer_prefixes, abs(total), t)
                if m is None:
                    thresholds[threshold_key(t)] = None
                    continue
                active = scaled_terms[:m]
                peak = max(active) if active else mp.mpf("0")
                effective = mp.fsum(active) / peak if peak != 0 else mp.mpf("0")
                avg = mp.fsum(active) / m if m else mp.mpf("0")
                thresholds[threshold_key(t)] = {
                    "m": m,
                    "m_over_N": mp.nstr(mp.mpf(m) / n, 12),
                    "peak_N2_shell": mp.nstr(peak, 12),
                    "avg_N2_shell": mp.nstr(avg, 12),
                    "effective_width": mp.nstr(effective, 12),
                    "effective_over_raw": mp.nstr(effective / m, 12) if m else None,
                    "effective_over_N": mp.nstr(effective / n, 12),
                }
            row["sigmas"][str(sigma)] = {
                "common_total": mp.nstr(total, 12),
                "thresholds": thresholds,
            }
        rows.append(row)
        s1 = row["sigmas"]["1.0"]["thresholds"]["0.9"]
        print(
            f"{label:5s} N={n:2d} "
            f"m90/N={s1['m_over_N']:>8s} "
            f"eff/raw={s1['effective_over_raw']:>10s} "
            f"eff/N={s1['effective_over_N']:>10s}",
            flush=True,
        )
    return {"label": label, "L": mp.nstr(L, 20), "dps": dps, "rows": rows}


def main():
    out = {"statement": "E79.3i effective edge width", "cases": []}
    for label, planted in [("zeta", None), ("plant", (GAMMA, "0.30", "5.0"))]:
        out["cases"].append(run_case(label, planted))
    out_path = HERE / "E79_3I_effective_edge_width_results.json"
    out_path.write_text(json.dumps(out, indent=2) + "\n", encoding="ascii")
    print(f"WROTE {out_path.name}")


if __name__ == "__main__":
    main()
