#!/usr/bin/env python3
import sys
import cmath
import numpy as np
from numpy.linalg import eigh, norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E71_9_relative_arch_background_probe import build  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_003_critical_source_probe import dd_kernel, pi_kernel  # noqa: E402


def setup_full(lam, n_modes):
    h_actual, idx, L = build(lam, n_modes, include_arith=True)
    vals, vecs = eigh(h_actual)
    xi = vecs[:, 0]
    xi = (xi + xi[::-1]) / 2.0
    xi = xi / norm(xi)
    d = 2.0 * np.pi * idx / L
    return idx.astype(int), d, L, xi


def source_vector(b, off_nodes, crit_nodes, d, L):
    total = np.zeros_like(d, dtype=complex)
    for k in crit_nodes:
        gamma = (-1j * k).real
        coeff = pi_kernel(b, k, off_nodes)
        total += coeff * np.array([dd_kernel(-gamma, dm, L) for dm in d], dtype=complex)
    return total


def scalar_formula(b, off_nodes, crit_nodes, d, xi, L):
    total = 0j
    for k in crit_nodes:
        gamma = (-1j * k).real
        c_gamma = cmath.exp(1j * gamma * L) - 1.0
        cauchy = np.sum(np.conjugate(xi) / (gamma + d))
        total += pi_kernel(b, k, off_nodes) * c_gamma * cauchy
    return total


def run():
    print("E73.022 scalar dual formula probe")
    print("Compares <xi,S_b> by direct mesh source and rational Cauchy scalar formula.")
    print(" lam     L       |direct|    |formula|      absErr     expWeighted")
    off_nodes = [0.20 + 1j * GAMMAS[0], 0.20 - 1j * GAMMAS[0], 0.20 + 1j * GAMMAS[1]]
    crit_nodes = [1j * g for g in GAMMAS[:5]]
    for lam, n_modes in [(8, 12), (10, 14), (12, 16), (14, 18), (16, 20), (18, 22)]:
        idx, d, L, xi = setup_full(lam, n_modes)
        for b in off_nodes:
            src = source_vector(b, off_nodes, crit_nodes, d, L)
            direct = np.vdot(xi, src)
            formula = scalar_formula(b, off_nodes, crit_nodes, d, xi, L)
            err = abs(direct - formula)
            weighted = abs(cmath.exp(b.real * L) * formula)
            print(
                f"{lam:4d} {L:7.3f} {abs(direct):12.3e} {abs(formula):12.3e} "
                f"{err:10.2e} {weighted:13.3e}"
            )


if __name__ == "__main__":
    run()
