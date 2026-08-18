#!/usr/bin/env python3
"""Exact lattice certificates for D.75.

We use the lattice spacing R=2 log(2), so exp(R/2)=2 and both primitive
characters are rational.  The script checks:

* the explicit primitive three-delta vector;
* exact cancellation of both tails of its Green potential;
* stability of the primitive ideal under convolution;
* the bimodule identity W(mu*nu)=mu*W(nu);
* decay of the approximate-identity error bound.
"""

from fractions import Fraction


def conv(a, b):
    out = {}
    for i, x in a.items():
        for j, y in b.items():
            out[i + j] = out.get(i + j, Fraction(0)) + x * y
    return {k: v for k, v in out.items() if v}


def moment(mu, sign):
    # exp(sign * nR/2)=2**(sign*n)
    ans = Fraction(0)
    for n, c in mu.items():
        weight = Fraction(2 ** n) if sign == 1 and n >= 0 else None
        if sign == 1 and n < 0:
            weight = Fraction(1, 2 ** (-n))
        if sign == -1 and n <= 0:
            weight = Fraction(2 ** (-n))
        if sign == -1 and n > 0:
            weight = Fraction(1, 2 ** n)
        ans += c * weight
    return ans


def green_potential(mu, n):
    # Common harmless normalization suppressed: G(n-j)=-2**(-abs(n-j)).
    return -sum(c * Fraction(1, 2 ** abs(n - j)) for j, c in mu.items())


def module_rhs(mu, nu, n):
    return sum(c * green_potential(nu, n - j) for j, c in mu.items())


def main():
    # epsilon_R for R=2 log 2: 1/(2 cosh(R/2))=2/5.
    eps = {-1: Fraction(-2, 5), 0: Fraction(1), 1: Fraction(-2, 5)}
    assert moment(eps, 1) == 0
    assert moment(eps, -1) == 0

    # The potential vanishes identically outside the convex hull [-1,1].
    for n in range(-8, -1):
        assert green_potential(eps, n) == 0
    for n in range(2, 9):
        assert green_potential(eps, n) == 0

    # Ideal stability.
    eps2 = conv(eps, eps)
    assert moment(eps2, 1) == 0
    assert moment(eps2, -1) == 0

    # Exact bimodule law W(eps*eps)=eps*W(eps).
    for n in range(-8, 9):
        assert green_potential(eps2, n) == module_rhs(eps, eps, n)

    # For R_N=2N log 2, the translation error is <=1/cosh(N log 2).
    bounds = []
    for n in (1, 2, 4, 8):
        bound = Fraction(2 ** (n + 1), 4 ** n + 1)
        bounds.append(bound)
    assert all(bounds[i + 1] < bounds[i] for i in range(len(bounds) - 1))

    print("D75 primitive-potential certificates: PASS")
    print("exact approximate-identity bounds:", bounds)


if __name__ == "__main__":
    main()
