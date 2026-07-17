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


def rank_svd(mat, reltol=1e-6):
    s = svd(mat, compute_uv=False, full_matrices=False)
    if len(s) == 0 or s[0] == 0:
        return 0, s
    return int(np.sum(s > reltol * s[0])), s


def orth_projector(mat, reltol=1e-6):
    u, s, _ = svd(mat, full_matrices=False)
    if len(s) == 0 or s[0] == 0:
        return np.zeros((mat.shape[0], 0), dtype=complex)
    rank = int(np.sum(s > reltol * s[0]))
    return u[:, :rank]


def local_data(lam, n_modes):
    h, mu, idx, d, L = setup(lam, n_modes)
    off_nodes = [0.20 + 1j * GAMMAS[0], 0.20 - 1j * GAMMAS[0], 0.20 + 1j * GAMMAS[1]]
    crit_nodes = [1j * g for g in GAMMAS[:5]]
    prim, _ = canonical_basis(off_nodes, crit_nodes, d, L, max_power=2, endpoint_powers=[1])
    src_basis, labels = canonical_basis(off_nodes, crit_nodes, d, L, max_power=3, endpoint_powers=[1, 2])
    principal = np.array([lab[0] != "endpoint" for lab in labels], dtype=bool)
    cauchy0_rows = [i for i, lab in enumerate(labels) if lab[0] == "cauchy0"]

    image = (h - mu * np.eye(h.shape[0])) @ prim
    coeff_cols = []
    image_rel = []
    for j in range(image.shape[1]):
        coeff, *_ = lstsq(src_basis, image[:, j], rcond=None)
        coeff_cols.append(coeff)
        image_rel.append(norm(image[:, j] - src_basis @ coeff) / max(norm(image[:, j]), 1e-30))
    coeff_action = np.column_stack(coeff_cols)
    m = coeff_action[principal, :]

    c = np.zeros((m.shape[0], len(cauchy0_rows)), dtype=complex)
    principal_indices = np.flatnonzero(principal)
    row_map = {orig: pos for pos, orig in enumerate(principal_indices)}
    for j, orig in enumerate(cauchy0_rows):
        c[row_map[orig], j] = 1.0
    return L, m, c, max(image_rel)


def run():
    print("E73.167 cauchy0/image intersection probe")
    print("C is the 5D cauchy0 coefficient subspace; M is Image(B_principal).")
    print(" lam     L rankM rankC angleInt quotient imageRel  C_to_M  M_to_C  angles")
    for lam, n_modes in [(8, 12), (10, 14), (12, 16), (14, 18), (16, 20), (20, 24), (24, 28), (32, 36)]:
        L, m, c, image_rel = local_data(lam, n_modes)
        rank_m, sm = rank_svd(m, reltol=1e-6)
        rank_c, sc = rank_svd(c, reltol=1e-12)

        qm = orth_projector(m, reltol=1e-6)
        qc = orth_projector(c, reltol=1e-12)
        c_to_m = norm(c - qm @ (qm.conj().T @ c)) / max(norm(c), 1e-30)
        m_to_c = norm(qm - qc @ (qc.conj().T @ qm)) / max(norm(qm), 1e-30)
        gap_svals = svd(qc.conj().T @ qm, compute_uv=False, full_matrices=False)
        angle_inter = int(np.sum(gap_svals > 0.99))
        quotient = rank_c - angle_inter
        gap_txt = ",".join(f"{x:.2e}" for x in gap_svals[:5])
        print(
            f"{lam:4d} {L:7.3f} {rank_m:5d} {rank_c:5d} "
            f"{angle_inter:8d} {quotient:8d} {image_rel:8.1e} "
            f"{c_to_m:7.2e} {m_to_c:7.2e} {gap_txt}"
        )


if __name__ == "__main__":
    run()
