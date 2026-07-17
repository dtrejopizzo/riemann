#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import norm, solve

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_79_bordered_minor_probe import finite_roots  # noqa: E402
from E72_112_operator_split_probe import lk_matrix, sigma_packet, weighted_even_matrix  # noqa: E402


def run():
    print("E72.132 mass source bound probe")
    print(" lam   L roots  ||b||  max||cpm||  ||b||||cpm||  massBound  actualMass")
    for lam, n_modes in [(6, 18), (8, 24), (10, 28), (12, 32), (14, 36), (16, 40)]:
        idx, L, d, xi, k, bq, c_actual, _ = setup_pair(lam, n_modes)
        roots = finite_roots(xi, d, hmax=6.0)
        if len(roots) == 0:
            continue
        mask = (np.abs(d) <= 8.0).astype(float)
        w = weighted_even_matrix(idx, mask)
        mass_full = mask * (w.T @ np.ones(w.shape[0], dtype=complex))
        b = bq.T @ mass_full
        lk = lk_matrix(d, k)
        factor = 2.0 / (L * np.sqrt(np.exp(L)))
        cinv_b_norm = norm(solve(c_actual, b))
        max_c = 0.0
        max_bound = 0.0
        max_actual = 0.0
        for tau in roots[:6]:
            y = sigma_packet(L, d, tau)
            zpm = factor * (lk @ y)
            cpm = bq.T @ (mask * zpm)
            actual = abs(np.vdot(b, solve(c_actual, cpm)))
            bound = cinv_b_norm * norm(cpm)
            max_c = max(max_c, norm(cpm))
            max_bound = max(max_bound, bound)
            max_actual = max(max_actual, actual)
        print(
            f"{lam:4.0f} {L:5.2f} {len(roots):5d} "
            f"{norm(b):6.2e} {max_c:10.3e} {norm(b)*max_c:13.3e} "
            f"{max_bound:9.3e} {max_actual:10.3e}"
        )


if __name__ == "__main__":
    run()
