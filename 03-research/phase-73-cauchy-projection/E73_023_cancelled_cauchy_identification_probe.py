#!/usr/bin/env python3
import sys
import cmath
import numpy as np
from numpy.linalg import eigh, norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E71_9_relative_arch_background_probe import build  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS, g_cancelled  # noqa: E402


def setup_full(lam, n_modes):
    h_actual, idx, L = build(lam, n_modes, include_arith=True)
    vals, vecs = eigh(h_actual)
    xi = vecs[:, 0]
    xi = (xi + xi[::-1]) / 2.0
    xi = xi / norm(xi)
    d = 2.0 * np.pi * idx / L
    return idx.astype(int), d, L, xi


def rational_dual_atom(gamma, d, xi, L):
    c_gamma = cmath.exp(1j * gamma * L) - 1.0
    return c_gamma * np.sum(np.conjugate(xi) / (gamma + d))


def run():
    print("E73.023 cancelled Cauchy identification probe")
    print("Compares E73 atom A_gamma with E72 g_cancelled(i gamma).")
    print(" lam     L      gamma       |A|          |G|          |A-G|       |A+G|")
    for lam, n_modes in [(8, 12), (10, 14), (12, 16), (14, 18), (16, 20), (18, 22)]:
        idx, d, L, xi = setup_full(lam, n_modes)
        for gamma in GAMMAS[:4]:
            atom = rational_dual_atom(gamma, d, xi, L)
            gval = g_cancelled(1j * gamma, d, xi, L)
            print(
                f"{lam:4d} {L:7.3f} {gamma:10.6f} "
                f"{abs(atom):11.3e} {abs(gval):11.3e} "
                f"{abs(atom - gval):11.2e} {abs(atom + gval):11.2e}"
            )


if __name__ == "__main__":
    run()
