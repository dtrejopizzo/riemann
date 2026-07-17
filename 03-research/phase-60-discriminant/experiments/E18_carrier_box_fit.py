#!/usr/bin/env python3
# IV.1b' (test limpio, sin Hilbert): ¿v_k = carrier_borde × modo-caja-Dirichlet_m ?
# overlap directo de v_k contra  cos(omega*(j-c))*sin(m*pi*(j+N+1)/(2N+2)),  m=1..8.
# Si v_k matchea mejor con m=k+1 y overlap alto => Â_∞ = caja libre de Dirichlet (V const),
# espectro n^2 por cuantizacion de caja, gamma=3. Cierra IV.1b'/d'.  (sin de-mod Hilbert).
import numpy as np, mpmath as mp
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
def ov(a,b):
    a=np.array(a,float); b=np.array(b,float)
    return abs(a@b)/(np.linalg.norm(a)*np.linalg.norm(b)+1e-300)

for lam,N in [(9.0,16),(11.0,18),(13.0,20)]:
    L=2*mp.log(mp.mpf(lam)); dim=2*N+1; idx=list(range(-N,N+1))
    M=mp.zeros(dim)
    for a in range(dim):
        for b in range(a,dim):
            v=QW_entry(idx[a],idx[b],L,mp.mpf(lam)); M[a,b]=v; M[b,a]=v
    E,V=mp.eigsy(M); order=sorted(range(dim),key=lambda j:E[j]); e0=E[order[0]]
    omega=2*np.pi*N/(2*N+1); c=(dim-1)/2.0; jj=np.arange(dim)
    car=np.cos(omega*(jj-c))      # carrier de borde (real)
    cars=np.sin(omega*(jj-c))
    print("="*60); print(f"lambda={lam} N={N} dim={dim}")
    print(" k | eps_k/eps_0 | best m | overlap | (m=k+1?)")
    for k in range(7):
        v=np.array([float(V[i,order[k]]) for i in range(dim)])
        best=(0,0.0)
        for m in range(1,9):
            D=np.sin(m*np.pi*(jj+1)/(dim+1))
            o=max(ov(v,car*D), ov(v,cars*D))   # permitir fase cos/sin del carrier
            if o>best[1]: best=(m,o)
        print(f" {k} |   {float(E[order[k]]/e0):.3f}   |   {best[0]}    | {best[1]:.3f}  | {'SI' if best[0]==k+1 else 'no'}")
