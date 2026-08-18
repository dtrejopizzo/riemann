#!/usr/bin/env python3
"""Lightweight audit of the directed summary emitted by D.199."""

from pathlib import Path
import sys
import numpy as np


path = Path(sys.argv[1] if len(sys.argv) > 1
            else "/tmp/t6_whitened_native_schur.npz")
z = np.load(path)

e = z["primitive_eigenvalues"]
g = z["safe_gershgorin"]
K = z["schur_center"]
R = z["schur_radius"]
det_c, det_r = z["schur_det"]

assert e.shape == (198,)
assert e[2] > 1.8e-11
assert g.shape == (196,) and np.min(g) > 0.999999999999
assert K.shape == R.shape == (2, 2)
assert K[0, 0] - R[0, 0] > 8.15e-17
assert det_c - det_r > 2.016e-30
assert np.max(R) < 5.0e-112

print("PASS D199 artifact: safe196 and directed delicate Schur are positive")
