#!/usr/bin/env python3
"""Falsification probe for the sufficient inequality R_ar <= 0.

This is not a proof tool.  It builds finite smooth trial spaces, imposes the
two ruling moments, and computes the largest generalized eigenvalue of
R_ar = B_nuc - Q_0.  A stable positive value disproves the proposed
sufficient comparison with the continuous Castelnuovo--Severi kernel.
"""

from __future__ import annotations

import math

import numpy as np


def mangoldt_terms(limit: int) -> list[tuple[int, float]]:
    sieve = np.ones(limit + 1, dtype=bool)
    sieve[:2] = False
    for p in range(2, int(math.isqrt(limit)) + 1):
        if sieve[p]:
            sieve[p * p : limit + 1 : p] = False
    out: list[tuple[int, float]] = []
    for p in np.flatnonzero(sieve):
        q = int(p)
        while q <= limit:
            out.append((q, math.log(int(p)) / math.sqrt(q)))
            if q > limit // int(p):
                break
            q *= int(p)
    return sorted(out)


def smooth_basis(t: np.ndarray, T: float, count: int) -> np.ndarray:
    x = t / T
    window = np.zeros_like(t)
    inside = np.abs(x) < 1
    window[inside] = np.exp(-1.0 / (1.0 - x[inside] ** 2))
    rows = []
    for k in range(count):
        rows.append(window * np.cos(k * math.pi * (t + T) / (2 * T)))
    return np.asarray(rows)


def symmetrize(a: np.ndarray) -> np.ndarray:
    return (a + a.T.conj()) / 2


def nullspace(a: np.ndarray) -> np.ndarray:
    _, singular, vh = np.linalg.svd(a, full_matrices=True)
    rank = int(np.sum(singular > singular[0] * 1e-12))
    return vh[rank:].T


def generalized_eigenvalues(a: np.ndarray, metric: np.ndarray) -> np.ndarray:
    chol = np.linalg.cholesky(metric)
    left_inverse = np.linalg.inv(chol)
    reduced = symmetrize(left_inverse @ a @ left_inverse.T.conj())
    return np.linalg.eigvalsh(reduced)


def digamma_vector(z: np.ndarray) -> np.ndarray:
    """Complex digamma by recurrence to Re(z)>=20 and asymptotics."""
    shifted = z + 24
    inv = 1.0 / shifted
    inv2 = inv * inv
    value = (
        np.log(shifted)
        - 0.5 * inv
        - inv2 / 12
        + inv2**2 / 120
        - inv2**3 / 252
        + inv2**4 / 240
        - 5 * inv2**5 / 660
        + 691 * inv2**6 / 32760
    )
    for k in range(24):
        value -= 1.0 / (z + k)
    return value


def trial(
    T: float, basis_count: int = 30, grid_count: int = 1601, pad_factor: int = 16
) -> None:
    t = np.linspace(-T, T, grid_count)
    dt = t[1] - t[0]
    length = grid_count * dt
    basis = smooth_basis(t, T, basis_count)

    # Trapezoidal endpoints vanish to infinite order for this basis.
    gram = dt * (basis @ basis.T)
    moments = dt * np.vstack(
        (basis @ np.exp(-t / 2), basis @ np.exp(t / 2))
    )
    z = nullspace(moments).astype(float)

    # Finite prime contact.
    k_mat = np.zeros((basis_count, basis_count), dtype=float)
    for n, weight in mangoldt_terms(int(math.exp(2 * T))):
        a = math.log(n)
        shifted_minus = np.asarray(
            [np.interp(t - a, t, row, left=0.0, right=0.0) for row in basis]
        )
        shifted_plus = np.asarray(
            [np.interp(t + a, t, row, left=0.0, right=0.0) for row in basis]
        )
        k_mat += weight * dt * basis @ (shifted_minus + shifted_plus).T
    k_mat = symmetrize(k_mat)

    # Archimedean Fourier multiplier.  With Fhat = dt*FFT(F),
    # d tau/(2 pi) is the reciprocal interval length.
    padded_count = pad_factor * grid_count
    padded = np.zeros((basis_count, padded_count), dtype=float)
    offset = (padded_count - grid_count) // 2
    padded[:, offset : offset + grid_count] = basis
    fhat = dt * np.fft.fft(padded, axis=1)
    tau = 2 * math.pi * np.fft.fftfreq(padded_count, d=dt)
    multiplier = math.log(math.pi) - np.real(digamma_vector(0.25 + 0.5j * tau))
    fourier_length = padded_count * dt
    g_mat = symmetrize((fhat * multiplier) @ fhat.conj().T / fourier_length).real

    # Continuous reference kernel Q_0.
    kernel = np.exp(np.abs(t[:, None] - t[None, :]) / 2)
    q0_mat = symmetrize((dt * dt) * basis @ kernel @ basis.T)

    b_mat = symmetrize(k_mat + g_mat)
    r_mat = symmetrize(b_mat - q0_mat)
    gp = symmetrize(z.T @ gram @ z)
    bp = symmetrize(z.T @ b_mat @ z)
    q0p = symmetrize(z.T @ q0_mat @ z)
    rp = symmetrize(z.T @ r_mat @ z)

    eig_b = generalized_eigenvalues(bp, gp)
    eig_q0 = generalized_eigenvalues(q0p, gp)
    eig_r = generalized_eigenvalues(rp, gp)
    residual = np.linalg.norm(moments @ z)
    print(
        f"T={T:.1f} pad={pad_factor} dim={z.shape[1]} "
        f"moment_residual={residual:.2e} "
        f"max(B)={eig_b[-1]:+.8e} max(Q0)={eig_q0[-1]:+.8e} "
        f"max(R)={eig_r[-1]:+.8e} min(R)={eig_r[0]:+.8e}"
    )


if __name__ == "__main__":
    for factor in (8, 16, 32):
        trial(2.0, pad_factor=factor)
    for support_radius in (3.0, 4.0):
        trial(support_radius, pad_factor=16)
