#!/usr/bin/env python3
import sys
import math
import numpy as np
from numpy.linalg import eigh, norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E71_9_relative_arch_background_probe import build  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_077_pair_coefficient_budget_probe import bexp  # noqa: E402


def setup_vector(lam, n_modes, include_arith):
    h, idx, L = build(lam, n_modes, include_arith=include_arith)
    vals, vecs = eigh(h)
    xi = vecs[:, 0]
    xi = (xi + xi[::-1]) / 2.0
    xi = xi / norm(xi)
    if xi[len(xi) // 2] < 0:
        xi = -xi
    d = 2.0 * np.pi * idx / L
    return h, vals[0], d, L, xi


def cauchy(t, d, xi):
    return float(np.sum(xi / (t - d)))


def run():
    print("E73.130 vector-swap CSV probe")
    print("Compares C_zeta, C_arch, and C_delta= C_zeta-C_arch from vector change.")
    print(" lam     L gamma      zetaB    archB   deltaB  z/a angle")
    for lam, n_modes in [(16, 20), (20, 24), (24, 28), (28, 32), (32, 36)]:
        _, _, dz, L, xz = setup_vector(lam, n_modes, include_arith=True)
        _, _, da, _, xa = setup_vector(lam, n_modes, include_arith=False)
        # Same pole mesh because lambda,N are identical; keep assertion soft.
        mesh_err = float(np.max(np.abs(dz - da)))
        if mesh_err > 1e-12:
            raise RuntimeError("mesh mismatch")
        for gamma in GAMMAS[:3]:
            t = -gamma
            cz = cauchy(t, dz, xz)
            ca = cauchy(t, dz, xa)
            cd = cauchy(t, dz, xz - xa)
            ratio = abs(cz) / max(abs(ca), 1e-300)
            # Cancellation angle proxy: |arch+delta|/(|arch|+|delta|)
            cancel = abs(cz) / max(abs(ca) + abs(cd), 1e-300)
            print(
                f"{lam:4d} {L:7.3f} {gamma:7.2f}"
                f" {bexp(abs(cz), L):9.3f} {bexp(abs(ca), L):8.3f}"
                f" {bexp(abs(cd), L):8.3f} {bexp(ratio, L):6.2f}"
                f" {bexp(cancel, L):7.3f}"
            )


if __name__ == "__main__":
    run()

