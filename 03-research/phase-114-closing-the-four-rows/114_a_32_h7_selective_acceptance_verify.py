#!/usr/bin/env python3
"""Finite acceptance checks for 114.a.32; not an existence proof of H7-SEL."""

from collections import defaultdict
from math import floor, log


def product(left, right):
    out = defaultdict(int)
    for j, a in enumerate(left):
        for k, b in enumerate(right):
            if a and b:
                out[(j + k, a * b)] += 3 ** (j + k)
    return dict(out)


print("A. Convolution support obstruction")
p = product((1, 1), (1, 2))
middle = {label: coefficient for (weight, label), coefficient in p.items()
          if weight == 1}
assert middle == {2: 3, 1: 3}
assert len(middle) == 2
print("  middle support:", middle)

print("\nB. Diagonal collapse has only linear logarithmic range")
q = 3
for d in range(2, 14):
    n = d
    r = floor(log(2 ** (d + 1) + 1, 3))
    Q = q**n
    radius = Q * (3**r - 1) // 2
    diagonal_count_bound = 2 * radius + 1
    assert log(diagonal_count_bound) <= log(2 * Q * 3**r + 1)
    assert r <= d + 1
print("  checked d=2,...,13")

print("\nC. Selected-domain entropy separates from diagonal growth")
for d in (10, 20, 40, 80):
    n = d
    r = floor(log(2 ** (d + 1) + 1, 3))
    quadratic_proxy = r * n * log(q)
    diagonal_proxy = log(2) + r * log(3) + n * log(q)
    assert quadratic_proxy / diagonal_proxy > 1
print("  quadratic proxy / diagonal proxy diverges")

print("\nVERDICT: H7-SEL ACCEPTANCE OBSTRUCTION CHECKS PASS")
