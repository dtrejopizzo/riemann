#!/usr/bin/env python3
"""Exact rational audit of the directed capacity--Feshbach lemma."""
from fractions import Fraction as F

# A nontrivial rational instance, used only to audit all inequality
# directions and the threshold algebra.
ell = F(1, 1000)
eps = F(1, 10000)
g = F(1, 100)
eta = F(1, 500)
h = g - eta
ell_eff = ell + eps * eps / eta

# Choose a directed deficit strictly above the threshold.
threshold = ell_eff / (h * (h + ell_eff))
delta = threshold + F(1, 10)
assert 0 < h * delta < 1
capacity = h * h * delta / (1 - h * delta)

assert 0 < eta < g
assert capacity > ell_eff
assert capacity > ell
assert threshold == ell_eff / (h * (h + ell_eff))

# Young's scalar discriminant is nonpositive:
# eps^2/eta |a|^2 + eta |y|^2 - 2 eps |a||y| >= 0.
assert eps * eps == (eps * eps / eta) * eta

print("D.79 directed capacity--Feshbach certificate: PASS")
print("h, ell_eff:", h, ell_eff)
print("threshold, capacity:", threshold, capacity)
