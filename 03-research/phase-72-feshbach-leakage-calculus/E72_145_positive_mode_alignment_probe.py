#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import cholesky, eigh, norm, solve

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_112_operator_split_probe import weighted_even_matrix  # noqa: E402


def relative_matrix(c_actual, c_model):
    delta = c_actual - c_model
    chol = cholesky(c_model)
    x = solve(chol, delta)
    rel = solve(chol, x.T).T
    return 0.5 * (rel + rel.T), chol


def whiten_candidate(chol, c):
    w = chol.T @ c
    n = norm(w)
    if n < 1e-14:
        return None
    return w / n


def candidate_vectors(idx, d, bq):
    mask = (np.abs(d) <= 8.0).astype(float)
    w_even = weighted_even_matrix(idx, mask)
    rows = []
    names = []
    base = w_even.T @ np.ones(w_even.shape[0])
    rows.append(mask * base)
    names.append("mass")
    for power in [2, 4, 6]:
        rows.append(mask * (d ** power) * base)
        names.append(f"d{power}")
    edge = np.zeros_like(d)
    active = np.where(mask > 0)[0]
    if len(active):
        edge[active[0]] = 1.0
        edge[active[-1]] = 1.0
    rows.append(edge)
    names.append("edge")
    center = np.zeros_like(d)
    center[np.argmin(np.abs(d))] = 1.0
    rows.append(center)
    names.append("center")
    return names, [bq.T @ row for row in rows]


def run():
    print("E72.145 positive mode alignment probe")
    print(" lam   L  topEig   mode  bestCand  bestCorr  mass  d2  d4  d6  edge center")
    for lam, n_modes in [(8, 24), (10, 28), (12, 32), (14, 36), (16, 40), (18, 44)]:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        rel, chol = relative_matrix(c_actual, c_model)
        eigs, vecs = eigh(rel)
        names, cands = candidate_vectors(idx, d, bq)
        wcands = [whiten_candidate(chol, c) for c in cands]
        order = np.argsort(eigs)[::-1]
        for rank, j in enumerate(order[:3], start=1):
            u = vecs[:, j]
            corrs = []
            for wc in wcands:
                corrs.append(0.0 if wc is None else abs(np.vdot(u, wc)))
            best = int(np.argmax(corrs))
            print(
                f"{lam:4.0f} {L:5.2f} {eigs[j]:7.3f} {rank:6d} "
                f"{names[best]:>8s} {corrs[best]:9.3f} "
                + " ".join(f"{c:5.2f}" for c in corrs)
            )


if __name__ == "__main__":
    run()
