#!/usr/bin/env python3
"""Finite numerical sanity check for the exact D.254/D.257 multipliers.

This script is not part of the proof.  The proof is the common-denominator
calculation in the accompanying notes.
"""

import cmath
import math


def check_prime(p: int, theta: float) -> tuple[float, float]:
    r = p ** -0.5
    ell = math.log(p)
    u = cmath.exp(1j * theta)
    h = 1 - r * u
    tangent = (ell * r / 2) * (u + u.conjugate() - 2 * r) / h
    dual = 1 / h.conjugate()
    cotangent = tangent.conjugate()
    central = 1 / h

    score = ell * ((1 - r * r) / abs(h) ** 2 - 1)
    d257 = cotangent.conjugate() * dual + dual.conjugate() * cotangent
    d254 = tangent.conjugate() * central + central.conjugate() * tangent
    return abs(d257 - score), abs(d254 - score)


def main() -> None:
    worst_257 = 0.0
    worst_254 = 0.0
    for p in (2, 3, 5, 7, 11, 101):
        for j in range(1, 64):
            err_257, err_254 = check_prime(p, 2 * math.pi * j / 67)
            worst_257 = max(worst_257, err_257)
            worst_254 = max(worst_254, err_254)
    print("maximum D.257 scalar residual =", worst_257)
    print("maximum D.254 scalar residual =", worst_254)
    assert worst_257 < 2e-13
    assert worst_254 < 2e-13
    print("D.254/D.257 multiplier sanity check: PASS")


if __name__ == "__main__":
    main()
