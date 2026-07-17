#!/usr/bin/env python3
import sys
import cmath
import math
import numpy as np
from numpy.linalg import eigh, norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")

from E71_9_relative_arch_background_probe import build  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS, g_cancelled  # noqa: E402


def setup_full(lam, n_modes):
    h_actual, idx, L = build(lam, n_modes, include_arith=True)
    vals, vecs = eigh(h_actual)
    xi = vecs[:, 0]
    xi = (xi + xi[::-1]) / 2.0
    xi = xi / norm(xi)
    d = 2.0 * np.pi * idx / L
    return d, L, xi


def confluent_matrix(a, m):
    mat = np.zeros((m, m), dtype=complex)
    for q in range(m):
        for p in range(m):
            mat[q, p] = ((-1) ** q) * math.comb(p + q, p) / ((2 * a) ** (p + q + 1))
    return mat


def qjet_coeff(a, k, m):
    return np.array([((-1) ** q) / ((a + k) ** (q + 1)) for q in range(m)], dtype=complex)


def hcoeff_for_k(a, k, m):
    return np.linalg.solve(confluent_matrix(a, m), qjet_coeff(a, k, m))


def hermite_norm(vec):
    return sum(abs(c) / math.factorial(i) for i, c in enumerate(vec))


def run():
    print("E73.033 DATA-HERM decomposition probe")
    print("Separates individual-smallness from signed Hermite cancellation.")
    print(" lam     L sigma      t  m  nK    maxData    l1Data    outNorm  l1Ratio  maxRatio")
    for lam, n_modes in [(8, 12), (10, 14), (12, 16), (14, 18), (16, 20), (18, 22), (20, 24)]:
        d, L, xi = setup_full(lam, n_modes)
        for nK in [3, 4, 5, 6]:
            crit_nodes = [1j * g for g in GAMMAS[:nK]]
            data = np.array([g_cancelled(k, d, xi, L) for k in crit_nodes], dtype=complex)
            for sigma, t, m in [(0.20, GAMMAS[0], 1), (0.20, GAMMAS[0], 2), (0.20, GAMMAS[0], 3)]:
                a = sigma + 1j * t
                coeff_mat = np.column_stack([hcoeff_for_k(a, k, m) for k in crit_nodes])
                out = coeff_mat @ data
                out_norm = hermite_norm(out)
                l1_ceiling = sum(hermite_norm(coeff_mat[:, j]) * abs(data[j]) for j in range(nK))
                max_ceiling = max(abs(data)) * sum(hermite_norm(coeff_mat[:, j]) for j in range(nK))
                print(
                    f"{lam:4d} {L:7.3f} {sigma:5.2f} {t:7.2f} {m:2d} {nK:3d} "
                    f"{max(abs(x) for x in data):10.3e} {sum(abs(x) for x in data):10.3e} "
                    f"{out_norm:9.3e} {out_norm/max(l1_ceiling,1e-300):8.2e} "
                    f"{out_norm/max(max_ceiling,1e-300):8.2e}"
                )


if __name__ == "__main__":
    run()
