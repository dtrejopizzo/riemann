#!/usr/bin/env python3
# IV.1 identificacion (limpio): separar sectores de PARIDAD (QW conmuta con J: j->-j) y
# verificar Sturm dentro de cada sector tras de-modular por el carrier de borde omega*.
# Si en sector PAR los modos tienen 0,2,4,.. nodos y en IMPAR 1,3,5,.. => operador de
# 2o orden tipo Sturm-Liouville/oscilacion (Gantmacher-Krein), espectro n^2 (Weyl).
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
def sgn_changes(v):
    s=[x for x in v if abs(x)>1e-9*(np.abs(v).max()+1e-300)]
    return sum(1 for i in range(1,len(s)) if s[i]*s[i-1]<0)

for lam,N in [(7.0,14),(9.0,16),(11.0,18)]:
    L=2*mp.log(mp.mpf(lam)); dim=2*N+1; idx=list(range(-N,N+1))
    M=mp.zeros(dim)
    for a in range(dim):
        for b in range(a,dim):
            v=QW_entry(idx[a],idx[b],L,mp.mpf(lam)); M[a,b]=v; M[b,a]=v
    E,V=mp.eigsy(M); order=sorted(range(dim),key=lambda j:E[j]); e0=E[order[0]]
    omega=2*np.pi*N/(2*N+1); c=(dim-1)/2.0; jj=np.arange(dim)
    print("="*70); print(f"lambda={lam} N={N}  carrier omega/pi={omega/np.pi:.3f}")
    print(" k | eps_k/eps_0 | paridad | env_nodos(demod cos) ")
    for k in range(8):
        v=np.array([float(V[i,order[k]]) for i in range(dim)])
        par = "PAR " if abs(v[::-1]@v - v@v)<1e-6*(v@v) else ("IMPAR" if abs(v[::-1]@v + v@v)<1e-6*(v@v) else "mix")
        # de-modular por coseno de borde: envelope real = v(j)/cos(omega*(j-c)) suavizado -> usar
        # proyeccion sobre cos: env(j) = v(j)*cos(omega*(j-c)) re-escala; mejor: |analitico|
        car=np.cos(omega*(jj-c))
        # envelope robusto: tomar v * carrier y sumar de a pares (downsample del producto)
        prod = v*car*2.0
        # suavizado: promedio movil de 2 para quitar la 2*omega
        env = np.convolve(prod, np.ones(3)/3, mode='same')
        print(f" {k} |  {float(E[order[k]]/e0):.3f}   |  {par}  |   {sgn_changes(env):>2}")
