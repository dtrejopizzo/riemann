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
    vals, _ = eigh(h_actual)
    d = 2.0 * np.pi * idx / L
    return h_actual, vals[0], idx.astype(int), d, L


def local_basis(off_nodes, crit_nodes, d, L, powers=(), poly_powers=()):
    cols = []
    labels = []
    for ki, k in enumerate(crit_nodes):
        gamma = (-1j * k).real
        dd = np.array([dd_kernel(-gamma, dm, L) for dm in d], dtype=complex)
        for bi, beta in enumerate(off_nodes):
            denom = np.array([dm * dm + beta * beta for dm in d], dtype=complex)
            for r in powers:
                col = dd.copy() if r == 0 else dd / (denom ** r)
                cols.append(col)
                labels.append(("rat", ki, bi, r))
        for q in poly_powers:
            cols.append((d ** (2 * q)) * dd)
            labels.append(("poly", ki, -1, q))
    return np.column_stack(cols), labels


def subbasis(off_nodes, crit_nodes, d, L, max_power=None, poly_powers=()):
    powers = [] if max_power is None else list(range(max_power + 1))
    return local_basis(off_nodes, crit_nodes, d, L, powers=powers, poly_powers=poly_powers)


def project_rel(target, basis, tol=1e-10):
    coeffs, *_ = lstsq(basis, target, rcond=None)
    residual = target - basis @ coeffs
    rel = norm(residual) / max(norm(target), 1e-30)
    s = svd(basis, compute_uv=False, full_matrices=False)
    rank = int(np.sum(s > tol * s[0])) if len(s) else 0
    return rel, rank


def block_columns(labels, kind, value):
    out = []
    for j, lab in enumerate(labels):
        if kind == "rat_r" and lab[0] == "rat" and lab[3] == value:
            out.append(j)
        if kind == "poly_q" and lab[0] == "poly" and lab[3] == value:
            out.append(j)
    return out


def run_case(lam, n_modes):
    h, mu, idx, d, L = setup_full(lam, n_modes)
    off_nodes = [0.20 + 1j * GAMMAS[0], 0.20 - 1j * GAMMAS[0], 0.20 + 1j * GAMMAS[1]]
    crit_nodes = [1j * g for g in GAMMAS[:5]]

    prim, plabels = local_basis(off_nodes, crit_nodes, d, L, powers=[0, 1, 2], poly_powers=[1])
    image = (h - mu * np.eye(h.shape[0])) @ prim

    rows = []
    for r in [0, 1, 2]:
        cols = block_columns(plabels, "rat_r", r)
        target = image[:, cols]
        tight, _ = subbasis(off_nodes, crit_nodes, d, L, max_power=r, poly_powers=[1, 2])
        tri, _ = subbasis(off_nodes, crit_nodes, d, L, max_power=r + 1, poly_powers=[1, 2])
        full, _ = subbasis(off_nodes, crit_nodes, d, L, max_power=3, poly_powers=[1, 2])
        rel_tight, rank_tight = project_rel(target, tight)
        rel_tri, rank_tri = project_rel(target, tri)
        rel_full, rank_full = project_rel(target, full)
        rows.append((f"rat{r}", len(cols), rank_tight, rel_tight, rank_tri, rel_tri, rank_full, rel_full))

    cols = block_columns(plabels, "poly_q", 1)
    target = image[:, cols]
    poly_low, _ = subbasis(off_nodes, crit_nodes, d, L, max_power=2, poly_powers=[1])
    poly_tri, _ = subbasis(off_nodes, crit_nodes, d, L, max_power=3, poly_powers=[1, 2])
    rel_low, rank_low = project_rel(target, poly_low)
    rel_tri, rank_tri = project_rel(target, poly_tri)
    rows.append(("poly1", len(cols), rank_low, rel_low, rank_tri, rel_tri, rank_tri, rel_tri))
    return L, len(idx), rows


def run():
    print("E73.016 triangular local action probe")
    print("For rat r, tight=source orders <=r, tri=source orders <=r+1.")
    print(" lam     L   dim   block cols tightRank   tightRel   triRank     triRel  fullRank    fullRel")
    for lam, n_modes in [(8, 12), (10, 14), (12, 16), (14, 18), (16, 20)]:
        L, dim, rows = run_case(lam, n_modes)
        for name, cols, rt, et, rtri, etri, rf, ef in rows:
            print(
                f"{lam:4d} {L:7.3f} {dim:5d} {name:>7s} {cols:4d} "
                f"{rt:9d} {et:10.2e} {rtri:9d} {etri:10.2e} {rf:9d} {ef:10.2e}"
            )


if __name__ == "__main__":
    run()
