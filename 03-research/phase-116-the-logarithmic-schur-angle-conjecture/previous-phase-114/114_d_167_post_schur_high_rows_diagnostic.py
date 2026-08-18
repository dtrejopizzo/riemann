#!/usr/bin/env python3
"""High-row diagnostic for the five D166 post-Schur graph columns.

This is deliberately not a certificate: the Schur graph and the rectangular
contact block are reconstructed from binary64 centres.  The Gamma contraction
is nevertheless evaluated with Arb before conversion to a midpoint.  This
avoids the catastrophic cancellation seen when a low-precision rectangular
Gamma matrix is converted entry by entry.
"""
import importlib.util, math, os, time
from pathlib import Path
import numpy as np
from numpy.polynomial.legendre import leggauss, legvander
from flint import arb_mat, ctx

HERE=Path(__file__).resolve().parent
N0=int(os.environ.get("D167_N0","200")); N1=int(os.environ.get("D167_N1","260"))
DPS=int(os.environ.get("D167_DPS","1500")); ctx.dps=DPS
assert N1>N0

z=np.load('/tmp/d166_nested200_centres.npz')
A,D,S,Y=(z[k] for k in ('A','D','S','Y'))
AYY=Y.T@A@Y; F=np.c_[D,S]
K=F.T@A@F-F.T@A@Y@np.linalg.solve(AYY,Y.T@A@F)
cs=-np.linalg.solve(K[5:,5:],K[5:,:5])
cy=-np.linalg.solve(AYY,Y.T@A@(D+S@cs))
X=D+S@cs+Y@cy

spec=importlib.util.spec_from_file_location('d147',HERE/'114_d_147_hurwitz_gamma_arb.py')
d147=importlib.util.module_from_spec(spec);spec.loader.exec_module(d147)
t=time.time(); G=d147.exact_gamma_block(N1,DPS)
print('Gamma assembly seconds =',time.time()-t,flush=True)
V=arb_mat([[repr(float(X[i,j])) for j in range(5)] for i in range(N0)])
GH=arb_mat([[G[i,j] for j in range(N0)] for i in range(N0,N1)])*V

# Polynomial-exact Gauss order in exact arithmetic; here its binary64
# evaluation is used only for the diagnostic contact centre.
q=N1+40; nodes,weights=leggauss(q); T=math.log(5)/2
C=np.zeros((N1,N0)); scales=np.sqrt((2*np.arange(N1)+1)/2)
for shift,c in ((math.log(2),math.log(2)/math.sqrt(2)),
                (math.log(3),math.log(3)/math.sqrt(3)),
                (2*math.log(2),math.log(2)/2)):
    d=shift/T; mid=-d/2; half=1-d/2; u=mid+half*nodes
    vx=legvander(u,N1-1)*scales
    vy=legvander(u+d,N1-1)*scales
    C-=c*half*((vx*weights[:,None]).T@vy[:,:N0]
               +(vy*weights[:,None]).T@vx[:,:N0])
CH=C[N0:]@X

centre=np.array([[float(GH[i,j].mid())+CH[i,j] for j in range(5)]
                 for i in range(N1-N0)])
radius=np.array([[float(GH[i,j].rad()) for j in range(5)]
                 for i in range(N1-N0)])
norms=np.sqrt(np.sum(centre*centre,axis=0))
print('Gamma contraction maximum Arb radius =',radius.max())
print(f'row {N0}:{N1} residual norms =',norms)
np.savez('/tmp/d167_post_schur_high_rows_diagnostic.npz',C=centre,R=radius,X=X)
assert radius.max()<1e-100
print('DIAGNOSTIC_ONLY: graph and contacts use binary64 centres')
