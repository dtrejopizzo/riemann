#!/usr/bin/env python3
"""Verify the fixed-depth Witt word Grams and their first constants."""

from __future__ import annotations

import math

import numpy as np


def mangoldt_sieve(N: int) -> np.ndarray:
    lam = np.zeros(N + 1)
    prime = np.ones(N + 1, dtype=bool)
    prime[:2] = False
    for p in range(2, N + 1):
        if not prime[p]:
            continue
        lp = math.log(p)
        x = p
        while x <= N:
            lam[x] = lp
            if x > N // p:
                break
            x *= p
        if p * p <= N:
            prime[p * p:N + 1:p] = False
    return lam


def dirichlet_convolution(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    N = min(len(a), len(b)) - 1
    out = np.zeros(N + 1)
    ia = np.flatnonzero(a)
    ib = np.flatnonzero(b)
    for d in ia:
        js = ib[ib <= N // d]
        out[d * js] += a[d] * b[js]
    return out


records = []
for N in (1000, 3000, 10000, 30000, 100000):
    lam = mangoldt_sieve(N)
    lam2 = dirichlet_convolution(lam, lam)
    n = np.arange(1, N + 1)
    V1 = np.sum(lam[1:] ** 2 / n)
    V2 = np.sum(lam2[1:] ** 2 / n)
    L = math.log(N)
    records.append((N, V1 / L**2, V2 / L**4))

# Ratios move toward 1/2 and 1/12 from below at these cutoffs.
assert 0.46 < records[-1][1] < 0.51
assert 0.06 < records[-1][2] < 0.09
assert records[-1][1] > records[0][1]
assert records[-1][2] > records[0][2]

# Exact collision identity H_{N,k}=Lambda_{2k}(N)/sqrt(N).
N = 144
lam = mangoldt_sieve(N)
lam2 = dirichlet_convolution(lam, lam)
lam4 = dirichlet_convolution(lam2, lam2)
active = np.flatnonzero(lam2)
H2 = sum(lam2[m] * lam2[N // m] for m in active if N % m == 0) / math.sqrt(N)
assert abs(H2 - lam4[N] / math.sqrt(N)) < 2e-12

# Leading normalized constants theta_k=1/(2k-1)!! are summable.
theta = []
for k in range(1, 20):
    value = (2.0**k * math.factorial(k)) / math.factorial(2 * k)
    odd_df = math.prod(range(1, 2 * k, 2))
    assert abs(value - 1.0 / odd_df) < 1e-15
    theta.append(value)
assert sum(theta) < 1.42

print("(N, V1/log^2, V2/log^4) =", records)
print("sum theta_1..theta_19 =", sum(theta))
print("D178 fixed-depth Witt word Gram: PASS")
