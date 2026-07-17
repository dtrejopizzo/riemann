#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import eigvalsh
from scipy.optimize import linprog

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
]


def phi(vals, a):
    r2 = (1.0 - a) ** 2
    return np.where(vals >= 0.0, r2 * vals * vals, vals * vals)


def moments(vals, degree):
    return np.array([np.sum(vals ** k) for k in range(degree + 1)], dtype=float)


def fit_majorant(a, m_bound, degree, objective_moments, grid_n=801):
    xs = np.linspace(-m_bound, m_bound, grid_n)
    vand = np.vstack([xs ** k for k in range(degree + 1)]).T
    # vand @ c >= phi  <=>  -vand @ c <= -phi
    res = linprog(
        c=objective_moments,
        A_ub=-vand,
        b_ub=-phi(xs, a),
        bounds=[(None, None)] * (degree + 1),
        method="highs",
    )
    if not res.success:
        raise RuntimeError(res.message)
    return res.x


def eval_poly_on_vals(coeff, vals):
    return float(sum(c * np.sum(vals ** k) for k, c in enumerate(coeff)))


def collect():
    data = []
    for lam, n_modes in WINDOWS:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        k0, k1 = two_blocks(lam, idx, L, bq, c_model, 0.60)
        data.append((lam, L, eigvalsh(k0), eigvalsh(k1)))
    return data


def run(degree=10):
    print("E72.171 fixed polynomial majorant probe")
    print(f"degree={degree}; intervals K0=[-0.9,0.9], K1=[-0.6,0.6]")
    data = collect()
    obj0 = sum(moments(v0, degree) for _, _, v0, _ in data) / len(data)
    obj1 = sum(moments(v1, degree) for _, _, _, v1 in data) / len(data)
    c0 = fit_majorant(0.70, 0.90, degree, obj0)
    c1 = fit_majorant(0.60, 0.60, degree, obj1)
    print(" lam    L   exact0   poly0  exact1   poly1  polySum  exactSum")
    worst = (0.0, None)
    for lam, L, v0, v1 in data:
        e0 = float(np.sum(phi(v0, 0.70)))
        e1 = float(np.sum(phi(v1, 0.60)))
        p0 = eval_poly_on_vals(c0, v0)
        p1 = eval_poly_on_vals(c1, v1)
        ps = p0 + p1
        if ps > worst[0]:
            worst = (ps, lam)
        print(
            f"{lam:4.0f} {L:5.2f} {e0:8.3f} {p0:7.3f} "
            f"{e1:7.3f} {p1:7.3f} {ps:8.3f} {e0+e1:8.3f}"
        )
    print(f"worst_poly_sum={worst[0]:.3f} at lambda={worst[1]:.0f}")
    print("coeff_K0=" + " ".join(f"{c:.8e}" for c in c0))
    print("coeff_K1=" + " ".join(f"{c:.8e}" for c in c1))


if __name__ == "__main__":
    run()
