#!/usr/bin/env python3
"""Finite tame-sandwich checks; plane tameness/scalar saturation stay open."""

from itertools import product
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
H17 = ROOT / "00-references/papers-nuevos/A/arXiv-1709.05831v1/HARAN_Dec2016_updated_4.tex"


def check(label, condition):
    if not condition:
        raise AssertionError(label)
    print("PASS", label)


source = H17.read_text()
for marker in (
    "we have ``coefficient-map'",
    "if these sets are equal we say $B$ is {\\it tame} in $K$",
    "In most of the examples these are injections",
):
    check(f"source marker {marker}", marker in source)


# A finite abstraction: operation elements have tuples of scalar sandwich
# values.  Tameness is injectivity of this signature.  If p is injective on
# every scalar coordinate, equality after p-scaling recovers the signature.
model_count = 0
for scalar_modulus in range(2, 14):
    for operation_count in range(1, min(7, scalar_modulus ** 2) + 1):
        signatures = [(i % scalar_modulus, (i // scalar_modulus) % scalar_modulus)
                      for i in range(operation_count)]
        if len(set(signatures)) != operation_count:
            continue
        for p in range(1, scalar_modulus):
            scalar_injective = all(
                (p * x) % scalar_modulus != (p * y) % scalar_modulus
                for x in range(scalar_modulus) for y in range(x + 1, scalar_modulus)
            )
            if not scalar_injective:
                continue
            scaled = [tuple((p * x) % scalar_modulus for x in sig)
                      for sig in signatures]
            if len(set(scaled)) != operation_count:
                raise AssertionError((scalar_modulus, operation_count, p))
            model_count += 1
check(f"tame scalar reduction in {model_count} finite separating models", True)


# Necessity of tameness as a hypothesis: identical sandwich signatures do
# not separate two distinct abstract operations even when scalars are regular.
operations = ("F", "G")
signatures = {"F": (1, 2), "G": (1, 2)}
check("non-tame warning has indistinguishable distinct operations",
      operations[0] != operations[1] and signatures["F"] == signatures["G"])


doc = (HERE / "114_a_84_H7_TAMENESS_REDUCES_ALL_ARITIES_TO_SCALARS.md").read_text()
for marker in (
    "H7-TAME-PLANE",
    "H7-SCALAR-SAT",
    "Later resolution (`a104`)",
    "fails H7-TAME-PLANE",
    "row A remain open",
):
    check(f"scope marker {marker}", marker in doc)

print("VERDICT: CONDITIONAL TAME PROMOTION VALID; a104 PROVES PLANE NONTAME")
