#!/usr/bin/env python3
"""Exact certificates for D.98 Markov/Tate boundary audit."""

from fractions import Fraction


def mat_vec(a, v):
    return [sum(a[i][j] * v[j] for j in range(len(v)))
            for i in range(len(a))]


def dot(v, w):
    return sum(v[i] * w[i] for i in range(len(v)))


def main() -> None:
    # Scalar Schur complement of the universal positive attachment.
    ell = Fraction(7, 3)
    m_trace = Fraction(5, 4)
    r = Fraction(11, 6)
    top = ell + m_trace * r * m_trace
    off = -m_trace * r
    schur = top - off * (1 / r) * off
    assert schur == ell

    # Minimal nonvacuous path model with two exponential moment vectors.
    lap = [
        [Fraction(1), Fraction(-1), Fraction(0)],
        [Fraction(-1), Fraction(2), Fraction(-1)],
        [Fraction(0), Fraction(-1), Fraction(1)],
    ]
    h_plus = [Fraction(1, 2), Fraction(1), Fraction(2)]
    h_minus = [Fraction(2), Fraction(1), Fraction(1, 2)]
    v = [Fraction(1), Fraction(-5, 2), Fraction(1)]
    assert dot(h_plus, v) == 0
    assert dot(h_minus, v) == 0
    energy = dot(v, mat_vec(lap, v))
    norm = dot(v, v)
    quotient = energy / norm
    assert energy == Fraction(49, 2)
    assert norm == Fraction(33, 4)
    assert quotient == Fraction(98, 33) < 3

    # A positive eigenvector on a finite conservative graph cannot carry a
    # nonzero eigenvalue: sum(Lh)=0 but sum(h)>0.
    h = [Fraction(1), Fraction(3), Fraction(2)]
    lh = mat_vec(lap, h)
    assert sum(lh) == 0
    assert sum(h) > 0

    print("D98 Markov boundary certificates: PASS")
    print("positive-attachment Schur complement:", schur)
    print("primitive path energy/norm/quotient:", energy, norm, quotient)
    print("sum(Lh), sum(h):", sum(lh), sum(h))


if __name__ == "__main__":
    main()
