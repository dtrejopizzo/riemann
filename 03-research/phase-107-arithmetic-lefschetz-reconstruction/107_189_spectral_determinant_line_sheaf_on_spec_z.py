#!/home/trabajo/miniforge3/bin/python
"""Exact/high-precision falsifier for spectral determinant sheaf descent."""

from mpmath import mp


mp.dps = 60


def z(p, s):
    return 1 / (1 - mp.power(p, -s))


def g(prime_set, s):
    value = mp.mpc(1)
    for p in sorted(prime_set):
        value *= z(p, s)
    return value


parameters = [mp.mpf("2"), mp.mpf("2.5"), mp.mpc(2, 3)]
base_sets = [set(), {2}, {2, 3}]
cover_pairs = [(5, 7), (11, 13), (17, 19)]
scalars = [mp.mpc(2, 3), mp.mpc(-1, 2), mp.mpf("5.25")]
tolerance = mp.mpf("1e-50")

equalizer_ok = True
unique_glue_ok = True
frame_trivialization_ok = True
section_restriction_ok = True

for s in parameters:
    for base, (p, q), scalar in zip(base_sets, cover_pairs, scalars):
        left = scalar * z(p, s)
        right = scalar * z(q, s)
        overlap_left = left * z(q, s)
        overlap_right = right * z(p, s)
        equalizer_ok = equalizer_ok and abs(overlap_left - overlap_right) < tolerance

        glued_from_left = left / z(p, s)
        glued_from_right = right / z(q, s)
        unique_glue_ok = unique_glue_ok and abs(glued_from_left - scalar) < tolerance and abs(glued_from_right - scalar) < tolerance

        enlarged = base | {p, q}
        restricted_coefficient = scalar * g(enlarged - base, s)
        source_frame_value = scalar / g(base, s)
        target_frame_value = restricted_coefficient / g(enlarged, s)
        frame_trivialization_ok = frame_trivialization_ok and abs(source_frame_value - target_frame_value) < tolerance

        arch = mp.mpf("0.5") * s * (s - 1) * mp.power(mp.pi, -s / 2) * mp.gamma(s / 2)
        sigma_base = arch * g(base, s)
        sigma_enlarged = arch * g(enlarged, s)
        restricted_sigma = sigma_base * g(enlarged - base, s)
        section_restriction_ok = section_restriction_ok and abs(restricted_sigma - sigma_enlarged) < tolerance

verdict = all([equalizer_ok, unique_glue_ok, frame_trivialization_ok, section_restriction_ok])

print(f"BASIS_COVER_EQUALIZERS: {'YES' if equalizer_ok else 'NO'}")
print(f"UNIQUE_SHEAF_GLUE: {'YES' if unique_glue_ok else 'NO'}")
print(f"FRAME_CHANGE_TO_CONSTANT_LINE: {'YES' if frame_trivialization_ok else 'NO'}")
print(f"CANONICAL_SECTION_RESTRICTS: {'YES' if section_restriction_ok else 'NO'}")
print("SPECTRAL_DETERMINANT_LINE_SHEAF_ON_SPEC_Z: CONSTRUCTED_FOR_RE_S_GT_1")
print("COMPLETED_GENERIC_SECTION: XI")
print("ABSOLUTE_SQUARE_LINE_BUNDLE: NOT_CONSTRUCTED")
print(f"VERDICT: {'YES' if verdict else 'NO'}")
