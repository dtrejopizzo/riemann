#!/usr/bin/env python3
"""Floating feasibility audit for the joint-multiplier/prolate split.

Contacts are kept inside the complete Fourier multiplier.  The prolate
concentration operator then bounds the low-frequency mass of the orthogonal
complement without ever estimating Q(contact)P separately.
"""
import math
import mpmath as mp
import numpy as np
from numpy.polynomial.legendre import leggauss

T=.5*math.log(5); R=150.; NQ=500
contacts=[(math.log(2),math.log(2)/math.sqrt(2)),
          (math.log(3),math.log(3)/math.sqrt(3)),
          (2*math.log(2),math.log(2)/2)]

def multiplier(t):
    return float(mp.re(mp.digamma(mp.mpf('.25')+.5j*t))-mp.log(mp.pi)
                 -2*sum(c*mp.cos(a*t) for a,c in contacts))

# Selection-only sampled bounds; a directed analytic bound must replace them
# in a certificate.
grid=np.linspace(0,R,3001); vals=np.array([multiplier(float(t)) for t in grid])
tail=np.linspace(R,R+300,6001); tailvals=np.array([multiplier(float(t)) for t in tail])
Mlow=max(0.,-vals.min()); gsample=tailvals.min()

u,w=leggauss(NQ); x=T*u; w=T*w
z=R*(x[:,None]-x[None,:])
K=(R/math.pi)*np.sinc(z/math.pi)*np.sqrt(w[:,None]*w[None,:])
lam=np.linalg.eigvalsh((K+K.T)/2)[::-1]
print('T,R,Shannon number:',T,R,2*T*R/math.pi)
print('sample low minimum / Mlow:',vals.min(),Mlow)
print('sample tail minimum [R,R+300]:',gsample)
for k in (80,85,90):
    qlower=gsample-(gsample+Mlow)*lam[k]
    print(f'K={k}: lambda_(K+1)={lam[k]:.17g}, sampled Q lower={qlower:.17g}')
print('FLOAT_FEASIBILITY_AUDIT_ONLY')
