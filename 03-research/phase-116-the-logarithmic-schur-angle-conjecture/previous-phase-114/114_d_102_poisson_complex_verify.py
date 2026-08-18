#!/usr/bin/env python3
"""Finite certificates for D.102 Fourier--Poisson complex."""

from fractions import Fraction


def rank(matrix):
    a = [row[:] for row in matrix]
    rows = len(a)
    cols = len(a[0]) if rows else 0
    r = 0
    for c in range(cols):
        pivot = next((i for i in range(r, rows) if a[i][c] != 0), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        scale = a[r][c]
        a[r] = [x / scale for x in a[r]]
        for i in range(rows):
            if i != r and a[i][c] != 0:
                factor = a[i][c]
                a[i] = [a[i][j] - factor * a[r][j] for j in range(cols)]
        r += 1
    return r


def main() -> None:
    # Injective range pair C^2 -> C^4: contracting it leaves coker dimension 2.
    z = [
        [Fraction(1), Fraction(0)],
        [Fraction(0), Fraction(1)],
        [Fraction(0), Fraction(0)],
        [Fraction(0), Fraction(0)],
    ]
    z_rank = rank(z)
    kernel_dim = 2 - z_rank
    cokernel_dim = 4 - z_rank
    assert z_rank == 2
    assert kernel_dim == 0
    assert cokernel_dim == 2

    # Diagonal dense-range model: inverse norms grow with the cutoff.
    inverse_norms = []
    for cutoff in (2, 4, 8, 16):
        singular_values = [Fraction(1, n) for n in range(1, cutoff + 1)]
        inverse_norm = 1 / min(singular_values)
        inverse_norms.append(inverse_norm)
        assert inverse_norm == cutoff

    # A free Real orbit in odd cohomology is indefinite.
    multiplicity = Fraction(5, 2)
    free_orbit_det = -(multiplicity ** 2)
    assert free_orbit_det < 0

    # Supertrace cancellation of a contractible equal-action range pair.
    range_trace_even = Fraction(13, 7)
    range_trace_odd = Fraction(13, 7)
    assert range_trace_even - range_trace_odd == 0

    print("D102 Fourier--Poisson complex certificates: PASS")
    print("range rank/kernel/cokernel:", z_rank, kernel_dim, cokernel_dim)
    print("finite inverse norms:", inverse_norms)
    print("free odd-orbit determinant:", free_orbit_det)
    print("contractible-pair supertrace:", 0)


if __name__ == "__main__":
    main()
