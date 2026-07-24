#!/usr/bin/env python3
"""E79.3c - shell decomposition inside the common-cloud part of ZERO.

After E79.3a/b the hard object is

    ZERO_N^common(sigma)
      = sum_{j<=d_N} P_sigma(kappa_j^(N+2)) - sum_{j<=d_N} P_sigma(kappa_j^(N))

with roots ordered by increasing |kappa|. This probe asks whether the common
part is concentrated near the OUTER edge of the common cloud, or whether it is
distributed throughout the cloud.
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
LAST_M_LIST = [2, 4, 6, 8, 10]


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
        dim_small = min(len(k_n), len(k_m))
        row = {"N": n, "dim_common": dim_small, "sigmas": {}}
        for sigma in SIGMAS:
            common_terms = [p_kernel(k_m[j], sigma) - p_kernel(k_n[j], sigma) for j in range(dim_small)]
            common_total = mp.fsum(common_terms)
            shells = {}
            for m in LAST_M_LIST:
                if m > dim_small:
                    continue
                outer = mp.fsum(common_terms[dim_small - m:dim_small])
                inner = common_total - outer
                shells[str(m)] = {
                    "outer": mp.nstr(outer, 12),
                    "inner": mp.nstr(inner, 12),
                    "abs_outer_over_common": None if common_total == 0 else mp.nstr(abs(outer / common_total), 12),
                }
            row["sigmas"][str(sigma)] = {
                "common_total": mp.nstr(common_total, 12),
                "shells": shells,
            }
        rows.append(row)
        s1 = row["sigmas"]["1.0"]
        sh8 = s1["shells"].get("8")
        print(
            f"{label:5s} N={n:2d} common={s1['common_total']:>14s} "
            f"outer8={None if sh8 is None else sh8['outer']:>14s} "
            f"share8={None if sh8 is None else sh8['abs_outer_over_common']}",
            flush=True,
        )
    return {"label": label, "L": mp.nstr(L, 20), "dps": dps, "rows": rows}


def main():
    out = {"statement": "E79.3c shell decomposition inside ZERO^common", "cases": []}
    for label, planted in [("zeta", None), ("plant", (GAMMA, "0.30", "5.0"))]:
        out["cases"].append(run_case(label, planted))
    out_path = HERE / "E79_3C_common_shell_results.json"
    out_path.write_text(json.dumps(out, indent=2) + "\n", encoding="ascii")
    print(f"WROTE {out_path.name}")


if __name__ == "__main__":
    main()
