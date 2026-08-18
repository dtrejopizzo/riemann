#!/usr/bin/env python3
"""Term-by-term floating normalization audit at T=log(5)/2.

Requires `/tmp/d83_degree9.npz` produced by `D83_LOG5=1 D83_SAVE=1`.
This is an audit/selection script, not a directed certificate.
"""
import math
import mpmath as mp
import numpy as np
from numpy.polynomial.legendre import leggauss,legvander

D=10;NC=109;T=.5*math.log(5);z=np.load('/tmp/d83_degree9.npz');A=z['AP']
g1,g2,g3=math.log(5/4),math.log(4/3),math.log(6/5)
hs=[g1/15]*15+[g2/20]*20+[g3/12]*12+[g1/15]*15+[g3/12]*12+[g2/20]*20+[g1/15]*15
left=np.r_[-T,-T+np.cumsum(hs)[:-1]];mid=left+np.asarray(hs)/2
t,w=leggauss(80);P=legvander(t,9)

# Exact-in-the-Galerkin-basis moment vectors and removal of the rho penalty.
mom=[]
for sig in (.5,-.5):
    gv=[]
    for h,m in zip(hs,mid):
        B=P*np.sqrt(np.arange(1,20,2)/h)
        gv.extend(math.exp(sig*m)*B.T@(h*w/2*np.exp(sig*h*t/2)))
    mom.append(gv)
G=np.asarray(mom).T;A0=A-1000*G@G.T

# Even parity and numerical exact-moment kernel.
U=np.zeros((NC*D,545));col=0
for i in range(54):
    for k in range(D):
        U[i*D+k,col]=2**-.5;U[(NC-1-i)*D+k,col]=(-1)**k*2**-.5;col+=1
for k in range(D):
    if k%2==0:U[54*D+k,col]=1;col+=1
Bp=U.T@A0@U;Cp=U.T@G
_,ss,vh=np.linalg.svd(Cp.T,full_matrices=True);N=vh[1:].T
ev,V=np.linalg.eigh(N.T@Bp@N);coef=U@(N@V[:,0]);coef/=np.linalg.norm(coef)

def translated_correlation(coef,shift):
    """Integral f(x)f(x+shift) dx on the exact common cell refinement."""
    tq,wq=leggauss(D)
    right=left+np.asarray(hs)
    corr=0.0
    for i in range(NC):
        for j in range(NC):
            lo=max(left[i],left[j]-shift)
            hi=min(right[i],right[j]-shift)
            if not hi>lo+2e-15:
                continue
            x=(lo+hi)/2+(hi-lo)*tq/2
            wi=(hi-lo)*wq/2
            ui=2*(x-mid[i])/hs[i]
            uj=2*(x+shift-mid[j])/hs[j]
            Bi=legvander(ui,D-1)*np.sqrt(np.arange(1,2*D,2)/hs[i])
            Bj=legvander(uj,D-1)*np.sqrt(np.arange(1,2*D,2)/hs[j])
            fi=Bi@coef[i*D:(i+1)*D]
            fj=Bj@coef[j*D:(j+1)*D]
            corr+=float(wi@(fi*fj))
    return corr

contacts=[];contact_total=0.0
for n,shift,c in [(2,math.log(2),math.log(2)/math.sqrt(2)),
                  (3,math.log(3),math.log(3)/math.sqrt(3)),
                  (4,2*math.log(2),math.log(2)/2)]:
    corr=translated_correlation(coef,shift)
    val=-2*c*corr;contacts.append((n,corr,val));contact_total+=val

assembled=float(coef@A0@coef);gamma_matrix=assembled-contact_total

# Direct Fourier evaluation of the same truncated gamma block.
X=[];W=[];F=[]
for i,(h,m) in enumerate(zip(hs,mid)):
    Bb=P*np.sqrt(np.arange(1,20,2)/h)
    X.extend(m+h*t/2);W.extend(h*w/2);F.extend(Bb@coef[i*D:(i+1)*D])
X=np.asarray(X);W=np.asarray(W);F=np.asarray(F)
bs=np.asarray([2*j+.5 for j in range(160)]+[320.5]);ww=np.asarray([1.]*160+[80.125])
M0=math.log(math.pi)+0.5772156649015329+math.pi/2+3*math.log(2)
Cinf=np.sum(2*ww/bs)-M0
tg,qg=leggauss(900);tau=200*(tg+1)/2;qw=100*qg
vhf=np.exp(-1j*tau[:,None]*X[None,:])@(W*F)
lor=np.sum(2*ww[:,None]*bs[:,None]/(bs[:,None]**2+tau[None,:]**2),axis=0)
gamma_fourier=Cinf-np.sum(qw*abs(vhf)**2*lor)/math.pi

mp.mp.dps=20
full=[]
for x in tau:
    full.append(float(mp.re(mp.digamma(mp.mpf('.25')+1j*mp.mpf(str(x))/2))-mp.log(mp.pi)))
full_partial=np.sum(qw*abs(vhf)**2*np.asarray(full))/math.pi

print('moment singular value / residual:',ss[0],np.linalg.norm(G.T@coef))
for n,corr,val in contacts:print(f'n={n}: correlation={corr:.17g}, form term={val:.17g}')
print('contact total:',contact_total)
print('truncated gamma, matrix:',gamma_matrix)
print('truncated gamma, direct Fourier:',gamma_fourier)
print('assembled constrained value:',assembled,'Ritz:',ev[0])
print('full gamma Fourier partial |tau|<=200:',full_partial)
print('AUDIT_ONLY')
