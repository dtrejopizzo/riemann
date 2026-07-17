#!/usr/bin/env python3
import math
import sys

import mpmath as mp
import numpy as np

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E71_9_relative_arch_background_probe import primes_upto  # noqa: E402
from E73_206_hp_matrix_entry_probe import entry_modes  # noqa: E402
from E73_201_mp_finite_assembly_probe import mp_exp_int, mp_y_exp_int  # noqa: E402


mp.mp.dps = 100


TARGETS = {8: -56.26, 10: -51.93, 12: -48.94}


def entry_work_size(m, n, L, lam, R=80):
    const, linear = entry_modes(m, n, L)
    total_abs = mp.mpf("0")
    ops = 0
    # w02 terms
    for alpha in [mp.mpf("0.5"), mp.mpf("-0.5")]:
        for om, c in const.items():
            total_abs += abs(c) * abs(mp_exp_int(alpha + 1j * mp.mpf(float(om)), L))
            ops += 1
        for om, c in linear.items():
            total_abs += abs(c) * abs(mp_y_exp_int(alpha + 1j * mp.mpf(float(om)), L))
            ops += 1
    # finite WR head
    b0 = sum(const.values())
    for r in range(R):
        alpha = -(2 * r + mp.mpf("0.5"))
        for om, c in const.items():
            total_abs += abs(c) * abs(mp_exp_int(alpha + 1j * mp.mpf(float(om)), L))
            ops += 1
        for om, c in linear.items():
            total_abs += abs(c) * abs(mp_y_exp_int(alpha + 1j * mp.mpf(float(om)), L))
            ops += 1
        total_abs += abs(b0) * abs(mp_exp_int(-(2 * r + mp.mpf("1.0")), L))
        ops += 1
    # prime side
    maxn = int(lam * lam)
    for p in primes_upto(maxn):
        lp = math.log(p)
        q = p
        k = 1
        while q <= maxn:
            y = k * lp
            weight = mp.mpf(lp) * mp.power(q, mp.mpf("-0.5"))
            sample_abs = mp.mpf("0")
            for om, c in const.items():
                sample_abs += abs(c) * abs(mp.e ** (1j * mp.mpf(float(om)) * y))
                ops += 1
            for om, c in linear.items():
                sample_abs += abs(c) * y * abs(mp.e ** (1j * mp.mpf(float(om)) * y))
                ops += 1
            total_abs += weight * sample_abs
            if q > maxn // p:
                break
            q *= p
            k += 1
    return total_abs, ops


def max_rounding_radius(lam, n_modes, digits):
    L = 2.0 * math.log(lam)
    idx = list(range(-n_modes, n_modes + 1))
    unit = mp.power(10, -digits)
    max_rad = mp.mpf("0")
    max_ops = 0
    for a, m in enumerate(idx):
        for n in idx[a:]:
            total_abs, ops = entry_work_size(m, n, L, lam)
            # Inflate by 10 to cover elementary function and summation constants
            # in this audit.  Final interval arithmetic replaces this heuristic.
            rad = 10 * ops * total_abs * unit
            max_rad = max(max_rad, rad)
            max_ops = max(max_ops, ops)
    return L, len(idx), max_rad, max_ops


def bexp(z, L):
    return np.log(max(float(abs(z)), 1e-300)) / np.log(L)


def run():
    print("E73.211 elementary rounding budget")
    print("Heuristic outward-rounding digit budget for finite elementary sums.")
    print(" lam     L    N  dim digits maxRadB targetB slack maxOps")
    for lam, n_modes in [(8, 6), (10, 8), (12, 10)]:
        for digits in [80, 100, 120, 140]:
            L, dim, rad, max_ops = max_rounding_radius(lam, n_modes, digits)
            target = mp.power(mp.mpf(L), TARGETS[lam])
            print(
                f"{lam:4d} {L:7.3f} {n_modes:4d} {dim:4d}"
                f" {digits:6d} {bexp(rad, L):8.2f}"
                f" {TARGETS[lam]:8.2f} {float(target / rad):9.2e}"
                f" {max_ops:6d}"
            )


if __name__ == "__main__":
    run()
