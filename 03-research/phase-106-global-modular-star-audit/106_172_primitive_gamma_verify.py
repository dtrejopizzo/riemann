#!/usr/bin/env python3
"""Numerical audit for the scalar finite part in Document 106.172."""

from __future__ import annotations

import math


def primes_up_to(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[:2] = b"\x00\x00"
    stop = math.isqrt(limit)
    for q in range(2, stop + 1):
        if sieve[q]:
            sieve[q * q : limit + 1 : q] = b"\x00" * (
                (limit - q * q) // q + 1
            )
    return [q for q in range(2, limit + 1) if sieve[q]]


def main() -> None:
    limit = 2_000_000
    primes = primes_up_to(limit)

    closed = sum(math.log(p) / (p * (p - 1)) for p in primes)

    # Independent repeated-winding truncation.  The omitted tail for each
    # fixed p is bounded geometrically and is far below the printed scale.
    direct = 0.0
    for p in primes:
        term = 1.0 / (p * p)
        local = 0.0
        while term > 1e-20:
            local += term
            term /= p
        direct += math.log(p) * local

    kappa = math.euler_gamma + closed if hasattr(math, "euler_gamma") else None
    # Python versions before 3.11 do not expose math.euler_gamma.
    if kappa is None:
        euler_gamma = 0.577215664901532860606512090082402431
        kappa = euler_gamma + closed

    print(f"prime cutoff                         {limit}")
    print(f"closed repeated-winding sum          {closed:.15e}")
    print(f"direct repeated-winding sum          {direct:.15e}")
    print(f"difference                           {abs(closed-direct):.3e}")
    print(f"partial kappa_infinity               {kappa:.15e}")
    print(f"positive                             {kappa > 0.0}")


if __name__ == "__main__":
    main()
