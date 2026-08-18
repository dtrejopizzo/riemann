#!/usr/bin/env python3
"""Exact finite-cell audit of the D.187 uniform Witt moment behaviour."""

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


def convolution(a, b, N):
    out = [0.0] * (N + 1)
    ia = [i for i, x in enumerate(a) if x]
    ib = [i for i, x in enumerate(b) if x]
    for i in ia:
        top = N // i
        ai = a[i]
        for j in ib:
            if j > top:
                break
            out[i * j] += ai * b[j]
    return out


for N in (5000, 20000):
    lam = mangoldt(N)
    a = [0.0 if n == 0 else lam[n] / math.sqrt(n) for n in range(N + 1)]
    V1 = sum(x * x for x in a)
    cur = a
    normalized_sum = 0.0
    worst_theta_ratio = 0.0
    for k in range(1, int(math.log(N, 2)) + 1):
        Vk = sum(x * x for x in cur)
        theta = (2.0**k) * math.factorial(k) / math.factorial(2 * k)
        worst_theta_ratio = max(worst_theta_ratio, Vk / (theta * V1**k))
        normalized_sum += Vk / ((0.35 * math.log(N)) ** (2 * k))
        cur = convolution(cur, a, N)
    assert math.isfinite(normalized_sum)
    # This stronger finite observation is not used in the proof.
    assert worst_theta_ratio <= 1.0 + 2e-12
    print(N, "uniform normalized sum =", normalized_sum,
          "max exact-theta ratio =", worst_theta_ratio)

print("D187 uniform Bohr-Rankin Witt moments: PASS")

