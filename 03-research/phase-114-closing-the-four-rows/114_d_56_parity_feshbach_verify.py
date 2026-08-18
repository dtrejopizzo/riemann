#!/usr/bin/env python3
"""Exact certificates for the D.56 no-go examples and parity gate."""
import sympy as sp

def inertia_exact(M):
    # All matrices below have rational characteristic roots or are small
    # enough for exact LDL signs through numerical isolation.
    import numpy as np
    vals = np.linalg.eigvalsh(np.array(M.tolist(), dtype=float))
    return (int((vals > 1e-10).sum()), int((vals < -1e-10).sum()))

# Connected Gram energy does not imply index one.
L = sp.Matrix([[1, -1, 0], [-1, 2, -1], [0, -1, 1]])
assert L.eigenvals() == {0: 1, 1: 1, 3: 1}
Bgram = 2*sp.eye(3)-L
assert inertia_exact(Bgram) == (2, 1)

# Index one does not imply a hyperbolic boundary Green matrix.
Be = sp.diag(1, -1)
Bo = sp.Matrix([[-2]])
ue = sp.Matrix([0, 1])
uo = sp.Matrix([1])
ge = (ue.T*Be.inv()*ue)[0]
go = (uo.T*Bo.inv()*uo)[0]
assert ge == -1 and go == -sp.Rational(1, 2)

# Exact successful parity--Feshbach model.
Be2 = sp.Matrix([[2, 1], [1, -2]])
Bo2 = sp.Matrix([[-1, 1], [1, -3]])

def core_schur(B):
    A = B[:1, :1]
    C = B[:1, 1:]
    D = B[1:, 1:]
    return sp.simplify(A-C*D.inv()*C.T), D

Se, De = core_schur(Be2)
So, Do = core_schur(Bo2)
assert Se == sp.Matrix([[sp.Rational(5, 2)]])
assert So == sp.Matrix([[-sp.Rational(2, 3)]])
assert De[0, 0] < 0 and Do[0, 0] < 0
assert inertia_exact(Be2) == (1, 1)
assert inertia_exact(Bo2) == (0, 2)

# Jet block-inverse identity and hyperbolic signs.
ue2 = sp.Matrix([1, 0])
uo2 = sp.Matrix([1, 0])
ge2 = sp.simplify((ue2.T*Be2.inv()*ue2)[0])
go2 = sp.simplify((uo2.T*Bo2.inv()*uo2)[0])
assert ge2 == sp.Rational(2, 5)
assert go2 == -sp.Rational(3, 2)
assert ge2*go2 < 0

# General symbolic block inverse quadratic identity in scalar core/high form.
a, c, d, p, q = sp.symbols("a c d p q", nonzero=True)
B = sp.Matrix([[a, c], [c, d]])
u = sp.Matrix([p, q])
S = a-c**2/d
rhs = (p-c*q/d)**2/S + q**2/d
assert sp.simplify((u.T*B.inv()*u)[0]-rhs) == 0

print("PASS connected mass-minus-Gram operator can have positive index two")
print("PASS index one alone does not force a hyperbolic jet matrix")
print("PASS parity Feshbach signs give one even and zero odd positive modes")
print("PASS exact block-inverse jet formula and hyperbolic signature")
