#!/usr/bin/env python3
"""Certificates for the D.88 Bloch--Floquet and Kunneth audit."""

from fractions import Fraction
import cmath


def discrete_zak(f, cell):
    """Unitary finite Zak analogue: DFT along lattice translates."""
    blocks = len(f) // cell
    out = [[0j for _ in range(cell)] for _ in range(blocks)]
    scale = blocks ** -0.5
    for theta in range(blocks):
        for x in range(cell):
            out[theta][x] = scale * sum(
                f[x + k * cell] *
                cmath.exp(2j * cmath.pi * k * theta / blocks)
                for k in range(blocks)
            )
    return out


def norm2(values):
    if values and isinstance(values[0], list):
        return sum(abs(z) ** 2 for row in values for z in row)
    return sum(abs(z) ** 2 for z in values)


def addition_pushforward_norm2(n):
    counts = list(range(1, n + 1)) + list(range(n - 1, 0, -1))
    return Fraction(sum(k * k for k in counts), n * n)


def main() -> None:
    # Finite Zak unitarity and deck diagonalization.
    cell = 3
    blocks = 4
    f = [complex(k + 1, (-1) ** k) for k in range(cell * blocks)]
    zf = discrete_zak(f, cell)
    assert abs(norm2(f) - norm2(zf)) < 1e-10

    # S_cell f(t)=f(t-cell) cyclically becomes the character multiplier.
    shifted = [f[(j - cell) % len(f)] for j in range(len(f))]
    zshift = discrete_zak(shifted, cell)
    for theta in range(blocks):
        character = cmath.exp(2j * cmath.pi * theta / blocks)
        for x in range(cell):
            assert abs(zshift[theta][x] - character * zf[theta][x]) < 1e-10

    # Exact triangular blow-up for the Kunneth-to-addition map.
    for n in (1, 2, 5, 20):
        exact = addition_pushforward_norm2(n)
        assert exact == Fraction(2 * n, 3) + Fraction(1, 3 * n)
    assert addition_pushforward_norm2(20) > 13

    # Closed Poisson multiplier contains the full power series at chi=1.
    r = Fraction(1, 3)
    poisson_at_one = (1 + r) / (1 - r)
    geometric_full = 1 + 2 * r / (1 - r)
    assert poisson_at_one == geometric_full == 2

    print("D88 Bloch--Floquet certificates: PASS")
    print("finite Zak norm squared:", round(norm2(zf), 12))
    print("addition norm squared N=20:", addition_pushforward_norm2(20))
    print("full Poisson tower at r=1/3:", poisson_at_one)


if __name__ == "__main__":
    main()
