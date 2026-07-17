#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import eigvalsh, norm
from numpy.polynomial import Chebyshev

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


def signed_residual_scalar(x, a):
    return np.where(x >= 0.0, (1.0 - a) * x, x)


def fit_cheb(a, m_bound, degree, grid_n=8001):
    xs = np.linspace(-m_bound, m_bound, grid_n)
    ys = signed_residual_scalar(xs, a)
    cheb = Chebyshev.fit(xs, ys, degree, domain=[-m_bound, m_bound])
    fine = np.linspace(-m_bound, m_bound, 120001)
    err = float(np.max(np.abs(cheb(fine) - signed_residual_scalar(fine, a))))
    return cheb.coef.copy(), err


def eval_cheb_matrix(mat, coeff, m_bound):
    x = mat / m_bound
    t0 = np.eye(mat.shape[0])
    if len(coeff) == 1:
        return coeff[0] * t0
    t1 = x
    out = coeff[0] * t0 + coeff[1] * t1
    for k in range(2, len(coeff)):
        t2 = 2.0 * x @ t1 - t0
        out = out + coeff[k] * t2
        t0, t1 = t1, t2
    return 0.5 * (out + out.T)


def collect():
    rows = []
    for lam, n_modes in WINDOWS:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        k0, k1 = two_blocks(lam, idx, L, bq, c_model, 0.60)
        op0 = float(np.max(np.abs(eigvalsh(k0))))
        op1 = float(np.max(np.abs(eigvalsh(k1))))
        rows.append((lam, L, k0, k1, op0, op1))
        print(f"prepared lambda={lam:.0f} dim={k0.shape[0]} op0={op0:.3f} op1={op1:.3f}", flush=True)
    return rows


def run():
    print("E72.179 adaptive SRP degree probe")
    print("Chebyshev matrix evaluation; intervals K0=[-0.9,0.9], K1=[-0.6,0.6]")
    rows = collect()
    print(" deg   err0     err1   maxBound  worstLam  per-window")
    for degree in [28, 40, 56, 80, 112]:
        c0, err0 = fit_cheb(0.70, 0.90, degree)
        c1, err1 = fit_cheb(0.60, 0.60, degree)
        worst = (0.0, None)
        parts = []
        for lam, L, k0, k1, op0, op1 in rows:
            if op0 > 0.90 or op1 > 0.60:
                bound = np.inf
            else:
                rpoly = eval_cheb_matrix(k0, c0, 0.90) + eval_cheb_matrix(k1, c1, 0.60)
                err_hs = np.sqrt(k0.shape[0]) * (err0 + err1)
                bound = norm(rpoly, "fro") + err_hs
            if bound > worst[0]:
                worst = (bound, lam)
            parts.append(f"{int(lam)}:{bound:.3f}")
        print(
            f"{degree:4d} {err0:8.3e} {err1:8.3e} "
            f"{worst[0]:8.3f} {int(worst[1]):8d} "
            + " ".join(parts),
            flush=True,
        )


if __name__ == "__main__":
    run()
