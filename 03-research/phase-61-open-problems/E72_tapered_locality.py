"""
P3 corregido. E71 uso el 2do momento CRUDO Lambda(n)n^{-1/2}(log n)^2 -> dominado por saltos
grandes (no-local), perfil OPUESTO al real. ERROR: omitio el taper (1-s/L) de autocorrelacion
que el engine SI tiene (q(y)=2(1-y/L)cos(..)). El taper suprime saltos grandes (s->L => 0) =
band-limiting/condicionamiento. Aqui: recomputar el 2do momento EFECTIVO con el taper y la
disponibilidad por posicion, y comparar el perfil c_2^eff(x) con el C(y) real de E70
(bump central centro/borde~1.51, aplana con lambda).
Tests:
 (1) con taper (1-s/L): ¿que fraccion de M2 dan los saltos chicos? ¿se vuelve local?
 (2) perfil c_2^eff(x): ¿bump CENTRAL (como E70) o deficit (como E71)?
 (3) centro/borde y su escala con lambda (debe -> 1, como std(C) 0.22->0.14).
 (4) variante: peso de salto efectivo = Lambda(n)n^{-1/2}(log n)^2 (1-s/L)^p, barrer p=0,1,2.
"""
import numpy as np, mpmath as mp
mp.mp.dps = 30

def primes_jumps(mx):
    sv=[True]*(mx+1); out=[]
    for i in range(2,int(mx**0.5)+1):
        if sv[i]:
            for j in range(i*i,mx+1,i): sv[j]=False
    for p in range(2,mx+1):
        if sv[p]:
            lp=mp.log(p); pm=p; me=1
            while pm<=mx:
                out.append((float(me*lp), float(lp*(mp.mpf(pm)**mp.mpf('-0.5')))))
                pm*=p; me+=1
    return out

def profile(lam, taper_p):
    L=float(2*mp.log(mp.mpf(lam))); mx=int(lam*lam)
    pj=[(s,w) for s,w in primes_jumps(mx) if s<L]   # taper anula s>=L
    # peso efectivo de cada salto: Lambda/√n * (log n)^2 * (1-s/L)^p
    eff=[(s, w*s*s*max(0.0,(1-s/L))**taper_p) for s,w in pj]
    M2=sum(e for s,e in eff)
    small=sum(e for s,e in eff if s<1.5)
    Nx=400; xs=np.linspace(0,L,Nx); c2=np.zeros(Nx)
    for s,e in eff:
        avail=0.5*((xs+s<=L).astype(float)+(xs-s>=0).astype(float))
        c2+=e*avail
    margin=0.73; bulk=(xs>margin)&(xs<L-margin)
    cb=c2[bulk]; flat=np.std(cb)/(np.mean(cb)+1e-12)
    cen=np.mean(c2[(xs>L/2-0.4)&(xs<L/2+0.4)])
    edg=np.mean(c2[(xs>margin)&(xs<margin+0.4)])
    return L,M2,small/M2 if M2>0 else 0,flat,cen/edg if edg>0 else float('nan')

print("E72: 2do momento EFECTIVO con taper (1-s/L)^p de autocorrelacion (lo que E71 omitio)")
print("real E70: C(y) bump central centro/borde~1.51, std/mean 0.22(λ7)->0.15->0.14, BUMP no deficit\n")
for p in [0,1,2,3]:
    print(f"--- taper_p={p} {'(=E71 crudo)' if p==0 else ''} ---")
    print(f"  {'lam':>4} {'L':>5} {'small%':>7} {'std/mean':>9} {'centro/borde':>12}")
    for lam in [7.0,9.0,11.0,13.0,16.0]:
        L,M2,sf,flat,cb=profile(lam,p)
        print(f"  {lam:>4} {L:>5.2f} {sf*100:>6.0f}% {flat:>9.3f} {cb:>12.3f}")
    print()
