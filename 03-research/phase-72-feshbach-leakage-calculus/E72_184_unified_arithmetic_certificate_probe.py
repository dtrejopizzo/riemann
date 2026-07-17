#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import eigvalsh, norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_159_prime_block_psd_probe import psd_part, relative_matrix  # noqa: E402
from E72_165_fixed_cut_stress_probe import two_blocks  # noqa: E402
from E72_181_chebyshev_abs_schedule_probe import signed_coeff, eval_cheb_matrix_scaled, theoretical_error_sum  # noqa: E402
from E72_182_adaptive_margin_probe import even_degree_for_margin  # noqa: E402


WINDOWS = [
    (6, 18),
    (8, 24),
    (10, 28),
    (12, 32),
    (14, 36),
    (16, 40),
    (18, 44),
    (20, 48),
    (22, 52),
    (24, 56),
    (26, 60),
    (28, 64),
    (30, 68),
    (32, 72),
]


def trace_ratio(mat, m_bound, r=8):
    vals = eigvalsh(mat)
    return float(np.sum((vals / m_bound) ** (2 * r)))


def finite_f2b(c_actual, c_model, blocks, a=0.70, b=0.60):
    krel = relative_matrix(c_actual - c_model, c_model)
    p0 = psd_part(blocks[0])
    p1 = psd_part(blocks[1])
    residual = krel - a * p0 - b * p1
    dist = norm(residual, "fro")
    return dist, 1.0 - dist * dist


def asrp(blocks, margin=0.05):
    k0, k1 = blocks
    dim = k0.shape[0]
    ntc0 = trace_ratio(k0, 0.90, 8)
    ntc1 = trace_ratio(k1, 0.60, 8)
    degree = even_degree_for_margin(dim, margin)
    n_terms = degree // 2
    c0 = signed_coeff(0.70, 0.90, n_terms)
    c1 = signed_coeff(0.60, 0.60, n_terms)
    eps_hs = np.sqrt(dim) * theoretical_error_sum(n_terms)
    g = eval_cheb_matrix_scaled(k0, c0, 0.90) + eval_cheb_matrix_scaled(k1, c1, 0.60)
    gnorm = norm(g, "fro")
    final = gnorm + eps_hs
    return {
        "ntc0": ntc0,
        "ntc1": ntc1,
        "degree": degree,
        "eps": eps_hs,
        "gnorm": gnorm,
        "final": final,
        "margin2": 1.0 - final * final,
        "pass": ntc0 < 1.0 and ntc1 < 1.0 and gnorm < 1.0 - margin and final < 1.0,
    }


def run():
    print("E72.184 unified arithmetic certificate probe")
    print("prestable: direct F2B; stable: NTC-8 + ASRP-0.05")
    print(" lam    L dim mode    metric1   metric2    D   eps   gnorm  final  pass")
    worst = (0.0, None)
    for lam, n_modes in WINDOWS:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        blocks = two_blocks(lam, idx, L, bq, c_model, 0.60)
        dim = blocks[0].shape[0]
        if lam < 12:
            dist, margin2 = finite_f2b(c_actual, c_model, blocks)
            final = dist
            ok = dist < 1.0
            print(
                f"{lam:4.0f} {L:5.2f} {dim:3d} F2B  "
                f"{dist:8.3f} {margin2:8.3f} "
                f"{'-':>4s} {'-':>5s} {'-':>7s} {final:6.3f} "
                f"{'YES' if ok else 'NO'}",
                flush=True,
            )
        else:
            s = asrp(blocks, 0.05)
            final = s["final"]
            ok = s["pass"]
            print(
                f"{lam:4.0f} {L:5.2f} {dim:3d} ASRP "
                f"{s['ntc0']:8.2e} {s['ntc1']:8.2e} "
                f"{s['degree']:4d} {s['eps']:5.3f} "
                f"{s['gnorm']:7.3f} {final:6.3f} "
                f"{'YES' if ok else 'NO'}",
                flush=True,
            )
        if final > worst[0]:
            worst = (final, lam)
    print(f"worst_certificate_value={worst[0]:.3f} at lambda={worst[1]:.0f}")


if __name__ == "__main__":
    run()
