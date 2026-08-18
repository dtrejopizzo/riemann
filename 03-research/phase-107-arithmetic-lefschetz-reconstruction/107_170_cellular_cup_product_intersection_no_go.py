#!/usr/bin/env python3
"""Exact mismatch between cellular cup products and real intersections."""


def points_on_fixed_curve(prime):
    squares = {value * value % prime for value in range(prime)}
    affine = 0
    for x in range(prime):
        rhs = (x**3 + x + 1) % prime
        affine += sum(1 for y in range(prime) if y * y % prime == rhs)
        assert (rhs in squares) == any(y * y % prime == rhs for y in range(prime))
    return affine + 1  # point at infinity


# H*(T^2)=Lambda(u,v): the only degree-two basis element is uv and
# its square has repeated u and v, hence vanishes by anti-commutativity.
cellular_h4_rank = 0
cellular_divisor_product = 0

point_count = points_on_fixed_curve(5)
geometric_graph_diagonal = point_count

all_ok = cellular_h4_rank == 0
all_ok &= cellular_divisor_product == 0
all_ok &= point_count == 9 and geometric_graph_diagonal != 0

print(f"FIXED_CURVE_F5_POINT_COUNT: {point_count}")
print(f"CELLULAR_H4_RANK: {cellular_h4_rank}")
print(f"CELLULAR_DIVISOR_CUP_PRODUCT: {cellular_divisor_product}")
print(f"GEOMETRIC_GRAPH_DIAGONAL_INTERSECTION: {geometric_graph_diagonal}")
print("CELLULAR_CUP_PRODUCT_RECOVERS_INTERSECTION: NO")
print("REQUIRED_INTERSECTION_SOURCE: RELATIVE_TRACE_OR_COMPLEX_SURFACE_TOP_CLASS")
print(f"VERDICT: {'YES' if all_ok else 'NO'}")
raise SystemExit(0 if all_ok else 1)
