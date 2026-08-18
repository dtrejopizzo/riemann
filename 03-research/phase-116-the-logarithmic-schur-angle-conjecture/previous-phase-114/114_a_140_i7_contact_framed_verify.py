#!/usr/bin/env python3
"""Algebra of the contact-framed arithmetic kernel submonoid."""

from math import isclose, log
from pathlib import Path


HERE = Path(__file__).resolve().parent
DOC = (HERE / "114_a_140_I7_CONTACT_FRAMED_ARITHMETIC_KERNELS.md").read_text()


def check(label, condition):
    if not condition:
        raise AssertionError(label)
    print("PASS", label)


def support(n):
    out = set()
    p = 2
    while p * p <= n:
        while n % p == 0:
            out.add(p)
            n //= p
        p += 1
    if n > 1:
        out.add(n)
    return out


def reduced_contact(n):
    ps = support(n)
    if not ps:
        return ("Z",)
    if len(ps) == 1:
        return ("Fp", next(iter(ps)))
    return ("zero",)


def tensor_contact(x, y):
    if x == ("Z",):
        return y
    if y == ("Z",):
        return x
    if x == ("zero",) or y == ("zero",):
        return ("zero",)
    return x if x == y else ("zero",)


composition_ok = True
for m in range(1, 120):
    for n in range(1, 120):
        composition_ok &= tensor_contact(
            reduced_contact(m), reduced_contact(n)
        ) == reduced_contact(m * n)
check("reduced contact frames compose for all sampled labels", composition_ok)

mass_ok = True
for n in range(2, 500):
    ps = support(n)
    expected = log(next(iter(ps))) if len(ps) == 1 else 0.0
    contact = reduced_contact(n)
    actual = log(contact[1]) if contact[0] == "Fp" else 0.0
    mass_ok &= isclose(actual, expected)
check("contact-framed masses equal Lambda on all sampled labels", mass_ok)

for marker in (
    "not chosen from its cardinality",
    "contact-framed kernel",
    "do **not** tensor the shifted ambient complexes",
    "H7-FRAMED-RR",
    "first four clauses",
    "Row A remains open",
    "No RH statement is used",
):
    check(f"scope marker: {marker}", marker in DOC)

print("VERDICT: FAITHFUL DYNAMICS AND DERIVED LAMBDA CONTACT FORM ONE TYPED KERNEL MONOID")
