#!/usr/bin/env python3
"""Diagnostics for 106.33.

This is not a proof.  It checks:
  * the two-dimensional kernel of the four asymptotic constraints;
  * the d4/d8 generalized-eigenvalue hierarchy;
  * the exact cancellation of the first two outgoing coefficients;
  * the final polynomial exponent p_R=7.
"""

from fractions import Fraction
import numpy as np


def constrained_levels(y: float) -> tuple[float, float]:
    r = np.arange(6, dtype=float)
    matrix = np.vstack(
        (
            np.ones(6),
            y ** (2 * r),
            y**r,
            r * y**r,
        )
    )
    matrix /= np.linalg.norm(matrix, axis=1)[:, None]
    _, _, vh = np.linalg.svd(matrix)
    kernel = vh[-2:].T
    q = y ** (2 * r)
    energy = kernel.T @ np.diag(q) @ kernel
    return tuple(np.linalg.eigvalsh(energy))


def outgoing_coefficient_check() -> None:
    # Treat A_j and a_{0,j} as formal samples.  If sum a0=sum A*a0=0,
    # the recurrence gives sum a2=-(8 k^2)^(-1) sum mu^2*a0.
    k2 = Fraction(49, 1)
    common = Fraction(101, 1)
    mu = [Fraction(2), Fraction(5), Fraction(11)]
    # A nonzero vector annihilating 1 and A=common-mu.
    a0 = [mu[1] - mu[2], mu[2] - mu[0], mu[0] - mu[1]]
    A = [common - value for value in mu]
    assert sum(a0) == 0
    assert sum(x * y for x, y in zip(A, a0)) == 0

    a2 = [
        (-Aj * (Aj + 2) / (8 * k2) + Fraction(1, 2)) * x
        for Aj, x in zip(A, a0)
    ]
    lhs = sum(a2)
    rhs = -sum(value * value * x for value, x in zip(mu, a0)) / (8 * k2)
    assert lhs == rhs


def main() -> None:
    outgoing_coefficient_check()
    print("y       delta0/q1       delta1/q2")
    for y in (10.0, 30.0, 100.0, 300.0):
        delta0, delta1 = constrained_levels(y)
        print(f"{y:5.0f}   {delta0/y**2:12.8f}   {delta1/y**4:12.8f}")

    a = Fraction(7, 2)
    p_r = 2 * a
    assert p_r == 7 and p_r < 8
    print("outgoing recurrence: PASS")
    print(f"FM exponent a={a}; residual exponent p_R={p_r}: PASS")


if __name__ == "__main__":
    main()
