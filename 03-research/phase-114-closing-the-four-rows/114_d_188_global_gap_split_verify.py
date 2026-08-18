#!/usr/bin/env python3
"""Arithmetic constants for D.188 global gap and long-time split."""

import math


def mangoldt(N):
    lam = [0.0] * (N + 1)
    sieve = bytearray(b"\x01") * (N + 1)
    sieve[:2] = b"\x00\x00"
    for p in range(2, N + 1):
        if sieve[p]:
            lp = math.log(p)
            q = p
            while q <= N:
                lam[q] = lp
                if q > N // p:
                    break
                q *= p
            if p * p <= N:
                sieve[p * p : N + 1 : p] = b"\x00" * (((N - p * p) // p) + 1)
    return lam


theta = 3.0
rows = []
for N in (1000, 10000, 100000):
    L = math.log(N)
    lam = mangoldt(N)
    W = sum(lam[n] / math.sqrt(n) for n in range(2, N + 1))
    A = 0.0
    for n in range(2, N + 1):
        if lam[n]:
            m = math.ceil(L / math.log(n) - 1e-14)
            gap = 1.0 - math.cos(math.pi / (m + 1))
            A += lam[n] / math.sqrt(n) * gap
    V = sum(lam[n] ** 2 / n for n in range(2, N + 1))
    H = sum(lam[d] * lam[N // d] for d in range(2, N + 1) if N % d == 0) / math.sqrt(N)
    long_bridge = (2.0 * W + 5.0) * math.exp(-theta) / A
    local = theta * (V + H) / A
    rows.append((N, A / math.sqrt(N), long_bridge, local))

assert rows[-1][2] < 0.25
assert rows[-1][3] < rows[0][3]
print("N, A/sqrtN, long bridge, localized endpoint =")
for row in rows:
    print(row)
print("D188 global gap long-time split: PASS")

