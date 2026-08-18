#!/usr/bin/env python3
"""Stable directed certificate for the primitive V_200 block at log(6)/2.

The contact matrix is assembled natively in Arb in this process.  A midpoint
QR is used only to choose a frozen decimal congruence; primitiveness remains
exact because that congruence is applied to the exact Tate graph.  The two
small modes are separated from the 196 safe modes and certified by a
directed 2-by-2 Feshbach bound.
"""
import importlib.util
import os
from pathlib import Path

import numpy as np
from flint import arb, arb_mat, ctx


HERE = Path(__file__).resolve().parent
N = 200
DPS = int(os.environ.get("D190_DPS", "1100"))
ctx.dps = DPS
T = arb(6).log() / 2


def load_script(name, filename):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def legvals(x, nmax):
    values = [arb(1)]
    if nmax == 1:
        return values
    values.append(x)
    for n in range(1, nmax - 1):
        values.append(((2 * n + 1) * x * values[-1] - n * values[-2]) / (n + 1))
    return values


# Native certified Gauss nodes avoid both the old bisection loop and every
# binary serialization.  QG=N+4 integrates all translated products exactly.
qg = N + 4
directed_rule = [arb.legendre_p_root(qg, k, weight=True) for k in range(qg)]
roots = [pair[0] for pair in directed_rule]
weights = [pair[1] for pair in directed_rule]
assert abs(sum(weights, arb(0)) - 2) < arb("1e-200")
contact = arb_mat(N, N)
norms = [(arb(2 * i + 1) / 2).sqrt() for i in range(N)]
for nn, lam in ((2, arb(2).log()), (3, arb(3).log()),
                (4, arb(2).log()), (5, arb(5).log())):
    d = arb(nn).log() / T
    midpoint = -d / 2
    half = 1 - d / 2
    coefficient = lam / arb(nn).sqrt()
    for node, weight in zip(roots, weights):
        u = midpoint + half * node
        vx = legvals(u, N)
        vy = legvals(u + d, N)
        for i in range(N):
            vx[i] *= norms[i]
            vy[i] *= norms[i]
        scale = -coefficient * half * weight
        for i in range(N):
            for j in range(N):
                contact[i, j] += scale * (vx[i] * vy[j] + vy[i] * vx[j])
    print("native contact", nn, "complete", flush=True)

gamma_source = load_script("gamma_native", "114_d_147_hurwitz_gamma_arb.py")
gamma = gamma_source.exact_gamma_block(N, DPS, T)
m0 = arb.pi().log() + arb.const_euler() + arb.pi() / 2 + 3 * arb(2).log()
A = gamma + contact
for i in range(N):
    A[i, i] -= m0


def tate(n, sign):
    k = T / 2
    integ = (2 * arb.pi() / k).sqrt() * k.bessel_i(arb(2 * n + 1) / 2)
    if sign < 0 and n % 2:
        integ = -integ
    return (T * arb(2 * n + 1) / 2).sqrt() * integ


gp = [tate(n, 1) for n in range(N)]
gm = [tate(n, -1) for n in range(N)]
head = arb_mat([[gp[0], gp[1]], [gm[0], gm[1]]])
tail_moments = arb_mat([[gp[j] for j in range(2, N)], [gm[j] for j in range(2, N)]])
Z = arb_mat(N, N - 2)
graph = -(head.inv() * tail_moments)
for i in range(2):
    for j in range(N - 2):
        Z[i, j] = graph[i, j]
for j in range(N - 2):
    Z[j + 2, j] = 1


def centre(M):
    return np.array([[float(M[i, j].mid()) for j in range(M.ncols())] for i in range(M.nrows())])


# Q=Z R^{-1}; R^{-1} is frozen as exact binary64 decimals, while Z remains
# an Arb primitive graph.  This makes Q close to orthonormal without changing
# its exact two-moment kernel property.
zc = centre(Z)
_, rmid = np.linalg.qr(zc, mode="reduced")
pinv = np.linalg.inv(rmid)
P = arb_mat([[arb(repr(float(pinv[i, j]))) for j in range(N - 2)] for i in range(N - 2)])
Q = Z * P
gram = Q.transpose() * Q
gram_c = centre(gram)
print("QR Gram infinity defect =", np.max(np.sum(np.abs(gram_c - np.eye(N - 2)), axis=1)), flush=True)
print("Tate residual radii =", (arb_mat([gp]) * Q).norm(), (arb_mat([gm]) * Q).norm(), flush=True)

B = Q.transpose() * A * Q
bc = centre(B)
bc = (bc + bc.T) / 2
evals, evecs = np.linalg.eigh(bc)
print("physical constrained centre eigenvalues first =", evals[:8], flush=True)
V = arb_mat([[arb(repr(float(evecs[i, j]))) for j in range(N - 2)] for i in range(N - 2)])
C = V.transpose() * B * V


def sub(M, r0, r1, c0, c1):
    return arb_mat([[M[i, j] for j in range(c0, c1)] for i in range(r0, r1)])


slow = 2
Css = sub(C, slow, N - 2, slow, N - 2)
safe_margins = []
for i in range(Css.nrows()):
    safe_margins.append(Css[i, i] - sum((abs(Css[i, j]) for j in range(Css.ncols()) if j != i), arb(0)))
delta = min(safe_margins, key=lambda x: float(x.lower()))
print("safe196 directed Gershgorin gap =", delta, flush=True)
assert delta.lower() > 0

Cll = sub(C, 0, slow, 0, slow)
Cls = sub(C, 0, slow, slow, N - 2)
lower = Cll - (Cls * Cls.transpose()) / delta
lc = centre(lower)
lc = (lc + lc.T) / 2
le, lv = np.linalg.eigh(lc)
W = arb_mat([[arb(repr(float(lv[i, j]))) for j in range(slow)] for i in range(slow)])
directed = W.transpose() * lower * W
margins = [
    directed[i, i] - sum((abs(directed[i, j]) for j in range(slow) if j != i), arb(0))
    for i in range(slow)
]
print("slow2 Feshbach centre eigenvalues =", le, flush=True)
print("slow2 directed Gershgorin margins =", margins, flush=True)
assert all(x.lower() > 0 for x in margins)

np.savez(
    os.environ.get("D190_SAVE", "/tmp/t6_stable_finite_certificate.npz"),
    eigenvalues=evals,
    qr_inverse=pinv,
    eigenvectors=evecs,
    safe_gap=np.array(float(delta.lower())),
    slow_centre=le,
    slow_lower=np.array([float(x.lower()) for x in margins]),
    endpoint=np.array(6),
    digits=np.array(DPS),
)
print("D190 T6 STABLE PRIMITIVE V200 FESHBACH: PASS")
