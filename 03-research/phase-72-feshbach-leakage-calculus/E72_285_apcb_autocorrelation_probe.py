#!/usr/bin/env python3
import sys

import numpy as np
from numpy.linalg import eigvalsh

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
from E71_9_relative_arch_background_probe import primes_upto  # noqa: E402

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_158_prime_cell_psd_probe import q_matrix  # noqa: E402
from E72_262_pole_relative_even_setup_audit import pole_relative_even_setup_pair  # noqa: E402


def prime_weights(lam, L):
    weights = []
    maxn = int(lam * lam)
    for p in primes_upto(maxn):
        lp = np.log(p)
        pm = p
        me = 1
        while pm <= maxn:
            y = me * lp
            weights.append((pm, lp * (pm ** -0.5), y))
            if pm > maxn // p:
                break
            pm *= p
            me += 1
    return weights


def apcb_profile(lam, n_modes):
    idx, L, xi, eb, c_actual, c_model, e_pole, odd_norm, even_leak = pole_relative_even_setup_pair(lam, n_modes)
    delta = c_actual - c_model
    vals = eigvalsh(delta)
    pos = max(float(vals[-1]), 0.0)
    neg = min(float(vals[0]), 0.0)

    weights = prime_weights(lam, L)
    incoh = 2.0 * sum(w for _, w, _ in weights)

    # Rebuild Delta from the autocorrelation cells to verify the exact finite form.
    rebuilt = np.zeros_like(delta)
    for _, weight, y in weights:
        rebuilt += eb.T @ (-weight * q_matrix(idx, L, y)) @ eb
    err = np.linalg.norm(rebuilt - delta) / max(np.linalg.norm(delta), 1e-30)
    return L, delta.shape[0], len(weights), pos, neg, max(abs(vals[0]), abs(vals[-1])), incoh, err


def run():
    print("E72.285 APCB autocorrelation probe")
    print("Delta_arith=-sum Lambda(n)n^-1/2 Q_log n; APCB asks lambda_max(Delta_arith)_+=O(L^2).")
    print("incoh=2 sum Lambda(n)n^-1/2 is the absolute autocorrelation ceiling.")
    print("lam L dim cells posDelta/L2 negDelta/L2 absDelta/L2 incoh/L2 rebuildRel")
    for lam, n_modes in [(16, 40), (20, 48), (24, 56), (28, 64), (32, 72)]:
        L, dim, cells, pos, neg, abs_delta, incoh, err = apcb_profile(lam, n_modes)
        L2 = L * L
        print(
            f"{lam:3.0f} {L:.6f} {dim:3d} {cells:5d} "
            f"{pos / L2:.6e} {neg / L2:.6e} {abs_delta / L2:.6e} "
            f"{incoh / L2:.6e} {err:.3e}",
            flush=True,
        )


if __name__ == "__main__":
    run()
