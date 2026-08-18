#!/usr/bin/env python3
"""Scalar-invisible labelled partitions are separated by full-bio probes."""

from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent


def check(label, condition):
    if not condition:
        raise AssertionError(label)
    print("PASS", label)


P0 = frozenset((frozenset((1, 2)), frozenset((3, 4))))
P1 = frozenset((frozenset((1, 3)), frozenset((2, 4))))
check("labelled pair partitions are distinct", P0 != P1)
check("both partitions cover the same fixed inputs",
      frozenset().union(*P0) == frozenset().union(*P1) == frozenset(range(1, 5)))
check("both have the same block-size multiset",
      sorted(map(len, P0)) == sorted(map(len, P1)) == [2, 2])


def delta2_pair(values, u):
    # Only Boolean/all-one exact evaluations are needed: a pair with k ones
    # has value k^u in the signed-power model.
    return Fraction(sum(values) ** u)


def evaluate(partition, vector, u):
    return sum(delta2_pair([vector[index - 1] for index in block], u)
               for block in partition)


for u in range(1, 8):
    all_ones = (1, 1, 1, 1)
    expected = Fraction(2 ** (u + 1))
    check(f"scalar invisibility u={u}",
          evaluate(P0, all_ones, u) == evaluate(P1, all_ones, u) == expected)

    pair_probe = (1, 1, 0, 0)
    left = evaluate(P0, pair_probe, u)
    right = evaluate(P1, pair_probe, u)
    check(f"pair-probe values u={u}", left == 2**u and right == 2)
    if u > 1:
        check(f"full-bio separation u={u}", left != right)


# Abstract extraction: equality of product contexts would imply equality of
# every extracted coordinate signature, contradicted by one differing bit.
signatures = {0: (Fraction(2**u) for u in range(2, 7)),
              1: (Fraction(2) for _ in range(2, 7))}
signatures = {key: tuple(value) for key, value in signatures.items()}
check("bit signatures are extractably distinct", signatures[0] != signatures[1])
for left_bits, right_bits in (((0, 0, 0), (0, 1, 1)),
                              ((0, 0, 0), (1, 0, 1)),
                              ((0, 0, 0), (1, 1, 0))):
    changed = [i for i in range(3) if left_bits[i] != right_bits[i]]
    check(f"even move {left_bits}->{right_bits} has extractable changed part",
          bool(changed)
          and any(signatures[left_bits[i]] != signatures[right_bits[i]] for i in changed))


doc = (HERE / "114_a_98_H7_SCALAR_INVISIBLE_RIGID_BITS_ARE_FULL_BIO_VISIBLE.md").read_text()
for marker in (
    "H7-NONEXTRACTABLE-RIGID",
    "closed negatively",
    "Merely hiding",
    "row A remain open",
):
    check(f"scope marker {marker}", marker in doc)

print("VERDICT: SCALAR-INVISIBLE READ-ONCE BITS ARE FULL-BIO VISIBLE; ENTANGLEMENT OPEN")
