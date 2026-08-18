#!/usr/bin/env python3
"""Finite noncommuting audit of the output-defect reduction."""
import numpy as np


def psqrt(a):
    d, u = np.linalg.eigh((a + a.T) / 2)
    return u @ np.diag(np.sqrt(np.maximum(d, 0))) @ u.T


def main():
    rng = np.random.default_rng(170)
    # Reference feature columns, old and boundary.
    X0 = rng.normal(size=(9, 5))
    XE = rng.normal(size=(9, 2))
    R0 = X0.T @ X0
    H = np.linalg.solve(R0, X0.T @ XE)
    XR = XE - X0 @ H
    S = XR.T @ XR
    Rih = np.linalg.inv(psqrt(R0))
    Sih = np.linalg.inv(psqrt(S))
    Xhat = np.column_stack((X0 @ Rih, XR @ Sih))
    assert np.linalg.norm(Xhat.T @ Xhat - np.eye(7)) < 2e-13

    # Scale a generic load so the old and enlarged comparisons contract.
    Y0 = rng.normal(size=(8, 5))
    YE = rng.normal(size=(8, 2))
    A = Y0 @ Rih
    y = (YE - Y0 @ H) @ Sih
    full = np.column_stack((A, y))
    scale = 0.7 / np.linalg.norm(full, 2)
    A *= scale
    y *= scale
    full = np.column_stack((A, y))

    defect = np.eye(7) - full.T @ full
    Din = np.eye(5) - A.T @ A
    Dout = np.eye(8) - A @ A.T
    block = np.block([[Din, -A.T @ y],
                      [-y.T @ A, np.eye(2) - y.T @ y]])
    assert np.linalg.norm(defect - block) < 2e-13

    short_in = (np.eye(2) - y.T @ y
                - y.T @ A @ np.linalg.inv(Din) @ A.T @ y)
    short_out = np.eye(2) - y.T @ np.linalg.inv(Dout) @ y
    assert np.linalg.norm(short_in - short_out) < 2e-13
    assert np.linalg.eigvalsh(short_out).min() > 0

    # Square-root Julia intertwining.
    Dinh = psqrt(Din)
    Douth = psqrt(Dout)
    assert np.linalg.norm(Dinh @ A.T - A.T @ Douth) < 2e-12
    print("minimum enlarged defect =", np.linalg.eigvalsh(defect).min())
    print("minimum output short =", np.linalg.eigvalsh(short_out).min())
    print("D170 output-defect channel reduction: PASS")


if __name__ == "__main__":
    main()
