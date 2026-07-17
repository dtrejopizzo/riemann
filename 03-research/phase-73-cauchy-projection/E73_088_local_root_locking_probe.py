#!/usr/bin/env python3
import sys
import math
import numpy as np

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_069_exact_far3_row_probe import setup_exact, finite_roots, cauchy_real  # noqa: E402
from E73_077_pair_coefficient_budget_probe import bexp  # noqa: E402


def derivative_abs_bound(t0, root, d, xi):
    left = min(t0, root)
    right = max(t0, root)
    vals = []
    for t in [left, right, 0.5 * (left + right)]:
        vals.append(float(np.sum(np.abs(xi) / np.maximum(np.abs(t - d), 1e-300) ** 2)))
    return max(vals)


def local_window(tau, nwin):
    pool = list(GAMMAS[:12])
    return sorted(pool, key=lambda g: (abs(g - tau), g))[:nwin]


def run():
    print("E73.088 local root-locking probe")
    print("Tests |C(-gamma)| <= dist(-gamma,root)*sup |C'| on Zloc=tau-near.")
    print(" lam     L tau  gamma      distB     derB  boundB  actualB   ratio")
    for lam, n_modes in [(16, 20), (18, 22), (20, 24), (24, 28)]:
        d, L, xi, _ = setup_exact(lam, n_modes)
        roots = finite_roots(d, xi, hmax=60.0)
        for tau in [GAMMAS[0], GAMMAS[1]]:
            for gamma in local_window(tau, 3):
                t0 = -gamma
                root = roots[int(np.argmin(np.abs(roots - t0)))]
                dist = abs(t0 - root)
                dist_eff = max(dist, 1e-15)
                der = derivative_abs_bound(t0, root, d, xi)
                bound = dist_eff * der
                actual = abs(cauchy_real(t0, d, xi))
                ratio = actual / max(bound, 1e-300)
                print(
                    f"{lam:4d} {L:7.3f} {tau:7.2f} {gamma:7.2f}"
                    f" {bexp(dist, L):9.3f} {bexp(der, L):8.3f}"
                    f" {bexp(bound, L):8.3f} {bexp(actual, L):8.3f}"
                    f" {ratio:8.3f}"
                )


if __name__ == "__main__":
    run()
