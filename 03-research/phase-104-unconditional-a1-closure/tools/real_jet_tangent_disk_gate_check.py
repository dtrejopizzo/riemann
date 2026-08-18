#!/usr/bin/env python3
"""Finite checks for 104_104_REAL_JET_TANGENT_DISK_GATE.md."""

from fractions import Fraction
from math import log

import numpy as np
from numpy.polynomial import Polynomial


def p_factor(s: complex, beta: float, gamma: float) -> complex:
    num = ((s - beta) ** 2 + gamma**2) * (
        (s - (1.0 - beta)) ** 2 + gamma**2
    )
    den = (beta**2 + gamma**2) * ((1.0 - beta) ** 2 + gamma**2)
    return num / den


def log_p_jets(s: float, beta: float, gamma: float):
    xs = (s - beta, s - (1.0 - beta))
    value = log(float(p_factor(s, beta, gamma).real))
    first = sum(2.0 * x / (x * x + gamma * gamma) for x in xs)
    second = sum(
        2.0 * (gamma * gamma - x * x) / (x * x + gamma * gamma) ** 2
        for x in xs
    )
    return value, first, second


def q_rational(n: int) -> Fraction:
    # u=2i: cos(pi*n/2) is exactly 1,0,-1,0.
    cosine = (1, 0, -1, 0)[n % 4]
    return Fraction(4) - 2 * (
        Fraction(2**n) + Fraction(1, 2**n)
    ) * cosine


def main() -> None:
    # Tangent-disk identity and the Euler horodisk.
    for x_num in range(-8, 9):
        for y_num in range(-8, 9):
            z = complex(x_num / 10.0, y_num / 10.0)
            if abs(z) >= 0.999 or abs(1.0 - z) < 1e-12:
                continue
            threshold = (1.0 - abs(z) ** 2) / (2.0 * (1.0 - z.real))
            r = max(1e-4, min(0.9 * threshold, 0.9))
            if threshold > 1e-4:
                assert abs(z - r) < 1.0 - r + 1e-12

            s = 1.0 / (1.0 - z)
            lhs = s.real > 1.0
            rhs = abs(z - 0.5) < 0.5
            assert lhs == rhs

    for r_num in range(5, 10):
        r = r_num / 10.0
        # Farthest point of D(r,1-r) from the Euler center is tangent.
        assert abs(r - 0.5) + (1.0 - r) <= 0.5 + 1e-15

    # Functional symmetry, normalization, and real positivity of P.
    beta = 0.73
    gamma = 11.0
    for s in (0.0, 0.2, 1.0, 1.7, 4.0, 2.3 + 0.7j):
        assert abs(p_factor(1.0 - s, beta, gamma) - p_factor(s, beta, gamma)) < 1e-12
        assert abs(p_factor(s.conjugate(), beta, gamma) - p_factor(s, beta, gamma).conjugate()) < 1e-12
    assert abs(p_factor(0.0, beta, gamma) - 1.0) < 1e-15
    assert abs(p_factor(1.0, beta, gamma) - 1.0) < 1e-15
    for zero in (
        beta + 1j * gamma,
        beta - 1j * gamma,
        1.0 - beta + 1j * gamma,
        1.0 - beta - 1j * gamma,
    ):
        assert abs(p_factor(zero, beta, gamma)) < 1e-12
    rho = beta + 1j * gamma
    assert abs(rho / (rho - 1.0)) > 1.0
    for j in range(-20, 81):
        assert p_factor(j / 10.0, beta, gamma).real > 0.0

    # C^2 invisibility: multiplying gamma by ten decreases fixed-compact
    # jets quadratically (allowing a small finite-gamma cushion).
    suprema = []
    for g in (30.0, 300.0, 3000.0):
        vals = [0.0, 0.0, 0.0]
        for j in range(101):
            s = 1.0 + 4.0 * j / 100.0
            jets = log_p_jets(s, beta, g)
            vals = [max(vals[k], abs(jets[k])) for k in range(3)]
        suprema.append(vals)
    for order in range(3):
        assert suprema[1][order] < suprema[0][order] / 90.0
        assert suprema[2][order] < suprema[1][order] / 90.0

    # Exact quartet with u=2i. Every four consecutive positive indices
    # contain a multiple of four and hence a negative excursion.
    for n in range(1, 65):
        q = q_rational(n)
        if n % 4 == 0:
            assert q < 0
    for start in range(1, 61):
        assert any(q_rational(n) < 0 for n in range(start, start + 4))

    # Exact finite-jet interpolator (28), with M_0=M_1=2 and s_1=2.
    # Q-1 has fourth-order zeros at 0,1,2,-1, hence log Q has vanishing
    # jets through order three at those nodes.
    base_zero = Polynomial([0.0, -1.0, 1.0])  # s(s-1)
    base_two = Polynomial([-2.0, -1.0, 1.0])  # (s-2)(s+1)
    q_poly = Polynomial([1.0]) + base_zero**4 * base_two**4
    for node in (0.0, 1.0, 2.0, -1.0):
        assert abs(q_poly(node) - 1.0) < 1e-12
        for order in range(1, 4):
            assert abs(q_poly.deriv(order)(node)) < 1e-9
    for s in np.linspace(-3.0, 4.0, 141):
        assert q_poly(s).real >= 1.0 - 1e-12
    for y in np.linspace(-5.0, 5.0, 101):
        value = q_poly(0.5 + 1j * y)
        assert value.real > 1.0
        assert abs(value.imag) < 1e-10 * abs(value.real) + 1e-8
    roots = q_poly.roots()
    strip_roots = [
        z for z in roots if 0.5 < z.real < 1.0 and abs(z.imag) > 1e-8
    ]
    assert strip_roots

    print("104_104 real-jet/tangent-disk checks: PASS")
    print("C2 suprema at gamma=30,300,3000:")
    for g, vals in zip((30, 300, 3000), suprema):
        print(f"  gamma={g:4d}: " + ", ".join(f"{v:.6e}" for v in vals))
    print("rational quartet Q_4, Q_8, Q_12:", q_rational(4), q_rational(8), q_rational(12))
    witness = strip_roots[0]
    print(f"exact-jet interpolator strip zero: {witness.real:.12f}{witness.imag:+.12f}i")


if __name__ == "__main__":
    main()
