#!/usr/bin/env python3
"""Directed constrained congruence for the T=log(5)/2 low block.

Inputs:
  * the exact Hurwitz--Lerch Gamma block of D.147 (evaluated in-process);
  * the polynomial-exact contact enclosure serialized by D.100;
  * exact Arb Bessel formulas for the two Tate moments.

The two moment equations are eliminated by a two-column graph.  A binary64
Cholesky factor is used only as an invertible rational-decimal congruence;
Arb interval arithmetic and Gershgorin prove the resulting matrix positive.
"""
from __future__ import annotations

import importlib.util
import math
import os
from pathlib import Path

import numpy as np
from flint import arb, arb_mat, ctx

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location(
    "d147", HERE / "114_d_147_hurwitz_gamma_arb.py"
)
d147 = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(d147)

N = int(os.environ.get("D148_N", "170"))
DPS = int(os.environ.get("D148_DPS", "1300"))
ctx.dps = DPS

gamma = d147.exact_gamma_block(N, DPS)
T = arb(5).log() / 2
m0 = arb.pi().log() + arb.const_euler() + arb.pi() / 2 + 3 * arb(2).log()

contact_data = np.load(os.environ.get("D148_CONTACTS", "/tmp/d100_contacts_arb.npz"))
cc = contact_data["C"]
rr = contact_data["R"]
assert cc.shape == (N, N) and rr.shape == (N, N)

A = arb_mat(N, N)
for i in range(N):
    for j in range(N):
        # D.100 versions prior to the serialized-radius patch stored only the
        # native Arb radius.  Half an ulp encloses conversion of the midpoint
        # to binary64 in either version (double-enlargement is harmless).
        round_error = abs(np.spacing(cc[i, j])) / 2 + np.nextafter(0.0, 1.0)
        # nextafter also covers a possible downward binary64 rounding when an
        # older D.100 output serialized the native Arb radius.
        safe_radius = np.nextafter(float(rr[i, j]), np.inf) + round_error
        contact = arb(repr(float(cc[i, j])), repr(float(safe_radius)))
        A[i, j] = gamma[i, j] + contact
        if i == j:
            A[i, j] -= m0


def tate_moment(n: int, sign: int) -> arb:
    """Integral of the normalized Legendre mode against exp(sign*x/2)."""
    k = T / 2
    order = arb(2 * n + 1) / 2
    integ = (2 * arb.pi() / k).sqrt() * k.bessel_i(order)
    if sign < 0 and n % 2:
        integ = -integ
    return (T * arb(2 * n + 1) / 2).sqrt() * integ


gp = [tate_moment(n, 1) for n in range(N)]
gm = [tate_moment(n, -1) for n in range(N)]

# G^t x=0.  Eliminate x_0,x_1 using the first two moment columns.
H = arb_mat([[gp[0], gp[1]], [gm[0], gm[1]]])
R = arb_mat([[gp[j] for j in range(2, N)], [gm[j] for j in range(2, N)]])
M = -(H.inv() * R)
Z = arb_mat(N, N - 2)
for i in range(2):
    for j in range(N - 2):
        Z[i, j] = M[i, j]
for j in range(N - 2):
    Z[j + 2, j] = 1

B = Z.transpose() * A * Z
center = np.array([[float(B[i, j].mid()) for j in range(N - 2)] for i in range(N - 2)])
center = (center + center.T) / 2
evals = np.linalg.eigvalsh(center)
print("directed-block centre eigenvalues first =", evals[:8], flush=True)
assert evals[0] > 0, "centre is not positive; no positive congruence exists"

# Physical (L2-orthonormal) constrained Ritz data, distinct from the graph
# coordinates used for the interval positivity congruence.
Acenter = np.array([[float(A[i, j].mid()) for j in range(N)] for i in range(N)])
Acenter = (Acenter + Acenter.T) / 2
Zcenter = np.array([[float(Z[i, j].mid()) for j in range(N - 2)] for i in range(N)])
Qphys, _ = np.linalg.qr(Zcenter, mode="reduced")
physical = (Qphys.T @ Acenter @ Qphys)
physical = (physical + physical.T) / 2
physical_evals, physical_vecs_graph = np.linalg.eigh(physical)
physical_vecs = Qphys @ physical_vecs_graph
print("physical constrained Ritz values first =", physical_evals[:8], flush=True)
save_path = os.environ.get("D148_SAVE")
if save_path:
    np.savez(save_path, A=Acenter, Z=Zcenter, values=physical_evals,
             vectors=physical_vecs)
    print("saved nested Ritz data to", save_path, flush=True)

# If center=L L^t, P=(L^t)^-1 is upper triangular with nonzero decimal
# diagonal, hence exactly invertible.  The following is therefore a genuine
# congruence, not a floating-point positivity test.
L = np.linalg.cholesky(center)
P0 = np.linalg.inv(L.T)
P = arb_mat([[arb(repr(float(P0[i, j]))) for j in range(N - 2)] for i in range(N - 2)])
C = P.transpose() * B * P

gersh = []
for i in range(N - 2):
    radius = arb(0)
    for j in range(N - 2):
        if i != j:
            radius += abs(C[i, j])
    gersh.append(C[i, i] - radius)

worst = min(gersh, key=lambda x: float(x.lower()))
print("minimum directed Gershgorin margin =", worst, flush=True)
assert all(g > 0 for g in gersh)
print("D148 T=log(5)/2 constrained low block: DIRECTED POSITIVITY PASS")
