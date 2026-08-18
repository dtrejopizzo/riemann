#!/usr/bin/env python3
"""E78.144 gate: does the bottom-mode boundary coupling c_0^{(N)} stay bounded
away from 0 relative to nu_0^{(N)}, for both builds?

A_N = H[1:-1,1:-1] (inner block, NEVER the full bordered H).
b_N = H[1:-1, -1]   (boundary column, restricted to inner rows).
c_0^{(N)} = <u_0^{(N)}, b_N>, u_0 = ground eigenvector of A_N.
S_N(mu) = sum_j |<u_j,b_N>|^2 / (nu_j-mu)^2, computed directly (full sum, not
just bottom mode) for comparison.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
PHASE76 = Path("/Users/dt/riemann/03-research/phase-76-normalized-adjugate-arithmetic-lock")
sys.path.insert(0, str(PHASE76))

from P76_002_mp_entry_audit import build_mp  # noqa: E402

GAMMA = "14.134725141734693790"
BETA = "0.30"
STRENGTH = "5"


def norm(vector: mp.matrix) -> mp.mpf:
    return mp.sqrt(mp.fsum(abs(vector[j]) ** 2 for j in range(vector.rows)))


def gate_one(lam: int, L_idx: int, n_modes: int, dps: int, planted=None):
    """L_idx is a placeholder param name; build_mp determines L internally
    from lam via L=2log(lam). We vary lam-independent L by choosing lam per
    call as done throughout the ledger (lam fixed=6, this arg unused beyond
    passing to build_mp)."""
    H, idx, L = build_mp(lam, n_modes, dps, planted=planted)
    inner = H[1:-1, H.cols - 2]
    # inner block: rows/cols 1..(2N-1) exclusive of first/last -> use slicing
    A = H[1 : H.rows - 1, 1 : H.cols - 1]
    b = mp.matrix([H[i, H.cols - 1] for i in range(1, H.rows - 1)])
    vals, vecs = mp.eigsy(A)
    u0 = vecs[:, 0]
    c0 = (u0.T * b)[0]
    nu0 = vals[0]
    return {
        "L": mp.nstr(L, 12),
        "n_modes": n_modes,
        "dim_inner": A.rows,
        "nu0": mp.nstr(nu0, 30),
        "nu1": mp.nstr(vals[1], 30),
        "c0": mp.nstr(c0, 30),
        "b_norm": mp.nstr(norm(b), 30),
    }, vals, vecs, b, nu0, c0


def S_N_full(vals, vecs, b, mu):
    total = mp.mpf(0)
    bottom = None
    for j in range(vals.rows):
        vec = vecs[:, j]
        coeff = (vec.T * b)[0]
        term = abs(coeff) ** 2 / (vals[j] - mu) ** 2
        if j == 0:
            bottom = term
        total += term
    return total, bottom


def run(lam_val: int, dps: int, n_modes_list, planted=None, mu_for_S=None):
    rows = []
    for n_modes in n_modes_list:
        rec, vals, vecs, b, nu0, c0 = gate_one(lam_val, None, n_modes, dps, planted=planted)
        mu = mu_for_S if mu_for_S is not None else mp.mpf(0)
        S_total, S_bottom = S_N_full(vals, vecs, b, mu)
        rec["S_total_at_mu"] = mp.nstr(S_total, 20)
        rec["S_bottom_at_mu"] = mp.nstr(S_bottom, 20)
        rec["bottom_fraction_of_S"] = mp.nstr(S_bottom / S_total, 15) if S_total != 0 else "n/a"
        rec["c0_over_nu0"] = mp.nstr(abs(c0) / abs(nu0), 20)
        rec["c0sq_over_nu0sq"] = mp.nstr(abs(c0) ** 2 / abs(nu0) ** 2, 20)
        rows.append(rec)
        print(
            f"lam={lam_val} N={n_modes} dim={rec['dim_inner']} nu0={rec['nu0']} "
            f"c0={rec['c0']} c0/nu0={rec['c0_over_nu0']} "
            f"S_total={rec['S_total_at_mu']} S_bottom={rec['S_bottom_at_mu']} "
            f"bottom_frac={rec['bottom_fraction_of_S']}"
        )
    return rows


def main():
    dps = 70
    n_modes_list = [6, 8, 10, 12, 14, 16]
    results = {}

    print("=== ZETA build, lambda=6, mu=0 (exact mu_L for zeta branch B) ===")
    results["zeta_lambda6"] = run(6, dps, n_modes_list, planted=None, mu_for_S=mp.mpf(0))

    print("\n=== PLANTED build, lambda=6, gamma=14.13..., beta=.30, strength=5 ===")
    planted = (GAMMA, BETA, STRENGTH)
    # proxy mu_L for the plant: use largest-N nu0 value as finite-N proxy.
    # First pass to get nu0 at N=16.
    rec16, vals16, vecs16, b16, nu0_16, c0_16 = gate_one(6, None, 16, dps, planted=planted)
    mu_proxy = mp.mpf(rec16["nu0"])
    print(f"plant mu_L proxy (nu0 at N=16) = {mp.nstr(mu_proxy, 20)}")
    results["planted_lambda6"] = run(6, dps, n_modes_list, planted=planted, mu_for_S=mu_proxy)
    results["planted_mu_proxy"] = mp.nstr(mu_proxy, 30)

    out_path = HERE / "E78_144_c0_gate_results.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nWrote {out_path}")


if __name__ == "__main__":
    main()
