#!/usr/bin/env python3
"""Exact checks for 104_17 (no floating-point sign decisions).

The witness is rho=(1+2i)/5, hence w=2i.  We verify the Li-quartet
coefficients, the cumulative/triangular sums, and the equality between the
special and general rational forms of the Abel germ at several rational q.
"""

from fractions import Fraction as F


def quartet_q(n: int) -> F:
    """Q_n for w=2i, evaluated in exact rational arithmetic."""
    if n % 2:
        return F(4)
    real_part = ((-1) ** (n // 2)) * (F(2) ** n + F(1, 2) ** n)
    return F(4) - 2 * real_part


def abel_special(q: F) -> F:
    return 4 * q / (1 - q) + 8 * q * q / (1 + 4 * q * q) + 2 * q * q / (4 + q * q)


def abel_general(q: F) -> F:
    beta = F(1, 5)
    gamma = F(2, 5)
    x = q / (1 - q)
    big_x = (x + beta) * (x + 1 - beta) + gamma * gamma
    big_y = gamma * (1 - 2 * beta)
    return 2 * q * (1 + q) * big_x / ((1 - q) ** 3 * (big_x * big_x + big_y * big_y))


def main() -> None:
    expected = {
        1: F(4),
        2: F(25, 2),
        3: F(4),
        4: F(-225, 8),
        5: F(4),
        6: F(4225, 32),
        7: F(4),
        8: F(-65025, 128),
    }
    actual = {n: quartet_q(n) for n in range(1, 9)}
    assert actual == expected

    c4 = sum((actual[n] for n in range(1, 5)), F(0))
    f4 = sum(((5 - n) * actual[n] for n in range(1, 5)), F(0))
    f8 = sum(((9 - n) * actual[n] for n in range(1, 9)), F(0))
    assert c4 == F(-61, 8)
    assert f4 == F(267, 8)
    assert f8 == F(-10885, 128)

    for q in (F(1, 10), F(1, 4), F(2, 5)):
        special = abel_special(q)
        general = abel_general(q)
        assert special == general
        assert special > 0
        print(f"q={q}: Abel={special} > 0")

    print("CERTIFIED EXACT: Q4<0, C4<0, F4>0, F8<0")
    print("CERTIFIED EXACT: special Abel form equals theorem (8) on test rationals")


if __name__ == "__main__":
    main()
