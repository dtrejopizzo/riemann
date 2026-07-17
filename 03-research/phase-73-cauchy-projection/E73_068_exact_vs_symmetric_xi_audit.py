#!/usr/bin/env python3
import sys
import math
import numpy as np
from numpy.linalg import eigh, norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")

from E71_9_relative_arch_background_probe import build  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402


def bexp(value, L):
    if value <= 0:
        return float("-inf")
    return math.log(value) / math.log(L)


def setup(lam, n_modes):
    h_actual, idx, L = build(lam, n_modes, include_arith=True)
    vals, vecs = eigh(h_actual)
    xi_exact = vecs[:, 0]
    if xi_exact[len(xi_exact) // 2] < 0:
        xi_exact = -xi_exact
    xi_sym = (xi_exact + xi_exact[::-1]) / 2.0
    xi_sym = xi_sym / norm(xi_sym)
    d = 2.0 * np.pi * idx / L
    e = h_actual - vals[0] * np.eye(len(idx))
    return d, L, e, xi_exact, xi_sym


def run():
    print("E73.068 exact-vs-symmetric xi audit")
    print("The projection lemma uses the exact eigenvector; symmetric xi is only a gauge.")
    print(" lam     L    ||Ex||B ||Esym||B  gamma exactB   symB    diffB")
    for lam, n_modes in [(16, 20), (18, 22), (20, 24), (24, 28)]:
        d, L, e, xi_exact, xi_sym = setup(lam, n_modes)
        ex = norm(e @ xi_exact)
        es = norm(e @ xi_sym)
        for gamma in GAMMAS[:3]:
            t = -gamma
            krow = 1.0 / (t - d)
            exact = abs(np.dot(krow, xi_exact))
            sym = abs(np.dot(krow, xi_sym))
            diff = abs(exact - sym)
            print(
                f"{lam:4d} {L:7.3f} {bexp(ex, L):9.3f} {bexp(es, L):9.3f}"
                f" {gamma:7.2f} {bexp(exact, L):7.3f} {bexp(sym, L):7.3f}"
                f" {bexp(diff, L):8.3f}"
            )


if __name__ == "__main__":
    run()
