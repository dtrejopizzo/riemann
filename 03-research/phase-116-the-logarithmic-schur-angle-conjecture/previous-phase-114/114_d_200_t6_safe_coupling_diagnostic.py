#!/usr/bin/env python3
"""Diagnostic safe-to-complement capacity at T=(log 6)/2.

This computes only a finite band of Legendre rows and uses binary64 contact
centres, so it is not a certificate.  Its purpose is to decide whether the
three-block Feshbach route has enough numerical budget before constructing
directed diagonal action bounds.
"""
import importlib.util
import math
import os
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss, legvander
from flint import arb, arb_mat, ctx


HERE = Path(__file__).resolve().parent
N0 = 200
N1 = int(os.environ.get("D200_N1", "240"))
SLOW = int(os.environ.get("D200_SLOW", "10"))
DPS = int(os.environ.get("D200_DPS", "350"))
ctx.dps = DPS
Tarb = arb(6).log() / 2
T = math.log(6) / 2

frame = np.load("/tmp/t6_direct_primitive_eigs.npz")
Xall = frame["Q"] @ frame["V"]
eigenvalues = frame["e"]
X = Xall[:, SLOW:]

rect_path = os.environ.get("D200_RECT")
if rect_path and Path(rect_path).exists():
    stored = np.load(rect_path)
    Arect = stored["C"]
    print("loaded cached rectangular block", rect_path, flush=True)
else:
    spec = importlib.util.spec_from_file_location(
        "gamma_rect", HERE / "114_d_147_hurwitz_gamma_arb.py"
    )
    gamma_rect = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(gamma_rect)
    G = gamma_rect.exact_gamma_block(N1, DPS, Tarb)
    Grect = np.array([[float(G[i, j].mid()) for j in range(N0)]
                      for i in range(N0, N1)])
    Grad = np.array([[float(G[i, j].rad()) for j in range(N0)]
                     for i in range(N0, N1)])

    order = N1 + 40
    nodes, weights = leggauss(order)
    scales = np.sqrt((2 * np.arange(N1) + 1) / 2)
    Ccontact = np.zeros((N1 - N0, N0))
    for nn, lam in ((2, math.log(2)), (3, math.log(3)),
                    (4, math.log(2)), (5, math.log(5))):
        d = math.log(nn) / T
        midpoint = -d / 2
        half = 1 - d / 2
        u = midpoint + half * nodes
        vx = legvander(u, N1 - 1) * scales
        vy = legvander(u + d, N1 - 1) * scales
        Ccontact -= (lam / math.sqrt(nn)) * half * (
            (vx[:, N0:] * weights[:, None]).T @ vy[:, :N0]
            + (vy[:, N0:] * weights[:, None]).T @ vx[:, :N0]
        )
    Arect = Grect + Ccontact
    save_rect = os.environ.get("D200_RECT_SAVE")
    if save_rect:
        np.savez(save_rect, C=Arect, gamma_radius=Grad,
                 row_start=np.array(N0), row_end=np.array(N1), digits=np.array(DPS))
        print("saved rectangular block", save_rect, flush=True)

residual = Arect @ X
column_energy = np.sum(residual * residual, axis=0)
weighted = column_energy / eigenvalues[SLOW:]
whitened = residual / np.sqrt(eigenvalues[SLOW:])[None, :]
singular_values = np.linalg.svd(whitened, compute_uv=False)
gram = whitened.T @ whitened
print("rows", N0, N1, "slow", SLOW)
print("unweighted residual Frobenius square =", np.sum(column_energy))
print("weighted trace lower-band diagnostic =", np.sum(weighted))
print("weighted operator-norm square lower-band diagnostic =", singular_values[0] ** 2)
print("weighted singular values first =", singular_values[:10])
print("largest weighted columns =", np.sort(weighted)[-10:])
np.savez(
    os.environ.get("D200_SAVE", "/tmp/t6_safe_coupling_band_diagnostic.npz"),
    residual=residual,
    whitened=whitened,
    singular_values=singular_values,
    gram=gram,
    eigenvalues=eigenvalues[SLOW:],
    slow=np.array(SLOW),
    row_start=np.array(N0),
    row_end=np.array(N1),
)
print("DIAGNOSTIC ONLY: finite row band and binary64 contacts")
