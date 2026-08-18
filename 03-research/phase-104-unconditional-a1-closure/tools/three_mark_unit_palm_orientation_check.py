#!/usr/bin/env python3
"""Exact checks for 104_55 (integers and Fraction only)."""

from fractions import Fraction as Q
from math import comb, factorial, gcd


def laguerre_p_coeffs(n):
    """P_n(x)=L_{n-1}^{(1)}(x), low-to-high coefficients."""
    return [Q((-1) ** j * comb(n, j + 1), factorial(j)) for j in range(n)]


def poly_eval(coeffs, x):
    value = Q(0)
    for coefficient in reversed(coeffs):
        value = value * x + coefficient
    return value


def lcm(a, b):
    return a * b // gcd(a, b)


def lcm3(a, b, c):
    return lcm(lcm(a, b), c)


def check_three_mark_palm():
    towers = [(Q(2), 2), (Q(3), 1)]
    marks = [(ell, Q(k) * ell) for ell, exponent in towers for k in range(1, exponent + 1)]
    total = sum((ell * exponent for ell, exponent in towers), Q(0))
    assert total == 7

    f = lambda x: 1 + x
    g = lambda x: 2 - x + x * x
    h = lambda x: 3 + 2 * x * x
    jf = sum((ell * f(x) for ell, x in marks), Q(0))
    jg = sum((ell * g(x) for ell, x in marks), Q(0))
    jh = sum((ell * h(x) for ell, x in marks), Q(0))
    ef = jf / total
    eg = jg / total
    eh = jh / total
    assert total**3 * ef * eg * eh == jf * jg * jh

    # The common-multiple sum uses lcm(d,e,r), not the product.
    assert lcm3(4, 8, 9) == 72
    assert lcm3(4, 9, 25) == 4 * 9 * 25
    print("PASS: exact third Palm normalization and triple-lcm kernel")


def check_polar_gamma_four():
    eps = Q(7, 3)
    assert Q(factorial(3), 1) / eps**3 == 6 / eps**3
    for a, b, c in ((1, 1, 1), (2, 3, 1), (4, 2, 3)):
        total = a + b + c
        base_product = Q(factorial(total), a * b * c) / eps**total

        # Under Gamma(4,eps), E[Y^k]=(k+3)!/(3!*eps^k).
        k = total - 3
        gamma_moment = Q(factorial(k + 3), factorial(3)) / eps**k
        biased_side = Q(6, 1) / eps**3 * gamma_moment / (a * b * c)
        assert biased_side == base_product
    print("PASS: exact factor 6 and Gamma(4,epsilon) polar comparator")


def mean(probabilities, values):
    return sum((p * x for p, x in zip(probabilities, values)), Q(0))


def check_cubic_completion_and_orientation():
    probabilities = [Q(1, 6), Q(1, 3), Q(1, 2)]
    d = [Q(-2), Q(1), Q(3)]
    transport = Q(7, 5)
    z = [x + transport for x in d]
    m = mean(probabilities, z)
    centered = [x - mean(probabilities, d) for x in d]
    variance = mean(probabilities, [x * x for x in centered])
    mu3 = mean(probabilities, [x**3 for x in centered])
    raw3 = mean(probabilities, [x**3 for x in z])
    assert raw3 == mu3 + 3 * m * variance + m**3

    budget = Q(11, 13)
    shifted3 = mean(probabilities, [(x - budget) ** 3 for x in z])
    margin = m - budget
    assert shifted3 == mu3 + 3 * margin * variance + margin**3

    # Enumerate three independent copies in the oriented U-statistic.
    oriented = Q(0)
    for pi, zi in zip(probabilities, z):
        for pj, zj in zip(probabilities, z):
            for pk, zk in zip(probabilities, z):
                oriented += pi * pj * pk * (zi - zj) ** 2 * (zk - budget)
    assert oriented == 2 * variance * margin
    assert variance > 0

    # General independent-last-copy factorization (19a), with a positive
    # weight depending on the first two copies only.
    general = Q(0)
    expected_h = Q(0)
    for pi, zi in zip(probabilities, z):
        for pj, zj in zip(probabilities, z):
            h_weight = (zi - zj) ** 4 + 1
            expected_h += pi * pj * h_weight
            for pk, zk in zip(probabilities, z):
                general += pi * pj * pk * h_weight * (zk - budget)
    assert expected_h > 0
    assert general == expected_h * margin
    print("PASS: cubic completion and exact oriented three-copy U-statistic")


def det3(matrix):
    return (
        matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )


def check_determinant_gate():
    atoms = [Q(1), Q(2), Q(4)]
    probabilities = [Q(1, 5), Q(2, 5), Q(2, 5)]
    unsquared = Q(0)
    squared = Q(0)
    for pa, a in zip(probabilities, atoms):
        for pb, b in zip(probabilities, atoms):
            for pc, c in zip(probabilities, atoms):
                matrix = [
                    [Q(1), Q(1), Q(1)],
                    [a, b, c],
                    [a * a, b * b, c * c],
                ]
                determinant = det3(matrix)
                weight = pa * pb * pc
                unsquared += weight * determinant
                squared += weight * determinant**2
    assert unsquared == 0
    assert squared > 0
    print("PASS: alternating 3x3 determinant averages to zero; its square is PSD")


def check_unit_and_shifted_third_skew():
    # Unit local reflection.
    for a in range(1, 10):
        midpoint = Q(a + 1, 2)
        for order in (1, 3, 5, 7):
            centered_average = sum(
                (Q(k) - midpoint) ** order for k in range(1, a + 1)
            ) / a
            assert centered_average == 0

    # Shifted p=5, 5^c=2, exponent a=2.
    p, q = Q(25, 42), Q(17, 42)
    reflection_defect = p * (Q(1) - Q(3, 2)) ** 3 + q * (Q(2) - Q(3, 2)) ** 3
    shifted_mean = p + 2 * q
    shifted_mu3 = p * (1 - shifted_mean) ** 3 + q * (2 - shifted_mean) ** 3
    assert reflection_defect == -Q(1, 42)
    assert shifted_mu3 == Q(425, 9261) > 0

    # N=6 gives negative skew for every 0<x<y; test the exact identity.
    x, y = Q(2), Q(3)
    probs = [x / (x + y), y / (x + y)]
    values = [x, y]
    mu = mean(probs, values)
    mu3 = mean(probs, [(v - mu) ** 3 for v in values])
    assert mu3 == -x * y * (y - x) ** 4 / (x + y) ** 3 < 0

    # For N=18 the actual ratio r=log(3)/log(2) lies in (3/2,8/5).
    assert 2**3 < 3**2 and 3**5 < 2**8
    # Q(3/2+t)=145/16+61t/4-6t^2-21t^3-9t^4.
    lower_bound = Q(145, 16) - Q(6, 100) - Q(21, 1000) - Q(9, 10000)
    assert lower_bound > 0
    for t in (Q(0), Q(1, 20), Q(1, 10)):
        r = Q(3, 2) + t
        original = -2 + 13 * r - 33 * r**2 + 33 * r**3 - 9 * r**4
        expanded = Q(145, 16) + Q(61, 4) * t - 6 * t**2 - 21 * t**3 - 9 * t**4
        assert original == expanded > 0
    print("PASS: unit reflection, shifted failure, and both real arithmetic skew signs")


def third_difference(n, t):
    p = laguerre_p_coeffs(n)
    return (
        poly_eval(p, t + 3)
        - 3 * poly_eval(p, t + 2)
        + 3 * poly_eval(p, t + 1)
        - poly_eval(p, t)
    )


def check_laguerre_third_difference():
    for n in (150, 151, 152):
        assert third_difference(n, Q(0)) < 0
        assert third_difference(n, Q(1)) > 0
    print("PASS: exact Laguerre third differences have both signs at n=150..152")


def main():
    check_three_mark_palm()
    check_polar_gamma_four()
    check_cubic_completion_and_orientation()
    check_determinant_gate()
    check_unit_and_shifted_third_skew()
    check_laguerre_third_difference()
    print("PASS: 104_55 three-mark unit-Palm orientation gate")


if __name__ == "__main__":
    main()
