#!/usr/bin/env python3
import numpy as np
from numpy.linalg import det, norm, svd


def rank_n_minus_one_matrix(n, seed):
    rng = np.random.default_rng(seed)
    x = rng.normal(size=n) + 1j * rng.normal(size=n)
    x = x / norm(x)
    q = np.eye(n, dtype=complex) - np.outer(x, np.conjugate(x))
    vals = 1.0 + np.arange(n)
    h = q @ np.diag(vals) @ q
    h = (h + h.conj().T) / 2
    return h, x


def rowspace_row(e, rng):
    coeff = rng.normal(size=e.shape[0]) + 1j * rng.normal(size=e.shape[0])
    return coeff @ e


def replace_row(e, i, row):
    out = e.copy()
    out[i, :] = row
    return out


def adjugate_rank_one(e, tol=1e-10):
    # For rank n-1 Hermitian matrices, adj(E) is the product of nonzero
    # eigenvalues times the null projection.
    vals, vecs = np.linalg.eigh(e)
    k = int(np.argmin(np.abs(vals)))
    scale = np.prod([vals[j] for j in range(len(vals)) if j != k])
    x = vecs[:, k]
    adj = scale * np.outer(x, np.conjugate(x))
    residual = norm(e @ adj) + norm(adj @ e)
    if residual > tol * max(1.0, norm(e) * norm(adj)):
        raise RuntimeError("rank-one adjugate residual too large")
    return adj, x, scale


def least_row_residual(row, e, x):
    # Since E is Hermitian with null vector x, the distance of a row to Row(E)
    # is exactly its component along x^*.
    amp = row @ x
    return abs(amp), amp * np.conjugate(x)


def run():
    print("E72.348 CERT-CFIR row-ideal algebra probe")
    print(
        " n  eps      max|detReplace|   ||r adj(E)||    dist(row,RowE)   "
        "||row||"
    )
    for n in [4, 6, 8, 10]:
        e, x = rank_n_minus_one_matrix(n, 100 + n)
        adj, x_adj, _ = adjugate_rank_one(e)
        # Align the phase of x from the adjugate with construction only for stable reporting.
        if abs(np.vdot(x, x_adj)) < 0.9:
            raise RuntimeError("null vector mismatch")
        rng = np.random.default_rng(1000 + n)
        base = rowspace_row(e, rng)
        null_row = np.conjugate(x)
        for eps in [0.0, 1e-12, 1e-9, 1e-6, 1e-3]:
            row = base + eps * null_row
            dets = [abs(det(replace_row(e, i, row))) for i in range(n)]
            max_det = max(dets)
            adj_norm = norm(row @ adj)
            dist, _ = least_row_residual(row, e, x)
            print(
                f"{n:2d} {eps:8.1e} {max_det:16.6e} {adj_norm:14.6e} "
                f"{dist:15.6e} {norm(row):10.6e}"
            )


if __name__ == "__main__":
    run()
