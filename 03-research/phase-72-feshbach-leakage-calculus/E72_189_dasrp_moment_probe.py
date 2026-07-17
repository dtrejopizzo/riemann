#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import eigvalsh

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_165_fixed_cut_stress_probe import two_blocks  # noqa: E402
from E72_181_chebyshev_abs_schedule_probe import signed_coeff, eval_cheb_matrix_scaled  # noqa: E402
from E72_182_adaptive_margin_probe import even_degree_for_margin  # noqa: E402


WINDOWS = [(12, 32), (16, 40), (20, 48), (24, 56), (28, 64), (32, 72), (36, 80)]


def moments(mat):
    vals = eigvalsh(mat)
    return (
        float(np.sum(vals**2)),
        float(np.sum(vals**3)),
        float(np.sum(vals**4)),
        float(np.sum(np.where(vals >= 0.0, vals**2, 0.0))),
        float(np.sum(np.where(vals < 0.0, vals**2, 0.0))),
    )


def run(margin=0.03):
    print("E72.189 D-ASRP moment probe")
    print("margin m*=0.03; reports pure G energy and low moments")
    print(" lam    L dim   D  G0sq  G1sq  Gsum  H0    S0/H0  H1    S1/H1")
    worst = (0.0, None)
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
        h0, tr30, tr40, p20, n20 = moments(k0)
        h1, tr31, tr41, p21, n21 = moments(k1)
        s0_over_h0 = (p20 - n20) / max(h0, 1e-30)
        s1_over_h1 = (p21 - n21) / max(h1, 1e-30)
        gsum = g0sq + g1sq
        if gsum > worst[0]:
            worst = (gsum, lam)
        print(
            f"{lam:4.0f} {L:5.2f} {k0.shape[0]:3d} {degree:3d} "
            f"{g0sq:5.3f} {g1sq:5.3f} {gsum:5.3f} "
            f"{h0:5.3f} {s0_over_h0:7.3f} "
            f"{h1:5.3f} {s1_over_h1:7.3f}",
            flush=True,
        )
    print(f"worst_Gdiag={worst[0]:.3f} at lambda={worst[1]:.0f}")


if __name__ == "__main__":
    run()
