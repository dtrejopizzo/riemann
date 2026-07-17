#!/usr/bin/env python3
import sys
import numpy as np

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_165_fixed_cut_stress_probe import two_blocks  # noqa: E402
from E72_181_chebyshev_abs_schedule_probe import signed_coeff, eval_cheb_matrix_scaled  # noqa: E402
from E72_182_adaptive_margin_probe import even_degree_for_margin  # noqa: E402


WINDOWS = [(12, 32), (16, 40), (20, 48), (24, 56), (28, 64), (32, 72), (36, 80)]
DEGREES = [2, 4, 8, 16, "auto"]


def cross_for(k0, k1, degree):
    if degree == "auto":
        degree = even_degree_for_margin(k0.shape[0], 0.03)
    n_terms = max(1, int(degree) // 2)
    c0 = signed_coeff(0.70, 0.90, n_terms)
    c1 = signed_coeff(0.60, 0.60, n_terms)
    g0 = eval_cheb_matrix_scaled(k0, c0, 0.90)
    g1 = eval_cheb_matrix_scaled(k1, c1, 0.60)
    return float(2.0 * np.trace(g0 @ g1))


def run():
    print("E72.194 XNEG degree probe")
    print("reports cross=2Tr(G0G1) for fixed degrees and adaptive degree")
    print(" lam    L dim " + " ".join(f"D{d:>5}" for d in DEGREES))
    max_by_degree = {d: -np.inf for d in DEGREES}
    for lam, n_modes in WINDOWS:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        k0, k1 = two_blocks(lam, idx, L, bq, c_model, 0.60)
        vals = []
        for degree in DEGREES:
            cross = cross_for(k0, k1, degree)
            max_by_degree[degree] = max(max_by_degree[degree], cross)
            vals.append(cross)
        print(
            f"{lam:4.0f} {L:5.2f} {k0.shape[0]:3d} "
            + " ".join(f"{v:+7.3f}" for v in vals),
            flush=True,
        )
    print("maxCross " + " ".join(f"D{d}:{max_by_degree[d]:+.3f}" for d in DEGREES))


if __name__ == "__main__":
    run()
