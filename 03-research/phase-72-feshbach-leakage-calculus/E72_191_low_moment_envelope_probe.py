#!/usr/bin/env python3
import sys
import numpy as np
from scipy.optimize import linprog
from numpy.linalg import eigvalsh

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_165_fixed_cut_stress_probe import two_blocks  # noqa: E402


WINDOWS = [(12, 32), (16, 40), (20, 48), (24, 56), (28, 64), (32, 72), (36, 80)]


def split_energy(vals, a):
    r2 = (1.0 - a) ** 2
    return float(np.sum(np.where(vals >= 0.0, r2 * vals * vals, vals * vals)))


def scaled_moments(vals, m_bound, degree):
    x = vals / m_bound
    return np.array([np.sum(x**k) for k in range(degree + 1)], dtype=float)


def fit_block_majorant(a, degree, objective):
    xs = np.linspace(-1.0, 1.0, 2001)
    target = np.where(xs >= 0.0, (1.0 - a) ** 2 * xs * xs, xs * xs)
    vand = np.vstack([xs**k for k in range(degree + 1)]).T
    res = linprog(
        c=objective,
        A_ub=-vand,
        b_ub=-target,
        bounds=[(None, None)] * (degree + 1),
        method="highs",
    )
    if not res.success:
        raise RuntimeError(res.message)
    return res.x


def eval_scaled_poly(coeff, vals, m_bound):
    x = vals / m_bound
    return float(sum(c * np.sum(x**k) for k, c in enumerate(coeff)))


def collect():
    rows = []
    for lam, n_modes in WINDOWS:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        k0, k1 = two_blocks(lam, idx, L, bq, c_model, 0.60)
        rows.append((lam, L, eigvalsh(k0), eigvalsh(k1)))
        print(f"prepared lambda={lam:.0f}", flush=True)
    return rows


def run():
    print("E72.191 low-moment envelope probe")
    print("Fits scalar majorants to e_a(t) on scaled interval [-1,1].")
    rows = collect()
    for degree in [4, 6, 8]:
        obj0 = sum(scaled_moments(v0, 0.90, degree) for _, _, v0, _ in rows) / len(rows)
        obj1 = sum(scaled_moments(v1, 0.60, degree) for _, _, _, v1 in rows) / len(rows)
        c0 = fit_block_majorant(0.70, degree, obj0)
        c1 = fit_block_majorant(0.60, degree, obj1)
        print(f"-- degree={degree}")
        print(" lam  exactBSE  envSum  slack  pass09409")
        worst = (0.0, None)
        for lam, L, v0, v1 in rows:
            exact = split_energy(v0, 0.70) + split_energy(v1, 0.60)
            env = (0.90**2) * eval_scaled_poly(c0, v0, 0.90) + (0.60**2) * eval_scaled_poly(c1, v1, 0.60)
            if env > worst[0]:
                worst = (env, lam)
            print(
                f"{lam:4.0f} {exact:9.3f} {env:7.3f} "
                f"{env-exact:6.3f} {'YES' if env < 0.9409 else 'NO'}",
                flush=True,
            )
        print(f"worst_env={worst[0]:.3f} at lambda={worst[1]:.0f}")
        print("coeff0=" + " ".join(f"{c:.8e}" for c in c0))
        print("coeff1=" + " ".join(f"{c:.8e}" for c in c1))


if __name__ == "__main__":
    run()
