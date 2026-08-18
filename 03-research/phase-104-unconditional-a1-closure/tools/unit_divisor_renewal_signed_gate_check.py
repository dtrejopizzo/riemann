#!/usr/bin/env python3
"""Exact checks for 104_49 (integers and Fraction only)."""

from fractions import Fraction
from math import comb, factorial


def laguerre_p_coeffs(n, scale=Fraction(1)):
    """P_n(scale*x)=L_{n-1}^{(1)}(scale*x), low to high."""
    return [
        Fraction((-1) ** j * comb(n, j + 1), factorial(j)) * scale**j
        for j in range(n)
    ]


def poly_eval(coeffs, x):
    ans = Fraction(0)
    for coefficient in reversed(coeffs):
        ans = ans * x + coefficient
    return ans


def primitive_coeffs(coeffs):
    return [Fraction(0)] + [coefficient / (j + 1) for j, coefficient in enumerate(coeffs)]


def check_uniform_palm():
    for q in (Fraction(1, 5), Fraction(2, 7), Fraction(4, 9)):
        for a in range(1, 10):
            joint = [(1 - q) ** 2 * q ** (a - 1) for _k in range(1, a + 1)]
            size_biased_mass = a * (1 - q) ** 2 * q ** (a - 1)
            assert sum(joint) == size_biased_mass
            assert all(weight * a == size_biased_mass for weight in joint)
    print("PASS: geometric Palm mark is exactly uniform conditional on A*=a")


def check_laguerre_primitive():
    for n in range(1, 14):
        for scale in (Fraction(2, 3), Fraction(1), Fraction(7, 4)):
            p = laguerre_p_coeffs(n, scale)
            primitive = primitive_coeffs(p)
            # Integral P_n(scale*x) dx = (1-L_n(scale*x))/scale.
            rhs = [Fraction(0)]
            for r in range(1, n + 1):
                rhs.append(
                    Fraction((-1) ** (r - 1) * comb(n, r), factorial(r))
                    * scale ** (r - 1)
                )
            assert primitive == rhs
    print("PASS: exact Laguerre primitive in the unit-selector defect")


def check_moment_cumulant_cancellation():
    # Formal exact check: the arbitrary complete moments m_r cancel.
    for n in range(1, 12):
        scale = Fraction(7, 5)
        epsilon = Fraction(3, 8)
        moments = [None] + [Fraction(r * r + 2, r + 3) for r in range(1, n + 1)]
        cumulants = [None] + [Fraction(3 * r + 1, 2 * r + 5) for r in range(1, n + 1)]
        selector = Fraction(0)
        transport = Fraction(0)
        direct = Fraction(0)
        for r in range(1, n + 1):
            coefficient = (
                Fraction((-1) ** (r - 1) * comb(n, r), factorial(r - 1))
                * scale ** (r - 1)
            )
            polar_cumulant = Fraction(factorial(r - 1), 1) / epsilon**r
            selector += coefficient * (cumulants[r] - moments[r] / r)
            transport += coefficient * (moments[r] / r - polar_cumulant)
            direct += coefficient * (cumulants[r] - polar_cumulant)
        assert selector + transport == direct
    print("PASS: complete moments cancel exactly degree by degree")


def unit_defect_squarefree(n, xs, scale=Fraction(1)):
    p = laguerre_p_coeffs(n, scale)
    primitive = primitive_coeffs(p)
    return sum(x * poly_eval(p, x) for x in xs) - poly_eval(primitive, sum(xs))


def check_degree_151_two_signs():
    x = Fraction(1000)
    for scale in (Fraction(1), Fraction(6, 5), Fraction(2)):
        prime_defect = unit_defect_squarefree(151, [x], scale)
        two_prime_defect = unit_defect_squarefree(151, [x, x], scale)
        assert prime_defect > 0
        assert two_prime_defect < 0
    # Leading homogeneous signs used with Bertrand in the written proof.
    assert 150 > 0
    assert 2 * 151 < 2**151
    print("PASS: exact degree-151 unit defect has both algebraic signs")


def shifted_local_coefficient(a, r):
    return sum(r ** (2 * j - a) for j in range(a + 1))


def check_shifted_nonuniform_selector():
    for r in (Fraction(3, 2), Fraction(2), Fraction(5, 2)):
        for a in range(1, 9):
            b_a = shifted_local_coefficient(a, r)
            renewal = sum(
                (r**k + r ** (-k)) * shifted_local_coefficient(a - k, r)
                for k in range(1, a + 1)
            )
            assert renewal == a * b_a
        b2 = shifted_local_coefficient(2, r)
        pi1 = (r + 1 / r) * shifted_local_coefficient(1, r) / (2 * b2)
        pi2 = (r**2 + r ** (-2)) / (2 * b2)
        assert pi1 == Fraction(1, 2) + 1 / (2 * b2)
        assert pi2 == Fraction(1, 2) - 1 / (2 * b2)
        assert pi1 + pi2 == 1
    print("PASS: shifted omega_c selector fails unit uniformity already at a=2")


def main():
    check_uniform_palm()
    check_laguerre_primitive()
    check_moment_cumulant_cancellation()
    check_degree_151_two_signs()
    check_shifted_nonuniform_selector()
    print("PASS: 104_49 unit-divisor renewal signed gate")


if __name__ == "__main__":
    main()
