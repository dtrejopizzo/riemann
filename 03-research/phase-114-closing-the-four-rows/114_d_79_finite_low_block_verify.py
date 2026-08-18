#!/usr/bin/env python3
"""Exact matrix audit of the finite low-block capacity identities."""
import sympy as sp

h = sp.Rational(2, 1)
R = sp.Matrix([[3, 1, 1], [1, 4, 0], [1, 0, 5]])
# L is spanned by the first two coordinate vectors; Q_L adds h only to K.
Q = sp.diag(0, 0, 1)
T = R + h * Q

# Direct Schur complement onto L.
TLL = T[:2, :2]
TLK = T[:2, 2:]
TKL = T[2:, :2]
TKK = T[2:, 2:]
short_direct = sp.simplify(TLL - TLK * TKK.inv() * TKL)

# Resolvent/capacity formula.
compressed_inverse = T.inv()[:2, :2]
capacity = sp.simplify(compressed_inverse.inv() - h * sp.eye(2))
assert sp.simplify(short_direct - (capacity + h * sp.eye(2))) == sp.zeros(2)

delta = sp.eye(2) / h - compressed_inverse
capacity_deficit = sp.simplify(h*h*delta*(sp.eye(2)-h*delta).inv())
assert sp.simplify(capacity - capacity_deficit) == sp.zeros(2)

# Young/Schur direction on a separate rational block.
g, eta = sp.Rational(5), sp.Rational(2)
A = sp.Matrix([[2, 0], [0, 3]])
B = sp.Matrix([[1, 2], [0, 1]])
D = sp.Rational(5) * sp.eye(2)
Aeff = A - B.T * B / eta
assert g - eta > 0
# The difference is the positive square
# eta^{-1} ||Bx+eta y||^2 when D=gI.
x = sp.Matrix(sp.symbols('x0:2'))
y = sp.Matrix(sp.symbols('y0:2'))
full = (x.T*A*x)[0] + 2*(y.T*B*x)[0] + (y.T*D*y)[0]
lower = (x.T*Aeff*x)[0] + (g-eta)*(y.T*y)[0]
square = ((B*x+eta*y).T*(B*x+eta*y))[0] / eta
assert sp.expand(full-lower-square) == 0

print("D.79 finite low-block capacity certificates: PASS")
print("capacity matrix:", capacity)
print("deficit matrix:", delta)
