#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import solve

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_79_bordered_minor_probe import finite_roots, setup  # noqa: E402
from E72_91_low_band_cofactor_probe import transport_vector  # noqa: E402


def m_prime(f, d, tau):
    return -np.dot(1 / (tau - d) ** 2, f)


def run():
    s = 10 + 0.2j
    hcut = 18
    print("E72.100 derivative normalization probe")
    print(" lam   N    tau      |D2|      |Mxi'|    |D2/Mxi'|  |<xi,Z>/Mxi'|")
    for lam, n_modes in [(8, 24), (12, 28), (16, 34), (20, 40), (24, 48)]:
        idx, L, d, xi, k, bq, ce = setup(lam, n_modes)
        mask = (np.abs(d) <= hcut).astype(float)
        a = bq.T @ (s / (s * s - d * d))
        for tau in finite_roots(xi, d, hmax=10.0)[:4]:
            z_tau = transport_vector(d, k, L, tau)
            c_tau = bq.T @ (mask * z_tau)
            d2 = np.vdot(a, solve(ce, c_tau))
            mp = m_prime(xi, d, tau)
            xiz = np.vdot(xi, z_tau)
            print(
                f"{lam:4.0f} {n_modes:3d} {tau:6.3f} "
                f"{abs(d2):10.3e} {abs(mp):10.3e} "
                f"{abs(d2/mp):11.3e} {abs(xiz/mp):14.3e}"
            )


if __name__ == "__main__":
    run()
