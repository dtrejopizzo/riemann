#!/usr/bin/env python3
"""Exact-quadrature contact tail on the endpoint-flat promoted safe frame.

All integrations are polynomial Gauss-Legendre integrations at binary64
centres.  Hence this sizes the finite-contact tail but is not an interval
certificate.  The source frame is B-orthonormal and removes the leading
generalized band singular directions.
"""

from __future__ import annotations

import math
import os

import numpy as np
from numpy.polynomial.legendre import leggauss, legvander


T = 0.5 * math.log(6.0)


def contact_rows(n0: int, n1: int) -> np.ndarray:
    """Rows n0:n1 of the complete 2,3,4,5 contact operator."""
    # Products have degree at most (n1-1)+199, so this order is exact.
    order = (n1 + 200 + 1) // 2 + 2
    nodes, weights = leggauss(order)
    scales = np.sqrt((2 * np.arange(n1) + 1) / 2)
    C = np.zeros((n1 - n0, 200))
    for nn, mangoldt in (
        (2, math.log(2.0)),
        (3, math.log(3.0)),
        (4, math.log(2.0)),
        (5, math.log(5.0)),
    ):
        d = math.log(nn) / T
        midpoint = -d / 2
        half = 1 - d / 2
        u = midpoint + half * nodes
        vx = legvander(u, n1 - 1) * scales
        vy = legvander(u + d, n1 - 1) * scales
        C -= (mangoldt / math.sqrt(nn)) * half * (
            (vx[:, n0:] * weights[:, None]).T @ vy[:, :200]
            + (vy[:, n0:] * weights[:, None]).T @ vx[:, :200]
        )
    return C


def promoted_safe(promote: int) -> np.ndarray:
    frame = np.load("/tmp/t6_direct_primitive_eigs.npz")
    X = frame["Q"] @ frame["V"]
    band = np.load("/tmp/t6_flatM20_safe_band230_rank40.npz")
    Y = band["Y"]
    B = band["energy"]
    L = np.linalg.cholesky(B)
    right = band["right"]
    # weighted = residual inv(L^T), so the input synthesis is
    # X_safe Y inv(L^T) right.
    return (
        X[:, int(band["slow"]):]
        @ Y
        @ np.linalg.inv(L.T)
        @ right[:, promote:]
    )


def main() -> None:
    n0 = int(os.environ.get("D206_N0", "260"))
    n1 = int(os.environ.get("D206_N1", "600"))
    promote = int(os.environ.get("D206_PROMOTE", "2"))
    save = os.environ.get(
        "D206_SAVE", f"/tmp/t6_contact_tail_{n0}_{n1}.npz"
    )
    S = promoted_safe(promote)
    gram_error = np.linalg.norm(S.T @ S - S.T @ S, ord=2)
    rows = contact_rows(n0, n1) @ S
    singular = np.linalg.svd(rows, compute_uv=False)
    gram = rows.T @ rows
    print("rows", n0, n1, "promote", promote, "safe dim", S.shape[1])
    print("contact tail operator norm square", singular[0] ** 2)
    print("contact tail trace", np.sum(singular * singular))
    print("first singular squares", singular[:20] ** 2)
    np.savez(
        save,
        rows=rows,
        gram=gram,
        singular_values=singular,
        source=S,
        n0=np.array(n0),
        n1=np.array(n1),
        promote=np.array(promote),
        gram_error=np.array(gram_error),
    )
    print("saved", save)
    print("DIAGNOSTIC ONLY: exact polynomial order, binary64 centres")


if __name__ == "__main__":
    main()
