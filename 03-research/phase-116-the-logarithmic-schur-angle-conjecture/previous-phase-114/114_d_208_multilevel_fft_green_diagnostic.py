#!/usr/bin/env python3
"""Sizing diagnostic for the operator-Green pivot at arbitrary Legendre N.

This recomputes the primitive chart, the complete multiplier action, and
the residual beyond V_N on one large FFT box.  It asks whether the scalar
complement test B-delta^{-1}C*C has become viable after enlarging the finite
core.  Binary64/FFT output is diagnostic only.
"""

from __future__ import annotations

import importlib.util
import os
from pathlib import Path

import numpy as np
import mpmath as mp


HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location(
    "d203", HERE / "114_d_203_t6_full_fft_residual_gram.py"
)
d203 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(d203)

T = 0.5 * np.log(6.0)
N = int(os.environ.get("D208_N", "260"))
POINTS = int(os.environ.get("D208_POINTS", str(2**18)))
BOX = float(os.environ.get("D208_BOX", "32"))
BATCH = int(os.environ.get("D208_BATCH", "12"))
DELTA = float(os.environ.get("D208_DELTA", ".219"))
SAVE = os.environ.get("D208_SAVE", f"/tmp/t6_multilevel_fft_N{N}.npz")


def primitive_frame() -> tuple[np.ndarray, np.ndarray]:
    k = T / 2
    n = np.arange(N)
    mp.mp.dps = 60
    common = np.array([
        float(mp.sqrt(T * (2 * int(j) + 1) / 2)
              * mp.sqrt(2 * mp.pi / k)
              * mp.besseli(int(j) + mp.mpf("0.5"), k))
        for j in n
    ])
    moments = np.vstack((common, common * np.where(n % 2 == 0, 1.0, -1.0)))
    _, singular, vh = np.linalg.svd(moments, full_matrices=True)
    assert singular[-1] > 0
    return vh[2:].T, moments


def shifted(values: np.ndarray, grid: np.ndarray, targets: np.ndarray) -> np.ndarray:
    return d203.shifted_columns(values, grid, targets)


def main() -> None:
    Q, moments = primitive_frame()
    ncols = N - 2
    dx = BOX / POINTS
    grid = (np.arange(POINTS) - POINTS // 2) * dx
    inside = np.flatnonzero(np.abs(grid) <= T)
    xin = grid[inside]
    u = xin / T
    frequency = 2 * np.pi * np.fft.rfftfreq(POINTS, d=dx)
    psi_q = d203.digamma_complex(np.array([0.25]))[0].real
    symbol = d203.digamma_complex(0.25 + 0.5j * frequency).real - psi_q
    m0 = np.log(np.pi) - psi_q
    contacts = ((2, np.log(2.0)), (3, np.log(3.0)),
                (4, np.log(2.0)), (5, np.log(5.0)))

    source = np.empty((len(inside), ncols))
    acted = np.empty_like(source)
    for start in range(0, ncols, BATCH):
        stop = min(start + BATCH, ncols)
        full = np.zeros((POINTS, stop - start))
        full[inside] = d203.synthesize(u, Q[:, start:stop])
        source[:, start:stop] = full[inside]
        transformed = np.fft.rfft(full, axis=0)
        image = np.fft.irfft(transformed * symbol[:, None], n=POINTS, axis=0)
        image -= m0 * full
        for integer, mangoldt in contacts:
            shift = np.log(float(integer))
            weight = mangoldt / np.sqrt(float(integer))
            image[inside] -= weight * (
                shifted(full, grid, xin + shift) + shifted(full, grid, xin - shift)
            )
        acted[:, start:stop] = image[inside]
        print("acted", start, stop, flush=True)

    G = dx * source.T @ source
    F = dx * source.T @ acted
    A2 = dx * acted.T @ acted
    G = (G + G.T) / 2
    F = (F + F.T) / 2
    A2 = (A2 + A2.T) / 2

    # Pass to a chart orthonormal for the measured quadrature Gram.
    L = np.linalg.cholesky(G)
    R = np.linalg.inv(L.T)
    B = R.T @ F @ R
    full_gram = R.T @ A2 @ R
    B = (B + B.T) / 2
    full_gram = (full_gram + full_gram.T) / 2
    Hraw = (full_gram - B @ B)
    Hraw = (Hraw + Hraw.T) / 2
    he, hv = np.linalg.eigh(Hraw)
    H = (hv * np.maximum(he, 0.0)) @ hv.T
    scalar_schur = B - H / DELTA
    se = np.linalg.eigvalsh((scalar_schur + scalar_schur.T) / 2)

    print("N, points, dx =", N, POINTS, dx)
    print("basis Gram range =", np.linalg.eigvalsh(G)[[0, -1]])
    print("finite B range =", np.linalg.eigvalsh(B)[[0, -1]])
    print("raw residual range =", he[[0, -1]])
    print("scalar-gap Schur min/count =", se[0], int(np.sum(se < 0)))
    np.savez(SAVE, N=np.array(N), Q=Q, moments=moments, G=G, B=B,
             full_gram=full_gram, Hraw=Hraw, H=H,
             scalar_schur_eigenvalues=se, points=np.array(POINTS),
             box=np.array(BOX), dx=np.array(dx), delta=np.array(DELTA))
    print("saved", SAVE)
    print("DIAGNOSTIC ONLY: FFT and binary64")


if __name__ == "__main__":
    main()
