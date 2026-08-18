#!/usr/bin/env python3
"""Finite checks for a_47: classification and nonfaithfulness of M_n."""

from math import gcd


def prime_factors(n: int) -> tuple[int, ...]:
    factors = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            factors.append(p)
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        factors.append(n)
    return tuple(factors)


def shadow(n: int):
    """None is the Z tensor unit, 1 is zero, p is the p-contact sheaf."""
    factors = prime_factors(n)
    if not factors:
        return None
    if len(factors) == 1:
        return factors[0]
    return 1


def tensor(left, right):
    if left is None:
        return right
    if right is None:
        return left
    return gcd(left, right)


print("A. Complete classification of contact shadows")
assert shadow(1) is None
for p in (2, 3, 5, 7, 11, 13):
    assert len({shadow(p**k) for k in range(1, 8)}) == 1
for n in range(2, 2001):
    factors = prime_factors(n)
    expected = factors[0] if len(factors) == 1 else 1
    assert shadow(n) == expected
print("  prime powers retain only p; multi-prime labels have zero shadow")

print("\nB. Monoidal law")
for m in range(1, 401):
    for n in range(1, 401):
        assert tensor(shadow(m), shadow(n)) == shadow(m * n)
print("  M_m tensor M_n = M_mn on the full grid")

print("\nC. Explicit nonfaithfulness")
assert shadow(2) == shadow(4) == shadow(8)
assert shadow(6) == shadow(10) == shadow(15) == 1
print("  2,4,8 collide; 6,10,15 collide in the zero shadow")

print("\nVERDICT: I7 CONTACT-SHADOW NONFAITHFULNESS CHECKS PASS")
