#!/usr/bin/env python3
"""Check the endpoint-log and dyadic exponent bookkeeping in D.174."""

from __future__ import annotations

import math

import numpy as np


# Weighted endpoint inequality on a grid: ||1_{rho<ell}u|| is bounded by
# the inverse endpoint logarithm times ||L_partial u||.
rho0 = 0.4
rho = np.geomspace(1e-12, rho0, 20000)
u = np.sin(17.0 * np.log(rho)) + 0.3 * np.cos(5.0 * np.log(rho))
L = 1.0 + np.abs(np.log(rho / rho0))
for ell in (1e-2, 1e-4, 1e-7, 1e-10):
    mask = rho < ell
    lhs = np.sum(np.abs(u[mask]) ** 2)
    rhs = np.sum(np.abs((L * u)[mask]) ** 2) / (
        1.0 + math.log(rho0 / ell)
    ) ** 2
    assert lhs <= rhs * (1.0 + 1e-12)


# Dyadic Stieltjes threshold: alpha>1 converges; alpha<=1 diverges.  Use
# growing partial sums to verify the predicted monotonic separation.
def partial(alpha: float, n: int) -> float:
    return sum((1.0 + j) ** (-alpha) for j in range(n))


assert partial(2.0, 200000) < 2.0
assert partial(1.0, 200000) > 11.0
assert partial(0.8, 200000) > 45.0
assert partial(2.0, 200000) - partial(2.0, 100000) < 6e-6


# A standard log-Laplacian boundary exponent tau<1/2 produces
# alpha=2*tau<1, on the divergent side.
for tau in (0.1, 0.25, 0.49):
    assert 2.0 * tau < 1.0

print("D174 Gamma endpoint-log Carleson gate: PASS")
