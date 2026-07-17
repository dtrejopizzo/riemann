#!/usr/bin/env python3
import math
import sys

import numpy as np
from scipy.special import polygamma

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_182_closed_series_arch_probe import (  # noqa: E402
    cauchy_rows,
    eval_modes,
    integrate_modes,
    packet_modes,
    setup,
)


def mode_derivative_at_zero(const, linear, order):
    total = 0j
    for om, c in const.items():
        total += c * (1j * om) ** order
    for om, c in linear.items():
        if order == 0:
            continue
        total += c * order * (1j * om) ** (order - 1)
    return total


def mode_derivative_bound(const, linear, order, L):
    total = 0.0
    for om, c in const.items():
        total += abs(c) * (abs(om) ** order)
    for om, c in linear.items():
        if order == 0:
            total += abs(c) * L
        else:
            total += abs(c) * (order * (abs(om) ** (order - 1)) + L * (abs(om) ** order))
    return total


def f_derivative_at_zero(const, linear, order):
    # F(y)=exp(y/2)B(y)-B(0), and the constant subtraction only affects order 0.
    total = 0j
    for j in range(order + 1):
        total += math.comb(order, j) * (0.5 ** (order - j)) * mode_derivative_at_zero(const, linear, j)
    if order == 0:
        total -= eval_modes(const, linear, 0.0)
    return total


def f_derivative_bound(const, linear, order, L):
    total = 0.0
    for j in range(order + 1):
        total += math.comb(order, j) * (0.5 ** (order - j)) * mode_derivative_bound(const, linear, j, L)
    return math.exp(L / 2.0) * total


def odd_power_tail(r_terms, power):
    # sum_{r=R}^\infty (2r+1)^(-power)
    # = (-1)^power / (2^power (power-1)!) psi_{power-1}(R+1/2)
    return ((-1) ** power) * float(polygamma(power - 1, r_terms + 0.5)) / (
        (2**power) * math.factorial(power - 1)
    )


def accelerated_wra(const, linear, L, r_terms, order):
    b0 = eval_modes(const, linear, 0.0)
    wra = 0j
    for r in range(r_terms):
        a = 2 * r + 1.0
        wra += integrate_modes(const, linear, -(a - 0.5), L)
        wra -= b0 * ((np.exp(-a * L) - 1.0) / (-a))
    for m in range(1, order + 1):
        cm = f_derivative_at_zero(const, linear, m) / math.factorial(m)
        wra += cm * math.factorial(m) * odd_power_tail(r_terms, m + 1)
    return wra


def tail_bound(const, linear, L, r_terms, order):
    m = order + 1
    bound = f_derivative_bound(const, linear, m, L)
    return bound * odd_power_tail(r_terms, m + 1)


def bexp(z, L):
    return np.log(max(float(abs(z)), 1e-300)) / np.log(L)


def run():
    print("E73.184 high-order WR tail probe")
    print("Taylor accelerates WR tail to order K and bounds by F^(K+1).")
    print(" lam     L gamma row R  K actualTailB boundB ratioB nextDerB")
    for lam, n_modes in [(12, 16), (16, 20), (20, 24), (24, 28)]:
        _h_model, idx, d, L, xi = setup(lam, n_modes)
        for gamma in GAMMAS[:2]:
            plane = cauchy_rows(-1j * gamma, d)
            for j in range(2):
                const, linear = packet_modes(plane[j], idx, d, xi, L)
                for order in [2, 4, 6, 8]:
                    r_terms = 80
                    ref = accelerated_wra(const, linear, L, 8000, order)
                    val = accelerated_wra(const, linear, L, r_terms, order)
                    actual = abs(ref - val)
                    bnd = tail_bound(const, linear, L, r_terms, order)
                    ratio = actual / max(bnd, 1e-300)
                    deriv = f_derivative_bound(const, linear, order + 1, L)
                    print(
                        f"{lam:4d} {L:7.3f} {gamma:7.2f} {j:3d}"
                        f" {r_terms:2d} {order:2d}"
                        f" {bexp(actual, L):11.2f} {bexp(bnd, L):6.2f}"
                        f" {bexp(ratio, L):6.2f} {bexp(deriv, L):8.2f}"
                    )


if __name__ == "__main__":
    run()
