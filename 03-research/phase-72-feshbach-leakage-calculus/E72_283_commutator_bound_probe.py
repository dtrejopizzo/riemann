#!/usr/bin/env python3
import sys

import numpy as np
from numpy.linalg import eigvalsh, norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_69_hpac_certificate_probe import finite_roots  # noqa: E402
from E72_262_pole_relative_even_setup_audit import pole_relative_even_setup_pair  # noqa: E402


def commutator_scale(lam, n_modes, hmax=8.0, s=10.0 + 0.2j):
    idx, L, xi, eb, c_actual, c_model, e_pole, odd_norm, even_leak = pole_relative_even_setup_pair(lam, n_modes)
    d = 2.0 * np.pi * idx / L
    vals = eigvalsh(c_actual)
    mu = float(vals[0])
    op_c = float(vals[-1])

    xi_even = eb.T @ xi
    a = eb.T @ (s / (s * s - d * d))
    a_perp = a - xi_even * np.vdot(xi_even, a) / np.vdot(xi_even, xi_even)

    max_sxi = 0.0
    for tau in finite_roots(xi, d, hmax=hmax):
        s_diag = 2.0 * tau / (tau * tau - d * d)
        s_even = eb.T @ (s_diag[:, None] * eb)
        max_sxi = max(max_sxi, norm(s_even @ xi_even))

    crude = norm(a_perp) * op_c * max_sxi / (mu * mu)
    return L, mu, op_c, norm(a_perp), max_sxi, crude


def run():
    print("E72.283 commutator-bound probe")
    print("Crude compact-root commutator scale: ||a|| ||C_E|| ||S_tau xi|| / mu^2.")
    print("lam L mu opC opC/L2 ||a|| max||Sxi|| crude")
    for lam, n_modes in [(16, 40), (20, 48), (24, 56), (28, 64), (32, 72)]:
        L, mu, op_c, a_norm, max_sxi, crude = commutator_scale(lam, n_modes)
        print(
            f"{lam:3.0f} {L:.6f} {mu:.6e} {op_c:.6e} "
            f"{op_c / (L * L):.6e} {a_norm:.6e} {max_sxi:.6e} {crude:.6e}",
            flush=True,
        )


if __name__ == "__main__":
    run()
