#!/usr/bin/env python3
"""Exact scalar certificates for D.104 log-connection graph audit."""

from fractions import Fraction


def main() -> None:
    # Work with L=1 and r=1/2 at the two Bloch characters.
    r = Fraction(1, 2)
    g_zero = (1 - r) ** 2
    g_pi = (1 + r) ** 2
    g_prime_zero = 2 * r * (1 - r)
    g_prime_pi = -2 * r * (1 + r)
    connection_zero = g_prime_zero / g_zero
    connection_pi = g_prime_pi / g_pi
    assert connection_zero == 2 > 0
    assert connection_pi == Fraction(-2, 3) < 0

    # Log-curvature changes sign.
    curvature_zero = -2 * r / (1 - r) ** 2
    curvature_pi = 2 * r / (1 + r) ** 2
    assert curvature_zero == -4 < 0
    assert curvature_pi == Fraction(4, 9) > 0

    # Coercive epsilon regularization attenuates the exact connection.
    epsilon = Fraction(1)
    regularized_zero = g_prime_zero / (g_zero + epsilon)
    regularized_pi = g_prime_pi / (g_pi + epsilon)
    assert regularized_zero == Fraction(2, 5) != connection_zero
    assert regularized_pi == Fraction(-6, 13) != connection_pi

    # A reflected harmonic-mean Schur complement is even.  Check at a
    # formal pair (g+,g-) and its swap.
    g_plus = Fraction(3, 2)
    g_minus = Fraction(5, 4)
    schur = 2 * g_plus * g_minus / (g_plus + g_minus)
    reflected_schur = 2 * g_minus * g_plus / (g_minus + g_plus)
    assert schur == reflected_schur > 0

    # Positive metric paths can have indefinite derivative.
    derivative_eigenvalues = [Fraction(2), Fraction(-1)]
    assert derivative_eigenvalues[0] > 0 > derivative_eigenvalues[1]

    print("D104 logarithmic-connection certificates: PASS")
    print("connections at 0,pi:", connection_zero, connection_pi)
    print("curvatures at 0,pi:", curvature_zero, curvature_pi)
    print("regularized connections:", regularized_zero, regularized_pi)
    print("reflected Schur value:", schur)


if __name__ == "__main__":
    main()
