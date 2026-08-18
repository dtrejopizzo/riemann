#!/usr/bin/env python3
"""Finite checks for 104_90.

The proof is in the markdown document.  This checker verifies the exact
rational functional equation, positivity/factorization of the added tower,
the mapped off-line locations, and the fixed-height numerical scales.
"""

from fractions import Fraction
from math import log


def zminus(t):
    return ((1 - 3 * t) * (1 - 2 * t)) / ((1 - t) * (1 - 6 * t))


def main():
    # Exact rational functional equation of the reticular seed.
    for t in (Fraction(1, 12), Fraction(2, 9), Fraction(3, 20)):
        assert zminus(t) == zminus(1 / (6 * t))

    # The added Mangoldt height is positive on every checked 7-tower level;
    # positivity for all levels follows from the exact factorization.
    for ell in range(1, 101):
        psi = 6**ell + 1 - 3**ell - 2**ell
        assert psi == (3**ell - 1) * (2**ell - 1)
        assert psi > 0

    sigma = log(42.0) / (2.0 * log(7.0))
    assert 0.0 < sigma < 1.0

    displacement = log(1.5) / (2.0 * log(7.0))
    left = 0.5 - displacement
    right = 0.5 + displacement
    assert left < 0.5 < right
    assert abs((left + right) - 1.0) < 1e-15

    height = 3.0e12
    radial = 1.0 / (2.0 * height * height)
    crossover = 4.0 * height**4
    assert abs(radial - 5.555555555555556e-26) < 1e-40
    assert abs(crossover - 3.24e50) / crossover < 1e-15

    print("104_90 checker: PASS")
    print(f"sigma={sigma:.12f} < 1")
    print(f"off-line real parts: {left:.12f}, {right:.12f}")
    print(f"a_H universal ceiling at H=3e12: {radial:.12e}")
    print(f"diagnostic crossover 4 H^4: {crossover:.12e}")


if __name__ == "__main__":
    main()
