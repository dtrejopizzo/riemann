#!/usr/bin/env python3
"""Exact finite certificates for D.124 annulus trace audit."""

from fractions import Fraction


def main() -> None:
    # Normalize D=1.  Constant endpoint profiles give c(delta)=delta.
    deltas = [Fraction(1, 5), Fraction(1, 2), Fraction(4, 5)]
    weights = [Fraction(2, 3), Fraction(3, 4), Fraction(5, 6)]
    total_mass = sum(weights)
    trace_square = sum(w*d*d for w, d in zip(weights, deltas))
    assert 0 < trace_square <= total_mass

    # Interior-mass lower bound with d=1/2.
    threshold = Fraction(1, 2)
    interior_mass = sum(w for w, d in zip(weights, deltas)
                        if d >= threshold)
    assert trace_square >= threshold**2 * interior_mass

    # Nested constant-profile frame has Gram min(delta_i,delta_j), positive
    # entries and coherent Rayleigh quotient.
    gram = [[min(x, y) for y in deltas] for x in deltas]
    assert all(entry >= 0 for row in gram for entry in row)
    ones = [Fraction(1)] * len(deltas)
    rayleigh_num = sum(ones[i]*gram[i][j]*ones[j]
                       for i in range(3) for j in range(3))
    rayleigh_den = sum(x*x for x in ones)
    assert rayleigh_num / rayleigh_den > 0

    print("D124 annulus Carleson-trace certificates: PASS")
    print("block mass / trace square:", total_mass, trace_square)
    print("interior lower mass:", threshold**2 * interior_mass)
    print("nested-frame Rayleigh quotient:", rayleigh_num/rayleigh_den)


if __name__ == "__main__":
    main()
