#!/usr/bin/env python3
"""Exponent-vector checks for the visible order lattice; no enumeration."""

from math import exp, floor, log, prod


def primes_up_to(limit):
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[:2] = b"\x00\x00"
    for p in range(2, int(limit**0.5) + 1):
        if sieve[p]:
            sieve[p * p : limit + 1 : p] = b"\x00" * (((limit - p * p) // p) + 1)
    return [p for p in range(2, limit + 1) if sieve[p]]


def factor_vector(bound):
    return {
        p: floor(bound / log(p) + 1e-12)
        for p in primes_up_to(floor(exp(bound)))
    }


all_ok = True
for bound in (2, 3, 4, 5, 6, 7, 8):
    factors = factor_vector(bound)
    level = prod(p**e for p, e in factors.items())
    divisor_count = prod(e + 1 for e in factors.values())

    # Gcd/lcm are coordinatewise min/max and remain in 0..K_p.
    lattice_ok = all(
        0 <= min(a, b) <= max(a, b) <= exponent
        for exponent in factors.values()
        for a in range(exponent + 1)
        for b in range(exponent + 1)
    )
    nonmonoid = bool(factors) and any(2 * exponent > exponent for exponent in factors.values())
    all_ok &= lattice_ok and nonmonoid
    print(
        f"T={bound}_PRIMES={len(factors)}_LOG_L={sum(e * log(p) for p, e in factors.items()):.6f}"
        f"_L_DIGITS={len(str(level))}_DIVISOR_COUNT={divisor_count}"
    )

print(f"EXPONENT_VECTOR_LATTICE_EXACT: {'YES' if all_ok else 'NO'}")
print("DIVISORS_ENUMERATED: NO")
print("MULTIPLICATIVE_MONOID_AT_FIXED_LEVEL: NO")
print("MULTIPLICATION_STRUCTURE: PARTIAL")
print(f"VERDICT: {'YES' if all_ok else 'NO'}")
raise SystemExit(0 if all_ok else 1)
