#!/usr/bin/env python3
"""Positive scalar-visible rigidification is incompatible with all even moves."""

from fractions import Fraction
from itertools import product
from pathlib import Path


HERE = Path(__file__).resolve().parent


def check(label, condition):
    if not condition:
        raise AssertionError(label)
    print("PASS", label)


def weights(a, b, edge):
    out = Fraction(1)
    for index, bit in enumerate(edge):
        out *= b[index] if bit else a[index]
    return out


models = 0
solutions = []
values = [Fraction(i) for i in range(-4, 5) if i]
for ratios in product(values, repeat=3):
    equations = (ratios[1] * ratios[2] == 1
                 and ratios[0] * ratios[2] == 1
                 and ratios[0] * ratios[1] == 1)
    if equations:
        solutions.append(ratios)
        if not (ratios[0] == ratios[1] == ratios[2]
                and ratios[0] * ratios[0] == 1):
            raise AssertionError(ratios)
    models += 1
check(f"even-move ratio system in {models} rational triples", True)
check("only common +/-1 ratios solve bounded system",
      set(solutions) == {(Fraction(1),) * 3, (Fraction(-1),) * 3})


# Exhaust positive weights: if all even moves agree, each bit weight agrees.
positive_models = 0
for a in product(range(1, 5), repeat=3):
    for b in product(range(1, 5), repeat=3):
        base = weights(a, b, (0, 0, 0))
        even_equal = all(weights(a, b, edge) == base
                         for edge in ((0, 1, 1), (1, 0, 1), (1, 1, 0)))
        if even_equal and a != b:
            raise AssertionError((a, b))
        positive_models += 1
check(f"positive rigidity no-go in {positive_models} weight pairs", True)


a = (Fraction(3),) * 3
b = (Fraction(5),) * 3
check("a96 witness W000=27", weights(a, b, (0, 0, 0)) == 27)
check("a96 witness W011=75", weights(a, b, (0, 1, 1)) == 75)
check("a96 decorations forbid first even move",
      weights(a, b, (0, 0, 0)) != weights(a, b, (0, 1, 1)))


doc = (HERE / "114_a_97_H7_POSITIVE_RIGIDIFICATION_KILLS_THE_EVEN_MOVES.md").read_text()
for marker in (
    "H7-SCALAR-INVISIBLE-RIGID",
    "closed negatively",
    "does not produce endpoints",
    "row A remain open",
):
    check(f"scope marker {marker}", marker in doc)

print("VERDICT: POSITIVE RIGIDIFICATION KILLS EVEN MOVES; SCALAR-INVISIBLE GATE OPEN")
