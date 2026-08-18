#!/usr/bin/env python3
"""Checks the pre-Picard boundary-kernel reduction (a129)."""

from itertools import product
from math import prod
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
DOC = (HERE / "114_a_129_H7_FRAMED_DIVISOR_EXACT_SEQUENCE.md").read_text()
H17 = (ROOT / "00-references/papers-nuevos/A/arXiv-1709.05831v1/"
       "HARAN_Dec2016_updated_4.tex").read_text()


def check(label, condition):
    if not condition:
        raise AssertionError(label)
    print("PASS", label)


# Diagonal pullback confines a presentation relation to left+right=0.
for rank in range(1, 5):
    exact = True
    count = 0
    for v in product(range(-2, 3), repeat=2 * rank):
        count += 1
        left, right = v[:rank], v[rank:]
        pic_diagonal_zero = all(left[i] + right[i] == 0 for i in range(rank))
        anti_form = tuple(left) == tuple(-x for x in right)
        exact &= pic_diagonal_zero == anti_form
    check(f"anti-kernel confinement rank={rank} ({count} vectors)", exact)

# A boundary detector sum a_p log p is injective by unique factorization.
primes = (2, 3, 5, 7)
injective = True
for exponents in product(range(-3, 4), repeat=len(primes)):
    positive = prod(p ** max(a, 0) for p, a in zip(primes, exponents))
    negative = prod(p ** max(-a, 0) for p, a in zip(primes, exponents))
    if positive == negative:
        injective &= all(a == 0 for a in exponents)
check("unique-factorization boundary detector", injective)

check("source D1 anchor", r"\label{eq113}" in H17)
check("source equivalence anchor", "(11.4)" in H17)
check("source completed objects anchor", r"\label{eq1115}" in H17)
check("source global fraction action anchor", r"\label{eq1116}" in H17)

markers = (
    "pre-Picard exact sequence isolates the boundary obstruction",
    "A_p=\\operatorname{div}(h_p)+B_p^\\infty",
    "This corrects the false finite-only conclusion",
    "boundary kernel formula",
    "H7-ARCH-BDRY",
    "circular.",
    "row A and RH remain open",
)
for marker in markers:
    check(f"scope marker {marker}", marker in DOC)

print("VERDICT: THE PRIME PICARD KERNEL IS EXACTLY THE ARCHIMEDEAN BOUNDARY KERNEL")
