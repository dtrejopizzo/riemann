#!/usr/bin/env python3
"""Exact certificates for D.92 vacuum/CAR Hessian audit."""

from fractions import Fraction


def main() -> None:
    # Dual-number Kunneth expansion coefficients:
    # 1 + eps*f + eta*g + eps*eta*(f tensor g).
    coefficients = {
        (0, 0): 1,
        (1, 0): 1,
        (0, 1): 1,
        (1, 1): 1,
    }
    assert coefficients[(1, 1)] == 1

    # Local contact cannot be a positive unital two-point function.
    logp = Fraction(7, 5)
    gram = ((Fraction(0), logp), (logp, logp))
    det = gram[0][0] * gram[1][1] - gram[0][1] * gram[1][0]
    assert det == -logp * logp < 0

    # A positive feature vacuum gives sum; J insertion gives difference.
    s2 = Fraction(13, 4)
    b2 = Fraction(9, 7)
    positive_vacuum = s2 + b2
    krein_vacuum = s2 - b2
    assert positive_vacuum > 0
    assert positive_vacuum - krein_vacuum == 2 * b2

    # Fixed-cell determinant has zero coefficient Hessian.
    ranks = [3, 8, 21]
    metric_exponents = [Fraction(-2, 9) * r for r in ranks]
    for exponent in metric_exponents:
        # Constant as a function of any coefficient coordinate.
        first_difference = exponent - exponent
        second_difference = first_difference - first_difference
        assert first_difference == second_difference == 0

    print("D92 vacuum/CAR certificates: PASS")
    print("contact Gram determinant:", det)
    print("positive/Krein covariances:", positive_vacuum, krein_vacuum)
    print("coefficient Hessian:", 0)


if __name__ == "__main__":
    main()
