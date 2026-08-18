#!/usr/bin/env python3
"""Finite exact models for the tame-versus-context-retraction dichotomy."""

from itertools import product
from pathlib import Path


HERE = Path(__file__).resolve().parent


def check(label, condition):
    if not condition:
        raise AssertionError(label)
    print("PASS", label)


# Operations are represented by their complete scalar sandwich signatures.
operations = {
    "d0": (0, 1, 3, 4),
    "d1": (0, 2, 3, 5),
    "d2": (1, 1, 0, 2),
}
check("ambient signature system is tame",
      len(set(operations.values())) == len(operations))


# A retractable context exposes every signature coordinate (possibly with a
# fixed harmless prefix).  Hence it preserves distinctness.
for prefix in ((9,), (7, 8), (0, 0, 0)):
    embedded = {name: prefix + signature for name, signature in operations.items()}
    check(f"retractable context preserves distinction prefix={prefix}",
          len(set(embedded.values())) == len(operations))


# Exhaust arbitrary finite signatures and coordinate projections: if the
# complete signature is injective and every coordinate is recoverable from
# the embedded signature, the embedding is injective.
models = 0
alphabet = range(3)
for signatures in product(product(alphabet, repeat=3), repeat=3):
    tame = len(set(signatures)) == 3
    if not tame:
        continue
    # All coordinates retained, in permuted order, is a retraction model.
    for permutation in ((0, 1, 2), (2, 0, 1), (1, 2, 0)):
        images = [tuple(signature[i] for i in permutation) for signature in signatures]
        if len(set(images)) != 3:
            raise AssertionError((signatures, permutation, images))
        models += 1
check(f"tame+retract implication in {models} finite systems", True)


# Removing tameness: distinct syntactic names can have equal signatures.
nontame = {"left": (1, 0), "right": (1, 0)}
check("equal ambient signatures witness nontameness",
      len(nontame) == 2 and len(set(nontame.values())) == 1)

# Removing retraction: a coarse context may forget the only separating
# coordinate even when the ambient signatures are distinct.
ambient = {"left": (0, 1), "right": (0, 2)}
coarse = {name: (signature[0],) for name, signature in ambient.items()}
check("nonretractable context can hide a tame distinction",
      len(set(ambient.values())) == 2 and len(set(coarse.values())) == 1)


doc = (HERE / "114_a_99_H7_NONEXTRACTABLE_RIGIDITY_SPLITS_INTO_NONTAMENESS_OR_NORETRACT.md").read_text()
for marker in (
    "H7-CONTEXT-RETRACT",
    "H7-NONTAME-WITNESS",
    "H7-NORETRACT-ENTANGLE",
    "does not by itself give prime torsion",
    "row A remain open",
):
    check(f"scope marker {marker}", marker in doc)

print("VERDICT: NONEXTRACTABLE RIGIDITY = NONTAMENESS OR CONTEXT NO-RETRACT")
