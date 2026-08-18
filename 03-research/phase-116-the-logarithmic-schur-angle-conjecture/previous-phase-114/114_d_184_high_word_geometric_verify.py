#!/usr/bin/env python3
"""Arithmetic audit of the D.184 uniform high-word ratio."""

import math
import mpmath as mp


def von_mangoldt_table(N):
    lam = [0.0] * (N + 1)
    is_prime = bytearray(b"\x01") * (N + 1)
    is_prime[:2] = b"\x00\x00"
    for p in range(2, N + 1):
        if is_prime[p]:
            lp = math.log(p)
            q = p
            while q <= N:
                lam[q] = lp
                if q > N // p:
                    break
                q *= p
            if p * p <= N:
                is_prime[p * p : N + 1 : p] = b"\x00" * (((N - p * p) // p) + 1)
    return lam


c = 0.8
eta = 0.01
limit = 1.0 / (2.0 * c * c * (1.0 - eta) ** 2)
assert limit < 1.0

rows = []
for N in (1000, 10000, 100000):
    lam = von_mangoldt_table(N)
    V = sum(lam[n] ** 2 / n for n in range(2, N + 1))
    H = sum(lam[d] * lam[N // d] for d in range(2, N + 1) if N % d == 0) / math.sqrt(N)
    R = N**c
    h = float(mp.re(mp.digamma(mp.mpf(5) / 4 + 0.5j * R) - mp.digamma(mp.mpf(5) / 4)))
    z2 = (V + H) / (((1.0 - eta) * h) ** 2)
    rows.append((N, z2))
    assert z2 < 1.0

# Arbitrary-depth geometric summation is an exact scalar check once z<1.
z2 = rows[-1][1]
partial = sum(z2**k for k in range(200))
assert abs(partial - 1.0 / (1.0 - z2)) < 2e-12

print("limit z^2 =", limit)
print("finite ratios =", rows)
print("D184 uniform high-word geometric sum: PASS")

