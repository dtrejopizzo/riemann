#!/usr/bin/env python3
"""Exact finite certificates for D.122 dyadic contact-frame audit."""

from fractions import Fraction


def main() -> None:
    # At zero frequency every translation phase is one: l1 mass, no l2 gain.
    weights = [Fraction(1, 2), Fraction(2, 3), Fraction(3, 5)]
    l1 = sum(weights)
    multiplier_zero = 2 * l1
    l2_square = sum(w*w for w in weights)
    assert multiplier_zero == Fraction(53, 15)
    assert l1*l1 > l2_square

    # The coherent Gram matrix vv^T has eigenvalue ||v||^2=sum weights.
    # Verify Gv=(sum weights)v without irrational square roots by using the
    # weighted-coordinate form G_ij=w_j on the constant phase direction.
    gram = [[weights[j] for j in range(len(weights))]
            for _ in range(len(weights))]
    ones = [Fraction(1)] * len(weights)
    image = [sum(gram[i][j] * ones[j] for j in range(len(weights)))
             for i in range(len(weights))]
    assert image == [l1] * len(weights)

    # Primitive does not mean ordinary mean zero.  Algebraically,
    # F=(D^2-1/4)u has Fhat(0)=-uhat(0)/4.
    uhat_zero = Fraction(7)
    fhat_zero = -uhat_zero / 4
    assert fhat_zero == Fraction(-7, 4) != 0

    # Gamma low-frequency strength is quadratic, so batch/Gamma ratio blows
    # up like W/tau^2 in a rational sample sequence.
    ratios = [l1 / Fraction(1, k*k) for k in (2, 4, 8, 16)]
    assert all(ratios[i+1] > ratios[i] for i in range(len(ratios)-1))

    print("D122 dyadic contact-frame certificates: PASS")
    print("coherent l1 multiplier / l2 square:", multiplier_zero, l2_square)
    print("primitive real-zero value:", fhat_zero)
    print("batch/Gamma low-frequency ratios:", ratios)


if __name__ == "__main__":
    main()
