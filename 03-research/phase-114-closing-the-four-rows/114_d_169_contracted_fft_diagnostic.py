#!/usr/bin/env python3
"""Stable *diagnostic* for the contracted Q_200 A X coupling at log(5)/2.

This deliberately applies the full multiplier to the five already-contracted
columns before taking high Legendre coefficients.  It avoids the catastrophic
high/low cancellation in the raw Hurwitz--Lerch matrix.  FFT discretisation and
periodisation are not directed, so this file is not a positivity certificate.
Its purpose is to size the rigorous bounds still required.
"""

from __future__ import annotations

import os
from pathlib import Path

import numpy as np


T = 0.5 * np.log(5.0)
HERE = Path(__file__).resolve().parent


def digamma_complex(z: np.ndarray) -> np.ndarray:
    """Double-precision digamma by recurrence to Re(z)>=20 and asymptotics."""
    z = np.asarray(z, dtype=np.complex128)
    w = z + 20.0
    out = (
        np.log(w)
        - 1.0 / (2.0 * w)
        - 1.0 / (12.0 * w**2)
        + 1.0 / (120.0 * w**4)
        - 1.0 / (252.0 * w**6)
        + 1.0 / (240.0 * w**8)
        - 5.0 / (660.0 * w**10)
        + 691.0 / (32760.0 * w**12)
    )
    for j in range(20):
        out -= 1.0 / (z + j)
    return out


def legendre_synthesis(u: np.ndarray, coeff: np.ndarray) -> np.ndarray:
    nmax, width = coeff.shape
    answer = np.sqrt(1.0 / (2.0 * T)) * coeff[0][None, :] * np.ones((len(u), 1))
    if nmax == 1:
        return answer
    p0 = np.ones_like(u)
    p1 = u.copy()
    answer += np.sqrt(3.0 / (2.0 * T)) * p1[:, None] * coeff[1]
    for n in range(2, nmax):
        p = ((2 * n - 1) * u * p1 - (n - 1) * p0) / n
        answer += np.sqrt((2 * n + 1) / (2.0 * T)) * p[:, None] * coeff[n]
        p0, p1 = p1, p
    return answer


def run(box: float, points: int, high: int) -> tuple[np.ndarray, np.ndarray]:
    dx = box / points
    x = (np.arange(points) - points // 2) * dx
    inside = np.flatnonzero(np.abs(x) <= T)
    u = x[inside] / T
    graph = np.load("/tmp/d166_graph_centres.npz")["X"]
    functions = np.zeros((points, graph.shape[1]))
    functions[inside] = legendre_synthesis(u, graph)

    frequency = 2.0 * np.pi * np.fft.fftfreq(points, d=dx)
    psi_quarter = digamma_complex(np.array([0.25]))[0].real
    gamma_symbol = digamma_complex(0.25 + 0.5j * frequency).real - psi_quarter
    acted = np.fft.ifft(
        np.fft.fft(functions, axis=0) * gamma_symbol[:, None], axis=0
    ).real
    acted -= (np.log(np.pi) - psi_quarter) * functions

    # Every active prime power n<5, with Lambda(4)=log(2).
    for n, mangoldt in ((2, np.log(2.0)), (3, np.log(3.0)), (4, np.log(2.0))):
        shift = np.log(float(n))
        weight = mangoldt / np.sqrt(float(n))
        for j in range(graph.shape[1]):
            acted[inside, j] -= weight * (
                np.interp(x[inside] + shift, x, functions[:, j], left=0.0, right=0.0)
                + np.interp(x[inside] - shift, x, functions[:, j], left=0.0, right=0.0)
            )

    rows = []
    p0 = np.ones_like(u)
    p1 = u.copy()
    for n in range(2, high):
        p = ((2 * n - 1) * u * p1 - (n - 1) * p0) / n
        if n >= 200:
            phi = np.sqrt((2 * n + 1) / (2.0 * T)) * p
            rows.append(dx * (phi @ acted[inside]))
        p0, p1 = p1, p
    total_gram = dx * (acted[inside].T @ acted[inside])
    return np.asarray(rows), total_gram


def main() -> None:
    box = float(os.environ.get("D169_BOX", "32"))
    points = int(os.environ.get("D169_POINTS", str(2**18)))
    high = int(os.environ.get("D169_HIGH", "800"))
    rows, total_gram = run(box, points, high)
    np.savez(
        "/tmp/d169_contracted_fft_diagnostic.npz",
        rows=rows,
        total_gram=total_gram,
        box=box,
        points=points,
    )
    print("D169 NON-DIRECTED diagnostic only")
    print("rows:", rows.shape)
    print("column norms:", np.linalg.norm(rows, axis=0))
    print("last-50 norms:", np.linalg.norm(rows[-50:], axis=0))
    print("total acted column norms:", np.sqrt(np.diag(total_gram)))


if __name__ == "__main__":
    main()
