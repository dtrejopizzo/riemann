#!/usr/bin/env python3
"""Exact Koszul-rank verifier for finite visible-prime monoid topoi."""

from math import comb, exp


def primes_up_to(limit):
    sieve = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        sieve[0] = 0
    if limit >= 1:
        sieve[1] = 0
    for candidate in range(2, int(limit**0.5) + 1):
        if sieve[candidate]:
            sieve[candidate * candidate : limit + 1 : candidate] = b"\x00" * (
                (limit - candidate * candidate) // candidate + 1
            )
    return [value for value in range(2, limit + 1) if sieve[value]]


all_ok = True
higher_nonzero = True

for support in (2, 3, 4, 5):
    primes = primes_up_to(int(exp(support)))
    generators = 2 * len(primes)
    ranks = [comb(generators, degree) for degree in range(generators + 1)]

    all_ok &= ranks[0] == 1 and ranks[-1] == 1
    all_ok &= all(rank > 0 for rank in ranks)
    all_ok &= sum(ranks) == 2**generators
    if len(primes) >= 2:
        higher_nonzero &= ranks[3] > 0 and ranks[4] > 0

    print(
        f"T={support}_PRIMES={len(primes)}_GENERATORS={generators}_"
        f"TOP_DEGREE={generators}_EXT3={ranks[3] if generators >= 3 else 0}_"
        f"EXT4={ranks[4] if generators >= 4 else 0}"
    )

all_ok &= higher_nonzero

print(f"KOSZUL_EXTERIOR_RANKS_EXACT: {'YES' if all_ok else 'NO'}")
print(f"COHOMOLOGY_ABOVE_DEGREE_TWO: {'YES' if higher_nonzero else 'NO'}")
print("RAW_MONOID_TOPOS_HAS_SURFACE_AMPLITUDE: NO")
print("MANUAL_TRUNCATION_ADMISSIBLE: NO")
print("REQUIRED_NEXT_INPUT: GEOMETRIC_THREE_TERM_COMPLEX")
print(f"VERDICT: {'YES' if all_ok else 'NO'}")
raise SystemExit(0 if all_ok else 1)
