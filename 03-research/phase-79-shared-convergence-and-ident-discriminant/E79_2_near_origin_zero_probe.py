#!/usr/bin/env python3
"""E79.2 - near-origin / tail split of ZERO_N(sigma).

For each consecutive pair N -> N+2 this probe splits

    ZERO_N(sigma) = sum_{kappa in K_{N+2}} P_sigma(kappa)
                  - sum_{kappa in K_N}     P_sigma(kappa)

into:
  (i) a partial sum over the m closest roots to the origin in each section,
  (ii) the complementary tail.

This does not prove a canonical pairing theorem yet. It answers a prior,
sharper question: does most of ZERO come from a small near-origin packet, or
from the bulk/tail of the spectral cloud?
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

SIGMAS = [mp.mpf("0.55"), mp.mpf("1.0"), mp.mpf("2.0"), mp.mpf("3.0")]
M_LIST = [2, 4, 6, 8, 10, 12]


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


def partial_zero(k_small, sigma):
    return mp.fsum(p_kernel(k, sigma) for k in k_small)


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
        row = {"N": n, "closest_N": [mp.nstr(v, 16) for v in k_n[:12]], "sigmas": {}}
        for sigma in SIGMAS:
            total = partial_zero(k_m, sigma) - partial_zero(k_n, sigma)
            sigma_row = {
                "total_ZERO": mp.nstr(total, 12),
                "splits": {},
            }
            for m in M_LIST:
                near = partial_zero(k_m[:m], sigma) - partial_zero(k_n[:m], sigma)
                tail = total - near
                share = None
                if total != 0:
                    share = abs(near / total)
                sigma_row["splits"][str(m)] = {
                    "near": mp.nstr(near, 12),
                    "tail": mp.nstr(tail, 12),
                    "abs_near_over_total": None if share is None else mp.nstr(share, 12),
                }
            rows.append(row) if False else None
            row["sigmas"][str(sigma)] = sigma_row
        rows.append(row)
        s1 = row["sigmas"]["1.0"]
        m8 = s1["splits"]["8"]
        print(
            f"{label:5s} N={n:2d} total={s1['total_ZERO']:>14s} "
            f"near8={m8['near']:>14s} tail8={m8['tail']:>14s} "
            f"| |near8/total|={m8['abs_near_over_total']}",
            flush=True,
        )
    return {"label": label, "L": mp.nstr(L, 20), "dps": dps, "rows": rows}


def main():
    out = {
        "statement": "E79.2 near-origin/tail split of ZERO_N(sigma)",
        "cases": [],
    }
    for label, planted in [("zeta", None), ("plant", (GAMMA, "0.30", "5.0"))]:
        out["cases"].append(run_case(label, planted))
    out_path = HERE / "E79_2_near_origin_zero_results.json"
    out_path.write_text(json.dumps(out, indent=2) + "\n", encoding="ascii")
    print(f"WROTE {out_path.name}")


if __name__ == "__main__":
    main()
