#!/usr/bin/env python3
import cmath
import sys

import numpy as np
from numpy.linalg import eigh, lstsq, norm, svd

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E71_9_relative_arch_background_probe import build  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_003_critical_source_probe import dd_kernel, pi_kernel  # noqa: E402


def setup_exact(lam, n_modes):
    h_actual, idx, L = build(lam, n_modes, include_arith=True)
    vals, vecs = eigh(h_actual)
    xi = vecs[:, 0]
    phase = np.sign(np.real(np.vdot(xi, np.ones_like(xi))))
    if phase == 0:
        phase = 1.0
    xi = phase * xi / norm(xi)
    d = 2.0 * np.pi * idx / L
    return h_actual, vals[0], idx.astype(int), d, L, xi


def local_basis(off_nodes, crit_nodes, d, L, powers, poly_powers):
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


def source_vector(b, off_nodes, crit_nodes, d, L):
    total = np.zeros_like(d, dtype=complex)
    for k in crit_nodes:
        gamma = (-1j * k).real
        coeff = pi_kernel(b, k, off_nodes)
        total += coeff * np.array([dd_kernel(-gamma, dm, L) for dm in d], dtype=complex)
    return total


def effective_rank(mat, tol=1e-10):
    s = svd(mat, compute_uv=False, full_matrices=False)
    rank = int(np.sum(s > tol * s[0])) if len(s) else 0
    cond = float(s[0] / s[rank - 1]) if rank else np.inf
    return rank, cond


def solve_in_basis(basis, target):
    coeff, *_ = lstsq(basis, target, rcond=None)
    resid = target - basis @ coeff
    rel = norm(resid) / max(norm(target), 1e-30)
    return coeff, rel


def run_case(lam, n_modes):
    h, mu, idx, d, L, xi = setup_exact(lam, n_modes)
    off_nodes = [0.20 + 1j * GAMMAS[0], 0.20 - 1j * GAMMAS[0], 0.20 + 1j * GAMMAS[1]]
    crit_nodes = [1j * g for g in GAMMAS[:5]]

    prim, _ = local_basis(off_nodes, crit_nodes, d, L, powers=[0, 1, 2], poly_powers=[1])
    source_basis, _ = local_basis(off_nodes, crit_nodes, d, L, powers=[0, 1, 2, 3], poly_powers=[1, 2])

    image = (h - mu * np.eye(h.shape[0])) @ prim
    bcols = []
    image_rel = []
    for j in range(image.shape[1]):
        coeff, rel = solve_in_basis(source_basis, image[:, j])
        bcols.append(coeff)
        image_rel.append(rel)
    coeff_action = np.column_stack(bcols)

    brank, bcond = effective_rank(coeff_action)
    srank, scond = effective_rank(source_basis)

    rows = []
    for b in off_nodes:
        src = source_vector(b, off_nodes, crit_nodes, d, L)
        scoeff, src_coord_rel = solve_in_basis(source_basis, src)
        y, *_ = lstsq(coeff_action, scoeff, rcond=None)
        coeff_resid = scoeff - coeff_action @ y
        coeff_rel = norm(coeff_resid) / max(norm(scoeff), 1e-30)
        mesh_resid = src - image @ y
        mesh_rel = norm(mesh_resid) / max(norm(src), 1e-30)
        exp_pair = abs(cmath.exp(b.real * L) * np.vdot(xi, mesh_resid))
        rows.append(
            {
                "b": b,
                "srcCoordRel": src_coord_rel,
                "coeffRel": coeff_rel,
                "meshRel": mesh_rel,
                "expPair": exp_pair,
            }
        )
    return {
        "lam": lam,
        "L": L,
        "dim": len(idx),
        "sourceRank": srank,
        "sourceCond": scond,
        "actionRank": brank,
        "actionCond": bcond,
        "imageRelMax": max(image_rel),
        "rows": rows,
    }


def run():
    print("E73.162 coefficient-defect smoke test")
    print("Builds coefficient action B_L by expressing (H-mu)P in the fixed rational source basis.")
    print("This is a numerical coordinate test, not the symbolic partial-fraction proof.")
    print(
        " lam     L   dim sRank     sCond aRank     aCond imageRel "
        "      bRe srcCoord   coeffRel    meshRel    expPair"
    )
    for lam, n_modes in [(8, 12), (10, 14), (12, 16), (14, 18), (16, 20)]:
        out = run_case(lam, n_modes)
        for row in out["rows"]:
            print(
                f"{out['lam']:4d} {out['L']:7.3f} {out['dim']:5d} "
                f"{out['sourceRank']:5d} {out['sourceCond']:9.1e} "
                f"{out['actionRank']:5d} {out['actionCond']:9.1e} "
                f"{out['imageRelMax']:8.1e} {row['b'].real:8.3f} "
                f"{row['srcCoordRel']:8.1e} {row['coeffRel']:10.1e} "
                f"{row['meshRel']:10.1e} {row['expPair']:10.1e}"
            )


if __name__ == "__main__":
    run()
