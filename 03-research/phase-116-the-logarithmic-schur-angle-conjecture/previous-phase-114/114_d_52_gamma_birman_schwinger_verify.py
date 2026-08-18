#!/usr/bin/env python3
"""Finite exact certificates for the identities used in D.52."""
import sympy as sp
import numpy as np

# An invertible Gamma reference with two positive directions.
Gamma = sp.diag(4, 1, -1, -9)
V = sp.Matrix([
    [-5, sp.Rational(-3, 2), sp.Rational(1, 2), 0],
    [sp.Rational(-3, 2), 0, sp.Rational(1, 2), -1],
    [sp.Rational(1, 2), sp.Rational(1, 2), -1, sp.Rational(1, 2)],
    [0, -1, sp.Rational(1, 2), 1],
])
B = Gamma+V

# Self-adjoint Birman--Schwinger congruence.
abs_half = sp.diag(2, 1, 1, 3)
abs_inv_half = sp.diag(sp.Rational(1, 2), 1, 1, sp.Rational(1, 3))
Jg = sp.diag(1, 1, -1, -1)
K = abs_inv_half*V*abs_inv_half
assert K == K.T
assert B == abs_half*(Jg+K)*abs_half

# Exact resolvent and boundary Green identities.
M = sp.Matrix([[1, 0, 1, 0], [0, 1, 0, 1]])
R_formula = (Gamma.inv()
             -Gamma.inv()*V*(sp.eye(4)+Gamma.inv()*V).inv()*Gamma.inv())
assert sp.simplify(B.inv()-R_formula) == sp.zeros(4)
G = sp.simplify(M*B.inv()*M.T)
assert G == sp.Matrix([
    [sp.Rational(-1052, 755), sp.Rational(-378, 755)],
    [sp.Rational(-378, 755), sp.Rational(68, 755)],
])
assert G.det() == sp.Rational(-284, 755)

# The primitive kernel of M is negative in this index-one/hyperbolic model.
N = sp.Matrix([[1, 0], [0, 1], [-1, 0], [0, -1]])
primitive = N.T*B*N
assert primitive.trace() < 0 and primitive.det() > 0

# Numerical inertia check (all algebraic identities above are exact).
def inertia(matrix):
    values = np.linalg.eigvalsh(np.array(matrix.evalf(40).tolist(), dtype=float))
    return (int(np.sum(values > 1e-10)), int(np.sum(values < -1e-10)),
            int(np.sum(np.abs(values) <= 1e-10)))

assert inertia(Gamma) == (2, 2, 0)
assert inertia(B) == (1, 3, 0)
assert inertia(G) == (1, 1, 0)
assert inertia(primitive) == (0, 2, 0)

# Sign table D.47/D.49: H0=-B and QW=R2-B.
C = sp.Matrix([[0, 1], [1, 0]])
R2 = M.T*C*M
H0 = -B
QW = R2-B
assert H0 == -B
assert QW == R2+H0
assert N.T*QW*N == -primitive  # M*N=0: primitive sign reversal.

print("PASS Gamma Birman--Schwinger congruence and inertia reduction")
print("PASS exact resolvent formula and hyperbolic boundary Green matrix")
print("PASS D.47/D.49 sign table on the primitive kernel")
