#!/usr/bin/env python3
"""Exact rational sign certificate for the primitive of psi(x)-x+1."""

from fractions import Fraction
from math import isqrt


SCALE = 10**20
TERMS = 15


def atanh_log_bounds(r: Fraction) -> tuple[Fraction, Fraction]:
    """Bounds log(r), for 1 <= r <= 2, by the atanh series."""
    z = (r - 1) / (r + 1)
    z2 = z * z
    power = z
    lower = Fraction(0)
    for j in range(TERMS + 1):
        lower += 2 * power / (2 * j + 1)
        power *= z2
    remainder = 2 * power / ((2 * TERMS + 3) * (1 - z2))
    return lower, lower + remainder


LOG2_LOWER, LOG2_UPPER = atanh_log_bounds(Fraction(2))


def scaled_log_bounds(n: int) -> tuple[int, int]:
    """Integers L,U such that L/SCALE <= log(n) <= U/SCALE."""
    exponent = n.bit_length() - 1
    reduced = Fraction(n, 1 << exponent)
    lower, upper = atanh_log_bounds(reduced)
    lower += exponent * LOG2_LOWER
    upper += exponent * LOG2_UPPER
    lower_scaled = lower.numerator * SCALE // lower.denominator
    upper_scaled = -((-upper.numerator * SCALE) // upper.denominator)
    return lower_scaled, upper_scaled


def primes_up_to(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[:2] = b"\x00\x00"
    for p in range(2, isqrt(limit) + 1):
        if sieve[p]:
            sieve[p * p : limit + 1 : p] = b"\x00" * (
                (limit - p * p) // p + 1
            )
    return [p for p in range(2, limit + 1) if sieve[p]]


PRIMES = primes_up_to(4000)


def scaled_G_bounds(x: int) -> tuple[int, int]:
    """Bounds SCALE*G(x), with G as in equation (16) of 103_64."""
    lower = upper = -((x - 1) ** 2 * SCALE // 2)
    for p in PRIMES:
        if p > x:
            break
        prime_power = p
        coefficient = 0
        while prime_power <= x:
            coefficient += x - prime_power
            prime_power *= p
        log_lower, log_upper = scaled_log_bounds(p)
        lower += coefficient * log_lower
        upper += coefficient * log_upper
    return lower, upper


def main() -> None:
    lower_2976, upper_2976 = scaled_G_bounds(2976)
    lower_4000, upper_4000 = scaled_G_bounds(4000)

    assert lower_2976 > 10 * SCALE
    assert upper_4000 < -3700 * SCALE

    print("SCALE", SCALE)
    print("2976", lower_2976, upper_2976)
    print("4000", lower_4000, upper_4000)
    print("CERTIFIED G(2976) > 10 and G(4000) < -3700")


if __name__ == "__main__":
    main()
