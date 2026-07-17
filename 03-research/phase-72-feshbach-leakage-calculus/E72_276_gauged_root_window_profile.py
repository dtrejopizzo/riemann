#!/usr/bin/env python3
import sys

import numpy as np
from numpy.linalg import solve

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_69_hpac_certificate_probe import finite_roots  # noqa: E402
from E72_262_pole_relative_even_setup_audit import pole_relative_even_setup_pair  # noqa: E402


def root_profile(lam, n_modes, hmax=8.0, s=10.0 + 0.2j):
    idx, L, xi, eb, c_actual, c_model, e_pole, odd_norm, even_leak = pole_relative_even_setup_pair(lam, n_modes)
    d = 2.0 * np.pi * idx / L
    roots = finite_roots(xi, d, hmax=hmax)
    a = eb.T @ (s / (s * s - d * d))
    xi_even = eb.T @ xi
    a_perp = a - xi_even * np.vdot(xi_even, a) / np.vdot(xi_even, xi_even)

    vals = []
    for tau in roots:
        alpha = 0.5 + 1j * tau
        s_tau = 2.0 * tau / (tau * tau - d * d)
        b_res = eb.T @ (1j * alpha * s_tau * xi)
        vals.append(abs(np.vdot(a_perp, solve(c_actual, b_res))))
    vals = np.array(vals)
    return L, roots, vals


def run():
    hmax = 8.0
    print("E72.276 gauged root-window profile")
    print("Residual: <a_s^perp,C_E^(-1)i alpha(tau_j)S_tau_j xi_x>.")
    print("Fixed compact height H=8; higher-height tails are a separate theorem.")
    print("lam L roots max mean")
    for lam, n_modes in [(16, 40), (20, 48), (24, 56), (28, 64), (32, 72)]:
        L, roots, vals = root_profile(lam, n_modes, hmax=hmax)
        print(
            f"{lam:3.0f} {L:.6f} {len(roots):5d} "
            f"{(np.max(vals) if len(vals) else np.nan):.6e} "
            f"{(np.mean(vals) if len(vals) else np.nan):.6e}",
            flush=True,
        )


if __name__ == "__main__":
    run()
