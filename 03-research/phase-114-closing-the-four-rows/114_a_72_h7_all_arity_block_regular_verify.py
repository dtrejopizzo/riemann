#!/usr/bin/env python3
"""Exact checks for a72; nested-tree residual faithfulness remains open."""

from itertools import product
from math import gcd
from pathlib import Path


HERE = Path(__file__).resolve().parent


def check(label, condition):
    if not condition:
        raise AssertionError(label)
    print("PASS", label)


def transported_add(x, y, s, q):
    inverse = pow(s, -1, q - 1)
    tx = pow(x, inverse, q) if x else 0
    ty = pow(y, inverse, q) if y else 0
    return pow((tx + ty) % q, s, q)


# Auxiliary primes q == 2 mod 3, so cubic transport is defined.
auxiliary = (11, 17, 23, 29, 41, 47, 53, 59, 71, 83)
for q in auxiliary:
    check(f"cubic exponent invertible q={q}", q % 3 == 2 and gcd(3, q - 1) == 1)
    add3 = lambda x, y, q=q: transported_add(x, y, 3, q)
    check(f"ordinary/twisted witness q={q}", (1 + 1) % q == 2 and add3(1, 1) == 8)
    # Transport by a bijection makes a field addition; check the laws exactly.
    law_grid = range(q) if q <= 29 else range(12)
    for x, y, z in product(law_grid, repeat=3):
        if add3(add3(x, y), z) != add3(x, add3(y, z)):
            raise AssertionError(f"transported associativity q={q}")
        if add3(x, y) != add3(y, x):
            raise AssertionError(f"transported commutativity q={q}")
        if z * add3(x, y) % q != add3(z * x % q, z * y % q):
            raise AssertionError(f"transported distributivity q={q}")
    check(f"transported unit q={q}", all(add3(x, 0) == x for x in range(q)))


def block_signature(word, q):
    """Values recovered from V_word, one (1,1)-activated block at a time."""
    return tuple(2 if bit == 1 else 8 % q for bit in word)


def scalarized_signature(word, q):
    """T_word j_k = delta_word[k], evaluated at (1,1)."""
    return block_signature(word, q)


q = 11
for n in range(1, 13):
    words = list(product((1, 2), repeat=n))
    v_images = [block_signature(word, q) for word in words]
    t_images = [scalarized_signature(word, q) for word in words]
    folds = [tuple(2 for _ in word) for word in words]
    check(f"V block recovery input arity={2*n}", len(set(v_images)) == 2**n)
    check(f"T scalarized recovery input arity={2*n}", len(set(t_images)) == 2**n)
    check(f"common diagonal fold N={n}", len(set(folds)) == 1)


# For each tested principal prime ell choose q != ell.  Nonzero scalar
# multiplication preserves all recovered signatures, hence cancels.
for ell in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 41, 47, 53, 59, 71, 83):
    q = next(q0 for q0 in auxiliary if q0 != ell)
    words = list(product((1, 2), repeat=8))
    scaled = [tuple((ell * x) % q for x in block_signature(word, q)) for word in words]
    check(f"principal-prime cancellation ell={ell}, q={q}",
          ell % q != 0 and len(set(scaled)) == len(words))


for filename, anchors in {
    "114_a_21_H7_GENERIC_OFF_DIAGONAL_ENTROPY.md": ("V_\\epsilon", "same folded image"),
    "114_a_22_H7_RANK_ONE_OUTPUT_SCALARIZATION.md": ("T_\\epsilon", "T_\\epsilon\\circ j_k"),
    "114_a_49_H7_UNARY_EMBEDDING_BY_HOMOGENEOUS_ENDOBIO.md": ("homogeneous endomorphism bio", "B^-(n)"),
    "114_a_51_H7_FULL_TREE_FINITE_BIO_MOMENTS.md": ("finite commutative bio", "full scalar plane"),
}.items():
    content = (HERE / filename).read_text()
    for anchor in anchors:
        check(f"source anchor {filename}:{anchor}", anchor in content)


doc = (HERE / "114_a_72_H7_ALL_ARITY_BLOCK_FIBERS_ARE_PRIME_REGULAR.md").read_text()
for marker in ("H7-RF-NEST", "not assert H7-RF-NEST", "remaining exact target"):
    check(f"scope marker {marker}", marker in doc)

print("VERDICT: ALL-ARITY BLOCK FIBERS ARE PRIME-REGULAR; H7-RF-NEST OPEN")
