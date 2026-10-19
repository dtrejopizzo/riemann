#!/usr/bin/env python3
# ======================================================================================
# Phase 60 — E9c: the decisive DISCRIMINANT, free of normalization. Trend in lambda.
#
# E9/E9b (lambda=6): ξ̂_DH places a real root at 85.731 (real projection of the off-line
# zero 85.699), convergent in N. Scenario A or B? Decided by the TREND IN LAMBDA of the gap
#   gap(lambda) = |closest_real_root(ξ̂_DH) - 85.699|.
#
#   Scenario B (blind): gap(lambda) -> 0  (ξ̂ converges its root to the real projection, as
#       if the zero were on-line). The "convergence=>RH bridge" is an illusion.
#   Scenario A (sees position): gap(lambda) does NOT -> 0 / it grows (Hurwitz: real-rooted
#       cannot converge to a complex zero). -> Theorem 2 with teeth.
#
# Control: same measure for an ON-line zero of L_DH at interior height (must -> 0 in both).
# And off-axis residual |f_DH(85.699-0.3085i)| normalized by the typical |f_DH| at that depth.
# ======================================================================================
import numpy as np, importlib.util
spec=importlib.util.spec_from_file_location("e5","/Users/dt/riemann/riemann-program/phase-60-discriminante/experiments/E5_ldh_violator.py")
e5=importlib.util.module_from_spec(spec); spec.loader.exec_module(e5)

OFF_IM=85.699; OFF_DEPTH=0.3085
rho0=OFF_IM-1j*OFF_DEPTH

def build_xi(lam,N):
    tgrid=np.arange(-3.5*120,3.5*120,0.01)+1e-6
    coeffs=e5.ldh_b_upto(int(lam*lam))
    QW,idx,L=e5.build_QW(lam,N,0.75,5.0,coeffs,False,tgrid)
    w,V=np.linalg.eigh(QW); xi=V[:,0]
    d=2*np.pi*idx/L; o=np.argsort(d); d=d[o]; xi=xi[o]
    return xi,d

def real_roots(xi,d,lo,hi):
    from scipy.optimize import brentq
    f=lambda s: np.sum(xi/(s-d)); r=[]
    for i in range(len(d)-1):
        a,b=d[i]+1e-7,d[i+1]-1e-7
        if a>=b or b<lo or a>hi: continue
        try:
            if f(a)*f(b)<0: r.append(brentq(f,a,b,xtol=1e-11))
        except Exception: pass
    return np.array(sorted([x for x in r if lo<x<hi]))

def fc(xi,d,s): return np.sum(xi/(s-d))

print("="*82)
print(" E9c: trend in lambda of the gap to the off-line zero of L_DH (t=85.699)")
print("="*82)
print(f"{'lambda':>7} {'T*':>7} {'x=85.7/T*':>10} {'N':>4} | {'raiz~85.7':>11} {'gap':>9} | {'|f(rho0)|':>11} {'|f|tipico':>10} {'ratio':>8}",flush=True)

for lam in [3.5,4.0,4.5,5.0,6.0,7.0,8.0]:
    Tstar=2*np.pi*lam*lam
    N=int(120*np.log(lam)/np.pi)+15
    xi,d=build_xi(lam,N)
    rr=real_roots(xi,d,78,94)
    if len(rr)==0:
        print(f"{lam:7.1f} {Tstar:7.1f} {OFF_IM/Tstar:10.3f} {N:4d} |  (no roots)",flush=True); continue
    near=rr[np.argmin(np.abs(rr-OFF_IM))]; gap=abs(near-OFF_IM)
    foff=abs(fc(xi,d,rho0))
    # typical |f| at depth OFF_DEPTH: median over t in [70,100] away from 85.7
    ts=np.arange(70,100,0.7)
    typ=np.median([abs(fc(xi,d,t-1j*OFF_DEPTH)) for t in ts if abs(t-OFF_IM)>2])
    print(f"{lam:7.1f} {Tstar:7.1f} {OFF_IM/Tstar:10.3f} {N:4d} | {near:11.5f} {gap:9.5f} | {foff:11.4e} {typ:10.3e} {foff/typ:8.3f}",flush=True)

print("\n READING:")
print("  gap(lambda) -> 0  => Scenario B (ξ̂ converges its root to the real projection = blind).")
print("  gap(lambda) flat/growing, or ratio |f(rho0)|/typical -> 0 (anomalous residual) => Scenario A.")
