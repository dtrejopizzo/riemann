#!/usr/bin/env python3
"""Verify the collision-only no-go of D.177."""

from __future__ import annotations

import math

import numpy as np


def von_mangoldt(n: int) -> float:
    if n < 2:
        return 0.0
    for p in range(2, n + 1):
        prime = all(p % d for d in range(2, int(math.sqrt(p)) + 1))
        if not prime:
            continue
        m = n
        while m % p == 0:
            m //= p
        if m == 1:
            return math.log(p)
    return 0.0


def H(N: int) -> float:
    return sum(von_mangoldt(n) * von_mangoldt(N // n)
               for n in range(1, N + 1) if N % n == 0) / math.sqrt(N)


def E0(N: int) -> float:
    return sum(von_mangoldt(n) / math.sqrt(n) for n in range(1, N + 1)) \
        - 2.0 * (math.sqrt(N) - 1.0)


for p in (5, 7, 11, 13, 17, 19):
    assert abs(H(p)) < 1e-15
    assert abs(E0(p)) > 1e-3

# Exact two-sided collision matrix at a composite cell.
N = 16
active = [n for n in range(2, N + 1) if von_mangoldt(n) > 0]
w = {n: von_mangoldt(n) / math.sqrt(n) for n in active}
V = sum(x * x for x in w.values())
Hn = sum(w[n] * w[m] for n in active for m in active if n * m == N)
assert abs(Hn - H(N)) < 2e-15
gram = np.array([[V, Hn], [Hn, V]])
assert np.linalg.eigvalsh(gram)[0] >= -1e-14

# A finite spatial discretization of the one-sided synthesis has rank d.
# Removing two arbitrary Tate target directions lowers rank by at most two,
# so for d>4 the centered target is not rank two.
d = 9
r = len(active)
B = np.vstack([w[n] * np.eye(d) for n in active])
assert np.linalg.matrix_rank(B) == d
rng = np.random.default_rng(177)
Z, _ = np.linalg.qr(rng.normal(size=(r * d, 2)))
P = np.eye(r * d) - Z @ Z.T
assert np.linalg.matrix_rank(P @ B, tol=1e-10) >= d - 2
assert np.linalg.matrix_rank(P @ B, tol=1e-10) > 2

print("prime witnesses E_N(0) =", {p: E0(p) for p in (5, 7, 11)})
print("N=16 (V_N,H_N) =", (V, Hn))
print("D177 collision-only reduction audit: PASS")
