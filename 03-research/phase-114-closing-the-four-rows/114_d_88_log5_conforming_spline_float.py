#!/usr/bin/env python3
"""Conforming spline Ritz selection at T=log(5)/2 (floating audit).

Unlike the earlier discontinuous cellwise Legendre space, this space is made
of cardinal B-splines supported inside [-T,T].  Its members and their first
P-1 derivatives vanish at the exterior endpoints, so truncated translations
do not create jump singularities.  The gamma block is assembled in Fourier
space from the 160-resolvent-plus-anchor lower multiplier.
"""
import math
import os
import numpy as np
from numpy.polynomial.legendre import leggauss

T=.5*math.log(5); DEG=int(os.environ.get('D88_DEG','5'))
NINT=int(os.environ.get('D88_NINT','120')); h=2*T/NINT; DIM=NINT-DEG
x0=-T

def cardinal(u):
    out=np.zeros_like(np.asarray(u,dtype=float))
    for k in range(DEG+2):
        out += (-1)**k*math.comb(DEG+1,k)*np.maximum(u-k,0.0)**DEG
    return out/math.factorial(DEG)

def overlap(delta):
    # integral B_p(u) B_p(u+delta) du, split at both knot families.
    knots=[float(k) for k in range(DEG+2)]
    knots += [float(k)-delta for k in range(DEG+2)]
    knots=sorted(set(z for z in knots if -1e-14<=z<=DEG+1+1e-14))
    tq,wq=leggauss(DEG+1); ans=0.0
    for a,b in zip(knots[:-1],knots[1:]):
        if b<=a+1e-14: continue
        u=(a+b)/2+(b-a)*tq/2
        ans+=(b-a)/2*np.dot(wq,cardinal(u)*cardinal(u+delta))
    return ans

# Toeplitz mass and translated contacts.
idx=np.arange(DIM); dif=idx[:,None]-idx[None,:]
massvals=np.array([h*overlap(float(d)) for d in range(-(DIM-1),DIM)])
M=massvals[dif+DIM-1]
A=np.zeros_like(M)
CONTACTS=[(math.log(2),math.log(2)/math.sqrt(2)),
          (math.log(3),math.log(3)/math.sqrt(3)),
          (2*math.log(2),math.log(2)/2)]
for shift,c in CONTACTS:
    # C_ij=int phi_i(x)phi_j(x+shift)dx; in cardinal coordinates the second
    # argument is u + (shift/h) + i-j.
    vals=np.array([h*overlap(shift/h+d) for d in range(-(DIM-1),DIM)])
    C=vals[dif+DIM-1]
    A-=c*(C+C.T)
Acontact=A.copy()

# Fourier Toeplitz gamma matrix.  Transform of a cardinal B-spline translate:
# h exp(-it centre) sinc(th/2)^(p+1).
terms=[(2*j+.5,1.) for j in range(160)]+[(320.5,80.125)]
M0=math.log(math.pi)+0.5772156649015329+math.pi/2+3*math.log(2)
Cinf=sum(2*w/b for b,w in terms)-M0
tg,wg=leggauss(96); gamma_vals=np.zeros(DIM)
for aa,bb in zip(np.arange(0.,2000.,10.),np.arange(10.,2010.,10.)):
    tau=(aa+bb)/2+(bb-aa)*tg/2; wt=(bb-aa)*wg/2
    mult=Cinf-sum(2*w*b/(b*b+tau*tau) for b,w in terms)
    ft2=h*h*np.sinc(tau*h/(2*math.pi))**(2*(DEG+1))
    gamma_vals += np.cos(tau[:,None]*h*np.arange(DIM)[None,:]).T@(wt*mult*ft2)/math.pi
A += gamma_vals[np.abs(dif)]
A=(A+A.T)/2; M=(M+M.T)/2

# Exact-polynomial common-refinement Gram of the entire contact image CP.
# This measures QCP without representing Q:
#   (QCP)^*(QCP) = (CP)^*(CP) - (PCP)^* M^{-1}(PCP).
def phi_eval(x):
    u=(np.asarray(x)[:,None]-(x0+h*np.arange(DIM)[None,:]))/h
    mask=(u>=0)&(u<=DEG+1)
    out=np.zeros_like(u); out[mask]=cardinal(u[mask])
    return out

cuts=[-T,T]
base=x0+h*np.arange(NINT+1)
cuts.extend(base)
for shift,_ in CONTACTS:
    cuts.extend(base+shift); cuts.extend(base-shift)
cuts=np.asarray(sorted(z for z in cuts if -T-1e-13<=z<=T+1e-13))
cuts=cuts[np.r_[True,np.diff(cuts)>1e-12]]
tc,wc=leggauss(DEG+1); xx=[]; ww=[]
for a,b in zip(cuts[:-1],cuts[1:]):
    xx.extend((a+b)/2+(b-a)*tc/2); ww.extend((b-a)*wc/2)
xx=np.asarray(xx); ww=np.asarray(ww); Phi=phi_eval(xx); CP=np.zeros_like(Phi)
for shift,c in CONTACTS:
    for sgn in (-1,1):
        y=xx+sgn*shift; inside=(y>=-T)&(y<=T)
        CP[inside]-=c*phi_eval(y[inside])
Mq=Phi.T@(ww[:,None]*Phi); Bc=Phi.T@(ww[:,None]*CP)
Dcp=CP.T@(ww[:,None]*CP)
Rcp=Dcp-Bc.T@np.linalg.solve(M,Bc); Rcp=(Rcp+Rcp.T)/2
Lr=np.linalg.cholesky(M); Lri=np.linalg.inv(Lr)
beta2=max(0.,np.linalg.eigvalsh(Lri@Rcp@Lri.T)[-1])

# Tate moment vectors by exact-degree quadrature on spline knot pieces.
tq,wq=leggauss(16); G=[]
for sig in (.5,-.5):
    g=[]
    for j in range(DIM):
        val=0.0
        for k in range(DEG+1):
            a=x0+(j+k)*h; b=a+h
            x=(a+b)/2+(b-a)*tq/2
            val+=(b-a)/2*np.dot(wq,cardinal((x-(x0+j*h))/h)*np.exp(sig*x))
        g.append(val)
    G.append(g)
G=np.asarray(G).T

# Generalized exact-moment Ritz via mass whitening.
L=np.linalg.cholesky(M); Li=np.linalg.inv(L)
B=Li@A@Li.T; C=Li@G
_,s,vh=np.linalg.svd(C.T,full_matrices=True); rank=np.sum(s>1e-11*s[0]); N=vh[rank:].T
ev=np.linalg.eigvalsh((N.T@B@N+N.T@B.T@N)/2)
print('degree, intervals, dimension:',DEG,NINT,DIM)
print('moment singular values/rank:',s,rank)
print('conforming exact-moment Ritz:',ev[:8])
print('mass/contact assembly errors:',np.linalg.norm(Mq-M),np.linalg.norm(Bc-Acontact))
print('contact QCP beta^2,beta:',beta2,math.sqrt(beta2))
print('FLOAT_SELECTION_AUDIT_ONLY')
