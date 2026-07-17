#!/usr/bin/env python3
import itertools
import math
import sys
from collections import defaultdict

import numpy as np
from numpy.linalg import cholesky, solve

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
from E71_9_relative_arch_background_probe import primes_upto  # noqa: E402

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_197_signed_green_word_probe import u_matrix  # noqa: E402


def relative_matrix_raw(mat, c_model):
    chol = cholesky(c_model)
    x = solve(chol, mat)
    return solve(chol, x.T).T


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
                ap = relative_matrix_raw(bq.T @ (-beta * u) @ bq, c_model)
                am = relative_matrix_raw(bq.T @ (-beta * u.conj().T) @ bq, c_model)
                ans.append((pm, +1, ap))
                ans.append((pm, -1, am))
            if pm > maxn // p:
                break
            pm *= p
            me += 1
    return ans


def mul_key(k1, k2):
    num = k1[0] * k2[0]
    den = k1[1] * k2[1]
    g = math.gcd(num, den)
    return num // g, den // g


def cell_key(n, sgn):
    return (n, 1) if sgn > 0 else (1, n)


def coeff_power(cells, r):
    coeffs = {(1, 1): np.eye(cells[0][2].shape[0], dtype=complex)}
    for _ in range(r):
        nxt = defaultdict(lambda: np.zeros_like(cells[0][2], dtype=complex))
        for key, mat in coeffs.items():
            for n, sgn, amat in cells:
                nxt[mul_key(key, cell_key(n, sgn))] += mat @ amat
        coeffs = dict(nxt)
    return coeffs


def run():
    print("E72.202 operator-valued group-algebra certificate probe")
    print("checks Tr(epsilon(A)^r)=sum_R Tr coeff_R(A^r)")
    print("lam block r coeffs direct coeffSum relErr")
    for lam, n_modes in [(6, 18), (8, 24), (10, 28)]:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        for block_id in [0, 1]:
            cells = signed_cells(lam, idx, L, bq, c_model, 0.60, block_id)
            ksum = sum((c[2] for c in cells), np.zeros_like(cells[0][2], dtype=complex))
            for r in [2, 3]:
                coeffs = coeff_power(cells, r)
                direct = np.trace(np.linalg.matrix_power(ksum, r))
                coeff_sum = sum(np.trace(m) for m in coeffs.values())
                rel = abs(direct - coeff_sum) / max(abs(direct), 1e-30)
                print(
                    f"{lam:3.0f} {block_id:5d} {r:1d} {len(coeffs):6d} "
                    f"{direct.real:+.12e} {coeff_sum.real:+.12e} {rel:.3e}"
                )


if __name__ == "__main__":
    run()
