#!/usr/bin/env python3
"""Finite regression checks for a77; global core confluence remains open."""

from functools import lru_cache
from itertools import combinations
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
H17 = ROOT / "00-references/papers-nuevos/A/arXiv-1709.05831v1/HARAN_Dec2016_updated_4.tex"


def check(label, condition):
    if not condition:
        raise AssertionError(label)
    print("PASS", label)


source = H17.read_text()
for marker in (
    r"(10.16) \quad {\bf cancellation}",
    r"(10.17) \quad {\bf commutativity}",
    r"Here $\overline X$ is a cut of the tree $F$",
):
    check(f"source marker {marker}", marker in source)


def ideals(n, edges):
    """Order ideals for the DAG whose vertices already have topological order."""
    incoming = [0] * n
    for u, v in edges:
        incoming[v] |= 1 << u
    # Transitive predecessor masks.
    for v in range(n):
        closure = incoming[v]
        for u in range(v):
            if closure >> u & 1:
                closure |= incoming[u]
        incoming[v] = closure
    return [mask for mask in range(1 << n)
            if all(not (mask >> v & 1) or incoming[v] & ~mask == 0
                   for v in range(n))]


dag_count = 0
ideal_count = 0
for n in range(0, 7):
    possible = list(combinations(range(n), 2))
    for edge_mask in range(1 << len(possible)):
        edges = [e for i, e in enumerate(possible) if edge_mask >> i & 1]
        js = ideals(n, edges)
        ideal_set = set(js)
        # Every nonzero ideal has a one-vertex deletion which is again an
        # ideal; iterating connects it to zero and hence connects all ideals.
        for start in js:
            if start and not any(
                (start ^ (1 << v)) in ideal_set
                for v in range(n) if start >> v & 1
            ):
                raise AssertionError((n, edges, start))
        dag_count += 1
        ideal_count += len(js)
check(f"cut graphs connected for {dag_count} DAGs/{ideal_count} ideals", True)


@lru_cache(None)
def bundle_terminals(a, b):
    if not a or not b:
        return {(a, b)}
    return bundle_terminals(a - 1, b - 1)


for a in range(9):
    for b in range(9):
        terminal = ((max(a - b, 0), max(b - a, 0)))
        if bundle_terminals(a, b) != {terminal}:
            raise AssertionError((a, b, terminal))
check("unique bundle normal forms through multiplicity eight", True)

for p in (2, 3, 5, 7, 11):
    for a in range(9):
        for b in range(9):
            for c in range(9):
                for d in range(9):
                    scaled_equal = p * (a - b) == p * (c - d)
                    original_equal = a - b == c - d
                    if scaled_equal != original_equal:
                        raise AssertionError((p, a, b, c, d))
check("local parallel-bundle p-root closure", True)


doc = (HERE / "114_a_77_H7_CUT_CONNECTIVITY_AND_LOCAL_CANCELLATION.md").read_text()
for marker in (
    "H7-CORE-CONFLUENCE",
    "No confluence theorem for those overlaps is asserted here",
    "completed lattice remain open",
    "topology-changing pruning/contraction",
):
    check(f"scope marker {marker}", marker in doc)

print("VERDICT: FIXED-DAG CUT/LOCAL BUNDLE PASS; FULL MACRO CONTEXT SYSTEM OPEN")
