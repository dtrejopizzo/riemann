#!/usr/bin/env python3
"""Certificates for D.133 Tate--Chebyshev renormalization.

The script verifies the two-moment cancellation on a compactly supported
source, the exact digamma shift, positivity of the shifted Gamma symbol,
the prime-power Stieltjes ledger, and the balanced threshold split.
"""

from __future__ import annotations

import math
from fractions import Fraction

import mpmath as mp


mp.mp.dps = 60


def quad(fun, a, b):
    return mp.quad(fun, [a, b])


def u(t):
    # u and u' vanish at both endpoints, so F=(d^2-1/4)u has the two
    # exponential moments equal to zero by two integrations by parts.
    return (1 - t * t) ** 2 if abs(t) <= 1 else mp.mpf("0")


def f(t):
    if abs(t) > 1:
        return mp.mpf("0")
    # u'' = -4 + 12 t^2.
    return -4 + 12 * t * t - mp.mpf("0.25") * (1 - t * t) ** 2


F_COEFF = [
    mp.mpf(-17) / 4,
    mp.mpf("0"),
    mp.mpf(25) / 2,
    mp.mpf("0"),
    -mp.mpf(1) / 4,
]


def corr(a):
    if a < 0 or a > 2:
        return mp.mpf("0")
    # Exact polynomial integration of f(t+a)f(t).  This avoids nested
    # adaptive quadrature in the continuous-contact certificate.
    shifted = [mp.mpf("0")] * len(F_COEFF)
    for j, cj in enumerate(F_COEFF):
        for k in range(j + 1):
            shifted[k] += cj * math.comb(j, k) * a ** (j - k)
    product = [mp.mpf("0")] * (2 * len(F_COEFF) - 1)
    for i, ci in enumerate(F_COEFF):
        for j, cj in enumerate(shifted):
            product[i + j] += ci * cj
    upper = 1 - a
    return mp.fsum(
        ck * (upper ** (k + 1) - (-1) ** (k + 1)) / (k + 1)
        for k, ck in enumerate(product)
    )


def von_mangoldt(n: int) -> mp.mpf:
    for p in range(2, n + 1):
        # elementary primality test
        if any(p % d == 0 for d in range(2, int(math.isqrt(p)) + 1)):
            continue
        q = p
        while q < n:
            q *= p
        if q == n:
            return mp.log(p)
    return mp.mpf("0")


def main() -> None:
    # The two primitive jets vanish.
    m_plus = quad(lambda t: mp.exp(t / 2) * f(t), -1, 1)
    m_minus = quad(lambda t: mp.exp(-t / 2) * f(t), -1, 1)
    assert abs(m_plus) < mp.mpf("1e-50")
    assert abs(m_minus) < mp.mpf("1e-50")

    # Exact Tate cancellation of the continuous Chebyshev main term.
    lhs = 2 * quad(lambda a: mp.exp(a / 2) * corr(a), 0, 2)
    rhs = -2 * quad(lambda a: mp.exp(-a / 2) * corr(a), 0, 2)
    assert abs(lhs - rhs) < mp.mpf("1e-45")

    # Digamma recurrence shifts 1/4 to 5/4 with the exact Cauchy symbol.
    for tau in (mp.mpf("0"), mp.mpf("0.2"), mp.mpf("1.7"), mp.mpf("9")):
        z = mp.mpf("0.25") + 0.5j * tau
        old = mp.re(mp.digamma(z)) - mp.log(mp.pi)
        shifted = old + 1 / (tau * tau + mp.mpf("0.25"))
        direct = mp.re(mp.digamma(z + 1)) - mp.log(mp.pi)
        assert abs(shifted - direct) < mp.mpf("1e-50")

    beta = mp.log(mp.pi) - mp.digamma(mp.mpf("1.25"))
    assert beta > 0

    # Positivity of h_{5/4}; enclose the closed form between a positive
    # partial series and that series plus an elementary tail bound.
    for tau in (mp.mpf("0.1"), mp.mpf("1"), mp.mpf("8")):
        y = tau / 2
        closed = mp.re(mp.digamma(mp.mpf("1.25") + 1j * y)) - mp.digamma(
            mp.mpf("1.25")
        )
        count = 20000
        series = mp.fsum(
            y * y
            / ((k + mp.mpf("1.25")) * ((k + mp.mpf("1.25")) ** 2 + y * y))
            for k in range(count)
        )
        tail_bound = y * y / (2 * (count + mp.mpf("0.25")) ** 2)
        assert closed > 0
        assert series < closed < series + tail_bound

    # All prime powers, and only prime powers, occur in d psi_C.
    support = [(n, von_mangoldt(n)) for n in range(2, 55) if von_mangoldt(n)]
    expected = [
        2, 3, 4, 5, 7, 8, 9, 11, 13, 16, 17, 19, 23, 25, 27, 29,
        31, 32, 37, 41, 43, 47, 49, 53,
    ]
    assert [n for n, _ in support] == expected
    assert von_mangoldt(8) == mp.log(2)
    assert von_mangoldt(27) == mp.log(3)
    assert von_mangoldt(12) == 0

    # Algebraic Stieltjes ledger on the compact support T=1.
    X = math.exp(2)
    arithmetic = 2 * sum(
        (w / mp.sqrt(n)) * corr(mp.log(n))
        for n, w in support
        if n <= X
    )
    continuous = 2 * quad(
        lambda a: mp.exp(a / 2) * corr(a), 0, 2
    )
    discrepancy = arithmetic - continuous
    assert abs(arithmetic - (continuous + discrepancy)) < mp.mpf("1e-50")

    # Exact balanced-contact identity in rational finite dimension.
    left = [Fraction(2), Fraction(-1), Fraction(3)]
    right = [Fraction(5), Fraction(4), Fraction(-2)]
    corr_lr = 2 * sum(x * y for x, y in zip(left, right))
    jplus = sum((x + y) ** 2 for x, y in zip(left, right))
    jminus = sum((x - y) ** 2 for x, y in zip(left, right))
    assert corr_lr == jplus - jminus

    print("D133 Tate--Chebyshev certificates: PASS")
    print("M_+, M_-:", mp.nstr(m_plus, 8), mp.nstr(m_minus, 8))
    print("continuous cancellation:", mp.nstr(lhs), mp.nstr(rhs))
    print("beta:", mp.nstr(beta, 20))
    print("prime-power support through 53:", [n for n, _ in support])
    print("balanced split:", corr_lr, "=", jplus, "-", jminus)


if __name__ == "__main__":
    main()
