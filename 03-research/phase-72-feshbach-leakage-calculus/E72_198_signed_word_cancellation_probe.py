#!/usr/bin/env python3
import itertools
import sys

import numpy as np
from numpy.linalg import cholesky, solve

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
from E71_9_relative_arch_background_probe import primes_upto  # noqa: E402

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_197_signed_green_word_probe import u_matrix  # noqa: E402


def relative_matrix(mat, c_model):
    chol = cholesky(c_model)
    x = solve(chol, mat)
    rel = solve(chol, x.T).T
    return 0.5 * (rel + rel.conj().T)


def signed_cells(lam, idx, L, bq, c_model, cut=0.60, block_id=0):
    ans = []
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
                u = u_matrix(idx, L, y)
                ans.append(relative_matrix(bq.T @ (-beta * u) @ bq, c_model))
                ans.append(relative_matrix(bq.T @ (-beta * u.conj().T) @ bq, c_model))
            if pm > maxn // p:
                break
            pm *= p
            me += 1
    return ans


def trace_product(word):
    prod = np.eye(word[0].shape[0], dtype=complex)
    for mat in word:
        prod = prod @ mat
    return np.trace(prod)


def abs_ceiling(cells, r):
    total = 0.0
    for word in itertools.product(range(len(cells)), repeat=r):
        total += abs(trace_product([cells[i] for i in word]))
    return float(total)


def run():
    print("E72.198 signed Green-word cancellation diagnostic")
    print("reports |Tr(K^r)| versus sum of absolute signed-word traces")
    print("lam block r cells signedTrace absCeil ratio")
    for lam, n_modes in [(6, 18), (8, 24), (10, 28)]:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        for block_id in [0, 1]:
            cs = signed_cells(lam, idx, L, bq, c_model, 0.60, block_id)
            ksum = sum(cs)
            for r in [2, 3]:
                direct = np.trace(np.linalg.matrix_power(ksum, r))
                ceil = abs_ceiling(cs, r)
                ratio = ceil / max(abs(direct), 1e-30)
                print(
                    f"{lam:3.0f} {block_id:5d} {r:1d} {len(cs):5d} "
                    f"{direct.real:+.6e} {ceil:.6e} {ratio:.3e}"
                )


if __name__ == "__main__":
    run()
