#!/usr/bin/env python3
"""Directed full (untruncated) Gamma matrix on 170 Legendre modes.

Implements D.146 using Hurwitz zeta and a directed rapidly convergent Lerch
series.  This file builds the archimedean block only; contacts are added by
the companion endpoint verifier.
"""
import math,os,time
import numpy as np
from flint import arb,arb_mat,ctx
ctx.prec=int(os.environ.get('D99_PREC','2048'))
N=int(os.environ.get('D99_N','170')); T=arb(5).log()/2; z=arb(1)/25

def lerch(r):
    # Positive series; the omitted tail is at most z^J/(1-z)/(J+1/4)^r.
    J=700;s=arb(0);zz=arb(1);a=arb(1)/4
    for j in range(J):s+=zz/(arb(j)+a)**r;zz*=z
    tail=zz/(1-z)/(arb(J)+a)**r
    return s+arb(0,tail)

wz=[arb(0)]*(2*N+1);wx=[arb(0)]*(2*N+1)
for r in range(2,2*N+1):
    base=(2*T)**(-r)
    wz[r]=base*arb(r).zeta(arb(1)/4)
    wx[r]=(-T).exp()*base*lerch(r)

# Coefficients q^-(x), endpoint derivative polynomials, and the weighted
# linear resolvent term.  Applying D uses parity suffix sums and is O(N^3).
qm=[[arb(0) for _ in range(N)] for _ in range(N)]
am=[[arb(0) for _ in range(N)] for _ in range(N)]
bp=[[arb(0) for _ in range(N)] for _ in range(N)]
L=[[arb(0) for _ in range(N)] for _ in range(N)]
for m in range(N):
    for s in range(m+1):
        val=arb(math.factorial(m+s))/(arb(2)**s*math.factorial(s)*math.factorial(m-s))
        bp[m][s]=val;am[m][s]=((-1)**(m+s))*val

for n in range(N):
    v=[0]*N;v[n]=1
    for r in range(1,n+2):
        sign=-1 if r%2==0 else 1
        qm[n][r-1]=arb(sign*sum(((-1)**j)*v[j] for j in range(N)))
        if r>=2:
            for j in range(N):
                if v[j]:L[j][n]+=wz[r]*arb(2*sign*v[j])/arb(2*j+1)
        suffix=[0,0];nv=[0]*N
        for j in range(N-1,-1,-1):
            nv[j]=(2*j+1)*suffix[1-j%2];suffix[j%2]+=v[j]
        v=nv

print('coefficient tables ready',flush=True)
A=arb_mat(am);B=arb_mat(bp);Q=arb_mat(qm)
Hz=arb_mat([[wz[p+q+2] for q in range(N)] for p in range(N)])
Hx=arb_mat([[wx[p+q+2] for q in range(N)] for p in range(N)])
Pminus=A*Hz*Q.transpose();Pexp=B*Hx*Q.transpose();Lin=arb_mat(L)
inside=Lin+Lin.transpose()-Pminus-Pminus.transpose()+Pexp+Pexp.transpose()

M0=arb.pi().log()+arb.const_euler()+arb.pi()/2+3*arb(2).log()
G=[[arb(0) for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        scale=T/2*(arb(2*i+1)*arb(2*j+1)).sqrt()
        G[i][j]=-scale*inside[i,j]
        if i==j:G[i][j]-=M0
print('full Gamma matrix ready',flush=True)

center=np.array([[float(G[i][j].mid()) for j in range(N)] for i in range(N)])
maxrad=max(float(G[i][j].rad()) for i in range(N) for j in range(N))
np.savez('/tmp/d99_full_gamma_arb.npz',G=center,maxrad=maxrad)
print('max entry radius=',maxrad)
print('Gamma center eigen first=',np.linalg.eigvalsh((center+center.T)/2)[:8])
assert maxrad < (1e-80 if ctx.prec < 1000 else 1e-100)
print('PASS directed full Hurwitz--Lerch Gamma matrix enclosure')
