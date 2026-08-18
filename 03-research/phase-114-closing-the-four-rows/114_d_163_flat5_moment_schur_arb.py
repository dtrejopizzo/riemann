#!/usr/bin/env python3
"""Ambient-moment projection-mismatch diagnostic for the flat-five frame.

The D.162 matrices are S^* M_r^j S, not S^*(P M_r P)^j S.  They cannot be
used as Feshbach moments for j>=2.  This script is retained only because its
indefinite reconstructed C^* D C is a useful diagnostic of the missing
intermediate projections.  It refuses to run unless explicitly enabled.
"""
import os
import numpy as np
from flint import arb,arb_mat,ctx
if os.environ.get('D163_ALLOW_AMBIENT_DIAGNOSTIC') != '1':
    raise SystemExit(
        'D163 ambient moments are not compressed powers; set '
        'D163_ALLOW_AMBIENT_DIAGNOSTIC=1 only to reproduce the no-go.'
    )
ctx.dps=int(os.environ.get('D163_DPS','160'))
src=np.load(os.environ.get('D163_FRAME','/tmp/d160_flat_arb_columns5_300.npz'))
mom=np.load(os.environ.get('D163_MOMENTS','/tmp/d162_matrix5_R2048_Q64.npz'))
C=np.asarray(src['C']);R=np.asarray(src['R']);K=C.shape[1]

def ball(c,r):
    rr=np.nextafter(float(r),np.inf)+abs(np.spacing(float(c)))/2+np.nextafter(0.,1.)
    return arb(repr(float(c)),repr(float(rr)))

cols=[[ball(C[n,a],R[n,a]) for a in range(K)] for n in range(C.shape[0])]
G=arb_mat([[sum((cols[n][a]*cols[n][b] for n in range(C.shape[0])),arb(0))
            for b in range(K)] for a in range(K)])

# Directed Cholesky: G=L L^t.  The interval L encloses the exact factor.
L=arb_mat(K,K)
for i in range(K):
    for j in range(i+1):
        s=G[i,j]-sum((L[i,k]*L[j,k] for k in range(j)),arb(0))
        L[i,j]=s.sqrt() if i==j else s/L[j,j]
U=L.transpose().inv()

HC=np.asarray(mom['C']);HR=np.asarray(mom['R'])
assert HC.shape==(4,K,K)
H=[]
for p in range(4):
    raw=arb_mat([[ball(HC[p,a,b],HR[p,a,b]) for b in range(K)] for a in range(K)])
    H.append(U.transpose()*raw*U)
B,H2,H3,H4=H
B2=B*B;M0=H2-B2
M1=H3-B2*B-B*M0-M0*B
M2=(H4-B2*B2-B2*M0-B*M0*B-M0*B2-M0*M0-B*M1-M1*B)
Z=M1.inv()*M0
short=B-M0*Z
res=M0-M1*Z-Z.transpose()*M1+Z.transpose()*M2*Z
delta=arb(os.environ.get('D163_DELTA','0.218'))
lower=short-res/delta

def centre(A):return np.array([[float(A[i,j].mid()) for j in range(K)] for i in range(K)])
print('short centre eig=',np.linalg.eigvalsh((centre(short)+centre(short).T)/2))
print('residual centre eig=',np.linalg.eigvalsh((centre(res)+centre(res).T)/2))
print('conditional lower centre eig=',np.linalg.eigvalsh((centre(lower)+centre(lower).T)/2))

# Frozen Cholesky congruence followed by directed Gershgorin.
lc=centre(lower);lc=(lc+lc.T)/2
if np.linalg.eigvalsh(lc)[0]>0:
    P0=np.linalg.inv(np.linalg.cholesky(lc).T)
    P=arb_mat([[arb(repr(float(P0[i,j]))) for j in range(K)] for i in range(K)])
    Q=P.transpose()*lower*P
    margins=[]
    for i in range(K):
        margins.append(Q[i,i]-sum((abs(Q[i,j]) for j in range(K) if j!=i),arb(0)))
    print('directed conditional Gershgorin margins=',margins)
    print('conditional directed pass=',all(x>0 for x in margins))
else:
    print('conditional centre is not positive')
print('WARNING: DELTA must be supplied by the separate safe-complement proof.')
