#!/usr/bin/env python3
# IV.1b'/c': TEST de Sturm-Liouville por RECONSTRUCCION DE POTENCIAL.
# Si Â_∞ es 2o orden  -φ'' + V(x)φ = μ φ, entonces V(x)=μ_k+φ_k''/φ_k debe ser el MISMO
# para todo k. Definimos V desde el ground nodeless φ_0 (valido en todo j) y verificamos
# que φ_1..φ_4 satisfacen -φ_k''+Vφ_k=μ_k φ_k (residual ~0). Tambien overlay directo V_k.
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

def envelope(v, omega, c):
    an = hilbert(v)
    e = np.real(an*np.exp(-1j*omega*(np.arange(len(v))-c)))
    return e

for lam,N in [(9.0,16),(11.0,18)]:
    L=2*mp.log(mp.mpf(lam)); dim=2*N+1; idx=list(range(-N,N+1))
    M=mp.zeros(dim)
    for a in range(dim):
        for b in range(a,dim):
            v=QW_entry(idx[a],idx[b],L,mp.mpf(lam)); M[a,b]=v; M[b,a]=v
    E,V=mp.eigsy(M); order=sorted(range(dim),key=lambda j:E[j]); e0=E[order[0]]
    omega=2*np.pi*N/(2*N+1); c=(dim-1)/2.0
    mu=[float(E[order[k]]/e0) for k in range(6)]
    phi=[envelope(np.array([float(V[i,order[k]]) for i in range(dim)]), omega, c) for k in range(6)]
    # normalizar signo (phi_0>0 en el centro)
    for k in range(6):
        if phi[k][int(c)]*( -1 if k%2 else 1) <0: pass
    def d2(f,j): return f[j+1]-2*f[j]+f[j-1]
    print("="*72); print(f"lambda={lam} N={N} dim={dim}  mu_k={[round(m,2) for m in mu]}")
    # V reconstruido desde phi_0 (nodeless): V(j)=mu_0 + phi0''/phi0
    th0=0.15*np.max(np.abs(phi[0]))
    Vrec={}
    for j in range(2,dim-2):
        if abs(phi[0][j])>th0:
            Vrec[j]=mu[0]+d2(phi[0],j)/phi[0][j]
    # residual de phi_k con ESE V
    print(" residual relativo de -φ_k''+Vφ_k=μ_k φ_k  (V de φ_0):")
    for k in range(1,6):
        num=0.0; den=0.0
        for j in Vrec:
            if abs(phi[k][j])>0.1*np.max(np.abs(phi[k])):
                r = -d2(phi[k],j)+Vrec[j]*phi[k][j]-mu[k]*phi[k][j]
                num+=r*r; den+=(mu[k]*phi[k][j])**2
        print(f"   k={k}: residual_rel = {np.sqrt(num/den) if den>0 else float('nan'):.4f}")
    # overlay directo: V_k(j) en 5 puntos interiores donde todos validos
    print(" overlay V_k(j) (debe coincidir entre k):")
    js=[int(c-6),int(c-3),int(c),int(c+3),int(c+6)]
    for j in js:
        row=[]
        for k in range(5):
            if abs(phi[k][j])>0.1*np.max(np.abs(phi[k])):
                row.append(mu[k]+d2(phi[k],j)/phi[k][j])
            else: row.append(float('nan'))
        vv=[x for x in row if not np.isnan(x)]
        sd = np.std(vv)/ (abs(np.mean(vv))+1e-9) if len(vv)>=2 else float('nan')
        print(f"   j={j-int(c):+d}: V_k={[round(x,2) if not np.isnan(x) else None for x in row]}  spread_rel={sd:.3f}")
