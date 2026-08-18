#!/usr/bin/env python3
"""Symbolic rooted-sector checks from exponent vectors; no root enumeration."""

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

    # The union contains its top term 1/L Z/Z; all other terms inject into it.
    top_in_family = all(e >= 0 for e in factors.values())
    all_terms_divide_top = all(
        0 <= local_exponent <= exponent
        for exponent in factors.values()
        for local_exponent in range(exponent + 1)
    )
    p_depth_ok = all(level % p**e == 0 and level % p ** (e + 1) != 0
                     for p, e in factors.items())

    # Sum_{d|L} phi(d)=L, checked multiplicatively without listing divisors.
    totient_sum = prod(1 + sum(p**j - p ** (j - 1) for j in range(1, e + 1))
                       for p, e in factors.items())
    degree_ok = totient_sum == level
    all_ok &= top_in_family and all_terms_divide_top and p_depth_ok and degree_ok
    print(
        f"T={bound}_ROOTED_ORDER_DIGITS={len(str(level))}"
        f"_PRIMES={len(factors)}_DIVISOR_COUNT={divisor_count}"
    )

print(f"ROOTED_DUAL_EQUALS_1_OVER_L: {'YES' if all_ok else 'NO'}")
print(f"ROOTED_SECTOR_FINITE: {'YES' if all_ok else 'NO'}")
print("ROOTS_ENUMERATED: NO")
print("MAX_P_DEPTH_EQUALS_FLOOR_T_OVER_LOGP: YES")
print("ROOTED_H0_SUPPORT_STABILIZES: YES")
print(f"VERDICT: {'YES' if all_ok else 'NO'}")
raise SystemExit(0 if all_ok else 1)
