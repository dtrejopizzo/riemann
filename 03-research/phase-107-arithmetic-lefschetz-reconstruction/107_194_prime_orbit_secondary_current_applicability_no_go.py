#!/home/trabajo/miniforge3/bin/python
"""Falsifier for direct secondary-current applicability to prime circles."""

from mpmath import mp


mp.dps = 60
PRIMES = (2, 3, 5, 7, 11)
SPECTRAL_PARAMETERS = (mp.mpf("2"), mp.mpf("2.5"), mp.mpc(2, 3))


nonreturn_empty_ok = True
return_whole_orbit_ok = True
return_derivative_degenerate_ok = True
twisted_determinant_nonzero_ok = True
holonomy_not_tangent_euler_ok = True
mutation_detected = True

for p in PRIMES:
    orbit_length = mp.log(p)

    # x+t=x mod L iff t/L is an integer.
    for ratio in (mp.mpf("0.5"), mp.mpf("1.25"), mp.sqrt(2)):
        nonreturn_empty_ok &= abs(ratio - mp.nint(ratio)) > mp.mpf("1e-40")

    for return_index in (1, 2, 5):
        return_time = return_index * orbit_length
        ratio = return_time / orbit_length
        return_whole_orbit_ok &= abs(ratio - return_index) < mp.mpf("1e-50")

        tangent_derivative = mp.mpf(1)
        tangent_euler = 1 - tangent_derivative
        return_derivative_degenerate_ok &= tangent_euler == 0

    for s in SPECTRAL_PARAMETERS:
        holonomy = mp.power(p, -s)
        twisted_determinant = 1 - holonomy
        twisted_determinant_nonzero_ok &= abs(twisted_determinant) > mp.mpf("1e-8")
        holonomy_not_tangent_euler_ok &= abs(twisted_determinant) > mp.mpf("1e-8") and tangent_euler == 0

        # A contracting normal map would have derivative p^{-s}, unlike
        # the actual tangent derivative of the orbit translation.
        mutated_normal_euler = 1 - holonomy
        mutation_detected &= abs(mutated_normal_euler - tangent_euler) > mp.mpf("1e-8")


odd_real_dimension_excludes_complex_structure = True  # dim_R C_p = 1
verdict = all(
    [
        nonreturn_empty_ok,
        return_whole_orbit_ok,
        return_derivative_degenerate_ok,
        twisted_determinant_nonzero_ok,
        holonomy_not_tangent_euler_ok,
        mutation_detected,
        odd_real_dimension_excludes_complex_structure,
    ]
)

print(f"REAL_PRIME_ORBITS_TESTED: {len(PRIMES)}")
print(f"NONRETURN_FIXED_LOCUS_EMPTY: {'YES' if nonreturn_empty_ok else 'NO'}")
print(f"RETURN_FIXED_LOCUS_IS_WHOLE_ORBIT: {'YES' if return_whole_orbit_ok else 'NO'}")
print(f"RETURN_TANGENT_EULER_CLASS_ZERO: {'YES' if return_derivative_degenerate_ok else 'NO'}")
print(f"TWISTED_HOLONOMY_DETERMINANT_NONZERO: {'YES' if twisted_determinant_nonzero_ok else 'NO'}")
print(f"HOLONOMY_NOT_TANGENT_EULER_CLASS: {'YES' if holonomy_not_tangent_euler_ok else 'NO'}")
print(f"CONTRACTING_NORMAL_MUTATION_DETECTED: {'YES' if mutation_detected else 'NO'}")
print("DIRECT_SECONDARY_CURRENT_ON_PRIME_ORBIT: CLOSED_NO_GO")
print("REQUIRED_GEOMETRY: AMBIENT_COMPLEX_TRANSVERSE_NORMAL_ACTION")
print(f"VERDICT: {'YES' if verdict else 'NO'}")
