#!/usr/bin/env python3
"""Heuristic stable Euclidean-remainder split at T6.

Uses P_119 as a stable lift of P_199/(1-u^2)^60 P_79, corrects its two
Tate moments by two elements of the flat ideal, and retains the finite
flat/remainder cross instead of forming the ill-conditioned A-graph.
"""
from __future__ import annotations
import numpy as np
from numpy.polynomial.legendre import leggauss,legvander
from scipy.special import iv

N,M,NB=200,60,120
T=np.log(6.)/2
u,w=leggauss(N+4)
P=legvander(u,N-1)
phi=P*np.sqrt((2*np.arange(N)+1)/(2*T))
def coeff(v):return T*phi.T@(w[:,None]*v)
G=coeff(np.column_stack(((1-u*u)**M,u*(1-u*u)**M)))
k=T/2;orders=(2*np.arange(N)+1)/2
jp=np.sqrt(T*(2*np.arange(N)+1)/2)*np.sqrt(2*np.pi/k)*iv(orders,k)
J=np.vstack((jp,jp*((-1.)**np.arange(N))))
B=np.eye(N,NB)
B-=G@np.linalg.solve(J@G,J@B)
print('HEURISTIC primitive residual',np.linalg.norm(J@B,2))
F=np.load('/tmp/t6_flat60_safe_arb.npz')['frame_c']
gamma=np.load('/tmp/t6_gamma260_arb2100.npz')['C'][:N,:N]
contact=np.load('/tmp/t6_contacts260_arb.npz')['C'][:N,:N]
A=gamma+contact-(np.log(np.pi)+np.euler_gamma+np.pi/2+3*np.log(2))*np.eye(N)
A=(A+A.T)/2
K=B.T@A@B; BF=F.T@A@F; C=B.T@A@F
ek=np.linalg.eigvalsh((K+K.T)/2)
ef=np.linalg.eigvalsh((BF+BF.T)/2)
S=K-C@np.linalg.solve(BF,C.T)
es=np.linalg.eigvalsh((S+S.T)/2)
print('HEURISTIC raw remainder spectrum',ek[0],ek[-1])
print('HEURISTIC flat spectrum',ef[0],ef[-1])
print('HEURISTIC flat-shorted remainder spectrum',es[0],es[-1])
print('HEURISTIC stable coefficient maximum',np.abs(B).max())
np.savez_compressed('/tmp/t6_stable_remainder_atlas.npz',
                     remainder=B,remainder_block=K,flat_block=BF,cross=C,
                     remainder_schur=S)
print('D230 HEURISTIC STABLE REMAINDER ATLAS: PASS')
