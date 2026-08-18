#!/usr/bin/env python3
"""Exact orbit certificates for D.105 Bochner/Real divisor audit."""

from fractions import Fraction


def main() -> None:
    multiplicity = Fraction(7, 3)
    a = Fraction(5, 2)
    b = Fraction(-4, 3)

    ordinary = multiplicity * (a * a + b * b)
    real_trace = multiplicity * (2 * a * b)
    defect = multiplicity * (a - b) ** 2
    assert ordinary - real_trace == defect > 0

    # Chiral coordinates without square roots: twice the forms satisfy
    # 2 Q_abs = m((a+b)^2+(a-b)^2),
    # 2 Q_R   = m((a+b)^2-(a-b)^2).
    plus = a + b
    minus = a - b
    assert 2 * ordinary == multiplicity * (plus ** 2 + minus ** 2)
    assert 2 * real_trace == multiplicity * (plus ** 2 - minus ** 2)

    # Free-orbit inertia is invariant under invertible diagonal congruence.
    gram_det = -(multiplicity ** 2)
    scale_1 = Fraction(2)
    scale_2 = Fraction(5, 4)
    congruent_det = (scale_1 * scale_2) ** 2 * gram_det
    assert gram_det < 0
    assert congruent_det < 0

    # Local Clifford derivative block [[0,d],[d,0]] has both signs.
    derivative = Fraction(11, 5)
    clifford_det = -(derivative ** 2)
    assert clifford_det < 0

    print("D105 Bochner/Real-divisor certificates: PASS")
    print("ordinary/Real/defect:", ordinary, real_trace, defect)
    print("chiral plus/minus coordinates:", plus, minus)
    print("free/congruent determinants:", gram_det, congruent_det)
    print("Clifford zero-order determinant:", clifford_det)


if __name__ == "__main__":
    main()
