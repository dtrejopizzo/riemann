#!/usr/bin/env python3
import itertools
import sys

import numpy as np
from numpy.linalg import cholesky, norm, solve

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
from E71_9_relative_arch_background_probe import primes_upto  # noqa: E402

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_158_prime_cell_psd_probe import q_matrix  # noqa: E402


def u_matrix(idx, L, y):
    d = 2.0 * np.pi * idx / L
    out = np.zeros((len(idx), len(idx)), dtype=complex)
    for a, dm in enumerate(d):
        for b, dn in enumerate(d):
            if a == b:
                out[a, b] = (1.0 - y / L) * np.exp(1j * dn * y)
            else:
                out[a, b] = (np.exp(1j * dn * y) - np.exp(1j * dm * y)) / (1j * L * (dm - dn))
    return out


def relative_matrix(mat, c_model):
    chol = cholesky(c_model)
    x = solve(chol, mat)
    rel = solve(chol, x.T).T
    return 0.5 * (rel + rel.conj().T)


def cells(lam, idx, L, bq, c_model, cut=0.60, block_id=0):
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
                qrel = relative_matrix(bq.T @ (-beta * q_matrix(idx, L, y)) @ bq, c_model)
                u = u_matrix(idx, L, y)
                up = relative_matrix(bq.T @ (-beta * u) @ bq, c_model)
                um = relative_matrix(bq.T @ (-beta * u.conj().T) @ bq, c_model)
                ans.append((pm, y, qrel, up, um))
            if pm > maxn // p:
                break
            pm *= p
            me += 1
    return ans


def trace_word(mats):
    prod = np.eye(mats[0].shape[0], dtype=complex)
    for m in mats:
        prod = prod @ m
    return np.trace(prod)


def signed_expansion_trace(word):
    total = 0.0j
    for signs in itertools.product([0, 1], repeat=len(word)):
        mats = [word[i][3] if s == 0 else word[i][4] for i, s in enumerate(signs)]
        total += trace_word(mats)
    return total


def run():
    print("E72.197 signed Green-word expansion probe")
    print("checks Q_y=U_y+U_y* after exact relative whitening")
    print("lam block r direct signed relErr imag")
    for lam, n_modes in [(6, 18), (8, 24), (12, 32)]:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        for block_id in [0, 1]:
            cs = cells(lam, idx, L, bq, c_model, 0.60, block_id)
            if len(cs) < 3:
                continue
            # Use the first few cells. This is an algebraic identity, not a stress over all words.
            for r in [2, 3]:
                word = cs[:r]
                direct = trace_word([c[2] for c in word])
                signed = signed_expansion_trace(word)
                rel = abs(direct - signed) / max(abs(direct), 1e-30)
                imag = max(abs(direct.imag), abs(signed.imag))
                print(
                    f"{lam:3.0f} {block_id:5d} {r:1d} "
                    f"{direct.real:+.12e} {signed.real:+.12e} {rel:.3e} {imag:.3e}"
                )


if __name__ == "__main__":
    run()
