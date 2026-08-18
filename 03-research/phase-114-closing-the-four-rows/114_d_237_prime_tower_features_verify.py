#!/usr/bin/env python3
"""Numerical regression for the exact identities in D.237.

This is not evidence for row D.  It only guards the algebraic resummation
of the two positive prime-tower Grams on finite cyclic unitary models.
"""

import numpy as np


def check(size: int, prime: int) -> tuple[float, float, float]:
    unitary = np.roll(np.eye(size), 1, axis=0)
    ident = np.eye(size)
    r = prime ** -0.5
    logp = np.log(prime)

    # The resolvent formulas are exact on every unitary model.
    resolvent = np.linalg.inv(ident - r * unitary)
    cminus2 = logp * r * (1.0 + r) / (2.0 * (1.0 - r))
    wminus = np.sqrt(cminus2) * resolvent @ (ident - unitary)

    aa = 1.0 - r + 2.0 * r * r
    bb = 1.0 - 3.0 * r
    tt = bb / aa
    ss = 0.0 if tt == 0.0 else -tt / (1.0 + np.sqrt(1.0 - tt * tt))
    cplus2 = logp * r * aa / ((1.0 - r) * (1.0 + ss * ss))
    wplus = np.sqrt(cplus2) * resolvent @ (ident - ss * unitary)

    # Independent functional-calculus form from D.237(1.3).
    poisson = (
        np.linalg.inv(ident - r * unitary)
        + np.linalg.inv(ident - r * unitary.T)
        - ident
    )
    mass = r / (1.0 - r)
    minus_gram = logp * ((mass + 0.5) * ident - 0.5 * poisson)
    plus_gram = logp * ((mass - 0.5) * ident + 0.5 * poisson)

    err_minus = np.max(np.abs(wminus.T @ wminus - minus_gram))
    err_plus = np.max(np.abs(wplus.T @ wplus - plus_gram))
    err_difference = np.max(
        np.abs((plus_gram - minus_gram) - logp * (poisson - ident))
    )
    return err_minus, err_plus, err_difference


def main() -> None:
    worst = np.zeros(3)
    for size in (7, 16, 31):
        for prime in (2, 3, 5, 7, 11, 101):
            errors = np.array(check(size, prime))
            worst = np.maximum(worst, errors)
            print(f"size={size:2d} p={prime:3d} errors={errors}")
    print("worst_errors=", worst)
    assert np.max(worst) < 2e-13


if __name__ == "__main__":
    main()
