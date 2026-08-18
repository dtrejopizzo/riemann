#!/usr/bin/env python3
"""Exact finite checks for 104_99.

The theorem is analytic.  This program only guards its finite algebra:
Legendre--Eratosthenes, the signed remainder, and the Liouville parity
identity.  All identities below use Python integers/Fraction.
"""

from fractions import Fraction
from math import isqrt


LIMIT = 300


def arithmetic_tables(limit: int):
    prime = [True] * (limit + 1)
    prime[0] = prime[1] = False
    for p in range(2, isqrt(limit) + 1):
        if prime[p]:
            for n in range(p * p, limit + 1, p):
                prime[n] = False

    primes = [n for n in range(2, limit + 1) if prime[n]]
    pi = [0] * (limit + 1)
    mu = [1] * (limit + 1)
    liouville = [1] * (limit + 1)
    largest_prime = [1] * (limit + 1)
    for n in range(2, limit + 1):
        pi[n] = pi[n - 1] + int(prime[n])
    for p in primes:
        for n in range(p, limit + 1, p):
            mu[n] *= -1
            liouville[n] *= -1
            largest_prime[n] = p
        pp = p * p
        for n in range(pp, limit + 1, pp):
            mu[n] = 0
        power = pp
        while power <= limit:
            # The first factor p was already inserted above.  Every
            # additional exponent flips Liouville once more.
            for n in range(power, limit + 1, power):
                liouville[n] *= -1
            if power > limit // p:
                break
            power *= p

    # Recompute Liouville independently through the smallest factor.
    lpf = list(range(limit + 1))
    for p in primes:
        for n in range(p, limit + 1, p):
            if lpf[n] == n:
                lpf[n] = p
    liouville2 = [1] * (limit + 1)
    for n in range(2, limit + 1):
        liouville2[n] = -liouville2[n // lpf[n]]
    assert liouville == liouville2

    L = [0] * (limit + 1)
    for n in range(1, limit + 1):
        L[n] = L[n - 1] + liouville[n]
    return prime, primes, pi, mu, liouville, largest_prime, L


def divisors_of_primorial(primes, z: int):
    divisors = [(1, 1)]
    for p in primes:
        if p > z:
            break
        divisors += [(p * d, -mu_d) for d, mu_d in divisors]
    return sorted(divisors)


def main():
    prime, primes, pi, mu, lam, largest_prime, L = arithmetic_tables(LIMIT)

    max_identity_error = 0
    for x in range(2, LIMIT + 1):
        z = isqrt(x)
        divisor_data = divisors_of_primorial(primes, z)
        ds = [d for d, _ in divisor_data]

        phi_ie = sum(mu_d * (x // d) for d, mu_d in divisor_data)
        phi_direct = sum(
            1
            for n in range(1, x + 1)
            if all(n % p for p in primes if p <= z)
        )
        assert phi_ie == phi_direct == 1 + pi[x] - pi[z]

        v = Fraction(1, 1)
        for p in primes:
            if p > z:
                break
            v *= Fraction(p - 1, p)
        r_e = sum(
            Fraction(mu_d, 1) * (Fraction(x // d, 1) - Fraction(x, d))
            for d, mu_d in divisor_data
        )
        assert Fraction(phi_ie, 1) == Fraction(x, 1) * v + r_e
        assert Fraction(pi[x], 1) == (
            Fraction(pi[z] - 1, 1) + Fraction(x, 1) * v + r_e
        )

        t = sum(L[x // d] for d in ds)
        parity_rhs = 1 + pi[z] - pi[x]
        max_identity_error = max(max_identity_error, abs(t - parity_rhs))
        assert t == parity_rhs

        # Divisibility data a^+ and a^- and their exact sieved masses.
        a_plus = [0] + [1 + lam[n] for n in range(1, x + 1)]
        a_minus = [0] + [1 - lam[n] for n in range(1, x + 1)]
        s_plus = 0
        s_minus = 0
        for n in range(1, x + 1):
            if all(n % p for p in primes if p <= z):
                s_plus += a_plus[n]
                s_minus += a_minus[n]
        assert s_plus == 2
        assert s_minus == 2 * (pi[x] - pi[z])

        s_plus_ie = 0
        s_minus_ie = 0
        for d, mu_d in divisor_data:
            ad_plus = sum(a_plus[n] for n in range(d, x + 1, d))
            ad_minus = sum(a_minus[n] for n in range(d, x + 1, d))
            # If d>x the two divisor sums and L(floor(x/d)) are zero.
            lam_d = mu_d  # every d here is squarefree
            assert ad_plus == x // d + lam_d * L[x // d]
            assert ad_minus == x // d - lam_d * L[x // d]
            s_plus_ie += mu_d * ad_plus
            s_minus_ie += mu_d * ad_minus
        assert s_plus_ie == s_plus
        assert s_minus_ie == s_minus

    print("ERATOSTHENES / PARITY EXACT CHECK")
    print(f"range: 2 <= x <= {LIMIT}")
    print(f"max error in sum_d L(floor(x/d)) identity: {max_identity_error}")
    print()
    print("x   D       l1 data difference d<=D   full sifted gap")
    for x in (30, 60, 120, 210, 300):
        for exponent_label, D in (("1/2", isqrt(x)), ("3/4", int(x ** 0.75)), ("1", x)):
            data_gap = 0
            for d in range(1, D + 1):
                data_gap += 2 * abs(L[x // d])
            z = isqrt(x)
            sifted_gap = 2 * (pi[x] - pi[z] - 1)
            print(f"{x:<3d} {exponent_label:>3s} {data_gap:>27d} {sifted_gap:>18d}")
        print()

    print("PASS: all finite identities are exact.")


if __name__ == "__main__":
    main()
