#!/usr/bin/env python3
"""High-precision checks of the stable kernel formula in D.145."""

from __future__ import annotations

import mpmath as mp

mp.mp.dps = 90


def q_coefficients(nmax: int, k: mp.mpf) -> list[list[mp.mpf]]:
    q = [[mp.mpf("0") for _ in range(nmax)] for _ in range(nmax)]
    for n in range(nmax):
        suffix = [mp.mpf("0"), mp.mpf("0")]
        for j in range(n, -1, -1):
            rhs = mp.mpf(1) if j == n else mp.mpf(0)
            q[j][n] = (rhs - (2 * j + 1) * suffix[1 - j % 2]) / k
            suffix[j % 2] += q[j][n]
    return q


def stable_raw(nmax: int, k: mp.mpf) -> mp.matrix:
    q = q_coefficients(nmax, k)
    qminus = [sum((-1) ** j * q[j][n] for j in range(n + 1)) for n in range(nmax)]
    eminus = [
        2
        * (-1) ** m
        * mp.sqrt(mp.pi / (2 * k))
        * mp.exp(-k)
        * mp.besseli(m + mp.mpf("0.5"), k)
        for m in range(nmax)
    ]
    ans = mp.matrix(nmax)
    for m in range(nmax):
        for n in range(nmax):
            tri_mn = 2 * q[m][n] / (2 * m + 1) - eminus[m] * qminus[n]
            tri_nm = 2 * q[n][m] / (2 * n + 1) - eminus[n] * qminus[m]
            ans[m, n] = tri_mn + tri_nm
    return ans


for k_text in ("0.4", "2", "10", "50", "250"):
    k = mp.mpf(k_text)
    nmax = 8
    coeff = q_coefficients(nmax, k)
    a = stable_raw(nmax, k)

    # Independent check of the triangular polynomial solve at sample
    # points: Q_n' + k Q_n = P_n.
    for n in range(nmax):
        def qpoly(u: mp.mpf) -> mp.mpf:
            return sum(coeff[j][n] * mp.legendre(j, u) for j in range(n + 1))

        for u_text in ("-0.73", "-0.1", "0.37", "0.88"):
            u = mp.mpf(u_text)
            residual = mp.diff(qpoly, u) + k * qpoly(u) - mp.legendre(n, u)
            assert abs(residual) < mp.mpf("1e-68")

    # Symmetry and the closed constant-mode formula.
    for m in range(nmax):
        for n in range(nmax):
            assert abs(a[m, n] - a[n, m]) < mp.mpf("1e-70")
    exact00 = 4 / k - 2 * (1 - mp.exp(-2 * k)) / k**2
    assert abs(a[0, 0] - exact00) < mp.mpf("1e-70")

    # Independent one-dimensional quadrature of the scaled Bessel boundary
    # integral used in the correction term.
    for m in (0, 1, 2, 5, 7):
        direct_boundary = mp.quad(
            lambda u: mp.legendre(m, u) * mp.exp(-k * (u + 1)),
            [-1, 1],
        )
        bessel_boundary = (
            2
            * (-1) ** m
            * mp.sqrt(mp.pi / (2 * k))
            * mp.exp(-k)
            * mp.besseli(m + mp.mpf("0.5"), k)
        )
        assert abs(direct_boundary - bessel_boundary) < mp.mpf("1e-68")

print("D145 stable Legendre--Gamma kernel certificates: PASS")
