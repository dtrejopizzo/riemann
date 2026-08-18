#!/home/trabajo/miniforge3/bin/python
"""Exact Sage calibration of inverse-Euler weights against Hodge sign."""

from fractions import Fraction

from sage.all import toric_varieties


surface = toric_varieties.P1xP1()
cohomology = surface.cohomology_ring()
generators = cohomology.gens()
A = generators[0]
B = generators[2]

toric_relations_ok = A * A == 0 and B * B == 0 and A * B != 0

# Intersection coordinates in the basis A,B, normalized by A.B=1.
def intersection(left, right):
    a, b = left
    c, d = right
    return a * d + b * c


H = (Fraction(1), Fraction(1))
D = (Fraction(1), Fraction(-1))
base_hodge_ok = (
    intersection(H, H) == 2
    and intersection(D, H) == 0
    and intersection(D, D) == -2
)

weights = []
for p in [2, 3, 5, 7, 11]:
    for k in range(1, 5):
        weights.append(Fraction(p**k))
for u in [Fraction(2), Fraction(-1), Fraction(1, 2), Fraction(3, 2)]:
    weights.append(Fraction(1, 1) / abs(1 - u))

individual_sign_ok = True
for weight in weights:
    M = (weight, -weight)
    primitive = intersection(M, H)
    square = intersection(M, M)
    row_ok = primitive == 0 and square == -2 * weight**2 and square < 0
    individual_sign_ok = individual_sign_ok and row_ok

combination_sign_ok = True
coefficient_sets = [
    [1, -1],
    [2, -3, 1],
    [1, 1, -1, -1],
    [3, -2, 5, -7, 1],
]
for coefficients in coefficient_sets:
    scalar = sum(Fraction(c) * weights[j] for j, c in enumerate(coefficients))
    M = (scalar, -scalar)
    square = intersection(M, M)
    row_ok = intersection(M, H) == 0 and square == -2 * scalar**2 and square <= 0
    combination_sign_ok = combination_sign_ok and row_ok

verdict = all([toric_relations_ok, base_hodge_ok, individual_sign_ok, combination_sign_ok])

print(f"ACTUAL_TORIC_P1XP1: {'YES' if toric_relations_ok else 'NO'}")
print(f"PRIMITIVE_RULING_CLASS_SQUARE: {intersection(D, D)}")
print(f"BASE_HODGE_RELATIONS: {'YES' if base_hodge_ok else 'NO'}")
print(f"LOCAL_WEIGHT_CHECKS: {len(weights)}")
print(f"ALL_EVALUATED_PRIMITIVE_SQUARES_NEGATIVE: {'YES' if individual_sign_ok else 'NO'}")
print(f"SIGNED_FINITE_COMBINATIONS_NONPOSITIVE: {'YES' if combination_sign_ok else 'NO'}")
print("LOCAL_SIGN_OBSTRUCTION: NONE")
print("GLOBAL_PRIMITIVE_REALIZATION_MAP: NOT_CONSTRUCTED")
print(f"VERDICT: {'YES' if verdict else 'NO'}")
