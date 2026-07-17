#!/usr/bin/env python3
import sys

import numpy as np
from numpy.linalg import eigvalsh

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_165_fixed_cut_stress_probe import two_blocks  # noqa: E402
from E72_193_lm8_asrp_probe import split_energy  # noqa: E402
from E72_252_homogeneous_lm8_extended_stress import R0_DEG8, R1_DEG8, eval_hom  # noqa: E402
from E72_256_strict_homogeneous_lm8_certificate import BUFFER  # noqa: E402


TARGET = 0.9409
WINDOWS = [(16, 40), (24, 56), (32, 72), (36, 80), (40, 88), (48, 104), (56, 120)]


def run():
    print("E72.257 strict homogeneous LM8 stress")
    print(f"Uses strict R-certified buffer {BUFFER:.1e}; no refit.")
    print("lam L dim exactBSE strictHom slack pass")
    r0 = R0_DEG8.copy()
    r1 = R1_DEG8.copy()
    r0[0] += BUFFER
    r1[0] += BUFFER
    worst = (-np.inf, None)
    for lam, n_modes in WINDOWS:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        k0, k1 = two_blocks(lam, idx, L, bq, c_model, 0.60)
        v0 = eigvalsh(k0)
        v1 = eigvalsh(k1)
        exact = split_energy(v0, 0.70) + split_energy(v1, 0.60)
        env = eval_hom(v0, 0.90, r0) + eval_hom(v1, 0.60, r1)
        worst = max(worst, (env, lam), key=lambda x: x[0])
        print(
            f"{lam:3.0f} {L:.6f} {len(v0):3d} {exact:.6e} "
            f"{env:.6e} {TARGET-env:+.6e} {'YES' if env < TARGET else 'NO'}",
            flush=True,
        )
    print(f"worst_strict_hom={worst[0]:.6e} at lambda={worst[1]:.0f}")


if __name__ == "__main__":
    run()
