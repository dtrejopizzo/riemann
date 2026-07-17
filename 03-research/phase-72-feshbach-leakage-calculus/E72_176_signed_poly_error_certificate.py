#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import eigvalsh, norm
from numpy.polynomial import Chebyshev, Polynomial

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_165_fixed_cut_stress_probe import two_blocks  # noqa: E402
from E72_175_signed_residual_polynomial_probe import eval_poly_matrix  # noqa: E402


def fit_poly(a, m_bound, degree, grid_n=4001):
    xs = np.linspace(-m_bound, m_bound, grid_n)
    ys = np.where(xs >= 0.0, (1.0 - a) * xs, xs)
    cheb = Chebyshev.fit(xs, ys, degree, domain=[-m_bound, m_bound])
    return cheb.convert(kind=Polynomial)


def max_abs_error_on_piece(poly, slope, lo, hi):
    diff = poly - Polynomial([0.0, slope])
    candidates = [lo, hi]
    for z in diff.deriv().roots():
        if abs(z.imag) < 1e-8 and lo <= z.real <= hi:
            candidates.append(float(z.real))
    vals = [(x, abs(float(diff(x)))) for x in candidates]
    return max(vals, key=lambda t: t[1]), vals


def certified_error(poly, a, m_bound):
    neg, _ = max_abs_error_on_piece(poly, 1.0, -m_bound, 0.0)
    pos, _ = max_abs_error_on_piece(poly, 1.0 - a, 0.0, m_bound)
    return max(neg[1], pos[1]), neg, pos


def run(degree=28):
    print("E72.176 signed polynomial error certificate")
    p0 = fit_poly(0.70, 0.90, degree)
    p1 = fit_poly(0.60, 0.60, degree)
    err0, neg0, pos0 = certified_error(p0, 0.70, 0.90)
    err1, neg1, pos1 = certified_error(p1, 0.60, 0.60)
    print(f"degree={degree}")
    print(f"K0 err={err0:.12e} negMax@{neg0[0]:+.12f} posMax@{pos0[0]:+.12f}")
    print(f"K1 err={err1:.12e} negMax@{neg1[0]:+.12f} posMax@{pos1[0]:+.12f}")
    print(" lam    L dim  polyR  certErrHS  certBound margin pass")
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
        rpoly = eval_poly_matrix(k0, p0.coef) + eval_poly_matrix(k1, p1.coef)
        poly_norm = norm(rpoly, "fro")
        err_hs = np.sqrt(k0.shape[0]) * (err0 + err1)
        bound = poly_norm + err_hs
        if bound > worst[0]:
            worst = (bound, lam)
        print(
            f"{lam:4.0f} {L:5.2f} {k0.shape[0]:3d} "
            f"{poly_norm:6.3f} {err_hs:9.3f} "
            f"{bound:9.3f} {1.0-bound*bound:7.3f} "
            f"{'YES' if bound < 1.0 else 'NO'}"
        )
        sys.stdout.flush()
    print(f"worst_cert_bound={worst[0]:.3f} at lambda={worst[1]:.0f}")


if __name__ == "__main__":
    run()
