#!/usr/bin/env python3
import sys

import numpy as np
from numpy.linalg import eigvalsh

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_165_fixed_cut_stress_probe import two_blocks  # noqa: E402
from E72_172_polynomial_majorant_certificate import C0 as PTC0, C1 as PTC1  # noqa: E402
from E72_192_low_moment_envelope_certificate import C0 as LM80, C1 as LM81  # noqa: E402
from E72_193_lm8_asrp_probe import eval_env, split_energy  # noqa: E402


WINDOWS = [(12, 32), (16, 40), (20, 48), (24, 56), (28, 64), (32, 72), (36, 80)]
LM8_TARGET = 0.9409


def constant_cost_lm8(dim):
    return dim * ((0.90**2) * LM80[0] + (0.60**2) * LM81[0])


def linear_cost_lm8(vals0, vals1):
    return (0.90**2) * LM80[1] * np.sum(vals0 / 0.90) + (0.60**2) * LM81[1] * np.sum(vals1 / 0.60)


def run():
    print("E72.247 majorant constant drift probe")
    print("LM8 uses scaled P_j(u) with contribution M_j^2 Tr P_j(K_j/M_j).")
    print("Polynomial endpoint data:")
    print(f"  LM8 P0(0)={LM80[0]:+.12e} P0'(0)={LM80[1]:+.12e}")
    print(f"  LM8 P1(0)={LM81[0]:+.12e} P1'(0)={LM81[1]:+.12e}")
    print(f"  PTC P0(0)={PTC0[0]:+.12e} P0'(0)={PTC0[1]:+.12e}")
    print(f"  PTC P1(0)={PTC1[0]:+.12e} P1'(0)={PTC1[1]:+.12e}")
    print("lam dim exact LM8 slack constCost const/slack linearTerm envNoConst")
    for lam, n_modes in WINDOWS:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        k0, k1 = two_blocks(lam, idx, L, bq, c_model, 0.60)
        v0 = eigvalsh(k0)
        v1 = eigvalsh(k1)
        dim = len(v0)
        exact = split_energy(v0, 0.70) + split_energy(v1, 0.60)
        env = eval_env(v0, LM80, 0.90) + eval_env(v1, LM81, 0.60)
        slack = LM8_TARGET - env
        const = constant_cost_lm8(dim)
        linear = linear_cost_lm8(v0, v1)
        print(
            f"{lam:3.0f} {dim:3d} {exact:.6e} {env:.6e} {slack:+.6e} "
            f"{const:.6e} {const/max(slack,1e-300):.3f} "
            f"{linear:+.6e} {env-const:.6e}",
            flush=True,
        )


if __name__ == "__main__":
    run()
