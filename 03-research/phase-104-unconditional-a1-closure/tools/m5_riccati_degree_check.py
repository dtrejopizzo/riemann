#!/usr/bin/env python3
"""Exact finite check of the degree Riccati recurrence in 104_13."""

from fractions import Fraction


def laguerre_values(n_max, x):
    vals = [Fraction(1)]
    if n_max == 0:
        return vals
    vals.append(1 - x)
    for n in range(1, n_max):
        vals.append(((2 * n + 1 - x) * vals[n] - n * vals[n - 1]) / (n + 1))
    return vals


def atom_transform(atoms, n_max):
    """atoms are (already Abel-weighted mass, logarithmic location)."""
    out = [Fraction(0) for _ in range(n_max + 1)]
    for mass, x in atoms:
        vals = laguerre_values(n_max, x)
        for n, value in enumerate(vals):
            out[n] += mass * value
    return out


def convolution(x, y, n):
    return sum((x[k] * y[n - k] for k in range(n + 1)), Fraction(0))


def main():
    n_max = 8
    eps = Fraction(2, 5)

    # A formal absolutely convergent Dirichlet series at s=a.  The first
    # coordinate already includes exp(-a*x); rational values make the check exact.
    atoms = [
        (Fraction(3, 7), Fraction(1, 2)),
        (Fraction(5, 11), Fraction(4, 3)),
        (Fraction(2, 13), Fraction(7, 4)),
    ]

    p = atom_transform(atoms, n_max + 1)

    # -ell' contributes x*mass at x; ell^2 contributes all ordered pairs.
    selberg_atoms = [(mass * x, x) for mass, x in atoms]
    selberg_atoms.extend(
        (mass_1 * mass_2, x_1 + x_2)
        for mass_1, x_1 in atoms
        for mass_2, x_2 in atoms
    )
    beta = atom_transform(selberg_atoms, n_max)

    j = [((eps - 1) ** n) / (eps ** (n + 1)) for n in range(n_max + 2)]
    c = [p[n] - j[n] for n in range(n_max + 2)]

    ratio = (1 - eps) / eps
    q = []
    for n in range(n_max + 1):
        previous = Fraction(0) if n == 0 else n * ratio ** (n - 1)
        q.append(2 * (-1) ** n * ((n + 1) * ratio**n + previous) / eps**2)
    d = [beta[n] - q[n] for n in range(n_max + 1)]

    # First verify that the pole sequence itself obeys the Riccati transform.
    for n in range(n_max + 1):
        jm1 = Fraction(0) if n == 0 else j[n - 1]
        square_n = convolution(j, j, n)
        square_m1 = Fraction(0) if n == 0 else convolution(j, j, n - 1)
        rhs_q = (
            -(n + 1) * j[n + 1]
            + (2 * n + 1) * j[n]
            - n * jm1
            + square_n
            - square_m1
        )
        assert rhs_q == q[n], ("pole", n, rhs_q, q[n])

    # Equation (10) of 104_13.
    for n in range(n_max + 1):
        cm1 = Fraction(0) if n == 0 else c[n - 1]
        jc_n = convolution(j, c, n)
        jc_m1 = Fraction(0) if n == 0 else convolution(j, c, n - 1)
        cc_n = convolution(c, c, n)
        cc_m1 = Fraction(0) if n == 0 else convolution(c, c, n - 1)
        rhs = (
            -(n + 1) * c[n + 1]
            + (2 * n + 1) * c[n]
            - n * cm1
            + 2 * (jc_n - jc_m1)
            + cc_n
            - cc_m1
        )
        assert rhs == d[n], ("centered", n, rhs, d[n])

    print("PASS: exact Selberg-Riccati degree recurrence n=0..8")
    print("PASS: exact double-pole subtraction and q_n formula")


if __name__ == "__main__":
    main()
