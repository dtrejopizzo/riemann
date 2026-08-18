#!/usr/bin/env python3
"""Exact checks for 104_48 (integers/Fraction only)."""

from fractions import Fraction
from math import comb, factorial


def laguerre_p_coeffs(n):
    """Coefficients of P_n(x)=L_{n-1}^{(1)}(x), low to high."""
    return [
        Fraction(((-1) ** j) * comb(n, j + 1), factorial(j))
        for j in range(n)
    ]


def poly_eval(coeffs, x):
    ans = Fraction(0)
    for coeff in reversed(coeffs):
        ans = ans * x + coeff
    return ans


def laplace_p(n, s):
    """Integral of exp(-s*x) P_n(x), evaluated coefficientwise."""
    return sum(
        coeff * factorial(j) / (s ** (j + 1))
        for j, coeff in enumerate(laguerre_p_coeffs(n))
    )


def eulerian_poly(j):
    """A_j(q) with sum k^j q^k=q*A_j(q)/(1-q)^(j+1)."""
    if j == 0:
        return [1]
    row = [1]
    for degree in range(2, j + 1):
        nxt = []
        for m in range(degree):
            value = 0
            if m < len(row):
                value += (m + 1) * row[m]
            if m >= 1:
                value += (degree - m) * row[m - 1]
            nxt.append(value)
        row = nxt
    return row


def power_sum_eulerian(j, q):
    numerator = q * poly_eval(eulerian_poly(j), q)
    return numerator / ((1 - q) ** (j + 1))


def power_sums_recursive(max_j, q):
    """Independent recursion from (1-q)S_j=q+q sum_{h<j} C(j,h)S_h."""
    values = [q / (1 - q)]
    for j in range(1, max_j + 1):
        lower = sum(comb(j, h) * values[h] for h in range(j))
        values.append(q * (1 + lower) / (1 - q))
    return values


def phi_closed(n, x, q):
    powers = power_sums_recursive(n - 1, q)
    return sum(
        coeff * (x ** j) * powers[j]
        for j, coeff in enumerate(laguerre_p_coeffs(n))
    )


def phi_truncated(n, x, q, cutoff):
    coeffs = laguerre_p_coeffs(n)
    return sum(
        (q ** k) * poly_eval(coeffs, k * x)
        for k in range(1, cutoff + 1)
    )


def c_add(z, w):
    return (z[0] + w[0], z[1] + w[1])


def c_mul(z, w):
    return (z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0])


def c_div(z, w):
    den = w[0] * w[0] + w[1] * w[1]
    return (
        (z[0] * w[0] + z[1] * w[1]) / den,
        (z[1] * w[0] - z[0] * w[1]) / den,
    )


def c_pow(z, n):
    ans = (Fraction(1), Fraction(0))
    base = z
    while n:
        if n & 1:
            ans = c_mul(ans, base)
        base = c_mul(base, base)
        n //= 2
    return ans


def norm_sq(z):
    return z[0] * z[0] + z[1] * z[1]


def check_laplace_and_pole():
    for n in range(1, 14):
        for s in (Fraction(2, 3), Fraction(5, 4), Fraction(7, 3)):
            expected = 1 - (1 - 1 / s) ** n
            assert laplace_p(n, s) == expected
        for a in (Fraction(3, 2), Fraction(7, 3), Fraction(4)):
            s = (a - 1) / a
            q_integral = laplace_p(n, s)
            assert q_integral == 1 - (-1 / (a - 1)) ** n
    print("PASS: exact Laguerre Laplace transform and polar term")


def check_eulerian_tower():
    for q in (Fraction(1, 5), Fraction(2, 7), Fraction(3, 8)):
        recursive = power_sums_recursive(11, q)
        for j, value in enumerate(recursive):
            assert value == power_sum_eulerian(j, q)
        for n in range(1, 11):
            x = Fraction(n + 2, n + 5)
            from_eulerian = sum(
                coeff * x ** j * power_sum_eulerian(j, q)
                for j, coeff in enumerate(laguerre_p_coeffs(n))
            )
            assert phi_closed(n, x, q) == from_eulerian
    print("PASS: exact Eulerian closed form for every tested tower")


def check_phase_atom():
    for r in (Fraction(3, 5), Fraction(1), Fraction(7, 5)):
        for y in (Fraction(1, 3), Fraction(5, 2), Fraction(17, 4)):
            w = c_div((r - 1, y), (r, y))
            identity = 1 - norm_sq(w)
            expected = (2 * r - 1) / (r * r + y * y)
            assert identity == expected > 0
            for n in range(1, 13):
                wn = c_pow(w, n)
                # Re(1-w^n) >= 1-|w|^n > 0; exact positivity is enough here.
                assert 1 - wn[0] > 0
    print("PASS: exact shifted phase atoms have the claimed sign for r>1/2")


def check_shifted_split():
    # Formal finite version of (20): q^k(h^k+h^-k).
    n = 9
    x = Fraction(4, 7)
    q = Fraction(1, 9)
    h = Fraction(3, 2)
    cutoff = 12
    coeffs = laguerre_p_coeffs(n)
    lhs = sum(
        q ** k * (h ** k + h ** (-k)) * poly_eval(coeffs, k * x)
        for k in range(1, cutoff + 1)
    )
    rhs = phi_truncated(n, x, q * h, cutoff) + phi_truncated(
        n, x, q / h, cutoff
    )
    assert lhs == rhs
    print("PASS: exact two-rate split of the shifted prime tower")


def check_n151_positive_tail():
    n = 151
    degree = n - 1
    x = degree * (degree + 1) + 1
    # Exact version of (29): every adjacent magnitude ratio exceeds one.
    for j in range(degree):
        assert x * (degree - j) > (j + 1) * (j + 2)
    coeffs = laguerre_p_coeffs(n)
    for k in (1, 2, 3):
        assert poly_eval(coeffs, k * x) > 0
    assert 33977 * 2 > 3 * 22651
    print("PASS: exact n=151 alternating-tail certificate (x>22650)")


def check_quartet():
    # Rational Cayley test w=i/2, together with conjugate and reciprocals.
    w = (Fraction(0), Fraction(1, 2))
    wbar = (w[0], -w[1])
    winv = c_div((Fraction(1), Fraction(0)), wbar)
    winv_bar = (winv[0], -winv[1])
    for n in (4, 8, 12, 152):
        power_sum = (Fraction(0), Fraction(0))
        for z in (w, wbar, winv, winv_bar):
            power_sum = c_add(power_sum, c_pow(z, n))
        assert power_sum[1] == 0
        # cos(n*pi/2)=1 for these n, hence 2(r^n+r^-n).
        expected = 2 * (Fraction(2) ** n + Fraction(2) ** (-n))
        assert power_sum[0] == expected
        response = 4 - power_sum[0]
        assert response == 4 - expected
    print("PASS: exact reciprocal-quartet cosh response")


def main():
    check_laplace_and_pole()
    check_eulerian_tower()
    check_phase_atom()
    check_shifted_split()
    check_n151_positive_tail()
    check_quartet()
    print("PASS: 104_48 prime-tower signed-coercivity gate")


if __name__ == "__main__":
    main()
