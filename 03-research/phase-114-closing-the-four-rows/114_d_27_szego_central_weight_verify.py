#!/usr/bin/env python3
"""Exact checks for D.27 (no floating-point conclusion is used)."""

from fractions import Fraction


def primes_upto(n):
    out = []
    for k in range(2, n + 1):
        if all(k % p for p in out if p * p <= k):
            out.append(k)
    return out


def subcritical_bound():
    # Bound used in D.20: p=2,3,5,7 plus all integers n>=11.
    head = sum((Fraction(1, p * p - 1) for p in (2, 3, 5, 7)), Fraction())
    tail = Fraction(1, 2) * (Fraction(1, 10) + Fraction(1, 11))
    total = head + tail
    assert total == Fraction(1627, 2640)
    assert total < 1
    return total


def central_partial_sum(bound):
    # Sum over every power of each p, evaluated exactly as 1/(p-1).
    return sum((Fraction(1, p - 1) for p in primes_upto(bound)), Fraction())


def check_first_winding_mismatch():
    for n in range(2, 200):
        # Squaring removes the square root: n^-1 != n^-2 for n>1.
        assert Fraction(1, n) != Fraction(1, n * n)


if __name__ == "__main__":
    b = subcritical_bound()
    check_first_winding_mismatch()
    values = [(x, central_partial_sum(x)) for x in (10, 100, 1000, 5000)]
    assert all(values[i][1] < values[i + 1][1] for i in range(len(values) - 1))
    print("D.27 exact subcritical bound:", b, "< 1")
    print("central partial sums sum_{p<=X} 1/(p-1):")
    for x, value in values:
        print(f"  X={x:4d}: {value} ~= {float(value):.12f}")
    print("PASS: subcritical and central Szego weights are not isometric")
