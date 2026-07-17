#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import det, solve

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_79_bordered_minor_probe import finite_roots, setup  # noqa: E402
from E72_91_low_band_cofactor_probe import transport_vector  # noqa: E402


def bordered_pairing(ce, a, c):
    top = np.column_stack([ce.astype(complex), c])
    bottom = np.concatenate([np.conjugate(a), np.array([0.0 + 0.0j])])[None, :]
    bordered = np.vstack([top, bottom])
    return -det(bordered) / det(ce)


def run():
    s = 10 + 0.2j
    hcut = 18
    print("E72.97 FBRT bordered minor probe")
    print("   lam    N      tau      |solve|       absdiff      reldiff")
    for lam, n_modes in [(6, 10), (8, 12), (10, 14), (12, 16)]:
        idx, L, d, xi, k, bq, ce = setup(lam, n_modes)
        mask = (np.abs(d) <= hcut).astype(float)
        a = bq.T @ (s / (s * s - d * d))
        for tau in finite_roots(xi, d, hmax=10.0)[:4]:
            z_tau = transport_vector(d, k, L, tau)
            c_tau = bq.T @ (mask * z_tau)
            direct = np.vdot(a, solve(ce, c_tau))
            minor = bordered_pairing(ce, a, c_tau)
            absdiff = abs(direct - minor)
            reldiff = absdiff / max(abs(direct), 1e-30)
            print(
                f"{lam:6.1f} {n_modes:4d} {tau:8.3f} "
                f"{abs(direct):12.3e} {absdiff:12.3e} {reldiff:12.3e}"
            )


if __name__ == "__main__":
    run()
