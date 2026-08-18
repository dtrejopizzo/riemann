#!/usr/bin/env python3
"""Directed finite Green capacity on a primitive band 200:N1 at T6.

The old safe space is the 196-column safe frame used by D.219 at N=200.
The trial space is the *orthogonal primitive complement* of V200 inside
V_N1.  Gamma, contacts, Tate equations, orthogonality, all three block
matrices, the band inverse and the final generalized inequality are
evaluated in Arb.  Binary64 chooses frames and frozen congruences only.
"""
from __future__ import annotations

import os
from pathlib import Path

import numpy as np
from flint import arb, arb_mat, ctx


N0 = 200
N1 = int(os.environ.get("D222_N1", "260"))
assert N1 > N0
ND = 2
NS = N0 - 2 - ND
NW = N1 - N0
DPS = int(os.environ.get("D222_DPS", "120"))
RHO = arb(os.environ.get("D222_RHO", ".09"))
ctx.dps = DPS
T = arb(6).log() / 2


def center(X: arb_mat) -> np.ndarray:
    return np.array([[float(X[i, j].mid()) for j in range(X.ncols())]
                     for i in range(X.nrows())])


def tate(n: int, sign: int) -> arb:
    k = T / 2
    value = (2 * arb.pi() / k).sqrt() * k.bessel_i(arb(2*n+1) / 2)
    if sign < 0 and n % 2:
        value = -value
    return (T * arb(2*n+1) / 2).sqrt() * value


def directed_gershgorin(X: arb_mat, name: str) -> list[arb]:
    margins = []
    for i in range(X.nrows()):
        off = sum((abs(X[i, j]) for j in range(X.ncols()) if i != j),
                  arb(0))
        margins.append(X[i, i] - off)
    worst = min(margins, key=lambda z: float(z.lower()))
    print(name, "directed Gershgorin", worst, flush=True)
    assert all(z.lower() > 0 for z in margins)
    return margins


def frozen_whitener(X: arb_mat) -> tuple[arb_mat, np.ndarray]:
    xc = center(X)
    xc = (xc + xc.T) / 2
    L = np.linalg.cholesky(xc)
    P0 = np.linalg.inv(L.T)
    P = arb_mat([[arb(repr(float(P0[i, j])))
                  for j in range(P0.shape[1])]
                 for i in range(P0.shape[0])])
    return P, P0


# Centre data choose the old primitive eigenframe only.
gamma_serial = np.load(os.environ.get(
    "D222_GAMMA_SERIAL", "/tmp/t6_gamma260_arb2100.npz"
))
contact_serial = np.load(os.environ.get(
    "D222_CONTACT_SERIAL", "/tmp/t6_contacts260_arb.npz"
))
Ac = (np.asarray(gamma_serial["C"])[:N0, :N0]
      + np.asarray(contact_serial["C"])[:N0, :N0])
m0 = arb.pi().log() + arb.const_euler() + arb.pi()/2 + 3*arb(2).log()
Ac -= float(m0.mid()) * np.eye(N0)
Ac = (Ac + Ac.T) / 2

gp = [tate(i, 1) for i in range(N1)]
gm = [tate(i, -1) for i in range(N1)]
Jc = np.array([[float(gp[i].mid()) for i in range(N0)],
               [float(gm[i].mid()) for i in range(N0)]])
_, _, vh = np.linalg.svd(Jc, full_matrices=True)
Q0 = vh[2:].T
evals, vecs = np.linalg.eigh(Q0.T @ Ac @ Q0)
Xc = Q0 @ vecs
print("old primitive centre eigenvalues", evals[:8], flush=True)

# Reimpose both Tate equations in Arb.  The first two columns are delicate;
# the remaining 196 columns are exactly the D.219 safe space.
head = arb_mat([[gp[0], gp[1]], [gm[0], gm[1]]])
X = arb_mat(N0, N0 - 2)
for col in range(N0 - 2):
    tail = [arb(repr(float(Xc[i, col]))) for i in range(2, N0)]
    rhs = arb_mat([
        [-sum((gp[i]*tail[i-2] for i in range(2, N0)), arb(0))],
        [-sum((gm[i]*tail[i-2] for i in range(2, N0)), arb(0))],
    ])
    solved = head.solve(rhs)
    X[0, col], X[1, col] = solved[0, 0], solved[1, 0]
    for i in range(2, N0):
        X[i, col] = tail[i-2]
assert (arb_mat([gp[:N0], gm[:N0]])*X).contains(
    arb_mat(2, N0-2)
)
S = arb_mat([[X[i, j] for j in range(ND, N0-2)]
             for i in range(N0)])

# Orthogonal primitive complement of V200 in V260.  The low component of
# each high Legendre vector is in span(gp_low,gm_low), the orthogonal
# complement of ker(M_low).  The 2x2 Gram solve imposes the global Tate
# equations without introducing an oblique low-space component.
tate_gram = arb_mat([
    [sum((gp[i]*gp[i] for i in range(N0)), arb(0)),
     sum((gp[i]*gm[i] for i in range(N0)), arb(0))],
    [sum((gm[i]*gp[i] for i in range(N0)), arb(0)),
     sum((gm[i]*gm[i] for i in range(N0)), arb(0))],
])
W = arb_mat(N1, NW)
for k in range(NW):
    n = N0 + k
    coeff = tate_gram.solve(arb_mat([[-gp[n]], [-gm[n]]]))
    for i in range(N0):
        W[i, k] = gp[i]*coeff[0, 0] + gm[i]*coeff[1, 0]
    W[n, k] = 1
assert (arb_mat([gp, gm])*W).contains(arb_mat(2, NW))
Xpad = arb_mat(N1, N0-2)
for i in range(N0):
    for j in range(N0-2):
        Xpad[i, j] = X[i, j]
orth = Xpad.transpose()*W
assert orth.contains(arb_mat(N0-2, NW))
print("exact Tate and V200-orthogonality: PASS", flush=True)

# Native complete operator on V260.
gamma_native = np.load(os.environ.get(
    "D222_GAMMA_NATIVE", "/tmp/t6_gamma260_native250.npz"
), allow_pickle=False)
contact_native = np.load(os.environ.get(
    "D222_CONTACT_NATIVE", "/tmp/t6_contact260_native_strings.npz"
), allow_pickle=False)
gs = gamma_native["G"]
cs = contact_native["C"]
assert gs.shape[0] >= N1 and cs.shape[0] >= N1
A = arb_mat([[arb(str(gs[i, j])) + arb(str(cs[i, j]))
              for j in range(N1)] for i in range(N1)])
for i in range(N1):
    A[i, i] -= m0
print("native complete V260 operator loaded", flush=True)

Spad = arb_mat(N1, NS)
for i in range(N0):
    for j in range(NS):
        Spad[i, j] = S[i, j]
B = Spad.transpose()*A*Spad
E = W.transpose()*A*W
C = Spad.transpose()*A*W
print("native finite Green blocks assembled", flush=True)

# Certify both positive diagonal blocks and the sharp finite capacity
# C E^{-1} C^* <= RHO B by frozen directed congruences.
PB, PB0 = frozen_whitener(B)
PE, PE0 = frozen_whitener(E)
QB = PB.transpose()*B*PB
QE = PE.transpose()*E*PE
directed_gershgorin(QB, "old-safe block")
directed_gershgorin(QE, "orthogonal band block")
CW = PB.transpose()*C*PE
capacity_schur = RHO*QB - CW*QE.inv()*CW.transpose()
capacity_schur = (capacity_schur + capacity_schur.transpose())/2
PS, PS0 = frozen_whitener(capacity_schur)
Qcap = PS.transpose()*capacity_schur*PS
margins = directed_gershgorin(Qcap, "rho-finite capacity")

# Exact Galerkin-corrected source.  Its A-image is orthogonal to W and its
# remaining projection to Z is precisely the residual R_W of D.210.
green_coeff = E.inv()*C.transpose()
Fcorr = Spad - W*green_coeff
assert (W.transpose()*A*Fcorr).contains(arb_mat(NW, NS))
fc = center(Fcorr)
fr = np.array([[float(Fcorr[i, j].rad()) for j in range(NS)]
               for i in range(N1)])
fr = np.nextafter(fr + np.abs(np.spacing(fc))/2, np.inf)
bc = center(B)
br = np.array([[float(B[i, j].rad()) for j in range(NS)]
               for i in range(NS)])
br = np.nextafter(br + np.abs(np.spacing(bc))/2, np.inf)
print("exact finite-Green corrected source: PASS", flush=True)

save = os.environ.get(
    "D222_SAVE", "/tmp/t6_finite_green_capacity_rho009_arb.npz"
)
np.savez_compressed(
    save,
    rho=np.array(float(RHO.mid())),
    old_eigenvalues=evals,
    old_whitener=PB0,
    band_whitener=PE0,
    schur_whitener=PS0,
    safe_source_c=center(Spad),
    corrected_source_c=fc,
    corrected_source_r=fr,
    old_safe_block_c=bc,
    old_safe_block_r=br,
    capacity_gersh_lower=np.array([float(z.lower()) for z in margins]),
    old_safe_dimension=np.array(NS),
    band_dimension=np.array(NW),
    old_cutoff=np.array(N0), new_cutoff=np.array(N1),
    digits=np.array(DPS),
)
print("saved", save, flush=True)
print("D222 DIRECTED FINITE GREEN CAPACITY rho<=0.09: PASS", flush=True)
