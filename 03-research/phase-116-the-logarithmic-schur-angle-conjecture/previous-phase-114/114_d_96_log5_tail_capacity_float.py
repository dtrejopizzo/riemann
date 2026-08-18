#!/usr/bin/env python3
"""Floating tail-capacity audit for the three D.95 near modes."""
import math
import mpmath as mp
import numpy as np
from numpy.polynomial.legendre import leggauss,legvander
z=np.load('/tmp/d95_n80_modes.npz'); modes=z['full']; eig=z['e']
N=modes.shape[0];T=.5*math.log(5)
u,w=leggauss(420);x=T*u;ww=T*w
B=legvander(u,N-1)*np.sqrt(np.arange(1,2*N,2)/(2*T))[None,:]
Fphys=B@modes[:,:3]
terms=[(2*j+.5,1.) for j in range(160)]+[(320.5,80.125)]
M0=math.log(math.pi)+0.5772156649015329+math.pi/2+3*math.log(2)
Cinf=sum(2*c/b for b,c in terms)-M0
mp.mp.dps=25; tg,wg=leggauss(64); cap=np.zeros(3)
for aa in np.arange(0.,100.,1.):
    tau=aa+.5+.5*tg;wt=.5*wg
    vh=np.exp(-1j*tau[:,None]*x[None,:])@(ww[:,None]*Fphys)
    low=Cinf-sum(2*c*b/(b*b+tau*tau) for b,c in terms)
    full=np.array([float(mp.re(mp.digamma(mp.mpf('.25')+.5j*float(t)))-mp.log(mp.pi)) for t in tau])
    delta=full-low
    cap+=np.sum((wt*delta/math.pi)[:,None]*abs(vh)**2,axis=0)
print('lower-model eigs:',eig[:3])
print('capacity [0,100]:',cap)
print('lifted partial values:',eig[:3]+cap)
print('FLOAT_CAPACITY_SELECTION_ONLY')
