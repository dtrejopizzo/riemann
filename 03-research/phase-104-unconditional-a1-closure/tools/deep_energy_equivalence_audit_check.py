#!/usr/bin/env python3
"""Exact finite checks for 104_105 (stdlib only)."""

from fractions import Fraction as Q


def cadd(z, w):
    return (z[0] + w[0], z[1] + w[1])


def csub(z, w):
    return (z[0] - w[0], z[1] - w[1])


def cmul(z, w):
    return (z[0] * w[0] - z[1] * w[1],
            z[0] * w[1] + z[1] * w[0])


def cconj(z):
    return (z[0], -z[1])


def cinv(z):
    den = z[0] * z[0] + z[1] * z[1]
    return (z[0] / den, -z[1] / den)


def cdiv(z, w):
    return cmul(z, cinv(w))


def cnorm2(z):
    return z[0] * z[0] + z[1] * z[1]


def check_mode_orientation():
    # A rational point strictly to the right of 1/2.
    rho = (Q(3, 4), Q(7, 5))
    one = (Q(1), Q(0))
    u = cdiv(rho, csub(rho, one))
    lhs = cnorm2(u) - 1
    rhs = (2 * rho[0] - 1) / cnorm2(csub(rho, one))
    assert lhs == rhs and lhs > 0

    # z_{1-conj(rho)} = conj(u_rho).
    partner = csub(one, cconj(rho))
    z_partner = cdiv(csub(partner, one), partner)
    assert z_partner == cconj(u)


def check_energy_kernel():
    # Signed arbitrary data; b_1 is deliberately absent.
    b = {2: Q(3, 7), 3: Q(-5, 11), 4: Q(2, 9),
         5: Q(-7, 13), 6: Q(1, 8)}
    N = 6
    B = {}
    running = Q(0)
    for m in range(2, N + 1):
        running += b[m]
        B[m] = running

    direct = sum(B[m] * B[m] / (m * (m + 1))
                 for m in range(2, N + 1))
    kernel = sum(
        b[r] * b[s] * (Q(1, max(r, s)) - Q(1, N + 1))
        for r in range(2, N + 1)
        for s in range(2, N + 1)
    )
    assert direct == kernel


def check_finite_abel():
    # For a finitely supported sequence and s=2, retain the constant
    # partial-sum tail [M+1,infinity). All integrals are exact.
    b = {2: Q(2, 5), 3: Q(-1, 7), 4: Q(3, 11), 5: Q(-2, 9)}
    M = 5
    s = 2
    lhs = sum(b[n] / (n ** s) for n in range(2, M + 1))

    running = Q(0)
    integral = Q(0)
    for m in range(2, M + 1):
        running += b[m]
        # s * int_m^{m+1} x^{-s-1} dx = m^{-s}-(m+1)^{-s}
        integral += running * (Q(1, m ** s) - Q(1, (m + 1) ** s))
    # s * int_{M+1}^infinity x^{-s-1} dx = (M+1)^{-s}
    integral += running * Q(1, (M + 1) ** s)
    assert lhs == integral


def check_periodic_deep_mass():
    # The rational quartet's bad class is 0 mod 4. Between X^(1/2)
    # and X its normalized harmonic main coefficient is (1/4)(1-1/2).
    alpha = Q(1, 2)
    residue_density = Q(1, 4)
    assert residue_density * (1 - alpha) == Q(1, 8)


if __name__ == "__main__":
    check_mode_orientation()
    check_energy_kernel()
    check_finite_abel()
    check_periodic_deep_mass()
    print("PASS deep/energy audit: orientation, max-kernel, Abel edge, deep 1/8")
