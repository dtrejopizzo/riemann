#!/usr/bin/env python3
"""Compare full-Gram singular directions with source-defined endpoint jets.

The right generalized singular subspace is pulled back from the whitened
safe coordinates to the primitive Legendre chart.  It is then compared,
through principal angles, with the projected Riesz representers of
F^(r)(+/-T).  This is a binary64 structural diagnostic.
"""

from __future__ import annotations

import math
import os

import numpy as np


T = 0.5 * math.log(6.0)


def orth(A: np.ndarray, tolerance: float = 1e-11) -> np.ndarray:
    """Rank-revealing orthonormal basis for the columns of A."""
    if A.shape[1] == 0:
        return A.copy()
    U, singular, _ = np.linalg.svd(A, full_matrices=False)
    scale = singular[0] if len(singular) else 0.0
    rank = int(np.sum(singular > tolerance * scale))
    return U[:, :rank]


def endpoint_jet(order: int, sign: int, nmax: int = 200) -> np.ndarray:
    """Scaled Legendre coefficients of the endpoint derivative functional."""
    n = np.arange(nmax)
    valid = n >= order
    logabs = np.full(nmax, -np.inf)
    nv = n[valid].astype(np.int64)
    # P_n^(r)(1)=(n+r)!/(2^r r! (n-r)!).
    logabs[valid] = (
        np.array([math.lgamma(int(v) + order + 1) for v in nv])
        - order * math.log(2.0)
        - math.lgamma(order + 1)
        - np.array([math.lgamma(int(v) - order + 1) for v in nv])
        - order * math.log(T)
        + 0.5 * np.log((2.0 * nv + 1.0) / (2.0 * T))
    )
    finite = np.isfinite(logabs)
    logabs[finite] -= np.max(logabs[finite])
    out = np.zeros(nmax)
    out[finite] = np.exp(logabs[finite])
    if sign < 0:
        out *= np.where((n + order) % 2 == 0, 1.0, -1.0)
    return out


def main() -> None:
    source = os.environ.get(
        "D204_SOURCE", "/tmp/t6_full_fft_residual_gram_20.npz"
    )
    top = int(os.environ.get("D204_TOP", "42"))
    max_order = int(os.environ.get("D204_MAX_ORDER", "80"))
    save = os.environ.get(
        "D204_SAVE", "/tmp/t6_endpoint_jet_overlap.npz"
    )
    z = np.load(source)
    X = z["X"]
    lam = z["eigenvalues"]
    slow = int(z["slow"])
    gvec = z["generalized_eigenvectors"]
    assert gvec.shape[0] == X.shape[1] - slow

    # M=Lambda^(-1/2) H Lambda^(-1/2).  A right eigenvector z therefore
    # corresponds to the input coefficient Lambda^(-1/2)z.
    safe = X[:, slow:]
    pulled = safe @ (
        gvec[:, :top] / np.sqrt(lam[slow:])[:, None]
    )
    Qsing = orth(pulled, tolerance=1e-12)
    print("singular input subspace rank", Qsing.shape[1])

    orders = []
    ranks = []
    residual_op = []
    residual_frob = []
    minimum_cosine = []
    jet_bases: list[np.ndarray] = []
    for rmax in range(max_order + 1):
        columns = []
        for r in range(rmax + 1):
            for sign in (1, -1):
                raw = endpoint_jet(r, sign)
                # Project to precisely the same safe primitive chart.
                columns.append(safe @ (safe.T @ raw))
        Qjet = orth(np.column_stack(columns), tolerance=1e-11)
        overlap = np.linalg.svd(Qjet.T @ Qsing, compute_uv=False)
        mincos = overlap[-1] if len(overlap) >= Qsing.shape[1] else 0.0
        residual = np.eye(200) - Qjet @ Qjet.T
        miss = residual @ Qsing
        op = np.linalg.norm(miss, ord=2)
        frob = np.linalg.norm(miss, ord="fro")
        orders.append(rmax)
        ranks.append(Qjet.shape[1])
        residual_op.append(op)
        residual_frob.append(frob)
        minimum_cosine.append(mincos)
        if (
            rmax <= 12
            or rmax % 4 == 0
            or op < 0.5
            or Qjet.shape[1] >= Qsing.shape[1]
        ):
            print(
                "rmax", rmax,
                "jet rank", Qjet.shape[1],
                "miss op", op,
                "miss frob", frob,
                "min cosine", mincos,
            )
        jet_bases.append(Qjet)

    residual_op_array = np.array(residual_op)
    for threshold in (0.5, 0.25, 0.1, 0.05, 0.01):
        found = np.flatnonzero(residual_op_array < threshold)
        print(
            "first rmax with miss <", threshold,
            int(found[0]) if len(found) else "none",
        )

    np.savez(
        save,
        source=np.array(source),
        top=np.array(top),
        slow=np.array(slow),
        orders=np.array(orders),
        ranks=np.array(ranks),
        residual_op=residual_op_array,
        residual_frob=np.array(residual_frob),
        minimum_cosine=np.array(minimum_cosine),
        singular_basis=Qsing,
    )
    print("saved", save)
    print("DIAGNOSTIC ONLY: source FFT singular subspace is not directed")


if __name__ == "__main__":
    main()
