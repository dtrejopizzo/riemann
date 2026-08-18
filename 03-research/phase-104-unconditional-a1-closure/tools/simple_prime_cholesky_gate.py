#!/usr/bin/env python3
"""Exact checks for 104_36 (Fraction only, no zeta numerics)."""

from fractions import Fraction as F
from math import comb, factorial


Gaussian = tuple[F, F]


def g_add(x: Gaussian, y: Gaussian) -> Gaussian:
    return (x[0] + y[0], x[1] + y[1])


def g_sub(x: Gaussian, y: Gaussian) -> Gaussian:
    return (x[0] - y[0], x[1] - y[1])


def g_mul(x: Gaussian, y: Gaussian) -> Gaussian:
    return (x[0] * y[0] - x[1] * y[1],
            x[0] * y[1] + x[1] * y[0])


def g_inv(x: Gaussian) -> Gaussian:
    den = x[0] * x[0] + x[1] * x[1]
    assert den
    return (x[0] / den, -x[1] / den)


def g_div(x: Gaussian, y: Gaussian) -> Gaussian:
    return g_mul(x, g_inv(y))


def g_pow(x: Gaussian, n: int) -> Gaussian:
    out: Gaussian = (F(1), F(0))
    base = x
    while n:
        if n & 1:
            out = g_mul(out, base)
        base = g_mul(base, base)
        n //= 2
    return out


def laguerre_laplace_sum(n: int, s: F) -> F:
    """Integral exp(-s*x) L_{n-1}^{(1)}(x) dx by coefficients."""
    return sum(
        F((-1) ** k * comb(n, k + 1) * factorial(k), factorial(k))
        / s ** (k + 1)
        for k in range(n)
    )


def laguerre_laplace_closed(n: int, s: F) -> F:
    return F(1) - ((s - 1) / s) ** n


def check_laguerre_transforms() -> None:
    for n in range(1, 13):
        for s in (F(3, 2), F(5, 3), F(7, 4)):
            direct = laguerre_laplace_sum(n, s)
            closed = laguerre_laplace_closed(n, s)
            assert direct == closed, (n, s, direct, closed)

        # Continuous pole in (9), tested at two safe rational regulators.
        for a in (F(3), F(7, 2)):
            q = (a - 1) / a
            integral = laguerre_laplace_sum(n, q)
            expected = F(1) + F((-1) ** (n + 1), 1) / (a - 1) ** n
            assert integral == expected, (n, a, integral, expected)


def check_offline_quartet() -> None:
    one: Gaussian = (F(1), F(0))
    half: Gaussian = (F(1, 2), F(0))
    w: Gaussian = (F(0), F(1, 2))
    rho = g_inv(g_sub(one, w))
    assert rho == (F(4, 5), F(2, 5))
    assert g_sub(rho, half)[0] == F(3, 10)

    # The Cayley identity 1 - 1/rho = w.
    assert g_sub(one, g_inv(rho)) == w

    n = 152
    wn = g_pow(w, n)
    assert wn == (F(1, 2 ** n), F(0))

    zrho = g_sub(rho, half)
    cayley_from_z = g_div(g_sub(zrho, half), g_add(zrho, half))
    assert cayley_from_z == w

    # G_n(zrho) = 1 - w^n is the exact residue multiplier.
    residue_multiplier = g_sub(one, g_pow(cayley_from_z, n))
    assert residue_multiplier == (F(1) - F(1, 2 ** n), F(0))
    assert residue_multiplier[0] > 0

    # Li contribution of the reciprocal quartet:
    # Q_n = 4 - 2 Re(w^n + w^{-n}) < 0.
    winv_n = g_pow(g_inv(w), n)
    qn = F(4) - 2 * (wn[0] + winv_n[0])
    assert qn == F(4) - 2 * (F(1, 2 ** n) + F(2 ** n))
    assert qn < 0

    print("offline quartet:")
    print(f"  rho = {rho[0]} + {rho[1]} i")
    print(f"  Re(rho)-1/2 = {zrho[0]}")
    print(f"  G_{n}(rho-1/2) = {residue_multiplier[0]}")
    print(f"  quartet Li contribution Q_{n} < 0: {qn < 0}")


def main() -> None:
    check_laguerre_transforms()
    check_offline_quartet()
    print("Laguerre Laplace identities: exact checks passed for n=1..12")
    print("104_36 exact algebra: PASS")


if __name__ == "__main__":
    main()
