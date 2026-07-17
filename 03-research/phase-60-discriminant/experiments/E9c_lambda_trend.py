#!/usr/bin/env python3
# ======================================================================================
# Phase 60 — E9c: el DISCRIMINANTE decisivo, libre de normalizacion. Tendencia en lambda.
#
# E9/E9b (lambda=6): ξ̂_DH pone una raiz real en 85.731 (proyeccion real del cero off-line
# 85.699), convergente en N. ¿Escenario A o B? Lo decide la TENDENCIA EN LAMBDA del hueco
#   gap(lambda) = |raiz_real_mas_cercana(ξ̂_DH) - 85.699|.
#
#   Escenario B (ciega): gap(lambda) -> 0  (ξ̂ converge su raiz a la proyeccion real, como
#       si el cero fuera on-line). El "puente convergencia=>RH" es ilusion.
#   Escenario A (ve posicion): gap(lambda) NO -> 0 / crece (Hurwitz: real-rooted no puede
#       converger a un cero complejo). -> Teorema 2 con dientes.
#
# Control: misma medida para un cero ON-line de L_DH a altura interior (debe -> 0 en ambos).
# Y off-axis residual |f_DH(85.699-0.3085i)| normalizado por |f_DH| tipico a esa profundidad.
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
print(" E9c: tendencia en lambda del hueco al cero off-line de L_DH (t=85.699)")
print("="*82)
print(f"{'lambda':>7} {'T*':>7} {'x=85.7/T*':>10} {'N':>4} | {'raiz~85.7':>11} {'gap':>9} | {'|f(rho0)|':>11} {'|f|tipico':>10} {'ratio':>8}",flush=True)

for lam in [3.5,4.0,4.5,5.0,6.0,7.0,8.0]:
    Tstar=2*np.pi*lam*lam
    N=int(120*np.log(lam)/np.pi)+15
    xi,d=build_xi(lam,N)
    rr=real_roots(xi,d,78,94)
    if len(rr)==0:
        print(f"{lam:7.1f} {Tstar:7.1f} {OFF_IM/Tstar:10.3f} {N:4d} |  (sin raices)",flush=True); continue
    near=rr[np.argmin(np.abs(rr-OFF_IM))]; gap=abs(near-OFF_IM)
    foff=abs(fc(xi,d,rho0))
    # |f| tipico a profundidad OFF_DEPTH: mediana sobre t en [70,100] lejos de 85.7
    ts=np.arange(70,100,0.7)
    typ=np.median([abs(fc(xi,d,t-1j*OFF_DEPTH)) for t in ts if abs(t-OFF_IM)>2])
    print(f"{lam:7.1f} {Tstar:7.1f} {OFF_IM/Tstar:10.3f} {N:4d} | {near:11.5f} {gap:9.5f} | {foff:11.4e} {typ:10.3e} {foff/typ:8.3f}",flush=True)

print("\n LECTURA:")
print("  gap(lambda) -> 0  => Escenario B (ξ̂ converge su raiz a la proyeccion real = ciega).")
print("  gap(lambda) plano/crece, o ratio |f(rho0)|/tipico -> 0 (residuo anomalo) => Escenario A.")
