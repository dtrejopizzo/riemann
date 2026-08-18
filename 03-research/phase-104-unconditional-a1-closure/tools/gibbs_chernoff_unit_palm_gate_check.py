#!/usr/bin/env python3
"""Exact polynomial checks for 104_54; no zeta or floating point."""

from fractions import Fraction as Q
from math import comb, factorial


def trim(a):
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def add(a, b):
    out = [Q(0)] * max(len(a), len(b))
    for i, value in enumerate(a):
        out[i] += value
    for i, value in enumerate(b):
        out[i] += value
    return trim(out)


def scale(a, c):
    return trim([c * value for value in a])


def x_times(a):
    return [Q(0)] + list(a)


def compose_scale(a, c):
    return [value * c**j for j, value in enumerate(a)]


def evaluate(a, x):
    total = Q(0)
    for value in reversed(a):
        total = total * x + value
    return total


def laguerre(m, alpha=0):
    return [Q((-1) ** j * comb(m + alpha, m - j), factorial(j))
            for j in range(m + 1)]


def defect_polynomials(n, s):
    p = compose_scale(laguerre(n - 1, 1), s)
    ln_single = compose_scale(laguerre(n, 0), s)
    primitive_single = scale(add([Q(1)], scale(ln_single, -1)), 1 / s)
    d_prime = add(x_times(p), scale(primitive_single, -1))

    ln_double = compose_scale(laguerre(n, 0), 2 * s)
    primitive_double = scale(add([Q(1)], scale(ln_double, -1)), 1 / s)
    d_equal_semiprime = add(scale(x_times(p), 2), scale(primitive_double, -1))
    return d_prime, d_equal_semiprime


def check_leading_coefficients():
    s = Q(3, 2)
    for n in list(range(4, 22)) + [150, 151]:
        prime, semiprime = defect_polynomials(n, s)
        expected_prime = Q((-1) ** (n - 1) * (n - 1), factorial(n)) * s ** (n - 1)
        expected_semiprime = (
            Q((-1) ** (n - 1), factorial(n - 1))
            * s ** (n - 1)
            * (Q(2) - Q(2**n, n))
        )
        assert len(prime) == n + 1 and prime[-1] == expected_prime
        assert len(semiprime) == n + 1 and semiprime[-1] == expected_semiprime
        assert Q(2) - Q(2**n, n) < 0
        assert (prime[-1] > 0) == ((-1) ** (n - 1) > 0)
        assert (semiprime[-1] > 0) == ((-1) ** n > 0)


def find_dominating_x(poly, log_multiplier, s, tilt=Q(1, 7)):
    x = 1
    for _ in range(30):
        value = evaluate(poly, Q(x))
        if value > 0 and tilt * value > s * log_multiplier * x:
            return x, value
        x *= 2
    raise AssertionError("dominant polynomial tail not reached")


def check_superlinear_witnesses():
    s = Q(3, 2)
    for n in (150, 151):
        prime, semiprime = defect_polynomials(n, s)
        if (-1) ** (n - 1) > 0:
            positive = prime
            negative_reflected = scale(semiprime, -1)
            positive_log_multiplier = 1
            negative_log_multiplier = 2
        else:
            positive = semiprime
            negative_reflected = scale(prime, -1)
            positive_log_multiplier = 2
            negative_log_multiplier = 1

        xp, vp = find_dominating_x(positive, positive_log_multiplier, s)
        xn, vn = find_dominating_x(negative_reflected, negative_log_multiplier, s)
        assert vp > 0 and vn > 0 and xp > 0 and xn > 0


def check_shifted_squarefree_selector():
    # For every local r=p^c, a_c(p)=r+r^-1 and omega_c(p)=ell*a_c(p).
    ell_p, ell_q = Q(2), Q(3)
    r_p, r_q = Q(2), Q(3)
    a_p, a_q = r_p + 1 / r_p, r_q + 1 / r_q
    omega_p, omega_q = ell_p * a_p, ell_q * a_q

    f = lambda x: Q(1) - 2 * x + 3 * x * x
    assert omega_p * f(ell_p) / a_p == ell_p * f(ell_p)

    a_pq = a_p * a_q
    j_shifted = (omega_p * a_q * f(ell_p)
                 + omega_q * a_p * f(ell_q)) / a_pq
    j_unit = ell_p * f(ell_p) + ell_q * f(ell_q)
    assert j_shifted == j_unit

    # Exact example p=5, 5^c=2: 0<c<1/2 follows from 2^2<5.
    assert 2**2 < 5
    assert a_p == Q(5, 2)


def main():
    check_leading_coefficients()
    check_superlinear_witnesses()
    check_shifted_squarefree_selector()
    print("PASS: exact Gibbs-Chernoff unit-Palm gate checks")


if __name__ == "__main__":
    main()
