#!/usr/bin/env python3
import sys

import numpy as np
from scipy.special import polygamma

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")

from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_182_closed_series_arch_probe import (  # noqa: E402
    arch_closed_series,
    cauchy_rows,
    eval_modes,
    integrate_modes,
    odd_cube_tail,
    odd_square_tail,
    packet_modes,
    second_derivative0_modes,
    setup,
)


def derivative0_modes(const, linear):
    total = 0j
    for om, c in const.items():
        total += 1j * om * c
    for _om, c in linear.items():
        total += c
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


def f3_bound(const, linear, L):
    b0 = mode_derivative_bound(const, linear, 0, L)
    b1 = mode_derivative_bound(const, linear, 1, L)
    b2 = mode_derivative_bound(const, linear, 2, L)
    b3 = mode_derivative_bound(const, linear, 3, L)
    return np.exp(L / 2.0) * (b3 + 1.5 * b2 + 0.75 * b1 + 0.125 * b0)


def odd_fourth_tail(r_terms):
    # sum_{r=R}^infty 1/(2r+1)^4 = psi_3(R+1/2)/96.
    return float(polygamma(3, r_terms + 0.5)) / 96.0


def wr_series_accelerated(const, linear, L, r_terms, accel=True):
    b0 = eval_modes(const, linear, 0.0)
    bp0 = derivative0_modes(const, linear)
    bpp0 = second_derivative0_modes(const, linear)
    c1 = bp0 + 0.5 * b0
    c2 = 0.5 * bpp0 + 0.5 * bp0 + 0.125 * b0
    wra = 0j
    for r in range(r_terms):
        wra += integrate_modes(const, linear, -(2 * r + 0.5), L)
        wra -= b0 * ((np.exp(-(2 * r + 1.0) * L) - 1.0) / (-(2 * r + 1.0)))
    if accel:
        wra += c1 * odd_square_tail(r_terms)
        wra += 2.0 * c2 * odd_cube_tail(r_terms)
    return wra


def bexp(z, L):
    return np.log(max(float(abs(z)), 1e-300)) / np.log(L)


def run():
    print("E73.183 WR Taylor-tail bound probe")
    print("Bounds the accelerated WR-series tail by M3*sum(2r+1)^-4.")
    print(" lam     L gamma row    R actualTailB boundB ratioB M3B")
    for lam, n_modes in [(12, 16), (16, 20), (20, 24), (24, 28)]:
        _h_model, idx, d, L, xi = setup(lam, n_modes)
        for gamma in GAMMAS[:2]:
            plane = cauchy_rows(-1j * gamma, d)
            for j in range(2):
                const, linear = packet_modes(plane[j], idx, d, xi, L)
                for r_terms in [80, 120, 200]:
                    tail_ref = wr_series_accelerated(const, linear, L, 5000, accel=True)
                    tail_r = wr_series_accelerated(const, linear, L, r_terms, accel=True)
                    actual_tail = abs(tail_ref - tail_r)
                    m3 = f3_bound(const, linear, L)
                    bound = m3 * odd_fourth_tail(r_terms)
                    ratio = actual_tail / max(bound, 1e-300)
                    print(
                        f"{lam:4d} {L:7.3f} {gamma:7.2f} {j:3d}"
                        f" {r_terms:4d} {bexp(actual_tail, L):11.2f}"
                        f" {bexp(bound, L):6.2f} {bexp(ratio, L):6.2f}"
                        f" {bexp(m3, L):6.2f}"
                    )


if __name__ == "__main__":
    # Keep one call to the imported evaluator alive for pyflakes-style sanity.
    _ = arch_closed_series
    run()
