#!/usr/bin/env python3
import sys

import numpy as np
from numpy.linalg import eigvalsh
from scipy.optimize import linprog

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_165_fixed_cut_stress_probe import two_blocks  # noqa: E402
from E72_193_lm8_asrp_probe import split_energy  # noqa: E402
from E72_248_homogeneous_lm8_probe import fit_homogeneous_r, scaled_power_moments, eval_hom  # noqa: E402
from E72_262_pole_relative_even_setup_audit import pole_relative_even_setup_pair  # noqa: E402


TARGET = 0.9409
STABLE_WINDOWS = [(16, 40), (20, 48), (24, 56)]


def collect(windows):
    rows = []
    for lam, n_modes in windows:
        idx, L, xi, eb, c_actual, c_model, e_pole, odd_norm, even_leak = pole_relative_even_setup_pair(lam, n_modes)
        k0, k1 = two_blocks(lam, idx, L, eb, c_model, 0.60)
        v0 = eigvalsh(k0)
        v1 = eigvalsh(k1)
        exact = split_energy(v0, 0.70) + split_energy(v1, 0.60)
        rows.append((lam, L, v0, v1, exact))
        print(f"prepared lambda={lam:.0f} exact={exact:.6e}", flush=True)
    return rows


def fit_for_rows(rows, r_degree):
    obj0 = sum(scaled_power_moments(v0, 0.90, r_degree) for _, _, v0, _, _ in rows) / len(rows)
    obj1 = sum(scaled_power_moments(v1, 0.60, r_degree) for _, _, _, v1, _ in rows) / len(rows)
    r0 = fit_homogeneous_r(0.70, r_degree, obj0)
    r1 = fit_homogeneous_r(0.60, r_degree, obj1)
    return r0, r1


def run():
    print("E72.263 pole-even homogeneous LM8 probe")
    print("Refits homogeneous P_j(u)=u^2R_j(u) in the corrected pole-relative even geometry.")
    print("Stable windows only; lambda=12 is an exact-BSE finite failure in E72.262.")
    rows = collect(STABLE_WINDOWS)
    for degree in [4, 6, 8, 10, 12]:
        r0, r1 = fit_for_rows(rows, degree)
        print(f"-- R degree={degree} / P degree={degree+2}")
        print("lam exactBSE env slack op0 op1 pass")
        worst = (-np.inf, None)
        for lam, L, v0, v1, exact in rows:
            env = eval_hom(v0, 0.90, r0) + eval_hom(v1, 0.60, r1)
            worst = max(worst, (env, lam), key=lambda x: x[0])
            print(
                f"{lam:3.0f} {exact:.6e} {env:.6e} {TARGET-env:+.6e} "
                f"{max(abs(v0)):.3e} {max(abs(v1)):.3e} "
                f"{'YES' if env < TARGET else 'NO'}",
                flush=True,
            )
        print(f"worst_env={worst[0]:.6e} at lambda={worst[1]:.0f}")
        print("R0=" + " ".join(f"{c:.10e}" for c in r0))
        print("R1=" + " ".join(f"{c:.10e}" for c in r1))


if __name__ == "__main__":
    run()
