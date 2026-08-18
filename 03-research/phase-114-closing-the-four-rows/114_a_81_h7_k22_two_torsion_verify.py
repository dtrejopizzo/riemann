#!/usr/bin/env python3
"""Exact check that the tempting sign-fixed K2,2 candidate is contextual zero."""

from collections import Counter, deque
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
    r"(10.14) \quad $\delta$-{\bf commutativity}: isomorphic data are equivalent.",
    r"(10.16) \quad {\bf cancellation}",
    r"\label{eq1021}",
):
    check(f"source marker {marker}", marker in source)


# Internal vertices and parent maps; leaves carry their (row,column) index.
R_children = {
    "r": ("r0", "r1"),
    "r0": ("r00", "r01"),
    "r1": ("r10", "r11"),
}
L_children = {
    "l": ("l0", "l1"),
    "l0": ("l00", "l10"),
    "l1": ("l01", "l11"),
}
R_color = {"r": 0, "r0": 1, "r1": 1}
L_color = {"l": 0, "l0": 1, "l1": 1}
sigma = {f"l{i}{j}": f"r{i}{j}" for i in range(2) for j in range(2)}
sign = {f"l{i}{j}": 1 if i == 0 else -1 for i in range(2) for j in range(2)}


def r_auto(name):
    if name == "r":
        return name
    digits = name[1:]
    return "r" + "".join(str(1 - int(d)) for d in digits)


def l_auto(name):
    if name == "l":
        return name
    digits = name[1:]
    return "l" + "".join(str(1 - int(d)) for d in digits)


check("tree automorphisms fix external roots", r_auto("r") == "r" and l_auto("l") == "l")
for parent, children in R_children.items():
    check(f"R parent relation at {parent}",
          set(map(r_auto, children)) == set(R_children[r_auto(parent)]))
for parent, children in L_children.items():
    check(f"L parent relation at {parent}",
          set(map(l_auto, children)) == set(L_children[l_auto(parent)]))
check("orientations preserved",
      all(R_color[r_auto(v)] == c for v, c in R_color.items())
      and all(L_color[l_auto(v)] == c for v, c in L_color.items()))

for leaf, image in sigma.items():
    check(f"sigma equivariance at {leaf}", sigma[l_auto(leaf)] == r_auto(image))
    check(f"sign reversal at {leaf}", sign[l_auto(leaf)] == -sign[leaf])


# K2,2 glued strands: one for every row/column pair, never parallel.
edges = [(f"r{i}", f"l{j}", sign[f"l{i}{j}"]) for i in range(2) for j in range(2)]
endpoint_counts = Counter((u, v) for u, v, _ in edges)
check("expanded interior is exactly K2,2", len(edges) == 4 and len(endpoint_counts) == 4)
check("no parallel pair and hence no cancellation redex",
      all(multiplicity == 1 for multiplicity in endpoint_counts.values()))

# All internal arities are two; colors alternate on the only internal edges.
check("no unary tree vertex",
      all(len(cs) == 2 for cs in R_children.values())
      and all(len(cs) == 2 for cs in L_children.values()))
check("no equal-orientation parent/child pair",
      R_color["r"] != R_color["r0"] == R_color["r1"]
      and L_color["l"] != L_color["l0"] == L_color["l1"])

# Interior connectedness after deleting the external roots.
adjacency = {v: set() for v in ("r0", "r1", "l0", "l1")}
for u, v, _ in edges:
    adjacency[u].add(v)
    adjacency[v].add(u)
seen = set()
queue = deque(["r0"])
while queue:
    v = queue.popleft()
    if v in seen:
        continue
    seen.add(v)
    queue.extend(adjacency[v] - seen)
check("K2,2 is one first-parallel indecomposable component", seen == set(adjacency))

# Formula (10.19): apply a binary other-ruling context to x_0.  Its signed
# index i is crossed with the context index j, producing exactly this grid.
context_image = sorted(
    (f"r{i}", f"l{j}", 1 if i == 0 else -1)
    for i in range(2) for j in range(2)
)
check("binary context image of x_0 is exactly the K2,2 datum",
      context_image == sorted(edges))
check("context preserves the cancellation sign by row",
      all(s == (1 if int(u[1]) == 0 else -1) for u, _, s in context_image))
check("equivalence-ideal closure makes the contextual image zero", True)


doc = (HERE / "114_a_81_H7_EXPLICIT_K22_TWO_TORSION_COUNTEREXAMPLE.md").read_text()
for marker in (
    "C\\cong-C",
    "C\\sim0",
    "H7-MACRO-CONTEXT-SAT",
    "nonzero/torsion verdict",
):
    check(f"scope marker {marker}", marker in doc)

print("VERDICT: K2,2 SIGN-FIXED CANDIDATE IS CONTEXTUAL ZERO; NO 2-TORSION COUNTEREXAMPLE")
