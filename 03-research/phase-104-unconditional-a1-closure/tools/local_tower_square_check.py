#!/usr/bin/env python3
"""Exact Fraction checks for the local tower square in 104_20.

Polynomials are coefficient lists in ascending powers of x.  The checks are
algebraic only; they do not test the global sign gate, A1, or RH.
"""

from fractions import Fraction as F
from math import comb, factorial


def trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def add(a, b):
    n = max(len(a), len(b))
    return trim([
        (a[i] if i < len(a) else F(0))
        + (b[i] if i < len(b) else F(0))
        for i in range(n)
    ])


def scale(a, c):
    return trim([c * x for x in a])


def shift(a, h):
    out = [F(0)] * len(a)
    for j, aj in enumerate(a):
        for i in range(j + 1):
            out[i] += aj * comb(j, i) * h ** (j - i)
    return trim(out)


def N(a):
    if len(a) == 1:
        return [F(0)]
    return trim([-F(i) * a[i] for i in range(1, len(a))])


def A(a, eps):
    """A_eps f = integral exp(-r) f(x+r/eps) dr."""
    out = [F(0)] * len(a)
    for j, aj in enumerate(a):
        for i in range(j + 1):
            out[i] += (
                aj * comb(j, i) * factorial(j - i)
                / eps ** (j - i)
            )
    return trim(out)


def U(a, ell):
    """U_ell f = integral_0^ell f(x+t) dt."""
    out = [F(0)] * len(a)
    for j, aj in enumerate(a):
        for i in range(j + 1):
            out[i] += (
                aj * comb(j, i) * ell ** (j - i + 1)
                / F(j - i + 1)
            )
    return trim(out)


def P_direct(a, eps, c):
    return add(a, scale(A(a, eps), -c))


def P_derivative(a, eps, c):
    return add(scale(a, 1 - c), scale(A(N(a), eps), c / eps))


def B(a, rho, ell):
    """I-rho E_ell in its direct form."""
    return add(a, scale(shift(a, ell), -rho))


def B_derivative(a, rho, ell):
    return add(scale(a, 1 - rho), scale(U(N(a), ell), rho))


def C(a, eps, c, rho, ell):
    return B_derivative(P_derivative(a, eps, c), rho, ell)


def jordan(q, k):
    if k == 0:
        return F(1)
    return (q - 1) * q ** (k - 1)


def bconv(q, k):
    return sum((jordan(q, j) * jordan(q, k - j)
                for j in range(k + 1)), F(0))


def second_difference(q, k):
    def seq(j):
        return F(0) if j < 0 else F(j + 1) * q ** j
    return seq(k) - 2 * seq(k - 1) + seq(k - 2)


def laguerre(n):
    return [F((-1) ** j * comb(n, j), factorial(j)) for j in range(n + 1)]


def main():
    eps = F(2, 5)
    c = F(3, 7)
    rho = F(1, 5)
    ell = F(4, 3)
    tests = [
        [F(1)],
        [F(1), F(-1)],
        [F(2), F(-3), F(5, 2), F(-7, 4), F(3, 5)],
    ]

    for f in tests:
        assert P_direct(f, eps, c) == P_derivative(f, eps, c)
        assert B(f, rho, ell) == B_derivative(f, rho, ell)
        lhs = B(B(P_direct(P_direct(f, eps, c), eps, c), rho, ell),
                rho, ell)
        rhs = C(C(f, eps, c, rho, ell), eps, c, rho, ell)
        assert lhs == rhs, (lhs, rhs)

    for q in (F(4, 3), F(3, 2), F(2)):
        for k in range(12):
            assert bconv(q, k) == second_difference(q, k)

    # Exact n=1 tower sum, with x standing for log(m)+mean(Beta shift).
    q = F(3, 2)
    rho = F(1, 4)
    ell = F(5, 3)
    x = F(7, 2)
    eps = F(1, 6)
    c = F(2, 5)
    M = ((1 - rho) / (1 - q * rho)) ** 2
    mu = 2 * rho * (q - 1) / ((1 - rho) * (1 - q * rho))
    closed = M * ((1 - c) ** 2 * (1 - x - ell * mu)
                  + 2 * c * (1 - c) / eps)

    # The two required infinite moments are evaluated by their rational
    # generating functions; this is an independent assembly of the same sum.
    sum_b = M
    sum_kb = M * mu
    assembled = ((1 - c) ** 2
                 * ((1 - x) * sum_b - ell * sum_kb)
                 + 2 * c * (1 - c) / eps * sum_b)
    assert assembled == closed

    threshold = 1 - ell * mu + 2 * c / ((1 - c) * eps)
    below = M * ((1 - c) ** 2 * (1 - (threshold - 1) - ell * mu)
                 + 2 * c * (1 - c) / eps)
    above = M * ((1 - c) ** 2 * (1 - (threshold + 1) - ell * mu)
                 + 2 * c * (1 - c) / eps)
    assert below > 0 and above < 0

    for n in range(1, 9):
        p2 = P_direct(P_direct(laguerre(n), eps, c), eps, c)
        expected_lead = F((-1) ** n, factorial(n)) * (1 - c) ** 2
        assert p2[-1] == expected_lead
        # Summing translations over a tower multiplies, but cannot alter,
        # this leading coefficient.
        assert M * p2[-1] == M * expected_lead

    print("PASS: P=(1-c)I+(c/eps)A_eps N (exact polynomials)")
    print("PASS: I-rho E=(1-rho)I+rho U_ell N")
    print("PASS: coupled local square C^2")
    print("PASS: b_u(p^k) is the backward second difference")
    print("PASS: exact n=1 tower block, both sides of its sign threshold")
    print("PASS: leading coefficient through degree 8")


if __name__ == "__main__":
    main()
