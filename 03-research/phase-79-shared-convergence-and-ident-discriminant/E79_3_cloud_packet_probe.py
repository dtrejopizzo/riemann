#!/usr/bin/env python3
"""E79.3a - cumulative cloud-packet audit for ZERO_N(sigma).

For each step N -> N+2, sort spec(K_N) and spec(K_{N+2}) by absolute value.
Define the cumulative packet contribution

    ZERO_N^(<=m)(sigma)
      = sum_{j<=m} P_sigma(kappa_j^{N+2}) - sum_{j<=m} P_sigma(kappa_j^N).

This probe asks:
  how large must m be, as a function of N, to capture a fixed fraction of
  |ZERO_N(sigma)|?

If m must be comparable to the full dimension, then the live E79.3 object is
truly a whole-cloud problem rather than a narrow cofinal packet.
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


def min_m_for_fraction(cumvals, total_abs, threshold):
    if total_abs == 0:
        return None
    for m, val in enumerate(cumvals, start=1):
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
        dim_small = min(len(k_n), len(k_m))
        row = {"N": n, "dim_N": len(k_n), "dim_Np2": len(k_m), "sigmas": {}}
        for sigma in SIGMAS:
            total_exact = mp.fsum(p_kernel(k, sigma) for k in k_m) - mp.fsum(p_kernel(k, sigma) for k in k_n)
            prefixes = []
            running = mp.mpf("0")
            for j in range(dim_small):
                running += p_kernel(k_m[j], sigma) - p_kernel(k_n[j], sigma)
                prefixes.append(running)
            common_total = prefixes[-1]
            extra_total = total_exact - common_total
            thresholds = {}
            for t in THRESHOLDS:
                m = min_m_for_fraction(prefixes, abs(total_exact), t)
                thresholds[threshold_key(t)] = None if m is None else {
                    "m": m,
                    "fraction_of_dim": m / dim_small,
                }
            row["sigmas"][str(sigma)] = {
                "total_ZERO_exact": mp.nstr(total_exact, 12),
                "common_prefix_total": mp.nstr(common_total, 12),
                "extra_root_total": mp.nstr(extra_total, 12),
                "thresholds": thresholds,
                "prefix_samples": {
                    str(m): mp.nstr(prefixes[m - 1], 12)
                    for m in [2, 4, 8, 12, 16, 20, dim_small]
                    if m <= dim_small
                },
            }
        rows.append(row)
        s1 = row["sigmas"]["1.0"]
        t50 = s1["thresholds"][threshold_key(mp.mpf("0.5"))]
        t90 = s1["thresholds"][threshold_key(mp.mpf("0.9"))]
        print(
            f"{label:5s} N={n:2d} dim={dim_small:2d} total={s1['total_ZERO_exact']:>14s} "
            f"common={s1['common_prefix_total']:>14s} extra={s1['extra_root_total']:>14s} "
            f"m50={None if t50 is None else t50['m']} "
            f"m90={None if t90 is None else t90['m']}",
            flush=True,
        )
    return {"label": label, "L": mp.nstr(L, 20), "dps": dps, "rows": rows}


def main():
    out = {"statement": "E79.3a cumulative cloud-packet audit for ZERO", "cases": []}
    for label, planted in [("zeta", None), ("plant", (GAMMA, "0.30", "5.0"))]:
        out["cases"].append(run_case(label, planted))
    out_path = HERE / "E79_3_cloud_packet_results.json"
    out_path.write_text(json.dumps(out, indent=2) + "\n", encoding="ascii")
    print(f"WROTE {out_path.name}")


if __name__ == "__main__":
    main()
