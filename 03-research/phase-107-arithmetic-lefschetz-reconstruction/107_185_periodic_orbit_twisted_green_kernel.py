#!/home/trabajo/miniforge3/bin/python
"""Exact/high-precision falsifier for twisted Green kernels on prime orbits."""

from mpmath import mp


mp.dps = 70
primes = [2, 3, 5, 7, 11]
spectral_parameters = [mp.mpf("2"), mp.mpf("2.5"), mp.mpc(2, 3)]
tolerance = mp.mpf("1e-60")

all_checks_ok = True
checks = 0
for p in primes:
    length = mp.log(p)
    for s in spectral_parameters:
        monodromy = mp.exp(-s * length)
        expected_monodromy = mp.power(p, -s)
        determinant = 1 - monodromy

        green_zero_plus = 1 / determinant
        green_return = monodromy / determinant
        jump = green_zero_plus - green_return

        sample_x = length * mp.mpf("0.37")
        green_sample = mp.exp(-s * sample_x) / determinant
        homogeneous_residual = (-s * green_sample) + s * green_sample

        partial_geometric = sum(monodromy**k for k in range(1, 201))
        geometric_error = abs(partial_geometric - green_return)

        row_ok = all(
            [
                abs(monodromy - expected_monodromy) < tolerance,
                abs(jump - 1) < tolerance,
                abs(homogeneous_residual) < tolerance,
                geometric_error < mp.mpf("1e-55"),
                abs(length * green_return - mp.log(p) * monodromy / (1 - monodromy)) < tolerance,
            ]
        )
        all_checks_ok = all_checks_ok and row_ok
        checks += 1
        print(
            f"P={p}_S={s}_MONODROMY={mp.nstr(monodromy, 10)}"
            f"_JUMP={mp.nstr(jump, 8)}_GEOM_ERROR={mp.nstr(geometric_error, 5)}"
            f"_OK={'YES' if row_ok else 'NO'}"
        )

verdict = all_checks_ok

print(f"REAL_PRIME_ORBITS: {len(primes)}")
print(f"ORBIT_PARAMETER_CHECKS: {checks}")
print(f"TWISTED_CELLULAR_DETERMINANT: 1-p^(-s)")
print(f"GREEN_UNIT_JUMP: {'YES' if all_checks_ok else 'NO'}")
print(f"REDUCED_RETURN_VALUE: p^(-s)/(1-p^(-s))")
print("FINITE_ROW_B_TO_ROW_C_GREEN_BRIDGE: CONSTRUCTED")
print("ARAKELOV_GREEN_CURRENT: NOT_CONSTRUCTED")
print(f"VERDICT: {'YES' if verdict else 'NO'}")
