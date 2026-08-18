#!/usr/bin/env python3
"""Finite sanity checks for the quantitative parts of 114.a.148."""

from math import comb, log


def main() -> None:
    for q in (3, 5, 7):
        for d in range(1, 16):
            n = 2**d
            Q = q**d
            assert Q >= n
            assert comb(n + Q - 1, n) >= 2 ** (n - 1)

    ratios = [((2**d - 1) * log(2)) / (2 * d * d) for d in range(8, 24)]
    assert all(a < b for a, b in zip(ratios, ratios[1:]))
    assert ratios[-1] > 1000

    c1 = 1 / (2 * log(3))
    for j in range(2, 10):
        cj = 1 / (2 * j * log(3))
        assert cj != c1 and cj > 0

    print("VERDICT: CURRENT-CARRIER TRILEMMA QUANTITATIVE CHECKS PASS")


if __name__ == "__main__":
    main()
