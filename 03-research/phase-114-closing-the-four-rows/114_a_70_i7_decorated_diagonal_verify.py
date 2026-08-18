#!/usr/bin/env python3
"""Exact finite checks for the Picard-decorated diagonal kernel monoid."""

from collections import Counter
from math import gcd, log


def check(label, condition):
    if not condition:
        raise AssertionError(label)
    print("PASS", label)


def valuations(n):
    out = Counter()
    p = 2
    x = n
    while p * p <= x:
        while x % p == 0:
            out[p] += 1
            x //= p
        p += 1
    if x > 1:
        out[x] += 1
    return out


def compose(label_a, label_b):
    out = Counter(label_a)
    out.update(label_b)
    return out


def contact(label):
    support = tuple(sorted(label))
    if not support:
        return None  # Z, the tensor unit
    return support[0] if len(support) == 1 else 1  # Z/p or the zero module Z/1


def tensor_contact(a, b):
    if a is None:
        return b
    if b is None:
        return a
    return gcd(a, b)


for a in range(1, 80):
    va = valuations(a)
    for b in range(1, 80):
        vb = valuations(b)
        check(f"decorated composition a={a}, b={b}",
              compose(va, vb) == valuations(a * b))
        for c in range(1, 18):
            vc = valuations(c)
            check(f"associativity a={a}, b={b}, c={c}",
                  compose(compose(va, vb), vc) == compose(va, compose(vb, vc)))

        left_contact = contact(compose(va, vb))
        ca, cb = contact(va), contact(vb)
        check(f"contact monoidal law a={a}, b={b}",
              left_contact == tensor_contact(ca, cb))

for n in range(2, 500):
    vn = valuations(n)
    c = contact(vn)
    size = c
    expected = log(next(iter(vn))) if len(vn) == 1 else 0.0
    check(f"Lambda mass n={n}", abs(log(size) - expected) < 1e-12)

for p in (2, 3, 5, 7):
    check(f"contact forgets prime exponent p={p}",
          contact(valuations(p)) == contact(valuations(p**4)))
    check(f"decorated label retains prime exponent p={p}",
          valuations(p) != valuations(p**4))

print("VERDICT: FAITHFUL DECORATED DYNAMIC MONOID AND CONTACT SHADOW PASS")
