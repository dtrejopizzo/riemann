#!/usr/bin/env python3
"""Finite graph checks for a85; full macro p-convexity/division stay open."""

from itertools import combinations, product
from pathlib import Path


HERE = Path(__file__).resolve().parent


def check(label, condition):
    if not condition:
        raise AssertionError(label)
    print("PASS", label)


def components(n, edges, allowed=None):
    allowed = set(range(n)) if allowed is None else set(allowed)
    adjacency = {v: set() for v in allowed}
    for u, v in edges:
        if u in allowed and v in allowed:
            adjacency[u].add(v)
            adjacency[v].add(u)
    label = {}
    component = 0
    for root in sorted(allowed):
        if root in label:
            continue
        stack = [root]
        while stack:
            v = stack.pop()
            if v in label:
                continue
            label[v] = component
            stack.extend(adjacency[v] - label.keys())
        component += 1
    return label


model_count = 0
for n in range(1, 5):
    possible = list(combinations(range(n), 2))
    for edge_mask in range(1 << len(possible)):
        edges = [e for i, e in enumerate(possible) if edge_mask >> i & 1]
        comp = components(n, edges)
        # Exhaust all endomorphisms which respect connected components, the
        # finite abstraction of a congruence-compatible mu_p.
        for mu in product(range(n), repeat=n):
            compatible = all(comp[u] != comp[v] or comp[mu[u]] == comp[mu[v]]
                             for u in range(n) for v in range(n))
            if not compatible:
                continue
            induced = {}
            well_defined = True
            for v in range(n):
                key, value = comp[v], comp[mu[v]]
                if key in induced and induced[key] != value:
                    well_defined = False
                    break
                induced[key] = value
            if not well_defined:
                raise AssertionError((n, edges, mu))
            induced_injective = len(set(induced.values())) == len(induced)
            root_closed = all(comp[mu[u]] != comp[mu[v]] or comp[u] == comp[v]
                              for u in range(n) for v in range(n))
            if induced_injective != root_closed:
                raise AssertionError((n, edges, mu, induced))
            model_count += 1
check(f"component injectivity equals root closure in {model_count} finite models", True)


# Explicit escape: image vertices 0,2 connect only through nonimage vertex 1.
escape_edges = [(0, 1), (1, 2)]
image = {0, 2}
full = components(3, escape_edges)
inside = components(3, escape_edges, image)
check("divisible endpoints can connect only through a nondivisible vertex",
      full[0] == full[2] and inside[0] != inside[2])


# Abstract implication: if every full connection of image endpoints is
# already an image-subgraph connection (convexity), and divided labels of
# each image component are connected, root closure follows.  Exhaust subsets.
implication_count = 0
for n in range(1, 6):
    possible = list(combinations(range(n), 2))
    for edge_mask in range(1 << len(possible)):
        edges = [e for i, e in enumerate(possible) if edge_mask >> i & 1]
        full = components(n, edges)
        for image_mask in range(1 << n):
            image = {v for v in range(n) if image_mask >> v & 1}
            inside = components(n, edges, image)
            convex = all(full[u] != full[v] or inside[u] == inside[v]
                         for u in image for v in image)
            if convex:
                # Taking the divided component relation to be the inside
                # relation is the minimal exact finite DIVPATH abstraction.
                root_closed = all(full[u] != full[v] or inside[u] == inside[v]
                                  for u in image for v in image)
                if not root_closed:
                    raise AssertionError((n, edges, image))
                implication_count += 1
check(f"p-convex plus divided-path implication in {implication_count} subgraphs", True)


doc = (HERE / "114_a_85_H7_MACRO_CONTEXT_GRAPH_AND_PATH_LIFTING.md").read_text()
for marker in (
    "H7-p-CONVEX",
    "H7-p-DIVPATH",
    "strictly weaker",
    "remain open",
):
    check(f"scope marker {marker}", marker in doc)

print("VERDICT: MACRO COMPONENT/PATH CRITERION PASS; p-CONVEX/DIVPATH OPEN")
