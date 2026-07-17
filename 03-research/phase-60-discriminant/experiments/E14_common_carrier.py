#!/usr/bin/env python3
# ======================================================================================
# IV.1 identificacion: de-modular TODOS los autovectores por el MISMO carrier de borde
# omega* (= carrier medido del fundamental, ~ 2*pi*N/(2N+1), borde de banda discreta).
# E12/E13 fallaron por usar (-1)^j (omega=pi) o un carrier por-modo mal extraido.
# Test: envelope_k(j)=Re(analytic(v_k)(j) e^{-i omega* (j-c)}); contar nodos (esperado k);
# overlap con modo Dirichlet sin((k+1)pi(j+N+1)/(2N+2)).  Si nodos=0,1,2,.. y overlap~1
# => Â_∞ = Laplaciano de Dirichlet con carrier de borde.  (mpmath para QW, numpy/scipy analisis)
# ======================================================================================
import numpy as np, mpmath as mp
from scipy.signal import hilbert
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
    s=[x for x in v if abs(x)>1e-9*max(abs(v).max(),1e-300)]; c=0
    for i in range(1,len(s)):
        if s[i]*s[i-1]<0: c+=1
    return c
def overlap(a,b):
    a=np.array(a,float); b=np.array(b,float)
    na=np.linalg.norm(a); nb=np.linalg.norm(b)
    return abs(a@b)/(na*nb) if na>0 and nb>0 else 0.0

for lam,N in [(7.0,14),(9.0,16),(11.0,18)]:
    L=2*mp.log(mp.mpf(lam)); dim=2*N+1; idx=list(range(-N,N+1))
    M=mp.zeros(dim)
    for a in range(dim):
        for b in range(a,dim):
            v=QW_entry(idx[a],idx[b],L,mp.mpf(lam)); M[a,b]=v; M[b,a]=v
    E,V=mp.eigsy(M); order=sorted(range(dim),key=lambda j:E[j]); e0=E[order[0]]
    vecs=[np.array([float(V[i,order[k]]) for i in range(dim)]) for k in range(8)]
    # carrier del fundamental por FFT
    F=np.abs(np.fft.rfft(vecs[0]*np.hanning(dim)))
    kpk=np.argmax(F[1:])+1; omega_star=2*np.pi*kpk/dim
    omega_edge=2*np.pi*N/(2*N+1)
    print("="*78)
    print(f"lambda={lam} N={N} dim={dim}  omega*/pi(medido)={omega_star/np.pi:.3f}  borde 2N/(2N+1)={omega_edge/np.pi:.3f}")
    print(f"eps_k/eps_0: "+"  ".join(f"{float(E[order[k]]/e0):.3f}" for k in range(7)))
    c=(dim-1)/2.0; jj=np.arange(dim)
    print(" k | env_nodos(omega*) | overlap_Dirichlet | (omega=pi nodos)")
    for k in range(7):
        v=vecs[k]
        an=hilbert(v)  # analytic signal
        env=np.real(an*np.exp(-1j*omega_star*(jj-c)))   # demod por carrier comun
        D=np.sin((k+1)*np.pi*(jj+1)/(dim+1))
        # alinear signo/maximizar overlap permitiendo reflexion par/impar de fase
        ov=max(overlap(env,D), overlap(-env,D))
        envpi=np.real(an*np.exp(-1j*np.pi*(jj-c)))
        print(f" {k} |       {sign_changes(env):>2}          |      {ov:.3f}        |    {sign_changes(envpi):>2}")
