#!/usr/bin/env python3
"""E79.3l - long-block coupling of the active edge with extra-root and remainder.

This probe tests whether the missing gain could come from a more global
compensation between:

- the signed active 99% edge package,
- the tiny interior remainder,
- the explicit extra-root term.

The active edge is partitioned into long blocks by normalized depth quartiles.
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
BLOCK_CUTS = [0.25, 0.5, 0.75, 1.0]


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
            extra_terms = [p_kernel(k_m[j], sigma) for j in range(dim_common, dim_m)]
            extra_total = mp.fsum(extra_terms)

            # Minimal 99% edge
            active = []
            running = mp.mpf("0")
            for r in range(dim_common):
                term = common_terms[dim_common - 1 - r]
                active.append(term)
                running += term
                if common_total != 0 and abs(running / common_total) >= mp.mpf("0.99"):
                    break
            m99 = len(active)
            outer99 = mp.fsum(active)
            remainder99 = common_total - outer99

            blocks = []
            start = 0
            for cut in BLOCK_CUTS:
                end = int(mp.ceil(cut * m99))
                block = active[start:end]
                blocks.append(mp.fsum(block))
                start = end

            block_data = {}
            for i, block_sum in enumerate(blocks):
                block_data[f"Q{i+1}"] = {
                    "sum": mp.nstr(block_sum, 12),
                    "abs_over_outer99": None if outer99 == 0 else mp.nstr(abs(block_sum / outer99), 12),
                    "abs_over_extra": None if extra_total == 0 else mp.nstr(abs(block_sum / extra_total), 12),
                    "abs_over_remainder": None if remainder99 == 0 else mp.nstr(abs(block_sum / remainder99), 12),
                }

            edge_plus_extra = outer99 + extra_total
            edge_plus_remainder = outer99 + remainder99
            row["sigmas"][str(sigma)] = {
                "common_total": mp.nstr(common_total, 12),
                "extra_total": mp.nstr(extra_total, 12),
                "outer99": mp.nstr(outer99, 12),
                "remainder99": mp.nstr(remainder99, 12),
                "m99": m99,
                "blocks": block_data,
                "abs_edge_plus_extra_over_outer99": None if outer99 == 0 else mp.nstr(abs(edge_plus_extra / outer99), 12),
                "abs_edge_plus_remainder_over_outer99": None if outer99 == 0 else mp.nstr(abs(edge_plus_remainder / outer99), 12),
            }
        rows.append(row)
        s1 = row["sigmas"]["1.0"]
        print(
            f"{label:5s} N={n:2d} "
            f"Q4/extra={s1['blocks']['Q4']['abs_over_extra']} "
            f"Q4/rem={s1['blocks']['Q4']['abs_over_remainder']} "
            f"edge+extra={s1['abs_edge_plus_extra_over_outer99']}",
            flush=True,
        )
    return {"label": label, "L": mp.nstr(L, 20), "dps": dps, "rows": rows}


def main():
    out = {"statement": "E79.3l edge coupling with extra-root and remainder", "cases": []}
    for label, planted in [("zeta", None), ("plant", (GAMMA, "0.30", "5.0"))]:
        out["cases"].append(run_case(label, planted))
    out_path = HERE / "E79_3L_edge_coupling_results.json"
    out_path.write_text(json.dumps(out, indent=2) + "\n", encoding="ascii")
    print(f"WROTE {out_path.name}")


if __name__ == "__main__":
    main()
