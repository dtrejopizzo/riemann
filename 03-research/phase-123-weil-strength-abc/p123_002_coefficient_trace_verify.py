#!/usr/bin/env python3
"""Finite regression checks for P123.001--P123.002.

This script checks the algebraic identities on finite-support elements of
the Dirichlet convolution algebra.  It is not a proof of localization,
descent, mixed Riemann--Roch, or a scalar intersection formula.
"""

from __future__ import annotations

from fractions import Fraction


Seq = dict[int, Fraction]


def conv(a: Seq, b: Seq) -> Seq:
    out: Seq = {}
    for m, am in a.items():
        for n, bn in b.items():
            out[m * n] = out.get(m * n, Fraction(0)) + am * bn
    return {n: c for n, c in out.items() if c}


def add(a: Seq, b: Seq) -> Seq:
    out = dict(a)
    for n, c in b.items():
        out[n] = out.get(n, Fraction(0)) + c
    return {n: c for n, c in out.items() if c}


def iota(a: Seq) -> list[list[Seq]]:
    zero: Seq = {}
    return [
        [zero, zero, zero],
        [zero, zero, zero],
        [zero, zero, a],
    ]


def matmul(a: list[list[Seq]], b: list[list[Seq]]) -> list[list[Seq]]:
    out = [[{} for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                out[i][j] = add(out[i][j], conv(a[i][k], b[k][j]))
    return out


def trace(a: list[list[Seq]]) -> Seq:
    return add(add(a[0][0], a[1][1]), a[2][2])


def delta(n: int, coefficient: int = 1) -> Seq:
    return {n: Fraction(coefficient)}


def main() -> None:
    unit = delta(1)
    samples = [
        add(delta(2, 3), delta(5, -1)),
        add(delta(3, 2), delta(7, 4)),
        add(delta(1, -2), delta(11, 5)),
    ]

    for a in samples:
        assert conv(a, unit) == a == conv(unit, a)
        assert trace(iota(a)) == a

    for a in samples:
        for b in samples:
            lhs = trace(matmul(iota(a), iota(b)))
            rhs = conv(a, b)
            assert lhs == rhs
            assert lhs == trace(matmul(iota(b), iota(a)))

    for m in (2, 3, 5, 7):
        for n in (2, 3, 5, 7):
            assert conv(delta(m), delta(n)) == delta(m * n)

    # Finite-support radical test: pairing with the convolution unit returns
    # the original coefficient vector.
    for a in samples:
        assert trace(matmul(iota(a), iota(unit))) == a

    print("P123.001 mixed endomorphism corner: PASS")
    print("P123.002 coefficient trace/cyclicity: PASS")
    print("P123.002 coefficient-valued radical test: PASS")
    print("Scope: finite regression only; kernel localization and scalar trace remain OPEN")


if __name__ == "__main__":
    main()

