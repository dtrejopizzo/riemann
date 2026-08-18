#!/usr/bin/env python3
"""Symbolic checks for the local Blaschke phase identity in D.33."""

import sympy as sp

r, theta = sp.symbols("r theta", positive=True, real=True)
z = sp.exp(sp.I * theta)
b = (z - r) / (1 - r * z)
phase_derivative = sp.simplify(sp.diff(sp.log(b), theta) / sp.I)
poisson = (1 - r**2) / ((1 - r * z) * (1 - r / z))
assert sp.simplify(phase_derivative - poisson) == 0

v = b / z
v_phase_derivative = sp.simplify(sp.diff(sp.log(v), theta) / sp.I)
assert sp.simplify(v_phase_derivative - (poisson - 1)) == 0

# Finite Fourier expansion certificate for P_r-1.
for order in range(1, 8):
    lhs = sp.series(poisson - 1, r, 0, order + 1).removeO().expand()
    rhs = sum(r**k * (z**k + z ** (-k)) for k in range(1, order + 1))
    rhs = sp.series(rhs, r, 0, order + 1).removeO().expand()
    assert sp.simplify(lhs - rhs) == 0

print("D.33 Blaschke defect certificates: PASS")
print("(1/i)d_theta log b_r = P_r")
print("(1/i)d_theta log(b_r/z) = P_r-1")
