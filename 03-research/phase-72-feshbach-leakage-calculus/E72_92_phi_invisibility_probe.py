#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import norm, solve

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_79_bordered_minor_probe import finite_roots, setup  # noqa: E402
from E72_91_low_band_cofactor_probe import transport_vector  # noqa: E402


def run():
    s = 10 + 0.2j
    hcut = 18
    print("E72.92 phi norm vs Cauchy invisibility probe")
    print("   lam    N      tau       ||phi||      |pair|    |pair|/||phi||")
    for lam, n_modes in [(8, 24), (12, 28), (16, 34), (20, 40), (24, 48)]:
        idx, L, d, xi, k, bq, ce = setup(lam, n_modes)
        mask = (np.abs(d) <= hcut).astype(float)
        r_even = s / (s * s - d * d)
        for tau in finite_roots(xi, d, hmax=10.0)[:4]:
            z_tau = transport_vector(d, k, L, tau)
            c_tau = bq.T @ (mask * z_tau)
            phi = bq @ solve(ce, c_tau)
            pair = np.vdot(r_even, phi)
            print(
                f"{lam:6.1f} {n_modes:4d} {tau:8.3f} "
                f"{norm(phi):12.3e} {abs(pair):11.3e} "
                f"{abs(pair)/max(norm(phi),1e-30):15.3e}"
            )


if __name__ == "__main__":
    run()
