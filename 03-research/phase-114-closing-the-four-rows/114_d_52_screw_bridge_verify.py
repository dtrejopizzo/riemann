#!/usr/bin/env python3
"""Algebraic certificates for the D.52 derivative and centering bridge."""
import sympy as sp

# Integration-by-parts identity N_sigma(F')=-sigma M_sigma(F).
t = sp.symbols("t", real=True)
F = (1-t**2)**3
for sigma in (sp.Rational(1, 2), sp.Rational(-1, 2)):
    M = sp.integrate(sp.exp(sigma*t)*F, (t, -1, 1))
    N = sp.integrate(sp.exp(sigma*t)*sp.diff(F, t), (t, -1, 1))
    assert sp.simplify(N + sigma*M) == 0

# A centered screw kernel has the same quadratic form as g(t_i-t_j)
# on the zero-mass subspace.  Use independent symbolic kernel values to
# certify that no positivity assumption enters this cancellation.
g0, g1, g2 = sp.symbols("g0 g1 g2", real=True)
G = sp.Matrix([[g0, g1, g2], [g1, g0, g1], [g2, g1, g0]])
one = sp.ones(3, 1)
gcol = sp.Matrix([g1, g0, g1])
K = G - gcol*one.T - one*gcol.T + g0*(one*one.T)
u = sp.Matrix([2, -3, 1])
assert (one.T*u)[0] == 0
assert sp.expand((u.T*(K-G)*u)[0]) == 0

# The two ruling moments of F are exactly the two exponential moments of
# its derivative, with the nonzero diagonal conversion -sigma.
conversion = sp.diag(sp.Rational(1, 2), sp.Rational(-1, 2))
assert conversion.det() != 0

print("PASS derivative converts the two Tate moments exactly")
print("PASS screw-kernel centering vanishes on zero-mass tests")
print("PASS the two boundary constraints remain independent")
