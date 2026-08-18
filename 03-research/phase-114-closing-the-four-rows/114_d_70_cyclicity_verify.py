#!/usr/bin/env python3
"""Exact checks for the D.70 cyclic Sturm counterexample."""

import sympy as sp

B = sp.diag(4, 3, 2, -1)
u = sp.Matrix([1, 1, 1, 1])
K = sp.Matrix.hstack(u, B*u, B**2*u, B**3*u)
assert K.det() != 0

v1 = sp.Matrix([1, -1, 0, 0])
v2 = sp.Matrix([1, 0, -1, 0])
assert (u.T*v1)[0] == 0 and (u.T*v2)[0] == 0
G = sp.Matrix([
    [(v1.T*B*v1)[0], (v1.T*B*v2)[0]],
    [(v2.T*B*v1)[0], (v2.T*B*v2)[0]],
])
assert G == sp.Matrix([[7, 4], [4, 6]])
assert G.det() > 0 and G.trace() > 0

# A mass-minus-positive-feature representation is always available here.
m = 4
L = m*sp.eye(4) - B
assert all(ev >= 0 for ev in L.eigenvals())

print(f"Krylov determinant={K.det()} (nonzero: u is cyclic)")
print(f"positive primitive 2x2 Gram={G.tolist()}, determinant={G.det()}")
print("PASS cyclicity and strict interlacing do not force primitive negativity")
print("PASS counterexample also has mass-minus-positive-energy form")
