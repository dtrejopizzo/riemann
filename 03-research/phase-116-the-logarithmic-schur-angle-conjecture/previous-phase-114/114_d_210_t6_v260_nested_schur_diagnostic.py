#!/usr/bin/env python3
"""Assemble the V260 centre and inspect the exact-Tate nested Schur split.

Gamma/contact inputs are directed files, but this script uses their centres
for choosing frames and sizing the nested certificate.  It is therefore a
diagnostic and writes a V260 primitive eigenframe for the subsequent full
residual computation.
"""
from __future__ import annotations

import os
import numpy as np
from flint import arb, ctx


ctx.dps = 180
N0, N1 = 200, 260
T = arb(6).log() / 2


def tate(n: int, sign: int) -> float:
    k = T / 2
    val = (2 * arb.pi() / k).sqrt() * k.bessel_i(arb(2*n+1)/2)
    if sign < 0 and n % 2:
        val = -val
    val *= (T * arb(2*n+1) / 2).sqrt()
    return float(val.mid())


g = np.load(os.environ.get("D210_GAMMA", "/tmp/t6_gamma260_arb2100.npz"))
c = np.load(os.environ.get("D210_CONTACT", "/tmp/t6_contacts260_arb.npz"))
G, C = np.asarray(g["C"]), np.asarray(c["C"])
assert G.shape == C.shape == (N1, N1)
m0 = float((arb.pi().log() + arb.const_euler() + arb.pi()/2
            + 3*arb(2).log()).mid())
A = (G + C - m0*np.eye(N1))
A = (A + A.T)/2

gp = np.array([tate(n, 1) for n in range(N1)])
gm = np.array([tate(n, -1) for n in range(N1)])
J = np.vstack((gp, gm))
_, _, vh = np.linalg.svd(J, full_matrices=True)
Q = vh[2:].T
evals, V = np.linalg.eigh(Q.T @ A @ Q)
X = Q @ V
print("V260 primitive eigenvalues first/last", evals[:8], evals[-1])

# Source-defined nested coordinates: the already primitive V200 plus each
# new high Legendre mode corrected only in coordinates 0,1 to satisfy Tate.
old = np.load("/tmp/t6_direct_primitive_eigs.npz")
X0 = old["Q"] @ old["V"]
Xpad = np.vstack((X0, np.zeros((N1-N0, X0.shape[1]))))
Y = np.zeros((N1, N1-N0))
head = J[:, :2]
for k in range(N1-N0):
    Y[N0+k, k] = 1
    Y[:2, k] = np.linalg.solve(head, -J[:, N0+k])
assert np.linalg.norm(J @ Xpad, ord=2) < 1e-11
assert np.linalg.norm(J @ Y, ord=2) < 1e-11

A00 = Xpad.T @ A @ Xpad
A01 = Xpad.T @ A @ Y
A11 = Y.T @ A @ Y
G11 = Y.T @ Y
high_eval = np.linalg.eigvalsh(
    np.linalg.solve(np.linalg.cholesky(G11), A11)
    @ np.linalg.inv(np.linalg.cholesky(G11).T)
)
K0 = A00 - A01 @ np.linalg.solve(A11, A01.T)
K0 = (K0 + K0.T)/2
ke = np.linalg.eigvalsh(K0)
print("high generalized range", high_eval[[0, -1]])
print("nested Schur on V200 minimum/count negative", ke[0], int(np.sum(ke < 0)))

np.savez(
    os.environ.get("D210_SAVE", "/tmp/t6_v260_nested_diagnostic.npz"),
    A=A, Q=Q, V=V, e=evals, X=X, Y=Y,
    A00=A00, A01=A01, A11=A11, high_gram=G11,
    nested_schur=K0, nested_eigenvalues=ke,
)
# Compatibility frame for D203.
np.savez("/tmp/t6_direct_primitive_eigs260.npz", Q=Q, V=V, e=evals)
print("D210 V260 NESTED SCHUR: DIAGNOSTIC ONLY")
