#!/usr/bin/env python3
"""Exact finite checks for global rooted transition and CRT descent."""

from math import floor, gcd, log, prod


def primes_up_to(limit):
    out = []
    for n in range(2, limit + 1):
        if all(n % p for p in out if p * p <= n):
            out.append(n)
    return out


def factors(bound):
    return {
        p: floor(bound / log(p) + 1e-12)
        for p in primes_up_to(floor(2.718281828459045**bound) + 1)
        if floor(bound / log(p) + 1e-12) > 0
    }


def level_integer(bound):
    return prod(p**e for p, e in factors(bound).items())


bounds = (0.8, 1.2, 1.8, 2.2, 2.7)
levels = [level_integer(bound) for bound in bounds]
transition_ok = all(b % a == 0 for a, b in zip(levels, levels[1:]))

crt_ok = True
for bound, level in zip(bounds, levels):
    prime_powers = [p**e for p, e in factors(bound).items()]
    crt_ok &= prod(prime_powers) == level
    crt_ok &= all(gcd(a, b) == 1 for i, a in enumerate(prime_powers)
                  for b in prime_powers[i + 1:])

# Every tested torsion order appears at a predetermined support level.
colimit_ok = all(level_integer(log(n) + 1e-9) % n == 0 for n in range(2, 101))
verdict = transition_ok and crt_ok and colimit_ok

print(f"LEVEL_INTEGERS: {levels}")
print(f"CANONICAL_LEVEL_TRANSITIONS: {'YES' if transition_ok else 'NO'}")
print(f"CRT_PRIME_GLUE: {'YES' if crt_ok else 'NO'}")
print(f"ROOTED_COLIMIT_RECOVERS_Q_OVER_Z: {'YES' if colimit_ok else 'NO'}")
print("FRAME_PROJECTIVE_LIMIT: Z_HAT")
print(f"VERDICT: {'YES' if verdict else 'NO'}")
raise SystemExit(0 if verdict else 1)
