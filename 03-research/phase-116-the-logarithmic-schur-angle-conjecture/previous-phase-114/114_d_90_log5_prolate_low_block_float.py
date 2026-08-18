#!/usr/bin/env python3
"""Floating low-block audit in the first 86 prolate modes at log(5)/2."""
import math
import os
import numpy as np
from numpy.polynomial.legendre import leggauss,legvander

T=.5*math.log(5); R=150.; NX=500; KMOD=int(os.environ.get('D90_K','86'))
u,w=leggauss(NX); x=T*u; w=T*w; sw=np.sqrt(w)
z=R*(x[:,None]-x[None,:])
K=(R/math.pi)*np.sinc(z/math.pi)*sw[:,None]*sw[None,:]
lam,V=np.linalg.eigh((K+K.T)/2); order=np.argsort(lam)[::-1]
lam=lam[order]; V=V[:,order[:KMOD]]
LEGENDRE=os.environ.get('D90_BASIS','prolate')=='legendre'
if LEGENDRE:
    # sqrt(quadrature-weight) times the first KMOD orthonormal Legendre
    # functions on [-T,T]; this defines an entirely explicit low space.
    V=legvander(u,KMOD-1)*np.sqrt(np.arange(1,2*KMOD,2)/2)[None,:]*np.sqrt(w/T)[:,None]

terms=[(2*j+.5,1.) for j in range(160)]+[(320.5,80.125)]
M0=math.log(math.pi)+0.5772156649015329+math.pi/2+3*math.log(2)
Cinf=sum(2*c/b for b,c in terms)-M0
contacts=[(math.log(2),math.log(2)/math.sqrt(2)),
          (math.log(3),math.log(3)/math.sqrt(3)),
          (2*math.log(2),math.log(2)/2)]
def rlower(t):
    ans=Cinf-sum(2*c*b/(b*b+t*t) for b,c in terms)
    ans-=2*sum(c*np.cos(a*t) for a,c in contacts)
    return ans

# Fourier quadratic form on the prolate basis, positive frequencies doubled.
tg,wg=leggauss(64); A=np.zeros((KMOD,KMOD)); WV=sw[:,None]*V
for ib,(aa,bb) in enumerate(zip(np.arange(0.,2000.,10.),np.arange(10.,2010.,10.))):
    tau=(aa+bb)/2+(bb-aa)*tg/2; wt=(bb-aa)*wg/2
    F=np.exp(-1j*tau[:,None]*x[None,:])@WV
    rr=rlower(tau)
    A += np.real(F.conj().T@((wt*rr/math.pi)[:,None]*F))
    if (ib+1)%50==0: print('Fourier blocks',ib+1,flush=True)
A=(A+A.T)/2
if os.environ.get('D90_SAVE','0')=='1':
    np.savez('/tmp/d90_low_block.npz',A=A,V=V)

# Exact-moment constraints in the physical Nyström metric.
G=np.column_stack([V.T@(sw*np.exp(.5*x)),V.T@(sw*np.exp(-.5*x))])
_,s,vh=np.linalg.svd(G.T,full_matrices=True); rank=np.sum(s>1e-11*s[0]); N=vh[rank:].T
ev=np.linalg.eigvalsh((N.T@A@N+N.T@A.T@N)/2)
print('basis:', 'Legendre' if LEGENDRE else 'prolate')
if not LEGENDRE: print(f'prolate lambda_{KMOD}:',lam[KMOD-1])
print('moment singular values/rank:',s,rank)
print('prolate constrained lower-model Ritz:',ev[:12])
print('FLOAT_SELECTION_AUDIT_ONLY')
