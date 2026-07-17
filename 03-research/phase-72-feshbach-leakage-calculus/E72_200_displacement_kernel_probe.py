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


def relative_matrix(mat, c_model):
    chol = cholesky(c_model)
    x = solve(chol, mat)
    rel = solve(chol, x.T).T
    return 0.5 * (rel + rel.conj().T)


def signed_cells(lam, idx, L, bq, c_model, cut=0.60, block_id=1):
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
                ans.append((pm, +1, y, relative_matrix(bq.T @ (-beta * u) @ bq, c_model)))
                ans.append((pm, -1, -y, relative_matrix(bq.T @ (-beta * u.conj().T) @ bq, c_model)))
            if pm > maxn // p:
                break
            pm *= p
            me += 1
    return ans


def key_for_word(word):
    num = 1
    den = 1
    disp = 0.0
    for n, sgn, signed_y, _ in word:
        disp += signed_y
        if sgn > 0:
            num *= n
        else:
            den *= n
        g = math.gcd(num, den)
        num //= g
        den //= g
    return (num, den), disp


def trace_product(word):
    prod = np.eye(word[0][3].shape[0], dtype=complex)
    for _, _, _, mat in word:
        prod = prod @ mat
    return np.trace(prod)


def class_sums(cells, r):
    by_key = defaultdict(complex)
    by_disp = {}
    for idxs in itertools.product(range(len(cells)), repeat=r):
        word = [cells[i] for i in idxs]
        key, disp = key_for_word(word)
        by_key[key] += trace_product(word)
        by_disp[key] = disp
    rows = []
    for key, val in by_key.items():
        rows.append((abs(val), val.real, by_disp[key], key))
    rows.sort(reverse=True)
    return rows


def run():
    print("E72.200 displacement-kernel probe")
    print("top non-resonant class sums for high block r=3")
    print("lam rank logR classSum abs key")
    for lam, n_modes in [(6, 18), (8, 24), (10, 28), (12, 32)]:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        cs = signed_cells(lam, idx, L, bq, c_model, 0.60, block_id=1)
        rows = [r for r in class_sums(cs, 3) if r[3] != (1, 1)]
        print(f"-- lambda={lam}, classes={len(rows)}")
        for rank, (absv, val, disp, key) in enumerate(rows[:12], start=1):
            print(f"{lam:3.0f} {rank:4d} {disp:+8.3f} {val:+.6e} {absv:.6e} {key[0]}/{key[1]}")


if __name__ == "__main__":
    run()
