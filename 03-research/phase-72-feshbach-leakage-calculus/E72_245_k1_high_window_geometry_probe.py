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
GRID = np.linspace(0.6001, 0.999, 401)


def rel_m(idx, L, bq, chol, u):
    raw = bq.T @ u_matrix(idx, L, u * L) @ bq
    x = solve(chol, raw)
    rel = solve(chol, x.T).T
    return 0.5 * (rel + rel.conj().T)


def high_prime_average(lam, L, k1_func):
    maxn = int(lam * lam)
    total = 0.0
    mass = 0.0
    count = 0
    for p in primes_upto(maxn):
        lp = np.log(p)
        pm = p
        while pm <= maxn:
            u = np.log(pm) / L
            if u > 0.60:
                beta = lp * pm ** -0.5
                total += beta * k1_func(u)
                mass += beta
                count += 1
            if pm > maxn // p:
                break
            pm *= p
    return total, mass, count


def run():
    print("E72.245 K1 high-window geometry probe")
    print("K1(u)=Tr(P M_u P). primeAvg=sum beta K1 / sum beta; sumBetaK1=-tB.")
    print("lam minK1 maxK1 meanK1 negFrac intK1 sumBetaK1 primeAvg mass count")
    for lam, n_modes in WINDOWS:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        chol = cholesky(c_model)
        p = subspace_coords(idx, k, bq, [0, 1])

        def k1_func(u):
            m = rel_m(idx, L, bq, chol, float(u))
            g = p.conj().T @ m @ p
            return float(np.trace(g).real)

        vals = np.array([k1_func(u) for u in GRID])
        int_k1 = float(np.trapezoid(vals, GRID) / (GRID[-1] - GRID[0]))
        sum_beta_k1, mass, count = high_prime_average(lam, L, k1_func)
        prime_avg = sum_beta_k1 / mass
        print(
            f"{lam:3.0f} {vals.min():+.6e} {vals.max():+.6e} "
            f"{vals.mean():+.6e} {np.mean(vals < 0.0):.3f} {int_k1:+.6e} "
            f"{sum_beta_k1:+.6e} {prime_avg:+.6e} {mass:.6e} {count:5d}",
            flush=True,
        )


if __name__ == "__main__":
    run()
