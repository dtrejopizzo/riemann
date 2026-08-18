#!/usr/bin/env python3
"""Checks for 104_78 (diagnostic; the proofs are in the document)."""

from fractions import Fraction
import math
import numpy as np


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def mobius(n):
    x = n
    primes = 0
    p = 2
    while p * p <= x:
        if x % p == 0:
            x //= p
            primes += 1
            if x % p == 0:
                return 0
            while x % p == 0:
                x //= p
        p += 1
    if x > 1:
        primes += 1
    return -1 if primes % 2 else 1


def necklace(d, alphabet):
    value = sum(mobius(e) * alphabet ** (d // e) for e in divisors(d))
    assert value % d == 0
    return value // d


def prime_multiplicity(d):
    return necklace(d, 6) + necklace(d, 1) - necklace(d, 3) - necklace(d, 2)


def check_necklaces(limit=50):
    for k in range(1, limit + 1):
        pi_k = prime_multiplicity(k)
        assert pi_k >= 0
        psi = sum(d * prime_multiplicity(d) for d in divisors(k))
        assert psi == 6**k + 1 - 3**k - 2**k


def zeta_of_t(t):
    return ((1 - 3 * t) * (1 - 2 * t)) / ((1 - t) * (1 - 6 * t))


def check_functional_equation():
    for t in (Fraction(1, 7), Fraction(2, 13), Fraction(3, 20), Fraction(5, 17)):
        if t in (Fraction(1, 6), Fraction(1, 1)):
            continue
        assert zeta_of_t(t) == zeta_of_t(1 / (6 * t))


def check_unit_renewal():
    # A formal integer is represented by (degree, exponent) pairs.
    samples = [
        [(1, 3)],
        [(2, 1), (5, 4)],
        [(3, 2), (7, 1), (11, 3)],
    ]
    for factors in samples:
        total_degree = sum(degree * exponent for degree, exponent in factors)
        marked_degree = sum(
            sum(degree for _ in range(1, exponent + 1))
            for degree, exponent in factors
        )
        assert marked_degree == total_degree


def degree_chebyshev(k):
    """Actual Mangoldt mass up to norm 6**k (including log 6)."""
    return math.log(6.0) * sum(6**j + 1 - 3**j - 2**j for j in range(1, k + 1))


def check_continuous_pnt_failure():
    # At a lattice point the ratio tends to 6 log(6)/5. Immediately before
    # the following lattice point it tends to log(6)/5, so psi(x)/x has no
    # limit.  This guards the precise scope of the falsifier.
    k = 50
    upper_endpoint_ratio = degree_chebyshev(k) / 6**k
    next_left_ratio = degree_chebyshev(k) / 6 ** (k + 1)
    assert abs(upper_endpoint_ratio - 6 * math.log(6.0) / 5) < 1e-12
    assert abs(next_left_ratio - math.log(6.0) / 5) < 1e-12
    assert abs(upper_endpoint_ratio - next_left_ratio) > 1.0


def check_li_dominant_mode():
    q, a, b = 6.0, 3.0, 2.0
    h = math.log(q)
    beta = math.log(a) / h
    w0 = 1.0 - 1.0 / beta
    r_growth = 1.0 / abs(w0)
    assert beta > 0.5
    assert abs((1.0 - beta) - math.log(b) / h) < 1e-14
    assert abs(w0 + math.log(2.0) / math.log(3.0)) < 1e-14
    assert abs(r_growth - math.log(3.0) / math.log(2.0)) < 1e-14

    # Cauchy extraction of G(z)=z d/dz log Xi(1/(1-z)).
    radius = 0.55
    count = 32768
    j = np.arange(count)
    z = radius * np.exp(2j * np.pi * j / count)
    s = 1.0 / (1.0 - z)
    t = np.exp(-h * s)
    dlog_xi = h + h * a * t / (1.0 - a * t) + h * b * t / (1.0 - b * t)
    generating = z * dlog_xi / (1.0 - z) ** 2
    coeff = np.fft.fft(generating) / count
    for n in (20, 30, 40, 50):
        lam = (coeff[n] / radius**n).real
        dominant = -(w0 ** (-n))
        assert abs(lam / dominant - 1.0) < 0.01
        assert lam < 0  # all selected n are even


def harmonic(n):
    return sum(1.0 / k for k in range(1, n + 1))


def deep_density_model(x):
    log_r = math.log(math.log(3.0) / math.log(2.0))
    threshold = math.ceil(math.sqrt(x) / log_r)
    mass = sum(1.0 / n for n in range(max(2, threshold), x + 1) if n % 2 == 0)
    return mass / harmonic(x)


def check_deep_density():
    values = [deep_density_model(x) for x in (10_000, 100_000, 1_000_000)]
    assert values[0] < values[1] < values[2] < 0.25
    # Convergence is logarithmic because the normalization is H_X.
    assert abs(values[-1] - 0.25) < 0.04


def main():
    check_necklaces()
    check_functional_equation()
    check_unit_renewal()
    check_continuous_pnt_failure()
    check_li_dominant_mode()
    check_deep_density()
    print("104_78 checker: PASS")
    print("pi_1..pi_8 =", [prime_multiplicity(d) for d in range(1, 9)])
    print("deep densities =", [round(deep_density_model(x), 6) for x in (10_000, 100_000, 1_000_000)])


if __name__ == "__main__":
    main()
