#!/usr/bin/env python3
"""Finite-set multiplication/contraction coordinate retractions."""

from itertools import product
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
    r"(3.2) \quad multiplication",
    r"(3.3) \quad contraction",
    r"extended, fiber by fiber",
    r"\pi \circ j = {\rm id}_{A_{[n]}}",
):
    check(f"source marker {marker}", marker in source)


def section(mapping, targets):
    chosen = {}
    for x, y in enumerate(mapping):
        chosen.setdefault(y, x)
    return {y: chosen[y] for y in targets}


models = 0
for source_size in range(1, 7):
    for target_size in range(1, source_size + 1):
        for mapping in product(range(target_size), repeat=source_size):
            if set(mapping) != set(range(target_size)):
                continue
            sec = section(mapping, range(target_size))
            check_section = all(mapping[sec[y]] == y for y in range(target_size))
            if not check_section:
                raise AssertionError((mapping, sec))
            for modulus in (2, 3, 5, 7):
                test_vectors = {(0,) * target_size, (1,) * target_size,
                                tuple((2 * y + 1) % modulus
                                      for y in range(target_size))}
                test_vectors.update(tuple(int(y == k) for y in range(target_size))
                                    for k in range(target_size))
                for b in test_vectors:
                    # Multiplication: unit coefficients, then selected projection.
                    multiplied = tuple(b[mapping[x]] for x in range(source_size))
                    projected = tuple(multiplied[sec[y]] for y in range(target_size))
                    if projected != b:
                        raise AssertionError(("mul", mapping, modulus, b, projected))

                    # Contraction: insert b on section, zero elsewhere.
                    inserted = [0] * source_size
                    coeff = [0] * source_size
                    for y in range(target_size):
                        inserted[sec[y]] = b[y]
                        coeff[sec[y]] = 1
                    contracted = tuple(
                        sum(inserted[x] * coeff[x]
                            for x in range(source_size) if mapping[x] == y) % modulus
                        for y in range(target_size)
                    )
                    if contracted != b:
                        raise AssertionError(("contract", mapping, modulus, b, contracted))
                    models += 1
check(f"coordinate retractions in {models} finite-map/ring/vector models", True)


# Nonsurjective maps split after restricting the target to the image.
nonsurjective = 0
for mapping in product(range(4), repeat=4):
    image = sorted(set(mapping))
    sec = section(mapping, image)
    if not all(mapping[sec[y]] == y for y in image):
        raise AssertionError((mapping, image, sec))
    if len(image) < 4:
        nonsurjective += 1
check(f"image-restricted sections for {nonsurjective} nonsurjective maps", True)


doc = (HERE / "114_a_100_H7_FINITE_SET_CONTRACTIONS_HAVE_COORDINATE_RETRACTIONS.md").read_text()
for marker in (
    "H7-COEFF-NORETRACT",
    "cannot by itself",
    "outer operation labels",
    "row A remain open",
):
    check(f"scope marker {marker}", marker in doc)

print("VERDICT: FINITE-SET REUSE RETRACTS; ONLY NONSPLIT COEFFICIENT CONTEXTS REMAIN")
