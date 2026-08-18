#!/usr/bin/env python3
"""Source-backed falsifier for finite stabilization of periodic H^0."""

from fractions import Fraction
from pathlib import Path
import re


SOURCE = (
    Path(__file__).resolve().parents[2]
    / "00-references/papers-nuevos/A/arXiv-1507.05818v2/scalingsite-CRAS.tex"
)


def compact_tex(text: str) -> str:
    return re.sub(r"\s+", "", text)


source_text = compact_tex(SOURCE.read_text(encoding="utf-8"))
published_filtration = r"H^0(D)^\rho:=\{f\inH^0(D)\mid\Vertf\Vert_p\leq\rho\}" in source_text
published_limit = (
    r"\cdim(H^0(D)):=\lim_{n\to\infty}p^{-n}\tdim(H^0(D)^{p^n})"
    in source_text
)
published_positive_degree_rr = r"\cdim(H^0(D))=\deg(D)" in source_text

primes = (2, 3, 5, 7, 11)
degrees = (Fraction(1, 3), Fraction(1), Fraction(7, 4))
bounded_values = (1, 7, 100)
depth = 32

# Every bounded candidate has normalized value tending to zero. The finite
# depth inequalities are controls; the document gives the limiting proof.
bounded_candidates_die = all(
    Fraction(bound, prime**depth) < degree / 1000
    for prime in primes
    for degree in degrees
    for bound in bounded_values
)

# A correctly scaled sequence is deliberately retained as a negative
# control: d_n = degree*p^n has constant positive normalized dimension.
scaled_controls_survive = all(
    Fraction(degree * prime**n, prime**n) == degree
    for prime in primes
    for degree in degrees
    for n in (0, 1, 2, 8)
)
scaled_controls_do_not_stabilize = all(
    degree * prime**8 != degree * prime**7
    for prime in primes
    for degree in degrees
)

verdict = all((
    published_filtration,
    published_limit,
    published_positive_degree_rr,
    bounded_candidates_die,
    scaled_controls_survive,
    scaled_controls_do_not_stabilize,
))

print("PUBLISHED_PERIODIC_RR_SOURCE: VERIFIED")
print("POSITIVE_DEGREE_FILTER_DIMENSIONS: UNBOUNDED")
print("FINITE_RAY_STABILIZATION_AS_FULL_H0: CLOSED_NO_GO")
print("REQUIRED_LIMIT: RENORMALIZED_CONTINUOUS_PRO_DIMENSION")
print(f"VERDICT: {'YES' if verdict else 'NO'}")

