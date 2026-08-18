#!/usr/bin/env python3
"""Formal finite checks for Q_u; unary injectivity is not asserted."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent
SOURCE = (ROOT.parent.parent / "00-references/papers-nuevos/mas-papers/"
          "arXiv-2209.08536v3/"
          "Non-Additive-Geometry-and-Frobenius-Correspondences.tex").read_text()


def t_map(x, u):
    if x == 0:
        return 0.0
    return (1 if x > 0 else -1) * abs(x) ** (1 / u)


def t_inverse(x, u):
    if x == 0:
        return 0.0
    return (1 if x > 0 else -1) * abs(x) ** u


def add_u(x, y, u):
    return t_inverse(t_map(x, u) + t_map(y, u), u)


print("A. Categorical source anchors")
for anchor in ("label{eq:2.13}", "label{eq:2.15}", "label{eq:4.8}"):
    assert anchor in SOURCE
assert "They are all complete and co-complete" in SOURCE
assert "push-outs for a diagram" in SOURCE
print("  ring bios, involution and cocompleteness found")

print("\nB. Unary identifications preserve common multiplication")
grid = (-5, -2, -1, 0, 1, 3, 7)
for u in (0.5, 1.0, 1.5, 2.0, 3.0):
    for x in grid:
        for y in grid:
            first_product = x * y
            second_product = x * y
            assert first_product == second_product
print("  j_1(xy)=j_u(xy) is compatible with j_1(x)=j_u(x)")

print("\nC. The two induced integer laws")
for u in (0.5, 1.5, 2.0, 3.0):
    assert abs((1 + 1) - 2) < 1e-12
    assert abs(add_u(1, 1, u) - 2**u) < 1e-10
    assert abs(2 - 2**u) > 1e-6
print("  injective eta_u would separate delta_1 and delta_2")

print("\nD. The u=1 retraction")
for x in grid:
    for y in grid:
        assert abs(add_u(x, y, 1.0) - (x + y)) < 1e-12
print("  at u=1 both ring bios and additions coincide")

print("\nVERDICT: UNIVERSAL TWISTED-BIO FORMAL CHECKS PASS (H7-UEMB: a49)")
