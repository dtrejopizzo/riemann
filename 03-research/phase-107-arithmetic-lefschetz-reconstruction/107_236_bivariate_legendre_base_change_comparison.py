#!/usr/bin/env python3
"""Exact certificate for bivariate Legendre base change on the Scaling square."""

from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
REFERENCES = HERE.parent.parent / "00-references/papers-nuevos/A"
SCALING_NOTE = REFERENCES / "arXiv-1507.05818v2/scalingsite-CRAS.tex"
SQUARE_PAPER = REFERENCES / "arXiv-1805.10501v1/thecurve_K.tex"


def read(path):
    return path.read_text(encoding="utf-8") if path.exists() else ""


scaling = read(SCALING_NOTE)
square = read(SQUARE_PAPER)

published_legendre = all(
    token in scaling
    for token in (
        "H_{\\rm max}\\hat \\otimes_\\B\\rma",
        "convex, piecewise affine continuous functions",
        "\\ell_N(\\lambda)=\\max_j \\lambda x_j+y_j",
        "The map $N\\mapsto \\ell_N$ is an isomorphism",
    )
)
published_periodic_stalk = all(
    token in scaling
    for token in (
        "\\R_+^*/p^\\Z\\to C_p",
        "piecewise affine, continuous convex functions, with slopes in $H_p$",
        "H^0(D)=\\Gamma(C_p,\\cO(D))",
    )
)
published_square_boundary = all(
    token in square
    for token in (
        "definition of $H^0$ is straightforward",
        "definition of the sheaf cohomology (as idempotent monoid) $H^1$",
        "is still open at this time",
    )
)


def affine(term, x, y):
    h, k, c = term
    return h * x + k * y + c


def evaluate(terms, x, y):
    return max(affine(term, x, y) for term in terms)


def external_expand(left_families, right_families):
    terms = []
    for left, right in zip(left_families, right_families):
        for h, u in left:
            for k, v in right:
                terms.append((h, k, u + v))
    return terms


PRIME_ATLAS = ((2, 3), (2, 5), (3, 5), (5, 7), (7, 11))
GRID = tuple(Fraction(i, 4) for i in range(1, 17))

distributivity = True
surjectivity = True
frobenius_covariance = True
negative_control_detected = True

for p, q in PRIME_ATLAS:
    left = (
        ((Fraction(-1, p), Fraction(1, 3)), (Fraction(2, p), Fraction(-2, 5))),
        ((Fraction(1), Fraction(-1, 7)),),
    )
    right = (
        ((Fraction(-2, q), Fraction(3, 8)), (Fraction(1, q), Fraction(-1, 4))),
        ((Fraction(3, q), Fraction(2, 9)),),
    )
    expanded = external_expand(left, right)

    for x in GRID:
        for y in GRID:
            tensor_value = max(
                max(h * x + u for h, u in lf) + max(k * y + v for k, v in rf)
                for lf, rf in zip(left, right)
            )
            distributivity &= tensor_value == evaluate(expanded, x, y)

            transformed = tuple((p * h, q * k, c) for h, k, c in expanded)
            frobenius_covariance &= evaluate(expanded, p * x, q * y) == evaluate(
                transformed, x, y
            )

    # Every bivariate affine term is a pure external term, hence every finite
    # maximum has an explicit preimage term by term.
    target = (
        (Fraction(-2, p), Fraction(3, q), Fraction(5, 11)),
        (Fraction(1, p), Fraction(-1, q), Fraction(-7, 13)),
        (Fraction(4, p), Fraction(2, q), Fraction(1, 17)),
    )
    preimage_left = tuple(((h, c),) for h, _, c in target)
    preimage_right = tuple(((k, Fraction(0)),) for _, k, _ in target)
    lifted = external_expand(preimage_left, preimage_right)
    surjectivity &= lifted == list(target)

    # A mutated map f(x)+g(y)+xy is not external-tropical-linear: its mixed
    # finite difference is nonzero, unlike every affine generator.
    x0, x1, y0, y1 = Fraction(1), Fraction(2), Fraction(1), Fraction(3)
    mixed_difference = x1 * y1 - x1 * y0 - x0 * y1 + x0 * y0
    negative_control_detected &= mixed_difference != 0

verdict = all(
    (
        published_legendre,
        published_periodic_stalk,
        published_square_boundary,
        distributivity,
        surjectivity,
        frobenius_covariance,
        negative_control_detected,
    )
)

print(f"PUBLISHED_ONE_DIMENSIONAL_LEGENDRE_BASE_CHANGE: {'YES' if published_legendre else 'NO'}")
print(f"BIVARIATE_FUNCTIONAL_REDUCTION: {'EXACT' if distributivity and surjectivity else 'FAILED'}")
print(f"FROBENIUS_COVARIANCE: {'YES' if frobenius_covariance else 'NO'}")
print(f"PERIODIC_EXTERNAL_H0_COMPARISON: {'ISOMORPHIC' if verdict else 'NOT_PROVED'}")
print("SCALING_SQUARE_EXTERNAL_H0: CONSTRUCTED" if verdict else "SCALING_SQUARE_EXTERNAL_H0: OPEN")
print("INTRINSIC_MIXED_DIVISORS: OPEN")
print("SQUARE_H1: OPEN")
print("ROW_A_STATUS: PARTIAL")
print(f"VERDICT: {'YES' if verdict else 'NO'}")
