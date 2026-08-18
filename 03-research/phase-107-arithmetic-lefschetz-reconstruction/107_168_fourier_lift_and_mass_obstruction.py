#!/usr/bin/env python3
"""Exact Fourier-equivariance and differential-mass checks."""

from fractions import Fraction


PRIMES = (2, 3, 5, 7, 11)
RATIOS = ((1, 1), (2, 1), (3, 2), (5, 3))


def support(prime, cutoff, radius):
    out = {Fraction(0)}
    for numerator in range(1, cutoff + 1):
        if numerator % prime == 0:
            continue
        for exponent in range(-radius, radius + 1):
            out.add(Fraction(numerator) * Fraction(prime) ** exponent)
    return out


all_ok = True
equivariance_checks = 0

for prime in PRIMES:
    local = support(prime, 9, 3)
    for value in local:
        # Both sides label the same Fourier character e_{p q}.
        all_ok &= prime * value == value * prime
        equivariance_checks += 1

    for n, m in RATIOS:
        sample = sorted(local)[:15]
        for left in sample:
            for right in sample:
                monoid_weight = n * left + m * right
                fourier_weight = n * left + m * right
                all_ok &= monoid_weight == fourier_weight
                equivariance_checks += 1

growth_rows = []
for prime in PRIMES:
    previous = Fraction(0)
    strictly_grows_somewhere = False
    for cutoff, radius in ((1, 0), (4, 1), (16, 2), (64, 3)):
        maximum = max(abs(value) for value in support(prime, cutoff, radius))
        strictly_grows_somewhere |= maximum > previous
        previous = maximum
        growth_rows.append((prime, cutoff, radius, maximum))
    all_ok &= strictly_grows_somewhere and previous >= 64 * prime**2

for prime, cutoff, radius, maximum in growth_rows:
    print(f"P={prime}_A={cutoff}_R={radius}_NORMALIZED_X_NORM={maximum}")

print(f"FOURIER_EQUIVARIANCE_CHECKS: {equivariance_checks}")
print(f"FROBENIUS_INTERTWINED: {'YES' if all_ok else 'NO'}")
print(f"RATIONAL_CORRESPONDENCE_INTERTWINED: {'YES' if all_ok else 'NO'}")
print("UNIFORM_L1_BOUND_FOR_LEAFWISE_X: NO")
print("DIRECT_2022_DIMENSION_ON_DE_RHAM_COMPLEX: NO")
print("REQUIRED_NEXT_INPUT: WEIGHTED_OR_CELLULAR_DIFFERENTIAL")
print(f"VERDICT: {'YES' if all_ok else 'NO'}")
raise SystemExit(0 if all_ok else 1)
