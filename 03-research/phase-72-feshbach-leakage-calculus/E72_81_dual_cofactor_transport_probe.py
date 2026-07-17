#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import solve

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_79_bordered_minor_probe import finite_roots, setup  # noqa: E402


def run():
    s = 10 + 0.2j
    print("E72.81 dual cofactor transport probe")
    print("   lam    N      tau      |direct|     fact.diff     root.diff")
    for lam, n_modes in [(8, 12), (10, 14), (12, 16), (16, 20)]:
        idx, L, d, xi, k, bq, ce = setup(lam, n_modes)
        one = np.ones_like(k)
        h = k - xi
        r_even = s / (s * s - d * d)
        a = bq.T @ r_even
        y = solve(ce, a)
        g = bq @ y
        for tau in finite_roots(xi, d)[:4]:
            e_tau = np.exp(1j * tau * L)
            s_tau = 2 * tau / (tau * tau - d * d)
            r_minus = 1 / (tau - d)

            w = 1j * s_tau * k - (e_tau - 1) / L * s_tau * np.dot(r_minus, h)
            direct = np.vdot(g, w)

            c_gk = np.vdot(g, s_tau * k)
            c_g1 = np.vdot(g, s_tau * one)
            m_h = np.dot(r_minus, h)
            m_k = np.dot(r_minus, k)
            factored = 1j * c_gk - (e_tau - 1) / L * c_g1 * m_h
            root_form = 1j * c_gk - (e_tau - 1) / L * c_g1 * m_k
            print(
                f"{lam:6.1f} {n_modes:4d} {tau:8.3f} "
                f"{abs(direct):12.3e} {abs(direct-factored):12.3e} "
                f"{abs(factored-root_form):12.3e}"
            )


if __name__ == "__main__":
    run()
