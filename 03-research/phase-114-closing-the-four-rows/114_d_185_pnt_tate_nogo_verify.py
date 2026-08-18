#!/usr/bin/env python3
"""Closed-form audit of the D.185 two-moment resonant countermodel."""

import cmath
import math
import numpy as np


def I0(z):
    return (cmath.exp(z) - 1.0) / z


def I1(z):
    return (cmath.exp(z) * (z - 1.0) + 1.0) / (z * z)


rows = []
for L in (20.0, 40.0, 80.0):
    R = math.exp(0.8 * L)
    eps = math.exp(-math.sqrt(L))

    # Oscillatory moments against 1 and e^v.  Correct with e^{v/2}(a+bv).
    osc0 = eps * I0(0.5 + 1j * R).real
    osc1 = eps * I0(1.5 + 1j * R).real
    mat = np.array(
        [[I0(0.5).real, I1(0.5).real], [I0(1.5).real, I1(1.5).real]]
    )
    a, b = np.linalg.solve(mat, -np.array([osc0, osc1]))
    assert abs(osc0 + a * mat[0, 0] + b * mat[0, 1]) < 2e-15
    assert abs(osc1 + a * mat[1, 0] + b * mat[1, 1]) < 2e-15

    # Fourier value of the weighted perturbation at the resonant frequency.
    resonant = 0.5 * eps * (I0(0.5) + I0(0.5 - 2j * R))
    correction = a * I0(0.5 - 1j * R) + b * I1(0.5 - 1j * R)
    normalized_spike = abs(resonant + correction) / eps
    main = 0.5 * I0(0.5).real
    assert abs(normalized_spike - main) < 1e-5
    assert max(abs(a), abs(b)) / eps < 20.0 / R
    rows.append((L, R, normalized_spike, max(abs(a), abs(b)) / eps))

print("L, R, spike/(eps sqrtN), correction/eps =")
for row in rows:
    print(row)
print("D185 PNT plus Tate low-block no-go: PASS")

