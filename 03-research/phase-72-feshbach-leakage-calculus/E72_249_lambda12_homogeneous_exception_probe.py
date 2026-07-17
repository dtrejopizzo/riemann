#!/usr/bin/env python3
import sys

import numpy as np
from numpy.linalg import eigvalsh
from scipy.optimize import linprog

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_165_fixed_cut_stress_probe import two_blocks  # noqa: E402
from E72_193_lm8_asrp_probe import split_energy  # noqa: E402


TARGET = 0.9409


def moments(vals, m_bound, r_degree):
    u = vals / m_bound
    return np.array([np.sum(u ** (ell + 2)) for ell in range(r_degree + 1)])


def fit_homogeneous_r(a, r_degree, objective):
    xs = np.linspace(-1.0, 1.0, 8001)
    lower = np.where(xs < 0.0, 1.0, (1.0 - a) ** 2)
    vand = np.vstack([xs**ell for ell in range(r_degree + 1)]).T
    res = linprog(
        c=objective,
        A_ub=-vand,
        b_ub=-lower,
        bounds=[(None, None)] * (r_degree + 1),
        method="highs",
    )
    if not res.success:
        return None, res.message
    return res.x, None


def eval_hom(vals, m_bound, coeff):
    u = vals / m_bound
    return (m_bound**2) * float(sum(c * np.sum(u ** (ell + 2)) for ell, c in enumerate(coeff)))


def run():
    print("E72.249 lambda=12 homogeneous exception probe")
    print("Optimizes P_j(u)=u^2R_j(u) specifically for the finite lambda=12 window.")
    idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(12, 32)
    k0, k1 = two_blocks(12, idx, L, bq, c_model, 0.60)
    v0 = eigvalsh(k0)
    v1 = eigvalsh(k1)
    exact = split_energy(v0, 0.70) + split_energy(v1, 0.60)
    print(f"lambda=12 dim={len(v0)} exactBSE={exact:.12e}")
    print("Rdeg Pdeg env slack pass status")
    for r_degree in [8, 10, 12, 14]:
        r0, err0 = fit_homogeneous_r(0.70, r_degree, moments(v0, 0.90, r_degree))
        r1, err1 = fit_homogeneous_r(0.60, r_degree, moments(v1, 0.60, r_degree))
        if r0 is None or r1 is None:
            print(f"{r_degree:4d} {r_degree+2:4d} nan nan NO {err0 or err1}")
            continue
        env = eval_hom(v0, 0.90, r0) + eval_hom(v1, 0.60, r1)
        print(
            f"{r_degree:4d} {r_degree+2:4d} {env:.12e} "
            f"{TARGET-env:+.12e} {'YES' if env < TARGET else 'NO'} ok",
            flush=True,
        )


if __name__ == "__main__":
    run()
