#!/usr/bin/env python3
import sys

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


def plus_cells(lam, idx, L, bq, c_model, cut=0.60, block_id=0):
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
                ans.append((y, ap))
            if pm > maxn // p:
                break
            pm *= p
            me += 1
    return ans


def eval_character(cells, t):
    out = np.zeros_like(cells[0][1], dtype=complex)
    for y, ap in cells:
        z = np.exp(1j * t * y)
        out += z * ap + np.conj(z) * ap.conj().T
    return 0.5 * (out + out.conj().T)


def trace_moment(cells, r, t):
    a = eval_character(cells, t)
    return float(np.real(np.trace(np.linalg.matrix_power(a, r))))


def jets(cells, r, h=1e-3):
    f0 = trace_moment(cells, r, 0.0)
    fp = trace_moment(cells, r, h)
    fm = trace_moment(cells, r, -h)
    fpp = trace_moment(cells, r, 2 * h)
    fmm = trace_moment(cells, r, -2 * h)
    first = (fp - fm) / (2 * h)
    second = (fp - 2 * f0 + fm) / (h * h)
    third = (fpp - 2 * fp + 2 * fm - fmm) / (2 * h**3)
    fourth = (fpp - 4 * fp + 6 * f0 - 4 * fm + fmm) / (h**4)
    return f0, first, second, third, fourth


def run():
    print("E72.206 trace character jet probe")
    print("finite-difference jets of Tr(A_j(t)^r) at augmentation")
    print("lam block r f0 f1 f2 f3 f4")
    for lam, n_modes in [(12, 32), (16, 40), (20, 48), (24, 56)]:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        for block_id in [0, 1]:
            cells = plus_cells(lam, idx, L, bq, c_model, 0.60, block_id)
            for r in [2, 3, 4, 8]:
                f0, f1, f2, f3, f4 = jets(cells, r)
                print(
                    f"{lam:3.0f} {block_id:5d} {r:2d} "
                    f"{f0:+.6e} {f1:+.2e} {f2:+.3e} {f3:+.2e} {f4:+.3e}"
                )


if __name__ == "__main__":
    run()
