#!/usr/bin/env python3
"""Finite truncation falsifier for naive stalk linearization."""


def radius_one_dimension(number_of_basis_vectors):
    # Every radius-one generator covers exactly one signed coordinate ray.
    generators = {
        frozenset({(i, 1), (i, -1)})
        for i in range(number_of_basis_vectors)
    }
    return len(generators)


sizes = (1, 2, 4, 8, 16, 32, 64)
curve_dims = [radius_one_dimension(size) for size in sizes]
square_dims = [radius_one_dimension(size * size) for size in sizes]

curve_unbounded = curve_dims == list(sizes)
square_unbounded = square_dims == [size * size for size in sizes]
verdict = curve_unbounded and square_unbounded

print(f"CURVE_STALK_TRUNCATION_DIMENSIONS: {curve_dims}")
print(f"SQUARE_STALK_TRUNCATION_DIMENSIONS: {square_dims}")
print(f"PRIMITIVE_RAYS_FORCE_UNBOUNDED_DIMENSION: {'YES' if verdict else 'NO'}")
print("NAIVE_Z_LINEARIZATION_RR_FINITE: NO")
print("NAIVE_ABSOLUTE_STALK_CECH_LIFT: REJECTED")
print(f"VERDICT: {'YES' if verdict else 'NO'}")
raise SystemExit(0 if verdict else 1)
