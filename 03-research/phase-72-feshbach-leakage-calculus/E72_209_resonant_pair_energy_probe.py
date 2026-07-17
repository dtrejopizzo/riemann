#!/usr/bin/env python3
import sys

import numpy as np
from numpy.linalg import cholesky, norm, solve

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
from E71_9_relative_arch_background_probe import primes_upto  # noqa: E402

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_197_signed_green_word_probe import u_matrix  # noqa: E402


WINDOWS = [(12, 32), (16, 40), (20, 48), (24, 56), (28, 64)]


def plus_cells(lam, idx, L, bq, c_model, cut=0.60, block_id=0):
    ans = []
    maxn = int(lam * lam)
    chol = cholesky(c_model)
    for p in primes_upto(maxn):
        lp = np.log(p)
        pm = p
        me = 1
        while pm <= maxn:
            y = me * lp
            bid = 0 if y <= cut * L else 1
            if bid == block_id:
                beta = lp * (pm ** -0.5)
                u = u_matrix(idx, L, y)
                ap0 = bq.T @ (-beta * u) @ bq
                x = solve(chol, ap0)
                ans.append(solve(chol, x.T).T)
            if pm > maxn // p:
                break
            pm *= p
            me += 1
    return ans


def block_moment2(cells):
    k = sum((a + a.conj().T for a in cells), np.zeros_like(cells[0], dtype=complex))
    return float(np.real(np.trace(k @ k)))


def resonant_pair(cells):
    return float(2.0 * sum(norm(a, "fro") ** 2 for a in cells))


def run():
    print("E72.209 resonant pair energy probe")
    print("r=2 resonant identity: Res2 = 2 sum_n ||A_n^+||_HS^2")
    print("lam block cells totalTrK2 Res2 NonRes2 ResFrac")
    for lam, n_modes in WINDOWS:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        for block_id in [0, 1]:
            cells = plus_cells(lam, idx, L, bq, c_model, 0.60, block_id)
            total = block_moment2(cells)
            res = resonant_pair(cells)
            non = total - res
            print(
                f"{lam:3.0f} {block_id:5d} {len(cells):5d} "
                f"{total:+.6e} {res:+.6e} {non:+.6e} {res / total:.3f}"
                ,
                flush=True,
            )


if __name__ == "__main__":
    run()
