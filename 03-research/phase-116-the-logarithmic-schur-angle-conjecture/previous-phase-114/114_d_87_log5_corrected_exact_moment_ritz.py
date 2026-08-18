#!/usr/bin/env python3
"""Corrected exact-moment Ritz audit at T=log(5)/2.

The contact matrices in the input were assembled by exact polynomial
integration on the common refinement of the mesh and all translated meshes.
This is a floating selection audit, not a directed certificate.
"""
import math
import numpy as np
from numpy.polynomial.legendre import leggauss, legvander

D=10; NC=109; T=.5*math.log(5)
z=np.load('/tmp/d83_degree9.npz'); A=z['AP']
g1,g2,g3=math.log(5/4),math.log(4/3),math.log(6/5)
hs=[g1/15]*15+[g2/20]*20+[g3/12]*12+[g1/15]*15+[g3/12]*12+[g2/20]*20+[g1/15]*15
left=np.r_[-T,-T+np.cumsum(hs)[:-1]]; mid=left+np.asarray(hs)/2
t,w=leggauss(24); P=legvander(t,D-1)

mom=[]
for sig in (.5,-.5):
    gv=[]
    for h,m in zip(hs,mid):
        B=P*np.sqrt(np.arange(1,2*D,2)/h)
        gv.extend(math.exp(sig*m)*B.T@(h*w/2*np.exp(sig*h*t/2)))
    mom.append(gv)
G=np.asarray(mom).T
A0=(A-1000*G@G.T); A0=(A0+A0.T)/2

def parity_basis(sgn):
    cols=NC//2*D+(D//2 if NC%2 else 0)
    U=np.zeros((NC*D,cols)); col=0
    for i in range(NC//2):
        for k in range(D):
            U[i*D+k,col]=2**-.5
            U[(NC-1-i)*D+k,col]=sgn*((-1)**k)*2**-.5
            col+=1
    if NC%2:
        for k in range(D):
            if (-1)**k==sgn:
                U[(NC//2)*D+k,col]=1; col+=1
    assert col==cols
    return U

for name,sgn in [('even',1),('odd',-1)]:
    U=parity_basis(sgn); B=U.T@A0@U; C=U.T@G
    _,s,vh=np.linalg.svd(C.T,full_matrices=True)
    rank=int(np.sum(s>1e-11*s[0]))
    N=vh[rank:].T
    vals=np.linalg.eigvalsh((N.T@B@N+N.T@B.T@N)/2)
    print(f'{name}: moment rank={rank}, singular values={s}')
    print(f'{name}: exact-moment Ritz first={vals[0]:.17g}, second={vals[1]:.17g}')
print('FLOAT_SELECTION_AUDIT_ONLY')
