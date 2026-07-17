#!/usr/bin/env python3
"""Evaluate the Phase 74 nodal observable on Davenport--Heilbronn CCM data."""

import sys

import numpy as np
from numpy.linalg import eigh, norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-60-discriminant/experiments")

from E5_ldh_violator import KAPPA, build_QW, ldh_b_upto  # noqa: E402


DH_CRITICAL = [5.094159844571, 14.40400311, 19.30880017, 26.094967, 33.699512, 35.891]
DH_OFFLINE = 0.308517 + 1j * 85.699348


def normalized_cauchy(z, d, xi):
    row = 1.0 / (z - d)
    return abs(np.dot(row / norm(row), xi))


def run_case(lam, n_modes, dt):
    # The archimedean quadrature only builds H.  The nodal observable itself
    # is evaluated directly from the resulting finite Weyl numerator.
    tgrid = np.arange(-220.0, 220.0, dt) + 3e-6
    coeffs = ldh_b_upto(int(lam * lam))
    h, idx, L = build_QW(
        lam,
        n_modes,
        a_arch=0.75,
        cond=5.0,
        coeffs=coeffs,
        use_pole=False,
        tgrid=tgrid,
    )
    vals, vecs = eigh(h)
    xi = vecs[:, 0]
    xi = (xi + xi[::-1]) / 2.0
    xi /= norm(xi)
    d = 2.0 * np.pi * idx / L

    print(f"kappa={KAPPA:.9f} L={L:.3f} N={n_modes} dt={dt:.4f} dmax={max(abs(d)):.2f} mu={vals[0]:.3e}")
    print("node                         reach       normalized-Cauchy")
    for gamma in DH_CRITICAL:
        print(f"critical {gamma:10.6f}       {max(abs(d))/gamma:5.2f}       {normalized_cauchy(gamma,d,xi):.3e}")
    # For rho=1/2+alpha+i gamma, the shifted Cauchy node is gamma+i alpha.
    zoff = DH_OFFLINE.imag + 1j * DH_OFFLINE.real
    print(
        f"off-line {zoff.real:10.6f}+{zoff.imag:.6f}i"
        f"   {max(abs(d))/abs(zoff):5.2f}       {normalized_cauchy(zoff,d,xi):.3e}"
    )


def run():
    print("E74.26 Davenport--Heilbronn nodal falsifier")
    for n_modes, dt in [(58, 0.05), (58, 0.025), (64, 0.025)]:
        run_case(7.0, n_modes, dt)


if __name__ == "__main__":
    run()
