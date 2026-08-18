#!/usr/bin/env python3
"""Exact finite certificates for D.100 Pontryagin-index audit."""

from fractions import Fraction


def determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    total = Fraction(0)
    for j, entry in enumerate(matrix[0]):
        minor = [row[:j] + row[j + 1:] for row in matrix[1:]]
        total += ((-1) ** j) * entry * determinant(minor)
    return total


def main() -> None:
    # A local Euler ratio is expansive and contractive on different arcs.
    r_plus = Fraction(1, 4)
    r_minus = Fraction(1, 2)
    at_one = (1 - r_plus) / (1 - r_minus)
    at_minus_one = (1 + r_plus) / (1 + r_minus)
    assert at_one == Fraction(3, 2) > 1
    assert at_minus_one == Fraction(5, 6) < 1

    # Negative multiples of Cauchy Grams have arbitrary finite negative
    # size.  Check Sylvester signs for the first four points y=1,...,4.
    size = 4
    cauchy = [[Fraction(1, (i + 1) + (j + 1))
               for j in range(size)] for i in range(size)]
    negative = [[-entry for entry in row] for row in cauchy]
    for k in range(1, size + 1):
        leading = [row[:k] for row in negative[:k]]
        det = determinant(leading)
        assert ((-1) ** k) * det > 0

    # Every nontrivial preparation angle contributes one negative direction.
    lambdas = [Fraction(1, 5), Fraction(2, 5), Fraction(4, 5)]
    block_determinants = [-4 * lam * (1 - lam) for lam in lambdas]
    assert all(det < 0 for det in block_determinants)

    print("D100 Pontryagin-index certificates: PASS")
    print("local Euler moduli at 1,-1:", at_one, at_minus_one)
    print("negative Cauchy leading minors certified through size:", size)
    print("preparation block determinants:", block_determinants)


if __name__ == "__main__":
    main()
