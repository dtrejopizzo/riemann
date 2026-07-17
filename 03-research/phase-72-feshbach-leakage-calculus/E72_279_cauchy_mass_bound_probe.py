#!/usr/bin/env python3
import sys

import numpy as np

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_262_pole_relative_even_setup_audit import pole_relative_even_setup_pair  # noqa: E402


def mass_bound(lam, n_modes, s=10.0 + 0.2j):
    idx, L, xi, eb, c_actual, c_model, e_pole, odd_norm, even_leak = pole_relative_even_setup_pair(lam, n_modes)
    d = 2.0 * np.pi * idx / L
    z = np.conjugate(s)
    xi_even = eb.T @ xi
    mu = float((np.vdot(xi_even, c_actual @ xi_even) / np.vdot(xi_even, xi_even)).real)
    kernel = 1.0 / (z * z - d * d)
    m_z = np.sum(xi * kernel)
    cs = np.sqrt(np.sum(np.abs(kernel) ** 2))
    return L, mu, abs(m_z), cs, abs(m_z) / mu, cs / mu, cs / np.sqrt(L)


def run():
    print("E72.279 Cauchy-mass bound probe")
    print("Uses |M_x(z)| <= ||xi_x||_2 (sum |z^2-d_n^2|^-2)^1/2 and mu in the pole-even complement.")
    print("s=10+0.2i, z=conj(s).")
    print("lam L mu |M| CS |M|/mu CS/mu CS/sqrtL")
    for lam, n_modes in [(16, 40), (20, 48), (24, 56), (28, 64), (32, 72)]:
        L, mu, m_z, cs, ratio, cs_ratio, scaled = mass_bound(lam, n_modes)
        print(
            f"{lam:3.0f} {L:.6f} {mu:.6e} "
            f"{m_z:.6e} {cs:.6e} {ratio:.6e} "
            f"{cs_ratio:.6e} {scaled:.6e}",
            flush=True,
        )


if __name__ == "__main__":
    run()
