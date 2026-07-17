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
from E72_206_trace_character_jet_probe import plus_cells, trace_moment  # noqa: E402


def signed_cells(lam, idx, L, bq, c_model, cut=0.60, block_id=0):
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
                ap = solve(chol, x.T).T
                ans.append((+y, ap))
                ans.append((-y, ap.conj().T))
            if pm > maxn // p:
                break
            pm *= p
            me += 1
    return ans


def trace_product(mats):
    prod = np.eye(mats[0].shape[0], dtype=complex)
    for mat in mats:
        prod = prod @ mat
    return np.trace(prod)


def displacement_square_sum(cells, r):
    total = 0.0
    for idxs in itertools.product(range(len(cells)), repeat=r):
        disp = sum(cells[i][0] for i in idxs)
        tr = trace_product([cells[i][1] for i in idxs])
        total += (disp * disp) * float(np.real(tr))
    return total


def fd_second(plus, r, h=1e-4):
    f0 = trace_moment(plus, r, 0.0)
    fp = trace_moment(plus, r, h)
    fm = trace_moment(plus, r, -h)
    return (fp - 2 * f0 + fm) / (h * h)


def run():
    print("E72.207 displacement-square identity probe")
    print("checks F''(0) = -sum_words Delta(word)^2 Tr(word)")
    print("lam block r fdSecond negDispSq relErr")
    for lam, n_modes in [(6, 18), (8, 24), (10, 28), (12, 32)]:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        for block_id in [0, 1]:
            signed = signed_cells(lam, idx, L, bq, c_model, 0.60, block_id)
            plus = plus_cells(lam, idx, L, bq, c_model, 0.60, block_id)
            for r in [2, 3]:
                fd2 = fd_second(plus, r)
                rhs = -displacement_square_sum(signed, r)
                rel = abs(fd2 - rhs) / max(abs(fd2), 1e-30)
                print(f"{lam:3.0f} {block_id:5d} {r:1d} {fd2:+.9e} {rhs:+.9e} {rel:.3e}")


if __name__ == "__main__":
    run()
