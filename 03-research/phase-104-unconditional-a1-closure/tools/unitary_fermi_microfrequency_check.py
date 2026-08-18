#!/usr/bin/env python3
"""Exact and diagnostic gates for 104_62.

The formal-power-series and quartet checks use Fraction.  The final Fourier
quadrature is explicitly diagnostic and is not used as a certificate.
"""

from fractions import Fraction
from math import comb, exp, log, sin, sinh, tanh


def mul(a, b, degree):
    out = [Fraction(0) for _ in range(degree + 1)]
    for i, ai in enumerate(a):
        if ai == 0:
            continue
        for j, bj in enumerate(b):
            if i + j > degree:
                break
            out[i + j] += ai * bj
    return out


def exp_series(a, degree):
    """exp(a(z)) through z**degree, assuming a[0] == 0."""
    assert a[0] == 0
    out = [Fraction(0) for _ in range(degree + 1)]
    out[0] = Fraction(1)
    for n in range(1, degree + 1):
        out[n] = sum(Fraction(k) * a[k] * out[n - k]
                     for k in range(1, n + 1)) / n
    return out


def laguerre_assoc(n, alpha, u):
    return sum(
        Fraction(comb(n + alpha, n - k) * (-1) ** k, 1)
        * u**k / Fraction(1 if k == 0 else factorial(k), 1)
        for k in range(n + 1)
    )


def factorial(n):
    out = 1
    for k in range(2, n + 1):
        out *= k
    return out


def check_laguerre_generators():
    degree = 14
    for u in (Fraction(1, 3), Fraction(2, 1), Fraction(7, 4)):
        # y=z/(1-z)=z+z^2+... and E=exp(-u*y).
        a = [Fraction(0)] + [-u for _ in range(degree)]
        e = exp_series(a, degree)

        # (1-E)/u: coefficient z^n is L_(n-1)^1(u)/n.
        harmonic = [Fraction(0)] + [-e[n] / u for n in range(1, degree + 1)]
        for n in range(1, degree + 1):
            expected = laguerre_assoc(n - 1, 1, u) / n
            assert harmonic[n] == expected

        # z/(1-z)^2 E: coefficient z^n is L_(n-1)^1(u).
        nonharmonic = [Fraction(0) for _ in range(degree + 1)]
        for n in range(1, degree + 1):
            nonharmonic[n] = sum(Fraction(j) * e[n - j]
                                 for j in range(1, n + 1))
            assert nonharmonic[n] == laguerre_assoc(n - 1, 1, u)


def pole_term(n, epsilon):
    return n * sum(
        Fraction(comb(n - 1, k - 1) * (-1) ** (k - 1), k)
        / epsilon**k
        for k in range(1, n + 1)
    )


def check_pole_generator():
    """Differentiate log(1+y/eps) and compare coefficients indirectly."""
    degree = 12
    for epsilon in (Fraction(1, 3), Fraction(2, 1), Fraction(5, 4)):
        # F(z)=sum p_n z^n/n.  Its derivative has coefficient p_n.
        # From log(1+y/eps), F' = 1/((1-z)*(eps+(1-eps)z)).
        one_over_1_minus_z = [Fraction(1) for _ in range(degree)]
        # 1/(eps+(1-eps)z).
        ratio = -(Fraction(1) - epsilon) / epsilon
        second = [ratio**k / epsilon for k in range(degree)]
        derivative = mul(one_over_1_minus_z, second, degree - 1)
        for n in range(1, degree + 1):
            assert derivative[n - 1] == pole_term(n, epsilon)


def gaussian_mul(z, w):
    return (z[0] * w[0] - z[1] * w[1],
            z[0] * w[1] + z[1] * w[0])


def gaussian_pow(z, n):
    out = (Fraction(1), Fraction(0))
    while n:
        if n & 1:
            out = gaussian_mul(out, z)
        z = gaussian_mul(z, z)
        n //= 2
    return out


def quartet(n):
    w = (Fraction(0), Fraction(2))
    winv = (Fraction(0), Fraction(-1, 2))
    wn = gaussian_pow(w, n)
    wni = gaussian_pow(winv, n)
    return Fraction(4) - 2 * (wn[0] + wni[0])


def check_quartet_microfrequency():
    for n in range(4, 257, 4):
        qn = quartet(n)
        assert qn == 4 - 2 * (Fraction(2) ** n + Fraction(2) ** (-n))
        # Since log(n+1)<=n, Y=-(Q+log(n+1)) >= -Q-n >= 2^n.
        assert -qn - n >= Fraction(2) ** n

    for blocks in (1, 10, 100, 1000):
        count = sum(n % 4 == 0 for n in range(1, 4 * blocks + 1))
        assert Fraction(count, 4 * blocks) == Fraction(1, 4)


def diagnostic_fourier_identity():
    # Midpoint rule away from the removable endpoint at zero.
    step = 2.5e-4
    cutoff = 12.0
    count = int(cutoff / step)
    for y in (-3.0, -1.0, 0.25, 2.0, 5.0):
        integral = 0.0
        for k in range(count):
            s = (k + 0.5) * step
            integral += sin(s * y) / sinh(3.141592653589793 * s)
        integral *= step
        lhs = 0.5 - integral
        rhs = 1.0 / (1.0 + exp(y))
        assert abs(lhs - rhs) < 2e-7
        assert abs(integral - 0.5 * tanh(y / 2.0)) < 2e-7


def main():
    check_laguerre_generators()
    check_pole_generator()
    check_quartet_microfrequency()
    diagnostic_fourier_identity()
    print("104_62 exact formal-series gates: PASS")
    print("Laguerre harmonic/nonharmonic generators: Fraction PASS through degree 14")
    print("regulated pole generator: Fraction PASS through degree 12")
    print("quartet bad class and Y_n >= 2^n: Fraction PASS through n=256")
    print("Fourier-logistic quadrature: diagnostic PASS")


if __name__ == "__main__":
    main()
