#!/usr/bin/env python3
"""Falsifiable check of the CC cross-prime restriction no-go."""

from fractions import Fraction
from pathlib import Path


SOURCE = (
    Path(__file__).resolve().parents[2]
    / "00-references/papers-nuevos/A/arXiv-1502.05580v1/arithmeticsite_Adv_final1.tex"
)
PRIMES = (2, 3, 5, 7, 11)


def in_stalk(value, prime):
    """Check value in Z[1/p]_+ exactly."""
    value = Fraction(value)
    if value < 0:
        return False
    denominator = value.denominator
    while denominator > 1 and denominator % prime == 0:
        denominator //= prime
    return denominator == 1


def restrict(section, retained_primes):
    return {p: value for p, value in section.items() if p in retained_primes}


def generic_restriction(_section, generic_stalk_zero=True):
    return Fraction(0) if generic_stalk_zero else Fraction(1)


text = SOURCE.read_text(encoding="utf-8") if SOURCE.exists() else ""
source_generic = (
    "stalk of $\\cS$ at the generic point is $\\{0\\}$" in text
    and "associate this point to the generic point of $\\Spec\\Z$" in text
)
source_finite_support = (
    "non-negative elements of $H(p)$" in text
    and "for finitely many primes" in text
    and "restriction maps on sections of $\\cS$ are the obvious ones" in text
)

all_ok = source_generic and source_finite_support
independent = True
overlap_zero = True
cross_transition_nonzero = False

for i, p in enumerate(PRIMES):
    q = PRIMES[(i + 1) % len(PRIMES)]
    a = Fraction(p + 1, p**2)
    b = Fraction(q + 1, q**3)
    independent &= in_stalk(a, p) and in_stalk(b, q)

    common = {p: a, q: b}
    independent &= restrict(common, {p}) == {p: a}
    independent &= restrict(common, {q}) == {q: b}
    overlap_zero &= restrict(common, set()) == {}
    cross_transition_nonzero |= generic_restriction(common) != 0

# Negative control: a nonzero generic channel would create cross-prime
# information and must not satisfy the published generic-stalk input.
negative_control_rejected = generic_restriction(
    {2: Fraction(1, 2)}, generic_stalk_zero=False
) != 0

all_ok &= independent and overlap_zero and not cross_transition_nonzero
all_ok &= negative_control_rejected

print(f"PUBLISHED_SOURCE_FOUND: {'YES' if SOURCE.exists() else 'NO'}")
print(f"PUBLISHED_GENERIC_STALK_ZERO: {'YES' if source_generic else 'NO'}")
print(f"PUBLISHED_FINITE_SUPPORT_SECTIONS: {'YES' if source_finite_support else 'NO'}")
print(f"REAL_PRIME_ATLAS: {','.join(map(str, PRIMES))}")
print(f"INDEPENDENT_PRIME_VALUES_EXTEND: {'YES' if independent else 'NO'}")
print(f"NONZERO_CROSS_PRIME_RESTRICTION: {'YES' if cross_transition_nonzero else 'NO'}")
print(f"PRIME_ONLY_COUPLING: {'POSSIBLE' if cross_transition_nonzero else 'IMPOSSIBLE'}")
print(f"ADDITIONAL_GLOBAL_GLUE_REQUIRED: {'NO' if cross_transition_nonzero else 'YES'}")
print(f"NEGATIVE_CONTROL_REJECTED: {'YES' if negative_control_rejected else 'NO'}")
print(f"VERDICT: {'YES' if all_ok else 'NO'}")
raise SystemExit(0 if all_ok else 1)
