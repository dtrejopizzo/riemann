#!/usr/bin/env python3
# ======================================================================================
# Phase 60 — CCM FIEL.  Primera implementacion correcta del spectral triple (CAND-1)
# en el programa.  Connes-Consani-Moscovici, "Zeta Spectral Triples" (arXiv:2511.22755).
#
# Construccion (Thm 1.1, Prop 3.2, eq 3.13-3.16):
#   L = 2 log λ ;  base V_k = κ(U_k), |k| <= N ;  d_k = 2π k / L
#   QW[m,n] = W02#(F) - WR#(F) - Σ_p Wp#(F),   F(u) = q(U_m,U_n)(log u)
#     q(U_m,U_n)(y), y∈[0,L]:  m=n: 2(1-y/L)cos(2πn y/L)
#                              m≠n: (sin(2πm y/L) - sin(2πn y/L)) / (π(n-m))
#     W02#(F) = ∫_0^L q(y)(e^{y/2}+e^{-y/2}) dy                                  (3.14)
#     WR#(F)  = ½(log4π+γ) q(0) + ∫_0^∞ [e^{y/2}q(y) - q(0)]/(2 sinh y) dy       (3.15)
#     Wp#(F)  = (log p) Σ_{m: p^m<=λ²} p^{-m/2} q(m log p)                       (3.16)
#   ξ = autovector del MENOR autovalor de QW (simple, par), normalizado δ_N(ξ)=1
#   Autovalores de H = raices reales de  f(s) = Σ_k ξ_k/(s - d_k) = 0   (Thm 1.1.iii;
#       derivado de ξ̂(s) = 2 L^{-1/2} sin(sL/2) Σ_k ξ_k/(s-d_k))
#
# GATE DURO (falsable): las raices positivas de f deben aproximar γ_ρ = 14.135, 21.022,...
# El paper reporta 1er cero a ~1e-55 con primos<=13 en el limite N→∞. Nosotros buscamos
# CONVERGENCIA CLARA al crecer N (mucho mejor que el 0.03 fortuito de E3), no 1e-55.
# ======================================================================================
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq

GAMMA = 0.5772156649015329
LOG4PI = np.log(4*np.pi)
ZEROS = [14.134725,21.022040,25.010858,30.424876,32.935062,37.586178,40.918719,43.327073,
         48.005151,49.773832]

def make_q(m,n,L):
    """q(U_m,U_n)(y) en y>=0, soporte [0,L]."""
    if m==n:
        return lambda y: 2*(1-y/L)*np.cos(2*np.pi*n*y/L) if 0<=y<=L else 0.0
    c=1.0/(np.pi*(n-m))
    return lambda y: (np.sin(2*np.pi*m*y/L)-np.sin(2*np.pi*n*y/L))*c if 0<=y<=L else 0.0

def QW_entry(m,n,L,lam):
    q=make_q(m,n,L); q0=q(0.0)
    # W02#
    W02,_=quad(lambda y: q(y)*(np.exp(y/2)+np.exp(-y/2)), 0, L, limit=200)
    # WR#: parte ½(log4π+γ)q0 + ∫_0^∞ [e^{y/2}q(y)-q0]/(2 sinh y) dy
    def wr_integrand(y):
        if y<1e-9:
            # limite: (q'(0)+q0/2)/2 ; aproximar numericamente
            h=1e-6; qp=(q(h)-q(0.0))/h
            return (qp+q0/2)/2.0
        sh=np.sinh(y)
        return (np.exp(y/2)*q(y)-q0)/(2*sh)
    # split [0,L] (q activo) y [L,∞) (q=0 -> -q0/(2 sinh y))
    WRa,_=quad(wr_integrand,0,L,limit=200)
    # cola: ∫_L^∞ -q0/(2 sinh y) dy = q0 * ½ ln tanh(L/2)
    WRb=q0*0.5*np.log(np.tanh(L/2))
    WR=0.5*(LOG4PI+GAMMA)*q0 + WRa + WRb
    # arithmetic Σ_p Wp#
    arith=0.0
    maxn=int(lam*lam)
    sieve=np.ones(maxn+1,bool); sieve[:2]=False
    for p in range(2,int(maxn**0.5)+1):
        if sieve[p]: sieve[p*p::p]=False
    for p in np.nonzero(sieve)[0]:
        lp=np.log(p); pm=p; mexp=1
        while pm<=maxn:
            arith+=lp*(pm**-0.5)*q(mexp*lp)
            pm*=p; mexp+=1
    return W02-WR-arith

def build_QW(lam,N):
    L=2.0*np.log(lam); dim=2*N+1; idx=np.arange(-N,N+1)
    M=np.zeros((dim,dim))
    for a in range(dim):
        for b in range(a,dim):
            v=QW_entry(idx[a],idx[b],L,lam)
            M[a,b]=v; M[b,a]=v
    return M, idx, L

def eigenvalues_from_xi(xi, idx, L, smax=55):
    d=2*np.pi*idx/L
    order=np.argsort(d); d=d[order]; xi=xi[order]
    f=lambda s: np.sum(xi/(s-d))
    roots=[]
    for i in range(len(d)-1):
        a,b=d[i]+1e-7,d[i+1]-1e-7
        if a>=b: continue
        try:
            fa,fb=f(a),f(b)
            if np.isfinite(fa) and np.isfinite(fb) and fa*fb<0:
                roots.append(brentq(f,a,b,xtol=1e-12))
        except Exception: pass
    roots=np.array(roots)
    return np.sort(roots[(roots>1)&(roots<smax)])

def run(lam,N):
    M,idx,L=build_QW(lam,N)
    w,V=np.linalg.eigh(M)
    xi=V[:,0]                      # menor autovalor
    # normalizar par: simetrizar (deberia ya ser par/impar)
    xi=(xi+xi[::-1])/2
    nrm=xi.sum()/np.sqrt(L)        # delta_N(xi)=L^{-1/2} Σ xi_k
    if abs(nrm)>1e-12: xi=xi/ (xi.sum())  # normalizacion de escala (no afecta raices)
    pos=eigenvalues_from_xi(xi,idx,L)
    return w[0],pos

if __name__=="__main__":
    print("="*78)
    print(" E4: CCM spectral triple FIEL  (primera impl. correcta del programa)")
    print("="*78)
    print(f" ceros objetivo: {ZEROS[:6]}\n")
    for lam in [3.7, 5.0, 7.0]:
        print(f"--- λ={lam} (primos p<=λ²={int(lam*lam)}) ---")
        prev=None
        for N in [10,20,40,80]:
            eps,pos=run(lam,N)
            # match primeros 4 ceros
            errs=[min(abs(pos-z)) if len(pos) else 9.9 for z in ZEROS[:4]]
            print(f"  N={N:3d}: eps_min={eps:+.4f}  #raices={len(pos):2d}  primeras={np.round(pos[:5],3)}")
            print(f"          err a ceros[1..4] = {np.round(errs,4)}")
