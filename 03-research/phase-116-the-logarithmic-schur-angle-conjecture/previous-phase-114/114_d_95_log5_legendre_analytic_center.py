#!/usr/bin/env python3
"""High-precision analytic center for the D.94 finite Legendre block.

This script contains no Fourier quadrature.  Exponential-kernel matrices are
obtained from the polynomial antiderivative equation (d/du+k)q=P_m; translated
contacts are integrated by polynomial-exact Gauss quadrature.  It is a center
generator for the subsequent Arb enclosure, not itself a certificate.
"""
import math,os,time
import mpmath as mp
import numpy as np
from numpy.polynomial.legendre import leggauss,legvander

N=int(os.environ.get('D95_N','170')); mp.mp.dps=int(os.environ.get('D95_DPS','650'))
T=mp.log(5)/2

def inv_derivative_shift(k):
    # Columns of (D+kI)^-1 in the Legendre basis.  P_l' contains (2j+1)P_j
    # exactly when l>j and l-j is odd; parity suffix sums make this O(N^2).
    Q=[[mp.mpf('0')]*N for _ in range(N)]
    for m in range(N):
        suffix=[mp.mpf('0'),mp.mpf('0')]
        for j in range(m,-1,-1):
            q=((1 if j==m else 0)-(2*j+1)*suffix[1-j%2])/k
            Q[j][m]=q; suffix[j%2]+=q
    return Q

def exp_kernel(b):
    k=mp.mpf(b)*T
    if os.environ.get('D95_UNSAFE_FLOAT','0')=='1' and k > N:
        kk=float(k)
        def finv(z):
            Q=np.zeros((N,N))
            for m in range(N):
                suffix=[0.,0.]
                for j in range(m,-1,-1):
                    q=((1. if j==m else 0.)-(2*j+1)*suffix[1-j%2])/z
                    Q[j,m]=q; suffix[j%2]+=q
            return Q
        Q=finv(kk); RR=finv(-kk)
        signs=(-1.)**np.arange(N)
        qm=signs@Q; rp=np.ones(N)@RR; rm=signs@RR
        J=math.exp(-kk)*rp-math.exp(kk)*rm
        tri=2*Q/(2*np.arange(N)[:,None]+1)-J[:,None]*(math.exp(-kk)*qm)[None,:]
        scale=float(T)/2*np.sqrt(np.outer(2*np.arange(N)+1,2*np.arange(N)+1))
        return scale*(tri+tri.T)
    Q=inv_derivative_shift(k)
    qm=[sum(((-1)**j)*Q[j][m] for j in range(m+1)) for m in range(N)]
    # Stable scaled exponential moments e_n=int P_n(u)e^{-k(u+1)}du.
    # Miller downward recurrence for the minimal solution avoids both Bessel
    # calls and exp(+k): e_{n-1}=e_{n+1}-(2n+1)e_n/k.
    MM=max(N+80,int(k)+80); seq=[mp.mpf('0')]*(MM+2);seq[MM]=mp.mpf(1)
    for n in range(MM,0,-1):seq[n-1]=seq[n+1]-(2*n+1)*seq[n]/k
    e0=-mp.expm1(-2*k)/k; fac=e0/seq[0];ee=[seq[n]*fac for n in range(N)]
    E=np.empty((N,N)); rawmat=np.empty((N,N))
    em=mp.exp(-k)
    for n in range(N):
        for m in range(N):
            tri=2*Q[n][m]/(2*n+1)-qm[m]*ee[n]
            trit=2*Q[m][n]/(2*m+1)-qm[n]*ee[m]
            rawmat[n,m]=float(tri+trit)
    scale=float(T)/2*np.sqrt(np.outer(2*np.arange(N)+1,2*np.arange(N)+1))
    return scale*rawmat

t0=time.time(); A=np.eye(N)*(sum(2*w/b for b,w in
    [(2*j+.5,1.) for j in range(160)]+[(320.5,80.125)])
    -(math.log(math.pi)+0.5772156649015329+math.pi/2+3*math.log(2)))
for it,(b,w) in enumerate([(2*j+.5,1.) for j in range(160)]+[(320.5,80.125)]):
    A-=w*exp_kernel(repr(b))
    if (it+1)%10==0: print('analytic kernels',it+1,'seconds',time.time()-t0,flush=True)

# Exact-polynomial contact quadrature (degree 2N-2, hence N Gauss nodes).
tg,wg=leggauss(N+4)
for shift,c in [(math.log(2),math.log(2)/math.sqrt(2)),
                (math.log(3),math.log(3)/math.sqrt(3)),
                (2*math.log(2),math.log(2)/2)]:
    d=shift/float(T); lo=-1.;hi=1.-d
    u=(lo+hi)/2+(hi-lo)*tg/2; ww=(hi-lo)*wg/2
    X=legvander(u,N-1)*np.sqrt(np.arange(1,2*N,2)/2)[None,:]
    Y=legvander(u+d,N-1)*np.sqrt(np.arange(1,2*N,2)/2)[None,:]
    C=X.T@(ww[:,None]*Y)
    A-=c*(C+C.T)
A=(A+A.T)/2

# Tate moments, evaluated from the same analytic antiderivative recurrence.
G=[]
for sig in (.5,-.5):
    k=abs(mp.mpf(repr(sig))*T);MM=N+100;seq=[mp.mpf('0')]*(MM+2);seq[MM]=1
    for n in range(MM,0,-1):seq[n-1]=seq[n+1]-(2*n+1)*seq[n]/k
    fac=(-mp.expm1(-2*k)/k)/seq[0]; vals=[]
    for n in range(N):
        integ=mp.exp(k)*seq[n]*fac
        if sig>0:integ*=(-1)**n
        vals.append(float(mp.sqrt(T*(2*n+1)/2)*integ))
    G.append(vals)
G=np.asarray(G).T
_,s,vh=np.linalg.svd(G.T,full_matrices=True);NN=vh[2:].T
ev=np.linalg.eigvalsh(NN.T@A@NN)
print('moment singular values',s)
print('analytic-center constrained Ritz',ev[:12])
np.savez('/tmp/d95_log5_legendre_center.npz',A=A,G=G,N=NN)
print('ANALYTIC_HIGH_PRECISION_CENTER_ONLY')
