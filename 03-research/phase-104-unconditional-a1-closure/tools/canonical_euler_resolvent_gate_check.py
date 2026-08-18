#!/usr/bin/env python3
"""Exact algebra and a non-certifying divergence table for 104_40."""

from fractions import Fraction as F
from math import asinh, log


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


def g_pow(x: Gaussian, n: int) -> Gaussian:
    out: Gaussian = (F(1), F(0))
    base = x
    while n:
        if n & 1:
            out = g_mul(out, base)
        base = g_mul(base, base)
        n //= 2
    return out


def norm_sq(x: Gaussian) -> F:
    return x[0] * x[0] + x[1] * x[1]


def check_offline_crossing() -> None:
    one: Gaussian = (F(1), F(0))
    half: Gaussian = (F(1, 2), F(0))
    w: Gaussian = (F(0), F(1, 2))
    rho = g_inv(g_sub(one, w))
    assert rho == (F(4, 5), F(2, 5))
    assert 2 * rho[0] == F(8, 5)
    assert g_sub(rho, half)[0] == F(3, 10)
    assert g_sub(one, g_inv(rho)) == w

    n = 152
    wn = g_pow(w, n)
    assert wn == (F(1, 2 ** n), F(0))
    multiplier = g_sub(one, wn)
    assert multiplier == (F(1) - F(1, 2 ** n), F(0))
    assert multiplier[0] > 0


def check_young_minimization() -> None:
    # For z=x+iy, r|z|^2+r^{-1} >= 2|z|.
    samples: tuple[Gaussian, ...] = (
        (F(3, 5), F(4, 5)),
        (F(-7, 4), F(1, 3)),
        (F(5, 2), F(-2, 7)),
    )
    multipliers = (F(1, 7), F(1, 2), F(1), F(3), F(11))
    for z in samples:
        z2 = norm_sq(z)
        # Avoid irrational square roots in the exact gate by squaring the
        # equivalent AM-GM statement (r*z2 + 1/r)^2 >= 4*z2.
        for r in multipliers:
            lhs = r * z2 + F(1, 1) / r
            assert lhs * lhs >= 4 * z2

    # An exact equality sample with |z|=5/2 and r=2/5.
    z = (F(3, 2), F(2))
    z2 = norm_sq(z)
    assert z2 == F(25, 4)
    r = F(2, 5)
    cost = r * z2 + F(1) / r
    assert cost == F(5)
    assert cost * cost == 4 * z2


def check_nonresonant_critical_model() -> None:
    # rho=1/2+i gives w=1-1/rho=(3+4i)/5.  A root of unity with
    # rational real part 3/5 is impossible; the finite exact checks below
    # cover the phase indices and exercise the Gaussian arithmetic.
    one: Gaussian = (F(1), F(0))
    rho: Gaussian = (F(1, 2), F(1))
    w = g_sub(one, g_inv(rho))
    assert w == (F(3, 5), F(4, 5))
    assert norm_sq(w) == 1
    for n in (149, 150, 151, 152, 220, 500):
        assert g_pow(w, n) != one


def divergence_table() -> None:
    print("critical-pole model integral I(delta)=2 asinh(1/delta):")
    previous = 0.0
    for k in (2, 4, 6, 8, 10, 12):
        delta = 10.0 ** (-k)
        value = 2.0 * asinh(1.0 / delta)
        asymptotic = 2.0 * log(2.0 / delta)
        assert value > previous
        previous = value
        print(
            f"  delta=1e-{k:02d}  I={value:.12f}  "
            f"I-2log(2/delta)={value-asymptotic:+.3e}"
        )


def main() -> None:
    check_offline_crossing()
    check_young_minimization()
    check_nonresonant_critical_model()
    divergence_table()
    print("offline crossing and residue multiplier: exact PASS")
    print("positive-multiplier Young optimum: exact PASS")
    print("104_40 canonical Euler resolvent gate: PASS")


if __name__ == "__main__":
    main()
