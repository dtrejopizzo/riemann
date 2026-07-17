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
                ans.append((pm, +1, relative_matrix(bq.T @ (-beta * u) @ bq, c_model)))
                ans.append((pm, -1, relative_matrix(bq.T @ (-beta * u.conj().T) @ bq, c_model)))
            if pm > maxn // p:
                break
            pm *= p
            me += 1
    return ans


def key_for_word(word):
    num = 1
    den = 1
    for n, sgn, _ in word:
        if sgn > 0:
            num *= n
        else:
            den *= n
        g = math.gcd(num, den)
        num //= g
        den //= g
    return num, den


def trace_product(word):
    prod = np.eye(word[0][2].shape[0], dtype=complex)
    for _, _, mat in word:
        prod = prod @ mat
    return np.trace(prod)


def analyze(cells, r):
    by_key = defaultdict(complex)
    by_abs = defaultdict(float)
    for idxs in itertools.product(range(len(cells)), repeat=r):
        word = [cells[i] for i in idxs]
        key = key_for_word(word)
        val = trace_product(word)
        by_key[key] += val
        by_abs[key] += abs(val)
    total = sum(by_key.values())
    resonant = by_key.get((1, 1), 0.0j)
    nonres = total - resonant
    abs_total = sum(by_abs.values())
    abs_nonres = abs_total - by_abs.get((1, 1), 0.0)
    return total, resonant, nonres, abs_total, abs_nonres, len(by_key)


def run():
    print("E72.199 signed displacement resonance probe")
    print("groups signed Green-words by exact product prod n^eps")
    print("lam block r groups total resonant nonres absTotal absNonres")
    for lam, n_modes in [(6, 18), (8, 24), (10, 28)]:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        for block_id in [0, 1]:
            cs = signed_cells(lam, idx, L, bq, c_model, 0.60, block_id)
            for r in [2, 3]:
                total, resonant, nonres, abs_total, abs_nonres, ng = analyze(cs, r)
                print(
                    f"{lam:3.0f} {block_id:5d} {r:1d} {ng:6d} "
                    f"{total.real:+.6e} {resonant.real:+.6e} {nonres.real:+.6e} "
                    f"{abs_total:.6e} {abs_nonres:.6e}"
                )


if __name__ == "__main__":
    run()
