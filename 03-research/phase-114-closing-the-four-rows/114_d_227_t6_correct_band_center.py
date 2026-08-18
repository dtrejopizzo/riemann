#!/usr/bin/env python3
"""Heuristic atlas for the correctly typed V200-perp band at T6.

This script deliberately proves nothing.  It uses binary64 centres only to
measure the exact D.210 decomposition that must later be rebuilt with Arb:
the source is the 196-dimensional safe block of D.219 and the trial band is

    (V400^prim) intersect (V200^prim)^perp.

Unlike the endpoint-flat D.226 band, this band lies in the high block on
which D.185 proves the 0.2199 gap.  The output is a route falsifier and is
always labelled HEURISTIC.
"""
from __future__ import annotations

import os
import numpy as np
from numpy.polynomial.legendre import leggauss, legvander
from flint import arb, ctx


N0, N1 = 200, 400
ctx.dps = 80
T = arb(6).log()/2


def tate(n: int, sign: int) -> float:
    k = T/2
    value = (2*arb.pi()/k).sqrt()*k.bessel_i(arb(2*n+1)/2)
    if sign < 0 and n % 2:
        value = -value
    return float(((T*arb(2*n+1)/2).sqrt()*value).mid())


def primitive_frame(n: int, jp: np.ndarray, jm: np.ndarray) -> np.ndarray:
    _, _, vh = np.linalg.svd(np.vstack((jp[:n], jm[:n])),
                             full_matrices=True)
    return vh[2:].T


def heuristic_contact(nbasis: int) -> np.ndarray:
    """Binary64 Gauss centre, used only when the Arb cache is unfinished."""
    nodes, weights = leggauss(nbasis+4)
    norms = np.sqrt((2*np.arange(nbasis)+1)/2)
    out = np.zeros((nbasis, nbasis))
    for nn, lam in ((2, np.log(2.0)), (3, np.log(3.0)),
                    (4, np.log(2.0)), (5, np.log(5.0))):
        d = np.log(nn)/float(T.mid())
        mid, half = -d/2, 1-d/2
        u = mid+half*nodes
        vx = legvander(u, nbasis-1)*norms
        vy = legvander(u+d, nbasis-1)*norms
        cross = vx.T@((half*weights)[:, None]*vy)
        out -= lam/np.sqrt(nn)*(cross+cross.T)
    return out


gamma_path = os.environ.get("D227_GAMMA", "/tmp/t6_gamma400_arb1000.npz")
contact_path = os.environ.get("D227_CONTACT", "/tmp/t6_contacts400_p1100.npz")
g = np.load(gamma_path, allow_pickle=False)["C"][:N1, :N1]
if os.path.exists(contact_path):
    c = np.load(contact_path, allow_pickle=False)["C"][:N1, :N1]
else:
    print("HEURISTIC binary64 contact fallback")
    c = heuristic_contact(N1)
m0 = float((arb.pi().log()+arb.const_euler()+arb.pi()/2
            +3*arb(2).log()).mid())
A = (g+c-m0*np.eye(N1))
A = (A+A.T)/2

jp = np.array([tate(i, 1) for i in range(N1)])
jm = np.array([tate(i, -1) for i in range(N1)])
X0 = primitive_frame(N0, jp, jm)
X0e = np.zeros((N1, N0-2))
X0e[:N0] = X0

# Reproduce the centre selection of D.219: two delicate eigenvectors and
# the remaining 196 safe eigenvectors.
B0 = X0.T@A[:N0, :N0]@X0
eval0, vec0 = np.linalg.eigh((B0+B0.T)/2)
S = X0e@vec0[:, 2:]
B = S.T@A@S

# The 202 constraints have rank 200: the two Tate rows restrict to the
# two-dimensional L2 complement of primitive V200.  Their common kernel is
# the correctly typed 200-dimensional primitive high band.
H = np.vstack((jp, jm, X0e.T))
_, sh, vh = np.linalg.svd(H, full_matrices=True)
rank = int(np.sum(sh > sh[0]*1e-12))
assert rank == N0
W = vh[rank:].T
assert W.shape == (N1, N1-N0)

print("HEURISTIC constraint residual", np.linalg.norm(H@W, ord=2))
E = W.T@A@W
C = S.T@A@W
eval_e = np.linalg.eigvalsh((E+E.T)/2)
print("HEURISTIC band spectrum", eval_e[0], eval_e[-1])
if eval_e[0] <= 0:
    print("HEURISTIC ROUTE REJECTED: finite high band is not positive")
    raise SystemExit(2)

lb = np.linalg.cholesky((B+B.T)/2)
le = np.linalg.cholesky((E+E.T)/2)
cw = np.linalg.solve(lb, C)
cw = np.linalg.solve(le, cw.T).T
svals = np.linalg.svd(cw, compute_uv=False)
rho = float(svals[0]**2)
print("HEURISTIC correctly typed finite Green capacity", rho)
print("HEURISTIC remaining rho budget to 0.7", 0.7-rho)

green = np.linalg.solve(E, C.T)
Scorr = S-W@green
print("HEURISTIC Galerkin residual in band",
      np.linalg.norm(W.T@A@Scorr, ord=2))
np.savez_compressed(
    os.environ.get("D227_SAVE", "/tmp/t6_correct_band_center.npz"),
    safe_frame=S, band_frame=W, corrected_safe=Scorr,
    safe_block=B, band_block=E, mixed_block=C,
    finite_capacity=np.array(rho), primitive_eigenvalues=eval0,
)
print("D227 HEURISTIC ONLY: PASS")
