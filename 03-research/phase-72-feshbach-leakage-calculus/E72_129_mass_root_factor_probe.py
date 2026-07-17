#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import norm, solve

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_79_bordered_minor_probe import finite_roots  # noqa: E402
from E72_112_operator_split_probe import (  # noqa: E402
    lk_matrix,
    sigma_packet,
    weighted_even_matrix,
)


def m_val(f, d, tau):
    return np.dot(f / (tau - d), np.ones_like(f))


def m_prime(f, d, tau):
    return -np.dot(f / (tau - d) ** 2, np.ones_like(f))


def mass_row(L, idx, d, k, bq, c_actual):
    mask = (np.abs(d) <= 8.0).astype(float)
    w = weighted_even_matrix(idx, mask)
    lk = lk_matrix(d, k)
    factor = 2.0 / (L * np.sqrt(np.exp(L)))
    qshort = bq @ solve(c_actual, bq.T)
    return np.ones(w.shape[0], dtype=complex) @ w @ (mask[:, None] * qshort) @ (
        mask[:, None] * (factor * lk)
    )


def nearest_distance(tau, roots):
    if len(roots) == 0:
        return np.nan
    return np.min(np.abs(roots - tau))


def run():
    print("E72.129 mass root-factor probe")
    print(
        " lam   L roots  max|mass|  med L2mass/|Mk|  med mass/|Mkp|  "
        "med mass/|Mxip|  med rootGap"
    )
    for lam, n_modes in [(8, 24), (10, 28), (12, 32), (14, 36), (16, 40)]:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        roots_a = finite_roots(xi, d, hmax=6.0)
        roots_m = finite_roots(k, d, hmax=6.0)
        if len(roots_a) == 0:
            continue
        mrow = mass_row(L, idx, d, k, bq, c_actual)
        masses = []
        r_mk = []
        r_mkp = []
        r_mxip = []
        gaps = []
        for tau in roots_a[:6]:
            y = sigma_packet(L, d, tau)
            mass = abs(mrow @ y)
            masses.append(mass)
            mk = abs(m_val(k, d, tau))
            mkp = abs(m_prime(k, d, tau))
            mxip = abs(m_prime(xi, d, tau))
            r_mk.append((L * L * mass) / max(mk, 1e-30))
            r_mkp.append(mass / max(mkp, 1e-30))
            r_mxip.append(mass / max(mxip, 1e-30))
            gaps.append(nearest_distance(tau, roots_m))
        print(
            f"{lam:4.0f} {L:5.2f} {len(roots_a):5d} {max(masses):10.3e} "
            f"{np.median(r_mk):15.3e} {np.median(r_mkp):15.3e} "
            f"{np.median(r_mxip):16.3e} {np.median(gaps):12.3e}"
        )


if __name__ == "__main__":
    run()
