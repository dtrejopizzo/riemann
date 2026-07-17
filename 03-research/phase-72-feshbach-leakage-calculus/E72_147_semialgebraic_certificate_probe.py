#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import cholesky, eigvalsh, norm, solve, svd

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_112_operator_split_probe import (  # noqa: E402
    cumulative_center_matrix,
    lk_matrix,
    sigma_packet,
    weighted_even_matrix,
)
from E72_79_bordered_minor_probe import finite_roots  # noqa: E402


def relative_matrix(c_actual, c_model):
    delta = c_actual - c_model
    chol = cholesky(c_model)
    x = solve(chol, delta)
    rel = solve(chol, x.T).T
    return 0.5 * (rel + rel.T)


def gcoer_margin(c_model, L):
    diag = np.abs(np.diag(c_model))
    off = np.sum(np.abs(c_model), axis=1) - diag
    return float(np.min(diag - off) / L)


def psd_distance_margin(c_actual, c_model):
    rel = relative_matrix(c_actual, c_model)
    eigs = eigvalsh(rel)
    neg = eigs[eigs < 0.0]
    dist2 = float(np.sum(neg * neg))
    return dist2, 1.0 - dist2


def msb_value(L, idx, d, k, bq, c_actual, roots, hcut=8.0):
    mask = (np.abs(d) <= hcut).astype(float)
    w = weighted_even_matrix(idx, mask)
    mass_full = mask * (w.T @ np.ones(w.shape[0], dtype=complex))
    b = bq.T @ mass_full
    lk = lk_matrix(d, k)
    factor = 2.0 / (L * np.sqrt(np.exp(L)))
    max_c = 0.0
    for tau in roots[:6]:
        y = sigma_packet(L, d, tau)
        zpm = factor * (lk @ y)
        cpm = bq.T @ (mask * zpm)
        max_c = max(max_c, norm(cpm))
    return norm(b) * max_c


def rop_value(L, idx, d, k, bq, c_actual, roots, hcut=8.0):
    mask = (np.abs(d) <= hcut).astype(float)
    w = weighted_even_matrix(idx, mask)
    tcent = cumulative_center_matrix(w.shape[0])
    lk = lk_matrix(d, k)
    factor = 2.0 / (L * np.sqrt(np.exp(L)))
    qshort = bq @ solve(c_actual, bq.T)
    rmat = tcent @ w @ (mask[:, None] * qshort) @ (mask[:, None] * (factor * lk))
    max_flux = 0.0
    for tau in roots[:6]:
        y = sigma_packet(L, d, tau)
        max_flux = max(max_flux, norm(rmat @ y))
    return max_flux


def graph_norm(d, bq, c_actual, s=10 + 0.2j):
    a = bq.T @ (s / (s * s - d * d))
    y = solve(c_actual, a)
    g = bq @ y
    total = max(norm(g) ** 2, 1e-30)
    graph = float(np.sum((d * d) * np.abs(g) ** 2) / total)
    return graph / (1.0 + abs(s) ** 2)


def run():
    print("E72.147 finite semialgebraic certificate probe")
    print(" lam   L roots  GCOER/L  PSDdist2  PSDmargin   MSB    ROP    GraphN")
    for lam, n_modes in [(6, 18), (8, 24), (10, 28), (12, 32), (14, 36), (16, 40)]:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        roots = finite_roots(xi, d, hmax=6.0)
        if len(roots) == 0:
            continue
        dist2, margin = psd_distance_margin(c_actual, c_model)
        print(
            f"{lam:4.0f} {L:5.2f} {len(roots):5d} "
            f"{gcoer_margin(c_model,L):8.3f} {dist2:9.3f} {margin:10.3f} "
            f"{msb_value(L,idx,d,k,bq,c_actual,roots):6.3f} "
            f"{rop_value(L,idx,d,k,bq,c_actual,roots):6.3f} "
            f"{graph_norm(d,bq,c_actual):7.3f}"
        )


if __name__ == "__main__":
    run()
