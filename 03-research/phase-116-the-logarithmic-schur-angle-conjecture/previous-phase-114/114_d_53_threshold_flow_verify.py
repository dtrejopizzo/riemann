#!/usr/bin/env python3
"""Exact certificates for D.53 threshold flow and hinge signs."""
import sympy as sp

# The exact nonmonotone four-dimensional activation path.
s = sp.symbols("s", real=True)
A = sp.Matrix([[0, 1], [1, 0]])
Gamma = sp.diag(-sp.Rational(1, 3), -sp.Rational(1, 3),
                sp.Rational(2, 3), sp.Rational(2, 3))
W = sp.diag(1, 1, 1, 1)
W[:2, :2] = A
W[2:, 2:] = A
B = Gamma + s*W

assert B.eigenvals() == {
    -s-sp.Rational(1, 3): 1,
    s-sp.Rational(1, 3): 1,
    sp.Rational(2, 3)-s: 1,
    s+sp.Rational(2, 3): 1,
}

def inertia_at(value):
    vals = [sp.sign(ev.subs(s, value)) for ev in B.eigenvals()]
    return (vals.count(1), vals.count(-1), vals.count(0))

assert inertia_at(sp.Rational(1, 4)) == (2, 2, 0)
assert inertia_at(sp.Rational(1, 2)) == (3, 1, 0)
assert inertia_at(sp.Rational(3, 4)) == (2, 2, 0)

# Crossing forms: symmetric and antisymmetric vectors of a shift block.
vp = sp.Matrix([1, 1])/sp.sqrt(2)
vm = sp.Matrix([1, -1])/sp.sqrt(2)
assert sp.simplify((vp.T*A*vp)[0]) == 1
assert sp.simplify((vm.T*A*vm)[0]) == -1

# A discrete exact version of h +/- S_a h.  S maps e0 to e1 and e1 to e2.
S = sp.Matrix([[0, 0, 0], [1, 0, 0], [0, 1, 0]])
Wa = S+S.T
h = sp.Matrix([1, 0, 0])
fplus = h+S*h
fminus = h-S*h
assert (fplus.T*Wa*fplus)[0] == 2
assert (fminus.T*Wa*fminus)[0] == -2

# Haynsworth negative-index subtraction in an exact two-mode model.
# A0 has exactly two negative modes, both detected by N.
A0 = sp.diag(-2, -3, 5, 7)
N = sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0]])
G = N*A0.inv()*N.T
assert G == sp.diag(-sp.Rational(1, 2), -sp.Rational(1, 3))
Z = sp.Matrix([[0, 0], [0, 0], [1, 0], [0, 1]])
restricted = Z.T*A0*Z
assert restricted == sp.diag(5, 7)

print("PASS one symmetrized threshold shift has both crossing orientations")
print("PASS exact activation path has nonmonotone positive index 2 -> 3 -> 2")
print("PASS maximal r=2 example: two negative modes are removed by two boundary moments")
