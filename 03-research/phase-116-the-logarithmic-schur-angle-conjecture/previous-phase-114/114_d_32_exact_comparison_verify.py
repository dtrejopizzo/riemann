#!/usr/bin/env python3
"""Exact finite certificates for D.32.

Checks the Szego matrix coefficient, the complete finite orbit Gram
identity, and the positive zero-two-jet direction which rules out a
primewise extension of D.31.
"""

from fractions import Fraction


def inner_h_shift_h(r: Fraction, k: int, cutoff: int) -> Fraction:
    """Truncated normalized Szego coefficient through degree cutoff."""
    one_minus = 1 - r * r
    return one_minus * sum(
        (r ** n) * (r ** (n - k)) for n in range(k, cutoff + 1)
    )


def exact_tail(r: Fraction, k: int, cutoff: int) -> Fraction:
    """The omitted geometric tail in inner_h_shift_h."""
    return r**k * r ** (2 * (cutoff - k + 1))


def orbit_q(r: Fraction, n: int) -> Fraction:
    """q for V=z^2(1+...+z^(n-1)); exact Toeplitz formula."""
    return 2 * sum((n - d) * r**d for d in range(1, n))


for denominator in (2, 3, 5, 7, 11):
    # Work with rational r only for a formal geometric-series certificate.
    r = Fraction(1, denominator)
    for k in range(8):
        for cutoff in (k, k + 3, k + 10):
            approx = inner_h_shift_h(r, k, cutoff)
            assert approx + exact_tail(r, k, cutoff) == r**k

for denominator in (2, 3, 5, 7, 11):
    r = Fraction(1, denominator)
    for n in range(2, 12):
        q = orbit_q(r, n)
        assert q > 0
        # Direct Toeplitz sum minus the input norm.
        gram = sum(r ** abs(i - j) for i in range(n) for j in range(n))
        assert gram - n == q

print("D.32 exact comparison certificates: PASS")
print("Szego coefficient: <h_r,z^k h_r> = r^k (geometric tail certified)")
print("zero-two-jet orbit direction: ||h_r V_N||^2-||V_N||^2 > 0")
