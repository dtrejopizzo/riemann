#!/usr/bin/env python3
"""Exact/diagnostic checks for 104_66.

The coefficient identity for p_n is checked with Fraction.  Floating-point
rows only illustrate asymptotic scales and are not certificates.
"""

from __future__ import annotations

from fractions import Fraction
from math import comb, exp, log, sqrt
import cmath


def p_binomial(n: int, eps: Fraction) -> Fraction:
    total = Fraction(0)
    for k in range(1, n + 1):
        total += (
            Fraction(n * comb(n - 1, k - 1) * (-1) ** (k - 1), k)
            / eps**k
        )
    return total


def p_closed(n: int, eps: Fraction) -> Fraction:
    return 1 + (-1) ** (n - 1) * ((1 - eps) / eps) ** n


def shifted_mode(rho: complex, eps: float) -> complex:
    return (rho - eps) / (rho - eps - 1.0)


def main() -> None:
    for eps in (Fraction(1, 3), Fraction(2, 5), Fraction(3, 7)):
        for n in range(1, 13):
            assert p_binomial(n, eps) == p_closed(n, eps)
    print("exact polar coefficient identity: PASS")

    r = Fraction(199, 200)
    assert r * r < Fraction(195, 196)
    c = 0.01
    eta = c - log(200.0 / 199.0)
    assert eta > 0.0
    print(f"r0={sqrt(195/196):.12f}  r={float(r):.12f}")
    print(f"C={c:.12f}  eta=C-log(200/199)={eta:.12f}")

    print("\ndiagonal polar scale: log|p_n-1| / (C/h^2) -> 1")
    hs = (0.01, 0.005, 0.002, 0.001, 0.0005)
    for h in hs:
        n = round(1.0 / h)
        eps = exp(-c / h)
        log_p = n * (log(1.0 - eps) - log(eps))
        reference = c / (h * h)
        print(
            f"  h={h:7g} n={n:5d} eps={eps:.4e} "
            f"ratio={log_p/reference:.9f}"
        )

    # A hypothetical off-line zero respecting the |gamma|>14 geometry.
    rho = complex(0.75, 14.25)
    base = shifted_mode(rho, 0.0)
    assert abs(base) > 1.0
    print("\nshifted exterior mode: n*|log(u_eps/u_0)| -> 0")
    for h in hs:
        n = round(1.0 / h)
        eps = exp(-c / h)
        moved = shifted_mode(rho, eps)
        defect = n * abs(cmath.log(moved / base))
        print(
            f"  h={h:7g} n={n:5d} eps={eps:.4e} "
            f"defect={defect:.9e}"
        )

    print("\nCauchy diagonal envelope (constant 2M_r omitted)")
    for h in hs:
        envelope = exp(-eta / h) / h
        print(f"  h={h:7g} h^-1 exp(-eta/h)={envelope:.9e}")

    print("\ndiagonal regulator versus minimum VK absolute damping")
    for n in (500, 1000, 2000, 5000):
        log_eps_diagonal = -c * n
        log_eps_vk = (-2.0 / 3.0) * log(n) + (2.0 / 3.0) * log(log(n))
        assert log_eps_diagonal < log_eps_vk
        print(
            f"  n={n:5d} log eps_diag={log_eps_diagonal:9.3f} "
            f"log eps_VK~={log_eps_vk:9.3f}"
        )

    print("\nPASS")


if __name__ == "__main__":
    main()
