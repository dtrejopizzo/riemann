#!/usr/bin/env python3
"""Checks for 104_98: finite Mellin energy and the zero-cross sign.

Only Python's standard library and numpy are used.  The finite max-kernel
identity is checked exactly with Fraction.  The arithmetic row uses the
literal prime indicator and Gauss--Legendre quadrature only for Li_2.
The last two checks concern the local logarithmic monodromy model; they do
not use numerical zeta zeros as an input to a theorem.
"""

from __future__ import annotations

from fractions import Fraction
import cmath
import math

import numpy as np


def exact_finite_identity() -> None:
    # Arbitrary rational increments; this checks all boundary signs.
    aa = {
        2: Fraction(3, 5),
        3: Fraction(-7, 11),
        4: Fraction(5, 13),
        5: Fraction(2, 7),
        6: Fraction(-4, 9),
        7: Fraction(1, 8),
    }
    nmax = max(aa)
    pp: dict[int, Fraction] = {}
    running = Fraction(0)
    for m in range(2, nmax + 1):
        running += aa[m]
        pp[m] = running

    direct = sum(pp[m] * pp[m] / Fraction(m * (m + 1))
                 for m in range(2, nmax + 1))
    kernel = Fraction(0)
    for r in range(2, nmax + 1):
        for q in range(2, nmax + 1):
            kernel += aa[r] * aa[q] * (
                Fraction(1, max(r, q)) - Fraction(1, nmax + 1)
            )
    assert direct == kernel

    # Phi_N(s) has these two algebraically identical descriptions.
    for s in (0.73 + 0.41j, 1.27 + 2.3j, 2.0 - 0.8j):
        lhs = sum(float(pp[m]) * (m ** (-s) - (m + 1) ** (-s))
                  for m in range(2, nmax + 1))
        rhs = sum(float(aa[m]) * m ** (-s) for m in range(2, nmax + 1))
        rhs -= float(pp[nmax]) * (nmax + 1) ** (-s)
        assert abs(lhs - rhs) < 3e-15

    print(f"exact rational finite energy = {float(direct):.15g}")


def primes_upto(n: int) -> np.ndarray:
    sieve = np.ones(n + 1, dtype=bool)
    sieve[:2] = False
    for p in range(2, int(math.isqrt(n)) + 1):
        if sieve[p]:
            sieve[p * p:n + 1:p] = False
    return sieve


def li2_integer_values(nmax: int) -> np.ndarray:
    # 24-point Gauss--Legendre on each unit interval [m-1,m].
    nodes, weights = np.polynomial.legendre.leggauss(24)
    out = np.zeros(nmax + 1, dtype=np.longdouble)
    running = np.longdouble(0.0)
    for m in range(3, nmax + 1):
        mid = np.longdouble(m - 0.5)
        xx = mid + np.longdouble(0.5) * nodes.astype(np.longdouble)
        inc = np.longdouble(0.5) * np.sum(
            weights.astype(np.longdouble) / np.log(xx), dtype=np.longdouble
        )
        running += inc
        out[m] = running
    return out


def arithmetic_boundary_check() -> None:
    nmax = 160
    isp = primes_upto(nmax)
    li = li2_integer_values(nmax)
    pi = np.cumsum(isp, dtype=np.int64)
    pp = pi.astype(np.longdouble) - li
    pp[0:2] = 0.0
    # P_2=1, since Li_2(2)=0.
    pp[2] = 1.0

    aa = np.zeros(nmax + 1, dtype=np.longdouble)
    aa[2] = pp[2]
    aa[3:] = pp[3:] - pp[2:-1]
    direct = np.sum(pp[2:] ** 2 /
                    (np.arange(2, nmax + 1, dtype=np.longdouble) *
                     np.arange(3, nmax + 2, dtype=np.longdouble)),
                    dtype=np.longdouble)

    idx = np.arange(2, nmax + 1)
    maxmat = np.maximum(idx[:, None], idx[None, :]).astype(np.longdouble)
    kernel = 1.0 / maxmat - np.longdouble(1.0 / (nmax + 1))
    via_kernel = aa[2:] @ kernel @ aa[2:]
    err = abs(direct - via_kernel)
    assert err < np.longdouble("3e-16")
    print(f"literal-prime finite energy N={nmax}: {float(direct):.15g}")
    print(f"finite boundary/kernel discrepancy: {float(err):.3e}")


def exp_integral(alpha: float, omega: float, a: float, b: float) -> complex:
    z = complex(alpha, omega)
    return (cmath.exp(z * b) - cmath.exp(z * a)) / z


def signed_zero_cross_check() -> None:
    # A conjugate pair contributes q(y)=2 Re(c exp(i gamma y)).  Its square
    # splits into a positive diagonal and a cross term with no fixed sign.
    beta = 0.65
    gamma = 7.0
    alpha = 2.0 * beta - 1.0
    c = -1.0 / complex(beta, gamma)
    h = 1.0

    best = None
    for y in np.linspace(0.0, 40.0, 20001):
        diag = 2.0 * abs(c) ** 2 * exp_integral(alpha, 0.0, y, y + h).real
        cross = 2.0 * (c * c * exp_integral(alpha, 2.0 * gamma,
                                             y, y + h)).real
        total = diag + cross
        if best is None or cross < best[0]:
            best = (cross, diag, total, y)
    assert best is not None
    cross, diag, total, y = best
    assert cross < 0.0 and total >= -2e-14 and abs((diag + cross) - total) < 1e-14
    print("conjugate-zero square at a block with negative cross:")
    print(f"  Y={y:.6f}, diagonal={diag:.12g}, cross={cross:.12g}, total={total:.12g}")


def monodromy_hardy_floor_check() -> None:
    # For log(re^{i theta})=log r+i theta, all negative Fourier modes are
    # fixed: coefficient m/k at mode -k.  An analytic polynomial can alter
    # only nonnegative modes.  The partial negative-mode energy tends to
    # m^2*pi^2/6.
    multiplicity = 3
    kmax = 200000
    kk = np.arange(1, kmax + 1, dtype=np.longdouble)
    partial = np.sum((np.longdouble(multiplicity) / kk) ** 2,
                     dtype=np.longdouble)
    target = np.longdouble(multiplicity ** 2) * np.longdouble(math.pi ** 2 / 6.0)
    # Integral-test tail: sum_{k>K} 1/k^2 lies between 1/(K+1) and 1/K.
    lower = partial + np.longdouble(multiplicity ** 2) / np.longdouble(kmax + 1)
    upper = partial + np.longdouble(multiplicity ** 2) / np.longdouble(kmax)
    assert lower < target < upper
    print(f"monodromy negative-mode energy K={kmax}: {float(partial):.12g}")
    print(f"Hardy floor m^2*pi^2/6: {float(target):.12g}")


def main() -> None:
    exact_finite_identity()
    arithmetic_boundary_check()
    signed_zero_cross_check()
    monodromy_hardy_floor_check()
    print("all 104_98 checks passed")


if __name__ == "__main__":
    main()
