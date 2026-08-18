#!/usr/bin/env python3
"""E79.3f - edge profile inside ZERO^common.

For the common-cloud contribution

    ZERO_N^common(sigma)
      = sum_{j<=d_N} common_terms_j(sigma),
    common_terms_j(sigma) = P_sigma(kappa_j^(N+2)) - P_sigma(kappa_j^(N)),

with roots ordered by increasing |kappa|, this probe inspects the terms by
fixed distance from the OUTER edge:

    EDGE_{N,r}(sigma) = common_terms_{d_N-r}(sigma),   r = 0,1,2,...

The question is whether the zeta-side active edge has a stable profile once the
terms are indexed by distance from the boundary and scaled by powers of N.
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
EDGE_DEPTHS = list(range(12))


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
        dim_common = min(len(k_n), len(k_m))
        row = {"N": n, "dim_common": dim_common, "sigmas": {}}
        for sigma in SIGMAS:
            common_terms = [p_kernel(k_m[j], sigma) - p_kernel(k_n[j], sigma) for j in range(dim_common)]
            total = mp.fsum(common_terms)
            edge_terms = {}
            running = mp.mpf("0")
            for r in EDGE_DEPTHS:
                if r >= dim_common:
                    continue
                term = common_terms[dim_common - 1 - r]
                running += term
                edge_terms[str(r)] = {
                    "term": mp.nstr(term, 12),
                    "N_term": mp.nstr(n * term, 12),
                    "N2_term": mp.nstr((n**2) * term, 12),
                    "edge_prefix": mp.nstr(running, 12),
                    "abs_prefix_over_common": None if total == 0 else mp.nstr(abs(running / total), 12),
                }
            row["sigmas"][str(sigma)] = {
                "common_total": mp.nstr(total, 12),
                "edge_terms": edge_terms,
            }
        rows.append(row)
        s1 = row["sigmas"]["1.0"]["edge_terms"]
        t0 = s1.get("0")
        t3 = s1.get("3")
        t7 = s1.get("7")
        print(
            f"{label:5s} N={n:2d} "
            f"N2t0={None if t0 is None else t0['N2_term']:>14s} "
            f"N2t3={None if t3 is None else t3['N2_term']:>14s} "
            f"share8={None if t7 is None else t7['abs_prefix_over_common']}",
            flush=True,
        )
    return {"label": label, "L": mp.nstr(L, 20), "dps": dps, "rows": rows}


def main():
    out = {"statement": "E79.3f edge profile inside ZERO^common", "cases": []}
    for label, planted in [("zeta", None), ("plant", (GAMMA, "0.30", "5.0"))]:
        out["cases"].append(run_case(label, planted))
    out_path = HERE / "E79_3F_edge_profile_results.json"
    out_path.write_text(json.dumps(out, indent=2) + "\n", encoding="ascii")
    print(f"WROTE {out_path.name}")


if __name__ == "__main__":
    main()
