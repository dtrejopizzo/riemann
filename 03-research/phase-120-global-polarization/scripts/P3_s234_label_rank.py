#!/usr/bin/env python3
"""Exact rank audit for the label-only S={2,3,4} divergence.

Columns are q_(2,1), q_(3,1), q_(2,2); rows are the rank-one contact
lines of the places 2 and 3.  This checks only the label-level map.  It does
not pretend to construct the missing physical Euler--Gamma synthesis.
"""

import sympy as sp


log2, log3 = sp.log(2), sp.log(3)
a21 = sp.sqrt(log2) * 2 ** sp.Rational(-1, 4)
a31 = sp.sqrt(log3) * 3 ** sp.Rational(-1, 4)
a22 = sp.sqrt(log2) * 2 ** sp.Rational(-1, 2)

D = sp.Matrix(
    [
        [a21, 0, a22],
        [0, a31, 0],
    ]
)
cycle = sp.Matrix([a22, 0, -a21])

assert D.rank() == 2
assert D * cycle == sp.zeros(2, 1)
assert len(D.nullspace()) == 1

print("columns: q_(2,1), q_(3,1), q_(2,2)")
print("rank:", D.rank())
print("nullity:", len(D.nullspace()))
print("kernel generator:", cycle.T)
print("D * generator:", (D * cycle).T)
