#!/usr/bin/env python3
"""Typed F2 parity fiber diagram; no macro torsion collision is asserted."""

from itertools import combinations, product
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
    r"putting for $X,Y \in {\mathbb F}$, $f \in {\rm Set} (X,Y)$",
    r"(3.7) \quad {\bf multiplication}",
    r"(3.8) \quad {\bf contraction}",
    r"\label{eq314}",
    r"\label{eq315}",
):
    check(f"source marker {marker}", marker in source)


E = list(product((0, 1), repeat=2))


def pi(index, point):
    i, j = point
    return (i, j, i ^ j)[index]


for a, b in combinations(range(3), 2):
    image = {(pi(a, point), pi(b, point)) for point in E}
    check(f"pair projection ({a + 1},{b + 1}) is bijective",
          len(image) == len(E) and image == set(product((0, 1), repeat=2)))


triple_image = {tuple(pi(index, point) for index in range(3)) for point in E}
expected = {(0, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 0)}
check("joint image is the even parity hypergraph", triple_image == expected)
check("all and only even-parity triples occur",
      all((sum(edge) % 2 == 0) == (edge in triple_image)
          for edge in product((0, 1), repeat=3)))

for part in range(3):
    for vertex in (0, 1):
        check(f"2-regular part={part}, vertex={vertex}",
              sum(edge[part] == vertex for edge in triple_image) == 2)


def disjoint(a, b):
    return all(x != y for x, y in zip(a, b))


check("typed parity hypergraph still has no perfect matching",
      not any(disjoint(a, b) for a, b in combinations(triple_image, 2)))


doc = (HERE / "114_a_92_H7_PARITY_FIBER_DIAGRAM_IS_TYPED.md").read_text()
for marker in (
    "H7-PARITY-TYPE is closed",
    "H7-PARITY-MACRO",
    "H7-PARITY-CLOSURE",
    "H7-PARITY-SEPARATE",
    "does not prove",
    "row A remain open",
):
    check(f"scope marker {marker}", marker in doc)

print("VERDICT: EVEN-PARITY ANCESTRY IS TYPED; MACRO COLLISION/NONZERO OPEN")
