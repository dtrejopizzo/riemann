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
    print("E73.032 DATA-HERM probe")
    print("Hermite projection of actual cancelled Cauchy critical data.")
    print(" lam     L  sigma      t   m nK      geomAbs      dataHerm      weighted   gain")
    for lam, n_modes in [(8, 12), (10, 14), (12, 16), (14, 18), (16, 20), (18, 22)]:
        d, L, xi = setup_full(lam, n_modes)
        crit_nodes = [1j * g for g in GAMMAS[:6]]
        data = np.array([g_cancelled(k, d, xi, L) for k in crit_nodes], dtype=complex)
        for sigma, t in [(0.05, GAMMAS[0]), (0.10, GAMMAS[0]), (0.20, GAMMAS[0]), (0.20, GAMMAS[1])]:
            for m in [1, 2, 3]:
                a = sigma + 1j * t
                coeff_mat = np.column_stack([hcoeff_for_k(a, k, m) for k in crit_nodes])
                out = coeff_mat @ data
                geom_abs = abs(cmath.exp(sigma * L)) * sum(hermite_norm(coeff_mat[:, j]) for j in range(len(crit_nodes)))
                data_herm = hermite_norm(out)
                weighted = abs(cmath.exp(sigma * L)) * data_herm
                data_max = max(abs(x) for x in data)
                ceiling = geom_abs * data_max
                gain = weighted / max(ceiling, 1e-300)
                print(
                    f"{lam:4d} {L:7.3f} {sigma:6.2f} {t:7.2f} {m:3d} {len(crit_nodes):2d} "
                    f"{geom_abs:12.3e} {data_herm:12.3e} {weighted:10.3e} {gain:8.2e}"
                )


if __name__ == "__main__":
    run()
