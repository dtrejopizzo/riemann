#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_165_fixed_cut_stress_probe import two_blocks  # noqa: E402
from E72_181_chebyshev_abs_schedule_probe import signed_coeff, eval_cheb_matrix_scaled, theoretical_error_sum  # noqa: E402
from E72_182_adaptive_margin_probe import even_degree_for_margin  # noqa: E402


WINDOWS = [(12, 32), (16, 40), (20, 48), (24, 56), (28, 64), (32, 72)]
CUTS = [0.55, 0.60, 0.65]


def prepare():
    rows = []
    for lam, n_modes in WINDOWS:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        rows.append((lam, L, idx, bq, c_model))
        print(f"prepared lambda={lam:.0f}", flush=True)
    return rows


def cross_for(prepared_row, cut, margin=0.05):
    lam, L, idx, bq, c_model = prepared_row
    k0, k1 = two_blocks(lam, idx, L, bq, c_model, cut)
    degree = even_degree_for_margin(k0.shape[0], margin)
    n_terms = degree // 2
    c0 = signed_coeff(0.70, 0.90, n_terms)
    c1 = signed_coeff(0.60, 0.60, n_terms)
    g0 = eval_cheb_matrix_scaled(k0, c0, 0.90)
    g1 = eval_cheb_matrix_scaled(k1, c1, 0.60)
    g0sq = float(np.trace(g0 @ g0))
    g1sq = float(np.trace(g1 @ g1))
    cross = float(2.0 * np.trace(g0 @ g1))
    eps = np.sqrt(k0.shape[0]) * theoretical_error_sum(n_terms)
    final = np.sqrt(max(g0sq + g1sq + cross, 0.0)) + eps
    return L, cross, g0sq + g1sq, final


def run():
    print("E72.187 XNEG cut-robustness probe")
    print("reports cross=2Tr(G0G1); negative supports XNEG")
    print("cut  maxCross  worstFinal  per-window")
    prepared = prepare()
    for cut in CUTS:
        max_cross = -np.inf
        worst_final = 0.0
        parts = []
        for row_data in prepared:
            lam = row_data[0]
            L, cross, diag, final = cross_for(row_data, cut)
            max_cross = max(max_cross, cross)
            worst_final = max(worst_final, final)
            parts.append(f"{int(lam)}:{cross:+.3f}")
        print(
            f"{cut:3.2f} {max_cross:+8.3f} {worst_final:10.3f} "
            + " ".join(parts),
            flush=True,
        )


if __name__ == "__main__":
    run()
