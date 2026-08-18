#!/usr/bin/env python3
"""Directed rows 200:260 of all active T6 contact operators."""
from __future__ import annotations
import os
import numpy as np
from flint import arb, arb_mat, ctx

N0,N1,Q=200,260,264
ctx.prec=int(os.environ.get("D211_PREC","1600"))
T=arb(6).log()/2

def legvals(x):
 out=[arb(1),x]
 for n in range(1,N1-1):out.append(((2*n+1)*x*out[-1]-n*out[-2])/(n+1))
 return out

directed=[arb.legendre_p_root(Q,k,weight=True) for k in range(Q)]
roots=[z[0] for z in directed];weights=[z[1] for z in directed]
assert abs(sum(weights,arb(0))-2)<arb("1e-100")
norm=[(arb(2*i+1)/2).sqrt() for i in range(N1)]
C=arb_mat(N1-N0,N1)
for nn,lam in ((2,arb(2).log()),(3,arb(3).log()),
               (4,arb(2).log()),(5,arb(5).log())):
 d=arb(nn).log()/T;mid=-d/2;half=1-d/2;c=lam/arb(nn).sqrt()
 for iq,(z,w) in enumerate(zip(roots,weights)):
  u=mid+half*z;vx=legvals(u);vy=legvals(u+d)
  for i in range(N1):vx[i]*=norm[i];vy[i]*=norm[i]
  scale=-c*half*w
  for i in range(N0,N1):
   ii=i-N0;xi=vx[i];yi=vy[i]
   for j in range(N1):C[ii,j]+=scale*(xi*vy[j]+yi*vx[j])
 if nn in (2,3,4,5):print("contact high rows",nn,"complete",flush=True)

centre=np.array([[float(C[i,j].mid()) for j in range(N1)] for i in range(N1-N0)])
radius=np.array([[float(C[i,j].rad()) for j in range(N1)] for i in range(N1-N0)])
saved=np.nextafter(radius+np.abs(np.spacing(centre))/2,np.inf)
np.savez(os.environ.get("D211_SAVE","/tmp/t6_contact_high200_260_arb.npz"),
 C=centre,R=saved,row_start=np.array(N0),row_end=np.array(N1),digits=np.array(ctx.prec))
print("max serialized radius",saved.max())
print("D211 DIRECTED T6 CONTACT HIGH ROWS: PASS")
