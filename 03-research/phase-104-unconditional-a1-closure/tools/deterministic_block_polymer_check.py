#!/usr/bin/env python3
"""Exact finite algebra for 104_68 (stdlib only)."""

from fractions import Fraction
from math import exp, log


def interval(leng: int) -> range:
    return range(leng * leng, leng * leng + leng)


def quartet(n: int) -> Fraction:
    if n % 2:
        return Fraction(4)
    magnitude = Fraction(2 ** n) + Fraction(1, 2 ** n)
    if n % 4 == 0:
        return Fraction(4) - 2 * magnitude
    return Fraction(4) + 2 * magnitude


def product(values: list[Fraction]) -> Fraction:
    out = Fraction(1)
    for value in values:
        out *= value
    return out


def subset_partition(activities: list[Fraction]) -> Fraction:
    total = Fraction(0)
    count = len(activities)
    for mask in range(1 << count):
        monomial = Fraction(1)
        for j, activity in enumerate(activities):
            if mask & (1 << j):
                monomial *= activity
        total += monomial
    return total


def main() -> None:
    # RH model lambda_n=0: a_n=1/(n+2), z_n=1/(n+1).
    for leng in range(2, 31):
        indices = list(interval(leng))
        a = [Fraction(1, n + 2) for n in indices]
        z = [Fraction(1, n + 1) for n in indices]
        sum_a = sum(a, Fraction(0))
        sum_z = sum(z, Fraction(0))
        p = product([1 - value for value in a])
        assert sum_a <= Fraction(leng, leng * leng + 2)
        assert sum_z <= Fraction(1, leng)
        assert 1 - sum_a <= p <= 1
        assert p == 1 / product([1 + value for value in z])

    # Polymer expansion and logistic identities for arbitrary rational sites.
    activities = [Fraction(1, 3), Fraction(2, 5), Fraction(7, 11),
                  Fraction(5, 13), Fraction(4, 17)]
    a = [z / (1 + z) for z in activities]
    p = product([1 - value for value in a])
    partition_product = product([1 + z for z in activities])
    partition_subsets = subset_partition(activities)
    assert partition_product == partition_subsets
    assert p == 1 / partition_product
    assert 1 - sum(a, Fraction(0)) <= p <= 1
    for z in activities:
        assert z <= partition_product - 1

    # Product telescoping bound used by the single diagonal (25d).
    left = [Fraction(1, 5), Fraction(2, 7), Fraction(3, 8)]
    right = [Fraction(1, 4), Fraction(1, 3), Fraction(4, 9)]
    assert abs(product(left) - product(right)) <= sum(
        (abs(x - y) for x, y in zip(left, right)), Fraction(0)
    )

    eta = 0.01 - log(200.0 / 199.0)
    assert eta > 0.0
    diagonal_envelopes = []
    for leng in (10, 20, 50, 100):
        nmax = leng * leng + leng - 1
        envelope = leng * nmax * exp(-eta * nmax)
        diagonal_envelopes.append(envelope)
    # The envelope need not be monotone before its asymptotic regime.
    assert diagonal_envelopes[-2] < 1
    assert diagonal_envelopes[-1] < Fraction(1, 10**12)

    # Every deterministic window of length >=4 sees n == 0 mod 4.
    for leng in range(4, 101):
        indices = list(interval(leng))
        bad = [n for n in indices if n % 4 == 0]
        assert bad
        d = bad[0]
        assert quartet(d) < -1
        assert -quartet(d) >= 2 ** d

    # A few exact displayed values, without constructing exp(2^d).
    for leng in (4, 5, 10, 25, 100):
        d = next(n for n in interval(leng) if n % 4 == 0)
        print(
            f"L={leng:3d} first_bad={d:5d} "
            f"rate_exponent_lower=2^{d}"
        )

    print("deterministic_block_polymer_check: PASS")


if __name__ == "__main__":
    main()
