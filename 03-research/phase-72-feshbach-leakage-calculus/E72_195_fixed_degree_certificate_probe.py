#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import eigvalsh

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_165_fixed_cut_stress_probe import two_blocks  # noqa: E402
from E72_181_chebyshev_abs_schedule_probe import signed_coeff, eval_cheb_matrix_scaled  # noqa: E402
from E72_192_low_moment_envelope_certificate import C0, C1  # noqa: E402


WINDOWS = [(12, 32), (16, 40), (20, 48), (24, 56), (28, 64), (32, 72), (36, 80)]


def trace_ratio(vals, m_bound, r=8):
    return float(np.sum((vals / m_bound) ** (2 * r)))


def lm8(vals0, vals1):
    u0 = vals0 / 0.90
    u1 = vals1 / 0.60
    e0 = 0.90**2 * float(sum(c * np.sum(u0**k) for k, c in enumerate(C0)))
    e1 = 0.60**2 * float(sum(c * np.sum(u1**k) for k, c in enumerate(C1)))
    return e0 + e1


def xneg32(k0, k1):
    c0 = signed_coeff(0.70, 0.90, 16)
    c1 = signed_coeff(0.60, 0.60, 16)
    g0 = eval_cheb_matrix_scaled(k0, c0, 0.90)
    g1 = eval_cheb_matrix_scaled(k1, c1, 0.60)
    return float(2.0 * np.trace(g0 @ g1))


def run():
    print("E72.195 fixed-degree stable certificate probe")
    print("target: NTC-8 + LM8-ASRP + XNEG-32")
    print(" lam    L dim   NTC0    NTC1    LM8   XNEG32 pass")
    worst_lm8 = (0.0, None)
    worst_cross = (-np.inf, None)
    for lam, n_modes in WINDOWS:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        k0, k1 = two_blocks(lam, idx, L, bq, c_model, 0.60)
        v0 = eigvalsh(k0)
        v1 = eigvalsh(k1)
        ntc0 = trace_ratio(v0, 0.90)
        ntc1 = trace_ratio(v1, 0.60)
        env = lm8(v0, v1)
        cross = xneg32(k0, k1)
        ok = ntc0 < 1.0 and ntc1 < 1.0 and env < 0.9409 and cross <= 0.0
        if env > worst_lm8[0]:
            worst_lm8 = (env, lam)
        if cross > worst_cross[0]:
            worst_cross = (cross, lam)
        print(
            f"{lam:4.0f} {L:5.2f} {len(v0):3d} "
            f"{ntc0:7.2e} {ntc1:7.2e} "
            f"{env:6.3f} {cross:+8.3f} "
            f"{'YES' if ok else 'NO'}",
            flush=True,
        )
    print(f"worst_LM8={worst_lm8[0]:.3f} at lambda={worst_lm8[1]:.0f}")
    print(f"max_XNEG32={worst_cross[0]:+.3f} at lambda={worst_cross[1]:.0f}")


if __name__ == "__main__":
    run()
