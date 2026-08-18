#!/usr/bin/env python3
"""Exact finite certificates for D.93 Ronkin/Monge--Ampere audit."""

from fractions import Fraction


def main() -> None:
    # Uniform three-state softmax Hessian, beta=3:
    # beta*(diag(1/3) - (1/3)(1/3)^T).
    beta = Fraction(3)
    n = 3
    h = [
        [beta * ((Fraction(1, n) if i == j else 0) - Fraction(1, n * n))
         for j in range(n)]
        for i in range(n)
    ]
    assert all(sum(row) == 0 for row in h)
    assert all(h[i][j] < 0 for i in range(n) for j in range(n) if i != j)
    v = [Fraction(1), Fraction(-2), Fraction(4)]
    q = sum(v[i] * h[i][j] * v[j] for i in range(n) for j in range(n))
    assert q > 0

    # Exact prime symbol comparison at r=1/2 and L=1.
    r = Fraction(1, 2)
    p_one = (1 + r) / (1 - r)
    p_minus_one = (1 - r) / (1 + r)
    desired_zero = p_one - 1
    desired_pi = p_minus_one - 1
    lap_zero = p_one - p_one
    lap_pi = p_minus_one - p_one
    missing_mass = p_one - 1
    assert desired_zero == 2 > 0
    assert desired_pi == Fraction(-2, 3) < 0
    assert lap_zero == 0
    assert lap_pi == Fraction(-8, 3) < 0
    assert desired_zero - lap_zero == missing_mass
    assert desired_pi - lap_pi == missing_mass

    # Exact Kunneth factorization of a positive partition sum.
    a = [Fraction(2), Fraction(3), Fraction(5)]
    b = [Fraction(7), Fraction(11)]
    product_partition = sum(x * y for x in a for y in b)
    factored_partition = sum(a) * sum(b)
    assert product_partition == factored_partition

    print("D93 tropical Monge--Ampere certificates: PASS")
    print("softmax row sums:", [sum(row) for row in h])
    print("softmax test quadratic:", q)
    print("desired symbol at 0, pi:", desired_zero, desired_pi)
    print("natural Laplacian at 0, pi:", lap_zero, lap_pi)
    print("exact missing mass:", missing_mass)


if __name__ == "__main__":
    main()
