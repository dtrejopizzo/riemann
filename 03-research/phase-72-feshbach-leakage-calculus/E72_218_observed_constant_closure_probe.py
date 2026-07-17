#!/usr/bin/env python3
import sys

import numpy as np
from numpy.linalg import eigvalsh

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
from E71_9_relative_arch_background_probe import primes_upto  # noqa: E402

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_210_cell_energy_factor_probe import cells  # noqa: E402


WINDOWS = [(12, 32), (16, 40), (20, 48), (24, 56), (28, 64)]


def sphi(lam, L, block, cut=0.60):
    total = 0.0
    maxn = int(lam * lam)
    for p in primes_upto(maxn):
        lp = np.log(p)
        pm = p
        me = 1
        while pm <= maxn:
            y = me * lp
            u = y / L
            bid = 0 if u <= cut else 1
            if bid == block:
                total += (lp * lp / pm) * np.sqrt(max(0.0, 1.0 - u))
            if pm > maxn // p:
                break
            pm *= p
            me += 1
    return total


def run():
    print("E72.218 observed-constant resonant closure probe")
    print("bound = (1.5/c_obs^2) L^-2 Sphi, c_obs=lambda_min(C)/L^2")
    print("lam block actual bound ratio c_obs Sphi")
    for lam, n_modes in WINDOWS:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        c_obs = float(eigvalsh(c_model)[0] / (L * L))
        rs = cells(lam, idx, L, bq, c_model)
        for block in [0, 1]:
            actual = sum(r[6] for r in rs if r[3] == block)
            sp = sphi(lam, L, block)
            bound = 1.5 * sp / (L * L * c_obs * c_obs)
            print(
                f"{lam:3.0f} {block:5d} {actual:.6e} {bound:.6e} "
                f"{bound/actual:.2f} {c_obs:.3f} {sp:.6e}",
                flush=True,
            )


if __name__ == "__main__":
    run()
