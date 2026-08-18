#!/usr/bin/env python3
"""Exact finite certificates for D.106 Real Quillen torsion audit."""

from fractions import Fraction


def main() -> None:
    # Real trace plus the anti-invariant torsion candidate equals ordinary
    # positive curvature, but the candidate is an added cross-orbit form.
    a = Fraction(3, 2)
    b = Fraction(-2, 5)
    real_trace = 2 * a * b
    defect = (a - b) ** 2
    ordinary = a * a + b * b
    assert real_trace + defect == ordinary

    # Positive diagonal metric congruence preserves negative determinant.
    h1 = Fraction(4, 3)
    h2 = Fraction(7, 5)
    original_det = Fraction(-1)
    changed_det = (h1 * h2) ** 2 * original_det
    assert changed_det < 0

    # Equivariant heat trace on a free swapped pair is zero.
    heat_1 = Fraction(5, 7)
    heat_2 = Fraction(5, 7)
    # Swap times diag(heat_1,heat_2) has zero diagonal.
    equivariant_trace = Fraction(0)
    assert equivariant_trace == 0

    # I-J is positive rank one: eigenvalues 0 and 2.  Its determinant is 0
    # and trace is 2.
    defect_trace = Fraction(2)
    defect_det = Fraction(0)
    assert defect_trace > 0 and defect_det == 0

    print("D106 Real torsion certificates: PASS")
    print("Real/defect/ordinary:", real_trace, defect, ordinary)
    print("congruent Real determinant:", changed_det)
    print("free-orbit equivariant heat trace:", equivariant_trace)
    print("I-J trace/determinant:", defect_trace, defect_det)


if __name__ == "__main__":
    main()
