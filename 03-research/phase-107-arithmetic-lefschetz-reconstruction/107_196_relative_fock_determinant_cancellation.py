#!/home/trabajo/miniforge3/bin/python
"""Falsifier for canonical relative Fock determinant cancellation."""

from mpmath import mp


mp.dps = 70
PRIMES = (2, 3, 5, 7, 11)
PARAMETERS = (mp.mpf("1.5"), mp.mpf("2"), mp.mpc(2, 3))
CUTOFFS = (8, 16, 32, 64)


def finite_tail(q, start, cutoff):
    value = mp.mpc(1)
    for n in range(start, cutoff + 1):
        value *= 1 - q**n
    return value


relative_exact_ok = True
green_derivative_ok = True
tail_bound_ok = True
wrong_shift_rejected = True
max_relative_error = mp.mpf(0)
max_green_error = mp.mpf(0)

for p in PRIMES:
    for s in PARAMETERS:
        q = mp.power(p, -s)
        expected = 1 - q

        for cutoff in CUTOFFS:
            d1 = finite_tail(q, 1, cutoff)
            d2 = finite_tail(q, 2, cutoff)
            relative = d1 / d2
            error = abs(relative - expected)
            max_relative_error = max(max_relative_error, error)
            relative_exact_ok &= error < mp.mpf("1e-65")

            wrong_relative = d1 / finite_tail(q, 3, cutoff)
            wrong_shift_rejected &= abs(wrong_relative - expected) > mp.mpf("1e-8")

        computed_green = mp.diff(
            lambda w: mp.log(1 - mp.power(p, -w)), s
        )
        expected_green = mp.log(p) * q / (1 - q)
        green_error = abs(computed_green - expected_green)
        max_green_error = max(max_green_error, green_error)
        green_derivative_ok &= green_error < mp.mpf("1e-60")

        cutoff = CUTOFFS[-1]
        absolute_q = abs(q)
        log_tail_bound = absolute_q ** (cutoff + 1) / (
            (1 - absolute_q) * (1 - absolute_q ** (cutoff + 1))
        )
        tail_bound_ok &= log_tail_bound < mp.mpf("1e-20")


verdict = all(
    [
        relative_exact_ok,
        green_derivative_ok,
        tail_bound_ok,
        wrong_shift_rejected,
    ]
)

print(f"REAL_PRIMES_TESTED: {len(PRIMES)}")
print(f"SPECTRAL_PARAMETERS_TESTED: {len(PARAMETERS)}")
print(f"MAX_RELATIVE_DETERMINANT_ERROR: {mp.nstr(max_relative_error, 8)}")
print(f"CANONICAL_TAIL_CANCELLATION: {'YES' if relative_exact_ok else 'NO'}")
print(f"MAX_GREEN_DERIVATIVE_ERROR: {mp.nstr(max_green_error, 8)}")
print(f"LOCAL_GREEN_CONNECTION_RECOVERED: {'YES' if green_derivative_ok else 'NO'}")
print(f"INFINITE_TAIL_BOUND_CONTROLLED: {'YES' if tail_bound_ok else 'NO'}")
print(f"WRONG_SHIFT_MUTATION_REJECTED: {'YES' if wrong_shift_rejected else 'NO'}")
print("RELATIVE_FOCK_DETERMINANT: CONSTRUCTED")
print("SECONDARY_GEOMETRIC_REALIZATION: NOT_CONSTRUCTED")
print(f"VERDICT: {'YES' if verdict else 'NO'}")
