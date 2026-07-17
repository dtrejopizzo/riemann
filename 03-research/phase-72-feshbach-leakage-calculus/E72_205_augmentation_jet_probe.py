#!/usr/bin/env python3
import sys

import numpy as np
from numpy.linalg import cholesky, eigh, solve

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


def jets(cells):
    shape = cells[0][1].shape
    a0 = np.zeros(shape, dtype=complex)
    a1 = np.zeros(shape, dtype=complex)
    a2 = np.zeros(shape, dtype=complex)
    for y, ap in cells:
        am = ap.conj().T
        a0 += ap + am
        a1 += 1j * y * ap - 1j * y * am
        a2 += -(y**2) * (ap + am)
    return (
        0.5 * (a0 + a0.conj().T),
        0.5 * (a1 + a1.conj().T),
        0.5 * (a2 + a2.conj().T),
    )


def eig_jet(a0, a1, a2):
    vals, vecs = eigh(a0)
    rows = []
    for pos in [0, len(vals) - 1]:
        lam0 = vals[pos]
        v = vecs[:, pos]
        lam1 = float(np.real(np.vdot(v, a1 @ v)))
        lam2_diag = float(np.real(np.vdot(v, a2 @ v)))
        # Rayleigh-Schr perturbation if the eigenvalue is simple enough.
        gap_sum = 0.0
        for k, mu in enumerate(vals):
            if k == pos:
                continue
            denom = lam0 - mu
            if abs(denom) > 1e-10:
                w = vecs[:, k]
                gap_sum += 2.0 * abs(np.vdot(w, a1 @ v)) ** 2 / denom
        lam2 = lam2_diag + float(np.real(gap_sum))
        rows.append((pos, float(lam0), lam1, lam2, lam2_diag, float(np.real(gap_sum))))
    return rows


def finite_eval(cells, t):
    out = np.zeros_like(cells[0][1], dtype=complex)
    for y, ap in cells:
        z = np.exp(1j * t * y)
        out += z * ap + np.conj(z) * ap.conj().T
    return 0.5 * (out + out.conj().T)


def finite_curvature(cells, pos, h=1e-3):
    vals0 = eigh(finite_eval(cells, 0.0))[0]
    valsp = eigh(finite_eval(cells, h))[0]
    valsm = eigh(finite_eval(cells, -h))[0]
    idx = 0 if pos == 0 else -1
    first = float((valsp[idx] - valsm[idx]) / (2 * h))
    second = float((valsp[idx] - 2 * vals0[idx] + valsm[idx]) / (h * h))
    return first, second


def run():
    print("E72.205 augmentation character jet probe")
    print("eig=min/max at t=0; lambda1, lambda2 are perturbative derivatives")
    print("lam block eig lambda0 lambda1 lambda2 fd1 fd2 diag2 mix2")
    for lam, n_modes in [(12, 32), (16, 40), (20, 48), (24, 56)]:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        for block_id in [0, 1]:
            cells = plus_cells(lam, idx, L, bq, c_model, 0.60, block_id)
            a0, a1, a2 = jets(cells)
            for pos, lam0, lam1, lam2, diag2, mix2 in eig_jet(a0, a1, a2):
                fd1, fd2 = finite_curvature(cells, pos)
                label = "min" if pos == 0 else "max"
                print(
                    f"{lam:3.0f} {block_id:5d} {label:>3s} "
                    f"{lam0:+.6f} {lam1:+.2e} {lam2:+.3e} "
                    f"{fd1:+.2e} {fd2:+.3e} {diag2:+.3e} {mix2:+.3e}"
                )


if __name__ == "__main__":
    run()
