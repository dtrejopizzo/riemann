#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import norm, solve

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_79_bordered_minor_probe import finite_roots, setup  # noqa: E402


def remainder_coefficients(roots, values):
    vand = np.polynomial.polynomial.polyvander(roots, len(roots) - 1)
    return solve(vand, values)


def eval_poly(coeffs, roots):
    vand = np.polynomial.polynomial.polyvander(roots, len(coeffs) - 1)
    return vand @ coeffs


def root_values(lam, n_modes, root_count=5):
    s = 10 + 0.2j
    idx, L, d, xi, k, bq, ce = setup(lam, n_modes)
    h = k - xi
    roots = finite_roots(xi, d)[:root_count]
    a = bq.T @ (s / (s * s - d * d))
    values = []
    for tau in roots:
        e_tau = np.exp(1j * tau * L)
        s_tau = 2 * tau / (tau * tau - d * d)
        r_minus = 1 / (tau - d)
        w = 1j * s_tau * k - (e_tau - 1) / L * s_tau * np.dot(r_minus, h)
        b = bq.T @ w
        values.append(np.vdot(a, solve(ce, b)))
    return roots, np.array(values)


def run():
    print("E72.80 root remainder probe")
    print("   lam    N roots    max|R(tau)|      ||coeff||2     interp.err")
    for lam, n_modes in [(6, 10), (8, 12), (10, 14), (12, 16)]:
        roots, values = root_values(lam, n_modes)
        coeffs = remainder_coefficients(roots, values)
        interp_err = norm(eval_poly(coeffs, roots) - values)
        print(
            f"{lam:6.1f} {n_modes:4d} {len(roots):5d} "
            f"{np.max(np.abs(values)):14.3e} {norm(coeffs):14.3e} {interp_err:14.3e}"
        )


if __name__ == "__main__":
    run()
