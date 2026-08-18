#!/usr/bin/env python3
"""E78.137 - mu_N -> 0 convergence gate probe.

Decisive question: does the second inner-block eigenvalue nu_1^(N) converge to
a strictly positive limit (Branch A: uniform gap, rank-one deflation valid) or
to 0 (Branch B: tower collapse, growing-rank deflation needed)?

Reuses P76.002 build_mp verbatim (genuine build planted=None; standard planted
falsifier ("14.134725141734693790","0.30","5.0")), lambda=6.
"""
import json
import sys
import mpmath as mp

sys.path.insert(0, "/Users/dt/riemann/03-research/phase-76-normalized-adjugate-arithmetic-lock")
from P76_002_mp_entry_audit import build_mp  # noqa: E402

PLANTED = ("14.134725141734693790", "0.30", "5.0")
DPS = 70
LAM = 6


def off_diag_norm_estimate(H):
    """Crude ||B_L|| proxy: Schur/Frobenius-type bound via max abs row sum of
    off-diagonal part (Gershgorin-style operator norm upper bound)."""
    n = H.rows
    max_row = mp.mpf(0)
    for i in range(n):
        s = mp.mpf(0)
        for j in range(n):
            if i != j:
                s += abs(H[i, j])
        if s > max_row:
            max_row = s
    return max_row


def run_one(L_int, N, dps, planted):
    H, idx, L = build_mp(L_int, N, dps, planted=planted)
    # Use the INNER block A_N = H[1:-1,1:-1] (indices -N+1..N-1), matching
    # E77.7d/E78.1: this is the H_L=D_L+B_L operator whose ground eigenvalue
    # is mu_N. The full bordered H includes the boundary Cauchy row/column
    # and is NOT the same operator.
    inner = H[1:-1, 1:-1]
    vals, vecs = mp.eigsy(inner)
    order = sorted(range(vals.rows), key=lambda i: vals[i])
    nu0 = vals[order[0]]
    nu1 = vals[order[1]]
    gap = nu1 - nu0
    Bnorm = off_diag_norm_estimate(inner)
    diag_bottom_gap = mp.log(2)  # log(1+1)-log(1+0)
    return {
        "N": N,
        "nu0": mp.nstr(nu0, 20),
        "nu1": mp.nstr(nu1, 20),
        "gap": mp.nstr(gap, 20),
        "Bnorm_upper": mp.nstr(Bnorm, 12),
        "diag_bottom_gap_log2": mp.nstr(diag_bottom_gap, 12),
    }


def run():
    results = {"lambda": LAM, "dps": DPS, "L_values": [4, 6, 8], "builds": {}}
    for build_name, planted in (("zeta", None), ("plant", PLANTED)):
        results["builds"][build_name] = {}
        for L_int in (4, 6, 8):
            rows = []
            Ns = list(range(6, 17, 2))
            for N in Ns:
                try:
                    r = run_one(L_int, N, DPS, planted)
                    rows.append(r)
                    print(build_name, "L=", L_int, r)
                except Exception as e:
                    print(build_name, "L=", L_int, "N=", N, "FAILED:", repr(e))
                    break
            # ratios of nu1 across steps of 2 in N
            ratios = []
            for i in range(1, len(rows)):
                try:
                    nu1_prev = mp.mpf(rows[i - 1]["nu1"])
                    nu1_cur = mp.mpf(rows[i]["nu1"])
                    if nu1_prev != 0:
                        ratios.append(mp.nstr(nu1_cur / nu1_prev, 12))
                    else:
                        ratios.append("undef")
                except Exception:
                    ratios.append("err")
            results["builds"][build_name][f"L={L_int}"] = {
                "rows": rows,
                "nu1_ratio_consecutive": ratios,
            }
    with open(
        "/Users/dt/riemann/03-research/phase-78-build-neutral-lp-and-ident/E78_137_mu_convergence_gate_results.json",
        "w",
    ) as f:
        json.dump(results, f, indent=2)
    print("WROTE JSON")


if __name__ == "__main__":
    run()
