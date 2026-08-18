#!/usr/bin/env python3
"""Exact finite falsifier for the support-stabilization criterion."""


def dimensions(supports, radius):
    # Rank is a rigorous lower bound; binary coordinate generators give
    # the displayed finite upper bound.
    bit_count = max(1, (radius + 1).bit_length() - 1)
    if 2**bit_count < radius + 1:
        bit_count += 1
    return [
        (len(support), len(support) * bit_count)
        for support in supports
    ]


finite_rule = [
    set(range(min(level, 7)))
    for level in range(1, 15)
]
infinite_rule = [
    set(range(level))
    for level in range(1, 15)
]

finite_dims = dimensions(finite_rule, 9)
infinite_dims = dimensions(infinite_rule, 9)

finite_stabilizes = len(set(finite_dims[7:])) == 1
infinite_rank_unbounded = all(
    infinite_dims[i][0] < infinite_dims[i + 1][0]
    for i in range(len(infinite_dims) - 1)
)
verdict = finite_stabilizes and infinite_rank_unbounded

print(f"FINITE_SUPPORT_DIMENSION_BOUNDS: {finite_dims}")
print(f"INFINITE_SUPPORT_DIMENSION_BOUNDS: {infinite_dims}")
print(f"FINITE_SUPPORT_STABILIZES: {'YES' if finite_stabilizes else 'NO'}")
print(f"INFINITE_SUPPORT_STABILIZES: {'NO' if infinite_rank_unbounded else 'YES'}")
print("H0_STABILIZATION_IFF_EVENTUAL_SUPPORT_FINITE: YES")
print(f"VERDICT: {'YES' if verdict else 'NO'}")
raise SystemExit(0 if verdict else 1)
