#!/usr/bin/env python3
import sys

import numpy as np

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
from E71_9_relative_arch_background_probe import primes_upto  # noqa: E402

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_219_raw_profiled_prime_sum_probe import raw_prime_sum  # noqa: E402


WINDOWS = [(12, 32), (16, 40), (20, 48), (24, 56), (28, 64)]


def beta_sum_weight(lam, L, block, cut=0.60, power=1.0):
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
                total += (lp * lp / pm) * (max(0.0, 1.0 - u) ** power)
            if pm > maxn // p:
                break
            pm *= p
            me += 1
    return total


def run():
    print("E72.222 even-leading Rraw bound probe")
    print("lead=0.5*dim_even*sum beta2*(1-u)")
    print("lam block qdim Rraw lead ratio leadL4 sum1-u")
    for lam, n_modes in WINDOWS:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        dim_even = bq.shape[1] + 1
        for block in [0, 1]:
            rraw = raw_prime_sum(lam, idx, L, bq, block)
            s1 = beta_sum_weight(lam, L, block, power=1.0)
            lead = 0.5 * dim_even * s1
            print(
                f"{lam:3.0f} {block:5d} {dim_even:4d} "
                f"{rraw:.6e} {lead:.6e} {lead/rraw:.3f} "
                f"{lead/(L**4):.6e} {s1:.6e}",
                flush=True,
            )


if __name__ == "__main__":
    run()
