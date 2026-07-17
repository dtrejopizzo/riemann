#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import eigvalsh, norm
from numpy.polynomial import Chebyshev, Polynomial

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_165_fixed_cut_stress_probe import two_blocks  # noqa: E402
from E72_166_residual_sign_gram_probe import spectral_parts  # noqa: E402


def signed_residual_scalar(t, a):
    return np.where(t >= 0.0, (1.0 - a) * t, t)


def fit_signed_poly(a, m_bound, degree, grid_n=4001):
    xs = np.linspace(-m_bound, m_bound, grid_n)
    ys = signed_residual_scalar(xs, a)
    cheb = Chebyshev.fit(xs, ys, degree, domain=[-m_bound, m_bound])
    poly = cheb.convert(kind=Polynomial)
    fine = np.linspace(-m_bound, m_bound, 40001)
    err = float(np.max(np.abs(poly(fine) - signed_residual_scalar(fine, a))))
    return np.array(poly.coef, dtype=float), err


def eval_poly_matrix(mat, coeff):
    out = coeff[0] * np.eye(mat.shape[0])
    power = np.eye(mat.shape[0])
    for k in range(1, len(coeff)):
        power = power @ mat
        out = out + coeff[k] * power
    return 0.5 * (out + out.T)


def exact_signed_matrix(mat, a):
    pos, neg = spectral_parts(mat)
    return (1.0 - a) * pos + neg


def run(degree=28):
    print("E72.175 signed residual polynomial probe")
    print(f"degree={degree}; intervals K0=[-0.9,0.9], K1=[-0.6,0.6]")
    g0, err0 = fit_signed_poly(0.70, 0.90, degree)
    g1, err1 = fit_signed_poly(0.60, 0.60, degree)
    print(f"uniform_errors err0={err0:.3e}, err1={err1:.3e}")
    print(" lam    L  dim  exactR  polyR  errHS  bound  margin  pass")
    worst = (0.0, None)
    for lam, n_modes in [
        (12, 32),
        (14, 36),
        (16, 40),
        (18, 44),
        (20, 48),
        (22, 52),
        (24, 56),
    ]:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        k0, k1 = two_blocks(lam, idx, L, bq, c_model, 0.60)
        op0 = float(np.max(np.abs(eigvalsh(k0))))
        op1 = float(np.max(np.abs(eigvalsh(k1))))
        if op0 > 0.90 or op1 > 0.60:
            raise RuntimeError(f"spectral interval failed at lambda={lam}")
        rexact = exact_signed_matrix(k0, 0.70) + exact_signed_matrix(k1, 0.60)
        rpoly = eval_poly_matrix(k0, g0) + eval_poly_matrix(k1, g1)
        exact_norm = norm(rexact, "fro")
        poly_norm = norm(rpoly, "fro")
        err_hs = np.sqrt(k0.shape[0]) * (err0 + err1)
        bound = poly_norm + err_hs
        if bound > worst[0]:
            worst = (bound, lam)
        print(
            f"{lam:4.0f} {L:5.2f} {k0.shape[0]:4d} "
            f"{exact_norm:7.3f} {poly_norm:6.3f} {err_hs:6.3f} "
            f"{bound:6.3f} {1.0-bound*bound:7.3f} "
            f"{'YES' if bound < 1.0 else 'NO'}"
        )
        sys.stdout.flush()
    print(f"worst_bound={worst[0]:.3f} at lambda={worst[1]:.0f}")
    print("coeff_g0=" + " ".join(f"{c:.12e}" for c in g0))
    print("coeff_g1=" + " ".join(f"{c:.12e}" for c in g1))


if __name__ == "__main__":
    run()
