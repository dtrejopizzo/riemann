#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_165_fixed_cut_stress_probe import two_blocks  # noqa: E402
from E72_181_chebyshev_abs_schedule_probe import signed_coeff, eval_cheb_matrix_scaled, theoretical_error_sum  # noqa: E402
from E72_182_adaptive_margin_probe import even_degree_for_margin  # noqa: E402


WINDOWS = [
    (12, 32),
    (16, 40),
    (20, 48),
    (24, 56),
    (28, 64),
    (32, 72),
    (34, 76),
    (36, 80),
]


def run(margin=0.05):
    print("E72.186 G-cycle block decomposition probe")
    print("G=g0(K0)+g1(K1); reports Tr(G0^2), Tr(G1^2), 2Tr(G0G1)")
    print(" lam    L dim   D   G0sq   G1sq   cross     G2  crossFrac final")
    for lam, n_modes in WINDOWS:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        k0, k1 = two_blocks(lam, idx, L, bq, c_model, 0.60)
        degree = even_degree_for_margin(k0.shape[0], margin)
        n_terms = degree // 2
        c0 = signed_coeff(0.70, 0.90, n_terms)
        c1 = signed_coeff(0.60, 0.60, n_terms)
        g0 = eval_cheb_matrix_scaled(k0, c0, 0.90)
        g1 = eval_cheb_matrix_scaled(k1, c1, 0.60)
        g0sq = float(np.trace(g0 @ g0))
        g1sq = float(np.trace(g1 @ g1))
        cross = float(2.0 * np.trace(g0 @ g1))
        g2 = g0sq + g1sq + cross
        eps = np.sqrt(k0.shape[0]) * theoretical_error_sum(n_terms)
        cross_frac = cross / max(g0sq + g1sq, 1e-30)
        print(
            f"{lam:4.0f} {L:5.2f} {k0.shape[0]:3d} {degree:3d} "
            f"{g0sq:6.3f} {g1sq:6.3f} {cross:8.3f} "
            f"{g2:6.3f} {cross_frac:9.3f} {np.sqrt(max(g2,0.0))+eps:6.3f}",
            flush=True,
        )


if __name__ == "__main__":
    run()
