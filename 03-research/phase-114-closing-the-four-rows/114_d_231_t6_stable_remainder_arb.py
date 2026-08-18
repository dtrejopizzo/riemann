#!/usr/bin/env python3
"""Directed stable P119 remainder lift at T6.

Constructs the first 120 physical Legendre modes, corrects their two Tate
moments by the exact flat functions (1-u^2)^60 and u(1-u^2)^60, and saves
the unshorted stable frame for cancellation-free action calculations.
"""
from __future__ import annotations
from fractions import Fraction
import os
import numpy as np
from flint import arb,arb_mat,ctx

N,NB,M=200,120,60
ctx.dps=int(os.environ.get('D231_DPS','180'))
T=arb(6).log()/2
def xmul(src):
 out=[Fraction(0) for _ in range(N)]
 for n,v in enumerate(src):
  if not v:continue
  if n+1<N:out[n+1]+=v*Fraction(n+1,2*n+1)
  if n:out[n-1]+=v*Fraction(n,2*n+1)
 return out
g0=[Fraction(0) for _ in range(N)];g0[0]=1
for _ in range(M):
 xx=xmul(xmul(g0));g0=[a-b for a,b in zip(g0,xx)]
g1=xmul(g0)
G=arb_mat(N,2)
for n in range(N):
 scale=(arb(2*n+1)/(2*T)).sqrt()
 for j,g in enumerate((g0,g1)):
  if g[n]:G[n,j]=(arb(g[n].numerator)/g[n].denominator)/scale
def tate(n,sign):
 k=T/2;v=(2*arb.pi()/k).sqrt()*k.bessel_i(arb(2*n+1)/2)
 if sign<0 and n%2:v=-v
 return (T*arb(2*n+1)/2).sqrt()*v
gp=[tate(i,1) for i in range(N)];gm=[tate(i,-1) for i in range(N)]
J=arb_mat([gp,gm]);head=J*G
B=arb_mat(N,NB)
for j in range(NB):B[j,j]=1
B-=G*head.solve(J*B)
assert (J*B).contains(arb_mat(2,NB))
print('exact stable primitive remainder: PASS',flush=True)
gn=np.load('/tmp/t6_gamma260_native250.npz',allow_pickle=False)['G']
cn=np.load('/tmp/t6_contact260_native_strings.npz',allow_pickle=False)['C']
A=arb_mat([[arb(str(gn[i,j]))+arb(str(cn[i,j])) for j in range(N)] for i in range(N)])
m0=arb.pi().log()+arb.const_euler()+arb.pi()/2+3*arb(2).log()
for i in range(N):A[i,i]-=m0
K=B.transpose()*A*B
def pack(X):
 c=np.array([[float(X[i,j].mid()) for j in range(X.ncols())] for i in range(X.nrows())])
 r=np.array([[float(X[i,j].rad()) for j in range(X.ncols())] for i in range(X.nrows())])
 return c,np.nextafter(r+np.abs(np.spacing(c))/2,np.inf)
bc,br=pack(B);kc,kr=pack(K)
bn=np.array([[str(B[i,j]) for j in range(NB)] for i in range(N)],dtype=str)
kn=np.array([[str(K[i,j]) for j in range(NB)] for i in range(NB)],dtype=str)
save=os.environ.get('D231_SAVE','/tmp/t6_stable_remainder_action_graph.npz')
np.savez_compressed(save,C=bc,R=br,K=kc,KR=kr,C_native=bn,K_native=kn,
 endpoint=np.array(6),dimension=np.array(N),native_digits=np.array(ctx.dps))
print('max stable coefficient',np.abs(bc).max(),flush=True)
print('saved',save,flush=True)
print('D231 DIRECTED STABLE REMAINDER: PASS')
