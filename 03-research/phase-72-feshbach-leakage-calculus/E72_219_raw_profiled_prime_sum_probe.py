#!/usr/bin/env python3
import sys

import numpy as np
from numpy.linalg import cholesky, eigvalsh, norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
from E71_9_relative_arch_background_probe import primes_upto  # noqa: E402

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_197_signed_green_word_probe import u_matrix  # noqa: E402
from E72_210_cell_energy_factor_probe import cells  # noqa: E402


WINDOWS = [(12, 32), (16, 40), (20, 48), (24, 56), (28, 64)]


def raw_prime_sum(lam, idx, L, bq, block, cut=0.60):
    total = 0.0
    maxn = int(lam * lam)
    for p in primes_upto(maxn):
        lp = np.log(p)
        pm = p
        me = 1
        while pm <= maxn:
            y = me * lp
            bid = 0 if y <= cut * L else 1
            if bid == block:
                beta2 = lp * lp / pm
                raw = bq.T @ u_matrix(idx, L, y) @ bq
                total += beta2 * float(norm(raw, "fro") ** 2)
            if pm > maxn // p:
                break
            pm *= p
            me += 1
    return total


def run():
    print("E72.219 raw-profiled prime sum probe")
    print("Rraw=sum beta2 ||B*U_logn B||_HS^2; bound=2Rraw/minC^2")
    print("lam block actual Rraw Rraw/L4 bound ratio c_obs")
    for lam, n_modes in WINDOWS:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        minc = float(eigvalsh(c_model)[0])
        cobs = minc / (L * L)
        rs = cells(lam, idx, L, bq, c_model)
        for block in [0, 1]:
            actual = sum(r[6] for r in rs if r[3] == block)
            rraw = raw_prime_sum(lam, idx, L, bq, block)
            bound = 2.0 * rraw / (minc * minc)
            print(
                f"{lam:3.0f} {block:5d} {actual:.6e} {rraw:.6e} "
                f"{rraw/(L**4):.6e} {bound:.6e} {bound/actual:.2f} {cobs:.3f}",
                flush=True,
            )


if __name__ == "__main__":
    run()
