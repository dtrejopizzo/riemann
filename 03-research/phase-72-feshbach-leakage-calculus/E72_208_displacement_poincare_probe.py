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
    return float(np.real(np.trace(prod)))


def moments(cells, r):
    m0 = 0.0
    m2 = 0.0
    res0 = 0.0
    non0 = 0.0
    non2 = 0.0
    non_abs0 = 0.0
    min_non = float("inf")
    for idxs in itertools.product(range(len(cells)), repeat=r):
        disp = sum(cells[i][0] for i in idxs)
        tr = trace_product([cells[i][1] for i in idxs])
        m0 += tr
        m2 += (disp * disp) * tr
        if abs(disp) < 1e-10:
            res0 += tr
        else:
            non0 += tr
            non2 += (disp * disp) * tr
            non_abs0 += abs(tr)
            min_non = min(min_non, abs(disp))
    return m0, m2, res0, non0, non2, non_abs0, min_non


def run():
    print("E72.208 displacement Poincare diagnostic")
    print("m0=sum Tr(word), m2=sum Delta^2 Tr(word)")
    print("lam block r m0 m2 res0 non0 non2 minD effGap absRatio")
    for lam, n_modes in [(6, 18), (8, 24), (10, 28), (12, 32)]:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        for block_id in [0, 1]:
            cells = signed_cells(lam, idx, L, bq, c_model, 0.60, block_id)
            for r in [2, 3]:
                m0, m2, res0, non0, non2, non_abs0, min_non = moments(cells, r)
                eff_gap = np.sqrt(abs(non2 / non0)) if abs(non0) > 1e-30 and non2 / non0 > 0 else np.nan
                abs_ratio = non_abs0 / max(abs(non0), 1e-30)
                print(
                    f"{lam:3.0f} {block_id:5d} {r:1d} "
                    f"{m0:+.6e} {m2:+.6e} {res0:+.6e} {non0:+.6e} "
                    f"{non2:+.6e} {min_non:.3f} {eff_gap:.3f} {abs_ratio:.2f}"
                )


if __name__ == "__main__":
    run()
