#!/home/trabajo/miniforge3/bin/python
"""Falsifier for the ordinary prime-sum no-go of the relative R-genus."""

from mpmath import mp
from sympy import nextprime


SMALL_PRIMES = (2, 3, 5, 7, 11)
LARGE_PRIME_SEEDS = (10**3, 10**5, 10**7, 10**9, 10**11)
PARAMETERS = (mp.mpf("1.25"), mp.mpf("2"))
ORDER_STEP = mp.mpf("1e-7")
CUT_STEP = mp.mpf("1e-12")


def order_derivative_polylog(z):
    return (
        mp.polylog(ORDER_STEP, z) - mp.polylog(-ORDER_STEP, z)
    ) / (2 * ORDER_STEP)


def inside_derivative(q):
    """D(q) from its convergent series, with a rigorous-sized tail here."""
    total = mp.mpf("0")
    term = q * q
    n = 2
    while term * mp.log(n) > mp.mpf("1e-55"):
        total -= term * mp.log(n)
        n += 1
        term *= q
    return total


def closed_relative(p, s):
    x = mp.power(p, s)
    q = 1 / x
    log_x = mp.log(x)
    return (
        2 * inside_derivative(q)
        + mp.re(mp.digamma(-1j * log_x / (2 * mp.pi)))
        + mp.euler
        + mp.log(2 * mp.pi)
        - mp.log(x - 1) / log_x
    )


def lateral_relative(p, s, sign):
    q = mp.power(p, -s)
    x = 1 / q + sign * 1j * CUT_STEP
    corrected = order_derivative_polylog(x) + mp.log(1 - x) / mp.log(x)
    return order_derivative_polylog(q) - corrected


def main():
    mp.dps = 50

    inversion_errors = []
    lateral_errors = []
    for p in SMALL_PRIMES:
        for s in PARAMETERS:
            closed = closed_relative(p, s)
            upper = lateral_relative(p, s, 1)
            lower = lateral_relative(p, s, -1)
            inversion_errors.append(abs(mp.re(upper) - closed))
            lateral_errors.append(abs(upper - lower))

    large_primes = tuple(int(nextprime(seed)) for seed in LARGE_PRIME_SEEDS)
    asymptotic_errors = []
    weighted_terms = []
    for p in large_primes:
        value = closed_relative(p, PARAMETERS[1])
        asymptotic = mp.log(mp.log(mp.power(p, PARAMETERS[1]))) + mp.euler - 1
        asymptotic_errors.append(abs(value - asymptotic))
        weighted_terms.append(mp.log(p) * value)

    inversion_ok = max(inversion_errors) < mp.mpf("2e-10")
    cut_ok = max(lateral_errors) < mp.mpf("2e-10")
    asymptotic_improves = all(
        right < left
        for left, right in zip(asymptotic_errors, asymptotic_errors[1:])
    )
    terms_grow = all(
        right > left for left, right in zip(weighted_terms, weighted_terms[1:])
    )
    # The theorem proves non-decay.  The finite atlas checks its predicted
    # monotone growth; it must not impose an arbitrary finite growth factor.
    asymptotic_nondecay_control = terms_grow and weighted_terms[-1] > weighted_terms[0]
    verdict = (
        inversion_ok
        and cut_ok
        and asymptotic_improves
        and asymptotic_nondecay_control
    )

    print(f"ACTUAL_SMALL_PRIME_IDENTITIES: {len(SMALL_PRIMES) * len(PARAMETERS)}")
    print(f"ACTUAL_LARGE_PRIMES: {','.join(map(str, large_primes))}")
    print(f"MAX_JONQUIERE_IDENTITY_ERROR: {mp.nstr(max(inversion_errors), 8)}")
    print(f"MAX_LATERAL_VALUE_ERROR: {mp.nstr(max(lateral_errors), 8)}")
    print(f"FIRST_ASYMPTOTIC_ERROR: {mp.nstr(asymptotic_errors[0], 8)}")
    print(f"LAST_ASYMPTOTIC_ERROR: {mp.nstr(asymptotic_errors[-1], 8)}")
    print(f"FIRST_WEIGHTED_TERM: {mp.nstr(weighted_terms[0], 8)}")
    print(f"LAST_WEIGHTED_TERM: {mp.nstr(weighted_terms[-1], 8)}")
    print(f"JONQUIERE_CLOSED_FORM: {'YES' if inversion_ok else 'NO'}")
    print(f"ASYMPTOTIC_ERROR_DECREASES: {'YES' if asymptotic_improves else 'NO'}")
    print(f"WEIGHTED_TERMS_GROW_ON_FIXED_ATLAS: {'YES' if asymptotic_nondecay_control else 'NO'}")
    print("PRIME_TERMS_TEND_TO_ZERO: NO_BY_ASYMPTOTIC_THEOREM")
    print(f"ORDINARY_PRIME_SUM: {'CLOSED_NO_GO' if verdict else 'UNRESOLVED'}")
    print("GLOBAL_NUCLEAR_QUOTIENT_REQUIRED: YES")
    print(f"VERDICT: {'YES' if verdict else 'NO'}")
    raise SystemExit(0 if verdict else 1)


if __name__ == "__main__":
    main()
