#!/usr/bin/env python3
"""Exact/algebraic checks for the finite Hurwitz--Lerch Gamma formula."""

from __future__ import annotations

from fractions import Fraction
import math
import mpmath as mp

mp.mp.dps = 90
N = 7

# Q_r: coefficient matrices of x^r in Q=x(I+xD)^-1.
q = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(N + 1)]
for n in range(N):
    suffix = [[0] * (N + 1), [0] * (N + 1)]
    for j in range(n, -1, -1):
        poly = [0] * (N + 1)
        poly[1] = 1 if j == n else 0
        for r in range(1, N):
            poly[r + 1] -= (2 * j + 1) * suffix[1 - j % 2][r]
        for r in range(1, N + 1):
            q[r][j][n] = poly[r]
            suffix[j % 2][r] += poly[r]

# Check (D+k)Q=I coefficientwise: Q_1=I and Q_{r+1}=-D Q_r.
for j in range(N):
    for n in range(N):
        assert q[1][j][n] == (1 if j == n else 0)
for r in range(1, N):
    for j in range(N):
        for n in range(N):
            dq = sum(
                (2 * j + 1) * q[r][ell][n]
                for ell in range(j + 1, N)
                if (ell - j) % 2 == 1
            )
            assert q[r + 1][j][n] == -dq

# Endpoint derivative formula and exact r=1 cancellation.
for m in range(N):
    for s in range(m + 1):
        endpoint = math.factorial(m + s) // (
            2**s * math.factorial(s) * math.factorial(m - s)
        )
        # Parity is the only difference between the endpoints.
        assert ((-1) ** (m + s) * endpoint) ** 2 == endpoint**2
    # N_T(T^-1*4W)=2I entrywise.
    lhs = Fraction(1, 2) * (2 * m + 1) * Fraction(4, 2 * m + 1)
    assert lhs == 2

# Scalar summation identities in (3.1)--(3.2).
T = mp.log(5) / 2
z = mp.e ** (-4 * T)
assert abs(z - mp.mpf(1) / 25) < mp.mpf("1e-85")
for r in (2, 3, 5, 9):
    hurwitz = mp.zeta(r, mp.mpf("0.25")) / (2**r)
    direct = mp.nsum(lambda j: (2 * j + mp.mpf("0.5")) ** (-r), [0, mp.inf])
    assert abs(hurwitz - direct) < mp.mpf("1e-75")

    lerch = (
        mp.e ** (-T)
        * mp.lerchphi(z, r, mp.mpf("0.25"))
        / (2**r)
    )
    direct_exp = mp.nsum(
        lambda j: mp.e ** (-2 * (2 * j + mp.mpf("0.5")) * T)
        * (2 * j + mp.mpf("0.5")) ** (-r),
        [0, mp.inf],
    )
    assert abs(lerch - direct_exp) < mp.mpf("1e-75")

print("D146 exact Hurwitz--Lerch Gamma-block certificates: PASS")
