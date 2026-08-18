#!/usr/bin/env python3
"""Exact checks for the adjacent Riccati/triangle gate of 104_39.

All arithmetic is rational.  The script checks three facts:

1. the determinant factors as the two triangle inequalities when
   H=x^2, d=y^2 and H_next=z^2;
2. a critical-line quartet can keep every H_n strictly positive while
   making the adjacent determinant negative;
3. the rational off-line quartet w=5i/4 eventually forces a first
   positive-to-negative crossing and hence breaks the same gate.
4. optimizing a general reference diagonal is tautological, and the
   prefix-orthogonal determinant is the same quadratic in another basis.
"""

from __future__ import annotations

from fractions import Fraction as F


Gaussian = tuple[F, F]


def gmul(z: Gaussian, w: Gaussian) -> Gaussian:
    return z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0]


def ginv(z: Gaussian) -> Gaussian:
    norm = z[0] * z[0] + z[1] * z[1]
    return z[0] / norm, -z[1] / norm


def gpow(z: Gaussian, n: int) -> Gaussian:
    out: Gaussian = (F(1), F(0))
    base = z
    exponent = n
    while exponent:
        if exponent & 1:
            out = gmul(out, base)
        base = gmul(base, base)
        exponent >>= 1
    return out


def determinant(h: F, d: F, h_next: F) -> F:
    return 4 * h * d - (h + d - h_next) ** 2


def critical_quartet(n: int) -> F:
    # 4 - 4 cos(n*pi/2), hence the exact cycle 0,4,8,4.
    cosine_cycle = (F(1), F(0), F(-1), F(0))
    return 4 - 4 * cosine_cycle[n % 4]


def offline_quartet(n: int) -> F:
    # Functional reciprocal quartet attached to w=5i/4:
    # 4 - (w^n + conjugate(w)^n + w^-n + conjugate(w)^-n).
    w: Gaussian = (F(0), F(5, 4))
    wn = gpow(w, n)
    win = gpow(ginv(w), n)
    return 4 - 2 * (wn[0] + win[0])


def main() -> None:
    # Exact triangle factorization.
    x, y, z = F(7, 3), F(5, 4), F(11, 6)
    left = determinant(x * x, y * y, z * z)
    right = ((x + y) ** 2 - z * z) * (z * z - (x - y) ** 2)
    assert left == right

    # Strict positivity of every H_n does not imply the adjacent gate.
    # Take H_n=1+L_n with a critical-line quartet and d_n=1.
    for n in range(1, 100):
        assert 1 + critical_quartet(n) >= 1
    n = 4
    h = 1 + critical_quartet(n)
    h_next = 1 + critical_quartet(n + 1)
    t = determinant(h, F(1), h_next)
    assert (h, h_next, t) == (F(1), F(5), F(-5))

    # General-reference optimization:
    # F(D)=4 H D-(H+D-H_next)^2 is maximal at D=H+H_next.
    h0, h1 = F(3), F(5)
    d_opt = h0 + h1
    assert determinant(h0, d_opt, h1) == 4 * h0 * h1

    # Prefix-orthogonal gauge.  Its determinant in {g_n,g_(n+1)}
    # agrees with F(D) in {g_n,phi_n}.
    kappa, gamma = F(3, 4), F(1, 2)
    a0, a1, b0, b1 = F(10), F(12), F(2), F(3)
    hp0, hp1 = kappa * a0 - b0, kappa * a1 - b1
    d_prefix = kappa * (a0 + a1) + gamma
    f_phi = determinant(hp0, d_prefix, hp1)
    f_prefix = 4 * hp0 * hp1 - (b0 + b1 + gamma) ** 2
    assert f_phi == f_prefix

    # The same positive critical quartet breaks the prefix-orthogonal
    # criterion for an integer multiplicity while preserving H>0.
    multiplicity = F(2)
    u_critical = 4 * F(1) * (1 + 4 * multiplicity) - (
        -4 * multiplicity
    ) ** 2
    assert u_critical == -28

    # The exact off-line point is rho=(1-w)^-1=16/41+20i/41.
    rho = ginv((F(1), F(-5, 4)))
    assert rho == (F(16, 41), F(20, 41))
    assert F(0) < rho[0] < F(1, 2)

    # Add the quartet to a polynomial baseline.  Locate the first exact
    # crossing; RT at the preceding index must be negative for every d>0
    # once H_next<0 (we display it for d=1).
    def h_off(k: int) -> F:
        return F(k * k) + offline_quartet(k)

    crossing = None
    for k in range(2, 200):
        if h_off(k) < 0:
            crossing = k
            break
    assert crossing is not None
    assert h_off(crossing - 1) >= 0 > h_off(crossing)
    t_cross = determinant(h_off(crossing - 1), F(1), h_off(crossing))
    assert t_cross < 0

    print("PASS exact triangle factorization")
    print(f"critical-line positive-margin witness: n=4, T={t}")
    print(
        "reference optimization witness: "
        f"F(H+H_next)={4*h0*h1}, prefix-critical U={u_critical}"
    )
    print(
        "off-line rational witness: "
        f"rho={rho[0]}+({rho[1]})i, first crossing n={crossing}, "
        f"T_(n-1)={t_cross}"
    )


if __name__ == "__main__":
    main()
