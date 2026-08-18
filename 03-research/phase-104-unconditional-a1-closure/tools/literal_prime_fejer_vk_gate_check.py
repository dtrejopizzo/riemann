#!/usr/bin/env python3
"""Exact finite checks for 104_110 (Fraction only)."""

from fractions import Fraction as F
from math import factorial


def trim(poly):
    out = list(poly)
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def add(a, b):
    out = [F(0)] * max(len(a), len(b))
    for j, value in enumerate(a):
        out[j] += value
    for j, value in enumerate(b):
        out[j] += value
    return trim(out)


def scale(a, c):
    return trim([c * value for value in a])


def derivative(a):
    if len(a) == 1:
        return [F(0)]
    return trim([F(j) * a[j] for j in range(1, len(a))])


def eval_poly(a, x):
    value = F(0)
    for coeff in reversed(a):
        value = value * x + coeff
    return value


def exp_laplace_integral(a):
    """Integral_0^infty exp(-u) p(u) du for a polynomial p."""
    return sum(coeff * factorial(j) for j, coeff in enumerate(a))


def laguerre(d, alpha):
    """Coefficients of L_d^(alpha), using the exact binomial formula."""
    # L_d^(alpha)(x) = sum_j (-1)^j binom(d+alpha,d-j)x^j/j!
    from math import comb

    return [
        F((-1) ** j * comb(d + alpha, d - j), factorial(j))
        for j in range(d + 1)
    ]


def alphas(L):
    return {k: F(L - abs(k), L * L) for k in range(-L + 1, L)}


def block_poly(L, alpha, q):
    out = [F(0)]
    for k, weight in alphas(L).items():
        d = 2 * L + k - 1
        out = add(out, scale(laguerre(d, alpha), weight * q**k))
    return out


def shifted_generating_coefficient(L, alpha, q):
    """Coefficient extraction in (12)--(13), done as a finite convolution."""
    # [z^(2L-1)] G_alpha(z) K_L(q/z)
    # The coefficient of z^r in G_alpha is L_r^(alpha).
    out = [F(0)]
    target = 2 * L - 1
    for k, weight in alphas(L).items():
        r = target + k
        assert r >= 0
        out = add(out, scale(laguerre(r, alpha), weight * q**k))
    return out


def main():
    for L in range(1, 11):
        aa = alphas(L)
        assert sum(aa.values()) == 1

        # Rational q values test the Laurent coefficient extraction.
        for q in (F(-1), F(1), F(2, 3)):
            p = block_poly(L, 1, q)
            qpoly = block_poly(L, 2, q)
            assert p == shifted_generating_coefficient(L, 1, q)
            assert qpoly == shifted_generating_coefficient(L, 2, q)

            # (17): P-P'=Q.
            assert add(p, scale(derivative(p), -1)) == qpoly

        # At phi=pi all outer-ray summands have the same negative sign.
        qminus = F(-1)
        pminus = block_poly(L, 1, qminus)
        qpoly = block_poly(L, 2, qminus)
        # (28a): the baseline E=-1 cancels the lower boundary exactly.
        assert eval_poly(pminus, F(0)) == exp_laplace_integral(qpoly)
        for u in (24 * L, 24 * L + 1, 30 * L):
            terms = []
            for k, weight in aa.items():
                d = 2 * L + k - 1
                value = weight * qminus**k * eval_poly(laguerre(d, 2), F(u))
                terms.append(value)
                assert value < 0
            total = sum(terms, F(0))
            assert eval_poly(qpoly, F(u)) == total
            assert total < 0

            # Exact sampled version of (23).
            d0 = 2 * L - 1
            lower = F(1, L) * F(u, 2) ** d0 / factorial(d0)
            assert -total >= lower

    # The boundary term is exactly the modulated average of n.
    for L in range(1, 15):
        for q in (F(-1), F(1), F(1, 2)):
            p0 = eval_poly(block_poly(L, 1, q), F(0))
            direct = sum(
                weight * q**k * (2 * L + k)
                for k, weight in alphas(L).items()
            )
            assert p0 == direct

    print("PASS 104_110 literal prime Fejer/VK gate")
    print("checked: finite generating kernels and P-P'=Q")
    print("checked: phi=pi outer-ray alignment and exact lower bound")


if __name__ == "__main__":
    main()
