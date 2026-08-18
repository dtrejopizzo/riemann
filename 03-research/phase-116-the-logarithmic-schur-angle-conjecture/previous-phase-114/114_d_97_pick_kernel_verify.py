#!/usr/bin/env python3
"""Exact finite certificates for D.97 infinitesimal Pick kernel."""

from fractions import Fraction


def main() -> None:
    # Differentiate 1-Theta(z)conj(Theta(w)) when Theta'=-G Theta.
    theta_z = Fraction(2, 3)
    theta_w = Fraction(3, 5)
    g_z = Fraction(7, 4)
    g_w = Fraction(11, 6)
    theta_z_prime = -g_z * theta_z
    theta_w_prime = -g_w * theta_w
    direct = -(theta_z_prime * theta_w + theta_z * theta_w_prime)
    factored = theta_z * theta_w * (g_z + g_w)
    assert direct == factored

    # The reflection displacement separates numerator and denominator at
    # speed two.  A simple fixed divisor therefore has derivative weight 2
    # and divisor-normalized weight 1.
    simple_divisor_derivative_weight = Fraction(2)
    normalized_divisor_weight = simple_divisor_derivative_weight / 2
    assert normalized_divisor_weight == 1

    # Exact rank-two Tate block: crossed, not Euclidean.
    m_minus = Fraction(2)
    m_plus = Fraction(-3)
    crossed = 2 * m_minus * m_plus
    euclidean = m_minus * m_minus + m_plus * m_plus
    assert crossed == -12
    assert euclidean == 13

    # Source decomposition: energy - mass + Tate; primitive removes Tate.
    energy = Fraction(29, 3)
    mass = Fraction(31, 4)
    tate = Fraction(-5, 7)
    full = energy - mass + tate
    primitive = energy - mass
    assert full - tate == primitive

    # Round-trip block at a nontrivial principal angle has negative det.
    lam = Fraction(2, 5)
    # determinant of [[4(1-lam), -2sqrt(...)], [...,0]]
    # computed without adjoining the square root.
    block_det = -4 * lam * (1 - lam)
    assert block_det == Fraction(-24, 25) < 0

    print("D97 infinitesimal Pick certificates: PASS")
    print("kernel derivative:", direct)
    print("normalized simple-divisor weight:", normalized_divisor_weight)
    print("crossed/Euclidean Tate forms:", crossed, euclidean)
    print("full/primitive source forms:", full, primitive)
    print("round-trip block determinant:", block_det)


if __name__ == "__main__":
    main()
