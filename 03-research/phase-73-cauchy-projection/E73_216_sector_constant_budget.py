#!/usr/bin/env python3
import math
import sys

import mpmath as mp
import numpy as np

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E73_210_psi_asymptotic_budget import digamma_tail_radius_for_entry  # noqa: E402
from E73_211_rounding_budget_probe import TARGETS  # noqa: E402
from E73_215_native_ball_entry_probe import elementary_entry_ball  # noqa: E402


mp.mp.dps = 100


def entry_base_data(lam, n_modes):
    L = 2.0 * math.log(lam)
    idx = list(range(-n_modes, n_modes + 1))
    target = mp.power(mp.mpf(L), TARGETS[lam])
    data = []
    for a, m in enumerate(idx):
        for n in idx[a:]:
            elem = elementary_entry_ball(m, n, L, lam).r
            exp_tail = mp.e ** (-(2 * 80 + mp.mpf("0.5")) * L)
            data.append((m, n, elem, exp_tail, target))
    return L, len(idx), data


def max_allowed_csec(L, data, K):
    max_c = mp.inf
    worst = None
    for m, n, elem, exp_tail, target in data:
            psi_unit = digamma_tail_radius_for_entry(m, n, L, 80, K)
            allowed = (target - elem - exp_tail) / psi_unit
            if allowed < max_c:
                max_c = allowed
                worst = (m, n)
    return max_c, worst


def run():
    print("E73.216 sector constant budget")
    print("Maximum Bernoulli sector constant C_sec allowed by BALL-ENTRY-CERT.")
    print(" lam     L    N  dim    K      Cmax       log10C worst")
    for lam, n_modes in [(8, 6), (10, 8), (12, 10)]:
        L, dim, data = entry_base_data(lam, n_modes)
        for K in [12, 16, 20, 24]:
            cmax, worst = max_allowed_csec(L, data, K)
            print(
                f"{lam:4d} {L:7.3f} {n_modes:4d} {dim:4d}"
                f" {K:4d} {mp.nstr(cmax, 8):>12s}"
                f" {float(mp.log10(cmax)):10.2f} {worst}"
            )


if __name__ == "__main__":
    run()
