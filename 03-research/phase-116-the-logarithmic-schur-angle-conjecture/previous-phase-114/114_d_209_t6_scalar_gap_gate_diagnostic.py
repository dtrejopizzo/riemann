#!/usr/bin/env python3
"""Audit the corrected scalar-gap Schur gate for the flat-60 split.

This is deliberately a binary64 FFT diagnostic.  It cannot prove a positive
sign, but a stable large negative sign shows that replacing A_QQ^{-1} by
delta^{-1} I is too lossy and therefore cannot close the endpoint route.
"""
from __future__ import annotations

import os
import numpy as np


DELTA = float(os.environ.get("D209_DELTA", ".219"))
residual = np.load(os.environ.get(
    "D209_RESIDUAL", "/tmp/t6_full_fft_residual_gram_20.npz"
))
split = np.load(os.environ.get(
    "D209_SPLIT", "/tmp/t6_flatprimM60_complete200_260_contact260_600.npz"
))

lam = np.asarray(residual["eigenvalues"])
H = np.asarray(residual["residual_psd"])
Y = np.asarray(split["Y"])
assert H.shape == (198, 198) and Y.shape == (198, 78)

# The scalar-gap elimination on the complete finite primitive block is
# split invariant: diag(lambda)-H/delta.  The D/S restrictions below merely
# locate its negative directions for the source-defined flat-60 split.
K = np.diag(lam) - H / DELTA
K = (K + K.T) / 2
Qs = np.linalg.qr(Y)[0]
_, _, vh = np.linalg.svd(Qs.T, full_matrices=True)
Qd = vh[Qs.shape[1]:].T
assert np.linalg.norm(Qs.T @ Qd, ord=2) < 1e-12


def report(name: str, Q: np.ndarray) -> np.ndarray:
    values = np.linalg.eigvalsh((Q.T @ K @ Q + Q.T @ K.T @ Q) / 2)
    print(name, "dimension", Q.shape[1], "minimum", values[0],
          "negative count", int(np.sum(values < 0)))
    return values


all_values = report("primitive", np.eye(198))
d_values = report("D=flat60 orthogonal complement", Qd)
s_values = report("S=flat60 primitive", Qs)
assert all_values[0] < -1
assert d_values[0] < -1

np.savez(
    os.environ.get("D209_SAVE", "/tmp/t6_scalar_gap_gate_diagnostic.npz"),
    primitive_eigenvalues=all_values,
    d_eigenvalues=d_values,
    s_eigenvalues=s_values,
    delta=np.array(DELTA),
    points=np.array(int(residual["points"])),
)
print("D209 RESULT: scalar-gap Schur route REFUTED (diagnostic, not theorem)")
print("Required replacement: directed operator-valued Green A_QQ^{-1}.")
