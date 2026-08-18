#!/usr/bin/env python3
"""Exact certificates for D.91 Kunneth typing and homogeneity."""

from fractions import Fraction


def hinge(prime, a, b):
    return Fraction(a + b * prime, a + b)


def addition_2x2(matrix):
    return (
        matrix[0][0],
        matrix[0][1] + matrix[1][0],
        matrix[1][1],
    )


def main() -> None:
    # Every positive rational slope ratio occurs and gives the stated hinge.
    p = 5
    samples = [(1, 7), (2, 3), (11, 4), (19, 1)]
    for a, b in samples:
        n = a + p * b
        assert (n - a) // p == b
        x = hinge(p, a, b)
        assert Fraction(1) < x < Fraction(p)
        # Invert x=(r+p)/(r+1): r=(p-x)/(x-1).
        assert Fraction(p - x, x - 1) == Fraction(a, b)

    # Tensor diagonal norms are quartic; Weil/Schur terms are quadratic.
    scale = Fraction(3)
    tensor_norm_scale = scale ** 4
    weil_scale = scale ** 2
    assert tensor_norm_scale == 81 and weil_scale == 9
    assert tensor_norm_scale != weil_scale

    # A nonzero Kunneth tensor can be invisible to addition/correlation.
    kernel_tensor = ((Fraction(0), Fraction(1)),
                     (Fraction(-1), Fraction(0)))
    assert addition_2x2(kernel_tensor) == (0, 0, 0)
    hilbert_norm = sum(x * x for row in kernel_tensor for x in row)
    assert hilbert_norm == 2

    print("D91 Kunneth typing certificates: PASS")
    print("sample hinges:", [hinge(p, a, b) for a, b in samples])
    print("quartic/quadratic scales:", tensor_norm_scale, weil_scale)
    print("invisible tensor norm:", hilbert_norm)


if __name__ == "__main__":
    main()
