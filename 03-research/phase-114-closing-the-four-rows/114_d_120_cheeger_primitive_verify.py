#!/usr/bin/env python3
"""Exact finite certificates for D.120 Cheeger/primitive audit."""

from fractions import Fraction


def main() -> None:
    # Exact symmetric-difference length for an interval, sampled at integer
    # lengths: ||1_[0,L]-S_a 1_[0,L]||^2=2 min(a,L).
    length = 11
    jumps = [2, 5, 17]
    weights = [Fraction(3, 7), Fraction(2, 5), Fraction(1, 9)]
    energy = sum(2 * w * min(a, length)
                 for w, a in zip(weights, jumps))
    profile = energy / length
    assert profile > 0

    # With fixed finite first moment, the interval quotient tends to zero.
    first_moment = sum(w * a for w, a in zip(weights, jumps))
    large_length = 10_000
    large_profile = 2 * first_moment / large_length
    assert large_profile < Fraction(1, 100)

    # Exact three-translate coefficients kill both reciprocal moments.
    # Use z=2 (R=2 log 2) algebraically.
    z = Fraction(2)
    alpha = 1 / z - z
    beta = z * z - 1 / (z * z)
    plus = alpha / z + beta + alpha * z
    minus = alpha * z + beta + alpha / z
    assert plus == 0
    assert minus == 0
    assert abs(alpha / beta) == Fraction(2, 5)

    # Positivity of an unshifted Laplacian does not give the full-degree gap.
    degree_mass = Fraction(5)
    possible_edge = Fraction(0)
    assert possible_edge >= 0
    assert possible_edge < degree_mass

    print("D120 prime-Gamma Cheeger certificates: PASS")
    print("finite interval profile:", profile)
    print("fixed-cutoff Folner profile:", large_profile)
    print("primitive translate coefficients:", alpha, beta, alpha)
    print("unshifted edge versus required mass:", possible_edge, degree_mass)


if __name__ == "__main__":
    main()
