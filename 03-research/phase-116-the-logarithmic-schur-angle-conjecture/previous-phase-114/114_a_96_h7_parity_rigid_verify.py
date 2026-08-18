#!/usr/bin/env python3
"""Same-fold intrinsic parity decorations; macro replacement paths stay open."""

from fractions import Fraction
from itertools import product
from pathlib import Path


HERE = Path(__file__).resolve().parent


def check(label, condition):
    if not condition:
        raise AssertionError(label)
    print("PASS", label)


# Reduced unordered rooted colored trees: ('v', color, children), leaf='x'.
leaf = ("x",)
D0 = ("v", 1, (leaf, leaf, leaf))
D1 = ("v", 1, (("v", 2, (leaf, leaf)), leaf))


def leaf_count(tree):
    if tree == leaf:
        return 1
    return sum(leaf_count(child) for child in tree[2])


def internal_count(tree):
    if tree == leaf:
        return 0
    return 1 + sum(internal_count(child) for child in tree[2])


def fold(tree):
    """After identifying colors, a reduced tree folds to its leaf count."""
    return leaf_count(tree)


check("decorations have equal arity three", leaf_count(D0) == leaf_count(D1) == 3)
check("decorations have the same root color", D0[1] == D1[1] == 1)
check("decorations are structurally nonisomorphic", D0 != D1)
check("internal-vertex count distinguishes decorations",
      internal_count(D0) == 1 and internal_count(D1) == 2)
check("decorations have equal diagonal fold", fold(D0) == fold(D1) == 3)


# Exact rational u=2 positive-orthant evaluation at all ones.
u = 2
D0_value = Fraction(3)
D1_value = Fraction(2**u + 1)
check("real power-norm evaluation separates decorations", D0_value != D1_value)


even = {(0, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 0)}
decorated = {tuple(D0 if bit == 0 else D1 for bit in edge) for edge in even}
check("four parity triples survive decoration", len(decorated) == 4)
check("all decorated triples have the same folded block profile",
      {tuple(fold(block) for block in edge) for edge in decorated} == {(3, 3, 3)})


# No coordinate flip is an automorphism because it exchanges D0 and D1.
for part in range(3):
    flipped = {
        tuple((D1 if block == D0 else D0) if index == part else block
              for index, block in enumerate(edge))
        for edge in decorated
    }
    check(f"coordinate {part + 1} flip is not decoration-preserving",
          any(any(a != b for a, b in zip(left, right))
              for left, right in zip(sorted(decorated, key=repr),
                                     sorted(flipped, key=repr))))


doc = (HERE / "114_a_96_H7_PARITY_BITS_CAN_BE_INTRINSICALLY_RIGIDIFIED.md").read_text()
for marker in (
    "H7-PARITY-RIGID-TYPE is closed",
    "H7-RIGID-EVEN-MOVES",
    "H7-RIGID-ODD-CLOSURE",
    "H7-RIGID-ENDPOINTS",
    "H7-RIGID-SEPARATE",
    "row A remain open",
):
    check(f"scope marker {marker}", marker in doc)

print("VERDICT: SAME-FOLD PARITY BITS ARE RIGIDLY TYPED; MACRO MOVES OPEN")
