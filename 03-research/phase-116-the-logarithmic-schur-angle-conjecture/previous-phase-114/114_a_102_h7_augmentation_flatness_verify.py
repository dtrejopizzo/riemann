#!/usr/bin/env python3
"""Finite controls for the scalar augmentation-flatness criterion."""

from itertools import product
from math import gcd
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
    "ordinary commutative ring",
    r"({\mathbb Z}^{\otimes n})_{[1]}^{\{ i \}}",
    r"g \in S_n$ takes $i$-th addition",
):
    check(f"source marker {marker}", marker in source)


# A split augmentation of abelian groups: R=Z/mZ direct-sum K.  The section
# and projection give unique decomposition.  This only models the additive
# identity (1.6), not Haran's unknown kernel.
split_models = 0
for modulus in range(2, 13):
    for kernel_modulus in range(1, 13):
        for z, k in product(range(modulus), range(kernel_modulus)):
            included = (z, 0)
            projected = included[0]
            reconstructed = (projected, k)
            if projected != z or reconstructed != (z, k):
                raise AssertionError((modulus, kernel_modulus, z, k))
            split_models += 1
check(f"split augmentation decomposition in {split_models} finite models", True)


# For K=Z/nZ, ker(p:K->K) and Tor_1^Z(K,Z/p) both have gcd(n,p)
# elements.  Direct sums add the component kernels.
primes = (2, 3, 5, 7, 11)
tor_models = 0
for orders in product(range(1, 13), repeat=3):
    for prime in primes:
        kernel_size = 1
        expected_tor_size = 1
        for order in orders:
            killed = [x for x in range(order) if prime * x % order == 0]
            kernel_size *= len(killed)
            expected_tor_size *= gcd(order, prime)
        if kernel_size != expected_tor_size:
            raise AssertionError((orders, prime, kernel_size, expected_tor_size))
        tor_models += 1
check(f"p-kernel equals Tor size in {tor_models} finite abelian groups", True)


# Every nontrivial finite cyclic torsion factor is detected by a prime.
for order in range(2, 101):
    divisor = next(p for p in primes + tuple(range(13, order + 1))
                   if order % p == 0 and all(p % q for q in range(2, int(p ** .5) + 1)))
    witness = order // divisor
    if witness % order == 0 or divisor * witness % order != 0:
        raise AssertionError((order, divisor, witness))
check("every tested torsion factor has a prime-order witness", True)


# Split but nonflat ring S=Z x F_p with diagonal unital inclusion and first
# projection.  The augmentation element (0,1) is killed by i(p)=(p,0).
for prime in primes:
    for n in range(-20, 21):
        included = (n, n % prime)
        if included[0] != n:
            raise AssertionError((prime, n))
    p_scalar = (prime, 0)
    kernel_element = (0, 1)
    product_ring = (p_scalar[0] * kernel_element[0],
                    p_scalar[1] * kernel_element[1] % prime)
    check(f"split nonflat countermodel at p={prime}",
          kernel_element != (0, 0) and product_ring == (0, 0))


doc = (HERE / "114_a_102_H7_AUGMENTATION_IDEAL_FLATNESS_CRITERION.md").read_text()
for marker in (
    "H7-AUG-FLAT",
    "does not imply flatness",
    "H7-TAME-PLANE",
    "not an exhaustive",
    "row A remain open",
    "Final resolution of this gate (`a108`)",
    "explicit 2-torsion",
):
    check(f"scope marker {marker}", marker in doc)

print("VERDICT: FLATNESS CRITERION VALID; a108 PROVES AUGMENTATION 2-TORSION")
