#!/usr/bin/env python3
"""Exhaustive finite check of the p-convex one-boundary criterion."""

from itertools import combinations
from pathlib import Path


HERE = Path(__file__).resolve().parent


def component_labels(vertices, edges):
    vertices = set(vertices)
    adjacency = {v: set() for v in vertices}
    for u, v in edges:
        if u in vertices and v in vertices:
            adjacency[u].add(v)
            adjacency[v].add(u)
    labels = {}
    index = 0
    for root in sorted(vertices):
        if root in labels:
            continue
        stack = [root]
        while stack:
            v = stack.pop()
            if v in labels:
                continue
            labels[v] = index
            stack.extend(adjacency[v] - labels.keys())
        index += 1
    return labels


def check(label, condition):
    if not condition:
        raise AssertionError(label)
    print("PASS", label)


models = 0
witnesses = 0
for n in range(6):
    possible = list(combinations(range(n), 2))
    for edge_mask in range(1 << len(possible)):
        edges = [e for i, e in enumerate(possible) if edge_mask >> i & 1]
        full = component_labels(range(n), edges)
        for subset_mask in range(1 << n):
            inside = {v for v in range(n) if subset_mask >> v & 1}
            outside = set(range(n)) - inside
            in_labels = component_labels(inside, edges)
            out_labels = component_labels(outside, edges)
            convex = all(full[u] != full[v] or in_labels[u] == in_labels[v]
                         for u in inside for v in inside)
            boundaries = {q: set() for q in set(out_labels.values())}
            for u, v in edges:
                if u in outside and v in inside:
                    boundaries[out_labels[u]].add(in_labels[v])
                if v in outside and u in inside:
                    boundaries[out_labels[v]].add(in_labels[u])
            one_boundary = all(len(bs) <= 1 for bs in boundaries.values())
            if convex != one_boundary:
                raise AssertionError((n, edges, inside, boundaries))
            if not convex:
                witnesses += 1
                if not any(len(bs) >= 2 for bs in boundaries.values()):
                    raise AssertionError((n, edges, inside, "no witness"))
            models += 1
check(f"one-boundary criterion in {models} graph/subset models", True)
check(f"every one of {witnesses} failures has a two-gate outside component", True)


doc = (HERE / "114_a_86_H7_P_CONVEXITY_BOUNDARY_ATTACHMENT_CRITERION.md").read_text()
for marker in (
    "H7-p-ONE-BOUNDARY",
    "equivalent to H7-p-CONVEX",
    "H7-p-DIVPATH remains",
    "row A remains open",
):
    check(f"scope marker {marker}", marker in doc)

print("VERDICT: p-CONVEX IFF EVERY NONDIVISIBLE COMPONENT HAS ONE DIVISIBLE BOUNDARY")
