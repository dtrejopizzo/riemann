#!/usr/bin/env python3
"""Exact/diagnostic checks for 104_57_LOW_ZERO_BLOCK_BUDGET.md.

No zero data are imported.  The script checks only algebraic normalization:
the modulus identity, the logarithmic-amplitude bracket, the quartet factor,
and the low-block budget equivalence.
"""

from fractions import Fraction
import cmath
import math


def check_modulus_and_amplitude() -> None:
    beta = Fraction(3, 4)
    gamma = Fraction(10, 1)
    d = 2 * beta - 1
    den = gamma * gamma + beta * beta

    modulus_sq_direct = (gamma * gamma + (1 - beta) ** 2) / den
    modulus_sq_reduced = 1 - d / den
    assert modulus_sq_direct == modulus_sq_reduced

    x = float(d / den)
    a = -0.5 * math.log1p(-x)
    lower = float(d / (2 * (gamma * gamma + beta * beta)))
    upper = float(d / (2 * (gamma * gamma + (1 - beta) ** 2)))
    assert lower <= a <= upper


def check_quartet_factor() -> None:
    beta = 0.75
    gamma = 10.0
    rho = complex(beta, gamma)
    orbit = (rho, rho.conjugate(), 1 - rho, 1 - rho.conjugate())
    w = 1 - 1 / rho
    a = -math.log(abs(w))
    theta = cmath.phase(w)

    for n in (1, 2, 7, 31):
        direct = sum(1 - (1 - 1 / z) ** n for z in orbit)
        closed = 4 - 4 * math.cosh(n * a) * math.cos(n * theta)
        assert abs(direct.imag) < 2e-10
        assert abs(direct.real - closed) < 2e-9


def check_budget_algebra() -> None:
    # lambda = A + Llow - epsilon and target lambda >= c*A.
    A = Fraction(120, 1)
    c = Fraction(1, 4)
    epsilon = Fraction(3, 1)
    boundary = -(1 - c) * A + epsilon

    for offset in (Fraction(-1), Fraction(0), Fraction(1)):
        low = boundary + offset
        lam = A + low - epsilon
        assert (lam >= c * A) == (low >= boundary)

    # Worst-case transfer from Llow >= -alpha*A-E.
    alpha = Fraction(1, 2)
    error = Fraction(4, 1)
    transport = Fraction(2, 1)
    low = -alpha * A - error
    lam_worst = A + low - transport
    budget_ok = error + transport <= (1 - c - alpha) * A
    assert (lam_worst >= c * A) == budget_ok


def main() -> None:
    check_modulus_and_amplitude()
    check_quartet_factor()
    check_budget_algebra()
    print("PASS 104_57 low-zero block algebra")
    print("RvM leading constants:")
    print(f"  positive ordinates: 1/(4*pi) = {1/(4*math.pi):.12f}")
    print(f"  symmetric labels:   1/(2*pi) = {1/(2*math.pi):.12f}")


if __name__ == "__main__":
    main()
