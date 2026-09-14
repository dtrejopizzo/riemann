#!/usr/bin/env python3
"""Finite regression checks for the rational dagger algebra of P123.003.

The analytic nuclearity and Fourier-uniqueness arguments are proofs in the
note.  This script checks their exact finite arithmetic identities and the
height-count estimate on increasing boxes.
"""

from __future__ import annotations

from fractions import Fraction
from math import gcd


Seq = dict[Fraction, complex]


def height(q: Fraction) -> int:
    return max(q.numerator, q.denominator)


def conv(a: Seq, b: Seq) -> Seq:
    out: Seq = {}
    for q, aq in a.items():
        for r, br in b.items():
            qr = q * r
            out[qr] = out.get(qr, 0j) + aq * br
    return {q: z for q, z in out.items() if z != 0}


def dagger(a: Seq) -> Seq:
    return {1 / q: z.conjugate() for q, z in a.items()}


def seminorm(a: Seq, k: int) -> float:
    return sum(abs(z) * height(q) ** k for q, z in a.items())


def exact_height_count(n: int) -> int:
    if n == 1:
        return 1
    return sum(
        1
        for a in range(1, n + 1)
        for b in range(1, n + 1)
        if max(a, b) == n and gcd(a, b) == 1
    )


def main() -> None:
    rationals = [
        Fraction(a, b)
        for a in range(1, 20)
        for b in range(1, 20)
        if gcd(a, b) == 1
    ]
    for q in rationals:
        assert height(1 / q) == height(q)
        for r in rationals:
            assert height(q * r) <= height(q) * height(r)

    a: Seq = {
        Fraction(2): 2 + 3j,
        Fraction(3, 5): -1j,
        Fraction(7, 2): 4 - 2j,
    }
    b: Seq = {
        Fraction(1, 3): 1 - 1j,
        Fraction(5): -2 + 0j,
        Fraction(2, 7): 3j,
    }

    assert dagger(dagger(a)) == a
    assert dagger(conv(a, b)) == conv(dagger(b), dagger(a))
    for k in range(6):
        assert seminorm(dagger(a), k) == seminorm(a, k)
        assert seminorm(conv(a, b), k) <= seminorm(a, k) * seminorm(b, k) + 1e-12

    partial_nuclear_sum = 0.0
    for n in range(1, 500):
        count = exact_height_count(n)
        assert count <= (1 if n == 1 else 2 * n)
        partial_nuclear_sum += count / n**4
    assert partial_nuclear_sum < 4.0

    # The old positive-integer algebra embeds with the same weights.
    for n in range(1, 100):
        assert height(Fraction(n, 1)) == n

    print("P123.003 symmetric height identities: PASS")
    print("P123.003 convolution/dagger identities: PASS")
    print("P123.003 finite nuclear-sum bound: PASS")
    print("Scope: regression only; strict crossed-product sheaf descent remains OPEN")


if __name__ == "__main__":
    main()

