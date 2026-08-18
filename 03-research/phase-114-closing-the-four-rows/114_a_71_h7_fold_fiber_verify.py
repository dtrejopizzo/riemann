#!/usr/bin/env python3
"""Exact checks for a71; this does not prove H7-PRIME-REG."""

from fractions import Fraction
from itertools import product
from pathlib import Path


HERE = Path(__file__).resolve().parent
SOURCE = (
    HERE.parent.parent / "00-references" / "papers-nuevos" / "A"
    / "arXiv-1709.05831v1" / "HARAN_Dec2016_updated_4.tex"
)


def check(label, condition):
    if not condition:
        raise AssertionError(label)
    print("PASS", label)


# Primary-source scope: representation plus relations, not a uniqueness claim.
src = SOURCE.read_text(encoding="utf-8")
start = src.index("\\label{eq106}")
stop = src.index("\\section{Completed vector bundles}")
trees = src[start:stop]
check("source says every element has a representation",
      "has a representation as" in trees)
for anchor in (
    "delta$-{\\bf unit}",
    "delta$-{\\bf commutativity}",
    "delta$-{\\bf associativity}",
    "{\\bf cancellation}",
    "{\\bf commutativity}",
):
    check(f"source relation {anchor}", anchor in trees)
check("source segment has no unique normal-form theorem",
      "normal form" not in trees.lower() and "unique representation" not in trees.lower())


def injective(values):
    return len(values) == len(set(values))


def fiber_criterion(A, B, r, mu_a, mu_b):
    """Return (global injectivity, all fiber restrictions injective)."""
    global_inj = injective([mu_a[a] for a in A])
    fiber_inj = True
    for b in B:
        fiber = [a for a in A if r[a] == b]
        images = [mu_a[a] for a in fiber]
        fiber_inj &= injective(images)
        for a in fiber:
            if r[mu_a[a]] != mu_b[b]:
                raise AssertionError(f"fiber target b={b}, a={a}")
    return global_inj, fiber_inj


# Exhaust a nontrivial family A=B x C.  mu_A=(mu_B,phi_b(c)), allowing
# different maps in different fibers.  For injective mu_B the theorem says
# global injectivity iff every phi_b is injective.
B = tuple(range(3))
C = tuple(range(3))
A = tuple(product(B, C))
r = {a: a[0] for a in A}
mu_b = {0: 1, 1: 2, 2: 0}  # injective permutation
check("base p-action injective", injective(list(mu_b.values())))

maps_c = list(product(C, repeat=len(C)))
model_count = 0
for map0, map1, map2 in product(maps_c, repeat=3):
    maps = (map0, map1, map2)
    mu_a = {
        (b, c): (mu_b[b], maps[b][c])
        for b, c in A
    }
    global_inj, fiber_inj = fiber_criterion(A, B, r, mu_a, mu_b)
    if global_inj != fiber_inj:
        raise AssertionError(f"fold-fiber equivalence maps={maps}")
    model_count += 1
check(f"fold-fiber equivalence exhaustive models={model_count}",
      model_count == len(maps_c) ** len(B))


# A split equivariant map with regular base but nonregular total space.
B0 = ("*",)
A0 = (0, 1)
r0 = {0: "*", 1: "*"}
i0 = {"*": 0}
mu_b0 = {"*": "*"}
mu_a0 = {0: 0, 1: 0}
check("split countermodel retract", r0[i0["*"]] == "*")
check("split countermodel equivariant",
      all(r0[mu_a0[a]] == mu_b0[r0[a]] for a in A0))
check("split countermodel base regular", injective(list(mu_b0.values())))
check("split countermodel total nonregular", not injective(list(mu_a0.values())))


# Fiberwise residual faithfulness can be strictly weaker than global
# faithfulness: epsilon forgets B but is injective on each B-fiber.
epsilon = {(b, c): c for b, c in A}
check("residual evaluation faithful on every fold fiber",
      all(injective([epsilon[(b, c)] for c in C]) for b in B))
check("residual evaluation not globally faithful",
      not injective([epsilon[a] for a in A]))


# Ordinary exact model of the localization lemma.  Equality of fractions is
# exact (Fraction), and multiplication by every tested prime remains injective.
localized = {
    Fraction(a, s)
    for a in range(-20, 21)
    for s in (1, 2, 4, 5, 8, 10, 20)
}
for p in (2, 3, 5, 7, 11):
    check(f"localized p-cancellation p={p}",
          injective([p * x for x in localized]))


doc = (HERE / "114_a_71_H7_FOLD_FIBERS_AND_NORMAL_FORM_GATE.md").read_text()
for claim in (
    "H7-RF-FOLD",
    "H7-NF",
    "`a4-strong` remain",
    "does not assert H7-RF-FOLD or H7-NF",
):
    check(f"scope marker {claim}", claim in doc)

print("VERDICT: FOLD-FIBER REDUCTION PASS; H7-RF-FOLD/H7-NF OPEN")
