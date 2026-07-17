#!/usr/bin/env python3
import sys

import numpy as np
from numpy.linalg import eigvalsh
from scipy.optimize import linprog

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_165_fixed_cut_stress_probe import two_blocks  # noqa: E402
from E72_193_lm8_asrp_probe import split_energy  # noqa: E402


WINDOWS = [(12, 32), (16, 40), (20, 48), (24, 56), (28, 64), (32, 72), (36, 80)]
TARGET = 0.9409


def scaled_power_moments(vals, m_bound, r_degree):
    u = vals / m_bound
    # P(u)=u^2 R(u), R(u)=sum b_l u^l.
    return np.array([np.sum(u ** (ell + 2)) for ell in range(r_degree + 1)], dtype=float)


def fit_homogeneous_r(a, r_degree, objective):
    xs = np.linspace(-1.0, 1.0, 4001)
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
        raise RuntimeError(res.message)
    return res.x


def eval_hom(vals, m_bound, coeff):
    u = vals / m_bound
    return (m_bound**2) * float(sum(c * np.sum(u ** (ell + 2)) for ell, c in enumerate(coeff)))


def collect():
    rows = []
    for lam, n_modes in WINDOWS:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        k0, k1 = two_blocks(lam, idx, L, bq, c_model, 0.60)
        rows.append((lam, L, eigvalsh(k0), eigvalsh(k1)))
        print(f"prepared lambda={lam:.0f}", flush=True)
    return rows


def run():
    print("E72.248 homogeneous LM8 probe")
    print("P_j(u)=u^2 R_j(u); no constant or linear drift.")
    rows = collect()
    for r_degree in [2, 4, 6, 8]:
        obj0 = sum(scaled_power_moments(v0, 0.90, r_degree) for _, _, v0, _ in rows) / len(rows)
        obj1 = sum(scaled_power_moments(v1, 0.60, r_degree) for _, _, _, v1 in rows) / len(rows)
        r0 = fit_homogeneous_r(0.70, r_degree, obj0)
        r1 = fit_homogeneous_r(0.60, r_degree, obj1)
        print(f"-- R degree={r_degree} / P degree={r_degree+2}")
        print(" lam exactBSE homEnv slack pass")
        worst = (0.0, None)
        for lam, L, v0, v1 in rows:
            exact = split_energy(v0, 0.70) + split_energy(v1, 0.60)
            env = eval_hom(v0, 0.90, r0) + eval_hom(v1, 0.60, r1)
            worst = max(worst, (env, lam), key=lambda x: x[0])
            print(
                f"{lam:4.0f} {exact:.6e} {env:.6e} {TARGET-env:+.6e} "
                f"{'YES' if env < TARGET else 'NO'}",
                flush=True,
            )
        print(f"worst_hom={worst[0]:.6e} at lambda={worst[1]:.0f}")
        print("R0=" + " ".join(f"{c:.10e}" for c in r0))
        print("R1=" + " ".join(f"{c:.10e}" for c in r1))


if __name__ == "__main__":
    run()
