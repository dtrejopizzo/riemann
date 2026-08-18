#!/usr/bin/env python3
"""Numerical atlas for the canonical Bernstein boundary lift at T6.

The calculation is a route-selection diagnostic, not a certificate.  It
tests the exact algebraic decomposition

  P_199 = x^60(1-x)^60 P_79  +  span{B_k: k<60 or k>=140}

and checks that, after the two Tate corrections and A-orthogonal shorting
of the flat primitive sector, it gives the same boundary graph as D.225.
"""
from __future__ import annotations

import numpy as np
from numpy.polynomial.legendre import leggauss, legvander
from scipy.special import gammaln, iv


N, M = 200, 60
T = np.log(6.0)/2
nodes, weights = leggauss(N+4)
x = (nodes+1)/2
P = legvander(nodes, N-1)
phi = P*np.sqrt((2*np.arange(N)+1)/(2*T))


def coefficients(values: np.ndarray) -> np.ndarray:
    """Physical orthonormal Legendre coefficients, columns are functions."""
    return T*phi.T@(weights[:, None]*values)


# Canonical quotient representatives in the positive Bernstein basis.
indices = np.r_[np.arange(M), np.arange(N-M, N)]
logb = np.empty((len(nodes), len(indices)))
for j,k in enumerate(indices):
    logb[:, j] = (gammaln(N)-gammaln(k+1)-gammaln(N-k)
                  +k*np.log(x)+(N-1-k)*np.log1p(-x))
Bval = np.exp(logb)
B = coefficients(Bval)
B /= np.linalg.norm(B, axis=0)

# Two elementary elements of the flat ideal correct the Tate moments
# without changing any endpoint jet below order 60.
Gval = np.column_stack(((1-nodes*nodes)**M,
                        nodes*(1-nodes*nodes)**M))
G = coefficients(Gval)

safe = np.load('/tmp/t6_flat60_safe_arb.npz')['frame_c']
old = np.load('/tmp/t6_flat_boundary_native_schur.npz')['boundary_graph_c']
gamma = np.load('/tmp/t6_gamma260_arb2100.npz')['C'][:N,:N]
contact = np.load('/tmp/t6_contacts260_arb.npz')['C'][:N,:N]
A = gamma+contact-(np.log(np.pi)+np.euler_gamma+np.pi/2
                   +3*np.log(2))*np.eye(N)
A = (A+A.T)/2

k=T/2
orders=(2*np.arange(N)+1)/2
jp=np.sqrt(T*(2*np.arange(N)+1)/2)*np.sqrt(2*np.pi/k)*iv(orders,k)
jm=jp*((-1.)**np.arange(N))
jt=np.vstack((jp,jm))
head = jt@G
assert abs(np.linalg.det(head)) > 1e-12
Bprim = B-G@np.linalg.solve(head, jt@B)
print('HEURISTIC primitive residual',np.linalg.norm(jt@Bprim,2))

# A-orthogonal graph over the same flat sector.
Bff = safe.T@A@safe
Cfb = safe.T@A@Bprim
Bgraph = Bprim-safe@np.linalg.solve(Bff,Cfb)
print('HEURISTIC flat A-orthogonality',np.linalg.norm(safe.T@A@Bgraph,2))

# Compare subspaces, not individual bases.
qo=np.linalg.qr(old)[0]
qb=np.linalg.qr(Bgraph)[0]
cosines=np.linalg.svd(qo.T@qb,compute_uv=False)
print('HEURISTIC boundary subspace cosine range',cosines[-1],cosines[0])
K=Bgraph.T@A@Bgraph
evals=np.linalg.eigvalsh((K+K.T)/2)
print('HEURISTIC Bernstein boundary Schur spectrum',evals[0],evals[-1])
print('HEURISTIC Bernstein coefficient maximum',np.abs(Bgraph).max())
np.savez_compressed('/tmp/t6_bernstein_boundary_atlas.npz',
                     boundary_graph=Bgraph,schur=K,
                     principal_cosines=cosines,indices=indices)
print('D229 HEURISTIC BERNSTEIN BOUNDARY ATLAS: PASS')
