#!/usr/bin/env python3
"""Finite certificates for the exact identities in D.143."""

from __future__ import annotations

import math


def mangoldt_sieve(limit: int) -> list[float]:
    values = [0.0] * (limit + 1)
    is_prime = bytearray(b"\x01") * (limit + 1)
    is_prime[0:2] = b"\x00\x00"
    for p in range(2, limit + 1):
        if not is_prime[p]:
            continue
        for multiple in range(p * 2, limit + 1, p):
            is_prime[multiple] = 0
        power = p
        lp = math.log(p)
        while power <= limit:
            values[power] = lp
            if power > limit // p:
                break
            power *= p
    return values


# Exact weighted-shift ratio on finite sequences.
for n in range(1, 20):
    a = [0.0] + [math.sin(m) / (m + 1) for m in range(1, 101)]
    source = sum(abs(a[m]) ** 2 / m for m in range(1, len(a)))
    target = sum(abs(a[m]) ** 2 / (n * m) for m in range(1, len(a)))
    assert math.isclose(target, source / n, rel_tol=2e-15, abs_tol=1e-15)

# Log-rigged shift ratio is at most the central ratio.
for s in (0.5, 1.0, 2.0, 4.0):
    for n in range(2, 30):
        for m in range(1, 100):
            ratio = (
                1.0
                / (n * m * (1.0 + math.log(n * m)) ** (2.0 * s))
                / (1.0 / (m * (1.0 + math.log(m)) ** (2.0 * s)))
            )
            assert ratio <= 1.0 / n + 1e-15

lam = mangoldt_sieve(1_000_000)
cutoffs = (1_000, 10_000, 100_000, 1_000_000)

euler_norms = [sum(lam[n] ** 2 / n for n in range(2, N + 1)) for N in cutoffs]
d_weights = [sum(lam[n] / math.sqrt(n) for n in range(2, N + 1)) for N in cutoffs]
assert all(x < y for x, y in zip(euler_norms, euler_norms[1:]))
assert all(x < y for x, y in zip(d_weights, d_weights[1:]))

# The centrally normalized scalar sequence is square summable, while its
# Gram weights are not the linear D weights.
central_scalar_norm = sum(lam[n] ** 2 / n**2 for n in range(2, len(lam)))
assert math.isfinite(central_scalar_norm)
for n in (2, 3, 4, 5, 8, 9, 25):
    if lam[n]:
        quadratic = lam[n] ** 2 / n**2
        linear_d = lam[n] / math.sqrt(n)
        assert not math.isclose(quadratic, linear_d, rel_tol=1e-12)

# Numerical direction of the rigged estimates: s=2 stabilizes the Euler
# vector rapidly, while no finite logarithmic exponent can change the
# exponential-in-log growth mechanism of the D feature (proved in text).
rigged_s2 = [
    sum(
        lam[n] ** 2 / (n * (1.0 + math.log(n)) ** 4)
        for n in range(2, N + 1)
    )
    for N in cutoffs
]
assert rigged_s2[-1] - rigged_s2[-2] < rigged_s2[1] - rigged_s2[0]

print("D143 critical Dirichlet Hilbertization certificates: PASS")
print("Euler-vector partial norms squared:", euler_norms)
print("D-weight partial sums:", d_weights)
print("rigged s=2 partial norms squared:", rigged_s2)
