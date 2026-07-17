#!/usr/bin/env python3
# ======================================================================================
# Phase 60 — E7: 2b en ALTA PRECISION.  ¿crece el horizonte H(λ)? (destraba el bloqueo float64)
#
# 2b: ξ̂_{λ,∞} -> Ξ cuando λ->∞.  Contenido = horizonte H(λ) de ceros resueltos -> ∞.
# Los ceros bajos ya estan a 1e-18 con primos<=13 (E4hp); el contenido de 2b esta en ceros
# ALTOS. Medimos el error de un cero FIJO ALTO (el k-esimo) al crecer λ. Si baja con λ =>
# evidencia de 2b. Tambien contamos #ceros resueltos a <1e-6 (horizonte) por λ, limpio (mpmath).
#
# Conjetura a contrastar: H(λ) tal que N(H(λ)) ~ π(λ²)  (conteo de ceros = conteo de primos).
# ======================================================================================
import mpmath as mp
mp.mp.dps=35
import importlib.util
spec=importlib.util.spec_from_file_location("e4h","/Users/dt/riemann/riemann-program/phase-60-discriminante/experiments/E4hp_convergence.py")
e4h=importlib.util.module_from_spec(spec); spec.loader.exec_module(e4h)

# ceros de zeta de referencia
ZER=[mp.im(mp.zetazero(k)) for k in range(1,40)]

def primepi(x):
    x=int(x); s=[True]*(x+1); s[0:2]=[False,False]
    for i in range(2,int(x**0.5)+1):
        if s[i]:
            for j in range(i*i,x+1,i): s[j]=False
    return sum(s)

def resolved(lam_s,N,eps=mp.mpf('1e-6'),Hmax=70):
    lam=mp.mpf(lam_s)
    xi,idx,L,e0=e4h.lowest_xi(lam,N)
    d=[2*mp.pi*k/L for k in idx]
    f=lambda s: mp.fsum([xi[i]/(s-d[i]) for i in range(len(d))])
    ds=sorted(d)
    # contar ceros consecutivos resueltos
    nres=0
    for z in ZER:
        if z>Hmax: break
        lo=max([x for x in ds if x<z],default=z-1); hi=min([x for x in ds if x>z],default=z+1)
        a,b=lo+mp.mpf('1e-9'),hi-mp.mpf('1e-9')
        try:
            r=mp.findroot(f,(a+b)/2,solver='bisect',tol=mp.mpf('1e-25')) if f(a)*f(b)<0 else mp.findroot(f,z)
            if abs(r-z)<eps: nres+=1
            else: break
        except Exception: break
    return nres,e0

if __name__=="__main__":
    print("="*72)
    print(" E7: horizonte H(λ) en alta precision (2b). eps=1e-6")
    print("="*72)
    print("  λ    primos≤λ²  π(λ²)   N    #ceros_resueltos   altura_H(λ)")
    Hmax=70
    for lam_s,N in [("2.5",30),("3.0",34),("3.7",40),("5.0",52)]:
        pp=primepi(float(lam_s)**2)
        nres,e0=resolved(lam_s,N,Hmax=Hmax)
        H = float(ZER[nres-1]) if nres>0 else 0.0
        print(f"  {lam_s:4s}    {int(float(lam_s)**2):4d}     {pp:3d}   {N:3d}      {nres:3d}            {H:7.3f}")
    print("\n contraste conjetura: H(λ) deberia crecer con λ; N(H)≈π(λ²)?")
