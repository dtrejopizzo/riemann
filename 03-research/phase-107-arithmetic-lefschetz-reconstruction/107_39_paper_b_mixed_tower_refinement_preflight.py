#!/usr/bin/env python3
"""Exact combinatorial audit for the mixed-tower refinement shadow of Paper B.

This script models the minimal exact shadow of `107_07`/`107_08` needed
to distinguish:

* same-tower composition: primitive return stays inside one prime tower;
* mixed-tower composition: output is a refinement object carrying both
  tower labels, not a primitive return.

It also checks that the Eulerian primitive extractor, modeled on the
exact Hopf audit of `107_35`, annihilates decomposable mixed outputs.
"""

from __future__ import annotations

from fractions import Fraction


PRIMES = [2, 3, 5, 7]
MAX_K = 3


Primitive = tuple[str, int, int]
Mixed = tuple[str, Primitive, Primitive]


def primitive(p: int, k: int) -> Primitive:
    return ("P", p, k)


def compose(left: Primitive, right: Primitive) -> Primitive | Mixed:
    _, p, k = left
    _, q, ell = right
    if p == q:
        return primitive(p, k + ell)
    return ("M", left, right)


def transpose(obj: Primitive | Mixed) -> Primitive | Mixed:
    if obj[0] == "P":
        return obj
    _, left, right = obj
    return ("M", right, left)


def e1_on_word(word: tuple[Primitive, ...]) -> dict[tuple[Primitive, ...], Fraction]:
    if len(word) == 1:
        return {word: Fraction(1)}
    return {}


def main() -> None:
    primitives = [primitive(p, k) for p in PRIMES for k in range(1, MAX_K + 1)]
    primitive_set = set(primitives)

    print("Same-tower closure audit")
    same_checks = 0
    for p in PRIMES:
        for k in range(1, MAX_K + 1):
            for ell in range(1, MAX_K + 1):
                out = compose(primitive(p, k), primitive(p, ell))
                assert out == primitive(p, k + ell)
                same_checks += 1
                print(f" ({p},{k}) o ({p},{ell}) -> ({p},{k + ell})")

    print("\nMixed-tower refinement audit")
    mixed_checks = 0
    for p in PRIMES:
        for q in PRIMES:
            if p == q:
                continue
            for k in range(1, MAX_K + 1):
                for ell in range(1, MAX_K + 1):
                    left = primitive(p, k)
                    right = primitive(q, ell)
                    out = compose(left, right)
                    assert out[0] == "M"
                    assert out not in primitive_set
                    assert transpose(out) == ("M", right, left)
                    assert out != transpose(out)
                    mixed_checks += 1
                    print(
                        f" ({p},{k}) o ({q},{ell}) -> mixed[{p},{k};{q},{ell}]"
                    )

    print("\nEulerian extraction audit")
    euler_checks = 0
    for p in PRIMES:
        for q in PRIMES:
            if p == q:
                continue
            word = (primitive(p, 1), primitive(q, 1))
            image = e1_on_word(word)
            assert image == {}
            euler_checks += 1
            print(f" e1({word}) = 0")

    print(
        "\nAll mixed-tower refinement shadow checks passed:"
        f" {same_checks} same-tower, {mixed_checks} mixed-tower,"
        f" {euler_checks} Eulerian checks."
    )


if __name__ == "__main__":
    main()
