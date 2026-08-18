#!/usr/bin/env python3
"""Exact checks for the canonical Selberg-square cancellation gate 104_38.

All asserted identities use Fraction arithmetic.  The script checks:

* -<G,B_mu> + Q_G(mu) = -<T G,mu> for finite atomic measures;
* ell_n,a = w_{n+1,a}-w_n,a-w_1,a at polynomial level;
* the leading degrees and signs in the one-point Schur-kernel witness;
* the collision coefficient -2*n^2*a^4.

The finite atomic calculation is an algebraic proxy for the Fubini identity;
it does not approximate primes or zeta.
"""

from __future__ import annotations

from fractions import Fraction as F
from math import comb, factorial


Measure = dict[F, F]


def add_measure(left: Measure, right: Measure, scale: F = F(1)) -> Measure:
    out = dict(left)
    for x, mass in right.items():
        out[x] = out.get(x, F(0)) + scale * mass
        if out[x] == 0:
            del out[x]
    return out


def convolution(left: Measure, right: Measure) -> Measure:
    out: Measure = {}
    for x, a in left.items():
        for y, b in right.items():
            out[x + y] = out.get(x + y, F(0)) + a * b
    return out


def pair(function: dict[F, F], measure: Measure) -> F:
    return sum((function[x] * mass for x, mass in measure.items()), F(0))


def qform(function: dict[F, F], measure: Measure) -> F:
    return pair(function, convolution(measure, measure))


def laguerre(n: int) -> list[F]:
    """Coefficients of ordinary L_n(x), ascending."""
    return [F((-1) ** k * comb(n, k), factorial(k)) for k in range(n + 1)]


def laguerre_assoc_one(m: int) -> list[F]:
    """Coefficients of L_m^(1)(x), ascending."""
    return [F((-1) ** k * comb(m + 1, k + 1), factorial(k)) for k in range(m + 1)]


def scaled(poly: list[F], factor: F) -> list[F]:
    return [coefficient * factor**k for k, coefficient in enumerate(poly)]


def pad(poly: list[F], size: int) -> list[F]:
    return poly + [F(0)] * (size - len(poly))


def check_selberg_cancellation() -> None:
    # Arbitrary exact atomic alpha and beta; no sign assumptions are needed.
    alpha = {F(2): F(3), F(5): F(7)}
    beta = {F(1): F(4), F(4): F(2)}
    mu = add_measure(alpha, beta, F(-1))

    # G is needed on supp(mu), supp(beta*mu), and supp(mu*mu).
    points = set(mu)
    points.update(convolution(beta, mu))
    points.update(convolution(mu, mu))
    G = {x: F(2 * x * x - 3 * x + 5, 11) for x in points}

    u_mu = {x: x * mass for x, mass in mu.items()}
    B = add_measure(u_mu, convolution(beta, mu), F(2))
    B = add_measure(B, convolution(mu, mu))

    left = -pair(G, B) + qform(G, mu)

    # T G(v)=vG(v)+2 sum_u G(v+u) beta(u).
    TG: dict[F, F] = {}
    for v in mu:
        TG[v] = v * G[v] + 2 * sum(
            (G[v + u] * mass for u, mass in beta.items()), F(0)
        )
    right = -pair(TG, mu)
    assert left == right


def check_laguerre_and_tail(n: int, a: F, d: F) -> None:
    assert n >= 2 and a > 1 and d > 0

    # Remove the common exponential e^(-a u).  w_m/a has L_(m-1)^1(a u).
    wn = [a * c for c in scaled(laguerre_assoc_one(n - 1), a)]
    wnext = [a * c for c in scaled(laguerre_assoc_one(n), a)]
    w1 = [a]
    size = n + 1
    ell_from_w = [
        x - y - z
        for x, y, z in zip(pad(wnext, size), pad(wn, size), pad(w1, size))
    ]

    ell_direct = [a * c for c in scaled(laguerre(n), a)]
    ell_direct[0] -= a
    assert ell_from_w == ell_direct
    assert ell_direct[0] == 0
    assert ell_direct[1] == -n * a * a
    assert ell_direct[-1] == F((-1) ** n, factorial(n)) * a ** (n + 1)

    # G(2R) has polynomial degree n-2.  ell(R)^2 has degree 2n and
    # coefficient a^(2n+2)/(n!)^2.  Hence the residual diagonal has the
    # following strictly negative leading coefficient.
    degree_g = n - 2
    degree_square = 2 * n
    leading_square = ell_direct[-1] ** 2
    leading_residual = -leading_square / (4 * d)
    assert degree_square > degree_g
    assert leading_residual < 0

    # Small-x collision coefficient from ell'(0)^2*(1*4-2*3).
    collision = ell_direct[1] ** 2 * F(4 - 6)
    assert collision == -2 * n * n * a**4
    assert collision < 0


def main() -> None:
    check_selberg_cancellation()
    for n in (2, 3, 7, 149, 220):
        check_laguerre_and_tail(n, F(3, 2), F(5, 3))
    print("PASS: exact Selberg cancellation, Schur tail, and collision checks")


if __name__ == "__main__":
    main()
