#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import eigh, norm, svd, lstsq

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E71_9_relative_arch_background_probe import build  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_003_critical_source_probe import dd_kernel  # noqa: E402


def setup_full(lam, n_modes):
    h_actual, idx, L = build(lam, n_modes, include_arith=True)
    vals, vecs = eigh(h_actual)
    d = 2.0 * np.pi * idx / L
    return h_actual, vals[0], idx.astype(int), d, L


def local_basis(off_nodes, crit_nodes, d, L, powers, poly_powers=()):
    cols = []
    labels = []
    for ki, k in enumerate(crit_nodes):
        gamma = (-1j * k).real
        dd = np.array([dd_kernel(-gamma, dm, L) for dm in d], dtype=complex)
        for bi, beta in enumerate(off_nodes):
            denom = np.array([dm * dm + beta * beta for dm in d], dtype=complex)
            for r in powers:
                if r == 0:
                    cols.append(dd.copy())
                else:
                    cols.append(dd / (denom ** r))
                labels.append((ki, bi, r))
        for q in poly_powers:
            cols.append((d ** (2 * q)) * dd)
            labels.append((ki, -1, -q))
    return np.column_stack(cols), labels


def projection_stats(target, basis, tol=1e-10):
    coeffs, *_ = lstsq(basis, target, rcond=None)
    approx = basis @ coeffs
    rel = norm(target - approx) / max(norm(target), 1e-30)
    u, s, vh = svd(basis, full_matrices=False)
    rank = int(np.sum(s > tol * s[0])) if len(s) else 0
    cond = float(s[0] / s[rank - 1]) if rank else np.inf
    return rel, rank, cond, coeffs


def run():
    print("E73.014 local action closure probe")
    print(" lam     L   dim  primCols srcCols srcRank  srcCond   relImage  actRank")
    off_nodes = [0.20 + 1j * GAMMAS[0], 0.20 - 1j * GAMMAS[0], 0.20 + 1j * GAMMAS[1]]
    crit_nodes = [1j * g for g in GAMMAS[:5]]
    for lam, n_modes in [(8, 12), (10, 14), (12, 16), (14, 18)]:
        h, mu, idx, d, L = setup_full(lam, n_modes)
        prim, plabels = local_basis(off_nodes, crit_nodes, d, L, powers=[0, 1, 2], poly_powers=[1])
        src, slabels = local_basis(off_nodes, crit_nodes, d, L, powers=[0, 1, 2, 3], poly_powers=[1, 2])
        image = (h - mu * np.eye(h.shape[0])) @ prim
        rel, srank, scond, coeffs = projection_stats(image, src)
        # Induced action rank after projecting image into source coordinates.
        _, svals, _ = svd(coeffs, full_matrices=False)
        arank = int(np.sum(svals > 1e-10 * svals[0])) if len(svals) else 0
        print(
            f"{lam:4.0f} {L:7.3f} {len(idx):5d} {prim.shape[1]:9d} {src.shape[1]:7d} "
            f"{srank:7d} {scond:8.1e} {rel:10.2e} {arank:8d}"
        )


if __name__ == "__main__":
    run()
