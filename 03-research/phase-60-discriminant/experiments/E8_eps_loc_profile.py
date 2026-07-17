#!/usr/bin/env python3
# ======================================================================================
# Phase 60 — E2.nucleo: PERFIL del error de aproximacion sobre el horizonte completo.
#
# Mide |rho_n(lambda,N) - gamma_n| para TODOS los ceros gamma_n <= T* = 2*pi*lambda^2,
# como funcion de x = gamma_n / T*. Distingue:
#   ESCENARIO A: error plano super-exponencial en el interior, sin capa de borde
#                -> eps_loc ~ e^{-c lambda^2} -> Teorema 2 mata RH.
#   ESCENARIO B: capa limite cerca de x->1 (borde del horizonte) cuya magnitud
#                crece -> eps_loc gobernado por la aritmetica fina -> RH-equivalente.
#
# Construccion CCM identica a E4hp (eq 3.13-3.16 de 2511.22755), en mpmath.
# rho_n = raices de f(s)=Sum_k xi_k/(s-2*pi*k/L), xi = autovector menor autovalor de QW.
# ======================================================================================
import sys
import mpmath as mp
mp.mp.dps = 30

GAMMA = mp.euler
LOG4PI = mp.log(4*mp.pi)

def q_func(m,n,L):
    if m==n:
        return lambda y: 2*(1-y/L)*mp.cos(2*mp.pi*n*y/L)
    c=1/(mp.pi*(n-m))
    return lambda y: (mp.sin(2*mp.pi*m*y/L)-mp.sin(2*mp.pi*n*y/L))*c

def QW_entry(m,n,L,lam,primes_pp):
    q=q_func(m,n,L); q0=q(mp.mpf(0))
    W02=mp.quad(lambda y: q(y)*(mp.e**(y/2)+mp.e**(-y/2)), [0,L])
    def wr_int(y):
        if y<mp.mpf('1e-12'):
            h=mp.mpf('1e-8'); qp=(q(h)-q0)/h
            return (qp+q0/2)/2
        return (mp.e**(y/2)*q(y)-q0)/(2*mp.sinh(y))
    WRa=mp.quad(wr_int,[0,L])
    WRb=q0*mp.log(mp.tanh(L/2))/2
    WR=(LOG4PI+GAMMA)*q0/2 + WRa + WRb
    arith=mp.mpf(0)
    for p,lp in primes_pp:
        pm=p; me=1
        while pm<=primes_pp_max:
            arith+=lp*(mp.mpf(pm)**mp.mpf('-0.5'))*q(me*lp)
            pm*=p; me+=1
    return W02-WR-arith

def sieve_primes(maxn):
    s=[True]*(maxn+1)
    for i in range(2,int(maxn**0.5)+1):
        if s[i]:
            for j in range(i*i,maxn+1,i): s[j]=False
    return [(p,mp.log(p)) for p in range(2,maxn+1) if s[p]]

def lowest_xi(lam,N):
    global primes_pp_max
    L=2*mp.log(lam); dim=2*N+1; idx=list(range(-N,N+1))
    primes_pp_max=int(lam*lam)
    primes_pp=sieve_primes(primes_pp_max)
    M=mp.zeros(dim)
    for a in range(dim):
        for b in range(a,dim):
            v=QW_entry(idx[a],idx[b],L,lam,primes_pp); M[a,b]=v; M[b,a]=v
        print(f"    .. fila {a+1}/{dim}",flush=True)
    E,V=mp.eigsy(M)
    jmin=min(range(dim),key=lambda j:E[j])
    xi=[V[i,jmin] for i in range(dim)]
    return xi,idx,L,E[jmin]

def root_near(xi,idx,L,target):
    d=[2*mp.pi*k/L for k in idx]
    f=lambda s: mp.fsum([xi[i]/(s-d[i]) for i in range(len(d))])
    ds=sorted(d)
    lo=max([x for x in ds if x<target], default=target-1)
    hi=min([x for x in ds if x>target], default=target+1)
    a,b=lo+mp.mpf('1e-9'),hi-mp.mpf('1e-9')
    try:
        if f(a)*f(b)<0:
            return mp.findroot(f,(a+b)/2,solver='bisect',tol=mp.mpf('1e-25'))
    except Exception: pass
    try: return mp.findroot(f,target)
    except Exception: return None

if __name__=="__main__":
    lam=mp.mpf(sys.argv[1]) if len(sys.argv)>1 else mp.mpf('3.7')
    N=int(sys.argv[2]) if len(sys.argv)>2 else 30
    Tstar=2*mp.pi*lam*lam
    Lat_max=2*mp.pi*N/(2*mp.log(lam))   # mayor polo del modelo
    horizon=min(Tstar,Lat_max)
    print("="*72)
    print(f" E8 PERFIL eps_loc:  lambda={mp.nstr(lam,4)}  N={N}  dim={2*N+1}")
    print(f" T*=2*pi*lambda^2={mp.nstr(Tstar,6)}  polo_max={mp.nstr(Lat_max,6)}  horizonte={mp.nstr(horizon,6)}")
    print("="*72,flush=True)
    print(" construyendo QW y autovector fundamental...",flush=True)
    xi,idx,L,eps=lowest_xi(lam,N)
    print(f" eps_0(menor autovalor)={mp.nstr(eps,4)}",flush=True)
    print("\n  n |        gamma_n        |  x=g/horiz | |rho_n - gamma_n| |  rho_n",flush=True)
    print(" ---+----------------------+------------+------------------+-----------",flush=True)
    n=1; maxerr=mp.mpf(0); errs=[]
    while True:
        g=mp.im(mp.zetazero(n))
        if g>horizon*mp.mpf('0.985'): break
        r=root_near(xi,idx,L,g)
        if r is None:
            print(f" {n:3d} | {mp.nstr(g,16):>20} |  (sin raiz)",flush=True); n+=1; continue
        err=abs(r-g); errs.append((n,g,g/horizon,err))
        if err>maxerr: maxerr=err
        print(f" {n:3d} | {mp.nstr(g,16):>20} | {mp.nstr(g/horizon,4):>10} | {mp.nstr(err,6):>16} | {mp.nstr(r,14)}",flush=True)
        n+=1
    print("\n RESUMEN:",flush=True)
    print(f"   sup_n |rho_n-gamma_n| (sobre horizonte) = {mp.nstr(maxerr,6)}",flush=True)
    print(f"   lambda^(-1/2) (umbral Teorema 2)        = {mp.nstr(lam**mp.mpf('-0.5'),6)}",flush=True)
    print(f"   e^(-c lambda^2), c=11 (tasa puntual)    = {mp.nstr(mp.e**(-11*lam*lam),6)}",flush=True)
    if errs:
        interior=[e[3] for e in errs if e[2]<0.6]
        edge=[e[3] for e in errs if e[2]>=0.6]
        if interior: print(f"   max error INTERIOR (x<0.6) = {mp.nstr(max(interior),6)}",flush=True)
        if edge:     print(f"   max error BORDE    (x>=0.6)= {mp.nstr(max(edge),6)}",flush=True)
