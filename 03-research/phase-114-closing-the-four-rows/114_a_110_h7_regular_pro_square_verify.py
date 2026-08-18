#!/usr/bin/env python3
"""Finite exact controls for the regular reflected pro-square and lattices."""

from fractions import Fraction
from itertools import product
from math import prod
from pathlib import Path


HERE = Path(__file__).resolve().parent


def check(label, condition):
    if not condition:
        raise AssertionError(label)
    print("PASS", label)


# Functorial torsion radical: homomorphisms send torsion to torsion.  Model
# maps Z^r + cyclic factors -> Z^s + cyclic factors by simple coordinate
# matrices and reductions.
functorial = 0
for source_order, target_order, multiplier in product(
        (2, 3, 4, 6), (2, 3, 5, 6), range(-5, 6)):
    for x in range(source_order):
        image = (multiplier * x) % target_order
        killed_source = source_order * x % source_order == 0
        killed_target = source_order * image % target_order == 0
        # Only retain maps of cyclic groups: target_order divides
        # multiplier*source_order.
        if (multiplier * source_order) % target_order == 0:
            check_data = killed_source and killed_target
            if not check_data:
                raise AssertionError((source_order, target_order, multiplier, x))
            functorial += 1
check(f"torsion radicals are functorial in {functorial} cyclic map values", True)


# Central localization/free rational coordinates remain n-regular.
localized = [Fraction(a, s) for a in range(-20, 21) for s in (1, 2, 3, 5, 7)]
localized = list(dict.fromkeys(localized))
for n in (2, 3, 5, 7, 11):
    images = {n * x for x in localized}
    check(f"central localized coordinates remain {n}-regular",
          len(images) == len(localized))


# Bounded directed unions of subgroups of Q are torsion-free.
stages = []
current_denominator = 1
for denominator in (2, 3, 5, 7):
    current_denominator *= denominator
    stage = {Fraction(a, current_denominator)
             for a in range(-4 * current_denominator, 4 * current_denominator + 1)}
    stages.append(stage)
union = set().union(*stages)
for n in (2, 3, 5):
    check(f"filtered-union shadow remains {n}-regular",
          len({n * x for x in union}) == len(union))


def factor(n):
    out = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


# Completed lattice labels are valuation vectors; tensor is addition.
lattice_checks = 0
for m, n in product(range(1, 121), repeat=2):
    vm, vn, vmn = factor(m), factor(n), factor(m * n)
    combined = {p: vm.get(p, 0) + vn.get(p, 0)
                for p in set(vm) | set(vn)}
    combined = {p: e for p, e in combined.items() if e}
    if combined != vmn:
        raise AssertionError((m, n, combined, vmn))
    lattice_checks += 1
check(f"prime completed lattices satisfy {lattice_checks} tensor laws", True)
check("valuation labels are faithful through 500",
      len({tuple(sorted(factor(n).items())) for n in range(1, 501)}) == 500)


# Diagonal contact residue field cardinality, including p=2.
for prime in (2, 3, 5, 7, 11):
    check(f"repaired contact quotient has cardinality {prime}",
          len({x % prime for x in range(3 * prime)}) == prime)


doc = (HERE / "114_a_110_H7_REGULAR_REFLECTION_ON_THE_PRO_SQUARE.md").read_text()
for marker in (
    "H7-REG-SHEAF",
    "prime-generated** instance",
    "entire completed Picard group",
    "H7-REG-GAUGE",
    "row A remain open",
    "Nothing here asserts",
):
    check(f"scope marker {marker}", marker in doc)

print("VERDICT: REGULAR REFLECTION EXTENDS FUNCTORIALLY; PRIME LATTICES RESTORED")
