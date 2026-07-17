#!/usr/bin/env python3
# IV.1-res: ¿es B = D·QW·D (D=diag((-1)^j), de-modulacion real ~ carrier de borde) una
# matriz de OSCILACION (Gantmacher-Krein)? Tests necesarios de total no-negatividad (TN):
#  (a) entradas de B >= 0 ?
#  (b) off-diagonals inmediatas B[i,i+1] > 0 ? (requisito de oscilacion)
#  (c) muestreo de menores 2x2 de filas/cols consecutivas >= 0 ?
#  (d) menores principales lideres > 0 ?
# Si TN => Gantmacher-Krein => autovectores Sturmianos + espectro simple => IV.1-res "blando".
# Si signos mixtos => no es TN; la oscilacion (medida) viene de Sturm-Liouville, no de TN.
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

for lam,N in [(7.0,14),(9.0,16)]:
    L=2*mp.log(mp.mpf(lam)); dim=2*N+1; idx=list(range(-N,N+1))
    Q=np.zeros((dim,dim))
    for a in range(dim):
        for b in range(a,dim):
            v=float(QW_entry(idx[a],idx[b],L,mp.mpf(lam))); Q[a,b]=v; Q[b,a]=v
    D=np.diag([(-1)**j for j in range(dim)]).astype(float)
    B=D@Q@D
    print("="*66); print(f"lambda={lam} N={N} dim={dim}")
    # (a) fraccion de entradas >=0
    fpos=(B>=-1e-14).mean()
    print(f" (a) fraccion entradas B>=0 : {fpos:.3f}  (1.0 = TN candidato)")
    # (b) off-diagonals inmediatas
    od=[B[i,i+1] for i in range(dim-1)]
    print(f" (b) min off-diag B[i,i+1] : {min(od):.3e}  (debe >0 para oscilacion)")
    # (c) muestreo menores 2x2 consecutivos
    bad2=0; tot2=0
    for i in range(dim-1):
        for j in range(dim-1):
            m2=B[i,j]*B[i+1,j+1]-B[i,j+1]*B[i+1,j]; tot2+=1
            if m2<-1e-12: bad2+=1
    print(f" (c) menores 2x2 consecutivos <0 : {bad2}/{tot2}  ({100*bad2/tot2:.1f}% violan TN)")
    # (d) menores principales lideres
    signs=[]
    for k in range(1,min(6,dim)+1):
        signs.append(np.sign(np.linalg.det(B[:k,:k])))
    print(f" (d) signos menores lideres 1..6 : {signs}")
    # comparacion: y en la base CRUDA (sin de-modular) ?
    fpos0=(Q>=-1e-14).mean()
    print(f"     (control cruda Q: fraccion >=0 = {fpos0:.3f})")
