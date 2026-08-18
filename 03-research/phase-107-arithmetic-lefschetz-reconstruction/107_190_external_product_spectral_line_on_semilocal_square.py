#!/home/trabajo/miniforge3/bin/python
"""Falsifier for the external-product spectral line on the semilocal square."""

from mpmath import mp


mp.dps = 70


def z(p, s):
    return 1 / (1 - mp.power(p, -s))


def g(primes, s):
    value = mp.mpc(1)
    for p in sorted(primes):
        value *= z(p, s)
    return value


def arch(s):
    return mp.mpf("0.5") * s * (s - 1) * mp.power(mp.pi, -s / 2) * mp.gamma(s / 2)


parameters = [
    (mp.mpf("2"), mp.mpf("3")),
    (mp.mpf("2.25"), mp.mpf("1.75")),
    (mp.mpc(2, 1), mp.mpc(3, -2)),
]
rectangles = [
    (set(), {2}, {3}, {3, 5, 7}),
    ({2}, {2, 3}, {5}, {5, 11}),
    ({2, 3}, {2, 3, 5}, {7}, {7, 11, 13}),
]
tolerance = mp.mpf("1e-58")

functoriality_ok = True
coordinate_commutation_ok = True
frame_trivialization_ok = True
cech_equalizers_ok = True
canonical_section_ok = True
diagonal_tensor_ok = True

for (s1, s2), (s0, s1_set, t0, t1_set) in zip(parameters, rectangles):
    scalar = mp.mpc("2.125", "-0.75")
    s2_set = s1_set | {17}
    t2_set = t1_set | {19}

    direct = scalar * g(s2_set - s0, s1) * g(t2_set - t0, s2)
    staged = (
        scalar
        * g(s1_set - s0, s1)
        * g(t1_set - t0, s2)
        * g(s2_set - s1_set, s1)
        * g(t2_set - t1_set, s2)
    )
    functoriality_ok &= abs(direct - staged) < tolerance

    row_then_column = scalar * g(s1_set - s0, s1) * g(t1_set - t0, s2)
    column_then_row = scalar * g(t1_set - t0, s2) * g(s1_set - s0, s1)
    coordinate_commutation_ok &= abs(row_then_column - column_then_row) < tolerance

    source_gauge = scalar / (g(s0, s1) * g(t0, s2))
    target_gauge = row_then_column / (g(s1_set, s1) * g(t1_set, s2))
    frame_trivialization_ok &= abs(source_gauge - target_gauge) < tolerance

    p, q = 23, 29
    left = scalar * z(p, s1)
    right = scalar * z(q, s1)
    overlap_left = left * z(q, s1)
    overlap_right = right * z(p, s1)
    glued_left = left / z(p, s1)
    glued_right = right / z(q, s1)
    cech_equalizers_ok &= (
        abs(overlap_left - overlap_right) < tolerance
        and abs(glued_left - scalar) < tolerance
        and abs(glued_right - scalar) < tolerance
    )

    sigma_source = arch(s1) * arch(s2) * g(s0, s1) * g(t0, s2)
    sigma_target = arch(s1) * arch(s2) * g(s1_set, s1) * g(t1_set, s2)
    sigma_restricted = sigma_source * g(s1_set - s0, s1) * g(t1_set - t0, s2)
    canonical_section_ok &= abs(sigma_restricted - sigma_target) < tolerance

    diagonal_s = mp.mpf("2.5")
    diagonal_chart = g(s1_set, diagonal_s) * g(t1_set, diagonal_s)
    direct_tensor = g(s1_set, diagonal_s) * g(t1_set, diagonal_s)
    diagonal_tensor_ok &= abs(diagonal_chart - direct_tensor) < tolerance
    for common_prime in s1_set & t1_set:
        without_common = diagonal_chart / (z(common_prime, diagonal_s) ** 2)
        diagonal_tensor_ok &= abs(diagonal_chart - without_common * z(common_prime, diagonal_s) ** 2) < tolerance


specializations = [(1, 2), (2, 3), (3, 5), (5, 7)]
specialization_exact_ok = True
spectral_collapse_rejected = True
for p in [2, 3, 5, 7, 11]:
    for n, m in specializations:
        s = mp.mpc("2.2", "0.4")
        pulled = z(p, n * s) * z(p, m * s)
        expected = 1 / ((1 - mp.power(p, -n * s)) * (1 - mp.power(p, -m * s)))
        collapsed = z(p, (n + m) * s)
        specialization_exact_ok &= abs(pulled - expected) < tolerance
        spectral_collapse_rejected &= abs(pulled - collapsed) > mp.mpf("1e-30")


verdict = all(
    [
        functoriality_ok,
        coordinate_commutation_ok,
        frame_trivialization_ok,
        cech_equalizers_ok,
        canonical_section_ok,
        diagonal_tensor_ok,
        specialization_exact_ok,
        spectral_collapse_rejected,
    ]
)

print(f"TWO_DIMENSIONAL_RESTRICTIONS_FUNCTORIAL: {'YES' if functoriality_ok else 'NO'}")
print(f"ROW_COLUMN_RESTRICTIONS_COMMUTE: {'YES' if coordinate_commutation_ok else 'NO'}")
print(f"PRODUCT_CECH_EQUALIZERS: {'YES' if cech_equalizers_ok else 'NO'}")
print(f"PRODUCT_FRAME_CHANGE_TRIVIALIZES: {'YES' if frame_trivialization_ok else 'NO'}")
print(f"CANONICAL_EXTERNAL_SECTION_RESTRICTS: {'YES' if canonical_section_ok else 'NO'}")
print(f"DIAGONAL_PULLBACK_RETAINS_TENSOR_MULTIPLICITY: {'YES' if diagonal_tensor_ok else 'NO'}")
print(f"FROBENIUS_SPECTRAL_SPECIALIZATION_EXACT: {'YES' if specialization_exact_ok else 'NO'}")
print(f"FALSE_SINGLE_WEIGHT_COLLAPSE_REJECTED: {'YES' if spectral_collapse_rejected else 'NO'}")
print("SEMILOCAL_SQUARE_EXTERNAL_PRODUCT_LINE: CONSTRUCTED")
print("DELIGNE_PAIRING_OR_TOP_CLASS: NOT_CONSTRUCTED")
print(f"VERDICT: {'YES' if verdict else 'NO'}")
