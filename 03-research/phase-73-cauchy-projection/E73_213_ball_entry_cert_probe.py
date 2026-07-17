#!/usr/bin/env python3
import math
import sys

import mpmath as mp
import numpy as np

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E73_210_psi_asymptotic_budget import digamma_tail_radius_for_entry  # noqa: E402
from E73_211_rounding_budget_probe import TARGETS, entry_work_size  # noqa: E402


mp.mp.dps = 100


def entry_radius(m, n, L, lam, digits=80, R=80, K=12):
    r_digamma = digamma_tail_radius_for_entry(m, n, L, R, K)
    work, ops = entry_work_size(m, n, L, lam, R=R)
    r_round = 10 * ops * work * mp.power(10, -digits)
    # Exponential tail after the explicitly summed correction in E73.198 is
    # astronomically below target for R=80.  Use a conservative geometric cap.
    r_exp = mp.e ** (-(2 * R + mp.mpf("0.5")) * L)
    return r_digamma + r_round + r_exp, r_digamma, r_round, r_exp


def bexp(z, L):
    return np.log(max(float(abs(z)), 1e-300)) / np.log(L)


def run():
    print("E73.213 BALL-ENTRY-CERT v0")
    print("Checks component entry radii against E73.209 per-entry targets.")
    print(" lam     L    N  dim targetB maxTotB maxPsiB maxRndB maxExpB slack")
    for lam, n_modes in [(8, 6), (10, 8), (12, 10)]:
        L = 2.0 * math.log(lam)
        idx = list(range(-n_modes, n_modes + 1))
        target = mp.power(mp.mpf(L), TARGETS[lam])
        max_total = mp.mpf("0")
        max_psi = mp.mpf("0")
        max_round = mp.mpf("0")
        max_exp = mp.mpf("0")
        worst = None
        for a, m in enumerate(idx):
            for n in idx[a:]:
                total, psi, rnd, exp = entry_radius(m, n, L, lam)
                if total > max_total:
                    worst = (m, n)
                max_total = max(max_total, total)
                max_psi = max(max_psi, psi)
                max_round = max(max_round, rnd)
                max_exp = max(max_exp, exp)
        print(
            f"{lam:4d} {L:7.3f} {n_modes:4d} {len(idx):4d}"
            f" {TARGETS[lam]:8.2f} {bexp(max_total, L):8.2f}"
            f" {bexp(max_psi, L):8.2f} {bexp(max_round, L):8.2f}"
            f" {bexp(max_exp, L):8.2f} {float(target/max_total):9.2e}"
            f" worst={worst}"
        )


if __name__ == "__main__":
    run()
