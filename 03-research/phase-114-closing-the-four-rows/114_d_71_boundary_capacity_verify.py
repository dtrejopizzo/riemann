#!/usr/bin/env python3
"""Exact checks for the D.71 stationary-action no-go."""

import sympy as sp

B = sp.diag(4, 3, 2, -1)
u = sp.Matrix([1, 1, 1, 1])
m0 = (u.T * B.inv() * u)[0]
assert m0 == sp.Rational(1, 12)

fstat = B.inv() * u / m0
assert (u.T * fstat)[0] == 1
assert (fstat.T * B * fstat)[0] == 12

v = sp.Matrix([1, -1, 0, 0])
assert (u.T * v)[0] == 0
assert (v.T * B * v)[0] == 7

t = sp.symbols("t", real=True)
action = sp.expand(((fstat + t*v).T * B * (fstat + t*v))[0])
assert sp.Poly(action, t).LC() == 7

# A scalar completion-of-square instance: a=2, b=1, D=-3, z=0.
x = sp.symbols("x", real=True)
q = 2 + 2*x - 3*x**2
capacity = sp.Rational(7, 3)
assert sp.expand(capacity - 3*(x-sp.Rational(1, 3))**2 - q) == 0

print(f"stationary resolvent value m(0)={m0}, action={1/m0}")
print(f"zero-boundary positive direction={int((v.T*B*v)[0])}")
print(f"unbounded action polynomial={action}")
print("PASS finite Poisson stationary action can coexist with infinite capacity")
print("PASS boundary capacity equals Schur complement under negative bulk")
