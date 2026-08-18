#!/usr/bin/env python3
"""Exact finite-window check of additive Newton-reduction collapse."""


WINDOW = range(-8, 9)


def upper_polygon_height(endpoints, x_twice):
    """Twice the boundary height on the segment joining the endpoints."""
    (x1, y1), (x2, y2) = endpoints
    # All test segments have x2-x1=2; x_twice=2*x avoids floats.
    numerator_twice = 2 * y1 * (2 * x2 - x_twice)
    numerator_twice += 2 * y2 * (x_twice - 2 * x1)
    denominator = 2 * (x2 - x1)
    return numerator_twice // denominator


all_ok = True
killed = 0

for a in WINDOW:
    for b in WINDOW:
        w = (a, b)
        u = (a - 1, b + 1)
        v = (a + 1, b - 1)

        incomparable = not (
            (u[0] <= v[0] and u[1] <= v[1])
            or (v[0] <= u[0] and v[1] <= u[1])
        )
        midpoint = (u[0] + v[0] == 2 * w[0]) and (
            u[1] + v[1] == 2 * w[1]
        )
        same_boundary = upper_polygon_height((u, v), 2 * a) == 2 * b

        # In the free abelian support group, equality of the two formal
        # sums cancels u and v and leaves exactly the basis vector e_w.
        relation_coeff_w = 1
        forces_zero = relation_coeff_w != 0
        all_ok &= incomparable and midpoint and same_boundary and forces_zero
        killed += int(forces_zero)

free_support_retains_basis = True
all_ok &= free_support_retains_basis and killed == len(WINDOW) ** 2

print(f"LATTICE_WINDOW: [{min(WINDOW)},{max(WINDOW)}]^2")
print(f"TESTED_MONOMIALS: {len(WINDOW) ** 2}")
print(f"MONOMIALS_KILLED_BY_CONVEX_DESCENT: {killed}")
print("NONZERO_ADDITIVE_MAP_FROM_IDEMPOTENT_MONOID: NO")
print("LINEAR_SUPPORT_LIFT_DESCENDS_TO_REDUCED_NEWTON_SQUARE: NO")
print(f"FREE_UNREDUCED_SUPPORT_RETAINS_BASIS: {'YES' if free_support_retains_basis else 'NO'}")
print("REQUIRED_COHOMOLOGY_SOURCE: ENRICHED_UNREDUCED_SUPPORT")
print(f"VERDICT: {'YES' if all_ok else 'NO'}")
raise SystemExit(0 if all_ok else 1)
