#!/usr/bin/env python3
"""Exact certificates for D.108 hard-Lefschetz transport audit."""

from fractions import Fraction


def determinant_2(a):
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]


def main() -> None:
    # Numerical ruling primitive: d2=-d1 gives -2 d1^2.
    d1 = Fraction(7, 3)
    d2 = -d1
    primitive_form = 2 * d1 * d2
    assert d1 + d2 == 0
    assert primitive_form == -2 * d1 * d1 < 0

    # Compare sum-depth and difference-depth prime kernels at p=4 so all
    # entries are rational; the rank statement is independent of primality.
    p = Fraction(4)
    root_p = Fraction(2)
    sum_kernel = [
        [1 / p, 1 / (p * root_p)],
        [1 / (p * root_p), 1 / (p * p)],
    ]
    diff_kernel = [
        [Fraction(1), 1 / root_p],
        [1 / root_p, Fraction(1)],
    ]
    det_sum = determinant_2(sum_kernel)
    det_diff = determinant_2(diff_kernel)
    assert det_sum == 0
    assert det_diff == Fraction(3, 4) > 0

    # Invertible diagonal torsor congruence preserves the zero determinant.
    scales = [Fraction(3), Fraction(5)]
    rescaled_sum = [
        [scales[i] * sum_kernel[i][j] * scales[j] for j in range(2)]
        for i in range(2)
    ]
    assert determinant_2(rescaled_sum) == 0

    print("D108 hard-Lefschetz transport certificates: PASS")
    print("ruling primitive form:", primitive_form)
    print("sum/difference kernel determinants:", det_sum, det_diff)
    print("torsor-rescaled sum determinant:", determinant_2(rescaled_sum))


if __name__ == "__main__":
    main()
