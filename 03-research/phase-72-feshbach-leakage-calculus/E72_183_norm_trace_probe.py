#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import eigvalsh

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_165_fixed_cut_stress_probe import two_blocks  # noqa: E402


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


def even_trace_ratio(mat, m_bound, r):
    vals = eigvalsh(mat)
    return float(np.sum((vals / m_bound) ** (2 * r)))


def run():
    print("E72.183 norm interval trace-power probe")
    print("If Tr((K/M)^(2r)) < 1, then ||K|| < M.")
    print(" lam    L dim  op0  op1  r4_K0 r4_K1  r8_K0 r8_K1  r12_K0 r12_K1 pass8")
    for lam, n_modes in WINDOWS:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        k0, k1 = two_blocks(lam, idx, L, bq, c_model, 0.60)
        op0 = float(np.max(np.abs(eigvalsh(k0))))
        op1 = float(np.max(np.abs(eigvalsh(k1))))
        ratios = []
        for r in [4, 8, 12]:
            ratios.append(even_trace_ratio(k0, 0.90, r))
            ratios.append(even_trace_ratio(k1, 0.60, r))
        pass8 = ratios[2] < 1.0 and ratios[3] < 1.0
        print(
            f"{lam:4.0f} {L:5.2f} {k0.shape[0]:3d} "
            f"{op0:4.3f} {op1:4.3f} "
            f"{ratios[0]:6.3e} {ratios[1]:6.3e} "
            f"{ratios[2]:6.3e} {ratios[3]:6.3e} "
            f"{ratios[4]:7.3e} {ratios[5]:7.3e} "
            f"{'YES' if pass8 else 'NO'}",
            flush=True,
        )


if __name__ == "__main__":
    run()
