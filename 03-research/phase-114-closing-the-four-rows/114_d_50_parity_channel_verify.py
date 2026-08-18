#!/usr/bin/env python3
"""Exact and numerical certificates for the D.50 parity audit."""
import sympy as sp

# Exact three-dimensional displacement-rank counterexample.
A = sp.Matrix([[0, 1, 1], [1, 10, 1], [1, 1, 0]])
D = sp.diag(-1, 0, 1)
J = sp.Matrix([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
eta = sp.Matrix([1, 1, 1])
beta = sp.Matrix([-1, 0, 1])
assert A*J == J*A
assert D*J == -J*D
assert D*A-A*D == beta*eta.T-eta*beta.T

# Exact parity spectrum of A.
odd = sp.Matrix([1, 0, -1])
assert A*odd == -odd
x = sp.symbols("x", real=True)
even_block = sp.Matrix([[1, sp.sqrt(2)], [sp.sqrt(2), 10]])
assert even_block.trace() == 11
assert even_block.det() == 8
even_low = (sp.Integer(11)-sp.sqrt(89))/2
assert sp.simplify(even_low+1) > 0

# Exact Tate rank-two decomposition on t=(-1,0,1).
t = [sp.Integer(-1), sp.Integer(0), sp.Integer(1)]
phi_minus = sp.Matrix([sp.exp(-q/2) for q in t])
phi_plus = sp.Matrix([sp.exp(q/2) for q in t])
phi_even = phi_plus+phi_minus
phi_odd = phi_plus-phi_minus
R_cross = phi_minus*phi_plus.T+phi_plus*phi_minus.T
R_parity = (phi_even*phi_even.T-phi_odd*phi_odd.T)/2
assert sp.simplify(R_cross-R_parity) == sp.zeros(3)

# H0=A-R2 has strictly negative off-diagonal entries, hence its heat
# semigroup is positivity improving by irreducible Metzler theory.
H0 = A-R_cross
for i in range(3):
    for j in range(3):
        if i != j:
            assert float(sp.N(H0[i, j], 30)) < 0

# Numerical confirmation of the parity reversal and the positive/even base
# ground state; no numerical assertion is used in the exact proof above.
import numpy as np
H0_np = np.array(H0.evalf(30).tolist(), dtype=float)
A_np = np.array(A.tolist(), dtype=float)
hvals, hvecs = np.linalg.eigh(H0_np)
avals, avecs = np.linalg.eigh(A_np)
assert hvals[0] < hvals[1]
assert np.all(np.abs(hvecs[:, 0]) > 1e-8)
J_np = np.array(J.tolist(), dtype=float)
assert np.linalg.norm(J_np.dot(hvecs[:, 0])-hvecs[:, 0]) < 1e-8
assert abs(avals[0]+1) < 1e-10
ground = avecs[:, 0]
assert np.linalg.norm(J_np.dot(ground)+ground) < 1e-8

print("PASS CCM displacement-rank identity and reflection")
print("PASS exact cosh/sinh rank-two polar decomposition")
print("PASS positivity-improving base has an even ground state")
print("PASS full operator has a simple odd ground state: structural no-go")
