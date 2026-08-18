#!/usr/bin/env python3
"""Directed polynomial-exact contact rows start:stop against V_cols at T6."""
from __future__ import annotations
import os
import numpy as np
from numpy.polynomial.legendre import leggauss
from flint import arb,arb_mat,ctx

START=int(os.environ.get('D233_START','400'));STOP=int(os.environ.get('D233_STOP','600'))
COLS=int(os.environ.get('D233_COLS','200'));PREC=int(os.environ.get('D233_PREC','1800'))
ctx.prec=PREC
# Products have degree at most (STOP-1)+(COLS-1); Q-point Gauss is exact.
Q=(STOP+COLS+1)//2+4
def vals(x,n):
 out=[arb(1),x]
 for k in range(1,n-1):out.append(((2*k+1)*x*out[-1]-k*out[-2])/(k+1))
 return out
def pq(x):return vals(x,Q+1)[-1]
approx=leggauss(Q)[0];pos=[]
assert Q%2==0
for ir,r in enumerate(approx[Q//2:]):
 lo=arb(repr(r-1e-10));hi=arb(repr(r+1e-10));flo=pq(lo)
 assert (flo<0)!=(pq(hi)<0)
 for _ in range(min(850,int(.72*ctx.prec))):
  mid=(lo+hi)/2;fm=pq(mid)
  if not(fm<0 or fm>0):break
  if (fm<0)==(flo<0):lo=mid;flo=fm
  else:hi=mid
 pos.append(arb(mid.mid(),(hi-lo)/2+mid.rad()))
 if (ir+1)%40==0:print('positive roots',ir+1,flush=True)
roots=[-z for z in reversed(pos)]+pos;weights=[]
for z in roots:
 v=vals(z,Q+1);der=Q*(z*v[Q]-v[Q-1])/(z*z-1)
 weights.append(2/((1-z*z)*der*der))
mass=abs(sum(weights,arb(0))-2);print('mass error',mass,flush=True)
assert mass<arb('1e-70')
B=STOP-START;C=arb_mat(B,COLS)
T=arb(6).log()/2
for nn,lam in ((2,arb(2).log()),(3,arb(3).log()),(4,arb(2).log()),(5,arb(5).log())):
 d=arb(nn).log()/T;mid=-d/2;half=1-d/2;coef=lam/arb(nn).sqrt()
 for iq,(z,w) in enumerate(zip(roots,weights)):
  u=mid+half*z;vx=vals(u,STOP);vy=vals(u+d,STOP);ww=half*w
  for k in range(STOP):
   sc=(arb(2*k+1)/2).sqrt();vx[k]*=sc;vy[k]*=sc
  mx=arb_mat([[vx[m]] for m in range(START,STOP)])
  my=arb_mat([[vy[m]] for m in range(START,STOP)])
  rx=arb_mat([[vx[n] for n in range(COLS)]])
  ry=arb_mat([[vy[n] for n in range(COLS)]])
  C-=coef*ww*(mx*ry+my*rx)
  if (iq+1)%100==0:print('contact',nn,'node',iq+1,flush=True)
c=np.array([[float(C[i,j].mid()) for j in range(COLS)] for i in range(B)])
r=np.array([[float(C[i,j].rad()) for j in range(COLS)] for i in range(B)])
r=np.nextafter(r+np.abs(np.spacing(c))/2,np.inf);assert np.isfinite(c).all() and np.isfinite(r).all()
s=np.array([[str(C[i,j]) for j in range(COLS)] for i in range(B)],dtype=str)
save=os.environ.get('D233_SAVE','/tmp/t6_contact_row400_600_col200.npz')
np.savez_compressed(save,C=c,R=r,A=s,start=np.array(START),stop=np.array(STOP),cols=np.array(COLS),bits=np.array(ctx.prec))
print('max radius',r.max(),flush=True);print('saved',save,flush=True)
print('D233 DIRECTED CONTACT ROW BAND: PASS')
