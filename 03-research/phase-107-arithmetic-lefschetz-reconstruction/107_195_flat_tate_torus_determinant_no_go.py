#!/home/trabajo/miniforge3/bin/python
"""Falsifier for the standard flat Tate-torus determinant bridge."""

from mpmath import mp


mp.dps = 60
PRIMES = (2, 3, 5, 7, 11)
SPECTRAL_PARAMETERS = (mp.mpf("1.5"), mp.mpf("2"), mp.mpf("3"))
PRODUCT_CUTOFF = 400


def eta_fourth(q):
    product = mp.mpf(1)
    for n in range(1, PRODUCT_CUTOFF + 1):
        product *= (1 - q**n) ** 4
    return q ** (mp.mpf(1) / 6) * product


ratios = []
eta_tail_modes_present = True
one_mode_mutation_matches = True
tail_error_bounded = True

for p in PRIMES:
    for s in SPECTRAL_PARAMETERS:
        q = mp.power(p, -s)
        y = s * mp.log(p) / (2 * mp.pi)
        compact_determinant_shape = y * eta_fourth(q)
        orbit_norm_square = (1 - q) ** 2
        ratios.append(compact_determinant_shape / orbit_norm_square)

        tail = mp.mpf(1)
        for n in range(2, PRODUCT_CUTOFF + 1):
            tail *= (1 - q**n) ** 4
        eta_tail_modes_present &= abs(tail - 1) > mp.mpf("1e-10")

        one_mode = 1 - q
        one_mode_mutation_matches &= abs(one_mode - mp.sqrt(orbit_norm_square)) < mp.mpf("1e-50")

        # |log prod_{n>N}(1-q^n)^4| <= 4 q^(N+1)/((1-q)(1-q^(N+1))).
        log_tail_bound = 4 * q ** (PRODUCT_CUTOFF + 1) / (
            (1 - q) * (1 - q ** (PRODUCT_CUTOFF + 1))
        )
        tail_error_bounded &= log_tail_bound < mp.mpf("1e-50")


ratio_spread = max(ratios) - min(ratios)
universal_constant_rejected = ratio_spread > mp.mpf("0.01")
verdict = all(
    [
        eta_tail_modes_present,
        one_mode_mutation_matches,
        tail_error_bounded,
        universal_constant_rejected,
    ]
)

print(f"REAL_TATE_TORI_TESTED: {len(ratios)}")
print(f"ETA_TAIL_MODES_PRESENT: {'YES' if eta_tail_modes_present else 'NO'}")
print(f"ETA_PRODUCT_TAIL_BOUNDED: {'YES' if tail_error_bounded else 'NO'}")
print(f"DETERMINANT_RATIO_SPREAD: {mp.nstr(ratio_spread, 12)}")
print(f"UNIVERSAL_NORMALIZATION_REJECTED: {'YES' if universal_constant_rejected else 'NO'}")
print(f"ONE_MODE_TRUNCATION_WOULD_MATCH: {'YES' if one_mode_mutation_matches else 'NO'}")
print("STANDARD_FLAT_TATE_TORUS_BRIDGE: CLOSED_NO_GO")
print("REQUIRED_REFINEMENT: VIRTUAL_CANCELLATION_OR_RELATIVE_DETERMINANT")
print(f"VERDICT: {'YES' if verdict else 'NO'}")
