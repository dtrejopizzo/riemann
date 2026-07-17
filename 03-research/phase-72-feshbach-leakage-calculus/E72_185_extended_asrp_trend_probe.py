#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import eigvalsh, norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_165_fixed_cut_stress_probe import two_blocks  # noqa: E402
from E72_181_chebyshev_abs_schedule_probe import signed_coeff, eval_cheb_matrix_scaled, theoretical_error_sum  # noqa: E402
from E72_182_adaptive_margin_probe import even_degree_for_margin  # noqa: E402
from E72_184_unified_arithmetic_certificate_probe import trace_ratio  # noqa: E402


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


def row(lam, n_modes, margin=0.05):
    idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
    k0, k1 = two_blocks(lam, idx, L, bq, c_model, 0.60)
    op0 = float(np.max(np.abs(eigvalsh(k0))))
    op1 = float(np.max(np.abs(eigvalsh(k1))))
    ntc0 = trace_ratio(k0, 0.90, 8)
    ntc1 = trace_ratio(k1, 0.60, 8)
    degree = even_degree_for_margin(k0.shape[0], margin)
    n_terms = degree // 2
    c0 = signed_coeff(0.70, 0.90, n_terms)
    c1 = signed_coeff(0.60, 0.60, n_terms)
    eps_hs = np.sqrt(k0.shape[0]) * theoretical_error_sum(n_terms)
    g = eval_cheb_matrix_scaled(k0, c0, 0.90) + eval_cheb_matrix_scaled(k1, c1, 0.60)
    gnorm = norm(g, "fro")
    final = gnorm + eps_hs
    return {
        "lam": lam,
        "L": L,
        "dim": k0.shape[0],
        "op0": op0,
        "op1": op1,
        "ntc0": ntc0,
        "ntc1": ntc1,
        "degree": degree,
        "eps": eps_hs,
        "gnorm": gnorm,
        "final": final,
        "g2": gnorm * gnorm,
        "pass": ntc0 < 1.0 and ntc1 < 1.0 and gnorm < 1.0 - margin and final < 1.0,
    }


def run():
    print("E72.185 extended ASRP trend probe")
    print("stable certificate: NTC-8 + ASRP-0.05")
    print(" lam    L dim  op0  op1    ntc1    D   eps   gnorm    g2   final pass")
    worst = (0.0, None)
    for lam, n_modes in WINDOWS:
        s = row(lam, n_modes)
        if s["final"] > worst[0]:
            worst = (s["final"], lam)
        print(
            f"{lam:4.0f} {s['L']:5.2f} {s['dim']:3d} "
            f"{s['op0']:4.3f} {s['op1']:4.3f} "
            f"{s['ntc1']:7.2e} {s['degree']:4d} "
            f"{s['eps']:5.3f} {s['gnorm']:7.3f} "
            f"{s['g2']:6.3f} {s['final']:7.3f} "
            f"{'YES' if s['pass'] else 'NO'}",
            flush=True,
        )
    print(f"worst_final={worst[0]:.3f} at lambda={worst[1]:.0f}")


if __name__ == "__main__":
    run()
