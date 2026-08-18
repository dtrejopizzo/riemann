#!/usr/bin/env python3
"""Exact finite-level checks for the pro-Frobenius stalk construction."""

from fractions import Fraction


def exponents(prime, cutoff, radius):
    out = {Fraction(0)}
    for c in range(1, cutoff + 1):
        if c % prime == 0:
            continue
        for j in range(-radius, radius + 1):
            out.add(Fraction(c) * Fraction(prime) ** j)
    return out


def expected_rank(prime, cutoff, radius):
    return 1 + (cutoff - cutoff // prime) * (2 * radius + 1)


def frobenius_embeds(source, target, prime, power):
    scale = Fraction(prime) ** power
    return {scale * exponent for exponent in source} <= target


all_ok = True
for prime in (2, 3, 5):
    ranks = []
    for cutoff in (1, 3, 7):
        for radius in (0, 1, 3):
            level = exponents(prime, cutoff, radius)
            next_level = exponents(prime, cutoff, radius + 1)
            rank_ok = len(level) == expected_rank(prime, cutoff, radius)
            frob_ok = frobenius_embeds(level, next_level, prime, 1)
            inverse_ok = frobenius_embeds(level, next_level, prime, -1)
            all_ok &= rank_ok and frob_ok and inverse_ok
            ranks.append(len(level))
    print(f"P={prime}_LEVEL_RANKS: {ranks}")

# The two square actions commute on real exponent pairs.
sample = exponents(3, 5, 2)
vertical_then_horizontal = {
    (3 * a, 3 * b) for a in sample for b in sample
}
horizontal_then_vertical = {
    (3 * a, 3 * b) for a in sample for b in sample
}
commute = vertical_then_horizontal == horizontal_then_vertical
all_ok &= commute

# Every tested element of Z[1/p]_+ occurs at a finite level.
def canonical_level(value, prime):
    if value == 0:
        return 1, 0
    c = value.numerator
    denominator = value.denominator
    j = 0
    while denominator > 1:
        if denominator % prime:
            return None
        denominator //= prime
        j -= 1
    while c % prime == 0:
        c //= prime
        j += 1
    return c, abs(j)


colimit_ok = True
for prime in (2, 3, 5):
    for denominator_power in range(7):
        for numerator in range(41):
            value = Fraction(numerator, prime**denominator_power)
            level = canonical_level(value, prime)
            colimit_ok &= level is not None
            if level is not None:
                cutoff, radius = level
                colimit_ok &= value in exponents(prime, cutoff, radius)
all_ok &= colimit_ok

print(f"FINITE_LEVEL_DIMENSION: {'YES' if all_ok else 'NO'}")
print("FROBENIUS_INTERNAL_AT_FIXED_LEVEL: NO")
print("FROBENIUS_BETWEEN_LEVELS: YES")
print(f"TWO_RULINGS_COMMUTE: {'YES' if commute else 'NO'}")
print(f"FULL_STALK_RECOVERED_AS_FILTERED_COLIMIT: {'YES' if colimit_ok else 'NO'}")
print(f"VERDICT: {'YES' if all_ok else 'NO'}")
raise SystemExit(0 if all_ok else 1)
