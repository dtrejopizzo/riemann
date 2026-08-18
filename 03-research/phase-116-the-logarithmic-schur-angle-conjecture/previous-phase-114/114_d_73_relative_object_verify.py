#!/usr/bin/env python3
"""Exact finite checks for the D.73 relative and support mechanisms."""

import sympy as sp

# The neutral diagonal in a hyperbolic plane is isotropic but not radical.
J = sp.diag(1, -1)
n = sp.Matrix([1, 1])
k = sp.Matrix([1, 0])
assert (n.T * J * n)[0] == 0
assert (n.T * J * k)[0] == 1

# Its J-orthogonal is the same line: x-y=0.
x, y = sp.symbols("x y", real=True)
v = sp.Matrix([x, y])
assert sp.solve([(n.T * J * v)[0]], [x], dict=True) == [{x: y}]

# Support compression is a negative square.
# A generic unitary rotation and P=diag(1,0) provide an exact check.
c, s = sp.symbols("c s", real=True)
U = sp.Matrix([[c, -s], [s, c]])
P = sp.diag(1, 0)
e1 = sp.Matrix([1, 0])
phase = sp.expand((e1.T * (U.T*P*U-P) * e1)[0])
assert phase == c**2 - 1
assert sp.simplify((phase + s**2).subs(c**2, 1-s**2)) == 0

# Codimension-two constraints cannot kill a rank-three cross block.
# Take b=I_3 and two coordinate functionals; their common kernel contains e3.
b = sp.eye(3)
e3 = sp.Matrix([0, 0, 1])
M = sp.Matrix([[1, 0, 0], [0, 1, 0]])
assert M*e3 == sp.zeros(2, 1)
assert b*e3 != sp.zeros(3, 1)

print("PASS neutral diagonal is isotropic but not radical")
print("PASS canonical Krein reduction of the diagonal is zero")
print("PASS supported phase compression gives a negative square")
print("PASS two scalar constraints cannot kill a rank-three cross block")
