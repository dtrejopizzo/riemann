#!/usr/bin/env python3
"""Full FFT residual-Gram diagnostic for the T6 primitive frame.

Unlike D.201, this computes every cross term.  In the orthonormal
finite-chart eigenframe X, if A is the zero-extension chart operator and
B=P_200 A P_200=diag(lambda), then

    H = (A X)^* (A X) - diag(lambda**2)

is the Gram matrix of the coupling from V_200 to its orthogonal
complement.  The generalized safe-tail matrix

    M_ij = H_ij / sqrt(lambda_i lambda_j)

has largest eigenvalue kappa.  This is a binary64 sizing diagnostic, not
a directed certificate.
"""

from __future__ import annotations

import os
from pathlib import Path

import numpy as np


T = 0.5 * np.log(6.0)
HERE = Path(__file__).resolve().parent


def digamma_complex(z: np.ndarray) -> np.ndarray:
    """Complex digamma by recurrence plus a long asymptotic expansion."""
    z = np.asarray(z, dtype=np.complex128)
    w = z + 20.0
    out = (
        np.log(w) - 1.0 / (2.0 * w) - 1.0 / (12.0 * w**2)
        + 1.0 / (120.0 * w**4) - 1.0 / (252.0 * w**6)
        + 1.0 / (240.0 * w**8) - 5.0 / (660.0 * w**10)
        + 691.0 / (32760.0 * w**12)
        - 1.0 / (12.0 * w**14)
    )
    for j in range(20):
        out -= 1.0 / (z + j)
    return out


def synthesize(u: np.ndarray, coeff: np.ndarray) -> np.ndarray:
    """Synthesize orthonormal Legendre columns on [-T,T]."""
    nmax, width = coeff.shape
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


def shifted_columns(
    values: np.ndarray, x: np.ndarray, targets: np.ndarray
) -> np.ndarray:
    """Linear interpolation of all columns at common target points."""
    dx = x[1] - x[0]
    position = (targets - x[0]) / dx
    left = np.floor(position).astype(np.int64)
    frac = position - left
    valid = (left >= 0) & (left + 1 < len(x))
    out = np.zeros((len(targets), values.shape[1]), dtype=np.float64)
    idx = left[valid]
    out[valid] = (
        (1.0 - frac[valid, None]) * values[idx]
        + frac[valid, None] * values[idx + 1]
    )
    return out


def main() -> None:
    points = int(os.environ.get("D203_POINTS", str(2**17)))
    box = float(os.environ.get("D203_BOX", "32"))
    batch = int(os.environ.get("D203_BATCH", "16"))
    slow = int(os.environ.get("D203_SLOW", "2"))
    save = os.environ.get(
        "D203_SAVE", "/tmp/t6_full_fft_residual_gram.npz"
    )

    frame = np.load(os.environ.get(
        "D203_FRAME", "/tmp/t6_direct_primitive_eigs.npz"
    ))
    X = frame["Q"] @ frame["V"]
    lam = np.asarray(frame["e"], dtype=np.float64)
    ncols = X.shape[1]
    assert X.shape[1] == X.shape[0] - 2
    assert len(lam) == ncols
    orth_error = np.linalg.norm(X.T @ X - np.eye(ncols), ord=2)
    print("primitive frame orthogonality error", orth_error, flush=True)

    dx = box / points
    x = (np.arange(points) - points // 2) * dx
    inside = np.flatnonzero(np.abs(x) <= T)
    u = x[inside] / T
    frequency = 2.0 * np.pi * np.fft.rfftfreq(points, d=dx)
    psi_quarter = digamma_complex(np.array([0.25]))[0].real
    symbol = digamma_complex(0.25 + 0.5j * frequency).real - psi_quarter
    m0 = np.log(np.pi) - psi_quarter
    contacts = (
        (2, np.log(2.0)),
        (3, np.log(3.0)),
        (4, np.log(2.0)),
        (5, np.log(5.0)),
    )

    # The chart restriction of both X and A X is retained.  The uniform
    # grid is not an exact Legendre quadrature, so the finite projection is
    # formed with its measured basis Gram rather than silently replacing
    # that Gram by the identity.
    basis_inside = np.empty((len(inside), ncols), dtype=np.float64)
    acted_inside = np.empty((len(inside), ncols), dtype=np.float64)
    xin = x[inside]
    for start in range(0, ncols, batch):
        stop = min(start + batch, ncols)
        functions = np.zeros((points, stop - start), dtype=np.float64)
        functions[inside] = synthesize(u, X[:, start:stop])
        basis_inside[:, start:stop] = functions[inside]
        transformed = np.fft.rfft(functions, axis=0)
        acted = np.fft.irfft(
            transformed * symbol[:, None], n=points, axis=0
        )
        acted -= m0 * functions
        for n, mangoldt in contacts:
            shift = np.log(float(n))
            weight = mangoldt / np.sqrt(float(n))
            acted[inside] -= weight * (
                shifted_columns(functions, x, xin + shift)
                + shifted_columns(functions, x, xin - shift)
            )
        acted_inside[:, start:stop] = acted[inside]
        print("acted columns", start, stop, flush=True)

    basis_gram = dx * (basis_inside.T @ basis_inside)
    basis_gram = 0.5 * (basis_gram + basis_gram.T)
    action_gram = dx * (acted_inside.T @ acted_inside)
    action_gram = 0.5 * (action_gram + action_gram.T)
    finite = dx * (basis_inside.T @ acted_inside)
    finite = 0.5 * (finite + finite.T)
    # This is B^* G^{-1} B.  When G=I and B=diag(lambda), it is exactly
    # the requested Bfinite^2.
    finite_square = finite.T @ np.linalg.solve(basis_gram, finite)
    finite_square = 0.5 * (finite_square + finite_square.T)
    residual_raw = 0.5 * (
        action_gram - finite_square
        + (action_gram - finite_square).T
    )

    # Exact H is PSD.  Clipping negative binary64 eigenvalues separates the
    # algebraic Gram identity from FFT/quadrature and frame errors.
    hval, hvec = np.linalg.eigh(residual_raw)
    residual_psd = (hvec * np.maximum(hval, 0.0)) @ hvec.T
    residual_psd = 0.5 * (residual_psd + residual_psd.T)

    hs = residual_psd[slow:, slow:]
    safe_lam = lam[slow:]
    invsqrt = 1.0 / np.sqrt(safe_lam)
    generalized = hs * invsqrt[:, None] * invsqrt[None, :]
    generalized = 0.5 * (generalized + generalized.T)
    gval, gvec = np.linalg.eigh(generalized)
    order = np.argsort(gval)[::-1]
    gval = gval[order]
    gvec = gvec[:, order]

    print("grid points/inside/dx", points, len(inside), dx)
    print(
        "basis Gram eigenvalue range",
        np.linalg.eigvalsh(basis_gram)[[0, -1]],
    )
    print(
        "FFT finite vs directed diagonal operator norm",
        np.linalg.norm(finite - np.diag(lam), ord=2),
    )
    print("raw H eigenvalue range", hval[0], hval[-1])
    print("raw H negative trace", np.sum(np.minimum(hval, 0.0)))
    print("PSD H trace", np.trace(residual_psd))
    print("slow", slow, "safe minimum lambda", safe_lam[0])
    print("generalized kappa", gval[0])
    print("generalized eigenvalues first 24", gval[:24])
    for promote in (0, 1, 2, 3, 4, 6, 8, 12, 16, 24, 32):
        if promote < len(gval):
            print(
                "promote", promote,
                "remaining generalized spectral value", gval[promote],
            )

    np.savez(
        save,
        X=X,
        eigenvalues=lam,
        basis_gram=basis_gram,
        finite=finite,
        action_gram=action_gram,
        finite_square=finite_square,
        residual_raw=residual_raw,
        residual_raw_eigenvalues=hval,
        residual_psd=residual_psd,
        generalized=generalized,
        generalized_eigenvalues=gval,
        generalized_eigenvectors=gvec,
        slow=np.array(slow),
        points=np.array(points),
        box=np.array(box),
        dx=np.array(dx),
        inside_count=np.array(len(inside)),
        orthogonality_error=np.array(orth_error),
    )
    print("saved", save)
    print("DIAGNOSTIC ONLY: FFT and binary64, no directed sign asserted")


if __name__ == "__main__":
    main()
