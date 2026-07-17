#!/usr/bin/env python3
import sys
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
    return d, L, xi


def cauchy(t, d, xi):
    return float(np.sum(xi / (t - d)))


def pair_stats(t, d, xi):
    order = np.argsort(np.abs(d))
    terms = xi / (t - d)
    abs_sum = float(np.sum(np.abs(terms)))
    signed = float(np.sum(terms))
    top = sorted((abs(terms[i]), d[i], terms[i]) for i in order)[-5:]
    return signed, abs_sum, list(reversed(top))


def run():
    print("E73.124 CSV source probe")
    print("Compares C_x(-gamma) for zeta-coupled vector and arch/free vector.")
    print(" rel = |C_zeta|/|C_arch|; cancel = |sum terms|/sum |terms|.")
    print(" lam     L tau     gamma    zetaB    archB     relB zCancelB aCancelB")
    for lam, n_modes in [(16, 20), (20, 24), (24, 28), (28, 32), (32, 36)]:
        dz, L, xz = setup_vector(lam, n_modes, include_arith=True)
        da, _, xa = setup_vector(lam, n_modes, include_arith=False)
        for tau in [GAMMAS[0], GAMMAS[1]]:
            for gamma in sorted(list(GAMMAS[:12]), key=lambda g: (abs(g - tau), g))[:3]:
                t = -gamma
                z_signed, z_abs, _ = pair_stats(t, dz, xz)
                a_signed, a_abs, _ = pair_stats(t, da, xa)
                rel = abs(z_signed) / max(abs(a_signed), 1e-300)
                z_cancel = abs(z_signed) / max(z_abs, 1e-300)
                a_cancel = abs(a_signed) / max(a_abs, 1e-300)
                print(
                    f"{lam:4d} {L:7.3f} {tau:7.2f} {gamma:7.2f}"
                    f" {bexp(abs(z_signed), L):8.3f} {bexp(abs(a_signed), L):8.3f}"
                    f" {bexp(rel, L):8.3f} {bexp(z_cancel, L):8.3f}"
                    f" {bexp(a_cancel, L):8.3f}"
                )


if __name__ == "__main__":
    run()

