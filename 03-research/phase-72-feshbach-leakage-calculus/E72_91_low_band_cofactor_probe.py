#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import solve

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_79_bordered_minor_probe import finite_roots, setup  # noqa: E402
from E72_88_finite_band_transport_probe import transport_residual  # noqa: E402


def transport_vector(d, k, L, tau):
    one = np.ones_like(k)
    e_tau = np.exp(1j * tau * L)
    s_tau = 2 * tau / (tau * tau - d * d)
    m_k = np.dot(1 / (tau - d), k)
    beta = (e_tau - 1) / L * m_k
    return 1j * s_tau * k - beta * s_tau * one


def run():
    s = 10 + 0.2j
    hcut = 18
    print("E72.91 low-band cofactor identity probe")
    print("   lam    N      tau      |direct|     |cofactor|      diff")
    for lam, n_modes in [(8, 24), (12, 28), (16, 34), (20, 40), (24, 48)]:
        idx, L, d, xi, k, bq, ce = setup(lam, n_modes)
        mask = (np.abs(d) <= hcut).astype(float)
        a = bq.T @ (s / (s * s - d * d))
        y = solve(ce, a)
        g = bq @ y
        for tau in finite_roots(xi, d, hmax=10.0)[:4]:
            z_tau = transport_vector(d, k, L, tau)
            direct = transport_residual(mask * g, d, k, L, tau)
            c_tau = bq.T @ (mask * z_tau)
            cofactor = np.vdot(y, c_tau)
            dual = np.vdot(a, solve(ce, c_tau))
            diff = max(abs(direct - cofactor), abs(direct - dual))
            print(
                f"{lam:6.1f} {n_modes:4d} {tau:8.3f} "
                f"{abs(direct):12.3e} {abs(cofactor):12.3e} {diff:9.2e}"
            )


if __name__ == "__main__":
    run()
