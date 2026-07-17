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


def masks(labels):
    principal = np.array([lab[0] != "endpoint" for lab in labels], dtype=bool)
    cauchy0_idx = [j for j, lab in enumerate(labels) if lab[0] == "cauchy0"]
    return principal, cauchy0_idx


def solve_in_basis(basis, target):
    coeff, *_ = lstsq(basis, target, rcond=None)
    return coeff


def transfer_matrix(lam, n_modes):
    h, mu, idx, d, L = setup(lam, n_modes)
    off_nodes = [0.20 + 1j * GAMMAS[0], 0.20 - 1j * GAMMAS[0], 0.20 + 1j * GAMMAS[1]]
    crit_nodes = [1j * g for g in GAMMAS[:5]]
    prim, _ = canonical_basis(off_nodes, crit_nodes, d, L, max_power=2, endpoint_powers=[1])
    src_basis, slabels = canonical_basis(off_nodes, crit_nodes, d, L, max_power=3, endpoint_powers=[1, 2])
    principal, cauchy0_idx = masks(slabels)

    image = (h - mu * np.eye(h.shape[0])) @ prim
    bcols = [solve_in_basis(src_basis, image[:, j]) for j in range(image.shape[1])]
    coeff_action = np.column_stack(bcols)
    principal_action = coeff_action[principal, :]

    tcols = []
    for col, j in enumerate(cauchy0_idx):
        source = np.zeros(len(slabels), dtype=complex)
        source[j] = 1.0
        y, *_ = lstsq(principal_action, source[principal], rcond=None)
        resid = source - coeff_action @ y
        tcols.append(resid[cauchy0_idx])
    trans = np.column_stack(tcols)
    return L, trans


def run():
    print("E73.165 canonical delta transfer probe")
    print("T maps original cauchy0/Pi coefficients to canonical delta coefficients.")
    print(" lam     L  erank       op   frob  distI  dist0   idem   herm  svals")
    prev_v = None
    for lam, n_modes in [(8, 12), (10, 14), (12, 16), (14, 18), (16, 20), (20, 24), (24, 28), (32, 36)]:
        L, trans = transfer_matrix(lam, n_modes)
        s = svd(trans, compute_uv=False)
        erank = int(np.sum(s > 1e-3 * s[0])) if len(s) else 0
        op = s[0] if len(s) else 0.0
        frob = norm(trans)
        dist_i = norm(trans - np.eye(trans.shape[0])) / norm(np.eye(trans.shape[0]))
        dist_0 = norm(trans) / np.sqrt(trans.shape[0])
        idem = norm(trans @ trans - trans) / max(norm(trans), 1e-30)
        herm = norm(trans - trans.conj().T) / max(norm(trans), 1e-30)
        # Track leading right singular direction stability.
        _, _, vh = svd(trans, full_matrices=False)
        v0 = vh[0, :]
        align = abs(np.vdot(prev_v, v0)) if prev_v is not None else np.nan
        prev_v = v0
        sval_txt = ",".join(f"{x:.2e}" for x in s[:5])
        print(
            f"{lam:4d} {L:7.3f} {erank:6d} {op:8.2e} {frob:6.2e} "
            f"{dist_i:6.2e} {dist_0:6.2e} {idem:6.1e} {herm:6.1e} "
            f"{sval_txt} align={align:.3f}"
        )


if __name__ == "__main__":
    run()
