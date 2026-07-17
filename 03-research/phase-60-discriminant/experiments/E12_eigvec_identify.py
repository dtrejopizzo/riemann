#!/usr/bin/env python3
# ======================================================================================
# IV.1 (cierre): IDENTIFICAR el operador limite por sus AUTOVECTORES.
# Si Â_∞ = -d²/dx² Dirichlet, los autovectores v_k de QW deben ser los modos discretos de
# Dirichlet  D_k(j) = sin((k+1)π (j+N+1)/(2N+2)),  con exactamente k cambios de signo (Sturm).
# Medimos: (a) #cambios de signo de v_k (debe ser k); (b) overlap |<v_k, D_k>| (debe ~1).
# Esto cierra IV.1: operador identificado por su sistema completo (autovalores n² + autovectores Dirichlet).
# ======================================================================================
import mpmath as mp
mp.mp.dps=30
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
def sign_changes(v):
    s=[x for x in v if abs(x)>mp.mpf('1e-12')]; c=0
    for i in range(1,len(s)):
        if s[i]*s[i-1]<0: c+=1
    return c
for lam in ['7.0']:
    L=2*mp.log(mp.mpf(lam)); N=14; dim=2*N+1; idx=list(range(-N,N+1))
    M=mp.zeros(dim)
    for a in range(dim):
        for b in range(a,dim):
            v=QW_entry(idx[a],idx[b],L,mp.mpf(lam)); M[a,b]=v; M[b,a]=v
    E,V=mp.eigsy(M)
    order=sorted(range(dim),key=lambda j:E[j])
    print(f"lambda={lam} N={N} dim={dim}")
    print(" k | eps_k/eps_0 | #sign changes | overlap con modo Dirichlet sin((k+1)pi(j+N+1)/(2N+2))")
    e0=E[order[0]]
    print(" (DE-MODULADO: envelope e_k(j)=v_k(j)*(-1)^j vs modo Dirichlet)")
    for k in range(8):
        col=order[k]; v=[V[i,col] for i in range(dim)]
        e=[v[j]*((-1)**j) for j in range(dim)]            # quitar carrier
        D=[mp.sin((k+1)*mp.pi*(j+N+1)/(2*N+2)) for j in range(dim)]
        ne=mp.sqrt(mp.fsum([x*x for x in e])); nD=mp.sqrt(mp.fsum([x*x for x in D]))
        ov=abs(mp.fsum([e[i]*D[i] for i in range(dim)]))/(ne*nD)
        print(f" {k} | {mp.nstr(E[col]/e0,6):>10} | env nodos={sign_changes(e):^3} | overlap_Dir={mp.nstr(ov,6)}")
