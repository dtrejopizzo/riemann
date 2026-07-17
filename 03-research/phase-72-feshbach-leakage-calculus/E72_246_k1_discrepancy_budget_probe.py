#!/usr/bin/env python3
import sys

import numpy as np
from numpy.linalg import cholesky, solve

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
from E71_9_relative_arch_background_probe import primes_upto  # noqa: E402

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_197_signed_green_word_probe import u_matrix  # noqa: E402
from E72_232_low_edge_subspace_probe import subspace_coords  # noqa: E402


WINDOWS = [(12, 32), (16, 40), (20, 48), (24, 56), (28, 64), (32, 72), (36, 80)]
GRID = np.linspace(0.6001, 0.999, 801)


def rel_m(idx, L, bq, chol, u):
    raw = bq.T @ u_matrix(idx, L, u * L) @ bq
    x = solve(chol, raw)
    rel = solve(chol, x.T).T
    return 0.5 * (rel + rel.conj().T)


def high_prime_average(lam, L, k1_func):
    maxn = int(lam * lam)
    total = 0.0
    mass = 0.0
    for p in primes_upto(maxn):
        lp = np.log(p)
        pm = p
        while pm <= maxn:
            u = np.log(pm) / L
            if u > 0.60:
                beta = lp * pm ** -0.5
                total += beta * k1_func(u)
                mass += beta
            if pm > maxn // p:
                break
            pm *= p
    return total / mass


def run():
    print("E72.246 K1 discrepancy budget probe")
    print("TV is total variation on grid; disc=primeAvg-contAvg.")
    print("lam contAvg primeAvg disc relDisc TV disc/TV margin/TV supSlope")
    for lam, n_modes in WINDOWS:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        chol = cholesky(c_model)
        p = subspace_coords(idx, k, bq, [0, 1])

        def k1_func(u):
            m = rel_m(idx, L, bq, chol, float(u))
            g = p.conj().T @ m @ p
            return float(np.trace(g).real)

        vals = np.array([k1_func(u) for u in GRID])
        cont = float(np.trapezoid(vals, GRID) / (GRID[-1] - GRID[0]))
        prime = high_prime_average(lam, L, k1_func)
        disc = prime - cont
        tv = float(np.sum(np.abs(np.diff(vals))))
        slopes = np.abs(np.diff(vals) / np.diff(GRID))
        sup_slope = float(slopes.max())
        print(
            f"{lam:3.0f} {cont:+.6e} {prime:+.6e} {disc:+.6e} "
            f"{disc/max(abs(cont),1e-300):+.3f} {tv:.6e} "
            f"{abs(disc)/max(tv,1e-300):.3f} {prime/max(tv,1e-300):.3f} "
            f"{sup_slope:.6e}",
            flush=True,
        )


if __name__ == "__main__":
    run()
