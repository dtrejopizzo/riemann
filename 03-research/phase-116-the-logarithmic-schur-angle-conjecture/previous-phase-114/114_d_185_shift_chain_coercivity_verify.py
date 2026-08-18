#!/usr/bin/env python3
"""Finite audits for the exact shift-chain bound in D.185."""

import math
import numpy as np


def jordan(m):
    out = np.zeros((m, m))
    if m > 1:
        out[np.arange(m - 1), np.arange(1, m)] = 1.0
    return out


for m in range(1, 80):
    j = jordan(m)
    radius = np.linalg.eigvalsh((j + j.T) / 2).max()
    assert abs(radius - math.cos(math.pi / (m + 1))) < 3e-14

for ratio in np.geomspace(1.0, 1.0e5, 10000):
    m = math.ceil(ratio)
    exact_gap = 1 - math.cos(math.pi / (m + 1))
    elementary = 2 / (9 * ratio * ratio)
    assert exact_gap + 1e-15 >= elementary


def mangoldt_table(nmax):
    lam = np.zeros(nmax + 1)
    sieve = np.ones(nmax + 1, dtype=bool)
    sieve[:2] = False
    for p in range(2, int(math.sqrt(nmax)) + 1):
        if sieve[p]:
            sieve[p * p :: p] = False
    for p in np.nonzero(sieve)[0]:
        q = int(p)
        while q <= nmax:
            lam[q] = math.log(p)
            q *= int(p)
    return lam


for nmax in (100, 1000, 10000, 100000):
    lam = mangoldt_table(nmax)
    length = math.log(nmax)
    exact = 0.0
    elementary = 0.0
    for n in np.nonzero(lam)[0]:
        b = math.log(n)
        w = lam[n] / math.sqrt(n)
        exact += w * (1 - math.cos(math.pi / (math.ceil(length / b) + 1)))
        elementary += w * 2 * b * b / (9 * length * length)
    assert exact >= elementary
    print(nmax, "A_N/sqrt(N)=", exact / math.sqrt(nmax))

print("D185 zero-extension shift-chain coercivity: PASS")
