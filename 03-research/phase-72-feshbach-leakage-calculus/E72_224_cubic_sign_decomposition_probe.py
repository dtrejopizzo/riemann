#!/usr/bin/env python3
import sys

import numpy as np
from numpy.linalg import cholesky, solve

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
from E71_9_relative_arch_background_probe import primes_upto  # noqa: E402

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_197_signed_green_word_probe import u_matrix  # noqa: E402


WINDOWS = [(12, 32), (16, 40), (20, 48), (24, 56), (28, 64), (32, 72)]


def plus_sum(lam, idx, L, bq, c_model, cut=0.60, block_id=1):
    chol = cholesky(c_model)
    out = np.zeros((bq.shape[1], bq.shape[1]), dtype=complex)
    maxn = int(lam * lam)
    for p in primes_upto(maxn):
        lp = np.log(p)
        pm = p
        me = 1
        while pm <= maxn:
            y = me * lp
            bid = 0 if y <= cut * L else 1
            if bid == block_id:
                beta = lp * (pm ** -0.5)
                raw = bq.T @ (-beta * u_matrix(idx, L, y)) @ bq
                x = solve(chol, raw)
                out += solve(chol, x.T).T
            if pm > maxn // p:
                break
            pm *= p
            me += 1
    return out


def tr3(a, b, c):
    return float(np.real(np.trace(a @ b @ c)))


def run():
    print("E72.224 cubic sign decomposition probe")
    print("High block: K=A+A*, decompose Tr(K^3) by cyclic sign types")
    print("lam dim total +++ --- ++- +-- mixed totalCheck")
    for lam, n_modes in WINDOWS:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        a = plus_sum(lam, idx, L, bq, c_model, 0.60, 1)
        b = a.conj().T
        total = tr3(a + b, a + b, a + b)
        ppp = tr3(a, a, a)
        mmm = tr3(b, b, b)
        # Cyclic trace makes the three ++- words equal in real trace, and same for +--.
        ppm = tr3(a, a, b)
        pmm = tr3(a, b, b)
        mixed = 3.0 * ppm + 3.0 * pmm
        check = ppp + mmm + mixed
        print(
            f"{lam:3.0f} {bq.shape[1]:3d} {total:+.6e} "
            f"{ppp:+.6e} {mmm:+.6e} {3*ppm:+.6e} {3*pmm:+.6e} "
            f"{mixed:+.6e} {check:+.6e}",
            flush=True,
        )


if __name__ == "__main__":
    run()
