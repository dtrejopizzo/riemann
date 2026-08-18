#!/home/trabajo/miniforge3/bin/python
"""Falsifier for nonunitary R-genus monodromy and its logarithmic lift."""

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


def check_prime(p):
    mp.dps = 45
    max_disc_error = mp.mpf(0)
    max_weighted_error = mp.mpf(0)
    min_disc_size = mp.inf
    for s in PARAMETERS:
        x = mp.power(p, s)
        upper = order_derivative_polylog(x + 1j * CUT_STEP)
        lower = order_derivative_polylog(x - 1j * CUT_STEP)
        discontinuity = upper - lower
        expected = 2j * mp.pi / mp.log(x)

        max_disc_error = max(max_disc_error, abs(discontinuity - expected))
        min_disc_size = min(min_disc_size, abs(discontinuity))

        weighted = mp.log(p) * discontinuity
        weighted_expected = 2j * mp.pi / s
        max_weighted_error = max(
            max_weighted_error, abs(weighted - weighted_expected)
        )
    return str(max_disc_error), str(max_weighted_error), str(min_disc_size)


def main():
    mp.dps = 45
    with ProcessPoolExecutor(max_workers=len(PRIMES)) as executor:
        results = tuple(executor.map(check_prime, PRIMES))

    max_disc_error = max(mp.mpf(result[0]) for result in results)
    max_weighted_error = max(mp.mpf(result[1]) for result in results)
    min_disc_size = min(mp.mpf(result[2]) for result in results)

    disc_ok = max_disc_error < mp.mpf("2e-11")
    weighted_ok = max_weighted_error < mp.mpf("3e-11")
    monodromy_nonzero = min_disc_size > mp.mpf("0.5")
    verdict = disc_ok and weighted_ok and monodromy_nonzero

    print(f"ACTUAL_PRIME_LIFTS_TESTED: {len(PRIMES) * len(PARAMETERS)}")
    print(f"MAX_POLYLOG_DISCONTINUITY_ERROR: {mp.nstr(max_disc_error, 8)}")
    print(f"MAX_ARITHMETIC_WEIGHTED_ERROR: {mp.nstr(max_weighted_error, 8)}")
    print(f"MIN_NONZERO_MONODROMY: {mp.nstr(min_disc_size, 8)}")
    print(f"R_GENUS_SINGLE_VALUED_ON_CHARACTER_DISK: {'NO' if monodromy_nonzero else 'UNRESOLVED'}")
    print(f"LOG_P_WEIGHT_CANCELS_PRIME_DEPENDENCE: {'YES' if weighted_ok else 'NO'}")
    print("UNLIFTED_NONUNITARY_R_GENUS: CLOSED_NO_GO")
    print("LOG_LIFTED_RELATIVE_R_GENUS: OPEN")
    print("GLOBAL_WHITE_LIGHT_CANCELLATION: NOT_CONSTRUCTED")
    print(f"VERDICT: {'YES' if verdict else 'NO'}")


if __name__ == "__main__":
    main()
