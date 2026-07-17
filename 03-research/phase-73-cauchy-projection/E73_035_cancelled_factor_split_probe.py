#!/usr/bin/env python3
import sys
import cmath
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


def cauchy_at_gamma(gamma, d, xi):
    # g_cancelled(i gamma)=(1-exp(i gamma L))*sum xi/(-gamma-d)
    return np.sum(xi / (-gamma - d))


def run():
    print("E73.035 cancelled factor split probe")
    print("Splits |g_cancelled| into mesh multiplier and raw Cauchy value.")
    print(" lam     L   gamma      |1-exp|       |Craw|      |g|       phaseDist")
    for lam, n_modes in [(8, 12), (10, 14), (12, 16), (14, 18), (16, 20), (18, 22), (20, 24), (24, 28)]:
        d, L, xi = setup_full(lam, n_modes)
        for gamma in GAMMAS[:5]:
            mult = abs(1.0 - cmath.exp(1j * gamma * L))
            craw = abs(cauchy_at_gamma(gamma, d, xi))
            gval = abs(g_cancelled(1j * gamma, d, xi, L))
            phase = abs(((gamma * L + np.pi) % (2 * np.pi)) - np.pi)
            phase_dist = min(phase, abs(2 * np.pi - phase))
            print(
                f"{lam:4d} {L:7.3f} {gamma:9.3f} {mult:12.3e} "
                f"{craw:11.3e} {gval:10.3e} {phase_dist:12.3e}"
            )


if __name__ == "__main__":
    run()
