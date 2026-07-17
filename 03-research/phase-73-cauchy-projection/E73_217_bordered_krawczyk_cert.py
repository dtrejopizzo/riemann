#!/usr/bin/env python3
import math
import sys

import mpmath as mp
import numpy as np

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E73_208_krawczyk_budget_probe import admissible, build_center  # noqa: E402
from E73_210_psi_asymptotic_budget import digamma_tail_radius_for_entry  # noqa: E402
from E73_215_native_ball_entry_probe import elementary_entry_ball  # noqa: E402


mp.mp.dps = 100


def entry_data(lam, n_modes, K=16):
    L = 2.0 * math.log(lam)
    idx = list(range(-n_modes, n_modes + 1))
    data = []
    for a, m in enumerate(idx):
        for n in idx[a:]:
            ball = elementary_entry_ball(m, n, L, lam).r
            psi_unit = digamma_tail_radius_for_entry(m, n, L, 80, K)
            exp_tail = mp.e ** (-(2 * 80 + mp.mpf("0.5")) * L)
            data.append((m, n, ball, psi_unit, exp_tail))
    return L, len(idx), data


def max_entry_radius(data, csec=1):
    max_total = mp.mpf("0")
    max_ball = mp.mpf("0")
    max_psi = mp.mpf("0")
    worst = None
    for m, n, ball, psi_unit, exp_tail in data:
            psi = csec * psi_unit
            total = ball + psi + exp_tail
            if total > max_total:
                worst = (m, n)
            max_total = max(max_total, total)
            max_ball = max(max_ball, ball)
            max_psi = max(max_psi, psi)
    return max_total, max_ball, max_psi, worst


def bexp(z, L):
    return np.log(max(float(abs(z)), 1e-300)) / np.log(L)


def run():
    print("E73.217 bordered Krawczyk certificate from BALL-ENTRY-CERT")
    print("Uses epsH = dim * max_entry_radius and verifies the Krawczyk inequality.")
    print(" lam     L    N  dim Csec expH_B stepB Y_B rhoB ratio maxEntryB worst")
    for lam, n_modes in [(8, 6), (10, 8), (12, 10)]:
        L, dim, data = entry_data(lam, n_modes)
        L2, n, step, ynorm = build_center(lam, n_modes)
        for csec in [mp.mpf(1), mp.mpf("1e6")]:
            max_ent, max_ball, max_psi, worst = max_entry_radius(data, csec=csec)
            epsH = dim * max_ent
            rho, ratio = admissible(ynorm, step, epsH, safety=mp.mpf("0.75"))
            print(
                f"{lam:4d} {L:7.3f} {n_modes:4d} {dim:4d}"
                f" {mp.nstr(csec, 3):>4s} {bexp(epsH, L):8.2f}"
                f" {bexp(step, L):7.2f} {bexp(ynorm, L):6.2f}"
                f" {bexp(rho, L) if rho else float('nan'):6.2f}"
                f" {float(ratio) if ratio else float('nan'):6.3f}"
                f" {bexp(max_ent, L):9.2f} {worst}"
            )


if __name__ == "__main__":
    run()
