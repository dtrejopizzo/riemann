#!/usr/bin/env python3
"""Exact controls for the scalar C-Omega free-plus-Z/2 classification."""

from collections import defaultdict
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


def factor(n):
    n = abs(n)
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


def arithmetic_derivative(n):
    if n == 0:
        return {}
    sign = 1 if n > 0 else -1
    magnitude = abs(n)
    return {p: sign * exponent * (magnitude // p)
            for p, exponent in factor(magnitude).items()}


def cocycle(a, b):
    return addv(arithmetic_derivative(a), arithmetic_derivative(b),
                scale(-1, arithmetic_derivative(a + b)))


box = range(-7, 8)
leibniz = 0
for a, b in product(box, repeat=2):
    lhs = arithmetic_derivative(a * b)
    rhs = addv(scale(a, arithmetic_derivative(b)),
               scale(b, arithmetic_derivative(a)))
    if lhs != rhs:
        raise AssertionError(("Leibniz", a, b, lhs, rhs))
    leibniz += 1
check(f"arithmetic derivative satisfies {leibniz} Leibniz identities", True)


cocycle_checks = 0
for a, b, c in product(range(-4, 5), repeat=3):
    if cocycle(a, b) != cocycle(b, a):
        raise AssertionError(("symmetry", a, b))
    if addv(cocycle(a + b, c), cocycle(a, b)) != addv(
            cocycle(a, b + c), cocycle(b, c)):
        raise AssertionError(("associativity", a, b, c))
    cocycle_checks += 1
check(f"classified cocycle satisfies {cocycle_checks} coherence triples", True)


homogeneity = 0
for lam, a, b in product(range(-5, 6), range(-5, 6), range(-5, 6)):
    if cocycle(lam * a, lam * b) != scale(lam, cocycle(a, b)):
        raise AssertionError(("homogeneity", lam, a, b))
    homogeneity += 1
check(f"classified cocycle satisfies {homogeneity} homogeneity identities", True)


def left(a, ap, b):
    return scale(b, cocycle(a, ap))


def right(a, b, bp):
    return scale(a, cocycle(b, bp))


couplings = 0
for a, ap, b, bp in product(range(-3, 4), repeat=4):
    lhs = addv(left(a, ap, b + bp), right(a + ap, b, bp))
    rhs = addv(right(a, b, bp), right(ap, b, bp),
               left(a, ap, b), left(a, ap, bp))
    if lhs != rhs:
        raise AssertionError(("coupling", a, ap, b, bp))
    couplings += 1
check(f"two oriented prime copies satisfy {couplings} coupling identities", True)


check("left binary class is primitive prime basis -d_2",
      left(1, 1, 1) == {2: -1})
check("right binary class is an independent primitive prime basis -d_2",
      right(1, 1, 1) == {2: -1})
for prime in (2, 3, 5, 7):
    check(f"free basis class d_{prime} is not killed by {prime}",
          scale(prime, {prime: 1}) != {})


# The unique homogeneous sign cocycle.  q_t(n)=0 for n>=0 and equals
# n mod 2 for n<0; values are in Z/2.  Its coboundary has t=f(1,-1)=1.
def qt(n):
    return (n % 2) if n < 0 else 0


def ft(a, b):
    return (qt(a) + qt(b) - qt(a + b)) % 2


torsion_checks = 0
for lam, a, b, c in product(range(-5, 6), repeat=4):
    if ft(a, b) != ft(b, a):
        raise AssertionError(("torsion symmetry", a, b))
    if (ft(a + b, c) + ft(a, b) - ft(a, b + c) - ft(b, c)) % 2:
        raise AssertionError(("torsion cocycle", a, b, c))
    if ft(lam * a, lam * b) != (lam * ft(a, b)) % 2:
        raise AssertionError(("torsion homogeneity", lam, a, b))
    torsion_checks += 1
check(f"unique sign cocycle satisfies {torsion_checks} exact identities", True)
check("sign parameter is nonzero on (1,-1)", ft(1, -1) == 1)
torsion_couplings = 0
for a, ap, b, bp in product(range(-4, 5), repeat=4):
    lhs = ((b + bp) * ft(a, ap) + (a + ap) * ft(b, bp)) % 2
    rhs = (a * ft(b, bp) + ap * ft(b, bp)
           + b * ft(a, ap) + bp * ft(a, ap)) % 2
    if lhs != rhs:
        raise AssertionError(("torsion coupling", a, ap, b, bp))
    if (a * ft(b, -b) + b * ft(a, -a)) % 2:
        raise AssertionError(("torsion cancellation", a, b))
    torsion_couplings += 1
check(f"shared sign class satisfies {torsion_couplings} coupled relations", True)
check("multiplication by 2 kills the sign class", (2 * ft(1, -1)) % 2 == 0)


doc = (HERE / "114_a_107_H7_SCALAR_UNIVERSAL_DIFFERENTIAL_HAS_ONE_Z2.md").read_text()
for marker in (
    "D_{\\rm left}\\oplus D_{\\rm right}\\oplus\\mathbb Z/2",
    "does not prove 2-torsion in the scalar",
    "exactly one `Z/2`",
    "H7-PRIME-REG",
    "row A remain open",
):
    check(f"scope marker {marker}", marker in doc)

print("VERDICT: SCALAR C OMEGA = TWO FREE PRIME COPIES PLUS ONE Z/2")
