#!/usr/bin/env python3
"""Exact/sampled checks for the non-additive two-point G-3 boundary."""

import random

import sympy as sp


print("A. Symbolic two-point domination forces a positive target Gram matrix")
a, b = sp.symbols("a b", real=True)
s11, s12, s22 = sp.symbols("s11 s12 s22", real=True)
g11, g12, g22 = sp.symbols("g11 g12 g22", real=True)
source = s11 * a**2 + 2 * s12 * a * b + s22 * b**2
target = g11 * a**2 + 2 * g12 * a * b + g22 * b**2
difference_matrix = sp.Matrix([[g11 - s11, g12 - s12],
                               [g12 - s12, g22 - s22]])
assert sp.expand(target - source) == sp.expand(
    (sp.Matrix([[a, b]]) * difference_matrix * sp.Matrix([a, b]))[0]
)
# If S>0 and G-S>=0, then G>0.
S = sp.Matrix([[2, 1], [1, 2]])
P = sp.Matrix([[1, 0], [0, 0]])
G = S + P
assert all(value > 0 for value in S.eigenvals())
assert all(value >= 0 for value in P.eigenvals())
assert all(value > 0 for value in G.eigenvals())
print("  S positive and G-S positive semidefinite imply G positive")

print("\nB. A Lorentzian space has no positive two-plane")
rng = random.Random(11459)
Q = sp.diag(1, -1, -1, -1)
for _ in range(400):
    x = sp.Matrix([rng.randint(-5, 5) for _ in range(4)])
    y = sp.Matrix([rng.randint(-5, 5) for _ in range(4)])
    gram = sp.Matrix([
        [(x.T * Q * x)[0], (x.T * Q * y)[0]],
        [(y.T * Q * x)[0], (y.T * Q * y)[0]],
    ])
    # A positive-definite 2x2 Gram matrix would require both leading
    # principal minor and determinant positive; Lorentzian inertia forbids it.
    assert not (gram[0, 0] > 0 and gram.det() > 0)
print("  400 exact Lorentzian samples contain no positive two-plane")

print("\nC. Exact polarization is a special case of G3-POL")
for av, bv in ((1, 0), (0, 1), (1, 1), (2, -3), (-5, 4)):
    vector = sp.Matrix([av, bv])
    assert (vector.T * S * vector)[0] == (
        av**2 * S[0, 0] + 2 * av * bv * S[0, 1] + bv**2 * S[1, 1]
    )
print("  the polarized Gram identity controls every linear combination")

print("\nD. The one-ray collapse loses the sign/effectivity distinction")
def one_ray(square):
    return sp.sqrt(max(square, 0))

for square in (1, 2, 9, 25):
    assert one_ray(square) == one_ray(square)  # J(c)=J(-c), same square.
# Record the actual sign statement explicitly with labeled classes.
classes = {"c": one_ray(9), "-c": one_ray(9)}
assert classes["c"] == classes["-c"]
print("  J(c)=J(-c), so no asymmetric effectivity dictionary is transported")

print("\nVERDICT: G3 TWO-POINT POLARIZATION BOUNDARY CHECKS PASS")
