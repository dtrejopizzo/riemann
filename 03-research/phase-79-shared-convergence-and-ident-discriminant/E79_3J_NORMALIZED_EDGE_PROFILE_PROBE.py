#!/usr/bin/env python3
"""E79.3j - normalized edge profile inside the active layer.

The previous probes established:

- raw active width m_theta(N) is linear in N,
- shell amplitudes near the edge scale like N^-2,
- effective width only improves the constant.

This probe asks whether the active edge has an intrinsic shape when depth is
normalized by the active width itself:

    u = r / m_theta(N),   0 <= u <= 1.

If the deep part of the edge decays according to a stable profile in u, that
could be the source of the missing gain.
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
U_BINS = [mp.mpf(k) / 10 for k in range(11)]


def threshold_key(t):
    return mp.nstr(t, 12)


def bin_key(u):
    return mp.nstr(u, 12)


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


def assigned_bin(u):
    best = None
    bestdist = None
    for b in U_BINS:
        dist = abs(u - b)
        if best is None or dist < bestdist:
            best = b
            bestdist = dist
    return best


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
    aggregate = {
        str(sigma): {threshold_key(t): {bin_key(b): [] for b in U_BINS} for t in THRESHOLDS}
        for sigma in SIGMAS
    }

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
                bins = {bin_key(b): [] for b in U_BINS}
                for r, val in enumerate(active):
                    u = mp.mpf(r) / m if m else mp.mpf("0")
                    b = assigned_bin(u)
                    norm = val / peak if peak != 0 else mp.mpf("0")
                    bins[bin_key(b)].append(norm)
                    aggregate[str(sigma)][threshold_key(t)][bin_key(b)].append(norm)
                thresholds[threshold_key(t)] = {
                    "m": m,
                    "peak_N2_shell": mp.nstr(peak, 12),
                    "bin_means": {
                        bk: None if not vals else mp.nstr(mp.fsum(vals) / len(vals), 12)
                        for bk, vals in bins.items()
                    },
                }
            row["sigmas"][str(sigma)] = {
                "common_total": mp.nstr(total, 12),
                "thresholds": thresholds,
            }
        rows.append(row)
        t90 = row["sigmas"]["1.0"]["thresholds"]["0.9"]
        bm = t90["bin_means"]
        print(
            f"{label:5s} N={n:2d} "
            f"u0={bm['0.0']} u0.5={bm['0.5']} u0.9={bm['0.9']} u1={bm['1.0']}",
            flush=True,
        )

    aggregate_means = {}
    for sigma in SIGMAS:
        sigma_key = str(sigma)
        aggregate_means[sigma_key] = {}
        for t in THRESHOLDS:
            tk = threshold_key(t)
            aggregate_means[sigma_key][tk] = {
                bk: None if not vals else mp.nstr(mp.fsum(vals) / len(vals), 12)
                for bk, vals in aggregate[sigma_key][tk].items()
            }

    return {
        "label": label,
        "L": mp.nstr(L, 20),
        "dps": dps,
        "u_bins": [bin_key(b) for b in U_BINS],
        "rows": rows,
        "aggregate_bin_means": aggregate_means,
    }


def main():
    out = {"statement": "E79.3j normalized edge profile", "cases": []}
    for label, planted in [("zeta", None), ("plant", (GAMMA, "0.30", "5.0"))]:
        out["cases"].append(run_case(label, planted))
    out_path = HERE / "E79_3J_normalized_edge_profile_results.json"
    out_path.write_text(json.dumps(out, indent=2) + "\n", encoding="ascii")
    print(f"WROTE {out_path.name}")


if __name__ == "__main__":
    main()
