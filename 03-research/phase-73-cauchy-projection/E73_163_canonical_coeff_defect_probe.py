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


def canonical_basis(off_nodes, crit_nodes, d, L, max_power, endpoint_powers):
    cols = []
    labels = []
    for ki, k in enumerate(crit_nodes):
        gamma = (-1j * k).real
        dd = np.array([dd_kernel(-gamma, dm, L) for dm in d], dtype=complex)
        cols.append(dd)
        labels.append(("cauchy0", ki, -1, 0))
        for bi, beta in enumerate(off_nodes):
            denom = np.array([dm * dm + beta * beta for dm in d], dtype=complex)
            for r in range(1, max_power + 1):
                cols.append(dd / (denom ** r))
                labels.append(("rat", ki, bi, r))
        for q in endpoint_powers:
            cols.append((d ** (2 * q)) * dd)
            labels.append(("endpoint", ki, -1, q))
    return np.column_stack(cols), labels


def exact_source_coeffs(b, off_nodes, crit_nodes, labels):
    coeff = np.zeros(len(labels), dtype=complex)
    for j, label in enumerate(labels):
        kind, ki, _, _ = label
        if kind == "cauchy0":
            coeff[j] = pi_kernel(b, crit_nodes[ki], off_nodes)
    return coeff


def source_vector(b, off_nodes, crit_nodes, d, L):
    total = np.zeros_like(d, dtype=complex)
    for k in crit_nodes:
        gamma = (-1j * k).real
        total += pi_kernel(b, k, off_nodes) * np.array(
            [dd_kernel(-gamma, dm, L) for dm in d], dtype=complex
        )
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


def label_masks(labels):
    principal = np.array([lab[0] != "endpoint" for lab in labels], dtype=bool)
    endpoint = ~principal
    cauchy0 = np.array([lab[0] == "cauchy0" for lab in labels], dtype=bool)
    rat = np.array([lab[0] == "rat" for lab in labels], dtype=bool)
    return principal, endpoint, cauchy0, rat


def run_case(lam, n_modes):
    h, mu, idx, d, L, xi = setup_exact(lam, n_modes)
    off_nodes = [0.20 + 1j * GAMMAS[0], 0.20 - 1j * GAMMAS[0], 0.20 + 1j * GAMMAS[1]]
    crit_nodes = [1j * g for g in GAMMAS[:5]]

    prim, _ = canonical_basis(off_nodes, crit_nodes, d, L, max_power=2, endpoint_powers=[1])
    src_basis, slabels = canonical_basis(off_nodes, crit_nodes, d, L, max_power=3, endpoint_powers=[1, 2])
    principal, endpoint, cauchy0, rat = label_masks(slabels)

    image = (h - mu * np.eye(h.shape[0])) @ prim
    bcols = []
    image_rel = []
    for j in range(image.shape[1]):
        coeff, rel = solve_in_basis(src_basis, image[:, j])
        bcols.append(coeff)
        image_rel.append(rel)
    coeff_action = np.column_stack(bcols)

    source_rank, source_cond = effective_rank(src_basis)
    action_rank, action_cond = effective_rank(coeff_action)
    principal_action = coeff_action[principal, :]
    principal_rank, principal_cond = effective_rank(principal_action)

    rows = []
    for b in off_nodes:
        exact_s = exact_source_coeffs(b, off_nodes, crit_nodes, slabels)
        src = source_vector(b, off_nodes, crit_nodes, d, L)
        source_check = norm(src - src_basis @ exact_s) / max(norm(src), 1e-30)

        y, *_ = lstsq(principal_action, exact_s[principal], rcond=None)
        principal_resid = exact_s[principal] - principal_action @ y
        principal_rel = norm(principal_resid) / max(norm(exact_s[principal]), 1e-30)

        full_coeff_resid = exact_s - coeff_action @ y
        coeff_rel = norm(full_coeff_resid) / max(norm(exact_s), 1e-30)
        endpoint_rel = norm(full_coeff_resid[endpoint]) / max(norm(exact_s), 1e-30)
        cauchy0_rel = norm(full_coeff_resid[cauchy0]) / max(norm(exact_s[cauchy0]), 1e-30)
        rat_rel = norm(full_coeff_resid[rat]) / max(norm(exact_s), 1e-30)

        mesh_resid = src - image @ y
        mesh_rel = norm(mesh_resid) / max(norm(src), 1e-30)
        exp_pair = abs(cmath.exp(b.real * L) * np.vdot(xi, mesh_resid))
        rows.append(
            {
                "b": b,
                "sourceCheck": source_check,
                "principalRel": principal_rel,
                "coeffRel": coeff_rel,
                "endpointRel": endpoint_rel,
                "cauchy0Rel": cauchy0_rel,
                "ratRel": rat_rel,
                "meshRel": mesh_rel,
                "expPair": exp_pair,
            }
        )

    return {
        "lam": lam,
        "L": L,
        "dim": len(idx),
        "srcRank": source_rank,
        "srcCond": source_cond,
        "actRank": action_rank,
        "actCond": action_cond,
        "pRank": principal_rank,
        "pCond": principal_cond,
        "imageRel": max(image_rel),
        "rows": rows,
    }


def run():
    print("E73.163 canonical coefficient-defect probe")
    print("Uses one cauchy0 column per critical node; source coefficients are exact Pi entries.")
    print(
        " lam     L   dim sR     sCond aR pR     pCond imageRel "
        "srcChk principal coeffRel endpoint cauchy0      rat   meshRel   expPair"
    )
    for lam, n_modes in [(8, 12), (10, 14), (12, 16), (14, 18), (16, 20)]:
        out = run_case(lam, n_modes)
        for row in out["rows"]:
            print(
                f"{out['lam']:4d} {out['L']:7.3f} {out['dim']:5d} "
                f"{out['srcRank']:2d} {out['srcCond']:9.1e} "
                f"{out['actRank']:2d} {out['pRank']:2d} {out['pCond']:9.1e} "
                f"{out['imageRel']:8.1e} {row['sourceCheck']:7.1e} "
                f"{row['principalRel']:9.1e} {row['coeffRel']:8.1e} "
                f"{row['endpointRel']:8.1e} {row['cauchy0Rel']:8.1e} "
                f"{row['ratRel']:8.1e} {row['meshRel']:9.1e} {row['expPair']:9.1e}"
            )


if __name__ == "__main__":
    run()
