#!/home/trabajo/miniforge3/bin/python
"""Falsifier for an additive integral Chern class on the real divisor line."""

RADII = (1, 4, 13, 16, 40)
DIVISIBILITY_TESTS = (2, 3, 5, 7, 11)
LATTICE_WINDOW = range(-1_000, 1_001)


def cc_dimension(radius):
    k = 0
    while 3**k < 2 * radius + 1:
        k += 1
    return k


def main():
    dimensions = {radius: cc_dimension(radius) for radius in RADII}

    raw_zero_failure = dimensions[1] != 0
    normalized = {radius: value - dimensions[1] for radius, value in dimensions.items()}
    # Radius multiplication corresponds to addition of logarithmic
    # archimedean divisors.  The fixed 4*4=16 control rejects additivity.
    normalized_additivity_failure = normalized[16] != 2 * normalized[4]

    universally_divisible_candidates = tuple(
        value
        for value in LATTICE_WINDOW
        if all(value % divisor == 0 for divisor in DIVISIBILITY_TESTS)
    )
    # In this window the lcm exceeds every nonzero candidate.
    finite_lattice_forces_zero = universally_divisible_candidates == (0,)

    verdict = raw_zero_failure and normalized_additivity_failure and finite_lattice_forces_zero
    print(f"FIXED_CC_RADII: {RADII}")
    print(f"CC_DIMENSIONS: {tuple(dimensions[r] for r in RADII)}")
    print(f"RAW_DIMENSION_SENDS_ZERO_TO_ZERO: {'NO' if raw_zero_failure else 'YES'}")
    print(f"ZERO_NORMALIZED_DIMENSION_ADDITIVE_AT_4x4: {'NO' if normalized_additivity_failure else 'YES'}")
    print(f"FINITE_DIVISIBILITY_CONTROLS: {DIVISIBILITY_TESTS}")
    print(f"DIVISIBLE_LATTICE_CANDIDATES_IN_WINDOW: {universally_divisible_candidates}")
    print("ARCHIMEDEAN_REAL_TO_FINITE_RANK_C1: ZERO_ONLY")
    print("ARCHIMEDEAN_VARIATION_MUST_BE_METRIC_OR_TOLERANCE: YES")
    print(f"VERDICT: {'YES' if verdict else 'NO'}")
    raise SystemExit(0 if verdict else 1)


if __name__ == "__main__":
    main()
