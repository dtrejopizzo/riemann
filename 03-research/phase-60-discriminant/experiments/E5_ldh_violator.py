#!/usr/bin/env python3
# ======================================================================================
# Phase 60 — E5: el VIOLADOR.  Operador CCM para L_DH (Davenport-Heilbronn).
#
# Tesis (mapa a RH, Eslabon 2): el operador CCM es auto-adjunto -> espectro REAL siempre.
# L_DH tiene un cero OFF-line en 1/2+0.3085+85.699i. Un autovalor real NO puede igualar
# un cero complejo => la aproximacion DEBE romperse cerca de t=85.7. ζ (cero on-line ahi)
# debe reproducirlo. El contraste = testigo de "convergencia <=> RH".
#
# Engine parametrizado en forma de Fourier (uniforme en (a,cond,coeffs,polo)):
#   L=2logλ, d_k=2πk/L, Vhat_k(t)=2 L^{-1/2} sin(tL/2)/(t-d_k)
#   Omega(t;a,cond)=Re ψ(a+it/2) - logπ + log(cond)        (= 2θ', archimedeano)
#   arch[m,n] = (1/2π) ∫ Vhat_m Vhat_n Omega dt
#   arith[m,n]= Σ_{2<=n'<=λ²} Λ_f(n') n'^{-1/2} q(U_m,U_n)(log n')
#       ζ:   a=1/4, cond=1,  Λ_f=von Mangoldt (potencias de primo), + termino de polo
#       L_DH:a=3/4, cond=5,  Λ_f=b(n) (coef de -f'/f, TODO n), sin polo (f entera)
#   QW = arch - arith (+ polo si ζ)
#   autovalores = raices de Σ_k ξ_k/(s-d_k), ξ=autovector menor autovalor de QW.
#
# GATE: ζ debe reproducir sus ceros (t~14 y t~85) en este engine antes de confiar en L_DH.
# ======================================================================================
import numpy as np
from scipy.special import digamma
from scipy.optimize import brentq

KAPPA = (np.sqrt(10-2*np.sqrt(5))-2)/(np.sqrt(5)-1)   # ~0.28408 (Davenport-Heilbronn)

def q_func(m,n,L):
    if m==n:
        return lambda y: 2*(1-y/L)*np.cos(2*np.pi*n*y/L)
    c=1.0/(np.pi*(n-m))
    return lambda y: (np.sin(2*np.pi*m*y/L)-np.sin(2*np.pi*n*y/L))*c

# ---- arithmetic coefficients ----
def vonmangoldt_upto(X):
    Lam=np.zeros(X+1); s=np.ones(X+1,bool); s[:2]=False
    for p in range(2,int(X**0.5)+1):
        if s[p]: s[p*p::p]=False
    for p in np.nonzero(s)[0]:
        pk=p; lp=np.log(p)
        while pk<=X: Lam[pk]=lp; pk*=p
    return Lam

def ldh_a(n):       # coeficientes de Dirichlet de f (periodo 5)
    r=n%5
    return [0.0,1.0,KAPPA,-KAPPA,-1.0][r]

def ldh_b_upto(X):  # b(n) = coef de -f'/f = (a*log) convol (1/f)
    a=np.array([ldh_a(n) for n in range(X+1)])
    c=np.zeros(X+1); c[1]=1.0/a[1]
    for n in range(2,X+1):
        s=0.0
        d=1
        while d<=n:
            if n%d==0 and d>1: s+=a[d]*c[n//d]
            d+=1
        c[n]=-s/a[1]
    b=np.zeros(X+1)
    for n in range(2,X+1):
        s=0.0; d=1
        while d<=n:
            if n%d==0: s+=a[d]*np.log(d)*c[n//d]
            d+=1
        b[n]=s
    return b

def build_QW(lam,N,a_arch,cond,coeffs,use_pole, tgrid):
    L=2.0*np.log(lam); idx=np.arange(-N,N+1); dim=2*N+1
    d=2*np.pi*idx/L
    # Vhat on grid: (dim, T)
    t=tgrid
    sint=np.sin(t*L/2.0)
    denom=t[None,:]-d[:,None]
    denom=np.where(np.abs(denom)<1e-12, 1e-12, denom)   # evitar 0/0 exacto en t=d_k
    Vhat=(2.0/np.sqrt(L))*sint[None,:]/denom
    Omega=np.real(digamma(a_arch+1j*t/2.0))-np.log(np.pi)+np.log(cond)
    dt=t[1]-t[0]
    arch=(1.0/(2*np.pi))*(Vhat*Omega[None,:])@Vhat.T*dt
    # arithmetic
    maxn=int(lam*lam)
    arith=np.zeros((dim,dim))
    qcache={}
    for a_i in range(dim):
        for b_i in range(a_i,dim):
            q=q_func(idx[a_i],idx[b_i],L)
            ssum=0.0
            for npow in range(2,maxn+1):
                cf=coeffs[npow]
                if cf!=0.0:
                    ssum+=cf*(npow**-0.5)*q(np.log(npow))
            arith[a_i,b_i]=ssum; arith[b_i,a_i]=ssum
    QW=arch-arith
    if use_pole:
        # termino de polo W02 = Re[ Vhat(i/2) outer Vhat(-i/2) + h.c. ]
        def vhat_c(s):
            return (2.0/np.sqrt(L))*np.sin(s*L/2.0)/(s-d)
        vp=vhat_c(0.5j); vm=vhat_c(-0.5j)
        W02=np.real(np.outer(vp,np.conj(vm))+np.outer(vm,np.conj(vp)))
        QW=QW+W02
    return (QW+QW.T)/2, idx, L

def roots_near(xi,idx,L,center,halfwidth):
    d=2*np.pi*idx/L; order=np.argsort(d); d=d[order]; xi=xi[order]
    f=lambda s: np.sum(xi/(s-d))
    out=[]
    for i in range(len(d)-1):
        a,b=d[i]+1e-7,d[i+1]-1e-7
        if a>=b or b<center-halfwidth or a>center+halfwidth: continue
        try:
            if np.isfinite(f(a)) and np.isfinite(f(b)) and f(a)*f(b)<0:
                out.append(brentq(f,a,b,xtol=1e-11))
        except Exception: pass
    return np.array(sorted(out))

def lowest_xi(QW):
    w,V=np.linalg.eigh(QW); return V[:,0], w[0]

if __name__=="__main__":
    tgrid=np.arange(-300,300,0.01)+1e-6   # offset evita coincidir con polos d_k=2πk/L
    LAM=3.7;
    print("="*78); print(f" E5: ζ (gate) vs L_DH (violador).  λ={LAM}, κ_DH={KAPPA:.6f}"); print("="*78)

    Lam_vm=vonmangoldt_upto(int(LAM*LAM))
    coeffs_zeta=Lam_vm
    coeffs_ldh =ldh_b_upto(int(LAM*LAM))
    print(f" coef ζ (Λ, n<=λ²={int(LAM*LAM)}): {np.round(coeffs_zeta[2:14],3)}")
    print(f" coef L_DH (b, n<=λ²):            {np.round(coeffs_ldh[2:14],3)}")

    for N in [10, 40]:
        print(f"\n--- N={N} ---")
        # ZETA gate
        QWz,idx,L=build_QW(LAM,N,0.25,1.0,coeffs_zeta,True,tgrid)
        xiz,_=lowest_xi(QWz)
        rz=roots_near(xiz,idx,L,14.13,3)
        rz85=roots_near(xiz,idx,L,85.7,4) if N>=36 else np.array([])
        print(f"  ζ raices ~14.13: {np.round(rz,4)}   (cero ζ=14.1347)")
        if N>=36: print(f"  ζ raices ~85.7 : {np.round(rz85,4)}   (ceros ζ~84.7355, 87.4253)")
        # L_DH
        QWd,idx,L=build_QW(LAM,N,0.75,5.0,coeffs_ldh,False,tgrid)
        xid,_=lowest_xi(QWd)
        rd=roots_near(xid,idx,L,14.13,3)
        rd85=roots_near(xid,idx,L,85.7,5) if N>=36 else np.array([])
        print(f"  L_DH raices ~14 : {np.round(rd,4)}")
        if N>=36:
            print(f"  L_DH raices ~85.7: {np.round(rd85,4)}   (cero OFF-line en 85.699+0.3085i)")
