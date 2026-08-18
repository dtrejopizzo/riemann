#!/usr/bin/env python3
"""Exact rational check of the positive-complement capacity lemma."""

import sympy as sp

# v=e_1, one negative eigenvalue, and a positive complement.
lam = sp.Rational(-2, 5)
Aplus = sp.diag(0, 3, 5)
R = sp.Matrix([
    [2, 1, sp.Rational(1, 2)],
    [1, 2, 0],
    [sp.Rational(1, 2), 0, 1],
])
assert all(x > 0 for x in R.cholesky().diagonal())

v = sp.Matrix([1, 0, 0])
tail_capacity = 1 / (v.T * R.inv() * v)[0]
B = Aplus + R
full_capacity = 1 / (v.T * B.inv() * v)[0]

assert full_capacity > tail_capacity
assert full_capacity > -lam

total = sp.diag(lam, 3, 5) + R
assert all(x > 0 for x in total.cholesky().diagonal())

# The capacity is the scalar Schur complement onto the first coordinate.
schur = B[0, 0] - (B[0, 1:] * B[1:, 1:].inv() * B[1:, 0])[0]
assert sp.factor(schur - full_capacity) == 0

print("D.79 positive-complement capacity certificate: PASS")
print("tail-only capacity:", tail_capacity)
print("retained-complement capacity:", full_capacity)
