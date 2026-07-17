#!/usr/bin/env python3
"""P75.010: finite numerator scaling and falsifier harness."""

import sys

import numpy as np
from numpy.linalg import cond, eigh, norm, svd
from scipy.optimize import newton

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-60-discriminant/experiments")

from E71_2_convergence_detector import build_QW as build_zeta_qw  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E5_ldh_violator import build_QW as build_dh_qw, ldh_b_upto  # noqa: E402


def cauchy(t, d, xi):
    return float(np.sum(xi / (t - d)))


def cauchy_prime(t, d, xi):
    return float(np.sum(-xi / (t - d) ** 2))


def local_root(gamma, d, xi):
    try:
        return float(
            newton(
                lambda t: cauchy(t, d, xi),
                gamma,
                fprime=lambda t: cauchy_prime(t, d, xi),
                tol=1e-12,
                maxiter=40,
            )
        )
    except (RuntimeError, OverflowError, ZeroDivisionError):
        return np.nan


def normalized_value(z, d, xi):
    row = 1.0 / (z - d)
    return abs(np.dot(row / norm(row), xi))


def gram_condition(gamma, d):
    q = np.vstack([1.0 / (gamma - d), 1.0 / (-gamma - d)])
    return cond(q @ q.T)


def schur_singulars(gamma, d, h, mu):
    q = np.vstack([1.0 / (gamma - d), 1.0 / (-gamma - d)])
    qq = q @ q.T
    qhq = q @ h @ q.T
    t = mu * np.eye(2) - qhq @ np.linalg.inv(qq)
    return svd(t, compute_uv=False)


def ground_data_zeta(lam, n_modes, planted=None):
    h, idx, L = build_zeta_qw(lam, n_modes, planted=planted)
    vals, vecs = eigh(h)
    xi = vecs[:, 0]
    xi = (xi + xi[::-1]) / 2.0
    xi /= norm(xi)
    d = 2.0 * np.pi * idx / L
    return h, d, xi, vals[0], L


def ground_data_dh(lam, n_modes, dt=0.05):
    tgrid = np.arange(-220.0, 220.0, dt) + 3e-6
    coeffs = ldh_b_upto(int(lam * lam))
    h, idx, L = build_dh_qw(
        lam,
        n_modes,
        a_arch=0.75,
        cond=5.0,
        coeffs=coeffs,
        use_pole=False,
        tgrid=tgrid,
    )
    vals, vecs = eigh(h)
    xi = vecs[:, 0]
    xi = (xi + xi[::-1]) / 2.0
    xi /= norm(xi)
    d = 2.0 * np.pi * idx / L
    return h, d, xi, vals[0], L


def random_symbol(n=24, L=12.0):
    rng = np.random.default_rng(7510)
    idx = np.r_[np.arange(-n, 0), np.arange(1, n + 1)]
    d = 2.0 * np.pi * idx / L
    a = rng.normal(size=(len(d), len(d)))
    h = (a + a.T) / 2.0
    vals, vecs = eigh(h)
    xi = vecs[:, 0]
    xi = (xi + xi[::-1]) / 2.0
    xi /= norm(xi)
    return h, d, xi, vals[0], L


def random_kerq(gamma, d):
    rng = np.random.default_rng(7511)
    q = np.vstack([1.0 / (gamma - d), 1.0 / (-gamma - d)])
    u, s, vh = svd(q)
    basis = vh[2:, :]
    coeff = rng.normal(size=basis.shape[0])
    xi = coeff @ basis
    return xi / norm(xi)


def report_case(tag, h, d, xi, mu, L, gammas):
    print(f"\n{tag} L={L:.3f} N={len(d)} dmax={max(abs(d)):.3f} mu={mu:.3e}")
    print("gamma       normQ        rootShift      |Cprime(root)|  gramCond      smin(T)      smax(T)")
    for gamma in gammas:
        tau = local_root(gamma, d, xi)
        deriv = abs(cauchy_prime(tau, d, xi)) if np.isfinite(tau) else np.nan
        svals = schur_singulars(gamma, d, h, mu)
        print(
            f"{gamma:8.3f} {normalized_value(gamma,d,xi):11.3e}"
            f" {tau-gamma if np.isfinite(tau) else np.nan:13.3e}"
            f" {deriv:15.3e} {gram_condition(gamma,d):10.3e}"
            f" {min(svals):11.3e} {max(svals):11.3e}"
        )


def run():
    print("P75.010 scaling and falsifier harness")
    gammas = GAMMAS[:3]

    report_case("zeta", *ground_data_zeta(12, 24), gammas)
    report_case("planted", *ground_data_zeta(12, 24, planted=(25.0, 0.30, 5.0)), gammas)
    report_case("Davenport-Heilbronn", *ground_data_dh(7.0, 58, dt=0.05), [5.094159844571, 14.40400311, 19.30880017])
    report_case("random-symbol", *random_symbol(), gammas)

    h, d, xi, mu, L = ground_data_zeta(12, 24)
    gamma = gammas[0]
    ker_xi = random_kerq(gamma, d)
    print(f"\nrandom-kerQ L={L:.3f} gamma={gamma:.3f}")
    print(f"normQ_at_gamma={normalized_value(gamma,d,ker_xi):.3e}")
    print(f"normQ_at_next_gamma={normalized_value(gammas[1],d,ker_xi):.3e}")


if __name__ == "__main__":
    run()

