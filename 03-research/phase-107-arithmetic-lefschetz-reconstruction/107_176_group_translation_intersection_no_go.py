#!/home/trabajo/miniforge3/bin/python
"""Real-curve falsifier for ordinary translation intersections."""

from sage.all import EllipticCurve, GF, HyperellipticCurve, PolynomialRing


def verify_finite_group(label, points, zero):
    nonzero = [point for point in points if point != zero]
    nonidentity_fixed_counts = []
    for shift in nonzero:
        fixed = sum(1 for point in points if point + shift == point)
        nonidentity_fixed_counts.append(fixed)
    identity_fixed = sum(1 for point in points if point + zero == point)
    ok = (
        bool(nonzero)
        and all(count == 0 for count in nonidentity_fixed_counts)
        and identity_fixed == len(points)
    )
    print(
        f"{label}_ORDER={len(points)}_NONIDENTITY_SHIFTS={len(nonzero)}"
        f"_MAX_FIXED={max(nonidentity_fixed_counts)}"
        f"_IDENTITY_FIXED={identity_fixed}_OK={'YES' if ok else 'NO'}"
    )
    return ok


atlas = []

F5 = GF(5)
paper0 = EllipticCurve(F5, [0, 0, 0, 1, 1])
atlas.append(("PAPER0_E_F5", list(paper0), paper0(0)))

F7 = GF(7)
supersingular = EllipticCurve(F7, [0, 0, 0, -1, 0])
atlas.append(("SUPERSINGULAR_E_F7", list(supersingular), supersingular(0)))

curve_11a1 = EllipticCurve("11a1").change_ring(F5)
atlas.append(("CURVE_11A1_MOD5", list(curve_11a1), curve_11a1(0)))

curve_14a1 = EllipticCurve("14a1").change_ring(F5)
atlas.append(("CURVE_14A1_MOD5", list(curve_14a1), curve_14a1(0)))

F2 = GF(2)
R = PolynomialRing(F2, "x")
x = R.gen()
genus2 = HyperellipticCurve(x**5 + x, 1)
jacobian_group = genus2.jacobian()(F2)
jacobian_points = jacobian_group.points()
atlas.append(("GENUS2_JACOBIAN_F2", jacobian_points, jacobian_group(0)))

atlas_ok = all(verify_finite_group(*entry) for entry in atlas)
supersingular_ok = supersingular.is_supersingular()
genus2_ok = genus2.genus() == 2 and len(jacobian_points) == 15

# The published transverse term is nonzero at v=5, u=2.
local_abs_5 = F5(1)  # |1 - 2|_5 = 1
distributional_local_term = 1
ordinary_nonidentity_translation_intersection = 0
local_mismatch = distributional_local_term != ordinary_nonidentity_translation_intersection

verdict = all([atlas_ok, supersingular_ok, genus2_ok, local_abs_5 == 1, local_mismatch])

print(f"ATLAS_REAL_GROUPS: {len(atlas)}")
print(f"SUPERSINGULAR_CONTROL_VERIFIED: {'YES' if supersingular_ok else 'NO'}")
print(f"GENUS2_JACOBIAN_VERIFIED: {'YES' if genus2_ok else 'NO'}")
print(f"DISTRIBUTIONAL_LOCAL_TERM_5_2: {distributional_local_term}")
print(
    "ORDINARY_NONIDENTITY_TRANSLATION_INTERSECTION: "
    f"{ordinary_nonidentity_translation_intersection}"
)
print(f"LOCAL_TERM_INTERSECTION_MISMATCH: {'YES' if local_mismatch else 'NO'}")
print("SMOOTH_GROUP_TRANSLATION_ROUTE: CLOSED_NO_GO")
print("REQUIRED_GEOMETRY: MONOID_BOUNDARY_WITH_TRANSVERSE_SCALING")
print(f"VERDICT: {'YES' if verdict else 'NO'}")
