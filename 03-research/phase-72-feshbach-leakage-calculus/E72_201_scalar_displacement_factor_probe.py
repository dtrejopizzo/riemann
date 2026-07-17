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
    rel = solve(chol, x.T).T
    return rel


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
                up = relative_matrix_raw(bq.T @ u @ bq, c_model)
                um = relative_matrix_raw(bq.T @ u.conj().T @ bq, c_model)
                ans.append((pm, +1, y, beta, up))
                ans.append((pm, -1, -y, beta, um))
            if pm > maxn // p:
                break
            pm *= p
            me += 1
    return ans


def key_for_word(word):
    num = 1
    den = 1
    disp = 0.0
    beta_prod = 1.0
    for n, sgn, signed_y, beta, _ in word:
        disp += signed_y
        beta_prod *= beta
        if sgn > 0:
            num *= n
        else:
            den *= n
        g = math.gcd(num, den)
        num //= g
        den //= g
    return (num, den), disp, beta_prod


def trace_product(word):
    prod = np.eye(word[0][4].shape[0], dtype=complex)
    for _, _, _, _, mat in word:
        prod = prod @ mat
    return np.trace(prod)


def collect(cells, r):
    by_key = defaultdict(list)
    for idxs in itertools.product(range(len(cells)), repeat=r):
        word = [cells[i] for i in idxs]
        key, disp, beta_prod = key_for_word(word)
        # Full signed cell uses -beta*U, so full class contribution is
        # (-1)^r beta_prod * trace_product(unit word).
        kval = trace_product(word).real
        by_key[key].append((disp, beta_prod, kval))
    return by_key


def summarize(by_key, r):
    rows = []
    for key, vals in by_key.items():
        if key == (1, 1) or len(vals) < 4:
            continue
        disp = vals[0][0]
        betas = np.array([v[1] for v in vals], dtype=float)
        kernels = np.array([v[2] for v in vals], dtype=float)
        contribs = ((-1.0) ** r) * betas * kernels
        class_sum = float(np.sum(contribs))
        weighted_kernel = float(np.sum(betas * kernels) / max(np.sum(betas), 1e-300))
        spread = float(np.std(kernels) / max(abs(np.mean(kernels)), 1e-30))
        abs_spread = float(np.max(kernels) - np.min(kernels))
        rows.append((abs(class_sum), class_sum, key, disp, len(vals), weighted_kernel, spread, abs_spread))
    rows.sort(reverse=True)
    return rows


def run():
    print("E72.201 scalar displacement factor test")
    print("tests whether same-R words share one scalar Green kernel")
    print("lam rank logR key words classSum wKernel relSpread absSpread")
    for lam, n_modes in [(6, 18), (8, 24), (10, 28)]:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        cells = signed_cells(lam, idx, L, bq, c_model, 0.60, block_id=1)
        rows = summarize(collect(cells, 3), 3)
        print(f"-- lambda={lam}")
        for rank, row in enumerate(rows[:12], start=1):
            _, class_sum, key, disp, nwords, wk, spread, abs_spread = row
            print(
                f"{lam:3.0f} {rank:4d} {disp:+8.3f} {key[0]}/{key[1]} "
                f"{nwords:5d} {class_sum:+.6e} {wk:+.6e} {spread:.3e} {abs_spread:.3e}"
            )


if __name__ == "__main__":
    run()
