#!/usr/bin/env python3
import math
import sys

import mpmath as mp
import numpy as np

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E71_9_relative_arch_background_probe import GAMMA, LOG4PI, primes_upto  # noqa: E402
from E73_206_hp_matrix_entry_probe import entry_modes  # noqa: E402
from E73_210_psi_asymptotic_budget import digamma_tail_radius_for_entry  # noqa: E402
from E73_211_rounding_budget_probe import TARGETS  # noqa: E402


mp.mp.dps = 100


class CBall:
    def __init__(self, center=0, radius=0):
        self.c = mp.mpc(center)
        self.r = mp.mpf(radius)

    def __add__(self, other):
        other = as_ball(other)
        return CBall(self.c + other.c, self.r + other.r)

    __radd__ = __add__

    def __neg__(self):
        return CBall(-self.c, self.r)

    def __sub__(self, other):
        return self + (-as_ball(other))

    def __rsub__(self, other):
        return as_ball(other) + (-self)

    def __mul__(self, other):
        other = as_ball(other)
        rad = abs(self.c) * other.r + abs(other.c) * self.r + self.r * other.r
        return CBall(self.c * other.c, rad)

    __rmul__ = __mul__

    def div_point(self, z):
        z = mp.mpc(z)
        return CBall(self.c / z, self.r / abs(z))


def as_ball(x):
    if isinstance(x, CBall):
        return x
    return CBall(x, 0)


def point(x, unit):
    z = mp.mpc(x)
    return CBall(z, unit * max(mp.mpf(1), abs(z)))


def ball_exp(z, unit):
    z = as_ball(z)
    center = mp.e ** z.c
    rad = mp.e ** (mp.re(z.c) + z.r) * (mp.e ** z.r - 1)
    rad += unit * max(mp.mpf(1), abs(center))
    return CBall(center, rad)


def ball_exp_int(alpha, L, unit):
    alpha = as_ball(alpha)
    Lb = point(L, unit)
    if abs(alpha.c) < mp.mpf("1e-70") and alpha.r == 0:
        return Lb
    e = ball_exp(alpha * Lb, unit)
    num = e - 1
    # In this finite matrix use alpha centers away from zero except the
    # handled case; alpha uncertainty is tiny and included in alpha.r.
    return num.div_point(alpha.c)


def ball_y_exp_int(alpha, L, unit):
    alpha = as_ball(alpha)
    Lb = point(L, unit)
    if abs(alpha.c) < mp.mpf("1e-70") and alpha.r == 0:
        return CBall(mp.mpf("0.5") * L * L, unit * max(1, L * L))
    aL = alpha * Lb
    e = ball_exp(aL, unit)
    num = e * (aL - 1) + 1
    return num.div_point(alpha.c * alpha.c)


def ball_eval_modes(const, linear, y, unit):
    yb = point(y, unit)
    total = CBall(0, 0)
    for om, coeff in const.items():
        phase = ball_exp(point(1j * float(om), unit) * yb, unit)
        total += point(coeff, unit) * phase
    for om, coeff in linear.items():
        phase = ball_exp(point(1j * float(om), unit) * yb, unit)
        total += point(coeff, unit) * yb * phase
    return total


def elementary_entry_ball(m, n, L, lam, digits=100, R=80):
    unit = mp.power(10, -digits)
    const, linear = entry_modes(m, n, L)
    b0 = ball_eval_modes(const, linear, 0, unit)
    total = CBall(0, 0)
    for alpha in [mp.mpf("0.5"), mp.mpf("-0.5")]:
        for om, coeff in const.items():
            total += point(coeff, unit) * ball_exp_int(point(alpha + 1j * float(om), unit), L, unit)
        for om, coeff in linear.items():
            total += point(coeff, unit) * ball_y_exp_int(point(alpha + 1j * float(om), unit), L, unit)
    wra = CBall(0, 0)
    for r in range(R):
        alpha0 = -(2 * r + mp.mpf("0.5"))
        for om, coeff in const.items():
            wra += point(coeff, unit) * ball_exp_int(point(alpha0 + 1j * float(om), unit), L, unit)
        for om, coeff in linear.items():
            wra += point(coeff, unit) * ball_y_exp_int(point(alpha0 + 1j * float(om), unit), L, unit)
        wra -= b0 * ball_exp_int(point(-(2 * r + mp.mpf("1.0")), unit), L, unit)
    wrb = b0 * point(mp.mpf("0.5") * mp.log(mp.tanh(mp.mpf(L) / 2)), unit)
    wr_const = b0 * point(mp.mpf("0.5") * (LOG4PI + GAMMA), unit)
    arch_elem = total - wra - wrb - wr_const

    prime = CBall(0, 0)
    maxn = int(lam * lam)
    for p in primes_upto(maxn):
        lp = math.log(p)
        q = p
        k = 1
        while q <= maxn:
            weight = point(mp.mpf(lp) * mp.power(q, mp.mpf("-0.5")), unit)
            prime += weight * ball_eval_modes(const, linear, k * lp, unit)
            if q > maxn // p:
                break
            q *= p
            k += 1
    return arch_elem - prime


def entry_radius(m, n, L, lam, digits=100, R=80, K=16):
    elem_ball = elementary_entry_ball(m, n, L, lam, digits=digits, R=R)
    r_psi = digamma_tail_radius_for_entry(m, n, L, R, K)
    r_exp = mp.e ** (-(2 * R + mp.mpf("0.5")) * L)
    return elem_ball.r + r_psi + r_exp, elem_ball.r, r_psi, r_exp


def bexp(z, L):
    return np.log(max(float(abs(z)), 1e-300)) / np.log(L)


def run():
    print("E73.215 native ball entry certificate")
    print("Propagates complex-ball radii for finite elementary entry pieces; K=16 for psi tail.")
    print(" lam     L    N  dim targetB maxTotB maxBallB maxPsiB maxExpB slack")
    for lam, n_modes in [(8, 6), (10, 8), (12, 10)]:
        L = 2.0 * math.log(lam)
        idx = list(range(-n_modes, n_modes + 1))
        target = mp.power(mp.mpf(L), TARGETS[lam])
        max_total = max_ball = max_psi = max_exp = mp.mpf("0")
        worst = None
        for a, m in enumerate(idx):
            for n in idx[a:]:
                total, ball, psi, exp = entry_radius(m, n, L, lam)
                if total > max_total:
                    worst = (m, n)
                max_total = max(max_total, total)
                max_ball = max(max_ball, ball)
                max_psi = max(max_psi, psi)
                max_exp = max(max_exp, exp)
        print(
            f"{lam:4d} {L:7.3f} {n_modes:4d} {len(idx):4d}"
            f" {TARGETS[lam]:8.2f} {bexp(max_total, L):8.2f}"
            f" {bexp(max_ball, L):8.2f} {bexp(max_psi, L):8.2f}"
            f" {bexp(max_exp, L):8.2f} {float(target/max_total):9.2e}"
            f" worst={worst}"
        )


if __name__ == "__main__":
    run()
