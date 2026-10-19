#!/usr/bin/env python3
# ======================================================================================
# Phase 60 — E9b: CLEAN classification. Real zeros of L_DH (mpmath) vs roots of ξ̂_DH.
#
# E9 showed: ξ̂_DH places a real root at 85.7306 (close to Re of the off-line zero 85.699),
# which CONVERGES. Is that "it sees an on-line zero that actually exists there" (no
# signal) or "it fills in the real projection of the off-line pair" (Scenario B, blind to
# position)? Decided by knowing where the TRUE zeros of L_DH are.
#
# f_DH(s) = 5^{-s} Σ_{r=1}^{5} a(r) ζ(s, r/5)   (Hurwitz), a=(1,κ,-κ,-1,0), κ=0.284079.
# We look for on-line zeros (s=1/2+it) by sign change of f on the line, and confirm
# the off-line pair 0.8085±... +85.699i. Then overlay with the real roots of ξ̂_DH.
# ======================================================================================
import numpy as np, importlib.util, mpmath as mp
mp.mp.dps=30
spec=importlib.util.spec_from_file_location("e5","/Users/dt/riemann/riemann-program/phase-60-discriminante/experiments/E5_ldh_violator.py")
e5=importlib.util.module_from_spec(spec); spec.loader.exec_module(e5)

KAPPA=mp.mpf((np.sqrt(10-2*np.sqrt(5))-2)/(np.sqrt(5)-1))
A=[mp.mpf(0),mp.mpf(1),KAPPA,-KAPPA,mp.mpf(-1)]   # a[r], r=1..4, a[5]=a[0]=0  -> index r%5

def f_dh(s):
    return mp.mpf(5)**(-s)*mp.fsum([A[r%5]*mp.zeta(s, mp.mpf(r)/5) for r in range(1,6)])

print("="*80)
print(" E9b: real zeros of L_DH (mpmath) vs roots of ξ̂_DH (CCM, lambda=6)")
print("="*80,flush=True)

# 1) confirm the known off-line zero
z_off=mp.mpf('0.5')+mp.mpf('0.3085')+1j*mp.mpf('85.699')
print(f"\n confirming off-line zero: f_DH(0.8085+85.699i) = {mp.nstr(f_dh(z_off),4)}",flush=True)
try:
    zo=mp.findroot(f_dh, mp.mpf('0.8085')+1j*mp.mpf('85.699'))
    print(f"   refined: s={mp.nstr(zo,10)}   (Re-1/2={mp.nstr(mp.re(zo)-0.5,4)}, Im={mp.nstr(mp.im(zo),8)})",flush=True)
except Exception as ex:
    print("   off-line findroot failed:",ex,flush=True)

# 2) ON-line zeros (s=1/2+it): sign changes of g(t)=f_dh(1/2+it) (real on the line? not necessarily)
#    f_DH is NOT self-dual real; we use a Z-function: rotate by the phase of the gamma factor. Simplest:
#    look for minima of |f_dh(1/2+it)| as a proxy for on-line zeros.
print("\n on-line zeros of L_DH (minima of |f_DH(1/2+it)|) in windows of interest:",flush=True)
def find_online_zeros(t0,t1,step=mp.mpf('0.05')):
    ts=[]; t=t0; prev=abs(f_dh(mp.mpf('0.5')+1j*t)); pt=t
    vals=[]
    tt=t0
    while tt<=t1:
        v=abs(f_dh(mp.mpf('0.5')+1j*tt)); vals.append((tt,v)); tt+=step
    # local minima below threshold
    out=[]
    for i in range(1,len(vals)-1):
        if vals[i][1]<vals[i-1][1] and vals[i][1]<vals[i+1][1] and vals[i][1]<0.05:
            # refine
            try:
                zr=mp.findroot(lambda t: f_dh(mp.mpf('0.5')+1j*t), vals[i][0])
                if abs(mp.im(zr))>0 and abs(mp.re(zr))<1e-6: pass
                out.append(complex(vals[i][0], float(vals[i][1])))
            except Exception: out.append(complex(vals[i][0], float(vals[i][1])))
    return out

for (lo,hi,lab) in [(44,54,"on-line interior ~49"),(80,92,"around off-line 85.7"),(110,118,"around off-line 114.2")]:
    zs=find_online_zeros(mp.mpf(lo),mp.mpf(hi))
    print(f"  [{lo},{hi}] {lab}: on-line |f| minima at t≈ {[round(z.real,3) for z in zs]}  (|f|={[round(z.imag,4) for z in zs]})",flush=True)

# 3) real roots of ξ̂_DH (CCM) in the same windows
print("\n real roots of ξ̂_DH (CCM lambda=6, N=80):",flush=True)
LAM=6.0; tgrid=np.arange(-600,600,0.01)+1e-6
coeffs_ldh=e5.ldh_b_upto(int(LAM*LAM))
QW,idx,L=e5.build_QW(LAM,80,0.75,5.0,coeffs_ldh,False,tgrid)
w,V=np.linalg.eigh(QW); xi=V[:,0]
d=2*np.pi*idx/L; o=np.argsort(d); d=d[o]; xi=xi[o]
from scipy.optimize import brentq
f=lambda s: np.sum(xi/(s-d)); roots=[]
for i in range(len(d)-1):
    aa,bb=d[i]+1e-7,d[i+1]-1e-7
    if aa>=bb or bb<40 or aa>120: continue
    try:
        if f(aa)*f(bb)<0: roots.append(brentq(f,aa,bb,xtol=1e-11))
    except Exception: pass
roots=np.array(sorted(roots))
for (lo,hi) in [(44,54),(80,92),(110,118)]:
    print(f"  [{lo},{hi}]: {np.round(roots[(roots>=lo)&(roots<=hi)],4)}",flush=True)

print("\n"+"="*80)
print(" READING: if ξ̂_DH has a real root at ~85.73 BUT L_DH has NO on-line zero there")
print("   (only the off-line pair) => ξ̂ FILLS IN the real projection = Scenario B (blind).")
print("   If L_DH has an on-line zero at ~85.73 => ξ̂ merely reproduces it, no signal.")
print("   If ξ̂ has a GAP where a zero should be => it detects off-line = Scenario A.")
