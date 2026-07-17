#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import eigvalsh, norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_165_fixed_cut_stress_probe import two_blocks  # noqa: E402
from E72_181_chebyshev_abs_schedule_probe import signed_coeff, eval_cheb_matrix_scaled, theoretical_error_sum  # noqa: E402


WINDOWS = [
    (12, 32),
    (14, 36),
    (16, 40),
    (18, 44),
    (20, 48),
    (22, 52),
    (24, 56),
    (26, 60),
    (28, 64),
]


def even_degree_for_margin(dim, margin):
    # Need sqrt(dim) * 0.99/(pi(D+1)) <= margin.
    need = 0.99 * np.sqrt(dim) / (np.pi * margin) - 1.0
    degree = int(np.ceil(max(0.0, need)))
    if degree % 2:
        degree += 1
    return degree


def run(margin=0.05):
    print("E72.182 adaptive margin SRP probe")
    print(f"margin m*={margin:.3f}; require ||G_D||_HS < {1-margin:.3f}")
    print(" lam    L dim   D   epsHS  ||G_D||  final  margin2 pass")
    worst = (0.0, None)
    for lam, n_modes in WINDOWS:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        k0, k1 = two_blocks(lam, idx, L, bq, c_model, 0.60)
        op0 = float(np.max(np.abs(eigvalsh(k0))))
        op1 = float(np.max(np.abs(eigvalsh(k1))))
        if op0 > 0.90 or op1 > 0.60:
            final = np.inf
            degree = -1
            eps_hs = np.inf
            gnorm = np.inf
        else:
            dim = k0.shape[0]
            degree = even_degree_for_margin(dim, margin)
            n_terms = degree // 2
            c0 = signed_coeff(0.70, 0.90, n_terms)
            c1 = signed_coeff(0.60, 0.60, n_terms)
            eps_hs = np.sqrt(dim) * theoretical_error_sum(n_terms)
            g = eval_cheb_matrix_scaled(k0, c0, 0.90) + eval_cheb_matrix_scaled(k1, c1, 0.60)
            gnorm = norm(g, "fro")
            final = gnorm + eps_hs
        if final > worst[0]:
            worst = (final, lam)
        print(
            f"{lam:4.0f} {L:5.2f} {k0.shape[0]:3d} "
            f"{degree:3d} {eps_hs:7.3f} {gnorm:8.3f} "
            f"{final:6.3f} {1.0-final*final:7.3f} "
            f"{'YES' if final < 1.0 and gnorm < 1.0-margin else 'NO'}",
            flush=True,
        )
    print(f"worst_final={worst[0]:.3f} at lambda={worst[1]:.0f}")


if __name__ == "__main__":
    run()
