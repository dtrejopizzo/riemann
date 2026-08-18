#!/usr/bin/env python3
"""Cell-Gauss audit of the FFT residual Gram at T=log(6)/2.

The old D.203 diagnostic integrated endpoint-logarithmic action columns by
the rectangle rule on the FFT grid.  This script evaluates the same action
on a fine convolution grid but integrates it on a composite Gauss rule.
It measures the finite-compression mismatch against the directed finite
matrix before using the residual.  Still binary64 and non-directed.
"""

from __future__ import annotations

import importlib.util
import os
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss


HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location(
    "d203", HERE / "114_d_203_t6_full_fft_residual_gram.py"
)
d203 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(d203)

T = 0.5 * np.log(6.0)
POINTS = int(os.environ.get("D211_POINTS", str(2**20)))
BOX = float(os.environ.get("D211_BOX", "32"))
CELLS = int(os.environ.get("D211_CELLS", "4000"))
QORDER = int(os.environ.get("D211_QORDER", "4"))
BATCH = int(os.environ.get("D211_BATCH", "12"))
DELTA = float(os.environ.get("D211_DELTA", ".219"))
SAVE = os.environ.get("D211_SAVE", "/tmp/t6_cell_gauss_fft_N200.npz")


def main() -> None:
    frame = np.load("/tmp/t6_direct_primitive_eigs.npz")
    X = frame["Q"] @ frame["V"]
    lam = frame["e"]
    N, width = X.shape
    assert (N, width) == (200, 198)

    # Composite Gauss chart, excluding the singular endpoints themselves.
    nodes, weights = leggauss(QORDER)
    edges = np.linspace(-T, T, CELLS + 1)
    midpoint = (edges[:-1] + edges[1:]) / 2
    half = (edges[1:] - edges[:-1]) / 2
    tq = (midpoint[:, None] + half[:, None] * nodes).reshape(-1)
    wq = (half[:, None] * np.broadcast_to(weights, (CELLS, QORDER))).reshape(-1)
    source_q = d203.synthesize(tq / T, X)
    acted_q = np.empty_like(source_q)

    dx = BOX / POINTS
    grid = (np.arange(POINTS) - POINTS // 2) * dx
    inside = np.flatnonzero(np.abs(grid) <= T)
    frequency = 2 * np.pi * np.fft.rfftfreq(POINTS, d=dx)
    psi_q = d203.digamma_complex(np.array([0.25]))[0].real
    symbol = d203.digamma_complex(0.25 + 0.5j * frequency).real - psi_q
    m0 = np.log(np.pi) - psi_q
    contacts = ((2, np.log(2.0)), (3, np.log(3.0)),
                (4, np.log(2.0)), (5, np.log(5.0)))

    for start in range(0, width, BATCH):
        stop = min(start + BATCH, width)
        full = np.zeros((POINTS, stop - start))
        full[inside] = d203.synthesize(grid[inside] / T, X[:, start:stop])
        image = np.fft.irfft(
            np.fft.rfft(full, axis=0) * symbol[:, None],
            n=POINTS, axis=0,
        )
        image -= m0 * full
        for integer, mangoldt in contacts:
            shift = np.log(float(integer))
            coefficient = mangoldt / np.sqrt(float(integer))
            image[inside] -= coefficient * (
                d203.shifted_columns(full, grid, grid[inside] + shift)
                + d203.shifted_columns(full, grid, grid[inside] - shift)
            )
        acted_q[:, start:stop] = d203.shifted_columns(image, grid, tq)
        print("acted", start, stop, flush=True)

    sw = np.sqrt(wq)[:, None]
    SQ = sw * source_q
    AQ = sw * acted_q
    G = SQ.T @ SQ
    F = SQ.T @ AQ
    A2 = AQ.T @ AQ
    G = (G + G.T) / 2
    F = (F + F.T) / 2
    A2 = (A2 + A2.T) / 2
    mismatch = F - np.diag(lam)
    Hraw = A2 - F.T @ np.linalg.solve(G, F)
    Hraw = (Hraw + Hraw.T) / 2
    he, hv = np.linalg.eigh(Hraw)
    H = (hv * np.maximum(he, 0.0)) @ hv.T
    test = np.diag(lam) - H / DELTA
    te = np.linalg.eigvalsh((test + test.T) / 2)

    print("points/dx/cells/order =", POINTS, dx, CELLS, QORDER)
    print("basis Gram range =", np.linalg.eigvalsh(G)[[0, -1]])
    print("finite mismatch eig range/op =",
          np.linalg.eigvalsh(mismatch)[[0, -1]], np.linalg.norm(mismatch, 2))
    print("residual raw range =", he[[0, -1]])
    print("scalar-gap test min/count =", te[0], int(np.sum(te < 0)))
    np.savez(SAVE, G=G, finite=F, action_gram=A2, mismatch=mismatch,
             Hraw=Hraw, H=H, test_eigenvalues=te, points=np.array(POINTS),
             dx=np.array(dx), cells=np.array(CELLS), order=np.array(QORDER))
    print("saved", SAVE)
    print("DIAGNOSTIC ONLY: FFT interpolation and binary64")


if __name__ == "__main__":
    main()
