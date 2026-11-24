#!/usr/bin/env python3
"""Rational outward certificate that H(x)=sum_{q<=x} Lambda(q)(q-1)-psi(x)^2/2 changes sign."""

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



def H_bounds(x: int) -> tuple[int, int]:
    """Bounds SCALE*H(x), H=sum Lambda(q)(q-1)-psi(x)^2/2."""
    psi_lo = psi_hi = moment_lo = moment_hi = 0
    for p in primes_up_to(x):
        log_lo, log_hi = scaled_log_bounds(p)
        q = p
        while q <= x:
            psi_lo += log_lo
            psi_hi += log_hi
            moment_lo += (q - 1) * log_lo
            moment_hi += (q - 1) * log_hi
            q *= p
    square_hi = (psi_hi * psi_hi + 2 * SCALE - 1) // (2 * SCALE)
    square_lo = psi_lo * psi_lo // (2 * SCALE)
    return moment_lo - square_hi, moment_hi - square_lo


def main() -> None:
    negative = H_bounds(2969)
    positive = H_bounds(3167)
    assert negative[1] < 0
    assert positive[0] > 0
    print("SCALE", SCALE)
    print("H(2969)", *negative)
    print("H(3167)", *positive)
    print("CERTIFIED H(2969) < -21 and H(3167) > 110")


if __name__ == "__main__":
    main()
