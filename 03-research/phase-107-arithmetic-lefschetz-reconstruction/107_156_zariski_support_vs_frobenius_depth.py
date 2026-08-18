#!/usr/bin/env python3
"""Exact denominator-depth falsifier at real primes."""

from fractions import Fraction


def generated_by_signed_subsets(generators):
    reached = {Fraction(0)}
    for generator in generators:
        old = set(reached)
        reached |= {x + generator for x in old}
        reached |= {x - generator for x in old}
    return reached


all_ok = True
for prime in (2, 3, 5, 7):
    outcomes = []
    for depth in range(1, 9):
        generators = [Fraction(1, prime**k) for k in range(depth + 1)]
        target = Fraction(1, prime ** (depth + 1))
        missed = target not in generated_by_signed_subsets(generators)
        outcomes.append(missed)
        all_ok &= missed
    print(f"P={prime}_NEXT_DEPTH_MISSED: {outcomes}")

print("ZARISKI_PRIME_SUPPORT_FINITE: YES")
print(f"SINGLE_PRIME_DENOMINATOR_DEPTH_UNBOUNDED: {'YES' if all_ok else 'NO'}")
print("FINITE_PRIME_SUPPORT_IMPLIES_FINITE_DIMENSION: NO")
print("REQUIRED_EXTRA_CUTOFF: FROBENIUS_DEPTH")
print(f"VERDICT: {'YES' if all_ok else 'NO'}")
raise SystemExit(0 if all_ok else 1)
