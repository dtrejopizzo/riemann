#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import cholesky, eigvalsh, norm, solve

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
from E71_9_relative_arch_background_probe import primes_upto  # noqa: E402

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402


def q_entry(m, n, L, y):
    if y < 0.0 or y > L:
        return 0.0
    if m == n:
        return 2.0 * (1.0 - y / L) * np.cos(2.0 * np.pi * n * y / L)
    c = 1.0 / (np.pi * (n - m))
    return (np.sin(2.0 * np.pi * m * y / L) - np.sin(2.0 * np.pi * n * y / L)) * c


def q_matrix(idx, L, y):
    mat = np.zeros((len(idx), len(idx)))
    for a, m in enumerate(idx):
        for b in range(a, len(idx)):
            val = q_entry(int(m), int(idx[b]), L, y)
            mat[a, b] = val
            mat[b, a] = val
    return mat


def prime_cells(lam, idx, L):
    cells = []
    maxn = int(lam * lam)
    for p in primes_upto(maxn):
        lp = np.log(p)
        pm = p
        me = 1
        while pm <= maxn:
            y = me * lp
            weight = lp * (pm ** -0.5)
            cells.append((pm, weight, y, q_matrix(idx, L, y)))
            if pm > maxn // p:
                break
            pm *= p
            me += 1
    return cells


def relative_matrix(mat, c_model):
    chol = cholesky(c_model)
    x = solve(chol, mat)
    rel = solve(chol, x.T).T
    return 0.5 * (rel + rel.T)


def psd_distance(krel, pmat):
    vals = eigvalsh(pmat)
    if vals[0] < -1e-8:
        return np.nan
    diff = krel - pmat
    return norm(diff, "fro")


def run(topk=3):
    print(f"E72.158 prime-cell PSD probe topk={topk}")
    print(" lam   L cells  distOpt  distTopCells  topMassFrac  topCellN")
    for lam, n_modes in [(6, 18), (8, 24), (10, 28), (12, 32)]:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        krel = relative_matrix(c_actual - c_model, c_model)
        eigs = eigvalsh(krel)
        dist_opt = np.sqrt(np.sum(eigs[eigs < 0.0] ** 2))

        cells = prime_cells(lam, idx, L)
        rel_cells = []
        total_norm = 0.0
        for nval, weight, y, qmat in cells:
            # actual-model = - prime part
            comp = bq.T @ (-weight * qmat) @ bq
            rcell = relative_matrix(comp, c_model)
            cn = norm(rcell, "fro")
            total_norm += cn
            rel_cells.append((cn, nval, rcell))
        rel_cells.sort(reverse=True, key=lambda t: t[0])
        psd = np.zeros_like(krel)
        for _, _, rcell in rel_cells[:topk]:
            vals, vecs = np.linalg.eigh(rcell)
            pos = np.maximum(vals, 0.0)
            psd += (vecs * pos) @ vecs.T
        dist = psd_distance(krel, psd)
        top_frac = sum(c for c, _, _ in rel_cells[:topk]) / max(total_norm, 1e-30)
        top_names = ",".join(str(n) for _, n, _ in rel_cells[:topk])
        print(
            f"{lam:4.0f} {L:5.2f} {len(cells):5d} "
            f"{dist_opt:8.3f} {dist:12.3f} {top_frac:12.3f} {top_names}"
        )


if __name__ == "__main__":
    run()
