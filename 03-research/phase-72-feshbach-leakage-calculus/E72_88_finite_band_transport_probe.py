#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import norm, solve

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_79_bordered_minor_probe import finite_roots, setup  # noqa: E402


def transport_residual(g, d, k, L, tau):
    one = np.ones_like(k)
    e_tau = np.exp(1j * tau * L)
    s_tau = 2 * tau / (tau * tau - d * d)
    r_minus = 1 / (tau - d)
    lhs = 1j * np.vdot(g, s_tau * k)
    rhs = (e_tau - 1) / L * np.vdot(g, s_tau * one) * np.dot(r_minus, k)
    return lhs - rhs


def run():
    s = 10 + 0.2j
    hcuts = [8, 12, 18, 24]
    print("E72.88 finite-band transport probe")
    print(" lam   N    tau Hcut     |full|     |band|     |tail-diff| tail-energy")
    for lam, n_modes in [(12, 28), (16, 34), (20, 40), (24, 48)]:
        idx, L, d, xi, k, bq, ce = setup(lam, n_modes)
        a = bq.T @ (s / (s * s - d * d))
        g = bq @ solve(ce, a)
        full_norm = norm(g) ** 2
        for tau in finite_roots(xi, d)[:3]:
            full = transport_residual(g, d, k, L, tau)
            for hcut in hcuts:
                mask = (np.abs(d) <= hcut).astype(float)
                g_band = mask * g
                band = transport_residual(g_band, d, k, L, tau)
                tail_energy = np.sum((1 - mask) * np.abs(g) ** 2) / full_norm
                print(
                    f"{lam:4.0f} {n_modes:3d} {tau:6.3f} {hcut:4.0f} "
                    f"{abs(full):10.3e} {abs(band):10.3e} "
                    f"{abs(full-band):13.3e} {tail_energy:11.3e}"
                )


if __name__ == "__main__":
    run()
