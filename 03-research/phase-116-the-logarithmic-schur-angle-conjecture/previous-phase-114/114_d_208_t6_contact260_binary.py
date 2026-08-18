#!/usr/bin/env python3
"""Polynomial-exact binary64 centre of the T6 contact block on V260."""

import math
import os

import numpy as np
from numpy.polynomial.legendre import leggauss, legvander


N = 260
T = 0.5 * math.log(6.0)
order = N + 4
nodes, weights = leggauss(order)
scales = np.sqrt((2 * np.arange(N) + 1) / 2)
C = np.zeros((N, N))
for nn, mangoldt in (
    (2, math.log(2.0)),
    (3, math.log(3.0)),
    (4, math.log(2.0)),
    (5, math.log(5.0)),
):
    d = math.log(nn) / T
    midpoint = -d / 2
    half = 1 - d / 2
    u = midpoint + half * nodes
    vx = legvander(u, N - 1) * scales
    vy = legvander(u + d, N - 1) * scales
    C -= (mangoldt / math.sqrt(nn)) * half * (
        (vx * weights[:, None]).T @ vy
        + (vy * weights[:, None]).T @ vx
    )
    print("contact", nn, "complete", flush=True)

symmetry_error = np.linalg.norm(C - C.T, ord=np.inf)
assert symmetry_error < 1e-12
save = os.environ.get("D208_CONTACT_SAVE", "/tmp/t6_contact260_binary.npz")
np.savez(save, C=(C + C.T) / 2, order=np.array(order), N=np.array(N))
print("symmetry error", symmetry_error)
print("saved", save)
print("D208 BINARY CONTACT260 CENTRE: PASS (diagnostic only)")
