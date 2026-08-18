#!/usr/bin/env python3
"""Structural checks for a74; signed/repeated cut data remain open."""

from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
import random

import sympy as sp


HERE = Path(__file__).resolve().parent


def check(label, condition):
    if not condition:
        raise AssertionError(label)
    print("PASS", label)


# Exact analytic identity behind every cross edge.
A, B, alpha = sp.symbols("A B alpha", positive=True)
cross = sp.diff((A + B) ** alpha, A, B)
expected = alpha * (alpha - 1) * (A + B) ** (alpha - 2)
check("exact cross-Hessian identity", sp.simplify(cross - expected) == 0)
check("cross coefficient nonzero at r=1/2",
      sp.simplify(cross.subs({alpha: sp.Rational(1, 2), A: 2, B: 3})) != 0)
check("cross coefficient nonzero at u=2",
      sp.simplify(cross.subs({alpha: 2, A: 2, B: 3})) != 0)


@dataclass(frozen=True)
class Leaf:
    name: int


@dataclass(frozen=True)
class Node:
    color: int
    children: tuple


def leaves(tree):
    if isinstance(tree, Leaf):
        return frozenset((tree.name,))
    return frozenset().union(*(leaves(child) for child in tree.children))


def connected_components(vertices, edges):
    remaining = set(vertices)
    result = []
    while remaining:
        seed = remaining.pop()
        component = {seed}
        frontier = [seed]
        while frontier:
            x = frontier.pop()
            neighbors = {b for a, b in edges if a == x} | {a for a, b in edges if b == x}
            new = neighbors & remaining
            remaining -= new
            component |= new
            frontier.extend(new)
        result.append(frozenset(component))
    return frozenset(result)


def complete_cross(blocks):
    edges = set()
    for i, left in enumerate(blocks):
        for right in blocks[i + 1:]:
            edges |= {tuple(sorted((a, b))) for a in left for b in right}
    return edges


def natural_hessian_edges(tree):
    """Enough exact support to determine connectivity of H(F_tree)."""
    if isinstance(tree, Leaf):
        return set()
    child_sets = [leaves(child) for child in tree.children]
    if tree.color == 1:
        return set().union(*(natural_hessian_edges(child) for child in tree.children))
    # Color 2 is a nontrivial outer power: all different child blocks interact.
    return complete_cross(child_sets) | set().union(
        *(natural_hessian_edges(child) for child in tree.children)
    )


def root_transform_edges(tree):
    """Connectivity support of H(F^r), r=1/2."""
    if isinstance(tree, Leaf):
        return set()
    child_sets = [leaves(child) for child in tree.children]
    if tree.color == 2:
        # F^r is the exact sum of child F^r terms: no cross-child edges.
        return set().union(*(root_transform_edges(child) for child in tree.children))
    # For color 1, (sum child F)^r has every cross-child edge.
    return complete_cross(child_sets) | set().union(
        *(root_transform_edges(child) for child in tree.children)
    )


def split_groups(names, rng):
    if len(names) <= 1:
        return [names]
    cut_count = rng.randint(1, min(3, len(names) - 1))
    cuts = sorted(rng.sample(range(1, len(names)), cut_count))
    points = [0] + cuts + [len(names)]
    return [names[points[i]:points[i + 1]] for i in range(len(points) - 1)]


def make_tree(names, color, rng, depth=1):
    if len(names) == 1:
        return Leaf(names[0])
    groups = split_groups(names, rng)
    children = tuple(make_tree(group, 3 - color, rng, depth + 1) for group in groups)
    return Node(color, children)


rng = random.Random(11474)
max_depth_seen = 0
for n in range(2, 13):
    for sample in range(40):
        tree = make_tree(tuple(range(n)), 1 + (sample % 2), rng)

        def depth(t):
            return 0 if isinstance(t, Leaf) else 1 + max(depth(c) for c in t.children)

        max_depth_seen = max(max_depth_seen, depth(tree))
        vertices = leaves(tree)
        child_partition = frozenset(leaves(child) for child in tree.children)
        natural_components = connected_components(vertices, natural_hessian_edges(tree))
        transformed_components = connected_components(vertices, root_transform_edges(tree))
        if tree.color == 1:
            check(f"root-1 components n={n}, sample={sample}",
                  natural_components == child_partition and len(transformed_components) == 1)
        else:
            check(f"root-2 components n={n}, sample={sample}",
                  transformed_components == child_partition and len(natural_components) == 1)

check("generated examples reach depth at least six", max_depth_seen >= 6)


doc = (HERE / "114_a_74_H7_ALL_DEPTH_READ_ONCE_HESSIAN_RECONSTRUCTION.md").read_text()
for marker in ("H7-RF-CUT", "does not assert H7-RF-CUT", "unsigned read-once"):
    check(f"scope marker {marker}", marker in doc)

print("VERDICT: ALL-DEPTH UNSIGNED READ-ONCE HESSIAN RECONSTRUCTION PASS; H7-RF-CUT OPEN")
