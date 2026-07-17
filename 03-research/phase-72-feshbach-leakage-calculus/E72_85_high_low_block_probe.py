#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import eigh, norm, solve, svd

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
from E71_9_relative_arch_background_probe import build  # noqa: E402


def even_basis_from_mask(idx, mask):
    n = len(idx)
    cols = []
    if mask[np.where(idx == 0)[0][0]]:
        col = np.zeros(n)
        col[np.where(idx == 0)[0][0]] = 1.0
        cols.append(col)
    for m in idx[idx > 0]:
        ip = np.where(idx == m)[0][0]
        im = np.where(idx == -m)[0][0]
        if mask[ip] and mask[im]:
            col = np.zeros(n)
            col[ip] = 1.0 / np.sqrt(2.0)
            col[im] = 1.0 / np.sqrt(2.0)
            cols.append(col)
    if not cols:
        return np.zeros((n, 0))
    return np.column_stack(cols)


def orth(a, tol=1e-10):
    if a.shape[1] == 0:
        return a
    u, s, _ = svd(a, full_matrices=False)
    return u[:, s > tol]


def setup_full(lam, n_modes):
    h_actual, idx, L = build(lam, n_modes, include_arith=True)
    h_model, _, _ = build(lam, n_modes, include_arith=False)
    evals_model, vec_model = eigh(h_model)
    k = vec_model[:, 0]
    k = (k + k[::-1]) / 2
    k = k / norm(k)
    d = 2 * np.pi * idx / L
    q = np.eye(len(idx)) - np.outer(k, k)
    c = q @ (h_actual - evals_model[0] * np.eye(len(idx))) @ q
    return idx, d, k, q, c


def low_high_bases(idx, d, k, hcut):
    q = np.eye(len(idx)) - np.outer(k, k)
    low_mask = np.abs(d) <= hcut
    high_mask = np.abs(d) > hcut
    e_low = even_basis_from_mask(idx, low_mask)
    e_high = even_basis_from_mask(idx, high_mask)
    b_low = orth(q @ e_low)
    high_raw = q @ e_high
    if b_low.shape[1] > 0:
        high_raw = high_raw - b_low @ (b_low.T @ high_raw)
    b_high = orth(high_raw)
    return b_low, b_high


def run():
    s_values = [5 + 0.2j, 10 + 0.2j, 15 + 0.2j]
    hcuts = [4, 8, 12, 18, 24]
    print("E72.85 high/low block decoupling probe")
    print(" lam   N Hcut dimL dimH  ||CHH^-1CHL||  max source-tail")
    for lam, n_modes in [(12, 28), (16, 34), (20, 40)]:
        idx, d, k, q, c = setup_full(lam, n_modes)
        for hcut in hcuts:
            b_low, b_high = low_high_bases(idx, d, k, hcut)
            if b_high.shape[1] == 0:
                continue
            chh = b_high.T @ c @ b_high
            chl = b_high.T @ c @ b_low
            try:
                decouple = norm(solve(chh, chl), 2) if b_low.shape[1] else 0.0
                source_tails = []
                for s in s_values:
                    src = q @ (s / (s * s - d * d))
                    source_tails.append(norm(b_high.T @ src) / max(norm(src), 1e-30))
                print(
                    f"{lam:4.0f} {n_modes:3d} {hcut:4.0f} "
                    f"{b_low.shape[1]:4d} {b_high.shape[1]:4d} "
                    f"{decouple:16.3e} {max(source_tails):16.3e}"
                )
            except np.linalg.LinAlgError:
                print(
                    f"{lam:4.0f} {n_modes:3d} {hcut:4.0f} "
                    f"{b_low.shape[1]:4d} {b_high.shape[1]:4d} singular"
                )


if __name__ == "__main__":
    run()
