#!/usr/bin/env python3
"""Algebraic checks and reproducible diagnostic for D.207."""

from pathlib import Path
import numpy as np


# Exact scalar example: failure of B-delta^-1 C*C cannot be repaired by
# merely renaming the finite coordinates.
B = np.diag([2.0, 3.0, 5.0])
C = np.array([[1.0, 2.0, -1.0], [0.5, -1.0, 2.0]])
delta = 1.0
worst = np.block([[B, C.T], [C, delta * np.eye(2)]])
schur = B - C.T @ C / delta
assert np.sum(np.linalg.eigvalsh(worst) < 0) == np.sum(
    np.linalg.eigvalsh(schur) < 0
)


# Route diagnostic from D.203.  It is deliberately labelled non-directed.
artifact = Path("/tmp/t6_full_fft_residual_gram_20.npz")
if artifact.exists():
    z = np.load(artifact)
    lam = z["eigenvalues"]
    H = z["residual_psd"]
    test = np.diag(lam) - H / 0.219
    eig = np.linalg.eigvalsh((test + test.T) / 2)
    print("T6 scalar-gap diagnostic min =", eig[0])
    print("T6 scalar-gap diagnostic negative count =", int(np.sum(eig < 0)))
    assert eig[0] < -5.0
    assert np.sum(eig < 0) >= 40
else:
    print("FFT artifact absent: exact algebraic audit only")

print("D207 scalar-gap split invariance: PASS")
print("FFT figures, when present, are DIAGNOSTIC ONLY")
