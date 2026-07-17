#!/usr/bin/env python3
import sys

import numpy as np
from numpy.linalg import eigvalsh

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_165_fixed_cut_stress_probe import two_blocks  # noqa: E402
from E72_193_lm8_asrp_probe import split_energy  # noqa: E402


TARGET = 0.9409

# E72.248, homogeneous R degree 8 / P degree 10, fitted over lambda=12..36.
R0_DEG8 = np.array(
    [
        9.9869861120e-01,
        -2.6126797623e00,
        -1.9804311573e01,
        1.2299851184e01,
        2.9969895233e02,
        1.4347637522e01,
        -1.7974700048e03,
        -1.9279016455e02,
        3.7159804900e03,
    ]
)

R1_DEG8 = np.array(
    [
        9.9923237079e-01,
        -1.5396362647e00,
        -8.7556751919e00,
        -5.5335239414e00,
        4.6182864473e01,
        8.4054305754e01,
        3.0021738439e00,
        -7.7401145547e01,
        -4.0848595496e01,
    ]
)

WINDOWS = [(16, 40), (24, 56), (32, 72), (36, 80), (40, 88), (48, 104), (56, 120)]


def eval_hom(vals, m_bound, coeff):
    u = vals / m_bound
    return (m_bound**2) * float(sum(c * np.sum(u ** (ell + 2)) for ell, c in enumerate(coeff)))


def run():
    print("E72.252 homogeneous LM8 extended stress")
    print("Uses fixed E72.248 P degree 10 homogeneous coefficients; no refit.")
    print("lam L dim exactBSE homEnv slack pass op0 op1")
    worst = (-np.inf, None)
    for lam, n_modes in WINDOWS:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        k0, k1 = two_blocks(lam, idx, L, bq, c_model, 0.60)
        v0 = eigvalsh(k0)
        v1 = eigvalsh(k1)
        exact = split_energy(v0, 0.70) + split_energy(v1, 0.60)
        env = eval_hom(v0, 0.90, R0_DEG8) + eval_hom(v1, 0.60, R1_DEG8)
        slack = TARGET - env
        if env > worst[0]:
            worst = (env, lam)
        print(
            f"{lam:3.0f} {L:.6f} {len(v0):3d} "
            f"{exact:.6e} {env:.6e} {slack:+.6e} "
            f"{'YES' if env < TARGET else 'NO'} "
            f"{max(abs(v0)):.3e} {max(abs(v1)):.3e}",
            flush=True,
        )
    print(f"worst_hom={worst[0]:.6e} at lambda={worst[1]:.0f}")


if __name__ == "__main__":
    run()
