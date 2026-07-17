#!/usr/bin/env python3
import sys

import numpy as np
from numpy.linalg import eigh, lstsq, norm, svd

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E71_9_relative_arch_background_probe import build  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_003_critical_source_probe import dd_kernel  # noqa: E402


def setup(lam, n_modes):
    h_actual, idx, L = build(lam, n_modes, include_arith=True)
    vals, _ = eigh(h_actual)
    d = 2.0 * np.pi * idx / L
    return h_actual, vals[0], idx.astype(int), d, L


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


def transfer_matrix(lam, n_modes):
    h, mu, idx, d, L = setup(lam, n_modes)
    off_nodes = [0.20 + 1j * GAMMAS[0], 0.20 - 1j * GAMMAS[0], 0.20 + 1j * GAMMAS[1]]
    crit_nodes = [1j * g for g in GAMMAS[:5]]
    prim, _ = canonical_basis(off_nodes, crit_nodes, d, L, max_power=2, endpoint_powers=[1])
    src_basis, labels = canonical_basis(off_nodes, crit_nodes, d, L, max_power=3, endpoint_powers=[1, 2])
    principal = np.array([lab[0] != "endpoint" for lab in labels], dtype=bool)
    cauchy0_idx = [j for j, lab in enumerate(labels) if lab[0] == "cauchy0"]
    image = (h - mu * np.eye(h.shape[0])) @ prim
    bcols = []
    for j in range(image.shape[1]):
        coeff, *_ = lstsq(src_basis, image[:, j], rcond=None)
        bcols.append(coeff)
    coeff_action = np.column_stack(bcols)
    principal_action = coeff_action[principal, :]
    tcols = []
    for j in cauchy0_idx:
        source = np.zeros(len(labels), dtype=complex)
        source[j] = 1.0
        y, *_ = lstsq(principal_action, source[principal], rcond=None)
        resid = source - coeff_action @ y
        tcols.append(resid[cauchy0_idx])
    return L, np.column_stack(tcols)


def orth(mat):
    q, r = np.linalg.qr(mat)
    keep = np.abs(np.diag(r)) > 1e-12 * max(1.0, np.abs(r[0, 0]))
    return q[:, keep]


def subspace_resid(target_basis, cand_basis):
    qt = orth(target_basis)
    qc = orth(cand_basis)
    resid = qt - qc @ (qc.conj().T @ qt)
    return norm(resid) / max(norm(qt), 1e-30)


def candidate_spaces(gammas, L):
    g = np.array(gammas, dtype=float)
    centered = g - np.mean(g)
    phase = np.angle(np.exp(1j * g * L))
    mesh = np.abs(1.0 - np.exp(1j * g * L))
    cands = {
        "1,g": np.column_stack([np.ones_like(g), g]),
        "1,g2": np.column_stack([np.ones_like(g), g * g]),
        "1,cg": np.column_stack([np.ones_like(g), centered]),
        "1,phase": np.column_stack([np.ones_like(g), phase]),
        "1,mesh": np.column_stack([np.ones_like(g), mesh]),
        "g,g2": np.column_stack([g, g * g]),
        "1,1/g": np.column_stack([np.ones_like(g), 1.0 / g]),
        "1,alt": np.column_stack([np.ones_like(g), (-1.0) ** np.arange(len(g))]),
    }
    return cands


def run():
    print("E73.166 projector moment probe")
    print("Compares Ker(T_L) with simple two-dimensional moment spaces.")
    print(" lam     L    null_svals                 best      resid  prevKer  prevRan    all")
    gammas = GAMMAS[:5]
    prev_null = None
    prev_range = None
    for lam, n_modes in [(8, 12), (10, 14), (12, 16), (14, 18), (16, 20), (20, 24), (24, 28), (32, 36)]:
        L, trans = transfer_matrix(lam, n_modes)
        u, s, vh = svd(trans, full_matrices=False)
        null_basis = vh[-2:, :].conj().T
        range_basis = vh[:3, :].conj().T
        prev_null_resid = subspace_resid(null_basis, prev_null) if prev_null is not None else np.nan
        prev_range_resid = subspace_resid(range_basis, prev_range) if prev_range is not None else np.nan
        prev_null = null_basis
        prev_range = range_basis
        scores = []
        for name, cand in candidate_spaces(gammas, L).items():
            scores.append((subspace_resid(null_basis, cand), name))
        scores.sort()
        all_txt = " ".join(f"{name}:{val:.2e}" for val, name in scores[:4])
        null_txt = ",".join(f"{x:.1e}" for x in s[-2:])
        print(
            f"{lam:4d} {L:7.3f} {null_txt:>22s} {scores[0][1]:>9s} "
            f"{scores[0][0]:9.2e} {prev_null_resid:8.2e} {prev_range_resid:8.2e} {all_txt}"
        )


if __name__ == "__main__":
    run()
