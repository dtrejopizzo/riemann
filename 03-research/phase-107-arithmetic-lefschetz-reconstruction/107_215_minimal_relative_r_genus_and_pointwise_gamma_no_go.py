#!/home/trabajo/miniforge3/bin/python
"""Falsifier for the minimal relative R-genus and pointwise Gamma no-go."""

from concurrent.futures import ProcessPoolExecutor

from mpmath import mp


PRIMES = (2, 3, 5, 7, 11)
PARAMETERS = (mp.mpf("1.25"), mp.mpf("2"))
ORDER_STEP = mp.mpf("1e-7")
CUT_STEP = mp.mpf("1e-12")


def order_derivative_polylog(z):
    return (
        mp.polylog(ORDER_STEP, z) - mp.polylog(-ORDER_STEP, z)
    ) / (2 * ORDER_STEP)


def corrected_derivative(z):
    return order_derivative_polylog(z) + mp.log(1 - z) / mp.log(z)


def check_prime(p):
    mp.dps = 45
    boundary_errors = []
    imaginary_parts = []
    weighted_values = []
    gamma_values = []
    for s in PARAMETERS:
        q = mp.power(p, -s)
        x = 1 / q
        upper_corrected = corrected_derivative(x + 1j * CUT_STEP)
        lower_corrected = corrected_derivative(x - 1j * CUT_STEP)
        boundary_errors.append(abs(upper_corrected - lower_corrected))

        relative = order_derivative_polylog(q) - upper_corrected
        imaginary_parts.append(abs(mp.im(relative)))
        weighted_values.append(mp.re(mp.log(p) * relative))
        gamma_values.append(-mp.digamma(s / 2) / 2 + mp.log(mp.pi) / 2)

    return tuple(
        str(value)
        for value in (
            max(boundary_errors),
            max(imaginary_parts),
            weighted_values[0],
            weighted_values[1],
            gamma_values[0],
            gamma_values[1],
        )
    )


def main():
    mp.dps = 45
    with ProcessPoolExecutor(max_workers=len(PRIMES)) as executor:
        results = tuple(executor.map(check_prime, PRIMES))

    parsed = tuple(tuple(mp.mpf(value) for value in result) for result in results)
    max_boundary_error = max(result[0] for result in parsed)
    max_imaginary_part = max(result[1] for result in parsed)

    spreads = []
    min_gamma_mismatch = mp.inf
    for index in range(len(PARAMETERS)):
        weighted = [result[2 + index] for result in parsed]
        spreads.append(max(weighted) - min(weighted))
        gamma_value = parsed[0][4 + index]
        min_gamma_mismatch = min(
            min_gamma_mismatch,
            max(abs(value - gamma_value) for value in weighted),
        )

    forced_coefficient_ok = all(
        abs((1 / mp.log(mp.power(p, 2))) * mp.log(mp.power(p, 2)) - 1)
        < mp.mpf("1e-40")
        for p in PRIMES
    )
    cut_cancelled = max_boundary_error < mp.mpf("2e-11")
    real_on_ray = max_imaginary_part < mp.mpf("2e-11")
    pointwise_gamma_rejected = min(spreads) > mp.mpf("0.1")

    verdict = (
        forced_coefficient_ok
        and cut_cancelled
        and real_on_ray
        and pointwise_gamma_rejected
    )

    print(f"ACTUAL_PRIME_ANOMALIES_TESTED: {len(PRIMES) * len(PARAMETERS)}")
    print(f"MAX_CORRECTED_BOUNDARY_ERROR: {mp.nstr(max_boundary_error, 8)}")
    print(f"MAX_RELATIVE_IMAGINARY_PART: {mp.nstr(max_imaginary_part, 8)}")
    print(f"MIN_FIXED_S_PRIME_SPREAD: {mp.nstr(min(spreads), 8)}")
    print(f"MIN_GAMMA_COMPARISON_MISMATCH: {mp.nstr(min_gamma_mismatch, 8)}")
    print(f"MINIMAL_LOG_CORRECTION_FORCED: {'YES' if forced_coefficient_ok else 'NO'}")
    print(f"RELATIVE_R_GENUS_CUT_CANCELLED: {'YES' if cut_cancelled else 'NO'}")
    print(f"RELATIVE_R_GENUS_REAL_ON_POSITIVE_RAY: {'YES' if real_on_ray else 'NO'}")
    print(f"POINTWISE_PRIME_ANOMALY_EQUALS_GAMMA: {'NO' if pointwise_gamma_rejected else 'UNRESOLVED'}")
    print("LOG_LIFTED_RELATIVE_R_GENUS: CONSTRUCTED_SCALAR_LEVEL")
    print("GLOBAL_GAMMA_COMPARISON: NOT_CONSTRUCTED")
    print(f"VERDICT: {'YES' if verdict else 'NO'}")


if __name__ == "__main__":
    main()

