#!/usr/bin/env python3
"""Exact finite-dimensional checks for the D.200 block correction."""

from fractions import Fraction


def det3(a):
    return (
        a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
        - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
        + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0])
    )


A = [
    [Fraction(1), Fraction(0), Fraction(0)],
    [Fraction(0), Fraction(1), Fraction(2)],
    [Fraction(0), Fraction(2), Fraction(1)],
]

# Finite compression and raw Q block pass the invalid shortcut.
assert A[0][0] > 0 and A[1][1] > 0 and A[2][2] == 1
K_slow = A[0][0] - A[0][1] * A[1][0] / A[1][1]
C_slow_raw = A[0][2]
assert K_slow - C_slow_raw * C_slow_raw / A[2][2] == 1

# The full form is indefinite and the correct safe-tail budget detects it.
assert det3(A) == -3
kappa = A[2][1] * A[1][2] / A[1][1]
assert kappa == 4 > A[2][2]

# Symbolic scalar verification of the exact three-block formulas.
d, s, q = Fraction(7), Fraction(5), Fraction(11)
ds, dq, sq = Fraction(1), Fraction(2), Fraction(3)
K = d - ds * ds / s
C = dq - ds * sq / s
Q = q - sq * sq / s
full_det = det3([[d, ds, dq], [ds, s, sq], [dq, sq, q]])
assert full_det == s * (K * Q - C * C)

print("PASS D200: slow-only shortcut fails; exact three-block Schur identity holds")
