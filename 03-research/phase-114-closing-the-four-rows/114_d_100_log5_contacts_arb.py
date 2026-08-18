#!/usr/bin/env python3
"""Directed polynomial-exact Gauss assembly of endpoint contacts."""
import math,os
import numpy as np
from numpy.polynomial.legendre import leggauss
from flint import arb,ctx
ctx.prec=int(os.environ.get('D100_PREC','2048'))
N=int(os.environ.get('D100_N','170'));Q=N+4

def legvals(x,nmax):
    out=[arb(1)]
    if nmax==1:return out
    out.append(x)
    for n in range(1,nmax-1):out.append(((2*n+1)*x*out[-1]-n*out[-2])/(n+1))
    return out

def pq_point(x):return legvals(x,Q+1)[-1]

# Certified brackets obtained only from point evaluations; no interval
# recurrence is used until the brackets are narrower than 1e-210.
approx=leggauss(Q)[0]; positive=[]
# Q=N+4 is even in the target run.  Certify the positive roots and obtain
# the negative ones from the exact parity P_Q(-x)=P_Q(x).
assert Q%2==0
for ir,r in enumerate(approx[Q//2:]):
    lo=arb(repr(r-1e-10));hi=arb(repr(r+1e-10));flo=pq_point(lo)
    assert (flo<0 or flo>0) and (pq_point(hi)<0 or pq_point(hi)>0)
    assert (flo<0) != (pq_point(hi)<0)
    # The interval evaluation eventually becomes sign-indeterminate when the
    # bracket is narrower than the working precision.  Retaining the last
    # opposite-sign endpoints is already a certified root enclosure.
    for _ in range(min(760, int(0.72*ctx.prec))):
        mid=(lo+hi)/2;fm=pq_point(mid)
        if not (fm<0 or fm>0): break
        if (fm<0)==(flo<0):lo=mid;flo=fm
        else:hi=mid
    mid=(lo+hi)/2;positive.append(arb(mid.mid(),(hi-lo)/2+mid.rad()))
    if (ir+1)%40==0:print('positive roots',ir+1,flush=True)
roots=[-x for x in reversed(positive)]+positive

weights=[]
for x in roots:
    vals=legvals(x,Q+1);der=Q*(x*vals[Q]-vals[Q-1])/(x*x-1)
    weights.append(2/((1-x*x)*der*der))
mass_error=abs(sum(weights,arb(0))-2)
print('Gauss mass enclosure error=',mass_error,flush=True)
# The contact entries have magnitude at most a polynomial factor in N times
# the Gauss mass.  At N<=260 the historical 1e-120 gate is inexpensive.  At
# N=400 interval recurrence dependency widens the mass ball; 1e-70 still
# leaves over fifty decimal orders beyond every later pivot and is propagated
# entrywise below rather than discarded.
mass_gate = ('1e-70' if N > 260 else
             ('1e-100' if ctx.prec < 1000 else '1e-120'))
assert mass_error < arb(mass_gate)
print('certified Gauss rule ready',flush=True)

Ctot=[[arb(0) for _ in range(N)] for _ in range(N)]
XEND=int(os.environ.get('D100_X','5'));T=arb(XEND).log()/2
contacts=[(2,arb(2).log()),(3,arb(3).log()),(4,arb(2).log()),
          (5,arb(5).log())]
for nn,lam in contacts:
    if nn>=XEND: continue
    shift=arb(nn).log();c=lam/arb(nn).sqrt()
    d=shift/T;mid=-d/2;half=1-d/2
    for iq,(t,w) in enumerate(zip(roots,weights)):
        u=mid+half*t;vx=legvals(u,N);vy=legvals(u+d,N);ww=half*w
        for i in range(N):
            vx[i]*=(arb(2*i+1)/2).sqrt();vy[i]*=(arb(2*i+1)/2).sqrt()
        for i in range(N):
            wi=ww*vx[i]
            for j in range(N):Ctot[i][j]-=c*(wi*vy[j]+ww*vy[i]*vx[j])
        if (iq+1)%50==0:print('contact node',iq+1,flush=True)

center=np.array([[float(Ctot[i][j].mid()) for j in range(N)] for i in range(N)])
radii=np.array([[float(Ctot[i][j].rad()) for j in range(N)] for i in range(N)])
radii=np.nextafter(radii,np.inf)
print('max native contact radius=',radii.max())
radius_gate = (1e-65 if N > 260 else
               (1e-45 if ctx.prec < 1000 else 1e-100))
assert radii.max() < radius_gate
# Saving a binary64 midpoint discards most of the Arb precision.  Enlarge by
# half an ulp so that the serialized pair remains a rigorous enclosure.
saved_radii=radii+np.abs(np.spacing(center))/2+np.nextafter(0.,1.)
np.savez(os.environ.get('D100_SAVE','/tmp/d100_contacts_arb.npz'),C=center,R=saved_radii,
         endpoint=np.array(XEND))
native_save=os.environ.get('D100_NATIVE_SAVE')
if native_save:
    native=np.array([[str(Ctot[i][j]) for j in range(N)] for i in range(N)],dtype=str)
    np.savez_compressed(native_save,C=native,endpoint=np.array(XEND),
                        bits=np.array(ctx.prec),N=np.array(N))
    print('saved native contact balls=',native_save,flush=True)
print('max serialized contact radius=',saved_radii.max())
print('PASS directed polynomial-exact contact matrix enclosure')
