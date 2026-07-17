#!/usr/bin/env python3
import sys
import numpy as np

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_79_bordered_minor_probe import finite_roots, setup  # noqa: E402
from E72_91_low_band_cofactor_probe import transport_vector  # noqa: E402


def m_val(f, d, tau):
    return np.dot(1 / (tau - d), f)


def m_prime(f, d, tau):
    return -np.dot(1 / (tau - d) ** 2, f)


def run():
    print("E72.99 Weyl derivative structure probe")
    print(
        " lam   N    tau   |Mxi|     |<xi,Z>|   |<k,Z>|    "
        "|<1,Z>|    |Mk'|     |Mxi'|"
    )
    for lam, n_modes in [(8, 24), (12, 28), (16, 34), (20, 40), (24, 48)]:
        idx, L, d, xi, k, _, _ = setup(lam, n_modes)
        one = np.ones_like(k)
        for tau in finite_roots(xi, d, hmax=10.0)[:4]:
            z_tau = transport_vector(d, k, L, tau)
            print(
                f"{lam:4.0f} {n_modes:3d} {tau:6.3f} "
                f"{abs(m_val(xi,d,tau)):9.2e} "
                f"{abs(np.vdot(xi,z_tau)):10.2e} "
                f"{abs(np.vdot(k,z_tau)):10.2e} "
                f"{abs(np.vdot(one,z_tau)):10.2e} "
                f"{abs(m_prime(k,d,tau)):9.2e} "
                f"{abs(m_prime(xi,d,tau)):9.2e}"
            )


if __name__ == "__main__":
    run()
