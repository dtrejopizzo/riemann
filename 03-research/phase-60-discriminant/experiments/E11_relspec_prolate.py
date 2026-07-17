#!/usr/bin/env python3
# ======================================================================================
# Phase 60 — N5 analitico: verificacion del espectro RELATIVO de QW (lynchpin de la ruta).
# La ruta Loewner/prolata se apoya en: ε_k/ε_0 -> espectro rigido tipo (k+1)^2 (prolata).
# Medimos ε_k/ε_0 para k=0..7 a varios lambda, alta precision (mpmath), y comparamos con
# (k+1)^2 [Dirichlet/banda] y k(k+1)+const [prolata/Legendre]. Decide la forma del limite.
# ======================================================================================
import mpmath as mp
mp.mp.dps=40
GAMMA=mp.euler; LOG4PI=mp.log(4*mp.pi)
def q_func(m,n,L):
    if m==n: return lambda y: 2*(1-y/L)*mp.cos(2*mp.pi*n*y/L)
    c=1/(mp.pi*(n-m))
    return lambda y:(mp.sin(2*mp.pi*m*y/L)-mp.sin(2*mp.pi*n*y/L))*c
def QW_entry(m,n,L,lam):
    q=q_func(m,n,L); q0=q(mp.mpf(0))
    W02=mp.quad(lambda y:q(y)*(mp.e**(y/2)+mp.e**(-y/2)),[0,L])
    def wr(y):
        if y<mp.mpf('1e-12'):
            h=mp.mpf('1e-8'); return ((q(h)-q0)/h+q0/2)/2
        return (mp.e**(y/2)*q(y)-q0)/(2*mp.sinh(y))
    WR=(LOG4PI+GAMMA)*q0/2+mp.quad(wr,[0,L])+q0*mp.log(mp.tanh(L/2))/2
    arith=mp.mpf(0); mx=int(lam*lam); sv=[True]*(mx+1)
    for i in range(2,int(mx**0.5)+1):
        if sv[i]:
            for j in range(i*i,mx+1,i): sv[j]=False
    for p in range(2,mx+1):
        if sv[p]:
            lp=mp.log(p); pm=p; me=1
            while pm<=mx: arith+=lp*(mp.mpf(pm)**mp.mpf('-0.5'))*q(me*lp); pm*=p; me+=1
    return W02-WR-arith
def spec(lam,N):
    L=2*mp.log(lam); dim=2*N+1; idx=list(range(-N,N+1)); M=mp.zeros(dim)
    for a in range(dim):
        for b in range(a,dim):
            v=QW_entry(idx[a],idx[b],L,lam); M[a,b]=v; M[b,a]=v
    E,_=mp.eigsy(M); return sorted([E[i] for i in range(dim)])
print("="*70); print(" E11: espectro relativo ε_k/ε_0  (lynchpin ruta prolata)"); print("="*70,flush=True)
for lam in ['5.0','7.0','9.0']:
    e=spec(mp.mpf(lam),16); e0=e[0]
    rr=[mp.nstr(e[k]/e0,7) for k in range(8)]
    print(f"\n λ={lam}: ε_k/ε_0 =",flush=True)
    print("   k :   ε_k/ε_0      (k+1)^2    k(k+1)",flush=True)
    for k in range(8):
        print(f"   {k} : {rr[k]:>12}   {(k+1)**2:>6}     {k*(k+1):>5}",flush=True)
