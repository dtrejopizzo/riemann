#!/usr/bin/env python3
"""Exact rational checks for the boundary--residue identity of 104_33.

Gaussian rationals are represented as pairs (real, imaginary) of Fraction.
No floating-point arithmetic is used.
"""

from fractions import Fraction as F


G = tuple[F, F]


def gadd(a: G, b: G) -> G:
    return (a[0] + b[0], a[1] + b[1])


def gneg(a: G) -> G:
    return (-a[0], -a[1])


def gsub(a: G, b: G) -> G:
    return gadd(a, gneg(b))


def gmul(a: G, b: G) -> G:
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def ginv(a: G) -> G:
    norm = a[0] * a[0] + a[1] * a[1]
    if norm == 0:
        raise ZeroDivisionError
    return (a[0] / norm, -a[1] / norm)


def gdiv(a: G, b: G) -> G:
    return gmul(a, ginv(b))


def gscale(c: F | int, a: G) -> G:
    return (F(c) * a[0], F(c) * a[1])


def gpow(a: G, n: int) -> G:
    if n < 0:
        return gpow(ginv(a), -n)
    out: G = (F(1), F(0))
    base = a
    exponent = n
    while exponent:
        if exponent & 1:
            out = gmul(out, base)
        base = gmul(base, base)
        exponent >>= 1
    return out


def fejer_laurent(w: G, n: int) -> G:
    total: G = (F(n), F(0))
    for d in range(1, n):
        pair = gadd(gpow(w, d), gpow(w, -d))
        total = gadd(total, gscale(n - d, pair))
    return total


def quartet_li(w: G, n: int) -> F:
    pair = gadd(gpow(w, n), gpow(w, -n))
    return F(4) - F(2) * pair[0]


def check_residue_identity() -> None:
    one: G = (F(1), F(0))
    w: G = (F(0), F(1, 2))
    rho = ginv(gsub(one, w))
    assert rho == (F(4, 5), F(2, 5))

    factor = gdiv(gmul(gsub(one, w), gsub(one, w)), w)
    for n in range(1, 21):
        lhs = gmul(factor, fejer_laurent(w, n))
        rhs = gsub(gadd(gpow(w, n), gpow(w, -n)), (F(2), F(0)))
        assert lhs == rhs, (n, lhs, rhs)
        residue_pair = F(2) * lhs[0]
        assert residue_pair == -quartet_li(w, n), n


def check_boundary_invariance() -> None:
    """Check Re Q'/Q=0 on the critical line for the rational quartet."""

    one: G = (F(1), F(0))
    half: G = (F(1, 2), F(0))
    w: G = (F(0), F(1, 2))
    rho = ginv(gsub(one, w))
    eta = gsub(rho, half)
    eta_bar = (eta[0], -eta[1])

    # In the centered variable x=s-1/2,
    # Q'/Q = 2x/(x^2-eta^2) + 2x/(x^2-conj(eta)^2).
    for t in (F(-7, 3), F(-1), F(0), F(2, 5), F(11, 4)):
        x: G = (F(0), t)
        two_x = gscale(2, x)
        first = gdiv(two_x, gsub(gmul(x, x), gmul(eta, eta)))
        second = gdiv(two_x, gsub(gmul(x, x), gmul(eta_bar, eta_bar)))
        ratio = gadd(first, second)
        assert ratio[0] == 0, (t, ratio)


def main() -> None:
    check_residue_identity()
    check_boundary_invariance()
    print("PASS: exact Gaussian-rational boundary/residue identities")
    print("PASS: right-half-plane residue pair equals minus quartet Li term")
    print("PASS: reciprocal quartet leaves the real critical-line symbol unchanged")
    print("STOP: a boundary-only estimate omits the RH-sensitive interior residues")


if __name__ == "__main__":
    main()
