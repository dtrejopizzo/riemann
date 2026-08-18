#!/usr/bin/env python3
"""Source and exact finite checks for H7-CART-ACT-DELTA."""

from math import gcd, log
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
H17 = ROOT / "00-references/papers-nuevos/A/arXiv-1709.05831v1/HARAN_Dec2016_updated_4.tex"
text = H17.read_text()


def check(label, condition):
    if not condition:
        raise AssertionError(label)
    print("PASS", label)


check("generalized-ring categories are cocomplete and have pushouts",
      "complete and co-complete" in text and "have push out diagrams" in text)
check("unary scalars form a central commutative monoid",
      "commutative, associative, unital monoid" in text
      and "acts centrally on all the sets" in text)
check("equivalence-ideal quotients exist",
      "We can then form the quotient" in text and r"\label{eq81}" in text)
check("ideals generate equivalence ideals", r"\label{eq83}" in text)
check("scheme fiber products use generalized tensor pushouts",
      r"\label{eq812}" in text and r"\underset{{\mathcal O}_Z({\mathcal W})}{\otimes}" in text)
check("Section 11 regularity is all-arity cancellation",
      r"\label{eq111}" in text and r"\Rightarrow a=a'" in text)


# A regular principal act: multiplication by a nonzero integer is injective,
# and every element in its image has a unique preimage.
for s in range(1, 9):
    image = {s * a: a for a in range(-40, 41)}
    check(f"principal act unique preimage s={s}", len(image) == 81)


primes = (2, 3, 5, 7, 11)
for p in primes:
    for k in range(0, 6):
        # p^k Z / p^(k+1) Z is represented by r*p^k, 0<=r<p.
        reps = {(r * p**k) % (p ** (k + 1)) for r in range(p)}
        check(f"normal layer cardinality p={p}, k={k}", len(reps) == p)

    # Under the distinguished p^k generators, graded multiplication is just
    # multiplication in F_p and hence induces F_p tensor F_p -> F_p.
    for a in range(0, 4):
        for b in range(0, 4):
            for x in range(p):
                for y in range(p):
                    lhs = (x * p**a) * (y * p**b)
                    rhs = ((x * y) % p) * p ** (a + b)
                    check(f"graded product p={p}, a={a}, b={b}, x={x}, y={y}",
                          (lhs - rhs) % (p ** (a + b + 1)) == 0)

for p in primes:
    for q in primes:
        if p != q:
            check(f"mixed-prime tensor vanishes p={p}, q={q}", gcd(p, q) == 1)


def von_mangoldt_mass(n):
    found = []
    for p in primes:
        x = n
        k = 0
        while x % p == 0:
            x //= p
            k += 1
        if k:
            found.append((p, k, x))
    if len(found) == 1 and found[0][2] == 1:
        return log(found[0][0])
    return 0.0


for n in range(1, 200):
    factors = []
    x = n
    for p in primes:
        if x % p == 0:
            factors.append(p)
            while x % p == 0:
                x //= p
    expected = log(factors[0]) if x == 1 and len(factors) == 1 else 0.0
    check(f"Lambda contact mass n={n}", abs(von_mangoldt_mass(n) - expected) < 1e-12)

doc = (HERE / "114_a_67_H7_TYPED_PRINCIPAL_CARTIER_ACT_AND_DIAGONAL_SHADOW.md").read_text()
check("a108 kills regular principal-act hypothesis at p=2",
      "hypothesis fails for `p=2`" in doc)
print("VERDICT: QUOTIENT/CONTACT PASS; REGULAR ACT CONDITION FAILS AT p=2")
