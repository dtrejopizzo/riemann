#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import cholesky, eigvalsh, norm, solve

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
from E71_9_relative_arch_background_probe import primes_upto  # noqa: E402

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_158_prime_cell_psd_probe import q_matrix  # noqa: E402


def relative_matrix(mat, c_model):
    chol = cholesky(c_model)
    x = solve(chol, mat)
    rel = solve(chol, x.T).T
    return 0.5 * (rel + rel.T)


def psd_part(mat):
    vals, vecs = np.linalg.eigh(mat)
    pos = np.maximum(vals, 0.0)
    return (vecs * pos) @ vecs.T


def block_matrices(lam, idx, L, bq, c_model, nbins):
    mats = [np.zeros((len(bq.T), len(bq.T))) for _ in range(nbins)]
    maxn = int(lam * lam)
    for p in primes_upto(maxn):
        lp = np.log(p)
        pm = p
        me = 1
        while pm <= maxn:
            y = me * lp
            weight = lp * (pm ** -0.5)
            bin_id = min(nbins - 1, int(nbins * y / max(L, 1e-30)))
            qmat = q_matrix(idx, L, y)
            comp = bq.T @ (-weight * qmat) @ bq
            mats[bin_id] += relative_matrix(comp, c_model)
            if pm > maxn // p:
                break
            pm *= p
            me += 1
    return mats


def run():
    print("E72.159 prime-block PSD probe")
    print(" lam   L bins  distOpt  distBlocks  bestBins  blockNorms")
    for nbins in [2, 3, 4, 6]:
        print(f"-- nbins={nbins}")
        for lam, n_modes in [(6, 18), (8, 24), (10, 28), (12, 32)]:
            idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
            krel = relative_matrix(c_actual - c_model, c_model)
            eigs = eigvalsh(krel)
            dist_opt = np.sqrt(np.sum(eigs[eigs < 0.0] ** 2))
            blocks = block_matrices(lam, idx, L, bq, c_model, nbins)
            pmat = np.zeros_like(krel)
            norms = []
            for block in blocks:
                pmat += psd_part(block)
                norms.append(norm(block, "fro"))
            dist = norm(krel - pmat, "fro")
            norm_str = ",".join(f"{v:.2f}" for v in norms)
            print(
                f"{lam:4.0f} {L:5.2f} {nbins:4d} "
                f"{dist_opt:8.3f} {dist:10.3f} all {norm_str}"
            )


if __name__ == "__main__":
    run()
