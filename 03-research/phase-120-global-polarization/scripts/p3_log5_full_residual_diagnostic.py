#!/usr/bin/env python3
"""Full V_200-to-complement residual diagnostic at T=log(5)/2.

This is a binary64/FFT sizing calculation, not an interval certificate.  It
retains the complete residual Gram

    H = (A X)^*(A X) - (P A X)^*(P A X)

in the physical constrained Ritz frame X.  Its generalized eigenvalues say
how many finite directions must be promoted before the scalar complement gap
delta=0.218 can possibly close the audited three-block gate.
"""

from __future__ import annotations

import os
from pathlib import Path

import numpy as np


T = 0.5 * np.log(5.0)


def digamma_complex(z: np.ndarray) -> np.ndarray:
    z = np.asarray(z, dtype=np.complex128)
    w = z + 20.0
    out = (
        np.log(w) - 1.0 / (2.0 * w) - 1.0 / (12.0 * w**2)
        + 1.0 / (120.0 * w**4) - 1.0 / (252.0 * w**6)
        + 1.0 / (240.0 * w**8) - 5.0 / (660.0 * w**10)
        + 691.0 / (32760.0 * w**12) - 1.0 / (12.0 * w**14)
    )
    for j in range(20):
        out -= 1.0 / (z + j)
    return out


def synthesize(u: np.ndarray, coeff: np.ndarray) -> np.ndarray:
    nmax = coeff.shape[0]
    p0 = np.ones_like(u)
    ans = np.sqrt(1.0 / (2.0 * T)) * p0[:, None] * coeff[0]
    if nmax == 1:
        return ans
    p1 = u.copy()
    ans += np.sqrt(3.0 / (2.0 * T)) * p1[:, None] * coeff[1]
    for n in range(2, nmax):
        p = ((2 * n - 1) * u * p1 - (n - 1) * p0) / n
        ans += np.sqrt((2 * n + 1) / (2.0 * T)) * p[:, None] * coeff[n]
        p0, p1 = p1, p
    return ans


def shifted(values: np.ndarray, x: np.ndarray, target: np.ndarray) -> np.ndarray:
    dx = x[1] - x[0]
    position = (target - x[0]) / dx
    left = np.floor(position).astype(np.int64)
    fraction = position - left
    valid = (left >= 0) & (left + 1 < len(x))
    out = np.zeros((len(target), values.shape[1]))
    index = left[valid]
    out[valid] = (
        (1.0 - fraction[valid, None]) * values[index]
        + fraction[valid, None] * values[index + 1]
    )
    return out


def main() -> None:
    points = int(os.environ.get("P3_LOG5_POINTS", str(2**18)))
    box = float(os.environ.get("P3_LOG5_BOX", "32"))
    batch = int(os.environ.get("P3_LOG5_BATCH", "16"))
    delta = float(os.environ.get("P3_LOG5_DELTA", "0.218"))
    frame_path = Path(os.environ.get("P3_LOG5_FRAME", "/tmp/p3_log5_ritz200.npz"))
    save_path = Path(os.environ.get(
        "P3_LOG5_SAVE", "/tmp/p3_log5_full_residual_diagnostic.npz"
    ))

    frame = np.load(frame_path)
    X = np.asarray(frame["vectors"], dtype=float)
    lam = np.asarray(frame["values"], dtype=float)
    n_modes, n_primitive = X.shape
    assert n_primitive == n_modes - 2 and lam.shape == (n_primitive,)

    dx = box / points
    x = (np.arange(points) - points // 2) * dx
    inside = np.flatnonzero(np.abs(x) <= T)
    xin = x[inside]
    u = xin / T
    frequency = 2.0 * np.pi * np.fft.rfftfreq(points, d=dx)
    psi_quarter = digamma_complex(np.array([0.25]))[0].real
    symbol = digamma_complex(0.25 + 0.5j * frequency).real - psi_quarter
    m0 = np.log(np.pi) - psi_quarter

    basis = np.empty((len(inside), X.shape[1]))
    action = np.empty_like(basis)
    for start in range(0, X.shape[1], batch):
        stop = min(start + batch, X.shape[1])
        functions = np.zeros((points, stop - start))
        functions[inside] = synthesize(u, X[:, start:stop])
        basis[:, start:stop] = functions[inside]
        acted = np.fft.irfft(
            np.fft.rfft(functions, axis=0) * symbol[:, None],
            n=points,
            axis=0,
        )
        acted -= m0 * functions
        for n, mangoldt in ((2, np.log(2.0)), (3, np.log(3.0)), (4, np.log(2.0))):
            shift = np.log(float(n))
            weight = mangoldt / np.sqrt(float(n))
            acted[inside] -= weight * (
                shifted(functions, x, xin + shift)
                + shifted(functions, x, xin - shift)
            )
        action[:, start:stop] = acted[inside]
        print("acted columns", start, stop, flush=True)

    G = dx * basis.T @ basis
    B = dx * basis.T @ action
    J = dx * action.T @ action
    G = 0.5 * (G + G.T)
    B = 0.5 * (B + B.T)
    J = 0.5 * (J + J.T)
    Hraw = J - B.T @ np.linalg.solve(G, B)
    Hraw = 0.5 * (Hraw + Hraw.T)
    hval, hvec = np.linalg.eigh(Hraw)
    H = (hvec * np.maximum(hval, 0.0)) @ hvec.T
    H = 0.5 * (H + H.T)

    invsqrt = 1.0 / np.sqrt(lam)
    generalized = H * invsqrt[:, None] * invsqrt[None, :]
    generalized = 0.5 * (generalized + generalized.T)
    gval, gvec = np.linalg.eigh(generalized)
    order = np.argsort(gval)[::-1]
    gval = gval[order]
    gvec = gvec[:, order]

    print("points/inside/dx", points, len(inside), dx)
    print(
        "frame orthogonality error",
        np.linalg.norm(X.T @ X - np.eye(n_primitive), 2),
    )
    print("grid Gram range", np.linalg.eigvalsh(G)[[0, -1]])
    print("finite action mismatch", np.linalg.norm(B - np.diag(lam), 2))
    print("raw residual eigenvalue range", hval[[0, -1]])
    print("raw negative trace", np.minimum(hval, 0.0).sum())
    print("generalized leading 24", gval[:24])
    print("count above delta", int(np.sum(gval > delta)), "delta", delta)
    if np.any(gval <= delta):
        first_below = int(np.flatnonzero(gval <= delta)[0])
        print("first index below delta", first_below, "value", gval[first_below])

    np.savez(
        save_path,
        residual=H,
        residual_raw=Hraw,
        generalized=generalized,
        generalized_values=gval,
        generalized_vectors=gvec,
        finite=B,
        gram=G,
        ritz_values=lam,
        ritz_vectors=X,
        points=np.array(points),
        dx=np.array(dx),
        delta=np.array(delta),
    )
    print("saved", save_path)
    print("DIAGNOSTIC ONLY: binary64 FFT, no directed sign asserted")


if __name__ == "__main__":
    main()
