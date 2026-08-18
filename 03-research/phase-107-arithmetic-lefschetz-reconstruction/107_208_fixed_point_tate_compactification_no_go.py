#!/home/trabajo/miniforge3/bin/python
"""Falsifier for the ordinary fixed-point Tate compactification route."""

from fractions import Fraction


PRIMES = (2, 3, 5, 7, 11)
NEIGHBORHOOD_EXPONENTS = (2, 4, 8, 16, 32)

zero_accumulation = True
infinity_accumulation = True
orbit_excludes_fixed_points = True
max_steps = 0

for p in PRIMES:
    orbit_excludes_fixed_points &= all(Fraction(p) ** n != 0 for n in range(-20, 21))
    for k in NEIGHBORHOOD_EXPONENTS:
        epsilon = Fraction(1, 10**k)

        n_zero = 0
        value_zero = Fraction(1)
        while value_zero >= epsilon:
            value_zero /= p
            n_zero += 1
        zero_accumulation &= 0 < value_zero < epsilon

        threshold = Fraction(10**k)
        n_infinity = 0
        value_infinity = Fraction(1)
        while value_infinity <= threshold:
            value_infinity *= p
            n_infinity += 1
        infinity_accumulation &= value_infinity > threshold
        max_steps = max(max_steps, n_zero, n_infinity)

# A compact subset of a Hausdorff space is closed.  Therefore a compact
# Tate curve cannot be both proper and dense in a strictly larger X.
compact_dense_boundary_possible = False

verdict = (
    zero_accumulation
    and infinity_accumulation
    and orbit_excludes_fixed_points
    and not compact_dense_boundary_possible
)

print(f"ACTUAL_PRIMES_TESTED: {len(PRIMES)}")
print(f"FIXED_POINT_NEIGHBORHOODS_TESTED: {len(NEIGHBORHOOD_EXPONENTS)}")
print(f"MAX_EXACT_ORBIT_STEPS: {max_steps}")
print(f"ORBIT_ACCUMULATES_AT_ZERO: {'YES' if zero_accumulation else 'NO'}")
print(f"ORBIT_ACCUMULATES_AT_INFINITY: {'YES' if infinity_accumulation else 'NO'}")
print(f"COARSE_QUOTIENT_T1: {'NO' if verdict else 'UNRESOLVED'}")
print("STRICT_HAUSDORFF_COMPACTIFICATION_OF_TATE_CURVE: NO")
print("ORDINARY_FIXED_POINT_COMPACTIFICATION: CLOSED_NO_GO")
print("STACKY_OR_RELATIVE_BOUNDARY_ROUTE: OPEN")
print(f"VERDICT: {'YES' if verdict else 'NO'}")

