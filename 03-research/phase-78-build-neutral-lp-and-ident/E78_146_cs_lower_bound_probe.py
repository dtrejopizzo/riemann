#!/usr/bin/env python3
"""E78.146 - Cauchy-Schwarz finite witness for BTG-DIV-L.

Idea (finite-witness reframing of E78.145's open c_0 gap):

  BTG-DIV-L at mu_L=0 is   S_N(0) = sum_j c_j^2 / nu_j^2 -> infinity,
  and S_N(0) = || A_N^{-1} b_N ||^2  (exact, no eigendecomposition).

  Cauchy-Schwarz lower bound, sign-free and eigendecomposition-free:

      S_N(0) = sum_j c_j^2/nu_j^2
             >= (sum_j c_j^2)^2 / (sum_j c_j^2 nu_j^2)
             =  ||b_N||^4 / ||A_N b_N||^2                       (CS-LB)

  If CS-LB -> infinity, BTG-DIV-L is PROVED (zeta, mu_L=0) with an elementary
  finite witness that never isolates c_0 or u_0 (sidesteps E78.145 sec 5).

We measure, per N and per build:
  - ||b_N||, ||A_N b_N||, CS-LB = ||b_N||^4 / ||A_N b_N||^2
  - the TRUE S_N(0) = ||A_N^{-1} b_N||^2 via linear solve (for comparison /
    to see how lossy CS is)
  - the ratio S_true / CS-LB (>=1 always; how much slack CS leaves)

Inner block convention: A_N = H[1:-1,1:-1], b_N = H[1:-1, -1] (boundary col
restricted to inner rows). Matches E78.145 sec 1 exactly.

zeta uses mu_L = 0 exactly. plant has no closed-form mu_L; CS-LB and S_true
are evaluated at mu=0 too (the plant does not collapse to 0, so both are
expected to stay bounded for the plant -- that is the Outcome-A contrast,
NOT the target).
"""

import json
import sys
import time

import mpmath as mp

sys.path.insert(0, "/Users/dt/riemann/03-research/phase-76-normalized-adjugate-arithmetic-lock")
from P76_002_mp_entry_audit import build_mp, vec_norm

PLANTED = ("14.134725141734693790", "0.30", "5.0")
LAM = 6


def run_one(n_modes, dps, planted=None):
    mp.mp.dps = dps
    H, idx, L = build_mp(mp.mpf(LAM), n_modes, dps, planted=planted)
    A = H[1:-1, 1:-1]
    b = H[1:-1, -1]  # boundary column, inner rows
    nb = vec_norm(b)
    Ab = A * b
    nAb = vec_norm(Ab)
    cs_lb = (nb**4) / (nAb**2)
    # true S_N(0) = ||A^{-1} b||^2 via linear solve A w = b
    w = mp.lu_solve(A, b)
    nw = vec_norm(w)
    s_true = nw**2
    return {
        "N": n_modes,
        "dim_inner": A.rows,
        "dps": dps,
        "norm_b": mp.nstr(nb, 15),
        "norm_Ab": mp.nstr(nAb, 15),
        "cs_lb": mp.nstr(cs_lb, 15),
        "s_true": mp.nstr(s_true, 15),
        "slack_ratio": mp.nstr(s_true / cs_lb, 8),
    }


def main():
    dps = 70
    Ns = [6, 8, 10, 12, 14, 16, 18]
    results = {"zeta": [], "planted": []}
    t0 = time.time()
    for N in Ns:
        rz = run_one(N, dps, planted=None)
        results["zeta"].append(rz)
        print("zeta N=%2d  cs_lb=%s  s_true=%s  slack=%s  t=%.1f"
              % (N, rz["cs_lb"], rz["s_true"], rz["slack_ratio"], time.time() - t0),
              flush=True)
        rp = run_one(N, dps, planted=PLANTED)
        results["planted"].append(rp)
        print("plant N=%2d cs_lb=%s  s_true=%s  slack=%s  t=%.1f"
              % (N, rp["cs_lb"], rp["s_true"], rp["slack_ratio"], time.time() - t0),
              flush=True)
    with open(
        "/Users/dt/riemann/03-research/phase-78-build-neutral-lp-and-ident/E78_146_cs_lower_bound_results.json",
        "w",
    ) as f:
        json.dump(results, f, indent=2)


if __name__ == "__main__":
    main()
