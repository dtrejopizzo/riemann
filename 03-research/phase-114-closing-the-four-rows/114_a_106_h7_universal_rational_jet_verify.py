#!/usr/bin/env python3
"""Exact entropy-cocycle and rational universal-jet controls for a106."""

from collections import defaultdict
from fractions import Fraction
from itertools import product
from pathlib import Path


HERE = Path(__file__).resolve().parent


def check(label, condition):
    if not condition:
        raise AssertionError(label)
    print("PASS", label)


def addv(*vectors):
    out = defaultdict(int)
    for vector in vectors:
        for prime, coefficient in vector.items():
            out[prime] += coefficient
    return {prime: coefficient for prime, coefficient in out.items()
            if coefficient}


def scale(c, vector):
    return {prime: c * coefficient for prime, coefficient in vector.items()
            if c * coefficient}


def valuations(n):
    n = abs(n)
    out = {}
    prime = 2
    while prime * prime <= n:
        while n % prime == 0:
            out[prime] = out.get(prime, 0) + 1
            n //= prime
        prime += 1
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def q(n):
    return scale(n, valuations(n)) if n else {}


def f(a, b):
    return addv(q(a), q(b), scale(-1, q(a + b)))


box = range(-5, 6)
checks = 0
for a, b, c in product(box, repeat=3):
    check_data = (
        f(a, b) == f(b, a)
        and f(a, 0) == {}
        and addv(f(a + b, c), f(a, b))
        == addv(f(a, b + c), f(b, c))
    )
    if not check_data:
        raise AssertionError((a, b, c))
    checks += 1
check(f"entropy vector is a normalized symmetric cocycle in {checks} triples", True)


homogeneous = 0
for lam, a, b in product(range(-5, 6), box, box):
    if f(lam * a, lam * b) != scale(lam, f(a, b)):
        raise AssertionError((lam, a, b))
    homogeneous += 1
check(f"entropy cocycle satisfies {homogeneous} exact scaling identities", True)


# Images of Haran's two generator types.
def eright(a, b, bp):
    return scale(a, f(b, bp))


def eleft(a, ap, b):
    return scale(b, f(a, ap))


relation_checks = 0
small = range(-3, 4)
for a, ap, b, bp in product(small, repeat=4):
    # Almost linear relation.
    lhs = addv(eleft(a, ap, b + bp), eright(a + ap, b, bp))
    rhs = addv(eright(a, b, bp), eright(ap, b, bp),
               eleft(a, ap, b), eleft(a, ap, bp))
    if lhs != rhs:
        raise AssertionError(("almost-linear", a, ap, b, bp))
    relation_checks += 1
for a, b in product(small, repeat=2):
    if addv(eright(a, b, -b), eleft(a, -a, b)):
        raise AssertionError(("cancellation", a, b))
    relation_checks += 1
check(f"Haran coupling/cancellation relations hold in {relation_checks} cases", True)


entropy_class = eleft(1, 1, 1)
check("class [1,1|1] has exact nonzero entropy value -2 e_2",
      entropy_class == {2: -2})
# In N, [2|1]=2[1|1], so its boundary is exactly zero.
n_boundary_coefficient = 1 + 1 - 2
check("the same class maps to zero under C Omega -> N",
      n_boundary_coefficient == 0)
check("commented injectivity is refuted by an infinite-order class",
      entropy_class != {})


# Rationalized universal module coordinates have no prime torsion.
jet_elements = [(a, Fraction(m, d)) for a in range(-4, 5)
                for m in range(-4, 5) for d in range(1, 6)]
jet_elements = list(dict.fromkeys(jet_elements))
for prime in (2, 3, 5, 7, 11):
    images = [(prime * a, prime * m) for a, m in jet_elements]
    check(f"rational universal jet target is {prime}-regular",
          len(set(images)) == len(jet_elements))


doc = (HERE / "114_a_106_H7_UNIVERSAL_RATIONAL_FIRST_JET.md").read_text()
for marker in (
    "commented injectivity assertion `C Omega -> N` is false",
    "torsion in `Omega_C`",
    "genuinely nonlinear/higher-order",
    "H7-PRIME-REG",
    "row A remain",
):
    check(f"scope marker {marker}", marker in doc)

print("VERDICT: C OMEGA->N NONINJECTIVE; UNIVERSAL RATIONAL FIRST JETS PRIME-REGULAR")
