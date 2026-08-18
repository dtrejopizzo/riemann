#!/usr/bin/env python3
"""E79.3n - sweep mesoscopic deep-tail cuts against ZERO^extra.

Replace the crude last-quartile tail by a family of tails consisting of the last
alpha fraction of the active 99% edge, and measure the signed pairing

    tail_alpha - ZERO^extra.
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
ALPHAS = [mp.mpf("0.20"), mp.mpf("0.30"), mp.mpf("0.40"), mp.mpf("0.50"), mp.mpf("0.60")]


def alpha_key(a):
    return mp.nstr(a, 12)


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
        dim_n = len(k_n)
        dim_m = len(k_m)
        dim_common = min(dim_n, dim_m)
        row = {"N": n, "dim_common": dim_common, "sigmas": {}}
        for sigma in SIGMAS:
            common_terms = [p_kernel(k_m[j], sigma) - p_kernel(k_n[j], sigma) for j in range(dim_common)]
            common_total = mp.fsum(common_terms)
            extra_total = mp.fsum(p_kernel(k_m[j], sigma) for j in range(dim_common, dim_m))

            active = []
            running = mp.mpf("0")
            for r in range(dim_common):
                term = common_terms[dim_common - 1 - r]
                active.append(term)
                running += term
                if common_total != 0 and abs(running / common_total) >= mp.mpf("0.99"):
                    break
            m99 = len(active)

            alphas = {}
            for alpha in ALPHAS:
                take = max(1, int(mp.ceil(alpha * m99)))
                tail = mp.fsum(active[m99 - take : m99])
                minus = tail - extra_total
                scale = max(abs(tail), abs(extra_total))
                alphas[alpha_key(alpha)] = {
                    "take": take,
                    "take_over_m99": mp.nstr(mp.mpf(take) / m99, 12),
                    "tail": mp.nstr(tail, 12),
                    "minus": mp.nstr(minus, 12),
                    "abs_minus_over_maxpiece": None if scale == 0 else mp.nstr(abs(minus) / scale, 12),
                    "N2_abs_minus": mp.nstr((n**2) * abs(minus), 12),
                }

            row["sigmas"][str(sigma)] = {
                "extra": mp.nstr(extra_total, 12),
                "m99": m99,
                "alphas": alphas,
            }
        rows.append(row)
        s1 = row["sigmas"]["1.0"]["alphas"]
        best = min((float(v["abs_minus_over_maxpiece"]), k, v) for k, v in s1.items())
        print(
            f"{label:5s} N={n:2d} best_alpha={best[1]} "
            f"ratio={best[2]['abs_minus_over_maxpiece']} N2minus={best[2]['N2_abs_minus']}",
            flush=True,
        )
    return {"label": label, "L": mp.nstr(L, 20), "dps": dps, "rows": rows}


def main():
    out = {"statement": "E79.3n mesoscopic tail sweep against extra-root", "cases": []}
    for label, planted in [("zeta", None), ("plant", (GAMMA, "0.30", "5.0"))]:
        out["cases"].append(run_case(label, planted))
    out_path = HERE / "E79_3N_tail_sweep_results.json"
    out_path.write_text(json.dumps(out, indent=2) + "\n", encoding="ascii")
    print(f"WROTE {out_path.name}")


if __name__ == "__main__":
    main()
