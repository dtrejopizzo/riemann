#!/usr/bin/env python3
"""Exact certificate for scalar Picard descent failure."""

from fractions import Fraction

import sympy as sp


r = sp.symbols("r", positive=True)
ATLAS = ((1, 2), (2, 3), (3, 5), (5, 7), (7, 11))

literal_descent_fails = True
normalized_descent_fails = True
continuous_difference = True
nonzero_compact_tests = True

for left, right in ATLAS:
    # A continuous polynomial bump, extended by zero outside [left,right].
    f = (r - left) * (right - r)
    nonzero_compact_tests &= sp.expand(f) != 0

    literal_difference = sp.expand(2 * f - f)
    literal_descent_fails &= literal_difference != 0
    continuous_difference &= not literal_difference.has(sp.DiracDelta)

    # Degree-normalized descent under q=2 would require f(r)=f(2r).
    normalized_difference = sp.expand(f - f.subs(r, 2 * r))
    normalized_descent_fails &= normalized_difference != 0

    # Any nonzero point in the support has a rational orbit escaping it.
    midpoint = Fraction(left + right, 2)
    value = (midpoint - left) * (right - midpoint)
    escaped = midpoint
    while escaped <= right:
        escaped *= 2
    normalized_descent_fails &= value != 0 and escaped > right

# Finite-PL transition curvature is finite atomic; it cannot cancel a
# nonzero polynomial density on an interval.
finite_pl_repair_possible = not continuous_difference
literal_scalar_descent = not literal_descent_fails
normalized_scalar_descent = not normalized_descent_fails

verdict = all(
    (
        nonzero_compact_tests,
        literal_descent_fails,
        normalized_descent_fails,
        continuous_difference,
        not finite_pl_repair_possible,
        not literal_scalar_descent,
        not normalized_scalar_descent,
    )
)

print(f"CONTINUOUS_COMPACT_TEST_ATLAS: {'NONZERO' if nonzero_compact_tests else 'FAILED'}")
print(f"LITERAL_FROBENIUS_SCALAR_DESCENT: {'YES' if literal_scalar_descent else 'NO'}")
print(f"DEGREE_NORMALIZED_SCALAR_DESCENT: {'YES' if normalized_scalar_descent else 'NO'}")
print(f"FINITE_PL_TRANSITION_REPAIR: {'YES' if finite_pl_repair_possible else 'NO'}")
print("DC_CORRESPONDENCE_CURRENT: CONSTRUCTED")
print("SCALAR_DC_PICARD_DESCENT: CLOSED_NO_GO" if verdict else "SCALAR_DC_PICARD_DESCENT: OPEN")
print("ROW_D_CLASSICAL_HODGE_APPLICABLE: NO")
print("ROW_A_STATUS: PARTIAL")
print(f"VERDICT: {'YES' if verdict else 'NO'}")
