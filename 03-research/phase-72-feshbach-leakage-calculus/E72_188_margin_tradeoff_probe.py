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
MARGINS = [0.05, 0.04, 0.03, 0.02]


def prepare():
    rows = []
    for lam, n_modes in WINDOWS:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        k0, k1 = two_blocks(lam, idx, L, bq, c_model, 0.60)
        rows.append((lam, L, k0, k1))
        print(f"prepared lambda={lam:.0f}", flush=True)
    return rows


def evaluate(rows, margin):
    worst_final = (0.0, None)
    worst_gnorm = (0.0, None)
    max_degree = 0
    parts = []
    for lam, L, k0, k1 in rows:
        degree = even_degree_for_margin(k0.shape[0], margin)
        max_degree = max(max_degree, degree)
        n_terms = degree // 2
        c0 = signed_coeff(0.70, 0.90, n_terms)
        c1 = signed_coeff(0.60, 0.60, n_terms)
        eps = np.sqrt(k0.shape[0]) * theoretical_error_sum(n_terms)
        g = eval_cheb_matrix_scaled(k0, c0, 0.90) + eval_cheb_matrix_scaled(k1, c1, 0.60)
        gnorm = norm(g, "fro")
        final = gnorm + eps
        if final > worst_final[0]:
            worst_final = (final, lam)
        if gnorm > worst_gnorm[0]:
            worst_gnorm = (gnorm, lam)
        parts.append(f"{int(lam)}:{gnorm:.3f}+{eps:.3f}")
    target = 1.0 - margin
    return max_degree, worst_gnorm, worst_final, target, parts


def run():
    print("E72.188 ASRP margin tradeoff probe")
    print("entries are ||G||+eps; target is ||G||<1-m and final<1")
    rows = prepare()
    print(" m*  maxD  worstG@lam  target  worstFinal@lam  per-window")
    for margin in MARGINS:
        max_degree, worst_g, worst_f, target, parts = evaluate(rows, margin)
        print(
            f"{margin:4.2f} {max_degree:5d} "
            f"{worst_g[0]:6.3f}@{int(worst_g[1]):02d} "
            f"{target:6.3f} "
            f"{worst_f[0]:6.3f}@{int(worst_f[1]):02d} "
            + " ".join(parts),
            flush=True,
        )


if __name__ == "__main__":
    run()
