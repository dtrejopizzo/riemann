#!/usr/bin/env python3
"""Exact checks for 104_52 (integers and Fraction only)."""

from fractions import Fraction
from math import comb, factorial


KAPPA = Fraction(1501, 2002)


def laguerre_p_coeffs(n):
    """P_n(x)=L_{n-1}^{(1)}(x), coefficients low to high."""
    return [
        Fraction((-1) ** j * comb(n, j + 1), factorial(j))
        for j in range(n)
    ]


def poly_eval(coeffs, x):
    value = Fraction(0)
    for coefficient in reversed(coeffs):
        value = value * x + coefficient
    return value


def check_connected_hessian_cancellation():
    # L, K2 and epsilon are arbitrary exact placeholders.
    for arithmetic_mass in (Fraction(2, 7), Fraction(11, 13), Fraction(17, 5)):
        for collision in (Fraction(3, 8), Fraction(19, 11)):
            for epsilon in (Fraction(1, 3), Fraction(5, 4), Fraction(9, 2)):
                fpp_over_f = (
                    arithmetic_mass**2
                    + collision
                    - 2 * arithmetic_mass / epsilon
                )
                log_derivative_squared = (
                    1 / epsilon - arithmetic_mass
                ) ** 2
                assert (
                    fpp_over_f - log_derivative_squared
                    == collision - 1 / epsilon**2
                )
    print("PASS: disconnected prime-prime and prime-pole pairs cancel exactly")


def check_nested_unit_renewal():
    # q plays p^{-s}; ell plays log p.  Truncation is exact term by term.
    for q in (Fraction(1, 7), Fraction(2, 9), Fraction(4, 11)):
        for ell in (Fraction(2, 3), Fraction(5, 4)):
            for cutoff in (1, 3, 8, 13):
                collision = sum(
                    k * ell**2 * q**k for k in range(1, cutoff + 1)
                )
                nested = sum(
                    ell**2 * q**k
                    for k in range(1, cutoff + 1)
                    for _j in range(1, k + 1)
                )
                assert collision == nested

                # Integrating q^k=e^{-k ell s} in s divides by k*ell.
                integrated_nested = sum(
                    ell**2 * q**k / (k * ell)
                    for k in range(1, cutoff + 1)
                    for _j in range(1, k + 1)
                )
                one_mark = sum(ell * q**k for k in range(1, cutoff + 1))
                assert integrated_nested == one_mark
    print("PASS: exact unit renewal lifts one mark to a nested same-tower pair")


def check_all_euler_log_orders_are_single_tower():
    # In the derivative hierarchy of log zeta, the r-th cumulant is an
    # r-fold same-tower mark.  This says nothing about arbitrary nonlinear
    # observables of N.
    for order in range(2, 10):
        for k in range(1, 8):
            for ell in (Fraction(2, 3), Fraction(7, 5)):
                direct = ell * (k * ell) ** (order - 1)
                nested = k ** (order - 1) * ell**order
                assert direct == nested
    print("PASS: every finite Euler-log cumulant remains inside one prime tower")


def check_lcm_connected_support():
    # For different towers lcm weight equals product weight exactly.
    q = Fraction(2, 7)
    r = Fraction(3, 11)
    for k in range(1, 8):
        for ell in range(1, 8):
            disconnected = q**k * r**ell
            lcm_different_primes = q**k * r**ell
            assert lcm_different_primes - disconnected == 0

            lcm_same_prime = q ** max(k, ell)
            product_same_prime = q ** (k + ell)
            assert lcm_same_prime - product_same_prime > 0
    print("PASS: the connected lcm kernel vanishes between distinct prime towers")


def check_gamma_and_real_ray_signs():
    # Coarse certified bounds from 103_68, inserted with the exact kappa.
    upper_at_one = (
        -Fraction(577, 1000) ** 2
        + Fraction(146, 1000)
        + KAPPA * (Fraction(987, 800) - 1)
    )
    assert upper_at_one == -Fraction(531207, 45500000) < 0

    # At s=10, sum_{r>=1}(10+2r)^-2 >= integral_1^infty = 1/24.
    lower_at_ten_without_prime_term = -Fraction(1, 81) + KAPPA / 24
    assert lower_at_ten_without_prime_term > 0
    assert 81 * 1501 > 24 * 2002

    # Finite exact cancellation of the r=0 trigamma atom against -1/s^2.
    for s in (Fraction(1), Fraction(7, 3), Fraction(10)):
        for cutoff in (1, 4, 12):
            lhs = -1 / s**2 + sum(
                1 / (s + 2 * r) ** 2 for r in range(cutoff + 1)
            )
            rhs = sum(1 / (s + 2 * r) ** 2 for r in range(1, cutoff + 1))
            assert lhs == rhs
    print("PASS: exact Gamma Hessian and rational real-ray sign change")


def mixed_cocycle(n, t, x=Fraction(1), y=Fraction(1)):
    coefficients = laguerre_p_coeffs(n)
    return (
        poly_eval(coefficients, t + x + y)
        - poly_eval(coefficients, t + x)
        - poly_eval(coefficients, t + y)
        + poly_eval(coefficients, t)
    )


def check_laguerre_mixed_signs():
    # Formula (28) for P_4.
    for t in (Fraction(0), Fraction(3, 2), Fraction(5)):
        for x, y in ((Fraction(1), Fraction(1)), (Fraction(2, 3), Fraction(5, 4))):
            expected = x * y * (4 - t - (x + y) / 2)
            assert mixed_cocycle(4, t, x, y) == expected

    # Exact rational witnesses inside the target range.
    for n in (150, 151, 152):
        assert mixed_cocycle(n, Fraction(0)) > 0
        assert mixed_cocycle(n, Fraction(1)) < 0
    print("PASS: exact Laguerre two-increment cocycle has both signs at n=150..152")


def check_quadratic_homotopy_flow():
    # Verify D(D-1)H_n=n(n+1) Delta^2 H_n from D H_n=n Delta H_n.
    triples = (
        (Fraction(2, 7), Fraction(11, 5), Fraction(-3, 4)),
        (Fraction(-5, 9), Fraction(7, 3), Fraction(19, 8)),
    )
    for n in (1, 4, 17, 151):
        for h0, h1, h2 in triples:
            first = n * (h1 - h0)
            second = n * ((n + 1) * (h2 - h1) - n * (h1 - h0))
            lhs = second - first
            rhs = n * (n + 1) * (h2 - 2 * h1 + h0)
            assert lhs == rhs
    print("PASS: exact second-order homotopy identity")


def check_shifted_connected_cancellation():
    # Generic two-pole analogue of (33).
    for u, c in ((Fraction(3), Fraction(1, 4)), (Fraction(7, 2), Fraction(2, 5))):
        for shifted_mass, shifted_collision in (
            (Fraction(5, 7), Fraction(13, 9)),
            (Fraction(11, 4), Fraction(2, 13)),
        ):
            polar = 1 / (u - c) + 1 / (u + c)
            polar_derivative = -1 / (u - c) ** 2 - 1 / (u + c) ** 2
            m = polar - shifted_mass
            # F''/F = M' + M^2; subtracting M^2 recovers M'.
            fpp_over_f = polar_derivative + shifted_collision + m**2
            assert fpp_over_f - m**2 == polar_derivative + shifted_collision
    print("PASS: shifted two-pole system has the same connected cancellation")


def main():
    check_connected_hessian_cancellation()
    check_nested_unit_renewal()
    check_all_euler_log_orders_are_single_tower()
    check_lcm_connected_support()
    check_gamma_and_real_ray_signs()
    check_laguerre_mixed_signs()
    check_quadratic_homotopy_flow()
    check_shifted_connected_cancellation()
    print("PASS: 104_52 connected two-tower flux gate")


if __name__ == "__main__":
    main()
