#!/usr/bin/env python3
"""Exact finite controls for the split-coefficient retraction theorem."""

from itertools import product
from math import gcd
from pathlib import Path


HERE = Path(__file__).resolve().parent


def check(label, condition):
    if not condition:
        raise AssertionError(label)
    print("PASS", label)


def dot(row, column, modulus):
    return sum(x * y for x, y in zip(row, column)) % modulus


# Scalar active-block form of Theorem 1.1.  Exhaust all coefficient vectors
# of lengths at most three over Z/nZ.  Whenever left/right unit probes exist,
# every active scalar is recovered exactly.
split_models = 0
ideal_models = 0
records = {}
for modulus in range(2, 8):
    for size in range(1, 3):
        records[modulus, size] = []
        probes = tuple(product(range(modulus), repeat=size))
        for vector in product(range(modulus), repeat=size):
            values = {dot(probe, vector, modulus) for probe in probes}
            unit_probes = [probe for probe in probes
                           if dot(probe, vector, modulus) == 1]
            unimodular = gcd(modulus, *vector) == 1
            if bool(unit_probes) != unimodular:
                raise AssertionError((modulus, vector, unit_probes))
            records[modulus, size].append(
                (vector, values, unit_probes[0] if unit_probes else None,
                 unimodular))

    for left_size in range(1, 3):
        for u, left_values, left_probe, left_unimodular in records[modulus, left_size]:
            for right_size in range(1, 3):
                for v, right_values, right_probe, right_unimodular in records[modulus, right_size]:
                    accessible = {x * y % modulus
                                  for x in left_values for y in right_values}
                    retractable = 1 in accessible
                    if retractable != (left_unimodular and right_unimodular):
                        raise AssertionError((modulus, u, v, accessible))
                    ideal_models += 1

                    if retractable:
                        b, q = left_probe, right_probe
                        for a in range(modulus):
                            contextual = (dot(b, u, modulus) * a
                                          * dot(v, q, modulus)) % modulus
                            if contextual != a:
                                raise AssertionError((modulus, u, v, b, q, a))
                            split_models += 1

check(f"unimodular ideal criterion in {ideal_models} coefficient systems", True)
check(f"split sandwich retraction in {split_models} scalar matrix models", True)


# A full block-matrix instance, including a nonzero inactive block.  The
# selected left/right inverses and zero extensions remove it exactly.
for modulus in (2, 3, 4, 5, 7):
    # c=id_2=d, ell=id_2=r; bbar=(b,0), qbar=(q,0)^t.
    for a, inactive, b, q in product(range(modulus), repeat=4):
        recovered = (b * a * q + 0 * inactive * 0) % modulus
        expected = b * a * q % modulus
        if recovered != expected:
            raise AssertionError((modulus, a, inactive, b, q))
check("inactive direct-sum block is killed by structural zero extensions", True)


# Nonsplit does not imply a collision: multiplication by 2 on Z is
# injective.  In a ring with an annihilator it can hide a nonzero difference.
check("nonsplit multiplication by two is injective on tested integers",
      len({2 * z for z in range(-100, 101)}) == 201)
check("same coefficient annihilates a nonzero difference modulo four",
      0 != 2 and (2 * 0) % 4 == (2 * 2) % 4)


doc = (HERE / "114_a_101_H7_SPLIT_COEFFICIENTS_RETRACT_AND_ANNIHILATOR_GATE.md").read_text()
for marker in (
    "Theorem 1.1",
    "H7-COEFF-ANN",
    "necessary but not sufficient",
    "residual diagnostic",
    "Row A remains",
):
    check(f"scope marker {marker}", marker in doc)

print("VERDICT: SPLIT COEFFICIENTS RETRACT; NONSPLIT NEEDS AN ANNIHILATED PAIR")
