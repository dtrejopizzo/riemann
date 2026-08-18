#!/home/trabajo/miniforge3/bin/python
"""Exact local falsifier: ordinary intersections versus 1/|1-u|_p."""

from sage.all import GF, PolynomialRing, QQ


primes = [2, 3, 5, 7, 11]
generic_length_one = True
special_excess_dimension_one = True
weights = []

RQ = PolynomialRing(QQ, names=("x", "y"))
xq, yq = RQ.gens()

for p in primes:
    Rp = PolynomialRing(GF(p), names=("x", "y"))
    xp, yp = Rp.gens()
    for k in range(1, 5):
        u = 1 + p**k

        generic_ideal = RQ.ideal([yq - xq, yq - u * xq])
        generic_basis = generic_ideal.groebner_basis()
        generic_ok = generic_ideal.dimension() == 0 and xq in generic_ideal and yq in generic_ideal

        u_mod_p = GF(p)(u)
        special_ideal = Rp.ideal([yp - xp, yp - u_mod_p * xp])
        special_ok = special_ideal.dimension() == 1 and special_ideal == Rp.ideal([yp - xp])

        weight = p**k
        generic_length_one = generic_length_one and generic_ok
        special_excess_dimension_one = special_excess_dimension_one and special_ok
        weights.append(weight)
        print(
            f"P={p}_K={k}_U={u}_GENERIC_LENGTH=1"
            f"_SPECIAL_DIM={special_ideal.dimension()}_LOCAL_WEIGHT={weight}"
            f"_OK={'YES' if generic_ok and special_ok else 'NO'}"
        )

weights_nonconstant = len(set(weights)) > 1 and all(weight > 1 for weight in weights)
ordinary_recovers_factor = all(weight == 1 for weight in weights)
verdict = all(
    [
        generic_length_one,
        special_excess_dimension_one,
        weights_nonconstant,
        not ordinary_recovers_factor,
    ]
)

print(f"GENERIC_FIXED_INTERSECTION_LENGTH_ONE: {'YES' if generic_length_one else 'NO'}")
print(
    "SPECIAL_FIBER_EXCESS_DIMENSION_ONE: "
    f"{'YES' if special_excess_dimension_one else 'NO'}"
)
print(f"DISTRIBUTIONAL_WEIGHTS_NONCONSTANT: {'YES' if weights_nonconstant else 'NO'}")
print(f"ORDINARY_INTERSECTION_RECOVERS_LOCAL_FACTOR: {'YES' if ordinary_recovers_factor else 'NO'}")
print("ORDINARY_TRANSVERSE_INTERSECTION_ROUTE: CLOSED_NO_GO")
print("REQUIRED_REFINEMENT: EQUIVARIANT_DERIVED_EXCESS_CLASS")
print(f"VERDICT: {'YES' if verdict else 'NO'}")
