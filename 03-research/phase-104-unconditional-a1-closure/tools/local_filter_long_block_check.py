#!/usr/bin/env python3
"""Exact checks for 104_65 (stdlib only)."""

from fractions import Fraction
from math import log


Gaussian = tuple[Fraction, Fraction]


def gadd(x: Gaussian, y: Gaussian) -> Gaussian:
    return (x[0] + y[0], x[1] + y[1])


def gmul(x: Gaussian, y: Gaussian) -> Gaussian:
    return (x[0] * y[0] - x[1] * y[1],
            x[0] * y[1] + x[1] * y[0])


def gpow(x: Gaussian, n: int) -> Gaussian:
    out: Gaussian = (Fraction(1), Fraction(0))
    base = x
    while n:
        if n & 1:
            out = gmul(out, base)
        base = gmul(base, base)
        n //= 2
    return out


def peval(coeffs: list[Fraction], z: Gaussian) -> Gaussian:
    out: Gaussian = (Fraction(0), Fraction(0))
    for c in reversed(coeffs):
        out = gadd(gmul(out, z), (c, Fraction(0)))
    return out


W: Gaussian = (Fraction(0), Fraction(2))
WINV: Gaussian = (Fraction(0), Fraction(-1, 2))


def quartet(n: int) -> Fraction:
    wn = gpow(W, n)
    win = gpow(WINV, n)
    return Fraction(4) - 2 * (wn[0] + win[0])


def filtered_direct(coeffs: list[Fraction], n: int) -> Fraction:
    return sum((c * quartet(n + h) for h, c in enumerate(coeffs)),
               Fraction(0))


def filtered_formula(coeffs: list[Fraction], n: int) -> Fraction:
    p1 = sum(coeffs, Fraction(0))
    pw = peval(coeffs, W)
    pwinv = peval(coeffs, WINV)
    term = gadd(gmul(gpow(W, n), pw), gmul(gpow(WINV, n), pwinv))
    return 4 * p1 - 2 * term[0]


def binomial(n: int, k: int) -> int:
    if k < 0 or k > n:
        return 0
    k = min(k, n - k)
    out = 1
    for j in range(1, k + 1):
        out = out * (n - k + j) // j
    return out


def difference_poly(k: int) -> list[Fraction]:
    return [Fraction(binomial(k, h) * ((-1) ** (k - h)))
            for h in range(k + 1)]


def moving_average_poly(j: int) -> list[Fraction]:
    return [Fraction(1, j + 1) for _ in range(j + 1)]


def positive_residue(pw: Gaussian) -> int:
    """Return r with Re(i^r P(2i)) > 0."""
    i: Gaussian = (Fraction(0), Fraction(1))
    vals = [(gmul(gpow(i, r), pw)[0], r) for r in range(4)]
    value, residue = max(vals)
    assert value > 0
    return residue


def check_filter_family(coeffs: list[Fraction]) -> None:
    pw = peval(coeffs, W)
    assert pw != (0, 0)
    r = positive_residue(pw)
    n = 96 + r
    assert n % 4 == r
    assert filtered_direct(coeffs, n) == filtered_formula(coeffs, n)
    assert filtered_direct(coeffs, n) < -1


def main() -> None:
    # Raw quartet and the four-step obstruction.
    for n in range(1, 81):
        if n % 4 == 0:
            assert quartet(n) < -1
            assert -quartet(n) >= 2 ** n
        else:
            assert quartet(n) >= 4
    for start in range(4, 77):
        assert any(quartet(n) < -1 for n in range(start, start + 4))

    # Formula (18) for several unrelated rational filters.
    filters = [
        [Fraction(3, 5), Fraction(-7, 11), Fraction(2, 3)],
        [Fraction(-2), Fraction(0), Fraction(5), Fraction(1, 7)],
        [Fraction(1), Fraction(4)],
    ]
    for coeffs in filters:
        for n in range(1, 30):
            assert filtered_direct(coeffs, n) == filtered_formula(coeffs, n)

    # Fixed differences and fixed moving averages retain a periodic
    # exponentially negative residue class.
    for k in range(0, 13):
        check_filter_family(difference_poly(k))
    for j in range(0, 13):
        check_filter_family(moving_average_poly(j))

    # Exact annihilator P(z)=z^2+4.
    annihilator = [Fraction(4), Fraction(0), Fraction(1)]
    assert peval(annihilator, W) == (0, 0)
    for n in range(1, 81):
        lhs = filtered_direct(annihilator, n)
        rhs = Fraction(20) - Fraction(15, 2) * gpow(WINV, n)[0]
        assert lhs == rhs
        assert lhs > 0

    # Logarithmic density of 4N and the limiting exponential rate.
    for x in (100, 1000, 10000):
        harmonic = sum((Fraction(1, n) for n in range(1, x + 1)),
                       Fraction(0))
        bad = sum((Fraction(1, n) for n in range(4, x + 1, 4)),
                  Fraction(0))
        ratio = float(bad / harmonic)
        print(f"X={x:5d} harmonic_bad_ratio={ratio:.9f}")

    rates = [log(float(-quartet(n))) / n for n in range(4, 81, 4)]
    print(f"last_bad_rate={rates[-1]:.12f} log2={log(2):.12f}")
    assert abs(rates[-1] - log(2)) < 0.02
    print("local_filter_long_block_check: PASS")


if __name__ == "__main__":
    main()
