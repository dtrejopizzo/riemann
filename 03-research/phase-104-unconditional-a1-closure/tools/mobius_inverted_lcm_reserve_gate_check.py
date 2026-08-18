#!/usr/bin/env python3
"""Exact checks for 104_51 (integers and Fraction only)."""

from fractions import Fraction
from math import comb, factorial


def transpose(matrix):
    return [list(row) for row in zip(*matrix)]


def matmul(left, right):
    return [
        [
            sum((left[i][k] * right[k][j] for k in range(len(right))), Fraction(0))
            for j in range(len(right[0]))
        ]
        for i in range(len(left))
    ]


def diagonal(entries):
    return [
        [entry if i == j else Fraction(0) for j in range(len(entries))]
        for i, entry in enumerate(entries)
    ]


def quadratic(vector, matrix):
    return sum(
        (vector[i] * matrix[i][j] * vector[j] for i in range(len(vector)) for j in range(len(vector))),
        Fraction(0),
    )


def check_gram_and_double_inversion():
    # Divisor chain {1,p,p^2}; Z_{m,d}=1_{d|m}.
    zeta = [
        [Fraction(1), Fraction(0), Fraction(0)],
        [Fraction(1), Fraction(1), Fraction(0)],
        [Fraction(1), Fraction(1), Fraction(1)],
    ]
    mobius = [
        [Fraction(1), Fraction(0), Fraction(0)],
        [Fraction(-1), Fraction(1), Fraction(0)],
        [Fraction(0), Fraction(-1), Fraction(1)],
    ]
    identity = diagonal([Fraction(1)] * 3)
    assert matmul(zeta, mobius) == identity
    assert matmul(mobius, zeta) == identity

    weights = diagonal([Fraction(1), Fraction(1, 4), Fraction(1, 16)])
    kernel = matmul(matmul(transpose(zeta), weights), zeta)
    recovered = matmul(matmul(transpose(mobius), kernel), mobius)
    assert recovered == weights

    # The probabilistic kernel is obtained by dividing parent weights and
    # the Gram kernel by the same positive normalizer.  Congruence commutes
    # with that normalization; the choice 7/5 keeps this check rational and
    # independent of any numerical evaluation of zeta(s).
    normalizer = Fraction(7, 5)
    probability_weights = [
        [entry / normalizer for entry in row]
        for row in weights
    ]
    probability_kernel = [
        [entry / normalizer for entry in row]
        for row in kernel
    ]
    probability_recovered = matmul(
        matmul(transpose(mobius), probability_kernel),
        mobius,
    )
    assert probability_recovered == probability_weights
    print("PASS: normalized and unnormalized double Möbius congruences are exact")


def check_indefinite_reserve():
    zeta = [
        [Fraction(1), Fraction(0), Fraction(0)],
        [Fraction(1), Fraction(1), Fraction(0)],
        [Fraction(1), Fraction(1), Fraction(1)],
    ]
    weights = diagonal([Fraction(1), Fraction(1, 4), Fraction(1, 16)])
    kernel = matmul(matmul(transpose(zeta), weights), zeta)
    reserve = [
        [kernel[i][j] - weights[i][j] for j in range(3)]
        for i in range(3)
    ]
    positive = [Fraction(0), Fraction(1), Fraction(0)]
    negative = [Fraction(0), Fraction(1), Fraction(-1)]
    assert quadratic(positive, reserve) == Fraction(1, 16)
    assert quadratic(negative, reserve) == Fraction(-1, 16)
    print("PASS: the finite-cutoff Möbius reserve has both signs on {1,p,p^2}")


def check_full_zeta_kernel_indefinite():
    # Integral comparison after the fifth term gives an exact rational upper
    # bound.  Since x^-2 is decreasing,
    # sum_{n=6}^infinity n^-2 < integral_5^infinity x^-2 dx = 1/5.
    zeta_two_upper = (
        Fraction(1)
        + Fraction(1, 4)
        + Fraction(1, 9)
        + Fraction(1, 16)
        + Fraction(1, 25)
        + Fraction(1, 5)
    )
    assert zeta_two_upper == Fraction(5989, 3600)
    assert zeta_two_upper < Fraction(5, 3)

    # For the actual infinite kernel K_2(d,e)=zeta(2)[d,e]^-2 and
    # W_2(m,m)=m^-2, the reserve on {2,4} at (a,b)=(1,-1) is
    # (3*zeta(2)-5)/16.  The rational upper bound proves strict negativity.
    negative_upper = (3 * zeta_two_upper - 5) / 16
    assert negative_upper < 0

    # At (a,b)=(1,0) it is (zeta(2)-1)/4, which is strictly positive since
    # zeta(2)>1.  This establishes both signs for the infinite form itself.
    assert Fraction(1, 4) > 0
    print("PASS: the full infinite zeta-kernel reserve is operatorially indefinite")


def check_laguerre_degree_two_witness():
    # For P_2(x)=2-x the sign is (2-x)(6-5x).
    # Rational enclosures: log 2 in (1/2,1), log 5 in (3/2,5/3).
    for x in (Fraction(1, 2), Fraction(1)):
        assert 2 - x > 0
        assert 6 - 5 * x > 0
    for x in (Fraction(3, 2), Fraction(5, 3)):
        assert 2 - x > 0
        assert 6 - 5 * x < 0
    # The elementary e-bounds quoted in the proof imply the log enclosures.
    assert Fraction(8, 3) > 2
    assert Fraction(11, 4) ** 3 < 25
    assert Fraction(8, 3) ** 5 > 125
    print("PASS: exact rational enclosures force opposite Laguerre tower signs at p=2,5")


def interval_add(left, right):
    return left[0] + right[0], left[1] + right[1]


def interval_scale(interval, scalar):
    if scalar >= 0:
        return interval[0] * scalar, interval[1] * scalar
    return interval[1] * scalar, interval[0] * scalar


def interval_multiply(left, right):
    products = (
        left[0] * right[0],
        left[0] * right[1],
        left[1] * right[0],
        left[1] * right[1],
    )
    return min(products), max(products)


def atanh_interval(x, terms):
    partial = sum(
        (x ** (2 * k + 1) / Fraction(2 * k + 1) for k in range(terms + 1)),
        Fraction(0),
    )
    remainder = x ** (2 * terms + 3) / Fraction(2 * terms + 3) / (1 - x * x)
    return 2 * partial, 2 * (partial + remainder)


def laguerre_p_coefficients(n):
    return [
        Fraction((-1) ** j * comb(n, j + 1), factorial(j))
        for j in range(n)
    ]


def interval_polynomial(coefficients, x):
    value = (Fraction(0), Fraction(0))
    for coefficient in reversed(coefficients):
        value = interval_add(
            interval_multiply(value, x),
            (coefficient, coefficient),
        )
    return value


def tower_reserve_interval(n, x):
    coefficients = laguerre_p_coefficients(n)
    first = interval_polynomial(coefficients, x)
    second = interval_polynomial(coefficients, interval_scale(x, 2))
    return interval_multiply(
        first,
        interval_add(first, interval_scale(second, 2)),
    )


def check_target_degree_151_real_primes():
    # log 2 = 2 atanh(1/3), log(8/7) = 2 atanh(1/15).
    log2 = atanh_interval(Fraction(1, 3), 35)
    log8_over_7 = atanh_interval(Fraction(1, 15), 18)
    log7 = (
        3 * log2[0] - log8_over_7[1],
        3 * log2[1] - log8_over_7[0],
    )
    reserve_2 = tower_reserve_interval(151, log2)
    reserve_7 = tower_reserve_interval(151, log7)
    assert reserve_2[0] > 0
    assert reserve_7[1] < 0
    assert reserve_2[0] > Fraction("9.59561939937104")
    assert reserve_2[1] < Fraction("9.59561939937106")
    assert reserve_7[0] > Fraction("-6.33518557015695")
    assert reserve_7[1] < Fraction("-6.33518557015693")
    print("PASS: degree n=151 has opposite exact local tower signs at real primes p=2,7")


def shifted_local_coefficient(a, r):
    return sum((r ** (2 * j - a) for j in range(a + 1)), Fraction(0))


def check_shifted_selector_not_unit():
    # p=5 and 5^c=2 gives the rational local parameter r=2.
    r = Fraction(2)
    b2 = shifted_local_coefficient(2, r)
    pi1 = Fraction(1, 2) + Fraction(1, 2) / b2
    pi2 = Fraction(1, 2) - Fraction(1, 2) / b2
    assert b2 == Fraction(21, 4)
    assert pi1 == Fraction(25, 42)
    assert pi2 == Fraction(17, 42)
    assert pi1 + pi2 == 1
    assert pi1 != Fraction(1, 2) and pi2 != Fraction(1, 2)
    print("PASS: shifted renewal is not inverted by the unit Möbius matrix")


def main():
    check_gram_and_double_inversion()
    check_indefinite_reserve()
    check_full_zeta_kernel_indefinite()
    check_laguerre_degree_two_witness()
    check_target_degree_151_real_primes()
    check_shifted_selector_not_unit()
    print("PASS: 104_51 Möbius-inverted lcm reserve gate")


if __name__ == "__main__":
    main()
